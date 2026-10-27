"""Download the ONNX embedding models into data/_models/<name>/ and verify their hashes.

    python scripts/fetch_models.py            # both models
    python scripts/fetch_models.py bge-small  # one model
"""
import base64
import glob
import hashlib
import shutil
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from models import MODELS  # noqa: E402


def fetch(name: str) -> None:
    spec = MODELS[name]
    out = ROOT / "data" / "_models" / name
    if (out / "model.onnx").exists() and (out / "tokenizer.json").exists():
        print(f"{name}: already present")
        return
    with tempfile.TemporaryDirectory() as tmp:
        tgz = Path(tmp) / "pkg.tgz"
        print(f"{name}: downloading {spec['npm_url']}")
        urllib.request.urlretrieve(spec["npm_url"], tgz)
        digest = "sha512-" + base64.b64encode(hashlib.sha512(tgz.read_bytes()).digest()).decode()
        if digest != spec["integrity"]:
            sys.exit(f"{name}: INTEGRITY MISMATCH\n  expected {spec['integrity']}\n  got      {digest}")
        print(f"{name}: integrity verified")
        ex = Path(tmp) / "x"
        with tarfile.open(tgz) as t:
            for m in t.getmembers():            # refuse anything that could escape the folder
                if m.name.startswith("/") or ".." in Path(m.name).parts or not (m.isfile() or m.isdir()):
                    continue
                t.extract(m, ex)
        out.mkdir(parents=True, exist_ok=True)
        for key, dest in (("onnx_glob", "model.onnx"), ("tokenizer_glob", "tokenizer.json")):
            hits = glob.glob(str(ex / spec[key]))
            if len(hits) != 1:
                sys.exit(f"{name}: expected exactly one match for {spec[key]}, got {hits}")
            shutil.copy(hits[0], out / dest)
    print(f"{name}: ready in {out}")


if __name__ == "__main__":
    for n in (sys.argv[1:] or list(MODELS)):
        fetch(n)
