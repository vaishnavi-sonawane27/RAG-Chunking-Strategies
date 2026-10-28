"""End-to-end sanity checks on the dataset and the scoring rule.

Needs data/docs (run: python scripts/fetch_corpus.py).
Run: python -m pytest -q   (or python tests/test_sanity.py)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

import dataset  # noqa: E402
from tokenization import Tok  # noqa: E402
import run_experiment as rx  # noqa: E402
from retrieval import BM25Retriever  # noqa: E402


TOK = Tok()


def _load():
    docs = dataset.load_docs()
    return docs, dataset.load_questions(docs)


def test_evidence_as_query_is_retrieved():
    """If the query IS the answer passage, retrieval must find it. If this fails, the
    harness is broken and no result from it means anything."""
    docs, qs = _load()
    for strategy, param in (("fixed", 200), ("sentence", 200), ("recursive", 200)):
        chunks = rx.build_chunks(strategy, param, 0, docs, None, TOK)
        retr = BM25Retriever(chunks)
        hits = sum(rx.first_rank(retr.search(q["evidence"], 10), chunks, q) == 1 for q in qs)
        rate = hits / len(qs)
        print(f"{strategy}: evidence-as-query recall@1 = {rate:.2f}")
        assert rate >= 0.9, f"{strategy} sanity check failed ({rate:.2f})"


def test_every_question_is_answerable_by_some_chunking():
    """Each question's evidence must be recoverable by at least one strategy, otherwise
    the question is unanswerable by construction rather than hard."""
    docs, qs = _load()
    chunks = rx.build_chunks("sentence", 400, 0, docs, None, TOK)
    missing = [q["id"] for q in qs if not any(rx.relevant(c, q) for c in chunks)]
    assert not missing, f"evidence unreachable even with large sentence chunks: {missing}"


def test_dev_test_split_is_deterministic_and_disjoint():
    docs, qs = _load()
    a = {q["id"]: q["split"] for q in dataset.assign_splits(qs, 0, 0.3)}
    docs2, qs2 = _load()
    b = {q["id"]: q["split"] for q in dataset.assign_splits(qs2, 0, 0.3)}
    assert a == b, "split is not deterministic"
    assert set(a.values()) == {"dev", "test"}
    n_dev = sum(v == "dev" for v in a.values())
    assert 0.2 < n_dev / len(a) < 0.4, f"dev fraction off: {n_dev}/{len(a)}"


def test_relevance_rule_rejects_a_half_overlap_miss():
    """A chunk covering less than half the evidence must not count as relevant."""
    docs, qs = _load()
    q = qs[0]
    s, e = q["span"]
    cut = s + int(0.4 * (e - s))

    class Fake:
        doc, start, end = q["doc"], s, cut

    assert not rx.relevant(Fake, q)

    class Full:
        doc, start, end = q["doc"], s, e

    assert rx.relevant(Full, q) and rx.intact(Full, q)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
