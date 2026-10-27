"""Check every question: evidence resolves to exactly one passage in its document.

Also prints the evidence-length distribution and flags suspicious question texts
(a question that shares a very long exact phrase with its evidence is too easy).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import dataset  # noqa: E402


def main() -> int:
    docs = dataset.load_docs()
    raw = dataset.json.loads(dataset.QUESTIONS.read_text(encoding="utf-8"))
    problems, resolved = 0, []
    for q in raw:
        try:
            resolved.append(dataset.resolve(q, docs))
        except ValueError as err:
            print("PROBLEM:", err)
            problems += 1
    words = sorted(q["evidence_words"] for q in resolved)
    if words:
        print(f"{len(resolved)} questions resolved; evidence length (words): min {words[0]}, "
              f"median {words[len(words)//2]}, max {words[-1]}; "
              f">25 words: {sum(w > 25 for w in words)}")
    leaks = 0
    for q in resolved:                           # longest common word run between question and evidence
        qw, ew = q["question"].lower().split(), q["evidence"].lower().split()
        best = 0
        for i in range(len(qw)):
            for j in range(len(ew)):
                k = 0
                while i + k < len(qw) and j + k < len(ew) and qw[i + k].strip("?,.") == ew[j + k].strip("?,."):
                    k += 1
                best = max(best, k)
        if best >= 6:
            print(f"WARNING {q['id']}: question repeats {best} consecutive evidence words")
            leaks += 1
    print(f"{problems} problems, {leaks} verbatim-overlap warnings")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
