"""Turn results/<tag>/*.csv into charts and a machine-written results section.

    python scripts/make_report.py --tag bge-small

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
NUM = ("param", "overlap", "n_chunks", "mean_words", "chunks_over_model_limit", "index_embed_words",
       "chunking_seconds", "evidence_intact", "answerable", "mean_words_in_budget")


def load(tag):
    d = ROOT / "results" / tag

    def rows(name):
        p = d / name
        if not p.exists():
            return []
        out = []
        for r in csv.DictReader(open(p, encoding="utf-8")):
            for k, v in list(r.items()):
                if k in ("strategy", "retriever", "metric"):
                    continue
                if k in ("headline", "main"):
                    r[k] = v == "True"
                else:
                    try:
                        r[k] = float(v)
                    except (ValueError, TypeError):
                        pass
            out.append(r)
        return out

    return d, rows("summary.csv"), rows("paired_vs_reference.csv"), rows("failure_taxonomy.csv"), \
        json.loads((d / "run_info.json").read_text())


def style(ax, xgrid=False):
    ax.set_facecolor(SURFACE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(axis="x" if xgrid else "y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def primary_of(rows):
    return "dense" if any(r["retriever"] == "dense" for r in rows) else "bm25"


def head(rows, retriever="dense"):
    return {r["strategy"]: r for r in rows if r["headline"] and r["retriever"] == retriever}


def present(rows):
    return [s for s in ORDER if any(r["strategy"] == s and r["headline"] for r in rows)]


# ------------------------------------------------------------------- charts
def chart_headline(d, rows, info):
    prim = primary_of(rows)
    dense, bm = head(rows, prim), (head(rows, "bm25") if prim == "dense" else {})
    if not dense:
        return
    names = [s for s in present(rows) if s in dense]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), facecolor=SURFACE)
    for ax, (m, title) in zip(axes, [("recall@3", "Recall@3"), ("mrr@10", "MRR@10")]):
        style(ax)
        for i, s in enumerate(names):
            r = dense[s]
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
    fig.suptitle(f"Retrieval quality by chunking strategy: {info['embedder']}, {info['n_questions']} questions",
                 x=0.01, ha="left", color=INK, fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(d / "chart_headline.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_paired(d, paired, info):
    """Difference vs the fixed-150 reference, on the same questions and the same bootstrap resamples."""
    prim = "dense" if any(r["retriever"] == "dense" for r in paired) else "bm25"
    rows = [r for r in paired if r["retriever"] == prim and r["headline"] and r["metric"] == "mrr@10"]
    rows = [r for r in rows if r["strategy"] in ORDER]
    if not rows:
        return
    rows.sort(key=lambda r: ORDER.index(r["strategy"]))
    fig, ax = plt.subplots(figsize=(9, 0.8 + 0.72 * len(rows)), facecolor=SURFACE)
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
    lim = max(abs(r["diff_lo"]) for r in rows), max(abs(r["diff_hi"]) for r in rows)
    ax.set_xlim(-max(lim) * 1.25, max(lim) * 2.5)
    ax.set_xlabel(f"change in MRR@10 vs {info['reference']} (same test questions, paired bootstrap)", color=INK2, fontsize=9)
    ax.set_title(f"Does any strategy beat the {info['reference']} baseline?", loc="left",
                 color=INK, fontsize=12, fontweight="bold")
    ax.text(0, -0.52, "  an interval crossing this line is not distinguishable from the baseline",
            color=INK2, fontsize=8.5, va="center")
    fig.tight_layout()
    fig.savefig(d / "chart_paired.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_intact(d, rows, info):
    """Why strategies differ: how often the answer passage survives inside a single chunk."""
    dense = head(rows, primary_of(rows))
    names = [s for s in present(rows) if s in dense]
    if not names:
        return
    fig, ax = plt.subplots(figsize=(9, 4.2), facecolor=SURFACE)
    style(ax)
    for i, s in enumerate(names):
        r = dense[s]
        ax.bar(i, r["evidence_intact"], width=0.6, color=COLOR[s], edgecolor=SURFACE, linewidth=2, zorder=2)
        ax.text(i, r["evidence_intact"] + 0.015, f"{r['evidence_intact']:.2f}", ha="center",
                color=INK, fontsize=10, fontweight="bold")
        ax.text(i, 0.03, f"MRR {r['mrr@10']:.2f}", ha="center", color=SURFACE, fontsize=9, zorder=4)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels([LABEL[s] for s in names], color=INK2, fontsize=9)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("share of questions whose answer passage\nsurvives whole inside one chunk", color=INK2, fontsize=9)
    ax.set_title("At the selected sizes the answer almost always survives, and that stops predicting quality",
                 loc="left", color=INK, fontsize=11.5, fontweight="bold")
    ax.text(0, 1.045, "Semantic keeps the most evidence intact and still ranks worst, so above ~90% intact the bottleneck is the retriever.",
            color=INK2, fontsize=8.5)
    fig.tight_layout()
    fig.savefig(d / "chart_intact.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


def chart_sweep(d, rows, info):
    prim = primary_of(rows)
    fig, ax = plt.subplots(figsize=(9, 4.4), facecolor=SURFACE)
    style(ax)
    for s in ORDER:
        pts = sorted((r["mean_words"], r["mrr@10"]) for r in rows
                     if r["strategy"] == s and r["retriever"] == prim)
        if len(pts) < 2:
            if pts:
                ax.scatter([pts[0][0]], [pts[0][1]], s=80, color=COLOR[s], edgecolor=SURFACE,
                           linewidth=2, label=LABEL[s], zorder=3)
            continue
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=COLOR[s], linewidth=2, marker="o", markersize=8,
                markeredgecolor=SURFACE, markeredgewidth=2, label=LABEL[s], zorder=3)
    cand = [r["mrr@10"] for r in rows if r["retriever"] == prim]
    top = max(cand) if cand else 1.0
    ax.set_ylim(0, min(1.0, top * 1.4))
    ax.set_xlim(left=0)
    ax.set_xlabel("mean chunk length (words)", color=INK2, fontsize=9)
    ax.set_ylabel(f"MRR@10 ({prim} retrieval)", color=INK2, fontsize=9)
    ax.legend(frameon=False, fontsize=8.5, labelcolor=INK2, loc="lower right", ncol=3)
    ax.set_title("Chunk size moves the needle more than strategy does", loc="left",
                 color=INK, fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(d / "chart_size_sweep.png", dpi=160, facecolor=SURFACE)
    plt.close(fig)


# ------------------------------------------------------------------- tables
def ci(r, m):
    return f"{r[m]:.2f} ({r[m + '_lo']:.2f}–{r[m + '_hi']:.2f})"


def table_headline(rows, retriever, budget_col):
    h = head(rows, retriever)
    names = [s for s in present(rows) if s in h]
    out = ["| Strategy | Chunks | Mean words | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @450w budget |",
           "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for s in names:
        r = h[s]
        out.append(f"| {LABEL[s]} | {int(r['n_chunks'])} | {r['mean_words']:.0f} | {r['evidence_intact']:.2f} | "
                   f"{ci(r, 'recall@1')} | {ci(r, 'recall@3')} | {ci(r, 'mrr@10')} | {ci(r, budget_col)} |")
    return "\n".join(out)


def table_sweep(rows):
    out = ["| Strategy | Setting | Mean words | Evidence intact | Recall@3 | MRR@10 |", "|---|---|---:|---:|---:|---:|"]
    for s in ORDER:
        for r in sorted((x for x in rows if x["strategy"] == s and x["retriever"] == "dense"),
                        key=lambda x: x["param"]):
            setting = (f"{int(r['param'])}th percentile" if s == "semantic"
                       else f"{int(r['param'])} words" + (f" + {int(r['overlap'])} overlap" if r["overlap"] else ""))
            out.append(f"| {LABEL[s]} | {setting} | {r['mean_words']:.0f} | {r['evidence_intact']:.2f} | "
                       f"{r['recall@3']:.2f} | {r['mrr@10']:.2f} |")
    return "\n".join(out)


def table_short_long(rows, budget_col):
    h = head(rows, primary_of(rows))
    names = [s for s in present(rows) if s in h]
    out = ["| Strategy | MRR@10 short evidence | MRR@10 long evidence |", "|---|---:|---:|"]
    for s in names:
        out.append(f"| {LABEL[s]} | {h[s]['mrr@10_short']:.2f} | {h[s]['mrr@10_long']:.2f} |")
    return "\n".join(out)


def table_cost(rows):
    h = head(rows, primary_of(rows))
    names = [s for s in present(rows) if s in h]
    base = h.get("fixed", {}).get("index_embed_words")
    out = ["| Strategy | Words embedded to build the index | Relative cost |", "|---|---:|---:|"]
    for s in names:
        w = h[s]["index_embed_words"]
        out.append(f"| {LABEL[s]} | {int(w):,} | {w / base:.2f}× |" if base else f"| {LABEL[s]} | {int(w):,} | n/a |")
    return "\n".join(out)


def table_paired(paired, budget_col):
    prim = "dense" if any(r["retriever"] == "dense" for r in paired) else "bm25"
    rows = [r for r in paired if r["retriever"] == prim and r["headline"]]
    if not rows:
        return ""
    out = ["| Strategy | Metric | Change vs baseline | 95% CI | Distinguishable? |", "|---|---|---:|---|---|"]
    for r in sorted(rows, key=lambda r: (ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9, r["metric"])):
        sep = "no, CI includes 0" if r["diff_lo"] <= 0 <= r["diff_hi"] else "**yes**"
        out.append(f"| {LABEL.get(r['strategy'], r['strategy'])} | {r['metric']} | {r['diff_vs_reference']:+.3f} | "
                   f"[{r['diff_lo']:+.3f}, {r['diff_hi']:+.3f}] | {sep} |")
    return "\n".join(out)


def table_taxonomy(tax):
    if not tax:
        return ""
    cols = ["evidence split across chunks", "right document, wrong passage", "wrong document"]
    out = ["| Strategy | Misses (not in top 5) | " + " | ".join(c.capitalize() for c in cols) + " |",
           "|---|---:|---:|---:|---:|"]
    for r in sorted(tax, key=lambda r: ORDER.index(r["strategy"]) if r["strategy"] in ORDER else 9):
        out.append(f"| {LABEL.get(r['strategy'], r['strategy'])} | {int(r['misses_top5'])} | "
                   + " | ".join(str(int(r[c])) for c in cols) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    args = ap.parse_args()
    d, rows, paired, tax, info = load(args.tag)
    budget_col = f"recall@{int(info['budget_words'])}w"

    chart_headline(d, rows, info)
    chart_paired(d, paired, info)
    chart_intact(d, rows, info)
    chart_sweep(d, rows, info)

    parts: list = [f"<!-- generated by scripts/make_report.py from results/{args.tag}; do not edit by hand -->",
             f"\n**Run:** {info['embedder']} · {info['n_docs']} documents · {info['n_questions']} questions "
             f"({info['n_short_evidence']} short evidence, {info['n_long_evidence']} long) · "
             f"{int(info['bootstrap_resamples']):,} bootstrap resamples.\n",
             f"**Protocol:** chunk sizes and thresholds were chosen on {info['n_dev']} dev questions; "
             f"every number below is measured on the {info['n_test']} held-out test questions "
             f"(split seed {info['split_seed']}). Selected on dev: "
             + ", ".join(f"`{k}={v}`" for k, v in sorted(info['selected_on_dev'].items())) + ".\n",
             f"### Headline comparison ({primary_of(rows)} retrieval)\n", "![Headline comparison](chart_headline.png)\n",
             table_headline(rows, primary_of(rows), budget_col)]
    if primary_of(rows) == "dense":
        parts += ["\n### Same chunks, BM25 instead of embeddings\n", table_headline(rows, "bm25", budget_col)]
    parts += [
             "\n### Is any strategy actually different from plain fixed-size chunking?\n",
             "![Paired differences](chart_paired.png)\n", table_paired(paired, budget_col),
             "\n### Does the answer passage survive chunking?\n", "![Evidence intact](chart_intact.png)",
             "\n### Chunk size sweep\n", "![Size sweep](chart_size_sweep.png)\n", table_sweep(rows),
             "\n### Short vs long evidence passages\n", table_short_long(rows, budget_col),
             "\n### Indexing cost\n", table_cost(rows),
             "\n### Where retrieval failed\n", table_taxonomy(tax)]
    (d / "results_section.md").write_text("\n".join(p for p in parts if p) + "\n", encoding="utf-8")
    print(f"wrote 4 charts and results_section.md in {d}")


if __name__ == "__main__":
    main()
