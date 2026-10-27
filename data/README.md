# Data, provenance and licensing

## Corpus

The corpus is **Pro Git, second edition**, by Scott Chacon and Ben Straub, chapters 1–8 and 10
(64 sections, ~107,000 words).

* Source: https://github.com/progit/progit2
* License: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
* https://creativecommons.org/licenses/by-nc-sa/3.0/

**The book text is not stored in this repository.** `scripts/fetch_corpus.py` clones the upstream
repository and converts the AsciiDoc sources to plain text in `data/docs/` (git-ignored). This keeps
the repo small and avoids redistributing the book.

### Why this corpus

* It is openly licensed and stable, so anyone can reproduce the exact inputs.
* It is long enough (~107k words) that retrieval has to discriminate, not just rank a handful of chunks.
* It contains **near-miss distractors by design**: `undoing` (ch. 2) vs `reset` (ch. 7), `branching`
  (ch. 3) vs `rebasing` (ch. 3/7), `remotes` (ch. 2) vs `distributed workflows` (ch. 5). These are
  exactly the confusions that make real RAG retrieval fail.

## Questions

`data/questions.json` holds **130 questions**. Each is tied to one evidence passage that occurs
**exactly once** in its source document, given either as:

* `evidence`: a verbatim string, or
* `evidence_from` + `evidence_to`: the passage starting at the first string and ending after the
  next occurrence of the second (used for multi-sentence evidence).

`scripts/validate_questions.py` checks that every passage resolves uniquely and warns when a question
repeats six or more consecutive words from its own evidence (which would make it trivially easy).

**Coverage:** questions cover 20 of the 64 documents. The remaining 44 documents act as distractors.
This is deliberate: a retriever must reject plausible but wrong sections, not just rank within a
small candidate set.

**Evidence length** ranges from 6 to 99 words (median 16). Because the relevance rule is an overlap
threshold, longer evidence is easier to hit, so every metric is also reported split by
short (≤25 words) and long (>25 words) evidence.

### Licensing of the questions

The evidence fields contain short verbatim excerpts of Pro Git. `data/questions.json` is therefore a
derivative work and is distributed under **CC BY-NC-SA 3.0**, the same license as the book, *not*
the MIT license that covers the code. The NonCommercial clause applies.

### Honest provenance

The questions were drafted with AI assistance and then checked programmatically: every evidence
passage is verified to exist exactly once in the source text, and questions are checked for verbatim
leakage. They were deliberately paraphrased rather than copied from the book, so that lexical
matching alone is not sufficient.

They have **not** all been independently reviewed by a second human. Treat the absolute scores as
properties of this question set, not as universal truths about chunking.
