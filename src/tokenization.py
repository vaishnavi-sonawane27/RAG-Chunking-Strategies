"""Token accounting, shared by the chunkers, the metrics and the size settings.

Every chunk size, context budget and token-level metric in this experiment is measured with
ONE canonical tokenizer (bge-small's WordPiece vocabulary), regardless of which embedding model
is being evaluated. That keeps chunk boundaries identical across models, so a difference between
models is a difference in the model and not in how the text was cut.

Reporting sizes in tokens rather than words is what makes these numbers comparable with the
published chunking evaluations, which all work in tokens.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "data" / "_models" / "bge-small" / "tokenizer.json"


class Tok:
    def __init__(self, path: Path | None = None):
        from tokenizers import Tokenizer

        p = Path(path or CANONICAL)
        if not p.exists():
            raise SystemExit(f"Tokenizer missing at {p}. Run: python scripts/fetch_models.py bge-small")
        self.tok = Tokenizer.from_file(str(p))
        self.tok.no_padding()
        self.tok.no_truncation()
        self.name = "bge-small WordPiece"
        # keyed by the text itself, NOT by id(text): CPython reuses ids after garbage
        # collection, so an id-keyed cache can serve one string's offsets for another.
        self._off: dict[str, list[tuple[int, int]]] = {}
        self._pre: dict[str, np.ndarray] = {}

    def offsets(self, text: str) -> list[tuple[int, int]]:
        """Character span of every token, in order. Cached per text object."""
        got = self._off.get(text)
        if got is None:
            got = [o for o in self.tok.encode(text, add_special_tokens=False).offsets if o[1] > o[0]]
            self._off[text] = got
        return got

    def prefix(self, text: str) -> np.ndarray:
        """prefix[i] = number of tokens that start strictly before character i."""
        got = self._pre.get(text)
        if got is None:
            mark = np.zeros(len(text) + 1, dtype=np.int64)
            for a, _ in self.offsets(text):
                mark[a + 1] = 1
            got = np.cumsum(mark)
            self._pre[text] = got
        return got

    def count(self, text: str) -> int:
        return len(self.tok.encode(text, add_special_tokens=False).ids)

    def span_count(self, text: str, start: int, end: int) -> int:
        """Tokens whose start lies inside [start, end)."""
        pre = self.prefix(text)
        return int(pre[min(end, len(text))] - pre[min(start, len(text))])

    def token_index_range(self, text: str, start: int, end: int) -> tuple[int, int]:
        """[first, last) token indices covered by a character span, for token-level metrics."""
        off = self.offsets(text)
        lo = np.searchsorted(np.array([o[0] for o in off]), start, side="left")
        hi = np.searchsorted(np.array([o[1] for o in off]), end, side="right")
        return int(lo), int(max(hi, lo))
