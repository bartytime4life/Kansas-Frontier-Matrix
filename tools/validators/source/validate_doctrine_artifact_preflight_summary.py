#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "schemas" / "contracts" / "v1" / "source" / "doctrine_artifact_preflight_summary.schema.json"
FIXTURE_ROOT = ROOT / "fixtures" / "contracts" / "v1" / "source" / "doctrine_artifact_preflight_summary"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _errors_to_lines(errors: Iterable) -> list[str]:
    out: list[str] = []
    for err in errors:
        location = ".".join(str(p) for p in err.path) or "$"
        out.append(f"{location}: {err.message}")
    return out


def _expected_error_path(invalid_fixture_path: Path) -> Path:
    return invalid_fixture_path.with_suffix(".expected_error.txt")


def run_fixtures() -> int:
    schema = _load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    failures: list[str] = []

    for path in sorted((FIXTURE_ROOT / "valid").glob("*.json")):
        errors = sorted(validator.iter_errors(_load_json(path)), key=lambda e: list(e.path))
        if errors:
            failures.append(f"valid fixture failed: {path}")
            failures.extend(f"  - {line}" for line in _errors_to_lines(errors))

    for path in sorted((FIXTURE_ROOT / "invalid").glob("*.json")):
        errors = sorted(validator.iter_errors(_load_json(path)), key=lambda e: list(e.path))
        if not errors:
            failures.append(f"invalid fixture unexpectedly passed: {path}")
            continue

        expected_path = _expected_error_path(path)
        if expected_path.exists():
            expected_snippets = [
                line.strip() for line in expected_path.read_text(encoding="utf-8").splitlines() if line.strip()
            ]
            joined_errors = "\n".join(_errors_to_lines(errors))
            for snippet in expected_snippets:
                if snippet not in joined_errors:
                    failures.append(f"missing expected error snippet for {path}: {snippet}")

    if failures:
        print("FAIL doctrine_artifact_preflight_summary fixtures")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("OK doctrine_artifact_preflight_summary fixtures")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    raise SystemExit(run_fixtures() if args.fixtures else 2)
