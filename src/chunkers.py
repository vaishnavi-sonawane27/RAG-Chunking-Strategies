"""Five chunking strategies.

Each chunker works on one document and returns Chunk objects that remember their character
span, so relevance can be judged independently of how the text was split.

Size is measured in MODEL TOKENS using the canonical tokenizer (see src/tokenization.py),
not in words or characters. The published chunking evaluations all report token sizes, so
this is what makes these results comparable with them.
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


def n_words(text: str) -> int:
    return len(WORD.findall(text))


# ---------------------------------------------------------------- 1. fixed-size
def fixed_size(doc: str, text: str, size: int, tok, overlap: int = 0) -> list[Chunk]:
    """Cut every `size` tokens, ignoring sentence and paragraph boundaries."""
    off = tok.offsets(text)
    if not off:
        return []
    step = max(1, size - overlap)
    out = []
    for i in range(0, len(off), step):
        j = min(i + size, len(off))
        c = _make(doc, text, off[i][0], off[j - 1][1])
        if c:
            out.append(c)
        if j == len(off):
            break
    return out


# ------------------------------------------------------------ sentence helpers
def sentence_spans(text: str) -> list[tuple[int, int]]:
    """Source text is roughly one sentence per line; also split lines holding several."""
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
def sentence_based(doc: str, text: str, size: int, tok) -> list[Chunk]:
    """Pack whole sentences until the next one would push the chunk past `size` tokens."""
    out, cur = [], None
    for s, e in sentence_spans(text):
        w = tok.span_count(text, s, e)
        if cur is None:
            cur = [s, e, w]
        elif cur[2] + w <= size:
            cur[1], cur[2] = e, cur[2] + w
        else:
            c = _make(doc, text, cur[0], cur[1])
            if c:
                out.append(c)
            cur = [s, e, w]
    if cur:
        c = _make(doc, text, cur[0], cur[1])
        if c:
            out.append(c)
    return out


# ---------------------------------------------------------------- 3. recursive
SEPARATORS = ["\n\n", "\n", ". ", " "]


def _leaf_split(text, start, end, size, off):
    """Last resort: cut the span every `size` tokens."""
    idx = [i for i, o in enumerate(off) if o[0] >= start and o[1] <= end]
    if not idx:
        return [(start, end)]
    return [(off[idx[i]][0], off[idx[min(i + size, len(idx)) - 1]][1]) for i in range(0, len(idx), size)]


def _recursive_spans(text, start, end, size, seps, pre, off):
    if pre[end] - pre[start] <= size:
        return [(start, end)]
    if not seps:
        return _leaf_split(text, start, end, size, off)
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
            out.extend(_recursive_spans(text, p[0], p[1], size, rest, pre, off))
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


def recursive(doc: str, text: str, size: int, tok) -> list[Chunk]:
    """Split on paragraph, then line, then sentence, then word boundaries, merging neighbours
    back together up to `size` tokens. Same idea as LangChain's RecursiveCharacterTextSplitter,
    reimplemented here so the repo has no heavy dependencies."""
    pre, off = tok.prefix(text), tok.offsets(text)
    out = []
    for s, e in _recursive_spans(text, 0, len(text), size, SEPARATORS, pre, off):
        c = _make(doc, text, s, e)
        if c:
            out.append(c)
    return out


# ---------------------------------------------------------------- 4. semantic
def semantic(doc: str, text: str, embedder, tok, percentile: float = 85,
             min_tokens: int = 50, max_tokens: int = 500) -> list[Chunk]:
    """Embed every sentence and start a new chunk where the meaning shifts most: where the
    distance (1 - cosine) between neighbouring sentences is above the given percentile for
    this document. Chunks are held between min_tokens and max_tokens."""
    spans = sentence_spans(text)
    if len(spans) < 2:
        c = _make(doc, text, 0, len(text))
        return [c] if c else []
    vecs = embedder.encode([text[s:e] for s, e in spans])
    dist = 1.0 - np.sum(vecs[:-1] * vecs[1:], axis=1)
    thr = np.percentile(dist, percentile)
    out = []
    cur = [spans[0][0], spans[0][1], tok.span_count(text, *spans[0])]
    for i in range(1, len(spans)):
        s, e = spans[i]
        w = tok.span_count(text, s, e)
        shift = dist[i - 1] >= thr and cur[2] >= min_tokens
        if shift or cur[2] + w > max_tokens:
            c = _make(doc, text, cur[0], cur[1])
            if c:
                out.append(c)
            cur = [s, e, w]
        else:
            cur[1], cur[2] = e, cur[2] + w
    c = _make(doc, text, cur[0], cur[1])
    if c:
        out.append(c)
    return out
