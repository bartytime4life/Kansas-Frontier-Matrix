#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

REQUIRED = [
    Path("data/catalog/README.md"),
    Path("data/catalog/stac/README.md"),
    Path("data/catalog/dcat/README.md"),
    Path("data/catalog/prov/README.md"),
]

missing = [str(p) for p in REQUIRED if not p.exists()]

if missing:
    print("catalog_validate: missing required scaffold paths:", file=sys.stderr)
    for path in missing:
        print(f"- {path}", file=sys.stderr)
    sys.exit(1)

print("catalog_validate: required catalog README scaffold is present")
