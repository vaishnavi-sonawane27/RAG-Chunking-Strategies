"""Embedding models used in the experiment.

Both models are run from ONNX exports with `onnxruntime` + `tokenizers` (no PyTorch needed).
The exports are obtained from the npm registry, because it is reachable from locked-down
environments where huggingface.co is not; each download is verified against a pinned
SHA-512 integrity hash. If you have normal internet access you can also run the official
Hugging Face models with `--embedder st:<model name>` (needs sentence-transformers).

Provenance
  bge-small : BAAI/bge-small-en-v1.5, ONNX export by Xenova (the one transformers.js uses),
              redistributed in npm package @coree-ai/coree-model-bge-small-en-v1.5 (Apache-2.0)
  minilm    : sentence-transformers/all-MiniLM-L6-v2 at revision c9745ed1..., ONNX export,
              redistributed in npm package @xcidos/genesis-memory-model (Apache-2.0)
"""
from __future__ import annotations

MODELS = {
    "bge-small": {
        "hf_name": "BAAI/bge-small-en-v1.5",
        "npm_url": "https://registry.npmjs.org/@coree-ai/coree-model-bge-small-en-v1.5/-/coree-model-bge-small-en-v1.5-1.0.2.tgz",
        "integrity": "sha512-Kc/i5xG5uyIvst7YGmSdiD1hvRHBE/kTufEKRklpCo9W8G1XODFV+R6FzirnLvhDzDcXLUe4GMh+YGzYyIq5kA==",
        "onnx_glob": "package/model/models--Xenova--bge-small-en-v1.5/snapshots/*/onnx/model.onnx",
        "tokenizer_glob": "package/model/models--Xenova--bge-small-en-v1.5/snapshots/*/tokenizer.json",
        "pooling": "cls",
        "max_len": 512,
        "query_prefix": "Represent this sentence for searching relevant passages: ",
    },
    "minilm": {
        "hf_name": "sentence-transformers/all-MiniLM-L6-v2",
        "npm_url": "https://registry.npmjs.org/@xcidos/genesis-memory-model/-/genesis-memory-model-0.1.0-alpha.1.tgz",
        "integrity": "sha512-kCEWeIgZnHWzmU7MYVce9bKRDC5QzHGzRWHYZy2palhJkWkDPb1pVPmablxciyDZxkrre9nk+QcGz1HL3WvZSA==",
        "onnx_glob": "package/onnx/model.onnx",
        "tokenizer_glob": "package/tokenizer.json",
        "pooling": "mean",
        "max_len": 256,           # the sentence-transformers default for this model
        "query_prefix": "",
    },
}
