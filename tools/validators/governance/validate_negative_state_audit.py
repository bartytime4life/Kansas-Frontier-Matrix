#!/usr/bin/env python3
"""Validate fixture-only Pass 11 NegativeStateAudit records."""

from __future__ import annotations

import argparse
import copy
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from hashing import CanonicalizationFailure, compute_spec_hash
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/negative_state_audit.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/governance/negative_state_audit/cases.json"
MAX_JSON_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
CASE_KINDS = {
    "APPROVED_ARTIFACT",
    "POLICY_DENIAL",
    "CITATION_OR_VALIDATION_FAILURE",
}


class DuplicateKeyError(ValueError):
    """Raised when a parsed JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON includes a non-standard finite-number violation."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS" and not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_UNREADABLE", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("JSON_ROOT_INVALID", "/")])


def _schema_findings(record: Mapping[str, Any]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = list(islice(Draft202012Validator(schema).iter_errors(record), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _spec_subject(record: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in record.items() if key != "spec_hash"}


def compute_record_spec_hash(record: Mapping[str, Any]) -> str:
    return compute_spec_hash(_spec_subject(record))


def _nonempty_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and len(value) == len(set(value))
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def _approved_case_is_safe(case: Mapping[str, Any]) -> bool:
    return all(
        [
            case.get("public_outcome") == "ANSWER",
            case.get("lifecycle_state") == "PUBLISHED",
            case.get("policy_outcome") == "ALLOW",
            case.get("validation_outcome") == "PASS",
            case.get("citation_outcome") == "PASS",
            isinstance(case.get("artifact_ref"), str),
            _nonempty_strings(case.get("evidence_bundle_refs")),
            isinstance(case.get("policy_decision_ref"), str),
            _nonempty_strings(case.get("validation_report_refs")),
            isinstance(case.get("citation_validation_report_ref"), str),
            isinstance(case.get("release_manifest_ref"), str),
            "failure_report_ref" not in case,
            case.get("reason_codes") == [],
        ]
    )


def _policy_denial_is_safe(case: Mapping[str, Any]) -> bool:
    return all(
        [
            case.get("public_outcome") == "DENY",
            case.get("lifecycle_state") == "QUARANTINE",
            case.get("policy_outcome") == "DENY",
            case.get("validation_outcome") == "NOT_EVALUATED",
            case.get("citation_outcome") == "NOT_EVALUATED",
            isinstance(case.get("policy_decision_ref"), str),
            "artifact_ref" not in case,
            "release_manifest_ref" not in case,
            bool(case.get("reason_codes")),
        ]
    )


def _failure_case_is_safe(case: Mapping[str, Any]) -> bool:
    validation_outcome = case.get("validation_outcome")
    citation_outcome = case.get("citation_outcome")
    has_failure = validation_outcome in {"FAIL", "ERROR"} or citation_outcome in {"FAIL", "ERROR"}
    validation_ref_ok = validation_outcome == "NOT_EVALUATED" or _nonempty_strings(case.get("validation_report_refs"))
    citation_ref_ok = citation_outcome == "NOT_EVALUATED" or isinstance(case.get("citation_validation_report_ref"), str)
    return all(
        [
            case.get("public_outcome") in {"ABSTAIN", "ERROR"},
            case.get("lifecycle_state") in {"WORK", "QUARANTINE"},
            case.get("policy_outcome") in {"ALLOW", "NOT_EVALUATED", "ERROR"},
            has_failure,
            isinstance(case.get("failure_report_ref"), str),
            validation_ref_ok,
            citation_ref_ok,
            "artifact_ref" not in case,
            "release_manifest_ref" not in case,
            bool(case.get("reason_codes")),
        ]
    )


def validate_record(record: Any) -> ValidationResult:
    if not isinstance(record, dict):
        return ValidationResult("ERROR", (Finding("JSON_ROOT_INVALID", "/"),))

    findings = _schema_findings(record)
    if findings:
        return ValidationResult("ERROR", tuple(sorted(findings)))

    try:
        expected_hash = compute_record_spec_hash(record)
    except CanonicalizationFailure:
        return ValidationResult("ERROR", (Finding("SPEC_HASH_CANONICALIZATION_ERROR", "/spec_hash"),))
    if record["spec_hash"] != expected_hash:
        return ValidationResult("ERROR", (Finding("SPEC_HASH_MISMATCH", "/spec_hash"),))

    denied: list[Finding] = []
    if record["deterministic"] is not True:
        denied.append(Finding("DETERMINISM_REQUIRED", "/deterministic"))
    if record["network_access"] is not False:
        denied.append(Finding("NETWORK_ACCESS_FORBIDDEN", "/network_access"))

    cases = record["cases"]
    kinds = [case["case_kind"] for case in cases]
    ids = [case["case_id"] for case in cases]
    if set(kinds) != CASE_KINDS or len(set(kinds)) != 3:
        return ValidationResult("ERROR", (Finding("CASE_MATRIX_INCOMPLETE", "/cases"),))
    if len(set(ids)) != len(ids):
        return ValidationResult("ERROR", (Finding("CASE_ID_DUPLICATE", "/cases"),))

    indexed = {case["case_kind"]: case for case in cases}
    if not _approved_case_is_safe(indexed["APPROVED_ARTIFACT"]):
        denied.append(Finding("APPROVED_CASE_INCOMPLETE", "/cases"))
    if not _policy_denial_is_safe(indexed["POLICY_DENIAL"]):
        denied.append(Finding("POLICY_DENIAL_OVERCLAIM", "/cases"))
    if not _failure_case_is_safe(indexed["CITATION_OR_VALIDATION_FAILURE"]):
        denied.append(Finding("FAILURE_CASE_INCOHERENT", "/cases"))

    derived = "DENY" if denied else "PASS"
    if record["audit_outcome"] != derived:
        denied.append(Finding("AUDIT_OUTCOME_MISMATCH", "/audit_outcome"))
        derived = "DENY"
    return ValidationResult(derived, tuple(sorted(set(denied))))


def evaluate(record: Any) -> str:
    return validate_record(record).outcome


def replay(path: Path = FIXTURES) -> list[tuple[str, str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[tuple[str, str, str]] = []
    for case in data["cases"]:
        actual = evaluate(case["record"])
        if actual != case["expected"]:
            failures.append((case["name"], case["expected"], actual))
    return failures


def _report(result: ValidationResult) -> dict[str, Any]:
    return {
        "authority": "NONE",
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome,
        "publication_authorized": False,
        "scope": "pass11-negative-state-audit",
        "status": "PASS" if result.outcome == "PASS" else "FAIL",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        failures = replay()
        if failures:
            for name, expected, actual in failures:
                print(json.dumps({"actual": actual, "expected": expected, "name": name}, sort_keys=True))
            return 1
        print(json.dumps({"cases": 7, "scope": "pass11-negative-state-audit", "status": "PASS"}, sort_keys=True))
        return 0

    if args.path is None:
        parser.error("path required unless --fixtures is used")
    record, findings = _load_object(args.path)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if record is None
        else validate_record(record)
    )
    print(json.dumps(_report(result), sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
