#!/usr/bin/env python3
"""Validate and optionally recompute the common KFM ``spec_hash`` contract.

The current executable grammar remains ``sha256:<64 lowercase hex>``. RFC 8785
JCS is the canonicalization profile used when a subject is supplied. This tool
creates no evidence, policy, review, promotion, release, publication, or public-
use authority.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(PACKAGE_SRC))

from hashing import (  # noqa: E402
    CANONICALIZATION_PROFILE,
    HASH_ALGORITHM,
    CanonicalizationFailure,
    JsonInputError,
    load_json_file,
    verify_spec_hash,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/spec_hash.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/common/spec_hash"
SCOPE = "common.spec_hash"
NON_EFFECTS = [
    "no_source_admission",
    "no_evidence_resolution",
    "no_policy_evaluation",
    "no_promotion_release_or_publication",
    "no_public_use_authority",
]


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    expected: str | None = None
    actual: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        if not self.findings:
            return "PASS"
        error_codes = {
            "CANONICALIZATION_ERROR",
            "CANDIDATE_JSON_INVALID",
            "SCHEMA_UNAVAILABLE",
            "SUBJECT_JSON_INVALID",
        }
        return "ERROR" if any(item.code in error_codes for item in self.findings) else "DENY"


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_document(candidate: Any, *, subject: Any | None = None) -> ValidationResult:
    findings: set[Finding] = set()
    try:
        validator = _load_schema_validator()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return ValidationResult((Finding("SCHEMA_UNAVAILABLE", "/"),))

    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
    )
    for error in errors:
        findings.add(Finding("SPEC_HASH_SCHEMA_INVALID", _pointer(tuple(error.absolute_path))))

    expected: str | None = None
    actual: str | None = None
    if not findings and subject is not None and isinstance(candidate, dict):
        expected_value = candidate.get("value")
        if isinstance(expected_value, str):
            expected = expected_value
            try:
                comparison = verify_spec_hash(subject, expected_value)
                actual = comparison.actual
                if not comparison.matches:
                    findings.add(Finding("SPEC_HASH_MISMATCH", "/value"))
            except CanonicalizationFailure:
                findings.add(Finding("CANONICALIZATION_ERROR", "/subject"))

    return ValidationResult(tuple(sorted(findings)), expected=expected, actual=actual)


def validate_file(candidate_path: Path, *, subject_path: Path | None = None) -> ValidationResult:
    try:
        candidate = load_json_file(candidate_path)
    except JsonInputError:
        return ValidationResult((Finding("CANDIDATE_JSON_INVALID", "/"),))

    subject: Any | None = None
    if subject_path is not None:
        try:
            subject = load_json_file(subject_path)
        except JsonInputError:
            return ValidationResult((Finding("SUBJECT_JSON_INVALID", "/subject"),))
    return validate_document(candidate, subject=subject)


def validate_fixture_tree(fixture_root: Path = FIXTURE_ROOT) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    valid_paths = sorted((fixture_root / "valid").glob("*.json"))
    invalid_paths = sorted((fixture_root / "invalid").glob("*.json"))
    if not valid_paths:
        findings.add(Finding("VALID_FIXTURES_MISSING", "/valid"))
    if not invalid_paths:
        findings.add(Finding("INVALID_FIXTURES_MISSING", "/invalid"))
    for path in valid_paths:
        if not validate_file(path).ok:
            findings.add(Finding("VALID_FIXTURE_REJECTED", f"/valid/{path.name}"))
    for path in invalid_paths:
        if validate_file(path).ok:
            findings.add(Finding("INVALID_FIXTURE_ACCEPTED", f"/invalid/{path.name}"))
    return tuple(sorted(findings))


def _report(result: ValidationResult, *, file: Path | None = None) -> dict[str, object]:
    payload: dict[str, object] = {
        "authority": "NONE",
        "canonicalization": CANONICALIZATION_PROFILE,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "hash_algorithm": HASH_ALGORITHM,
        "non_effects": NON_EFFECTS,
        "outcome": result.outcome,
        "scope": SCOPE,
    }
    if file is not None:
        payload["file"] = str(file)
    if result.expected is not None:
        payload["expected"] = result.expected
    if result.actual is not None:
        payload["actual"] = result.actual
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate current spec-hash shape and optional RFC 8785 recomputation."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--fixtures", action="store_true")
    mode.add_argument("--candidate", type=Path)
    parser.add_argument("--subject", type=Path)
    parser.add_argument("--fixture-root", type=Path, default=FIXTURE_ROOT)
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.subject is not None:
            parser.error("--subject cannot be combined with --fixtures")
        result = ValidationResult(validate_fixture_tree(args.fixture_root))
        file = args.fixture_root
    else:
        assert args.candidate is not None
        result = validate_file(args.candidate, subject_path=args.subject)
        file = args.candidate

    print(json.dumps(_report(result, file=file), sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
