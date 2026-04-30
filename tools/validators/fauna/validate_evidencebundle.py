#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from jsonschema import Draft202012Validator
from packages.evidence.evidencebundle_hash import compute_spec_hash

SCHEMA_PATH = Path("schemas/contracts/v1/fauna/evidence_bundle.schema.json")
SPEC_HASH_RE = re.compile(r"^sha256:[a-f0-9]{64}$")


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a fauna EvidenceBundle.")
    parser.add_argument("path", nargs="?", help="EvidenceBundle JSON path")
    parser.add_argument("--file", dest="file_path", help="EvidenceBundle JSON path")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])
    target = args.file_path or args.path
    if not target:
        fail("usage: validate_evidencebundle.py [--file] <evidencebundle.json>")

    path = Path(target)
    if not path.exists():
        fail(f"missing EvidenceBundle: {path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    doc = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    if errors:
        for err in errors:
            loc = ".".join(str(p) for p in err.path) or "<root>"
            print(f"DENY: schema error at {loc}: {err.message}", file=sys.stderr)
        sys.exit(1)

    if not doc.get("source_uri"):
        fail("source_uri missing")
    if not doc.get("query_predicate"):
        fail("query_predicate missing")

    spec_hash = doc.get("kfm:spec_hash")
    if not spec_hash:
        fail("kfm:spec_hash missing")
    if not isinstance(spec_hash, str) or not SPEC_HASH_RE.match(spec_hash):
        fail("kfm:spec_hash malformed")

    expected_hash = compute_spec_hash(doc)
    if spec_hash != expected_hash:
        fail("kfm:spec_hash does not match canonical spec hash")

    print(f"ALLOW: valid fauna EvidenceBundle: {path}")


if __name__ == "__main__":
    main()
