"""Assemble the publishable article from the prose template plus the real results.

    python scripts/make_report.py   --tag bge-small --compare minilm
    python scripts/build_article.py --tag bge-small --compare minilm

Writes article/FINAL.md. Every {placeholder} in article/template.md is filled from the result
CSVs. If a placeholder has no matching fact the build FAILS rather than shipping an article with
a hand-typed or stale number in it.
"""
from __future__ import annotations

import argparse
import re
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from make_report import LABEL, ORDER, head, load, primary_of  # noqa: E402


def ci(r, m, nd=2):
    return f"{r[m]:.{nd}f} (95% CI {r[m + '_lo']:.{nd}f}–{r[m + '_hi']:.{nd}f})"


def pct(x):
    return f"{100 * x:.0f}%"


def facts(tag, compare=None):
    d, rows, paired, tax, dvb, info = load(tag)
    info["overlap_size"] = next((r["param"] for r in rows if r["strategy"] == "fixed_overlap"), 200)
    prim = primary_of(rows)
    H, bm = head(rows, prim), head(rows, "bm25")
    k, bt = int(info["token_metric_k"]), int(info["budget_tokens"])
    budget = f"recall@{bt}tok"
    tp, tpu = f"token_precision@{k}", f"token_precision_union@{k}"

    f = {"tag": tag, "embedder": info["embedder"], "tokenizer": info["tokenizer"],
         "n_docs": int(info["n_docs"]), "n_questions": int(info["n_questions"]),
         "n_dev": int(info["n_dev"]), "n_test": int(info["n_test"]),
         "n_boot": f"{int(info['bootstrap_resamples']):,}", "reference": info["reference"],
         "budget_tokens": bt, "token_k": k, "retriever": prim,
         "sizes": ", ".join(str(int(x)) for x in info["sizes_tokens"]),
         "overlaps": ", ".join(str(int(x)) for x in info["overlaps_tokens"]),
         "python": info["platform"]["python"], "os": info["platform"]["os"],
         "cpu_count": info["platform"]["cpu_count"], "runtime_min": f"{info['seconds'] / 60:.0f}",
         "selected": ", ".join(f"`{s} {v['size']}" + (f"+{v['overlap']}" if v["overlap"] else "") + "`"
                               for s, v in sorted(info["selected_on_dev"].items()))}

    ranked = sorted(H.values(), key=lambda r: -r["mrr@10"])
    best, worst = ranked[0], ranked[-1]
    f["best_name"], f["worst_name"] = LABEL[best["strategy"]], LABEL[worst["strategy"]]
    f["best_mrr"], f["worst_mrr"] = ci(best, "mrr@10"), ci(worst, "mrr@10")
    f["best_label"], f["spread"] = best["label"], f"{best['mrr@10'] - worst['mrr@10']:.2f}"
    f["best_tprec"] = f"{100 * best[tp]:.2f}%"

    ref = H.get("fixed", ranked[-1])
    f["ref_name"], f["ref_mrr"] = LABEL[ref["strategy"]], ci(ref, "mrr@10")
    f["bm25_ref_mrr"] = ci(bm["fixed"], "mrr@10") if "fixed" in bm else "n/a"
    dvb_m = [r for r in dvb if r["metric"] == "mrr@10"]
    r_dvb = next((r for r in dvb_m if r["strategy"] == "fixed"), None)
    f["dense_vs_bm25"] = (f"{r_dvb['dense_minus_bm25']:+.3f} MRR (95% CI "
                          f"[{r_dvb['diff_lo']:+.3f}, {r_dvb['diff_hi']:+.3f}])") if r_dvb else "n/a"
    dvb_sig = [r for r in dvb_m if r["diff_lo"] > 0]
    f["dvb_n_sig"], f["dvb_n_total"] = len(dvb_sig), len(dvb_m)
    if dvb_sig:
        b = max(dvb_sig, key=lambda r: r["dense_minus_bm25"])
        f["dvb_best"] = (f"{LABEL[b['strategy']]} at {b['diff_vs_reference'] if False else b['dense_minus_bm25']:+.3f} "
                         f"MRR (95% CI [{b['diff_lo']:+.3f}, {b['diff_hi']:+.3f}])")
        f["dvb_best_name"] = LABEL[b["strategy"]]
        f["dvb_best_val"] = f"{b['dense_minus_bm25']:+.3f}"
    f["dvb_exceptions"] = ", ".join(LABEL[r["strategy"]] for r in dvb_m if r["diff_lo"] <= 0) or "none"

    pm = [r for r in paired if r["retriever"] == prim and r["headline"] and r["metric"] == "mrr@10"]
    allp = [r for r in paired if r["retriever"] == prim and r["headline"]]
    sep = [r for r in allp if not (r["diff_lo"] <= 0 <= r["diff_hi"])]
    f["n_compared"], f["n_all_comparisons"], f["n_all_separated"] = len(pm), len(allp), len(sep)
    f["n_mrr_crossing"] = sum(1 for r in pm if r["diff_lo"] <= 0 <= r["diff_hi"])
    f["widest_ci"] = f"{max(r['diff_hi'] - r['diff_lo'] for r in pm):.2f}" if pm else "n/a"
    f["sep_detail"] = "; ".join(
        f"**{LABEL.get(r['strategy'], r['strategy'])}** on {r['metric']} ({r['diff_vs_reference']:+.3f}, "
        f"CI [{r['diff_lo']:+.3f}, {r['diff_hi']:+.3f}])"
        for r in sorted(sep, key=lambda r: (ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9, r["metric"]))
    ) or "no comparison separated from the baseline on any metric"

    # ---- overlap sweep
    ov = sorted((r for r in rows if r["retriever"] == prim and r["strategy"] in ("fixed", "fixed_overlap")
                 and r["param"] == info["overlap_size"]), key=lambda r: r["overlap"])
    if len(ov) >= 2:
        z, hi = ov[0], ov[-1]
        f["ov_size"] = int(z["param"])
        f["ov_max"] = f"{int(hi['overlap'])} tokens ({100 * hi['overlap'] / hi['param']:.0f}%)"
        f["ov_recall_0"], f["ov_recall_max"] = f"{z['recall@3']:.2f}", f"{hi['recall@3']:.2f}"
        f["ov_budget_0"], f["ov_budget_max"] = f"{z[budget]:.2f}", f"{hi[budget]:.2f}"
        f["ov_tprec_dup"] = f"{100 * z[tp]:.2f}% to {100 * hi[tp]:.2f}%"
        f["ov_tprec_uni"] = f"{100 * z[tpu]:.2f}% to {100 * hi[tpu]:.2f}%"
        f["ov_index_growth"] = f"{hi['index_embed_tokens'] / z['index_embed_tokens']:.2f}×"
        f["ov_dup_dir"] = "falls" if hi[tp] < z[tp] else "rises"
        f["ov_uni_dir"] = "falls" if hi[tpu] < z[tpu] else "rises"
        mrrs = [f"{r['mrr@10']:.3f}" for r in ov]
        f["ov_mrr_path"] = " then ".join(mrrs)
        f["ov_first_gain"] = f"{ov[1]['mrr@10'] - ov[0]['mrr@10']:+.3f}"
        f["ov_rest_gain"] = f"{ov[-1]['mrr@10'] - ov[1]['mrr@10']:+.3f}"
        f["ov_first_step"] = f"{int(ov[1]['overlap'])} tokens ({100 * ov[1]['overlap'] / ov[1]['param']:.0f}%)"
        f["ov_verdict"] = ("the two denominators disagree about whether overlap costs you context efficiency"
                           if (hi[tp] < z[tp]) != (hi[tpu] < z[tpu])
                           else "both denominators agree on the direction")

    # ---- does strategy or size move the numbers more?
    grid = {(r["strategy"], int(r["param"])): r["mrr@10"] for r in rows
            if r["retriever"] == prim and r["overlap"] == 0 and r["strategy"] in ("fixed", "sentence", "recursive")}
    sizes_l = sorted({sz for (_, sz) in grid})
    strat_spreads, size_spreads = [], []
    for sz in sizes_l:
        v = [grid[(st, sz)] for st in ("fixed", "sentence", "recursive") if (st, sz) in grid]
        if len(v) > 1:
            strat_spreads.append(max(v) - min(v))
    for st in ("fixed", "sentence", "recursive"):
        v = [grid[(st, sz)] for sz in sizes_l if (st, sz) in grid]
        if len(v) > 1:
            size_spreads.append(max(v) - min(v))
    f["strategy_spread"] = f"{min(strat_spreads):.3f} to {max(strat_spreads):.3f}"
    f["size_spread"] = f"{min(size_spreads):.3f} to {max(size_spreads):.3f}"
    f["matters_more"] = "strategy" if sum(strat_spreads) / len(strat_spreads) > sum(size_spreads) / len(size_spreads) else "size"
    f["matters_less"] = "size" if f["matters_more"] == "strategy" else "strategy"
    f["mean_strategy_spread"] = f"{sum(strat_spreads) / len(strat_spreads):.3f}"
    f["mean_size_spread"] = f"{sum(size_spreads) / len(size_spreads):.3f}"

    # ---- how many strategies actually beat the plain-fixed baseline, with significance
    mrr_sep = [r for r in pm if r["diff_lo"] > 0]
    f["n_beat_baseline"] = len(mrr_sep)
    f["beat_baseline_detail"] = "; ".join(
        f"**{LABEL[r['strategy']]}** {r['diff_vs_reference']:+.3f} [{r['diff_lo']:+.3f}, {r['diff_hi']:+.3f}]"
        for r in sorted(mrr_sep, key=lambda r: -r["diff_vs_reference"]))
    f["all_beat_baseline"] = "every single one" if len(mrr_sep) == len(pm) else f"only {len(mrr_sep)}"

    # ---- token efficiency across sizes
    small = min((r for r in rows if r["retriever"] == prim and r["strategy"] == "fixed"), key=lambda r: r["param"])
    large = max((r for r in rows if r["retriever"] == prim and r["strategy"] == "fixed"), key=lambda r: r["param"])
    f["tprec_small"] = f"{100 * small[tp]:.2f}% at {int(small['param'])} tokens"
    f["tprec_large"] = f"{100 * large[tp]:.2f}% at {int(large['param'])} tokens"
    f["intact_table"] = ", ".join(f"{LABEL[s]} {pct(H[s]['evidence_intact'])}" for s in ORDER if s in H)
    f["intact_small"] = pct(small["evidence_intact"])
    f["small_size"] = int(small["param"])

    if "semantic" in H and "fixed" in H:
        f["semantic_cost"] = f"{H['semantic']['index_embed_tokens'] / H['fixed']['index_embed_tokens']:.1f}×"
        f["semantic_mrr"] = ci(H["semantic"], "mrr@10")
    trunc = {LABEL[s]: (int(v["chunks_over_model_limit"]), int(v["n_chunks"])) for s, v in H.items()}
    f["truncation"] = ", ".join(f"{a} {n}/{t}" for a, (n, t) in trunc.items())
    worst_t = max(trunc.items(), key=lambda kv: kv[1][0] / max(kv[1][1], 1))
    f["worst_trunc"] = f"{worst_t[0]} ({100 * worst_t[1][0] / max(worst_t[1][1], 1):.0f}% of its chunks)"

    if tax:
        f["total_misses"] = sum(int(r["misses_top5"]) for r in tax)
        f["split_misses"] = sum(int(r["evidence split across chunks"]) for r in tax)
        f["wrongdoc_misses"] = sum(int(r["wrong document"]) for r in tax)
        f["wrongpassage_misses"] = sum(int(r["right document, wrong passage"]) for r in tax)
    f["n_selected_configs"] = len(info["selected_on_dev"])
    ans = {r["answerable"] for r in rows}
    f["answerable_note"] = ("`answerable` = 1.00 in all %d rows of summary.csv" % len(rows)) if ans == {1.0} \
        else f"answerable ranged {min(ans):.2f}–{max(ans):.2f}"

    # ---- second embedding model
    if compare:
        _, rows2, _, _, _, info2 = load(compare)
        B = head(rows2, "dense")
        names = [s for s in ORDER if s in H and s in B]
        ra = sorted(names, key=lambda s: -H[s]["mrr@10"])
        rb = sorted(names, key=lambda s: -B[s]["mrr@10"])
        f["embedder2"] = info2["embedder"]
        f["model2_best"] = LABEL[rb[0]]
        f["model1_best"] = LABEL[ra[0]]
        f["ranking_same"] = "identical" if ra == rb else "different"
        moved = [f"{LABEL[s]} {ra.index(s) + 1}→{rb.index(s) + 1}" for s in names if ra.index(s) != rb.index(s)]
        f["rank_moves"] = ", ".join(moved) if moved else "no strategy changed rank"
        f["model2_spread"] = f"{B[rb[0]]['mrr@10'] - B[rb[-1]]['mrr@10']:.2f}"
        f["model2_mrr_range"] = f"{B[rb[-1]]['mrr@10']:.2f} to {B[rb[0]]['mrr@10']:.2f}"
        f["ends_stable"] = ("the best and worst strategies are the same on both models"
                            if ra[0] == rb[0] and ra[-1] == rb[-1] else "even the extremes move")
        f["worst_both"] = LABEL[ra[-1]] if ra[-1] == rb[-1] else f"{LABEL[ra[-1]]} then {LABEL[rb[-1]]}"
        mid = [LABEL[s2] for s2 in names if ra.index(s2) != rb.index(s2)]
        f["middle_moves"] = ", ".join(mid) if mid else "nothing moved"
    f["results_section"] = (d / "results_section.md").read_text(encoding="utf-8")
    return d, f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--compare", default=None)
    ap.add_argument("--template", default="article/template.md")
    ap.add_argument("--out", default="article/FINAL.md")
    args = ap.parse_args()
    _, f = facts(args.tag, args.compare)
    tpl = (ROOT / args.template).read_text(encoding="utf-8")
    needed = {x[1] for x in string.Formatter().parse(tpl) if x[1]}
    missing = sorted(needed - set(f))
    if missing:
        sys.exit(f"BUILD FAILED: template needs facts the results do not provide: {missing}")
    out = tpl.format(**f)
    if re.search(r"\{[a-z_0-9]+\}", out):
        sys.exit("BUILD FAILED: unfilled placeholder remains")
    (ROOT / args.out).write_text(out, encoding="utf-8")
    print(f"wrote {args.out} ({len(out.split())} words) from results/{args.tag}")
    print(f"unused facts (fine): {sorted(set(f) - needed - {'results_section'})}")


if __name__ == "__main__":
    main()
