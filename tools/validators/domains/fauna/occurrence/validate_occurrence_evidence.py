#!/usr/bin/env python3
"""Validate the draft KFM Fauna OccurrenceEvidence machine profile.

The validator is deterministic, no-network, fixture-first, and non-authoritative.
A PASS means only that the declared object satisfies the draft schema and the
bounded semantic checks in this module. It does not admit a source, resolve an
EvidenceBundle, approve policy or steward review, release data, or publish an
occurrence.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[5]
HASH_SRC = ROOT / "packages" / "hashing" / "src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

try:
    from hashing import JsonInputError, compute_spec_hash, load_json_file
except ImportError as exc:  # pragma: no cover - exercised as a fail-closed CLI path
    JsonInputError = ValueError  # type: ignore[assignment]
    _HASH_IMPORT_ERROR: Exception | None = exc
else:
    _HASH_IMPORT_ERROR = None

SCHEMA_PATH = (
    ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "domains"
    / "fauna"
    / "occurrence_evidence.schema.json"
)
FIXTURE_ROOT = ROOT / "fixtures" / "domains" / "fauna" / "occurrence_evidence"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
SCOPE = "fauna-occurrence-evidence-draft-v1"
FAUNA_SRC = ROOT / "packages" / "domains" / "fauna" / "src"
if str(FAUNA_SRC) not in sys.path:
    sys.path.insert(0, str(FAUNA_SRC))

from fauna.identity import compute_occurrence_spec_hash, occurrence_identity_subject
from fauna.validation import Finding, ValidationResult, validate_candidate as _validate_candidate


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code, path)
    if finding not in findings:
        findings.append(finding)


def _load_schema() -> Mapping[str, Any]:
    if _HASH_IMPORT_ERROR is not None:
        raise RuntimeError("hashing package unavailable") from _HASH_IMPORT_ERROR
    schema = load_json_file(SCHEMA_PATH)
    if not isinstance(schema, Mapping):
        raise RuntimeError("schema root is not an object")
    Draft202012Validator.check_schema(schema)
    return schema


def validate_candidate(candidate: object) -> ValidationResult:
    """Compatibility entrypoint using the canonical repository schema."""
    if not isinstance(candidate, Mapping):
        return ValidationResult((Finding("schema.root_not_object", "/"),))
    try:
        schema = _load_schema()
    except (OSError, UnicodeError, ValueError, RuntimeError, RecursionError):
        return ValidationResult((Finding("schema.unavailable", "/"),))
    return _validate_candidate(candidate, schema=schema)


def validate_file(path: Path | str) -> ValidationResult:
    """Load and validate one bounded JSON file."""

    if _HASH_IMPORT_ERROR is not None:
        return ValidationResult((Finding("schema.hashing_unavailable", "/"),))
    try:
        candidate = load_json_file(Path(path))
    except JsonInputError:
        return ValidationResult((Finding("schema.input_invalid", "/"),))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.input_error", "/"),))
    return validate_candidate(candidate)


def validate_fixture_manifest() -> ValidationResult:
    """Replay every declared fixture and compare exact expected findings."""

    if _HASH_IMPORT_ERROR is not None:
        return ValidationResult((Finding("schema.hashing_unavailable", "/"),))
    try:
        manifest = load_json_file(MANIFEST_PATH)
    except (JsonInputError, OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/"),))
    if not isinstance(manifest, Mapping):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/"),))

    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return ValidationResult((Finding("schema.fixture_manifest_invalid", "/cases"),))

    findings: list[Finding] = []
    declared_paths: list[str] = []
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            _add(findings, "schema.fixture_case_invalid", f"/cases/{index}")
            continue
        relative_path = case.get("path")
        expected = case.get("expected_findings")
        if not isinstance(relative_path, str) or not isinstance(expected, list):
            _add(findings, "schema.fixture_case_invalid", f"/cases/{index}")
            continue
        declared_paths.append(relative_path)
        fixture_path = FIXTURE_ROOT / relative_path
        actual = validate_file(fixture_path).findings
        expected_pairs: list[Finding] = []
        for expected_index, item in enumerate(expected):
            if not isinstance(item, Mapping):
                _add(
                    findings,
                    "schema.fixture_expectation_invalid",
                    f"/cases/{index}/expected_findings/{expected_index}",
                )
                continue
            code = item.get("code")
            path = item.get("path")
            if not isinstance(code, str) or not isinstance(path, str):
                _add(
                    findings,
                    "schema.fixture_expectation_invalid",
                    f"/cases/{index}/expected_findings/{expected_index}",
                )
                continue
            expected_pairs.append(Finding(code, path))
        if tuple(sorted(expected_pairs)) != actual:
            _add(
                findings,
                "schema.fixture_outcome_mismatch",
                f"/cases/{index}",
            )

    if declared_paths != sorted(set(declared_paths)):
        _add(findings, "schema.fixture_paths_not_canonical", "/cases")

    actual_paths = sorted(
        str(path.relative_to(FIXTURE_ROOT))
        for folder in (FIXTURE_ROOT / "valid", FIXTURE_ROOT / "semantic_invalid")
        for path in folder.glob("*.json")
    )
    if declared_paths != actual_paths:
        _add(findings, "schema.fixture_inventory_mismatch", "/cases")

    return ValidationResult(tuple(sorted(set(findings))))


def _payload(path: str, result: ValidationResult) -> dict[str, Any]:
    return {
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "input": path,
        "outcome": result.outcome,
        "scope": SCOPE,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate draft Fauna OccurrenceEvidence JSON without network."
    )
    parser.add_argument("paths", nargs="*", help="JSON files to validate")
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="replay the exact fixture manifest",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        result = validate_fixture_manifest()
        print(json.dumps(_payload("fixture-manifest", result), sort_keys=True))
        return 0 if result.ok else 1
    if not args.paths:
        build_parser().error("provide at least one path or --fixtures")

    exit_code = 0
    for raw_path in args.paths:
        result = validate_file(Path(raw_path))
        print(json.dumps(_payload(raw_path, result), sort_keys=True))
        if not result.ok:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
