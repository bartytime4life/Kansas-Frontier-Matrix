#!/usr/bin/env python3
"""Validate fixture-only distribution and coverage assessment candidates.

Validation is deterministic and local. A coherent candidate returns HOLD,
never ALLOW; it creates no distribution fact, source admission, evidence,
geography authority, policy, review, release, publication, or public-use right.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    canonicalize_json,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/distribution_coverage_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/distribution_coverage_assessment/cases.json"
IDENTITY_PREFIX = "kfm:distribution-coverage:"
SCOPE = "distribution-coverage-assessment-fixture-only-v1"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.outcome == "HOLD" and not self.findings


DERIVED: dict[str, tuple[str, str, str]] = {
    "PRESENT": ("ANSWER", "SOURCE_REPORTS_PRESENT", "DO_NOT_INFER_ABUNDANCE"),
    "EXPLICITLY_ABSENT": ("ANSWER", "SOURCE_EXPLICITLY_REPORTS_ABSENT", "DO_NOT_GENERALIZE_ABSENCE"),
    "NOT_ASSESSED": ("ABSTAIN", "COVERAGE_NOT_ASSESSED", "ASSESS_COVERAGE"),
    "UNKNOWN": ("ABSTAIN", "DISTRIBUTION_UNKNOWN", "DO_NOT_INFER_ABSENCE"),
    "SUPPRESSED": ("DENY", "DISTRIBUTION_SUPPRESSED", "PRESERVE_SUPPRESSION"),
    "DISPUTED": ("ABSTAIN", "DISTRIBUTION_DISPUTED", "RECONCILE_CONFLICTS"),
    "STALE": ("ABSTAIN", "COVERAGE_STALE", "REFRESH_COVERAGE"),
    "OUT_OF_SCOPE": ("ABSTAIN", "SUBJECT_OUT_OF_SCOPE", "DO_NOT_EXTEND_SCOPE"),
}


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: copy.deepcopy(value)
        for key, value in candidate.items()
        if key not in {"assessment_id", "spec_hash"}
    }


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return a copy with deterministic RFC 8785 identity fields."""
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["assessment_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _is_sorted_unique(values: object) -> bool:
    if not isinstance(values, list):
        return False
    keys = [canonicalize_json(value) for value in values]
    return keys == sorted(keys) and len(keys) == len(set(keys))


def derive(candidate: Mapping[str, Any]) -> tuple[str, str, str, str]:
    geography = _mapping(candidate.get("geography_binding"))
    coverage = _mapping(candidate.get("coverage_assessment"))
    assertion = _mapping(candidate.get("distribution_assertion"))

    relation = geography.get("boundary_relation")
    if coverage.get("disclosure_state") == "SUPPRESSED" or relation == "WITHHELD":
        status = "SUPPRESSED"
    elif coverage.get("subject_in_scope") is False:
        status = "OUT_OF_SCOPE"
    elif coverage.get("source_row_state") == "MISSING":
        return "UNKNOWN", "ABSTAIN", "SOURCE_ROW_MISSING", "DO_NOT_INFER_ABSENCE"
    elif relation == "UNRESOLVED":
        return "UNKNOWN", "ABSTAIN", "GEOGRAPHY_BINDING_UNRESOLVED", "RESOLVE_GEOGRAPHY_BINDING"
    elif coverage.get("coverage_current") is False or relation == "SUPERSEDED":
        status = "STALE"
    elif assertion.get("conflicting_assertion_refs"):
        status = "DISPUTED"
    elif coverage.get("assessment_scope") == "NOT_DECLARED":
        status = "NOT_ASSESSED"
    elif coverage.get("mapping_basis") == "EXPLICIT_PRESENT":
        status = "PRESENT"
    elif (
        coverage.get("mapping_basis") == "EXPLICIT_ABSENT"
        and coverage.get("assessment_scope") == "COMPLETE"
        and bool(coverage.get("coverage_effort_evidence_refs"))
    ):
        status = "EXPLICITLY_ABSENT"
    elif coverage.get("mapping_basis") == "EXPLICIT_ABSENT":
        status = "NOT_ASSESSED"
    else:
        status = "UNKNOWN"

    decision, reason, obligation = DERIVED[status]
    return status, decision, reason, obligation


def validate_document(candidate: object) -> Result:
    findings: set[Finding] = set()
    try:
        schema = load_json_file(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (JsonInputError, ValueError, TypeError, RecursionError):
        return Result("DENY", (Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings.update(
        Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path)))
        for error in errors[:100]
    )
    if errors or not isinstance(candidate, Mapping):
        return Result("DENY", tuple(sorted(findings)))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError):
        return Result("DENY", (Finding("CANONICALIZATION_ERROR", "/"),))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    descriptor_ref = candidate.get("source_descriptor_ref")
    descriptor_version = candidate.get("source_descriptor_version")
    if (
        not isinstance(descriptor_ref, str)
        or not isinstance(descriptor_version, str)
        or not descriptor_ref.endswith("@" + descriptor_version)
    ):
        findings.add(Finding("SOURCE_DESCRIPTOR_VERSION_MISMATCH", "/source_descriptor_ref"))

    geography = _mapping(candidate.get("geography_binding"))
    relation = geography.get("boundary_relation")
    crosswalk = geography.get("boundary_crosswalk_ref")
    if relation in {"CROSSWALKED", "SUPERSEDED"} and crosswalk is None:
        findings.add(Finding("GEOGRAPHY_CROSSWALK_REQUIRED", "/geography_binding/boundary_crosswalk_ref"))
    if relation == "EXACT" and crosswalk is not None:
        findings.add(Finding("GEOGRAPHY_CROSSWALK_UNEXPECTED", "/geography_binding/boundary_crosswalk_ref"))
    if relation == "WITHHELD" and geography.get("geography_type") != "SUPPRESSED":
        findings.add(Finding("SUPPRESSED_GEOGRAPHY_TYPE_REQUIRED", "/geography_binding/geography_type"))

    coverage = _mapping(candidate.get("coverage_assessment"))
    native_status = coverage.get("source_native_status")
    mapping_basis = coverage.get("mapping_basis")
    if coverage.get("source_row_state") == "MISSING" and (
        native_status is not None or mapping_basis != "NO_EXPLICIT_STATUS"
    ):
        findings.add(Finding("MISSING_ROW_NATIVE_STATUS_FORBIDDEN", "/coverage_assessment"))
    if mapping_basis == "NO_EXPLICIT_STATUS" and native_status is not None:
        findings.add(Finding("SOURCE_NATIVE_STATUS_MISMATCH", "/coverage_assessment/source_native_status"))
    if mapping_basis in {"EXPLICIT_PRESENT", "EXPLICIT_ABSENT"} and native_status is None:
        findings.add(Finding("SOURCE_NATIVE_STATUS_REQUIRED", "/coverage_assessment/source_native_status"))

    assertion = _mapping(candidate.get("distribution_assertion"))
    for key, values in (
        ("coverage_effort_evidence_refs", coverage.get("coverage_effort_evidence_refs")),
        ("evidence_refs", assertion.get("evidence_refs")),
        ("conflicting_assertion_refs", assertion.get("conflicting_assertion_refs")),
        ("reason_codes", assertion.get("reason_codes")),
        ("obligations", assertion.get("obligations")),
    ):
        if not _is_sorted_unique(values):
            parent = "coverage_assessment" if key == "coverage_effort_evidence_refs" else "distribution_assertion"
            findings.add(Finding("NORMALIZED_COLLECTION_REQUIRED", f"/{parent}/{key}"))

    asserted = _time(assertion.get("asserted_at"))
    assessed = _time(coverage.get("assessed_at"))
    valid_from = _time(assertion.get("valid_from")) if assertion.get("valid_from") is not None else None
    valid_to = _time(assertion.get("valid_to")) if assertion.get("valid_to") is not None else None
    if asserted is None or assessed is None or asserted > assessed:
        findings.add(Finding("DISTRIBUTION_TIME_INVALID", "/distribution_assertion/asserted_at"))
    if valid_from is not None and valid_to is not None and valid_from > valid_to:
        findings.add(Finding("DISTRIBUTION_TIME_INVALID", "/distribution_assertion/valid_from"))

    status, decision, reason, obligation = derive(candidate)
    if assertion.get("status") != status:
        findings.add(Finding("DISTRIBUTION_STATUS_MISMATCH", "/distribution_assertion/status"))
    if assertion.get("decision") != decision:
        findings.add(Finding("DISTRIBUTION_DECISION_MISMATCH", "/distribution_assertion/decision"))
    reasons = assertion.get("reason_codes")
    obligations = assertion.get("obligations")
    if not isinstance(reasons, list) or reason not in reasons:
        findings.add(Finding("DISTRIBUTION_REASON_REQUIRED", "/distribution_assertion/reason_codes"))
    if not isinstance(obligations, list) or obligation not in obligations:
        findings.add(Finding("DISTRIBUTION_OBLIGATION_REQUIRED", "/distribution_assertion/obligations"))

    if status in {"PRESENT", "EXPLICITLY_ABSENT"} and not assertion.get("evidence_refs"):
        findings.add(Finding("DISTRIBUTION_EVIDENCE_REQUIRED", "/distribution_assertion/evidence_refs"))
    if status == "DISPUTED" and not assertion.get("conflicting_assertion_refs"):
        findings.add(Finding("DISTRIBUTION_CONFLICT_REQUIRED", "/distribution_assertion/conflicting_assertion_refs"))

    return Result("DENY" if findings else "HOLD", tuple(sorted(findings)))


def validate_file(path: Path | str) -> Result:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return Result("DENY", (Finding("INPUT_JSON_INVALID", "/"),))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        return Result("DENY", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/")]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent: Any = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list):
        parent[int(parts[-1])] = copy.deepcopy(value)
    else:
        parent[parts[-1]] = copy.deepcopy(value)


def fixture_cases(path: Path = CASES_PATH) -> list[tuple[Mapping[str, Any], Result, str, tuple[str, ...]]]:
    matrix = load_json_file(path)
    if not isinstance(matrix, Mapping) or not isinstance(matrix.get("base"), Mapping) or not isinstance(matrix.get("cases"), list):
        raise ValueError("fixture matrix is invalid")
    base = seal(matrix["base"])
    materialized: list[tuple[Mapping[str, Any], Result, str, tuple[str, ...]]] = []
    for raw_case in matrix["cases"]:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise ValueError("fixture case is invalid")
        candidate = copy.deepcopy(base)
        mutations = raw_case.get("mutations", [])
        if not isinstance(mutations, list):
            raise ValueError("case mutations are invalid")
        for mutation in mutations:
            if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
                raise ValueError("case mutation is invalid")
            _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw_case.get("reseal", True) is True:
            candidate = seal(candidate)
        expected_outcome = raw_case.get("expected_outcome")
        expected_findings = raw_case.get("expected_findings", [])
        if not isinstance(expected_outcome, str) or not isinstance(expected_findings, list) or not all(isinstance(code, str) for code in expected_findings):
            raise ValueError("case expectations are invalid")
        materialized.append((candidate, validate_document(candidate), expected_outcome, tuple(expected_findings)))
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    try:
        cases = fixture_cases(path)
    except (JsonInputError, ValueError, TypeError, KeyError, CanonicalizationFailure):
        print(json.dumps({"scope": SCOPE, "status": "FAIL", "reason": "FIXTURE_MATRIX_INVALID"}, sort_keys=True, separators=(",", ":")))
        return 1
    failures: list[int] = []
    for index, (_candidate, result, expected_outcome, expected_findings) in enumerate(cases):
        codes = {finding.code for finding in result.findings}
        if result.outcome != expected_outcome or not set(expected_findings).issubset(codes):
            failures.append(index)
    print(json.dumps({"cases": len(cases), "failed_case_indexes": failures, "scope": SCOPE, "status": "FAIL" if failures else "PASS"}, sort_keys=True, separators=(",", ":")))
    return 1 if failures else 0


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide candidate files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        print(json.dumps({
            "file": _display(path),
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        }, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
