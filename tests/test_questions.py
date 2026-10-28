"""Invariants the question set must hold. These ran as a one-off audit when the set was rebuilt;
they live here so the set cannot quietly regress.

Needs the corpus, so these skip when data/docs is empty (scripts/fetch_corpus.py populates it).
"""
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "data" / "docs"
QUESTIONS = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))

# a passage opening with a back-reference cannot be judged relevant on its own, and one opening
# with a bare discourse connective reads as a fragment lifted out of an argument
BANNED_FIRST = {"this", "that", "it", "these", "those", "they", "then", "so", "such", "here",
                "there", "he", "she", "his", "her", "its", "their", "also", "thus", "hence",
                "however", "instead", "both", "which"}

pytestmark = pytest.mark.skipif(
    not any(DOCS.glob("*.txt")), reason="corpus not fetched; run scripts/fetch_corpus.py")


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


@pytest.fixture(scope="module")
def texts():
    return {p.stem: p.read_text(encoding="utf-8") for p in DOCS.glob("*.txt")}


@pytest.mark.parametrize("q", QUESTIONS, ids=lambda q: q["id"])
def test_question_is_well_formed(q, texts):
    assert set(q) == {"id", "doc", "question", "evidence"}, q["id"]
    assert q["doc"] in texts, f"{q['id']}: unknown document {q['doc']}"
    text, ev = texts[q["doc"]], q["evidence"]

    assert text.count(ev) == 1, f"{q['id']}: evidence occurs {text.count(ev)}x, must be exactly once"
    assert 10 <= len(ev.split()) <= 40, f"{q['id']}: evidence is {len(ev.split())} words"

    first = words(ev)[:1]
    assert first and first[0] not in BANNED_FIRST, f"{q['id']}: evidence opens with {first}"

    assert q["question"].rstrip().endswith("?"), f"{q['id']}: question is not a question"
    assert not re.search(r"\b(according to|as (mentioned|stated|described))\b", q["question"], re.I), \
        f"{q['id']}: question refers to the source instead of asking about the subject"

    # a question that repeats a long run of its own evidence is answerable by string matching
    ew, qw = words(ev), words(q["question"])
    grams = {tuple(ew[i:i + 6]) for i in range(len(ew) - 5)}
    assert not any(tuple(qw[i:i + 6]) in grams for i in range(len(qw) - 5)), \
        f"{q['id']}: question repeats 6+ consecutive words of its evidence"


def test_ids_are_unique_and_sequential():
    ids = [q["id"] for q in QUESTIONS]
    assert len(set(ids)) == len(ids)
    assert ids == [f"q{i:03d}" for i in range(1, len(ids) + 1)]


def test_no_duplicate_questions_or_evidence():
    qs = [" ".join(words(q["question"])) for q in QUESTIONS]
    assert len(set(qs)) == len(qs), "duplicate question text"
    ev = [(q["doc"], q["evidence"]) for q in QUESTIONS]
    assert len(set(ev)) == len(ev), "two questions share one evidence passage"


def test_evidence_spans_do_not_overlap(texts):
    """Two questions pointing at overlapping text would be scored by the same retrieved chunk."""
    by_doc = {}
    for q in QUESTIONS:
        start = texts[q["doc"]].index(q["evidence"])
        by_doc.setdefault(q["doc"], []).append((start, start + len(q["evidence"]), q["id"]))
    for doc, spans in by_doc.items():
        spans.sort()
        for (_, end_a, id_a), (start_b, _, id_b) in zip(spans, spans[1:]):
            assert start_b >= end_a, f"{id_a} and {id_b} overlap in {doc}"


def test_every_document_carries_questions(texts):
    """Coverage must stay even: a set crowded onto a few documents reports on a fraction of the
    corpus while leaving the rest as decoration."""
    counts = {}
    for q in QUESTIONS:
        counts[q["doc"]] = counts.get(q["doc"], 0) + 1
    assert set(counts) == set(texts), f"uncovered: {sorted(set(texts) - set(counts))}"
    assert max(counts.values()) / len(QUESTIONS) <= 0.05, "one document dominates the set"
