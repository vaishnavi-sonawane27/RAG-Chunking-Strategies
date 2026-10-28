"""Audit the question set and write data/question_audit.json.

A retrieval benchmark is only as good as its questions, and published evaluations rarely
report anything about theirs beyond how many there are. This measures the properties that
decide whether the numbers mean anything:

  * near-duplicate questions, which would weight some passages twice
  * verbatim leakage, where the question repeats its own evidence and becomes a lookup
  * question-to-evidence similarity, which shows whether questions are paraphrased or copied
  * ambiguity, where another question's evidence matches a question better than its own
  * self-containment, where evidence opens with an anaphor and needs preceding context
  * coverage and concentration across the corpus

Run: python scripts/analyse_questions.py [--embedder onnx:bge-small]
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import dataset  # noqa: E402

ANAPHOR = re.compile(r"^(in that case|this |that |it |these |those |they |then |so |such |here |there )", re.I)
DUP_THRESHOLD = 0.90
WORD = re.compile(r"[a-z]{4,}")


def longest_shared_run(a: str, b: str) -> int:
    aw, bw = a.lower().split(), b.lower().split()
    best = 0
    for i in range(len(aw)):
        for j in range(len(bw)):
            k = 0
            while i + k < len(aw) and j + k < len(bw) and aw[i + k].strip("?,.") == bw[j + k].strip("?,."):
                k += 1
            best = max(best, k)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--embedder", default="onnx:bge-small")
    args = ap.parse_args()

    docs = dataset.load_docs()
    qs = dataset.load_questions(docs)
    out: dict = {"n_questions": len(qs), "n_docs": len(docs)}

    # --- lexical checks (no model needed)
    leak = [q["id"] for q in qs if longest_shared_run(q["question"], q["evidence"]) >= 6]
    overlap_heavy = []
    for q in qs:
        qw = set(WORD.findall(q["question"].lower()))
        ew = set(WORD.findall(q["evidence"].lower()))
        if qw and len(qw & ew) / len(qw) > 0.75:
            overlap_heavy.append(q["id"])
    anaphoric = [q["id"] for q in qs if ANAPHOR.match(q["evidence"].strip())]
    short_ev = [q["id"] for q in qs if len(q["evidence"].split()) <= 8]
    per_doc = collections.Counter(q["doc"] for q in qs)
    out.update({
        "verbatim_leak": leak,
        "high_lexical_overlap": overlap_heavy,
        "anaphoric_evidence": anaphoric,
        "very_short_evidence": short_ev,
        "docs_with_questions": len(per_doc),
        "max_questions_in_one_doc": max(per_doc.values()),
        "max_doc_share": round(max(per_doc.values()) / len(qs), 3),
        "evidence_words": {"min": min(len(q["evidence"].split()) for q in qs),
                           "median": int(np.median([len(q["evidence"].split()) for q in qs])),
                           "max": max(len(q["evidence"].split()) for q in qs)},
    })

    # --- semantic checks (need an embedding model)
    if args.embedder != "none":
        from models import MODELS
        from retrieval import OnnxEmbedder
        name = args.embedder.split(":", 1)[-1]
        m = MODELS[name]
        d = ROOT / "data" / "_models" / name
        if not (d / "model.onnx").exists():
            sys.exit(f"Model missing. Run: python scripts/fetch_models.py {name}")
        emb = OnnxEmbedder(name, d, m["pooling"], m["max_len"], m["query_prefix"])
        Q = emb.encode([q["question"] for q in qs], is_query=True)
        E = emb.encode([q["evidence"] for q in qs])
        S = Q @ Q.T
        np.fill_diagonal(S, -1)
        dups = [[qs[i]["id"], qs[j]["id"], round(float(S[i, j]), 3)]
                for i in range(len(qs)) for j in range(i + 1, len(qs)) if S[i, j] > DUP_THRESHOLD]
        own = np.sum(Q * E, axis=1)
        cross = Q @ E.T
        np.fill_diagonal(cross, -1)
        margin = own - cross.max(axis=1)
        out.update({
            "embedder": emb.name,
            "duplicate_pairs": dups,
            "question_evidence_similarity": {"mean": round(float(own.mean()), 3),
                                             "min": round(float(own.min()), 3)},
            "n_ambiguous": int((margin < 0).sum()),
            "ambiguous_share": round(float((margin < 0).mean()), 3),
            "most_ambiguous": [qs[int(i)]["id"] for i in np.argsort(margin)[:5]],
        })

    (ROOT / "data" / "question_audit.json").write_text(json.dumps(out, indent=2))
    print(f"{out['n_questions']} questions over {out['docs_with_questions']} of {out['n_docs']} documents")
    print(f"  verbatim leakage        : {len(leak)}")
    print(f"  high lexical overlap    : {len(overlap_heavy)}")
    print(f"  anaphoric evidence      : {len(anaphoric)}")
    print(f"  very short evidence     : {len(short_ev)}")
    print(f"  largest single-doc share: {out['max_doc_share']:.0%}")
    if "n_ambiguous" in out:
        print(f"  near-duplicate questions: {len(out['duplicate_pairs'])}")
        print(f"  another passage matches better: {out['n_ambiguous']} ({out['ambiguous_share']:.0%})")
    print("wrote data/question_audit.json")


if __name__ == "__main__":
    main()
