"""Compare chunking strategies for RAG retrieval, with confidence intervals.

    python run_experiment.py --embedder onnx:bge-small --tag bge-small
    python run_experiment.py --embedder onnx:minilm    --tag minilm
    python run_experiment.py --embedder none --tag smoke --smoke     # BM25 only, no model

Design decisions that make the numbers mean something:
  * sizes are in MODEL TOKENS (canonical tokenizer), so they are comparable with published work
  * relevance is chunking-independent: a chunk counts if it covers >= 50% of the evidence span
  * settings are chosen on a dev split and reported on held-out test questions
  * every comparison is paired, sharing one set of bootstrap resamples
  * recall is also reported at a fixed TOKEN budget, since equal-k silently favours small chunks
  * token-level recall/precision/IoU measure how much of the retrieved context is actually answer
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
import chunkers  # noqa: E402
import dataset  # noqa: E402
from models import MODELS  # noqa: E402
from retrieval import BM25Retriever, DenseRetriever, OnnxEmbedder, SentenceTransformerEmbedder  # noqa: E402
from tokenization import Tok  # noqa: E402

KS = (1, 3, 5)
MAX_RANK = 10
TOKEN_METRIC_K = 5                  # token-level precision/IoU are measured over the top 5
SIZES = (100, 200, 400)             # tokens; brackets the 200 that Chroma found strong
OVERLAP_SIZE = 200                  # overlap is swept at this chunk size
OVERLAPS = (20, 40, 80)             # tokens, i.e. 10% / 20% / 40%
SEM_PERCENTILES = (75, 85, 95)
BUDGET_TOKENS = 1000                # a realistic context budget to fill
REFERENCE = ("fixed", 200, 0)       # paired comparisons are made against this
SHORT_EVIDENCE_TOKENS = 40
N_BOOT = 5000
SPLIT_SEED = 0
DEV_FRAC = 0.3


def make_embedder(spec: str):
    if spec == "none":
        return None
    if spec.startswith("onnx:"):
        name = spec[5:]
        m = MODELS[name]
        d = ROOT / "data" / "_models" / name
        if not (d / "model.onnx").exists():
            sys.exit(f"Model files missing. Run: python scripts/fetch_models.py {name}")
        return OnnxEmbedder(name, d, m["pooling"], m["max_len"], m["query_prefix"])
    if spec.startswith("st:"):
        return SentenceTransformerEmbedder(spec[3:])
    sys.exit(f"unknown embedder {spec!r}; use none, onnx:<{'|'.join(MODELS)}> or st:<huggingface name>")


def configs(smoke: bool = False, with_embedder: bool = True):
    """(strategy, size-or-percentile, overlap) triples."""
    sizes = (OVERLAP_SIZE,) if smoke else SIZES
    for size in sizes:
        for s in ("fixed", "sentence", "recursive"):
            yield s, size, 0
    for ov in ((OVERLAPS[0],) if smoke else OVERLAPS):
        yield "fixed_overlap", OVERLAP_SIZE, ov
    if with_embedder:
        for p in ((85,) if smoke else SEM_PERCENTILES):
            yield "semantic", p, 0


def build_chunks(strategy, param, overlap, docs, embedder, tok):
    out = []
    for name, text in docs.items():
        if strategy in ("fixed", "fixed_overlap"):
            out += chunkers.fixed_size(name, text, int(param), tok, overlap=overlap)
        elif strategy == "sentence":
            out += chunkers.sentence_based(name, text, int(param), tok)
        elif strategy == "recursive":
            out += chunkers.recursive(name, text, int(param), tok)
        elif strategy == "semantic":
            out += chunkers.semantic(name, text, embedder, tok, percentile=param)
    return out


# ------------------------------------------------------------------ scoring
def overlap_chars(chunk, q):
    if chunk.doc != q["doc"]:
        return 0
    s, e = q["span"]
    return max(0, min(chunk.end, e) - max(chunk.start, s))


def relevant(chunk, q) -> bool:
    s, e = q["span"]
    return overlap_chars(chunk, q) >= 0.5 * (e - s)


def intact(chunk, q) -> bool:
    s, e = q["span"]
    return overlap_chars(chunk, q) >= (e - s)


def first_rank(retrieved, chunks, q):
    for r, idx in enumerate(retrieved, 1):
        if relevant(chunks[idx], q):
            return r
    return None


def budget_hit(retrieved, chunks, q, ntok, budget) -> tuple[bool, int]:
    """Fill a fixed token budget from the ranking and ask whether the answer made it in."""
    used, hit = 0, False
    for n, idx in enumerate(retrieved):
        t = ntok[idx]
        if n > 0 and used + t > budget:
            break
        used += t
        hit = hit or relevant(chunks[idx], q)
    return hit, used


def token_scores(retrieved, chunks, q, ntok, tokrange, k):
    """How much of the retrieved context is actually the answer.

    Two denominators are reported, because the choice changes the verdict on overlap:
      * "dup"   counts every retrieved token, so text appearing in two overlapping chunks is
                counted twice. This is what Chroma's published implementation does, and it
                mechanically penalises overlap.
      * "union" counts each distinct piece of source text once, so redundancy is free.
    recall is identical under both (an evidence token counts once either way).
    """
    e_lo, e_hi = q["tok_span"]
    need = e_hi - e_lo
    if need <= 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    covered, seen, total_dup = set(), set(), 0
    for idx in retrieved[:k]:
        total_dup += int(ntok[idx])
        lo, hi = tokrange[idx]
        d = chunks[idx].doc
        seen.update((d, t) for t in range(lo, hi))
        if d == q["doc"]:
            covered |= set(range(max(lo, e_lo), min(hi, e_hi)))
    c, total_uni = len(covered), len(seen)
    p_dup = c / total_dup if total_dup else 0.0
    i_dup = c / (total_dup + need - c) if (total_dup + need - c) else 0.0
    p_uni = c / total_uni if total_uni else 0.0
    i_uni = c / (total_uni + need - c) if (total_uni + need - c) else 0.0
    return c / need, p_dup, i_dup, p_uni, i_uni


def boot_means(values: np.ndarray, idx: np.ndarray) -> np.ndarray:
    return values[idx].mean(axis=1)


def ci(arr):
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def snippet(text, n=240):
    t = " ".join(text.split())
    return t if len(t) <= n else t[: n - 1] + "…"


def label(strategy, param, overlap):
    if strategy == "semantic":
        return f"semantic p{int(param)}"
    return f"{strategy} {int(param)}" + (f"+{int(overlap)}" if overlap else "")


# --------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--embedder", default="onnx:bge-small")
    ap.add_argument("--tag", default=None)
    ap.add_argument("--smoke", action="store_true", help="small config subset, for CI")
    args = ap.parse_args()
    tag = args.tag or args.embedder.split(":", 1)[-1].replace("/", "_")
    out_dir = ROOT / "results" / tag
    out_dir.mkdir(parents=True, exist_ok=True)

    tok = Tok()
    docs = dataset.load_docs()
    questions = dataset.assign_splits(dataset.load_questions(docs), SPLIT_SEED, DEV_FRAC)
    for q in questions:
        q["tok_span"] = tok.token_index_range(docs[q["doc"]], *q["span"])
        q["evidence_tokens"] = q["tok_span"][1] - q["tok_span"][0]
    n = len(questions)
    short = np.array([q["evidence_tokens"] <= SHORT_EVIDENCE_TOKENS for q in questions])
    is_dev = np.array([q["split"] == "dev" for q in questions])
    is_test = ~is_dev
    test_pos = np.flatnonzero(is_test)

    embedder = make_embedder(args.embedder)
    kinds = ("dense", "bm25") if embedder is not None else ("bm25",)
    ename = embedder.name if embedder else "none (BM25 only)"
    print(f"embedder={ename} docs={len(docs)} questions={n} "
          f"(short evidence <= {SHORT_EVIDENCE_TOKENS} tok: {short.sum()}, long: {(~short).sum()})")
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(test_pos), size=(N_BOOT, len(test_pos)))

    summary, per_q, store, taxonomy, failures, fail_store = [], [], {}, [], [], {}
    t_start = time.time()
    for strategy, param, ov in configs(args.smoke, embedder is not None):
        t0 = time.time()
        chunks = build_chunks(strategy, param, ov, docs, embedder, tok)
        t_chunk = time.time() - t0
        ntok = np.array([tok.count(c.text) for c in chunks])
        tokrange = [tok.token_index_range(docs[c.doc], c.start, c.end) for c in chunks]
        over = int((ntok > (embedder.max_len if isinstance(embedder, OnnxEmbedder) else 512)).sum())
        embed_tokens = int(ntok.sum())
        if strategy == "semantic":
            embed_tokens += sum(tok.span_count(t, s, e) for t in docs.values()
                                for s, e in chunkers.sentence_spans(t))
        integrity = np.array([any(intact(c, q) for c in chunks) for q in questions], dtype=float)
        answerable = np.array([any(relevant(c, q) for c in chunks) for q in questions], dtype=float)

        for kind in kinds:
            retr = DenseRetriever(embedder, chunks) if kind == "dense" else BM25Retriever(chunks)
            ranks, bhits, bused, tops = [], [], [], []
            trec, tprec, tiou, tprec_u, tiou_u = [], [], [], [], []
            for q in questions:
                got = retr.search(q["question"], MAX_RANK)
                r = first_rank(got, chunks, q)
                h, used = budget_hit(got, chunks, q, ntok, BUDGET_TOKENS)
                a, b, c3, b_u, c_u = token_scores(got, chunks, q, ntok, tokrange, TOKEN_METRIC_K)
                ranks.append(r); bhits.append(float(h)); bused.append(used); tops.append(chunks[got[0]])
                trec.append(a); tprec.append(b); tiou.append(c3)
                tprec_u.append(b_u); tiou_u.append(c_u)
                per_q.append({"strategy": strategy, "param": param, "overlap": ov, "retriever": kind,
                              "qid": q["id"], "split": q["split"], "rank_of_first_relevant": r or "",
                              "budget_hit": int(h), "top1_doc": chunks[got[0]].doc})
            metric = {f"recall@{k}": np.array([1.0 if (r and r <= k) else 0.0 for r in ranks]) for k in KS}
            metric["mrr@10"] = np.array([1.0 / r if r else 0.0 for r in ranks])
            metric[f"recall@{BUDGET_TOKENS}tok"] = np.array(bhits)
            metric[f"token_recall@{TOKEN_METRIC_K}"] = np.array(trec)
            metric[f"token_precision@{TOKEN_METRIC_K}"] = np.array(tprec)
            metric[f"token_iou@{TOKEN_METRIC_K}"] = np.array(tiou)
            metric[f"token_precision_union@{TOKEN_METRIC_K}"] = np.array(tprec_u)
            metric[f"token_iou_union@{TOKEN_METRIC_K}"] = np.array(tiou_u)
            row = {"strategy": strategy, "param": param, "overlap": ov, "retriever": kind,
                   "label": label(strategy, param, ov), "headline": False,
                   "n_chunks": len(chunks), "mean_tokens": round(float(ntok.mean()), 1),
                   "median_tokens": int(np.median(ntok)), "chunks_over_model_limit": over,
                   "index_embed_tokens": embed_tokens, "chunking_seconds": round(t_chunk, 2),
                   "evidence_intact": round(float(integrity[test_pos].mean()), 3),
                   "answerable": round(float(answerable[test_pos].mean()), 3),
                   "mean_tokens_in_budget": round(float(np.mean(np.asarray(bused)[test_pos])), 1)}
            for name, vals in metric.items():
                tv = vals[test_pos]
                lo, hi = ci(boot_means(tv, idx))
                nd = 4 if name.startswith("token_") else 3
                row[name] = round(float(tv.mean()), nd)
                row[name + "_lo"], row[name + "_hi"] = round(lo, nd), round(hi, nd)
                row[name + "_dev"] = round(float(vals[is_dev].mean()), nd) if is_dev.any() else ""
                for t_, m_ in (("short", short & is_test), ("long", (~short) & is_test)):
                    row[name + "_" + t_] = round(float(vals[m_].mean()), nd) if m_.any() else ""
            summary.append(row)
            store[(strategy, param, ov, kind)] = metric
            if kind == kinds[0]:
                fail_store[(strategy, param, ov)] = [
                    (q, r, top, ("evidence split across chunks" if not answerable[qi]
                                 else "right document, wrong passage" if top.doc == q["doc"] else "wrong document"))
                    for qi, (q, r, top) in enumerate(zip(questions, ranks, tops))
                    if is_test[qi] and (r is None or r > 5)]
            print(f"{label(strategy, param, ov):18s}{kind:5s} chunks={len(chunks):5d} tok={ntok.mean():6.1f} "
                  f"intact={row['evidence_intact']:.2f} R@3={row['recall@3']:.2f} MRR={row['mrr@10']:.3f} "
                  f"R@{BUDGET_TOKENS}t={row[f'recall@{BUDGET_TOKENS}tok']:.2f} "
                  f"tPrec={row[f'token_precision@{TOKEN_METRIC_K}']:.4f} "
                  f"tIoU={row[f'token_iou@{TOKEN_METRIC_K}']:.4f}" + (f" trunc={over}" if over else ""))

    # ---- choose one configuration per strategy on the DEV questions only
    primary = kinds[0]
    best: dict[str, tuple] = {}
    for (strategy, param, ov, k), met in store.items():
        if k != primary:
            continue
        score = float(met["mrr@10"][is_dev].mean()) if is_dev.any() else float(met["mrr@10"].mean())
        if strategy not in best or score > best[strategy][1]:
            best[strategy] = ((param, ov), score)
    selected = {s: key for s, (key, _) in best.items()}
    for row in summary:
        row["headline"] = selected.get(row["strategy"]) == (row["param"], row["overlap"])
    ref_key = ("fixed",) + selected["fixed"] if "fixed" in selected else REFERENCE
    print("\nselected on dev: " + ", ".join(f"{s}={label(s, *selected[s])}" for s in sorted(selected))
          + f"  | reference = {label(*ref_key)}")

    for strategy, (param, ov) in selected.items():
        cats = {"evidence split across chunks": 0, "right document, wrong passage": 0, "wrong document": 0}
        for q, r, top, why in fail_store.get((strategy, param, ov), []):
            cats[why] += 1
            failures.append((label(strategy, param, ov), q, r, top, why))
        taxonomy.append({"strategy": strategy, "label": label(strategy, param, ov),
                         "misses_top5": sum(cats.values()), **cats})

    # ---- paired comparisons, on the same test questions and the same resamples
    PAIR_METRICS = ("recall@3", "mrr@10", f"recall@{BUDGET_TOKENS}tok",
                    f"token_precision@{TOKEN_METRIC_K}", f"token_iou@{TOKEN_METRIC_K}",
                    f"token_precision_union@{TOKEN_METRIC_K}")
    paired = []
    for kind in kinds:
        ref = store[ref_key + (kind,)]
        for (strategy, param, ov, k), met in store.items():
            if k != kind or (strategy, param, ov) == ref_key:
                continue
            for mname in PAIR_METRICS:
                d = (met[mname] - ref[mname])[test_pos]
                boots = boot_means(d, idx)
                lo, hi = ci(boots)
                paired.append({"retriever": kind, "strategy": strategy, "param": param, "overlap": ov,
                               "label": label(strategy, param, ov), "metric": mname,
                               "diff_vs_reference": round(float(d.mean()), 4),
                               "diff_lo": round(lo, 4), "diff_hi": round(hi, 4),
                               "headline": selected.get(strategy) == (param, ov),
                               "share_of_resamples_above_zero": round(float((boots > 0).mean()), 3)})

    def write_csv(name, rows):
        if not rows:
            return
        with open(out_dir / name, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    write_csv("summary.csv", summary)
    write_csv("paired_vs_reference.csv", paired)
    write_csv("per_question.csv", per_q)
    write_csv("failure_taxonomy.csv", taxonomy)
    if len(kinds) == 2:
        dvb = []
        for strategy, (param, ov) in selected.items():
            for mname in PAIR_METRICS:
                d = (store[(strategy, param, ov, "dense")][mname] - store[(strategy, param, ov, "bm25")][mname])[test_pos]
                lo, hi = ci(boot_means(d, idx))
                dvb.append({"strategy": strategy, "label": label(strategy, param, ov), "metric": mname,
                            "dense_minus_bm25": round(float(d.mean()), 4),
                            "diff_lo": round(lo, 4), "diff_hi": round(hi, 4)})
        write_csv("paired_dense_vs_bm25.csv", dvb)

    info = {"embedder": embedder.name if embedder else "none", "spec": args.embedder,
            "tokenizer": tok.name, "size_unit": "tokens",
            "selected_on_dev": {k: {"size": v[0], "overlap": v[1]} for k, v in selected.items()},
            "reference": label(*ref_key), "split_seed": SPLIT_SEED, "dev_frac": DEV_FRAC,
            "n_docs": len(docs), "n_questions": n, "n_dev": int(is_dev.sum()), "n_test": int(is_test.sum()),
            "n_short_evidence": int(short.sum()), "n_long_evidence": int((~short).sum()),
            "short_evidence_tokens": SHORT_EVIDENCE_TOKENS, "budget_tokens": BUDGET_TOKENS,
            "token_metric_k": TOKEN_METRIC_K, "sizes_tokens": list(SIZES), "overlaps_tokens": list(OVERLAPS),
            "bootstrap_resamples": N_BOOT, "seconds": round(time.time() - t_start, 1),
            "platform": {"python": platform.python_version(), "os": platform.platform(),
                         "cpu_count": os.cpu_count(), "numpy": np.__version__}}
    if isinstance(embedder, OnnxEmbedder):
        info.update({"pooling": embedder.pooling, "max_len": embedder.max_len})
    (out_dir / "run_info.json").write_text(json.dumps(info, indent=2))

    lines = [f"# Failure cases: {info['embedder']}, {kinds[0]} retrieval, selected configurations\n",
             "A question counts as a miss when its first relevant chunk is not in the top 5.\n"]
    for lab, q, r, top, why in failures:
        lines += [f"## {lab} - {q['id']}: {why}\n", f"- **Question:** {q['question']}",
                  f"- **Evidence ({q['doc']}):** {snippet(q['evidence'], 320)}",
                  f"- **First relevant rank:** {r if r else '>10'}",
                  f"- **Top-1 retrieved ({top.doc}):** {snippet(top.text)}\n"]
    (out_dir / "failures.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nwrote results to {out_dir}  ({info['seconds']} s)")


if __name__ == "__main__":
    main()
