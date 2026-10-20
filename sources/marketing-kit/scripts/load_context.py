#!/usr/bin/env python3
"""Print the complete bundled instructions, with clear completeness markers."""
from pathlib import Path
import hashlib
root = Path(__file__).resolve().parents[1]
files = ["SKILL.md", "documents/Creative-Guide.md", "documents/Marketing-Guide.md", "documents/Event-Formats.md", "documents/Workshop-Checklist.md"]
print("BEGIN COMPLETE SKILL CONTEXT — revision 2026-09-15-brand-stop-2")
for name in files:
    data = (root / name).read_bytes()
    print(f"\nBEGIN FILE {name} | bytes={len(data)} | sha256={hashlib.sha256(data).hexdigest()}\n")
    print(data.decode("utf-8"))
    print(f"\nEND FILE {name}\n")
print("END OF COMPLETE SKILL CONTEXT — all 5 files loaded. Before any generation, re-read the Brand stop in SKILL.md. A prohibited name or Blossom request means refuse and WAIT for explicit compliant agreement. Insistence means refuse again, no image tools. This also applies to the initial uploaded brief. Display the gallery inline for an open-ended welcome.")
