"""Render article/FINAL.md to .docx and .pdf for reading and review.

The article's chart references are relative to the results directory they were written into, so
this resolves them before handing the file to pandoc. Wide results tables are the hard part: the
default Word margins shred them, so the reference document is patched to narrow margins and a
smaller table font.

    python scripts/build_doc.py --tag bge-small
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def reference_doc(dest: Path) -> Path:
    """pandoc's own default reference.docx, with margins narrowed and table text shrunk."""
    base = dest / "reference-raw.docx"
    subprocess.run(["pandoc", "-o", str(base), "--print-default-data-file", "reference.docx"],
                   check=True, stdout=subprocess.DEVNULL)
    if not base.exists():                      # older pandoc writes to stdout instead
        with open(base, "wb") as fh:
            subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                           check=True, stdout=fh)
    out = dest / "reference.docx"
    with zipfile.ZipFile(base) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                # 680 twips ~= 1.2 cm; the default 1440 leaves too little room for the tables
                data = re.sub(rb'w:left="\d+"', b'w:left="680"', data)
                data = re.sub(rb'w:right="\d+"', b'w:right="680"', data)
            if item.filename == "word/styles.xml":
                data = data.replace(b'w:styleId="Compact"',
                                    b'w:styleId="Compact" w:customStyle="0"')
                # shrink Compact (what pandoc puts inside table cells): 15 half-points = 7.5pt
                data = re.sub(rb'(<w:style [^>]*w:styleId="Compact".*?)<w:sz w:val="\d+"/>',
                              rb'\1<w:sz w:val="15"/>', data, flags=re.S)
            zout.writestr(item, data)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="bge-small", help="results directory holding the charts")
    ap.add_argument("--name", default="RAG Chunking Strategies - Article")
    args = ap.parse_args()

    src = ROOT / "article" / "FINAL.md"
    charts = ROOT / "results" / args.tag
    if not src.exists():
        sys.exit("article/FINAL.md not found; run scripts/build_article.py first")

    text = src.read_text(encoding="utf-8")
    missing = [m for m in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text) if not (charts / m).exists()]
    if missing:
        sys.exit(f"chart(s) missing from {charts}: {', '.join(missing)}")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        # absolute chart paths so pandoc embeds the images wherever it is run from
        body = re.sub(r"(!\[[^\]]*\]\()([^)]+)(\))",
                      lambda m: m.group(1) + str(charts / m.group(2)) + m.group(3), text)
        # Word has no break opportunity inside "token_precision@5" and so wraps it mid-word.
        # A zero-width space after each underscore and before each @ lets it break sensibly.
        # Table rows only, so prose and code spans are untouched.
        def breakable(line: str) -> str:
            if not line.startswith("|"):
                return line
            return line.replace("_", "_\u200b").replace("@", "\u200b@")
        body = "\n".join(breakable(l) for l in body.splitlines())

        md = tmp / "article.md"
        md.write_text(body, encoding="utf-8")
        ref = reference_doc(tmp)

        docx = ROOT / "article" / f"{args.name}.docx"
        subprocess.run(["pandoc", str(md), "-o", str(docx), "--reference-doc", str(ref),
                        "--toc", "--toc-depth=2", "-V", "linkcolor=blue"], check=True)
        print("wrote", docx.name)

        r = subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf",
                            "--outdir", str(tmp), str(docx)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        produced = tmp / (docx.stem + ".pdf")
        if r.returncode == 0 and produced.exists():
            shutil.copy(produced, ROOT / "article" / produced.name)
            print("wrote", produced.name)
        else:
            print("PDF conversion failed; the .docx is still good", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
