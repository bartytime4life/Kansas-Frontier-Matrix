#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/evidence/gbif_evidencebundle.schema.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    args = ap.parse_args()
    doc = json.loads(Path(args.path).read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(doc), key=lambda e: list(e.path))
    if errors:
        for e in errors:
            loc = ".".join(str(p) for p in e.path) or "<root>"
            print(f"DENY: {loc}: {e.message}", file=sys.stderr)
        sys.exit(1)
    print("ALLOW")

if __name__ == "__main__":
    main()
