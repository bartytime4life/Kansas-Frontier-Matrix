#!/usr/bin/env python3
"""Validate fixture-only distribution and coverage assessments.

The validator is deterministic and local. A coherent candidate returns HOLD,
never ALLOW; it creates no occurrence or absence fact, source, policy, review,
release, publication, or public-use authority.
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
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/distribution_coverage_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/distribution_coverage_assessment/cases.json"
IDENTITY_PREFIX = "kfm:distribution-coverage:"
SCOPE = "distribution-coverage-fixture-only-v1"


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


DERIVED: dict[str, tuple[str, str, str, str]] = {
    "PRESENT": ("ASSESSED", "ANSWER", "SOURCE_REPORTS_PRESENT", "DO_NOT_INFER_ABUNDANCE"),
    "EXPLICITLY_ABSENT": (
        "ASSESSED",
        "ANSWER",
        "SOURCE_REPORTS_EXPLICITLY_ABSENT",
        "DO_NOT_INFER_TRUE_ABSENCE",
    ),
    "NOT_ASSESSED": ("NOT_ASSESSED", "ABSTAIN", "SOURCE_NOT_ASSESSED", "PRESERVE_NOT_ASSESSED"),
    "UNKNOWN": ("UNKNOWN", "ABSTAIN", "SOURCE_STATUS_UNKNOWN", "RESOLVE_SOURCE_STATUS"),
    "SUPPRESSED": ("SUPPRESSED", "DENY", "SOURCE_STATUS_SUPPRESSED", "WITHHOLD_RESTRICTED_DETAIL"),
    "STALE": ("STALE", "ABSTAIN", "SOURCE_COVERAGE_STALE", "REFRESH_BEFORE_CONSEQUENTIAL_USE"),
    "MISSING_ROW": ("MISSING_ROW", "ABSTAIN", "SOURCE_ROW_MISSING", "DO_NOT_TREAT_MISSING_AS_ABSENCE"),
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


def _canonical_unique_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _derive(candidate: Mapping[str, Any]) -> tuple[str, str, str, str]:
    source = _mapping(candidate.get("source_assertion"))
    geography = _mapping(candidate.get("geography_binding"))
    conflicts = candidate.get("conflict_assertion_refs")
    if isinstance(conflicts, list) and conflicts:
        return (
            "CONFLICTED",
            "ABSTAIN",
            "SOURCE_CONFLICT_UNRESOLVED",
            "RESOLVE_SOURCE_CONFLICT",
        )
    if geography.get("boundary_relation") in {"CHANGED", "UNRESOLVED"}:
        return (
            "GEOGRAPHY_UNRESOLVED",
            "ABSTAIN",
            "GEOGRAPHY_VERSION_UNRESOLVED",
            "RESOLVE_GEOGRAPHY_BINDING",
        )
    return DERIVED.get(
        str(source.get("row_state")),
        ("UNKNOWN", "ABSTAIN", "SOURCE_STATUS_UNKNOWN", "RESOLVE_SOURCE_STATUS"),
    )


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
    findings.update(Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path))) for error in errors[:100])
    if errors or not isinstance(candidate, Mapping):
        return Result("DENY", tuple(sorted(findings)))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return Result("DENY", tuple(sorted(findings)))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    source = _mapping(candidate.get("source_assertion"))
    geography = _mapping(candidate.get("geography_binding"))
    coverage = _mapping(candidate.get("coverage_assessment"))

    row_state = source.get("row_state")
    record_ref = source.get("source_record_ref")
    native_status = source.get("source_native_status")
    if row_state == "MISSING_ROW":
        if record_ref is not None:
            findings.add(Finding("MISSING_ROW_HAS_RECORD_REF", "/source_assertion/source_record_ref"))
        if native_status is not None:
            findings.add(Finding("MISSING_ROW_HAS_NATIVE_STATUS", "/source_assertion/source_native_status"))
    else:
        if record_ref is None:
            findings.add(Finding("SOURCE_RECORD_REF_REQUIRED", "/source_assertion/source_record_ref"))
        if native_status is None:
            findings.add(Finding("SOURCE_NATIVE_STATUS_REQUIRED", "/source_assertion/source_native_status"))

    first_observed = source.get("first_observed_at")
    first_support = source.get("first_observed_support_ref")
    if first_observed is not None:
        if row_state != "PRESENT":
            findings.add(Finding("FIRST_OBSERVED_STATE_UNSUPPORTED", "/source_assertion/first_observed_at"))
        if first_support is None:
            findings.add(Finding("FIRST_OBSERVED_SUPPORT_REQUIRED", "/source_assertion/first_observed_support_ref"))
    elif first_support is not None:
        findings.add(Finding("FIRST_OBSERVED_TIME_REQUIRED", "/source_assertion/first_observed_at"))

    valid_from = _time(source.get("source_valid_from")) if source.get("source_valid_from") is not None else None
    valid_to = _time(source.get("source_valid_to")) if source.get("source_valid_to") is not None else None
    first_time = _time(first_observed) if first_observed is not None else None
    evaluated = _time(candidate.get("evaluated_at"))
    if evaluated is None:
        findings.add(Finding("EVALUATED_TIME_INVALID", "/evaluated_at"))
    if source.get("source_valid_from") is not None and valid_from is None:
        findings.add(Finding("SOURCE_VALID_FROM_INVALID", "/source_assertion/source_valid_from"))
    if source.get("source_valid_to") is not None and valid_to is None:
        findings.add(Finding("SOURCE_VALID_TO_INVALID", "/source_assertion/source_valid_to"))
    if first_observed is not None and first_time is None:
        findings.add(Finding("FIRST_OBSERVED_TIME_INVALID", "/source_assertion/first_observed_at"))
    if valid_from is not None and valid_to is not None and valid_from > valid_to:
        findings.add(Finding("SOURCE_VALID_INTERVAL_INVALID", "/source_assertion"))
    if valid_to is not None and evaluated is not None and valid_to > evaluated:
        findings.add(Finding("SOURCE_VALIDITY_AFTER_EVALUATION", "/evaluated_at"))
    if first_time is not None and evaluated is not None and first_time > evaluated:
        findings.add(Finding("FIRST_OBSERVED_AFTER_EVALUATION", "/source_assertion/first_observed_at"))

    assertion_ref = source.get("assertion_ref")
    supersedes = source.get("supersedes_assertion_ref")
    if supersedes is not None and supersedes == assertion_ref:
        findings.add(Finding("SELF_SUPERSESSION", "/source_assertion/supersedes_assertion_ref"))
    evidence_refs = source.get("evidence_bundle_refs")
    if not _canonical_unique_strings(evidence_refs):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/source_assertion/evidence_bundle_refs"))
    conflicts = candidate.get("conflict_assertion_refs")
    if not _canonical_unique_strings(conflicts):
        findings.add(Finding("CONFLICT_REFS_NOT_CANONICAL", "/conflict_assertion_refs"))
    elif isinstance(conflicts, list) and assertion_ref in conflicts:
        findings.add(Finding("SELF_CONFLICT", "/conflict_assertion_refs"))

    method = geography.get("binding_method")
    relation = geography.get("boundary_relation")
    fips_code = geography.get("fips_code")
    crosswalk_ref = geography.get("crosswalk_ref")
    if method == "FIPS":
        if fips_code is None:
            findings.add(Finding("FIPS_CODE_REQUIRED", "/geography_binding/fips_code"))
        if crosswalk_ref is not None:
            findings.add(Finding("FIPS_CROSSWALK_UNEXPECTED", "/geography_binding/crosswalk_ref"))
        if relation == "CROSSWALKED":
            findings.add(Finding("FIPS_RELATION_INVALID", "/geography_binding/boundary_relation"))
    elif method == "BOUNDARY_CROSSWALK":
        if crosswalk_ref is None:
            findings.add(Finding("CROSSWALK_REF_REQUIRED", "/geography_binding/crosswalk_ref"))
        if fips_code is not None:
            findings.add(Finding("CROSSWALK_FIPS_UNEXPECTED", "/geography_binding/fips_code"))
        if relation != "CROSSWALKED":
            findings.add(Finding("CROSSWALK_RELATION_REQUIRED", "/geography_binding/boundary_relation"))
    elif method == "SOURCE_NATIVE":
        if geography.get("source_geography_ref") != geography.get("canonical_geography_ref"):
            findings.add(Finding("SOURCE_NATIVE_GEOGRAPHY_MISMATCH", "/geography_binding"))
        if fips_code is not None or crosswalk_ref is not None or relation != "EXACT":
            findings.add(Finding("SOURCE_NATIVE_BINDING_INVALID", "/geography_binding"))

    derived_state, derived_decision, reason, obligation = _derive(candidate)
    if coverage.get("coverage_state") != derived_state:
        findings.add(Finding("COVERAGE_STATE_MISMATCH", "/coverage_assessment/coverage_state"))
    if coverage.get("decision") != derived_decision:
        findings.add(Finding("COVERAGE_DECISION_MISMATCH", "/coverage_assessment/decision"))
    reasons = coverage.get("reason_codes")
    obligations = coverage.get("obligations")
    if not isinstance(reasons, list) or reason not in reasons:
        findings.add(Finding("COVERAGE_REASON_REQUIRED", "/coverage_assessment/reason_codes"))
    if not isinstance(obligations, list) or obligation not in obligations:
        findings.add(Finding("COVERAGE_OBLIGATION_REQUIRED", "/coverage_assessment/obligations"))

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
    failures = []
    for index, (_candidate, result, expected_outcome, expected_findings) in enumerate(cases):
        codes = {finding.code for finding in result.findings}
        if result.outcome != expected_outcome or not set(expected_findings).issubset(codes):
            failures.append(index)
    payload = {"cases": len(cases), "failed_case_indexes": failures, "scope": SCOPE, "status": "FAIL" if failures else "PASS"}
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
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
        parser.error("provide assessment files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        payload = {
            "file": _display(path),
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
