#!/usr/bin/env python3
"""Validate proposed CatalogClosurePacket records without network access.

The validator checks only packet shape and internal readiness relationships.
A PASS does not create evidence/proof closure, approve policy or review, or
authorize promotion, release, publication, or public use.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/catalog_closure_packet.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/data/catalog_closure_packet"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "catalog-closure-readiness-only"
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_COMPLEXITY_LIMIT",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "JSON_NOT_UTF8",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON uses NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"

    @property
    def error(self) -> bool:
        return self.outcome == "ERROR"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _sorted_unique_strings(values: list[Any]) -> bool:
    return (
        all(isinstance(item, str) for item in values)
        and values == sorted(set(values))
    )


def _canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    scope = _mapping(candidate.get("scope"))
    records = _array(candidate.get("catalog_records"))
    policy = _mapping(candidate.get("policy"))
    review = _mapping(candidate.get("review"))
    release = _mapping(candidate.get("release"))
    governance = _mapping(candidate.get("governance"))

    supplied_hash = candidate.get("spec_hash")
    if isinstance(supplied_hash, str):
        try:
            expected_hash = _canonical_spec_hash(candidate)
        except (TypeError, ValueError, RecursionError):
            expected_hash = None
        if expected_hash is not None and supplied_hash != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    record_types = [
        item.get("record_type") for item in records if isinstance(item, dict)
    ]
    if record_types != sorted(record_types) or len(record_types) != len(set(record_types)):
        findings.append(Finding("CATALOG_RECORDS_NOT_CANONICAL", "/catalog_records"))
    if set(record_types) != {"DCAT", "PROV", "STAC"}:
        findings.append(Finding("CATALOG_FAMILY_INCOMPLETE", "/catalog_records"))

    artifact_id = scope.get("artifact_id")
    artifact_digest = scope.get("artifact_digest")
    release_candidate_ref = release.get("release_candidate_ref")
    for index, item in enumerate(records):
        if not isinstance(item, dict):
            continue
        if item.get("artifact_id") != artifact_id:
            findings.append(
                Finding("CATALOG_IDENTITY_MISMATCH", f"/catalog_records/{index}/artifact_id")
            )
        if item.get("artifact_digest") != artifact_digest:
            findings.append(
                Finding("CATALOG_DIGEST_MISMATCH", f"/catalog_records/{index}/artifact_digest")
            )
        if item.get("release_candidate_ref") != release_candidate_ref:
            findings.append(
                Finding(
                    "CATALOG_RELEASE_REF_MISMATCH",
                    f"/catalog_records/{index}/release_candidate_ref",
                )
            )
        if item.get("resolved") is not True:
            findings.append(
                Finding("CATALOG_RECORD_UNRESOLVED", f"/catalog_records/{index}/resolved")
            )

    for field in (
        "source_descriptor_refs",
        "evidence_refs",
        "validation_report_refs",
    ):
        if not _sorted_unique_strings(_array(candidate.get(field))):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/{field}"))
    if not _sorted_unique_strings(_array(release.get("correction_refs"))):
        findings.append(Finding("REFS_NOT_CANONICAL", "/release/correction_refs"))

    policy_outcome = policy.get("outcome")
    policy_ref = policy.get("policy_decision_ref")
    rights_resolved = policy.get("rights_resolved")
    sensitivity_resolved = policy.get("sensitivity_resolved")
    if policy_outcome == "ALLOW":
        if (
            not isinstance(policy_ref, str)
            or rights_resolved is not True
            or sensitivity_resolved is not True
        ):
            findings.append(Finding("POLICY_ALLOW_INCONSISTENT", "/policy"))
    elif policy_outcome == "HOLD":
        if (
            not isinstance(policy_ref, str)
            or (rights_resolved is True and sensitivity_resolved is True)
        ):
            findings.append(Finding("POLICY_HOLD_INCONSISTENT", "/policy"))
    elif policy_outcome == "DENY":
        if not isinstance(policy_ref, str):
            findings.append(Finding("POLICY_DENY_INCONSISTENT", "/policy"))

    review_state = review.get("state")
    review_ref = review.get("review_record_ref")
    if review_state in {"APPROVED", "REJECTED"}:
        if not isinstance(review_ref, str):
            findings.append(Finding("REVIEW_STATE_INCONSISTENT", "/review"))
    elif review_state in {"NOT_REQUIRED", "PENDING"} and review_ref is not None:
        findings.append(Finding("REVIEW_STATE_INCONSISTENT", "/review"))

    transition = scope.get("requested_transition")
    if transition == "RELEASE_REVIEW":
        if not isinstance(release_candidate_ref, str) or not isinstance(
            release.get("rollback_ref"), str
        ):
            findings.append(Finding("RELEASE_READINESS_INCOMPLETE", "/release"))

    authority_flags = (
        "proof_closed",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
        "public_use_allowed",
    )
    if any(governance.get(field) is not False for field in authority_flags):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def _derive_outcome(candidate: Mapping[str, Any], findings: Sequence[Finding]) -> str:
    if any(item.code in ERROR_CODES for item in findings):
        return "ERROR"
    if findings:
        return "FAIL"
    policy = _mapping(candidate.get("policy"))
    review = _mapping(candidate.get("review"))
    if policy.get("outcome") == "DENY" or review.get("state") == "REJECTED":
        return "DENY"
    if policy.get("outcome") == "HOLD" or review.get("state") == "PENDING":
        return "HOLD"
    return "PASS"


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult(_derive_outcome({}, ordered), ordered)
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_derive_outcome(candidate, ordered), ordered)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(directory.glob(f"{prefix}*.json"), key=lambda path: path.as_posix())


def _load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_root = FIXTURE_ROOT / "valid"
    invalid_root = FIXTURE_ROOT / "invalid"
    valid_files = _fixture_files(valid_root, "valid_")
    invalid_files = _fixture_files(invalid_root, "invalid_")
    outcomes = _load_json_object(valid_root / "expected_outcomes.json")
    findings_manifest = _load_json_object(
        invalid_root / "expected_findings_manifest.json"
    )
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = validate_record(path)
        print(_serialize(path, result))
        expected = outcomes.get(path.name)
        if result.findings or result.outcome != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": {
                            "outcome": result.outcome,
                            "findings": sorted(
                                {item.code for item in result.findings}
                            ),
                        },
                        "expected": {"outcome": expected, "findings": []},
                        "file": _display_path(path),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )

    for path in invalid_files:
        result = validate_record(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        expected = sorted(findings_manifest.get(path.name, []))
        if result.outcome != "FAIL" or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": {"outcome": result.outcome, "findings": actual},
                        "expected": {"outcome": "FAIL", "findings": expected},
                        "file": _display_path(path),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )

    if set(outcomes) != {path.name for path in valid_files}:
        passed = False
    if set(findings_manifest) != {path.name for path in invalid_files}:
        passed = False
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate CatalogClosurePacket records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        return run_fixture_profile()
    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2

    exit_code = 0
    blocking = {"FAIL": 1, "ERROR": 2, "HOLD": 3, "DENY": 4}
    for path in args.files:
        result = validate_record(path)
        print(_serialize(path, result))
        exit_code = max(exit_code, blocking.get(result.outcome, 0))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
