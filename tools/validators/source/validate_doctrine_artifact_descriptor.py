#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "schemas" / "contracts" / "v1" / "source" / "doctrine_artifact_descriptor.schema.json"
FIXTURE_ROOT = ROOT / "fixtures" / "contracts" / "v1" / "source" / "doctrine_artifact_descriptor"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_fixtures() -> int:
    schema = _load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    failures: list[str] = []

    for path in sorted((FIXTURE_ROOT / "valid").glob("*.json")):
        errors = sorted(validator.iter_errors(_load_json(path)), key=lambda e: e.path)
        if errors:
            failures.append(f"valid fixture failed: {path}")

    for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
        if path.name.endswith(".expected_error.txt"):
            continue
        errors = sorted(validator.iter_errors(_load_json(path)), key=lambda e: e.path)
        if not errors:
            failures.append(f"invalid fixture unexpectedly passed: {path}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("OK doctrine_artifact_descriptor fixtures")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", action="store_true", help="Validate standard fixture set")
    args = parser.parse_args()

    if args.fixtures:
        return run_fixtures()

    print("No action selected. Use --fixtures.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
