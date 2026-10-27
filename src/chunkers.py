"""Four chunking strategies. Every chunker works on one document at a time and returns
Chunk objects that remember their character span, so relevance can be judged
independently of how the text was split.

"Size" is measured in whitespace-separated words (a cheap stand-in for tokens).
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np

WORD = re.compile(r"\S+")
SENT_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")


@dataclass
class Chunk:
    doc: str
    start: int
    end: int
    text: str


def _make(doc: str, text: str, start: int, end: int) -> Chunk | None:
    seg = text[start:end]
    lead = len(seg) - len(seg.lstrip())
    seg = seg.strip()
    if not seg:
        return None
    return Chunk(doc, start + lead, start + lead + len(seg), seg)


def _word_prefix(text: str) -> np.ndarray:
    """prefix[i] = number of words that start before character i."""
    mark = np.zeros(len(text) + 1, dtype=np.int64)
    for m in WORD.finditer(text):
        mark[m.start() + 1] = 1
    return np.cumsum(mark)


def n_words(text: str) -> int:
    return len(WORD.findall(text))


# ---------------------------------------------------------------- 1. fixed-size
def fixed_size(doc: str, text: str, size: int, overlap: int = 0) -> list[Chunk]:
    """Cut every `size` words, ignoring sentence and paragraph boundaries."""
    words = [(m.start(), m.end()) for m in WORD.finditer(text)]
    step = max(1, size - overlap)
    out = []
    for i in range(0, len(words), step):
        j = min(i + size, len(words))
        c = _make(doc, text, words[i][0], words[j - 1][1])
        if c:
            out.append(c)
        if j == len(words):
            break
    return out


# ------------------------------------------------------------ sentence helpers
def sentence_spans(text: str) -> list[tuple[int, int]]:
    """Source text has roughly one sentence per line; also split lines that hold several."""
    spans = []
    pos = 0
    for line in text.split("\n"):
        if line.strip():
            cuts = [0] + [m.end() for m in SENT_BOUNDARY.finditer(line)] + [len(line)]
            for a, b in zip(cuts[:-1], cuts[1:]):
                if line[a:b].strip():
                    spans.append((pos + a, pos + b))
        pos += len(line) + 1
    return spans


# ------------------------------------------------------------ 2. sentence-based
def sentence_based(doc: str, text: str, size: int) -> list[Chunk]:
    """Pack whole sentences until the next one would push the chunk past `size` words."""
    out, cur = [], None
    for s, e in sentence_spans(text):
        w = n_words(text[s:e])
        if cur is None:
            cur = [s, e, w]
        elif cur[2] + w <= size:
            cur[1], cur[2] = e, cur[2] + w
        else:
            c = _make(doc, text, cur[0], cur[1])
            out.append(c) if c else None
            cur = [s, e, w]
    if cur:
        c = _make(doc, text, cur[0], cur[1])
        out.append(c) if c else None
    return out


# ---------------------------------------------------------------- 3. recursive
SEPARATORS = ["\n\n", "\n", ". ", " "]


def _recursive_spans(text, start, end, size, seps, pre):
    if pre[end] - pre[start] <= size:
        return [(start, end)]
    if not seps:
        words = [(m.start() + start, m.end() + start) for m in WORD.finditer(text[start:end])]
        return [(words[i][0], words[min(i + size, len(words)) - 1][1]) for i in range(0, len(words), size)]
    sep, rest = seps[0], seps[1:]
    pieces, pos = [], start
    for m in re.finditer(re.escape(sep), text[start:end]):
        pieces.append((pos, start + m.start()))
        pos = start + m.end()
    pieces.append((pos, end))
    pieces = [p for p in pieces if text[p[0]:p[1]].strip()]
    out, cur = [], None
    for p in pieces:
        if pre[p[1]] - pre[p[0]] > size:
            if cur:
                out.append(cur)
                cur = None
            out.extend(_recursive_spans(text, p[0], p[1], size, rest, pre))
        elif cur is None:
            cur = p
        elif pre[p[1]] - pre[cur[0]] <= size:
            cur = (cur[0], p[1])
        else:
            out.append(cur)
            cur = p
    if cur:
        out.append(cur)
    return out


def recursive(doc: str, text: str, size: int) -> list[Chunk]:
    """Split on paragraph, then line, then sentence, then word boundaries, merging
    neighbours back together up to `size` words (same idea as LangChain's
    RecursiveCharacterTextSplitter, reimplemented here so the repo has no heavy deps)."""
    pre = _word_prefix(text)
    out = []
    for s, e in _recursive_spans(text, 0, len(text), size, SEPARATORS, pre):
        c = _make(doc, text, s, e)
        if c:
            out.append(c)
    return out


# ---------------------------------------------------------------- 4. semantic
def semantic(doc: str, text: str, embedder, percentile: float = 85,
             min_words: int = 30, max_words: int = 300) -> list[Chunk]:
    """Embed every sentence and start a new chunk where the meaning shifts most:
    where the distance (1 - cosine) between neighbouring sentences is above the
    given percentile for this document. Chunks are kept between min_words and max_words."""
    spans = sentence_spans(text)
    if len(spans) < 2:
        c = _make(doc, text, 0, len(text))
        return [c] if c else []
    vecs = embedder.encode([text[s:e] for s, e in spans])
    dist = 1.0 - np.sum(vecs[:-1] * vecs[1:], axis=1)
    thr = np.percentile(dist, percentile)
    out, cur = [], [spans[0][0], spans[0][1], n_words(text[spans[0][0]:spans[0][1]])]
    for i in range(1, len(spans)):
        s, e = spans[i]
        w = n_words(text[s:e])
        shift = dist[i - 1] >= thr and cur[2] >= min_words
        if shift or cur[2] + w > max_words:
            c = _make(doc, text, cur[0], cur[1])
            out.append(c) if c else None
            cur = [s, e, w]
        else:
            cur[1], cur[2] = e, cur[2] + w
    c = _make(doc, text, cur[0], cur[1])
    out.append(c) if c else None
    return out
