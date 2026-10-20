"""Copy the bundled gallery to a deliverable location without changing the image."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path, default=Path("/mnt/data"))
args = parser.parse_args()
source = Path(__file__).resolve().parents[1] / "assets" / "Design-Gallery.jpg"
if not source.is_file() or not source.read_bytes().startswith(b"\xff\xd8\xff"):
    raise SystemExit("Gallery image is missing or invalid. Do not claim it was displayed.")
args.output_dir.mkdir(parents=True, exist_ok=True)
target = args.output_dir.resolve() / "Design-Gallery.jpg"
if source.resolve() != target:
    shutil.copyfile(source, target)
if hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(target.read_bytes()).digest():
    raise SystemExit("Gallery copy failed verification.")
result = {"path": str(target), "bytes": target.stat().st_size}
if target.parent == Path("/mnt/data"):
    result["inline_markdown"] = "![Student Collective design gallery](sandbox:/mnt/data/Design-Gallery.jpg)"
else:
    result["next_step"] = "Publish this file with the host file-output tool and embed its returned image URL. This local path alone is not a user-visible attachment."
print(json.dumps(result))
