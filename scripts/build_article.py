"""Assemble the publishable article from the prose template + the real results.

    python scripts/make_report.py   --tag bge-small
    python scripts/build_article.py --tag bge-small

Writes article/FINAL.md. Every {placeholder} in article/template.md is filled from the
result CSVs. If a placeholder has no matching fact the build FAILS rather than shipping
an article with a hand-typed or stale number in it.
"""
from __future__ import annotations

import argparse
import json
import re
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from make_report import LABEL, ORDER, head, load, primary_of  # noqa: E402


def pct(x):
    return f"{100 * x:.0f}%"


def ci(r, m):
    return f"{r[m]:.2f} (95% CI {r[m + '_lo']:.2f}–{r[m + '_hi']:.2f})"


def facts(tag):
    d, rows, paired, tax, info = load(tag)
    prim = primary_of(rows)
    H = head(rows, prim)
    bm = head(rows, "bm25")
    budget = f"recall@{int(info['budget_words'])}w"
    f = {"tag": tag, "embedder": info["embedder"], "n_docs": int(info["n_docs"]),
         "n_questions": int(info["n_questions"]), "n_dev": int(info["n_dev"]), "n_test": int(info["n_test"]),
         "n_boot": f"{int(info['bootstrap_resamples']):,}", "reference": info["reference"],
         "budget_words": int(info["budget_words"]), "retriever": prim,
         "python": info["platform"]["python"], "os": info["platform"]["os"],
         "cpu_count": info["platform"]["cpu_count"], "runtime_min": f"{info['seconds'] / 60:.0f}",
         "selected": ", ".join(f"`{k}` at {v}" for k, v in sorted(info["selected_on_dev"].items()))}

    ranked = sorted(H.values(), key=lambda r: -r["mrr@10"])
    best, worst = ranked[0], ranked[-1]
    f["best_name"] = LABEL[best["strategy"]]
    f["best_mrr"] = ci(best, "mrr@10")
    f["best_r3"] = ci(best, "recall@3")
    f["worst_name"] = LABEL[worst["strategy"]]
    f["worst_mrr"] = ci(worst, "mrr@10")
    f["spread"] = f"{best['mrr@10'] - worst['mrr@10']:.2f}"

    ref = H.get("fixed") or ranked[-1]
    f["ref_mrr"] = ci(ref, "mrr@10")
    f["ref_name"] = LABEL[ref["strategy"]]
    if "fixed" in bm:
        f["bm25_ref_mrr"] = ci(bm["fixed"], "mrr@10")
        f["dense_minus_bm25"] = f"{ref['mrr@10'] - bm['fixed']['mrr@10']:+.2f}"
    else:
        f["bm25_ref_mrr"] = f["dense_minus_bm25"] = "n/a"

    pm = [r for r in paired if r["retriever"] == prim and r["headline"] and r["metric"] == "mrr@10"]
    cross = [r for r in pm if r["diff_lo"] <= 0 <= r["diff_hi"]]
    f["n_compared"] = len(pm)
    f["n_crossing_zero"] = len(cross)
    f["n_separated"] = len(pm) - len(cross)
    f["crossing_names"] = ", ".join(LABEL.get(r["strategy"], r["strategy"]) for r in cross) or "none"
    sep = [r for r in pm if not (r["diff_lo"] <= 0 <= r["diff_hi"])]
    f["separated_names"] = ", ".join(LABEL.get(r["strategy"], r["strategy"]) for r in sep) or "none"
    f["widest_ci"] = f"{max((r['diff_hi'] - r['diff_lo']) for r in pm):.2f}" if pm else "n/a"

    # separations across every metric, not just MRR, otherwise the article understates the result
    allp = [r for r in paired if r["retriever"] == prim and r["headline"]]
    sep_all = [r for r in allp if not (r["diff_lo"] <= 0 <= r["diff_hi"])]
    f["n_all_comparisons"] = len(allp)
    f["n_all_separated"] = len(sep_all)
    f["sep_detail"] = "; ".join(
        f"**{LABEL.get(r['strategy'], r['strategy'])}** on {r['metric']} "
        f"({r['diff_vs_reference']:+.3f}, CI [{r['diff_lo']:+.3f}, {r['diff_hi']:+.3f}])"
        for r in sorted(sep_all, key=lambda r: (ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9, r["metric"]))
    ) or "no comparison separated on any metric"
    f["sep_metrics"] = ", ".join(sorted({r["metric"] for r in sep_all})) or "none"

    # mechanism: evidence survival at the smallest size tried
    small = {}
    for r in rows:
        if r["retriever"] != prim:
            continue
        small.setdefault(r["strategy"], r)
        if r["param"] < small[r["strategy"]]["param"]:
            small[r["strategy"]] = r
    if "fixed" in small and "sentence" in small:
        f["intact_fixed_small"] = pct(small["fixed"]["evidence_intact"])
        f["intact_sentence_small"] = pct(small["sentence"]["evidence_intact"])
        f["small_size"] = int(small["fixed"]["param"])
    f["intact_table"] = ", ".join(f"{LABEL[s]} {pct(H[s]['evidence_intact'])}" for s in ORDER if s in H)

    if "fixed_overlap" in H and "fixed" in H:
        f["overlap_delta"] = f"{H['fixed_overlap']['mrr@10'] - H['fixed']['mrr@10']:+.3f}"
        f["overlap_intact"] = pct(H["fixed_overlap"]["evidence_intact"])
        ov = next((r for r in pm if r["strategy"] == "fixed_overlap"), None)
        f["overlap_ci"] = f"[{ov['diff_lo']:+.3f}, {ov['diff_hi']:+.3f}]" if ov else "n/a"
    if "semantic" in H and "fixed" in H:
        f["semantic_cost"] = f"{H['semantic']['index_embed_words'] / H['fixed']['index_embed_words']:.1f}×"
        f["semantic_mrr"] = ci(H["semantic"], "mrr@10")
    f["budget_best"] = ci(best, budget)
    trunc = {LABEL[k]: (int(v["chunks_over_model_limit"]), int(v["n_chunks"])) for k, v in H.items()}
    f["truncation"] = ", ".join(f"{k} {n}/{tot}" for k, (n, tot) in trunc.items())
    worst_t = max(trunc.items(), key=lambda kv: kv[1][0] / max(kv[1][1], 1))
    f["worst_trunc_name"] = worst_t[0]
    f["worst_trunc_pct"] = f"{100 * worst_t[1][0] / worst_t[1][1]:.0f}%"

    if tax:
        tot = sum(int(r["misses_top5"]) for r in tax)
        f["total_misses"] = tot
        f["split_misses"] = sum(int(r["evidence split across chunks"]) for r in tax)
        f["wrongdoc_misses"] = sum(int(r["wrong document"]) for r in tax)
        f["wrongpassage_misses"] = sum(int(r["right document, wrong passage"]) for r in tax)
    # which wrong documents the retriever actually fell into, at the selected settings
    import collections, csv as _csv
    sel = {k: float(v) for k, v in info["selected_on_dev"].items()}
    cnt: collections.Counter = collections.Counter()
    pq = d / "per_question.csv"
    if pq.exists():
        for r in _csv.DictReader(open(pq, encoding="utf-8")):
            if r["retriever"] != prim or r.get("split") != "test":
                continue
            if sel.get(r["strategy"]) != float(r["param"]):
                continue
            rank = r["rank_of_first_relevant"]
            if rank == "" or int(rank) > 5:
                cnt[r["top1_doc"]] += 1
    f["top_wrong_docs"] = ", ".join(f"`{doc}` ({n})" for doc, n in cnt.most_common(3)) or "n/a"
    # overlap: where does its benefit actually land? (short vs long evidence)
    if "fixed_overlap" in H and "fixed" in H:
        o, b = H["fixed_overlap"], H["fixed"]
        f["ov_short_r3"] = f"{b['recall@3_short']:.2f} to {o['recall@3_short']:.2f}"
        f["ov_long_r3"] = f"{b['recall@3_long']:.2f} to {o['recall@3_long']:.2f}"
        f["ov_long_mrr"] = f"{b['mrr@10_long']:.2f} to {o['mrr@10_long']:.2f}"
        bm_ov = next((r for r in paired if r["retriever"] == "bm25" and r["strategy"] == "fixed_overlap"
                      and r["metric"] == "recall@3"), None)
        f["ov_bm25"] = (f"{bm_ov['diff_vs_reference']:+.3f} (CI [{bm_ov['diff_lo']:+.3f}, {bm_ov['diff_hi']:+.3f}])"
                        if bm_ov else "n/a")
        ov_mrr = next((r for r in pm if r["strategy"] == "fixed_overlap"), None)
        if ov_mrr:
            f["overlap_delta"] = f"{ov_mrr['diff_vs_reference']:+.3f}"   # from the paired file, not rounded means

    # dense vs BM25, paired like everything else
    dvb_rows = []
    dvb = d / "paired_dense_vs_bm25.csv"
    if dvb.exists():
        import csv as _c
        dvb_rows = [r for r in _c.DictReader(open(dvb, encoding="utf-8"))]
    ref_dvb = next((r for r in dvb_rows if r["strategy"] == "fixed" and r["metric"] == "mrr@10"), None)
    f["dense_vs_bm25_paired"] = (f"{float(ref_dvb['dense_minus_bm25']):+.3f} MRR "
                                 f"(95% CI [{float(ref_dvb['diff_lo']):+.3f}, {float(ref_dvb['diff_hi']):+.3f}])"
                                 ) if ref_dvb else "n/a"

    # the "evidence split" bucket could not have been non-zero: say so
    ans = {r["answerable"] for r in rows}
    f["answerable_note"] = ("every configuration, at every size tried, left at least half of every "
                            "evidence passage inside some chunk (`answerable` = 1.00 in all "
                            f"{len(rows)} rows of summary.csv)") if ans == {1.0} else \
                           f"answerable ranged {min(ans):.2f}–{max(ans):.2f} across configurations"
    f["n_selected_configs"] = len(info["selected_on_dev"])
    sweep_tr = [(LABEL.get(r["strategy"], r["strategy"]), int(r["chunks_over_model_limit"]), int(r["n_chunks"]))
                for r in rows if r["retriever"] == prim]
    worst_sweep = max(sweep_tr, key=lambda t: t[1] / max(t[2], 1))
    f["worst_sweep_trunc"] = f"{worst_sweep[0]} at the largest size tried ({100 * worst_sweep[1] / worst_sweep[2]:.0f}% of its chunks)"
    f["results_section"] = (d / "results_section.md").read_text(encoding="utf-8")
    return d, f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--template", default="article/template.md")
    ap.add_argument("--out", default="article/FINAL.md")
    args = ap.parse_args()
    d, f = facts(args.tag)
    tpl = (ROOT / args.template).read_text(encoding="utf-8")
    needed = {x[1] for x in string.Formatter().parse(tpl) if x[1]}
    missing = sorted(needed - set(f))
    if missing:
        sys.exit(f"BUILD FAILED: template needs facts that the results do not provide: {missing}")
    out = tpl.format(**f)
    if re.search(r"\{[a-z_]+\}", out):
        sys.exit("BUILD FAILED: unfilled placeholder remains")
    (ROOT / args.out).write_text(out, encoding="utf-8")
    print(f"wrote {args.out} ({len(out.split())} words) from results/{args.tag}")
    print(f"unused facts (fine): {sorted(set(f) - needed - {'results_section'})}")


if __name__ == "__main__":
    main()
