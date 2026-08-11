"""Validate fixture-only DISTINCT and NULL deduplication assessments.

The validator checks declarations and synthetic summary counts only. It does
not execute SQL, inspect rows, reconcile identity, resolve references, decide
policy or review, or grant release or publication authority.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/distinct_null_deduplication_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/distinct_null_deduplication_assessment/cases.json"
ABSTAIN_CODES = {
    "FIXTURE_NOT_RUN",
    "NULL_EQUIVALENCE_UNRESOLVED",
    "NULL_ROW_POSTURE_UNRESOLVED",
    "OPERATION_KIND_UNRESOLVED",
    "TUPLE_BASIS_UNRESOLVED",
    "USE_CASE_UNRESOLVED",
}
ERROR_CODES = {
    "CANONICALIZATION_FAILED",
    "FIXTURE_RECORDED_ERROR",
    "INPUT_INVALID",
    "NULL_SEMANTICS_RECORDED_ERROR",
    "SCHEMA_INVALID",
}
SQL_OPERATIONS = {"SQL_DISTINCT", "EXPLICIT_GROUP_BY"}

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def compute_profile_hash(candidate: Mapping[str, Any]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return compute_spec_hash(subject)


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(candidate: object) -> list[Finding]:
    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", _json_path(error.absolute_path))
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _null_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    semantics = candidate["null_semantics"]
    assert isinstance(semantics, Mapping)
    row_posture = semantics["row_posture"]
    equivalence = semantics["null_equivalence"]
    basis = semantics["multi_column_basis"]
    fields = candidate["distinct_fields"]
    assert isinstance(fields, list)

    if row_posture == "ERROR" or equivalence == "ERROR":
        findings.add(Finding("NULL_SEMANTICS_RECORDED_ERROR", "$.null_semantics"))
        return findings
    if row_posture == "UNRESOLVED":
        findings.add(Finding("NULL_ROW_POSTURE_UNRESOLVED", "$.null_semantics.row_posture"))
    if equivalence == "UNRESOLVED":
        findings.add(Finding("NULL_EQUIVALENCE_UNRESOLVED", "$.null_semantics.null_equivalence"))
    if basis == "UNRESOLVED":
        findings.add(Finding("TUPLE_BASIS_UNRESOLVED", "$.null_semantics.multi_column_basis"))
    elif len(fields) == 1 and basis != "SINGLE_FIELD":
        findings.add(Finding("SINGLE_FIELD_BASIS_MISMATCH", "$.null_semantics.multi_column_basis"))
    elif len(fields) > 1 and basis != "ORDERED_VALUE_TUPLE":
        findings.add(Finding("MULTI_COLUMN_BASIS_MISMATCH", "$.null_semantics.multi_column_basis"))
    return findings


def _fixture_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    check = candidate["fixture_check"]
    assert isinstance(check, Mapping)
    state = check["state"]
    if state == "ERROR":
        return {Finding("FIXTURE_RECORDED_ERROR", "$.fixture_check.state")}
    if state == "NOT_RUN":
        populated = any(
            check[name] is not None
            for name in (
                "fixture_ref",
                "fixture_digest",
                "expected_distinct_count",
                "observed_distinct_count",
                "receipt_ref",
            )
        )
        coverage = check["coverage"]
        assert isinstance(coverage, Mapping)
        if populated or any(coverage.values()):
            return {Finding("FIXTURE_NOT_RUN_INCOHERENT", "$.fixture_check")}
        return {Finding("FIXTURE_NOT_RUN", "$.fixture_check.state")}

    required = (
        "fixture_ref",
        "fixture_digest",
        "expected_distinct_count",
        "observed_distinct_count",
        "receipt_ref",
    )
    findings: set[Finding] = set()
    if any(check[name] is None for name in required):
        findings.add(Finding("FIXTURE_RESULT_INCOMPLETE", "$.fixture_check"))
        return findings
    coverage = check["coverage"]
    assert isinstance(coverage, Mapping)
    if not coverage["null_rows"]:
        findings.add(Finding("FIXTURE_NULL_COVERAGE_REQUIRED", "$.fixture_check.coverage.null_rows"))
    if not coverage["duplicate_rows"]:
        findings.add(Finding("FIXTURE_DUPLICATE_COVERAGE_REQUIRED", "$.fixture_check.coverage.duplicate_rows"))
    fields = candidate["distinct_fields"]
    assert isinstance(fields, list)
    if len(fields) > 1 and not coverage["multi_column_tuples"]:
        findings.add(Finding("FIXTURE_MULTI_COLUMN_COVERAGE_REQUIRED", "$.fixture_check.coverage.multi_column_tuples"))
    expected = check["expected_distinct_count"]
    observed = check["observed_distinct_count"]
    if state == "MISMATCH" or expected != observed:
        findings.add(Finding("FIXTURE_RESULT_MISMATCH", "$.fixture_check"))
    return findings


def _use_case_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    use_case = candidate["use_case"]
    operation = candidate["operation_kind"]
    adjacent = candidate["adjacent_contracts"]
    assert isinstance(adjacent, Mapping)

    if use_case == "UNRESOLVED":
        findings.add(Finding("USE_CASE_UNRESOLVED", "$.use_case"))
    if operation == "UNRESOLVED":
        findings.add(Finding("OPERATION_KIND_UNRESOLVED", "$.operation_kind"))
    if operation in SQL_OPERATIONS and candidate["dialect_profile_ref"] is None:
        findings.add(Finding("SQL_DIALECT_PROFILE_REQUIRED", "$.dialect_profile_ref"))
    if use_case == "COUNT_POPULATION" and adjacent["count_population_disclosure_ref"] is None:
        findings.add(Finding("COUNT_POPULATION_DISCLOSURE_REQUIRED", "$.adjacent_contracts.count_population_disclosure_ref"))
    if use_case not in {"COUNT_POPULATION", "UNRESOLVED"} and adjacent["count_population_disclosure_ref"] is not None:
        findings.add(Finding("COUNT_POPULATION_REFERENCE_INCOHERENT", "$.adjacent_contracts.count_population_disclosure_ref"))
    if use_case == "ENTITY_MATCH_CANDIDATE":
        if operation != "DETERMINISTIC_RECONCILIATION":
            findings.add(Finding("ENTITY_MATCH_REQUIRES_RECONCILIATION", "$.operation_kind"))
        elif adjacent["reconciliation_contract_ref"] is None:
            findings.add(Finding("RECONCILIATION_CONTRACT_REQUIRED", "$.adjacent_contracts.reconciliation_contract_ref"))
    elif use_case != "UNRESOLVED" and adjacent["reconciliation_contract_ref"] is not None:
        findings.add(Finding("RECONCILIATION_REFERENCE_INCOHERENT", "$.adjacent_contracts.reconciliation_contract_ref"))
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(set(schema_findings))))
    assert isinstance(candidate, Mapping)

    findings: set[Finding] = set()
    if not _is_utc(candidate["assessed_at"]):
        findings.add(Finding("ASSESSED_AT_NOT_UTC", "$.assessed_at"))
    if not _canonical_strings(candidate["distinct_fields"]):
        findings.add(Finding("DISTINCT_FIELDS_NOT_CANONICAL", "$.distinct_fields"))
    disclosure = candidate["disclosure"]
    assert isinstance(disclosure, Mapping)
    if not _canonical_strings(disclosure["review_record_refs"]):
        findings.add(Finding("REVIEW_REFS_NOT_CANONICAL", "$.disclosure.review_record_refs"))
    if disclosure["intended_use"] == "PUBLIC_CANDIDATE" and not disclosure["review_record_refs"]:
        findings.add(Finding("PUBLIC_DISCLOSURE_REVIEW_REQUIRED", "$.disclosure.review_record_refs"))

    findings.update(_null_findings(candidate))
    if "NULL_SEMANTICS_RECORDED_ERROR" not in {item.code for item in findings}:
        findings.update(_fixture_findings(candidate))
        findings.update(_use_case_findings(candidate))

    try:
        if candidate["profile_spec_hash"] != compute_profile_hash(candidate):
            findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "$.profile_spec_hash"))
    except CanonicalizationFailure:
        return ValidationResult("ERROR", (Finding("CANONICALIZATION_FAILED", "$"),))

    codes = {finding.code for finding in findings}
    if codes & ERROR_CODES:
        outcome = "ERROR"
    elif codes - ABSTAIN_CODES:
        outcome = "DENY"
    elif codes:
        outcome = "ABSTAIN"
    else:
        outcome = "PASS"
    return ValidationResult(outcome, tuple(sorted(findings)))


def _deep_merge(base: object, patch: object) -> object:
    if isinstance(base, dict) and isinstance(patch, dict):
        merged = copy.deepcopy(base)
        for key, value in patch.items():
            merged[key] = _deep_merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(patch)


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = _deep_merge(manifest["base_candidate"], case.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if case.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "0" * 64
    return candidate


def load_fixture_manifest() -> dict[str, Any]:
    value = load_json_file(FIXTURE_PATH)
    if not isinstance(value, dict):
        raise JsonInputError("fixture manifest root must be an object")
    return value


def validate_fixture_manifest() -> tuple[tuple[str, str, tuple[str, ...]], ...]:
    manifest = load_fixture_manifest()
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        raise JsonInputError("fixture cases must be an array")
    observed: list[tuple[str, str, tuple[str, ...]]] = []
    for raw_case in cases:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise JsonInputError("fixture case must be a named object")
        candidate = materialize_case(manifest, raw_case)
        result = validate_candidate(candidate)
        expected = raw_case.get("expected")
        if not isinstance(expected, Mapping):
            raise JsonInputError("fixture case expected result must be an object")
        expected_outcome = expected.get("outcome")
        expected_codes = expected.get("codes")
        if result.outcome != expected_outcome or result.codes != expected_codes:
            raise AssertionError(f"fixture polarity mismatch: {raw_case['name']}")
        observed.append((raw_case["name"], result.outcome, tuple(result.codes)))
    return tuple(observed)


def _main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures == (args.candidate is not None):
        parser.error("choose exactly one candidate path or --fixtures")
    try:
        if args.fixtures:
            results = validate_fixture_manifest()
            print(json.dumps({"outcome": "PASS", "cases": len(results)}, sort_keys=True))
            return 0
        value = load_json_file(args.candidate)
        result = validate_candidate(value)
    except (JsonInputError, OSError, AssertionError):
        print(json.dumps({"outcome": "ERROR", "codes": ["INPUT_INVALID"]}, sort_keys=True))
        return 2
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(_main())
