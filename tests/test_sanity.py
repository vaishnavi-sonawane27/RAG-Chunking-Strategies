"""End-to-end sanity check: if the query IS the evidence sentence, retrieval should find it.

Requires data/docs (python scripts/fetch_corpus.py). Run: python tests/test_sanity.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
import run_experiment as rx  # noqa: E402
from retrieval import BM25Retriever  # noqa: E402


def test_evidence_as_query_is_found_by_bm25():
    docs = rx.load_docs()
    qs = rx.load_questions(docs)
    for strategy, param in (("fixed", 150), ("sentence", 150), ("recursive", 150)):
        chunks = rx.build_chunks(strategy, param, docs, None)
        retr = BM25Retriever(chunks)
        hits = sum(rx.first_rank(retr.search(q["evidence"], 10), chunks, q) == 1 for q in qs)
        rate = hits / len(qs)
        print(f"{strategy}: evidence-as-query recall@1 = {rate:.2f}")
        assert rate >= 0.9, f"{strategy} sanity check failed ({rate:.2f})"


if __name__ == "__main__":
    test_evidence_as_query_is_found_by_bm25()
    print("ok")
