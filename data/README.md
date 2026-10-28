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

`data/questions.json` holds **215 questions**. Each is tied to one evidence passage that occurs
**exactly once** in its source document, given either as:

* `evidence`: a verbatim string, or
* `evidence_from` + `evidence_to`: the passage starting at the first string and ending after the
  next occurrence of the second (used for multi-sentence evidence).

`scripts/validate_questions.py` checks that every passage resolves uniquely and warns when a question
repeats six or more consecutive words from its own evidence (which would make it trivially easy).

**Coverage:** every one of the 64 documents carries questions, 3 or 4 each, and no single document
holds more than 2% of the set. For any given question the other 63 documents are distractors, so a
retriever still has to reject plausible but wrong sections. An earlier version of this set put 130
questions on 20 documents; that concentrated the headline result on under a third of the corpus and
left 44 sections as decoration, so it was rebuilt.

**Evidence length** is constrained to 10 to 39 words (median 24). Because the relevance rule is an
overlap threshold, longer evidence is easier to hit, so every metric is also reported split by short
(≤40 tokens, 171 questions) and long (>40 tokens, 44 questions) evidence.

**Every passage stands alone.** No evidence passage opens with a back-reference (this, that, it,
these, they, so, such, here, there, also, however, instead, thus, hence), and no two questions in the
same document point at overlapping spans of text. A passage that begins "This is why it fails" cannot
be judged relevant or not on its own, which makes it unusable as ground truth.

### Licensing of the questions

The evidence fields contain short verbatim excerpts of Pro Git. `data/questions.json` is therefore a
derivative work and is distributed under **CC BY-NC-SA 3.0**, the same license as the book, *not*
the MIT license that covers the code. The NonCommercial clause applies.

### Audit

`scripts/analyse_questions.py` writes `data/question_audit.json` and reports:

| Check | Result | Previous set |
|---|---|---|
| Near-duplicate questions (cosine > 0.90) | 0 | 0 |
| Questions repeating 6+ consecutive words of their own evidence | 0 | 0 |
| Questions with >75% lexical overlap with their evidence | 0 | 1 |
| Evidence passages opening with an anaphor (not self-contained) | 0 of 215 | 19 of 130 |
| Evidence passages of 9 words or fewer | 0 | 6 |
| Documents carrying questions | 64 of 64 | 20 of 64 |
| Largest share from a single document | 2% | 15% |
| Mean question-to-evidence cosine similarity | 0.729 | 0.737 |
| Questions where another passage matches better | 67 (31%) | 54 (42%) |

Read the last two rows together. A mean similarity of 0.73 with 31% of questions matching some other
labelled passage more closely means the questions are genuinely paraphrased rather than lookups,
which is what you want. It also means a minority are ambiguous enough that a passage scored as wrong
could be defended as right. That lowers every strategy's absolute score about equally, so comparisons
between strategies hold, but absolute numbers are a floor rather than a ceiling.

The 31% is measured against a *larger* field than the 42% it replaces: 215 competing passages instead
of 130, so the improvement is not an artefact of having fewer rivals to lose to.

### Honest provenance

The questions were drafted with AI assistance and then checked programmatically: every evidence
passage is verified to exist exactly once in the source text, and questions are checked for verbatim
leakage. They were deliberately paraphrased rather than copied from the book, so that lexical
matching alone is not sufficient.

They have **not** all been independently reviewed by a second human. Treat the absolute scores as
properties of this question set, not as universal truths about chunking.
