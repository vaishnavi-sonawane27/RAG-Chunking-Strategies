"""Corpus and question loading, shared by the experiment, the validator and the tests.

A question in data/questions.json has either
  * "evidence": a verbatim passage that occurs exactly once in the document, or
  * "evidence_from" + "evidence_to": the passage starts at the unique string `evidence_from`
    and ends right after the first following occurrence of `evidence_to`
    (used for multi-sentence evidence so newlines need not be escaped).
Either way the resolved passage is stored as q["evidence"] and its character span as q["span"].
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "data" / "docs"
QUESTIONS = ROOT / "data" / "questions.json"


def load_docs() -> dict[str, str]:
    docs = {p.stem: p.read_text(encoding="utf-8") for p in sorted(DOCS_DIR.glob("*.txt"))}
    if not docs:
        raise SystemExit("No documents found. Run: python scripts/fetch_corpus.py")
    return docs


def resolve(q: dict, docs: dict[str, str]) -> dict:
    if q["doc"] not in docs:
        raise ValueError(f"{q['id']}: unknown document {q['doc']}")
    text = docs[q["doc"]]
    if "evidence" in q:
        ev = q["evidence"]
        if text.count(ev) != 1:
            raise ValueError(f"{q['id']}: evidence occurs {text.count(ev)} times in {q['doc']}: {ev[:60]!r}")
        s = text.find(ev)
        e = s + len(ev)
    else:
        a, b = q["evidence_from"], q["evidence_to"]
        if text.count(a) != 1:
            raise ValueError(f"{q['id']}: evidence_from occurs {text.count(a)} times: {a[:60]!r}")
        s = text.find(a)
        j = text.find(b, s)
        if j < 0:
            raise ValueError(f"{q['id']}: evidence_to not found after evidence_from: {b[:60]!r}")
        e = j + len(b)
    out = dict(q)
    out["evidence"] = text[s:e]
    out["span"] = (s, e)
    out["evidence_words"] = len(out["evidence"].split())
    return out


def load_questions(docs: dict[str, str]) -> list[dict]:
    raw = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    ids = [q["id"] for q in raw]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate question ids")
    return [resolve(q, docs) for q in raw]


def assign_splits(questions: list[dict], seed: int = 0, dev_frac: float = 0.3) -> list[dict]:
    """Deterministically mark each question dev or test, stratified by source document.

    The dev questions are the ONLY ones used to choose chunk sizes and thresholds; every
    headline number is reported on test. This stops the experiment from tuning on the data
    it reports, which is the usual way a benchmark quietly inflates itself.
    """
    import random

    by_doc: dict[str, list[dict]] = {}
    for q in questions:
        by_doc.setdefault(q["doc"], []).append(q)
    rng = random.Random(seed)
    for doc in sorted(by_doc):
        group = sorted(by_doc[doc], key=lambda q: q["id"])
        rng.shuffle(group)
        n_dev = round(dev_frac * len(group)) if len(group) > 1 else 0
        for i, q in enumerate(group):
            q["split"] = "dev" if i < n_dev else "test"
    return questions
