"""Chunker invariants. Run: python -m pytest -q"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import chunkers  # noqa: E402
from tokenization import Tok  # noqa: E402

TEXT = ("Git stores snapshots. Every commit records the staged state.\n"
        "Branches are cheap pointers. They move forward on each commit.\n\n"
        "Merging combines histories. A fast-forward just moves a pointer.\n" * 6)
TOK = Tok()


class FakeEmbedder:
    def encode(self, texts, is_query=False):
        v = np.random.default_rng(0).standard_normal((len(texts), 8))
        return v / np.linalg.norm(v, axis=1, keepdims=True)


def check_spans(chunks, text):
    for c in chunks:
        assert text[c.start:c.end] == c.text, "chunk text must equal its source span"
        assert c.text.strip() == c.text


def test_all_strategies_keep_valid_spans():
    for ch in (chunkers.fixed_size("d", TEXT, 40, TOK),
               chunkers.fixed_size("d", TEXT, 40, TOK, overlap=10),
               chunkers.sentence_based("d", TEXT, 40, TOK),
               chunkers.recursive("d", TEXT, 40, TOK),
               chunkers.semantic("d", TEXT, FakeEmbedder(), TOK, percentile=70, min_tokens=10, max_tokens=80)):
        assert ch
        check_spans(ch, TEXT)


def test_token_size_limits_are_respected():
    for ch in (chunkers.fixed_size("d", TEXT, 40, TOK), chunkers.recursive("d", TEXT, 40, TOK)):
        assert max(TOK.count(c.text) for c in ch) <= 40
    sem = chunkers.semantic("d", TEXT, FakeEmbedder(), TOK, 70, 10, 80)
    assert max(TOK.count(c.text) for c in sem) <= 80


def test_fixed_covers_every_token_without_overlap():
    ch = chunkers.fixed_size("d", TEXT, 40, TOK)
    assert sum(TOK.count(c.text) for c in ch) >= TOK.count(TEXT) - len(ch)


def test_overlap_increases_total_indexed_tokens():
    plain = chunkers.fixed_size("d", TEXT, 40, TOK)
    over = chunkers.fixed_size("d", TEXT, 40, TOK, overlap=20)
    assert sum(TOK.count(c.text) for c in over) > sum(TOK.count(c.text) for c in plain)
    assert len(over) > len(plain)


def test_sentence_chunks_end_on_sentence_boundaries():
    for c in chunkers.sentence_based("d", TEXT, 40, TOK):
        assert c.text.rstrip()[-1] in ".!?"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
