"""Compare chunking strategies for RAG retrieval.

    python scripts/fetch_corpus.py
    python scripts/fetch_models.py
    python run_experiment.py --embedder onnx:bge-small
    python run_experiment.py --embedder onnx:minilm
    python run_experiment.py --embedder st:BAAI/bge-small-en-v1.5      # same model via Hugging Face

Relevance rule (independent of how the text was chunked): a retrieved chunk is relevant when
it lies in the right document and overlaps the question's evidence passage by at least 50% of
the passage's length.

Outputs go to results/<tag>/ (see README for the file list).
"""
from __future__ import annotations

import argparse
import csv
import os
import platform
import json
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

KS = (1, 3, 5)
MAX_RANK = 10
SIZES = (75, 150, 300)             # words
SEM_PERCENTILES = (75, 85, 95)
HEADLINE = {"fixed": 150, "sentence": 150, "recursive": 150, "semantic": 85, "fixed_overlap": 150}
MAIN_SEM = 85
REFERENCE = ("fixed", 150)          # paired comparisons are made against this
BUDGET_WORDS = 450                  # context budget for the budget-matched recall
SHORT_EVIDENCE_WORDS = 25
N_BOOT = 5000
SPLIT_SEED = 0
DEV_FRAC = 0.3                      # dev questions pick the settings; test questions are reported


# -------------------------------------------------------------------- setup
def make_embedder(spec: str):
    if spec == "none":                       # BM25 only; used by CI to test the pipeline offline
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
    """Full grid, or a fast subset for CI. Semantic chunking needs an embedder."""
    sizes = (150,) if smoke else SIZES
    for size in sizes:
        for s in ("fixed", "sentence", "recursive"):
            yield s, size, 0
    yield "fixed_overlap", 150, 30
    if with_embedder:
        for p in ((MAIN_SEM,) if smoke else SEM_PERCENTILES):
            yield "semantic", p, 0


def build_chunks(strategy, param, overlap, docs, embedder):
    out = []
    for name, text in docs.items():
        if strategy in ("fixed", "fixed_overlap"):
            out += chunkers.fixed_size(name, text, int(param), overlap=overlap)
        elif strategy == "sentence":
            out += chunkers.sentence_based(name, text, int(param))
        elif strategy == "recursive":
            out += chunkers.recursive(name, text, int(param))
        elif strategy == "semantic":
            out += chunkers.semantic(name, text, embedder, percentile=param)
    return out


def is_headline(strategy, param):
    return HEADLINE.get(strategy) == param


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


def budget_hit(retrieved, chunks, q, budget=BUDGET_WORDS) -> tuple[bool, int]:
    used, hit = 0, False
    for n, idx in enumerate(retrieved):
        w = chunkers.n_words(chunks[idx].text)
        if n > 0 and used + w > budget:
            break
        used += w
        hit = hit or relevant(chunks[idx], q)
    return hit, used


def boot_means(values: np.ndarray, idx: np.ndarray) -> np.ndarray:
    return values[idx].mean(axis=1)


def ci(arr):
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def snippet(text, n=240):
    t = " ".join(text.split())
    return t if len(t) <= n else t[: n - 1] + "…"


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

    docs = dataset.load_docs()
    questions = dataset.assign_splits(dataset.load_questions(docs), SPLIT_SEED, DEV_FRAC)
    n = len(questions)
    short = np.array([q["evidence_words"] <= SHORT_EVIDENCE_WORDS for q in questions])
    is_dev = np.array([q["split"] == "dev" for q in questions])
    is_test = ~is_dev
    test_pos = np.flatnonzero(is_test)
    embedder = make_embedder(args.embedder)
    kinds = ("dense", "bm25") if embedder is not None else ("bm25",)
    print(f"embedder={embedder.name if embedder else 'none (BM25 only)'} docs={len(docs)} questions={n} (short evidence: {short.sum()}, long: {(~short).sum()})")
    rng = np.random.default_rng(0)
    # one shared set of resamples over the TEST questions, so every comparison is paired
    idx = rng.integers(0, len(test_pos), size=(N_BOOT, len(test_pos)))

    summary, per_q, store, taxonomy, failures, fail_store = [], [], {}, [], [], {}
    t_start = time.time()
    for strategy, param, overlap in configs(args.smoke, embedder is not None):
        t0 = time.time()
        chunks = build_chunks(strategy, param, overlap, docs, embedder)
        t_chunk = time.time() - t0
        words = [chunkers.n_words(c.text) for c in chunks]
        over = embedder.n_over_limit([c.text for c in chunks]) if hasattr(embedder, "n_over_limit") else 0
        embed_words = sum(words)
        if strategy == "semantic":                       # extra pass: every sentence is embedded to find breakpoints
            embed_words += sum(chunkers.n_words(t[s:e]) for t in docs.values() for s, e in chunkers.sentence_spans(t))
        integrity = np.array([any(intact(c, q) for c in chunks) for q in questions], dtype=float)
        answerable = np.array([any(relevant(c, q) for c in chunks) for q in questions], dtype=float)
        integrity_test = float(integrity[test_pos].mean())
        answerable_test = float(answerable[test_pos].mean())

        for kind in kinds:
            retr = DenseRetriever(embedder, chunks) if kind == "dense" else BM25Retriever(chunks)
            ranks, bhits, bused, tops = [], [], [], []
            for q in questions:
                got = retr.search(q["question"], MAX_RANK)
                r = first_rank(got, chunks, q)
                h, used = budget_hit(got, chunks, q)
                ranks.append(r)
                bhits.append(float(h))
                bused.append(used)
                tops.append(chunks[got[0]])
                per_q.append({"strategy": strategy, "param": param, "overlap": overlap, "retriever": kind, "qid": q["id"],
                              "rank_of_first_relevant": r or "", "budget_hit": int(h), "top1_doc": chunks[got[0]].doc,
                              "split": q["split"]})
            metric = {f"recall@{k}": np.array([1.0 if (r and r <= k) else 0.0 for r in ranks]) for k in KS}
            metric["mrr@10"] = np.array([1.0 / r if r else 0.0 for r in ranks])
            metric[f"recall@{BUDGET_WORDS}w"] = np.array(bhits)
            row = {"strategy": strategy, "param": param, "overlap": overlap, "retriever": kind,
                   "headline": is_headline(strategy, param), "n_chunks": len(chunks),
                   "mean_words": round(float(np.mean(words)), 1), "chunks_over_model_limit": over,
                   "index_embed_words": embed_words, "chunking_seconds": round(t_chunk, 2),
                   "evidence_intact": round(integrity_test, 3), "answerable": round(answerable_test, 3),
                   "evidence_intact_all": round(float(integrity.mean()), 3),
                   "mean_words_in_budget": round(float(np.mean(np.asarray(bused)[test_pos])), 1)}
            for name, vals in metric.items():
                tv = vals[test_pos]                      # reported numbers come from test only
                lo, hi = ci(boot_means(tv, idx))
                row[name] = round(float(tv.mean()), 3)
                row[name + "_lo"], row[name + "_hi"] = round(lo, 3), round(hi, 3)
                row[name + "_dev"] = round(float(vals[is_dev].mean()), 3) if is_dev.any() else ""
                for tag, mask in (("short", short & is_test), ("long", (~short) & is_test)):
                    row[name + "_" + tag] = round(float(vals[mask].mean()), 3) if mask.any() else ""
            summary.append(row)
            store[(strategy, param, kind)] = metric
            if kind == kinds[0]:
                fail_store[(strategy, param)] = [
                    (q, r, top, ("evidence split across chunks" if not answerable[qi]
                                 else "right document, wrong passage" if top.doc == q["doc"] else "wrong document"))
                    for qi, (q, r, top) in enumerate(zip(questions, ranks, tops))
                    if is_test[qi] and (r is None or r > 5)]
            print(f"{strategy:13s}{param:>4} {kind:5s} chunks={len(chunks):4d} words={np.mean(words):6.1f} intact={integrity.mean():.2f} "
                  f"R@1={row['recall@1']:.2f} R@3={row['recall@3']:.2f} R@5={row['recall@5']:.2f} "
                  f"MRR={row['mrr@10']:.3f} R@{BUDGET_WORDS}w={row[f'recall@{BUDGET_WORDS}w']:.2f}" + (f" over_limit={over}" if over else ""))

    # ---- pick ONE configuration per strategy using the dev questions only
    primary = kinds[0]
    best: dict[str, tuple] = {}
    for (strategy, param, k), met in store.items():
        if k != primary:
            continue
        score = float(met["mrr@10"][is_dev].mean()) if is_dev.any() else float(met["mrr@10"].mean())
        if strategy not in best or score > best[strategy][1]:
            best[strategy] = (param, score)
    selected = {s: p for s, (p, _) in best.items()}
    for row in summary:
        row["headline"] = selected.get(row["strategy"]) == row["param"]
    ref_key = ("fixed", selected["fixed"]) if "fixed" in selected else REFERENCE
    print("\nselected on dev: " + ", ".join(f"{s}={selected[s]:g}" for s in sorted(selected))
          + f"  | reference = {ref_key[0]} {ref_key[1]:g}")

    for strategy, param in selected.items():
        cats = {"evidence split across chunks": 0, "right document, wrong passage": 0, "wrong document": 0}
        for q, r, top, why in fail_store.get((strategy, param), []):
            cats[why] += 1
            failures.append((strategy, q, r, top, why))
        taxonomy.append({"strategy": strategy, "param": param, "misses_top5": sum(cats.values()), **cats})

    # ---- paired comparisons against that reference, on the same test questions
    paired = []
    for kind in kinds:
        ref = store[(ref_key[0], ref_key[1], kind)]
        for (strategy, param, k), met in store.items():
            if k != kind or (strategy, param) == ref_key:
                continue
            for mname in ("recall@3", "mrr@10", f"recall@{BUDGET_WORDS}w"):
                d = (met[mname] - ref[mname])[test_pos]
                boots = boot_means(d, idx)
                lo, hi = ci(boots)
                paired.append({"retriever": kind, "strategy": strategy, "param": param, "metric": mname,
                               "diff_vs_reference": round(float(d.mean()), 3), "diff_lo": round(lo, 3), "diff_hi": round(hi, 3),
                               "headline": selected.get(strategy) == param,
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
    if len(kinds) == 2:
        dvb = []
        for strategy, param in selected.items():
            for mname in ("recall@3", "mrr@10", f"recall@{BUDGET_WORDS}w"):
                d = (store[(strategy, param, "dense")][mname] - store[(strategy, param, "bm25")][mname])[test_pos]
                lo, hi = ci(boot_means(d, idx))
                dvb.append({"strategy": strategy, "param": param, "metric": mname,
                            "dense_minus_bm25": round(float(d.mean()), 3),
                            "diff_lo": round(lo, 3), "diff_hi": round(hi, 3)})
        write_csv("paired_dense_vs_bm25.csv", dvb)
    write_csv("per_question.csv", per_q)
    write_csv("failure_taxonomy.csv", taxonomy)
    info = {"embedder": embedder.name if embedder else "none", "spec": args.embedder,
            "selected_on_dev": {k: (int(v) if float(v).is_integer() else v) for k, v in selected.items()},
            "reference": f"{ref_key[0]}-{ref_key[1]:g}", "split_seed": SPLIT_SEED, "dev_frac": DEV_FRAC,
            "n_dev": int(is_dev.sum()), "n_test": int(is_test.sum()),
            "platform": {"python": platform.python_version(), "os": platform.platform(),
                         "cpu_count": os.cpu_count(), "numpy": np.__version__}, "n_docs": len(docs), "n_questions": n,
            "n_short_evidence": int(short.sum()), "n_long_evidence": int((~short).sum()),
            "short_evidence_words": SHORT_EVIDENCE_WORDS, "budget_words": BUDGET_WORDS,
            "bootstrap_resamples": N_BOOT, "seconds": round(time.time() - t_start, 1)}
    if isinstance(embedder, OnnxEmbedder):
        info.update({"pooling": embedder.pooling, "max_len": embedder.max_len})
    (out_dir / "run_info.json").write_text(json.dumps(info, indent=2))

    lines = [f"# Failure cases: {info['embedder']}, {kinds[0]} retrieval, headline configurations\n",
             "A question counts as a miss when its first relevant chunk is not in the top 5.\n"]
    for strategy, q, r, top, why in failures:
        lines += [f"## {strategy} - {q['id']}: {why}\n", f"- **Question:** {q['question']}",
                  f"- **Evidence ({q['doc']}):** {snippet(q['evidence'], 320)}",
                  f"- **First relevant rank:** {r if r else '>10'}",
                  f"- **Top-1 retrieved ({top.doc}):** {snippet(top.text)}\n"]
    (out_dir / "failures.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nwrote results to {out_dir}  ({info['seconds']} s)")


if __name__ == "__main__":
    main()
