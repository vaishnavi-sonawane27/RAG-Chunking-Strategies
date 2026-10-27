"""Run with: python -m pytest -q   (or python tests/test_chunkers.py)"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import chunkers  # noqa: E402

TEXT = ("Git stores snapshots. Every commit records the staged state.\n"
        "Branches are cheap pointers. They move forward on each commit.\n\n"
        "Merging combines histories. A fast-forward just moves a pointer.\n" * 6)


class FakeEmbedder:
    def encode(self, texts, is_query=False):
        rng = np.random.default_rng(0)
        v = rng.standard_normal((len(texts), 8))
        return v / np.linalg.norm(v, axis=1, keepdims=True)


def check_spans(chunks, text):
    for c in chunks:
        assert text[c.start:c.end] == c.text, "chunk text must equal its source span"
        assert c.text.strip() == c.text


def test_all_strategies_keep_valid_spans():
    for ch in (chunkers.fixed_size("d", TEXT, 20), chunkers.fixed_size("d", TEXT, 20, overlap=5),
               chunkers.sentence_based("d", TEXT, 20), chunkers.recursive("d", TEXT, 20),
               chunkers.semantic("d", TEXT, FakeEmbedder(), percentile=70, min_words=5, max_words=40)):
        assert ch
        check_spans(ch, TEXT)


def test_size_limits():
    assert max(chunkers.n_words(c.text) for c in chunkers.fixed_size("d", TEXT, 20)) <= 20
    assert max(chunkers.n_words(c.text) for c in chunkers.recursive("d", TEXT, 20)) <= 20
    assert max(chunkers.n_words(c.text) for c in chunkers.semantic("d", TEXT, FakeEmbedder(), 70, 5, 40)) <= 40


def test_fixed_covers_every_word():
    ch = chunkers.fixed_size("d", TEXT, 20)
    assert sum(chunkers.n_words(c.text) for c in ch) == chunkers.n_words(TEXT)


def test_sentence_chunks_end_on_sentence_boundaries():
    for c in chunkers.sentence_based("d", TEXT, 20):
        assert c.text.rstrip()[-1] in ".!?"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
