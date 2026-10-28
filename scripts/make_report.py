"""Turn results/<tag>/*.csv into charts and a machine-written results section.

    python scripts/make_report.py --tag bge-small
    python scripts/make_report.py --tag bge-small --compare minilm

Every number in the generated markdown is read from the CSVs; none is hand-typed.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["fixed", "fixed_overlap", "sentence", "recursive", "semantic"]
LABEL = {"fixed": "Fixed-size", "fixed_overlap": "Fixed + overlap", "sentence": "Sentence-based",
         "recursive": "Recursive", "semantic": "Semantic"}
COLOR = {"fixed": "#2a78d6", "fixed_overlap": "#eb6834", "sentence": "#1baf7a",
         "recursive": "#eda100", "semantic": "#e87ba4"}
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"


def load(tag):
    d = ROOT / "results" / tag

    def rows(name):
        p = d / name
        if not p.exists():
            return []
        out = []
        for r in csv.DictReader(open(p, encoding="utf-8")):
            for k, v in list(r.items()):
                if k in ("strategy", "retriever", "metric", "label"):
                    continue
                if k == "headline":
                    r[k] = v == "True"
                else:
                    try:
                        r[k] = float(v)
                    except (ValueError, TypeError):
                        pass
            out.append(r)
        return out

    return d, rows("summary.csv"), rows("paired_vs_reference.csv"), rows("failure_taxonomy.csv"), \
        rows("paired_dense_vs_bm25.csv"), json.loads((d / "run_info.json").read_text())


def primary_of(rows):
    return "dense" if any(r["retriever"] == "dense" for r in rows) else "bm25"


def head(rows, retriever):
    return {r["strategy"]: r for r in rows if r["headline"] and r["retriever"] == retriever}


def present(rows):
    return [s for s in ORDER if any(r["strategy"] == s and r["headline"] for r in rows)]


def style(ax, xgrid=False):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(axis="x" if xgrid else "y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


# ------------------------------------------------------------------- charts
def chart_headline(d, rows, info):
    prim = primary_of(rows)
    H, bm = head(rows, prim), (head(rows, "bm25") if prim == "dense" else {})
    names = [s for s in present(rows) if s in H]
    if not names:
        return
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), facecolor=SURFACE)
    for ax, (m, title) in zip(axes, [("recall@3", "Recall@3"), ("mrr@10", "MRR@10")]):
        style(ax)
        for i, s in enumerate(names):
            r = H[s]
            v, lo, hi = r[m], r[m + "_lo"], r[m + "_hi"]
            ax.bar(i, v, width=0.6, color=COLOR[s], edgecolor=SURFACE, linewidth=2, zorder=2)
            ax.errorbar(i, v, yerr=[[v - lo], [hi - v]], color=INK, linewidth=1.3, capsize=4, zorder=3)
            ax.text(i, 0.03, f"{v:.2f}", ha="center", color=SURFACE, fontsize=10, fontweight="bold", zorder=4)
            if s in bm:
                ax.scatter(i, bm[s][m], marker="D", s=44, facecolor=SURFACE, edgecolor=INK, linewidth=1.5, zorder=5)
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels([LABEL[s] for s in names], color=INK2, fontsize=8.5)
        ax.set_ylim(0, 1.0)
        ax.set_title(title, loc="left", color=INK, fontsize=12, fontweight="bold")
    axes[0].set_ylabel("higher is better", color=INK2, fontsize=9)
    axes[1].scatter([], [], marker="D", s=44, facecolor=SURFACE, edgecolor=INK, linewidth=1.5, label="BM25, same chunks")
    axes[1].errorbar([], [], yerr=[[0], [0]], color=INK, label="95% bootstrap CI")
    axes[1].legend(frameon=False, fontsize=8.5, labelcolor=INK2, loc="upper right")
    fig.suptitle(f"Retrieval quality by chunking strategy: {info['embedder']}, {info['n_test']} test questions",
                 x=0.01, ha="left", color=INK, fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(d / "chart_headline.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_paired(d, paired, info):
    prim = "dense" if any(r["retriever"] == "dense" for r in paired) else "bm25"
    rows = [r for r in paired if r["retriever"] == prim and r["headline"] and r["metric"] == "mrr@10"]
    rows = [r for r in rows if r["strategy"] in ORDER]
    if not rows:
        return
    rows.sort(key=lambda r: ORDER.index(r["strategy"]))
    fig, ax = plt.subplots(figsize=(9.5, 0.9 + 0.72 * len(rows)), facecolor=SURFACE)
    style(ax, xgrid=True)
    for i, r in enumerate(rows):
        v, lo, hi = r["diff_vs_reference"], r["diff_lo"], r["diff_hi"]
        c = COLOR[r["strategy"]]
        ax.plot([lo, hi], [i, i], color=c, linewidth=3, solid_capstyle="round", zorder=2)
        ax.scatter(v, i, s=90, color=c, edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.text(hi + 0.006, i, f"{v:+.3f}  [{lo:+.3f}, {hi:+.3f}]", va="center", color=INK, fontsize=9)
    ax.axvline(0, color=INK, linewidth=1.2, zorder=1)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([LABEL[r["strategy"]] for r in rows], color=INK2)
    ax.set_ylim(-0.95, len(rows) - 0.45)
    lim = max(max(abs(r["diff_lo"]), abs(r["diff_hi"])) for r in rows)
    ax.set_xlim(-lim * 1.25, lim * 2.6)
    ax.set_xlabel(f"change in MRR@10 vs {info['reference']} (same test questions, paired bootstrap)",
                  color=INK2, fontsize=9)
    ax.text(0, -0.55, "  an interval crossing this line is not distinguishable from the baseline",
            color=INK2, fontsize=8.5, va="center")
    ax.set_title(f"Does any strategy beat the {info['reference']} baseline?", loc="left",
                 color=INK, fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(d / "chart_paired.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_overlap(d, rows, info):
    """The overlap sweep, and why the precision denominator decides the verdict."""
    prim = primary_of(rows)
    k = int(info["token_metric_k"])
    pts = [r for r in rows if r["retriever"] == prim and r["strategy"] in ("fixed", "fixed_overlap")
           and r["param"] == info.get("overlap_size", 200)]
    if len(pts) < 2:
        return
    pts.sort(key=lambda r: r["overlap"])
    xs = [int(r["overlap"]) for r in pts]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), facecolor=SURFACE)
    style(axes[0])
    for m, lab, col in (("recall@3", "Recall@3", COLOR["fixed"]),
                        (f"recall@{int(info['budget_tokens'])}tok", f"Recall @{int(info['budget_tokens'])}-token budget", COLOR["sentence"])):
        ys = [r[m] for r in pts]
        axes[0].plot(xs, ys, marker="o", markersize=8, linewidth=2, color=col,
                     markeredgecolor=SURFACE, markeredgewidth=2, label=lab)
        axes[0].fill_between(xs, [r[m + "_lo"] for r in pts], [r[m + "_hi"] for r in pts], color=col, alpha=0.13)
    axes[0].set_ylim(0, 1.0)
    axes[0].set_xlabel("overlap (tokens)", color=INK2, fontsize=9)
    axes[0].set_title("Coverage rises with overlap", loc="left", color=INK, fontsize=11.5, fontweight="bold")
    axes[0].legend(frameon=False, fontsize=8.5, labelcolor=INK2, loc="lower right")

    style(axes[1])
    for m, lab, col in ((f"token_precision@{k}", "counting duplicate text twice (as Chroma does)", COLOR["fixed_overlap"]),
                        (f"token_precision_union@{k}", "counting each piece of text once", COLOR["recursive"])):
        axes[1].plot(xs, [r[m] for r in pts], marker="o", markersize=8, linewidth=2, color=col,
                     markeredgecolor=SURFACE, markeredgewidth=2, label=lab)
    axes[1].set_xlabel("overlap (tokens)", color=INK2, fontsize=9)
    axes[1].set_ylabel(f"token precision @{k}", color=INK2, fontsize=9)
    axes[1].set_title("…but whether that costs you depends on how you count", loc="left",
                      color=INK, fontsize=11.5, fontweight="bold")
    axes[1].legend(frameon=False, fontsize=8, labelcolor=INK2, loc="best")
    fig.suptitle("Overlap sweep at a fixed chunk size", x=0.01, ha="left", color=INK, fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(d / "chart_overlap.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_sweep(d, rows, info):
    prim = primary_of(rows)
    fig, ax = plt.subplots(figsize=(9, 4.4), facecolor=SURFACE)
    style(ax)
    for s in ORDER:
        pts = sorted((r["mean_tokens"], r["mrr@10"]) for r in rows
                     if r["strategy"] == s and r["retriever"] == prim)
        if not pts:
            continue
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=COLOR[s], linewidth=2, marker="o", markersize=8,
                markeredgecolor=SURFACE, markeredgewidth=2, label=LABEL[s], zorder=3)
    cand = [r["mrr@10"] for r in rows if r["retriever"] == prim]
    ax.set_ylim(0, min(1.0, max(cand) * 1.4) if cand else 1.0)
    ax.set_xlim(left=0)
    ax.set_xlabel("mean realised chunk length (tokens)", color=INK2, fontsize=9)
    ax.set_ylabel(f"MRR@10 ({prim} retrieval)", color=INK2, fontsize=9)
    ax.legend(frameon=False, fontsize=8.5, labelcolor=INK2, loc="lower right", ncol=3)
    ax.set_title("Strategy separates more than size does: fixed-size is last at every size", loc="left",
                 color=INK, fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(d / "chart_size_sweep.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_models(d, rows_a, info_a, rows_b, info_b):
    """Does the ranking survive a change of embedding model, on the SAME chunks?"""
    A = head(rows_a, "dense")
    by_b = {(r["strategy"], int(r["param"]), int(r["overlap"])): r for r in rows_b if r["retriever"] == "dense"}
    B = {}
    for st, v in info_a["selected_on_dev"].items():
        key = (st, int(v["size"]), int(v["overlap"]))
        if key in by_b:
            B[st] = by_b[key]
    names = [s for s in ORDER if s in A and s in B]
    if len(names) < 2:
        return
    fig, ax = plt.subplots(figsize=(9.5, 4.6), facecolor=SURFACE)
    style(ax)
    for i, s in enumerate(names):
        ax.plot([0, 1], [A[s]["mrr@10"], B[s]["mrr@10"]], color=COLOR[s], linewidth=2.5, zorder=2)
        ax.scatter([0, 1], [A[s]["mrr@10"], B[s]["mrr@10"]], s=90, color=COLOR[s],
                   edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.text(-0.03, A[s]["mrr@10"], LABEL[s], ha="right", va="center", color=INK, fontsize=9)
        ax.text(1.03, B[s]["mrr@10"], f"{B[s]['mrr@10']:.2f}", ha="left", va="center", color=INK, fontsize=9)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([info_a["embedder"], info_b["embedder"]], color=INK, fontsize=10, fontweight="bold")
    ax.set_xlim(-0.42, 1.3)
    ax.set_ylabel("MRR@10", color=INK2, fontsize=9)
    ax.set_title("Same chunks, different embedding model: does the ranking survive?", loc="left",
                 color=INK, fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(d / "chart_models.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


# ------------------------------------------------------------------- tables
def ci(r, m, nd=2):
    return f"{r[m]:.{nd}f} ({r[m + '_lo']:.{nd}f}–{r[m + '_hi']:.{nd}f})"


def table_headline(rows, retriever, info):
    H = head(rows, retriever)
    names = [s for s in present(rows) if s in H]
    bt, k = int(info["budget_tokens"]), int(info["token_metric_k"])
    out = [f"| Strategy | Setting | Chunks | Mean tokens | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @{bt} tok | Token precision@{k} |",
           "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for s in names:
        r = H[s]
        setting = r["label"].split(" ", 1)[1] if " " in r["label"] else r["label"]
        out.append(f"| {LABEL[s]} | `{setting}` | {int(r['n_chunks'])} | {r['mean_tokens']:.0f} | "
                   f"{r['evidence_intact']:.2f} | {ci(r, 'recall@1')} | {ci(r, 'recall@3')} | "
                   f"{ci(r, 'mrr@10')} | {ci(r, f'recall@{bt}tok')} | {100 * r[f'token_precision@{k}']:.2f}% |")
    return "\n".join(out)


def table_sweep(rows, info):
    prim = primary_of(rows)
    k = int(info["token_metric_k"])
    out = ["| Configuration | Chunks | Mean tokens | Evidence intact | Recall@3 | MRR@10 | Token precision@%d |" % k,
           "|---|---:|---:|---:|---:|---:|---:|"]
    for s in ORDER:
        for r in sorted((x for x in rows if x["strategy"] == s and x["retriever"] == prim),
                        key=lambda x: (x["param"], x["overlap"])):
            out.append(f"| `{r['label']}` | {int(r['n_chunks'])} | {r['mean_tokens']:.0f} | "
                       f"{r['evidence_intact']:.2f} | {r['recall@3']:.2f} | {r['mrr@10']:.2f} | "
                       f"{100 * r[f'token_precision@{k}']:.2f}% |")
    return "\n".join(out)


def table_overlap(rows, info):
    prim = primary_of(rows)
    k, bt = int(info["token_metric_k"]), int(info["budget_tokens"])
    pts = sorted((r for r in rows if r["retriever"] == prim and r["strategy"] in ("fixed", "fixed_overlap")
                  and r["param"] == info.get("overlap_size", 200)), key=lambda r: r["overlap"])
    if len(pts) < 2:
        return ""
    out = [f"| Overlap | Chunks | Tokens indexed | Recall@3 | Recall @{bt} tok | Token precision@{k} (duplicates counted) | Token precision@{k} (counted once) |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for r in pts:
        pc = 100 * r["overlap"] / r["param"]
        out.append(f"| {int(r['overlap'])} tok ({pc:.0f}%) | {int(r['n_chunks'])} | {int(r['index_embed_tokens']):,} | "
                   f"{ci(r, 'recall@3')} | {ci(r, f'recall@{bt}tok')} | "
                   f"{100 * r[f'token_precision@{k}']:.2f}% | {100 * r[f'token_precision_union@{k}']:.2f}% |")
    return "\n".join(out)


def table_paired(paired, info):
    prim = "dense" if any(r["retriever"] == "dense" for r in paired) else "bm25"
    rows = [r for r in paired if r["retriever"] == prim and r["headline"]]
    if not rows:
        return ""
    out = ["| Strategy | Metric | Change vs baseline | 95% CI | Distinguishable? |", "|---|---|---:|---|---|"]
    for r in sorted(rows, key=lambda r: (ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9, r["metric"])):
        sep = "no, CI includes 0" if r["diff_lo"] <= 0 <= r["diff_hi"] else "**yes**"
        nd = 4 if r["metric"].startswith("token_") else 3
        out.append(f"| {LABEL.get(r['strategy'], r['strategy'])} | {r['metric']} | {r['diff_vs_reference']:+.{nd}f} | "
                   f"[{r['diff_lo']:+.{nd}f}, {r['diff_hi']:+.{nd}f}] | {sep} |")
    return "\n".join(out)


def table_cost(rows, info):
    prim = primary_of(rows)
    H = head(rows, prim)
    names = [s for s in present(rows) if s in H]
    base = H.get("fixed", {}).get("index_embed_tokens")
    out = ["| Strategy | Tokens embedded to build the index | Relative cost |", "|---|---:|---:|"]
    for s in names:
        w = H[s]["index_embed_tokens"]
        out.append(f"| {LABEL[s]} | {int(w):,} | {w / base:.2f}× |" if base else f"| {LABEL[s]} | {int(w):,} | n/a |")
    return "\n".join(out)


def table_taxonomy(tax):
    if not tax:
        return ""
    cols = ["evidence split across chunks", "right document, wrong passage", "wrong document"]
    out = ["| Configuration | Misses (not in top 5) | " + " | ".join(c.capitalize() for c in cols) + " |",
           "|---|---:|---:|---:|---:|"]
    for r in sorted(tax, key=lambda r: ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9):
        out.append(f"| `{r['label']}` | {int(r['misses_top5'])} | " + " | ".join(str(int(r[c])) for c in cols) + " |")
    return "\n".join(out)


def table_models(rows_a, info_a, rows_b, info_b):
    A = head(rows_a, "dense")
    by_b = {(r["strategy"], int(r["param"]), int(r["overlap"])): r for r in rows_b if r["retriever"] == "dense"}
    B = {st: by_b[(st, int(v["size"]), int(v["overlap"]))] for st, v in info_a["selected_on_dev"].items()
         if (st, int(v["size"]), int(v["overlap"])) in by_b}
    names = [s for s in ORDER if s in A and s in B]
    if len(names) < 2:
        return ""
    ra = sorted(names, key=lambda s: -A[s]["mrr@10"])
    rb = sorted(names, key=lambda s: -B[s]["mrr@10"])
    out = [f"| Strategy | Configuration | MRR@10 ({info_a['embedder']}) | rank | MRR@10 ({info_b['embedder']}) | rank |",
           "|---|---|---:|---:|---:|---:|"]
    for s in names:
        out.append(f"| {LABEL[s]} | `{A[s]['label']}` | {A[s]['mrr@10']:.2f} | {ra.index(s) + 1} | "
                   f"{B[s]['mrr@10']:.2f} | {rb.index(s) + 1} |")
    return "\n".join(out)


def table_dense_vs_bm25(dvb):
    if not dvb:
        return ""
    out = ["| Strategy | Metric | Dense minus BM25 | 95% CI |", "|---|---|---:|---|"]
    for r in dvb:
        if r["metric"] not in ("mrr@10", "recall@3"):
            continue
        out.append(f"| {LABEL.get(r['strategy'], r['strategy'])} | {r['metric']} | "
                   f"{r['dense_minus_bm25']:+.3f} | [{r['diff_lo']:+.3f}, {r['diff_hi']:+.3f}] |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--compare", default=None, help="a second tag (another embedding model)")
    args = ap.parse_args()
    d, rows, paired, tax, dvb, info = load(args.tag)
    info["overlap_size"] = next((r["param"] for r in rows if r["strategy"] == "fixed_overlap"), 200)
    prim = primary_of(rows)
    bt = int(info["budget_tokens"])

    chart_headline(d, rows, info)
    chart_paired(d, paired, info)
    chart_overlap(d, rows, info)
    chart_sweep(d, rows, info)

    sel = ", ".join(f"`{k} {v['size']}" + (f"+{v['overlap']}" if v["overlap"] else "") + "`"
                    for k, v in sorted(info["selected_on_dev"].items()))
    parts = [f"<!-- generated by scripts/make_report.py from results/{args.tag}; do not edit by hand -->",
             f"\n**Run:** {info['embedder']} · {info['n_docs']} documents · {info['n_questions']} questions "
             f"· {int(info['bootstrap_resamples']):,} bootstrap resamples. Sizes are in "
             f"{info['tokenizer']} tokens.\n",
             f"**Protocol:** chunk sizes, overlaps and thresholds were chosen on {int(info['n_dev'])} dev questions; "
             f"every number below is measured on the {int(info['n_test'])} held-out test questions "
             f"(split seed {int(info['split_seed'])}). Selected on dev: {sel}.\n",
             f"### Headline comparison ({prim} retrieval)\n", "![Headline comparison](chart_headline.png)\n",
             table_headline(rows, prim, info)]
    if prim == "dense":
        parts += ["\n### Same chunks, BM25 instead of embeddings\n", table_headline(rows, "bm25", info),
                  "\n### Dense versus BM25, paired on the same questions\n", table_dense_vs_bm25(dvb)]
    parts += [f"\n### Is any strategy actually different from the {info['reference']} baseline?\n",
              "![Paired differences](chart_paired.png)\n", table_paired(paired, info),
              "\n### The overlap sweep\n", "![Overlap sweep](chart_overlap.png)\n", table_overlap(rows, info),
              "\n### Every configuration tried\n", "![Size sweep](chart_size_sweep.png)\n", table_sweep(rows, info),
              "\n### Indexing cost\n", table_cost(rows, info),
              "\n### Where retrieval failed\n", table_taxonomy(tax)]

    if args.compare:
        d2, rows2, _, _, _, info2 = load(args.compare)
        chart_models(d, rows, info, rows2, info2)
        parts += ["\n### Same chunks, a different embedding model\n",
                  "![Model comparison](chart_models.png)\n", table_models(rows, info, rows2, info2)]

    (d / "results_section.md").write_text("\n".join(p for p in parts if p) + "\n", encoding="utf-8")
    print(f"wrote charts and results_section.md in {d}")


if __name__ == "__main__":
    main()
