#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from tools.validators.place_name_search_projection_common import (
    FIXTURE_ROOT,
    ROOT,
    Finding,
    Result,
    canonical_spec_hash as _canonical_spec_hash,
    load_fixture_bundle,
    materialize_fixture,
    obj,
    read_object,
    schema_findings,
)
from tools.validators.place_name_search_projection_semantics import semantic_findings

SCOPE = "internal-place-name-search-candidate-projection-only"


def validate_candidate(candidate: Mapping[str, Any]) -> Result:
    return Result(tuple(sorted(set(schema_findings(candidate) + semantic_findings(candidate)))))


def validate_record(path: Path) -> Result:
    candidate, findings = read_object(path)
    return Result(tuple(sorted(set(findings)))) if candidate is None else validate_candidate(candidate)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        bundle = load_fixture_bundle()
        valid, invalid = obj(bundle.get("valid")), obj(bundle.get("invalid"))
    except ValueError:
        return 1
    passed = bool(valid and invalid)
    for name, case in sorted(valid.items()):
        result = validate_candidate(materialize_fixture(case, bundle))
        print(_serialize(FIXTURE_ROOT / "valid" / name, result))
        passed = passed and result.ok
    for name, case in sorted(invalid.items()):
        result = validate_candidate(materialize_fixture(case, bundle))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(item for item in case.get("expected_findings", []) if isinstance(item, str))
        print(_serialize(FIXTURE_ROOT / "invalid" / name, result))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {"actual": actual, "expected": expected, "file": name, "outcome": "FIXTURE_POLARITY_ERROR"},
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate PlaceNameSearchProjection records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return 2 if args.files else run_fixture_profile()
    if not args.files:
        return 2
    code = 0
    for path in args.files:
        result = validate_record(path)
        print(_serialize(path, result))
        code = max(code, 0 if result.ok else (2 if result.error else 1))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
