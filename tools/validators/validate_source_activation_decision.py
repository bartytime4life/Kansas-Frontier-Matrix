"""Validate proposed KFM SourceActivationDecision records without network access.

A passing result proves only bounded shape and local consistency. It does not
resolve policy or review references, activate a source, write lifecycle state,
emit an IngestReceipt, release, or publish.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._source_activation.io import (
    Finding,
    MAX_FILE_BYTES,
    MAX_JSON_DEPTH,
    MAX_SCHEMA_FINDINGS,
    ValidationResult,
    load_schema_validator,
    mapping,
    read_json_object,
    schema_findings,
)
from tools.validators._source_activation.semantics import semantic_findings

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_activation_decision.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_activation_decision"


def validate_decision(path: Path) -> ValidationResult:
    candidate, findings = read_json_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(findings)), None, None)
    try:
        validator = load_schema_validator(SCHEMA_PATH)
    except (OSError, UnicodeError, ValueError):
        return ValidationResult((Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be loaded"),), None, None)
    findings.extend(schema_findings(validator, candidate))
    findings.extend(semantic_findings(candidate))
    decision = mapping(candidate.get("decision"))
    route = decision.get("route")
    state = decision.get("activation_state")
    return ValidationResult(
        tuple(sorted(set(findings))),
        route if isinstance(route, str) else None,
        state if isinstance(state, str) else None,
    )


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": "source-activation-decision-shape-routing-and-lineage-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_codes(path: Path) -> tuple[str, ...]:
    sidecar = path.with_suffix(".expected_findings.txt")
    if sidecar.is_file():
        return tuple(sorted(line.strip() for line in sidecar.read_text(encoding="utf-8").splitlines() if line.strip()))
    try:
        manifest = json.loads((path.parent / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ()
    value = manifest.get(path.name) if isinstance(manifest, dict) else None
    return tuple(sorted(item for item in value if isinstance(item, str) and item)) if isinstance(value, list) else ()


def _fixture_files(directory: Path) -> list[Path]:
    return sorted(
        (path for path in directory.glob("*.json") if path.name.startswith(("valid_", "invalid_"))),
        key=lambda path: path.as_posix(),
    )


def _validate_lane(directory: Path, expect_valid: bool) -> bool:
    files = _fixture_files(directory)
    if not files:
        print(json.dumps({"file": directory.as_posix(), "findings": [{"code": "FIXTURE_LANE_EMPTY", "field": "/"}], "outcome": "FAIL"}, sort_keys=True, separators=(",", ":")))
        return False
    ok = True
    for path in files:
        result = validate_decision(path)
        print(_serialize(path, result))
        if expect_valid:
            ok = result.ok and ok
            continue
        expected = _expected_codes(path)
        actual = tuple(sorted({finding.code for finding in result.findings}))
        if result.ok or not expected or actual != expected:
            ok = False
            print(json.dumps({"actual": actual, "expected": expected, "file": path.as_posix(), "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    return ok


def run_fixture_profile() -> int:
    passed = all(
        (
            _validate_lane(FIXTURE_ROOT / "valid", True),
            _validate_lane(FIXTURE_ROOT / "invalid", False),
            _validate_lane(FIXTURE_ROOT / "semantic_invalid", False),
        )
    )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM SourceActivationDecision records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_decision(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
