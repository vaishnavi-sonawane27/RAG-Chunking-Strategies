"""Embedders and retrievers.

Embedders return L2-normalised vectors, so a dot product is cosine similarity.

* OnnxEmbedder                - ONNX BERT-style encoder run with onnxruntime (no PyTorch).
* SentenceTransformerEmbedder - the same models through sentence-transformers / Hugging Face.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from pathlib import Path

import numpy as np

TOKEN = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())


# ------------------------------------------------------------------ embedders
class SentenceTransformerEmbedder:
    def __init__(self, model_name: str, query_prefix: str | None = None):
        from sentence_transformers import SentenceTransformer  # imported lazily

        self.name = model_name
        self.model = SentenceTransformer(model_name)
        if query_prefix is None and "bge" in model_name.lower() and "m3" not in model_name.lower():
            query_prefix = "Represent this sentence for searching relevant passages: "
        self.query_prefix = query_prefix or ""

    def encode(self, texts: list[str], is_query: bool = False) -> np.ndarray:
        if is_query and self.query_prefix:
            texts = [self.query_prefix + t for t in texts]
        return np.asarray(
            self.model.encode(texts, normalize_embeddings=True, batch_size=64, show_progress_bar=False),
            dtype=np.float32,
        )


class OnnxEmbedder:
    """Runs an ONNX BERT-style encoder with onnxruntime + tokenizers (no PyTorch).

    pooling="cls"  -> first token (BGE models);  pooling="mean" -> attention-masked mean (MiniLM).
    Inputs longer than max_len word pieces are truncated; `n_truncated` counts how often.
    """

    def __init__(self, name: str, model_dir: Path, pooling: str, max_len: int, query_prefix: str = "", batch: int = 16):
        import onnxruntime as ort
        from tokenizers import Tokenizer

        self.name = name
        self.pooling, self.max_len, self.query_prefix, self.batch = pooling, max_len, query_prefix, batch
        so = ort.SessionOptions()
        so.intra_op_num_threads = 2
        self.sess = ort.InferenceSession(str(Path(model_dir) / "model.onnx"), so, providers=["CPUExecutionProvider"])
        self.tok = Tokenizer.from_file(str(Path(model_dir) / "tokenizer.json"))
        self.tok.no_padding()
        self.tok.no_truncation()
        self.input_names = {i.name for i in self.sess.get_inputs()}
        self.n_encoded = 0
        self.n_truncated = 0
        self._cache: dict[tuple[bool, str], np.ndarray] = {}

    def _encode_batch(self, texts: list[str]) -> np.ndarray:
        encs = self.tok.encode_batch(texts)
        ids = []
        for e in encs:
            self.n_encoded += 1
            x = e.ids
            if len(x) > self.max_len:
                self.n_truncated += 1
                x = x[: self.max_len - 1] + [x[-1]]      # keep the final [SEP]
            ids.append(x)
        width = max(len(x) for x in ids)
        arr = np.zeros((len(ids), width), dtype=np.int64)
        mask = np.zeros((len(ids), width), dtype=np.int64)
        for i, x in enumerate(ids):
            arr[i, : len(x)] = x
            mask[i, : len(x)] = 1
        feed = {"input_ids": arr, "attention_mask": mask}
        if "token_type_ids" in self.input_names:
            feed["token_type_ids"] = np.zeros_like(arr)
        hidden = self.sess.run(None, feed)[0]
        if self.pooling == "cls":
            vec = hidden[:, 0, :]
        else:
            m = mask[:, :, None].astype(np.float32)
            vec = (hidden * m).sum(axis=1) / np.maximum(m.sum(axis=1), 1e-9)
        return vec / np.maximum(np.linalg.norm(vec, axis=1, keepdims=True), 1e-9)

    def n_over_limit(self, texts: list[str]) -> int:
        """How many of these texts exceed max_len word pieces and would be truncated."""
        return sum(len(e.ids) > self.max_len for e in self.tok.encode_batch(list(texts)))

    def encode(self, texts: list[str], is_query: bool = False) -> np.ndarray:
        if is_query and self.query_prefix:
            texts = [self.query_prefix + t for t in texts]
        keys = [(is_query, t) for t in texts]
        missing = sorted({k for k in keys if k not in self._cache}, key=lambda k: len(k[1]))
        for i in range(0, len(missing), self.batch):
            part = missing[i : i + self.batch]
            vecs = self._encode_batch([k[1] for k in part])
            for k, v in zip(part, vecs):
                self._cache[k] = v.astype(np.float32)
        return np.stack([self._cache[k] for k in keys])


# ----------------------------------------------------------------- retrievers
class DenseRetriever:
    def __init__(self, embedder, chunks):
        self.embedder = embedder
        self.mat = embedder.encode([c.text for c in chunks])

    def search(self, query: str, k: int) -> list[int]:
        q = self.embedder.encode([query], is_query=True)[0]
        sims = self.mat @ q
        return list(np.argsort(-sims, kind="stable")[:k])


class BM25Retriever:
    """Plain Okapi BM25 over chunk text (k1=1.5, b=0.75). Used as a non-neural reference."""

    def __init__(self, chunks, k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.tf = [Counter(tokenize(c.text)) for c in chunks]
        self.len = np.array([sum(t.values()) for t in self.tf], dtype=np.float64)
        self.avg = self.len.mean()
        df = Counter(t for tf in self.tf for t in tf)
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def search(self, query: str, k: int) -> list[int]:
        scores = np.zeros(len(self.tf))
        for t in set(tokenize(query)):
            idf = self.idf.get(t)
            if idf is None:
                continue
            for i, tf in enumerate(self.tf):
                f = tf.get(t, 0)
                if f:
                    scores[i] += idf * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
        return list(np.argsort(-scores, kind="stable")[:k])
