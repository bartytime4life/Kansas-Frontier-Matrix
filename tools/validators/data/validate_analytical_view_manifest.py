"""Validate fixture-only analytical view manifests.

This validator checks declaration coherence only. It does not parse or execute
SQL, connect to a database, create a view, refresh data, authenticate carried
references, decide policy or review, or grant release authority.
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

REPO_ROOT = Path(__file__).resolve().parents[3]
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

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/analytical_view_manifest.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/data/analytical_view_manifest/cases.json"
ABSTAIN_CODES = {
    "MUTATION_POSTURE_UNRESOLVED",
    "VALIDATION_PARTIAL",
    "VIEW_KIND_UNRESOLVED",
    "VIEW_NOT_VALIDATED",
}
ERROR_CODES = {
    "CANONICALIZATION_FAILED",
    "INPUT_INVALID",
    "SCHEMA_INVALID",
    "VALIDATION_RECORDED_ERROR",
}
GUARD_MODES = {"LOCAL", "CASCADED", "EQUIVALENT_GUARD"}
CANONICAL_ARRAY_PATHS = (
    ("upstream", "dataset_refs", "UPSTREAM_REFS_NOT_CANONICAL"),
    ("semantic_dependencies", "join_assessment_refs", "JOIN_REFS_NOT_CANONICAL"),
    ("semantic_dependencies", "aggregate_disclosure_refs", "AGGREGATE_REFS_NOT_CANONICAL"),
    ("semantic_dependencies", "window_disclosure_refs", "WINDOW_REFS_NOT_CANONICAL"),
    ("validation", "validation_report_refs", "VALIDATION_REFS_NOT_CANONICAL"),
    ("disclosure", "review_record_refs", "REVIEW_REFS_NOT_CANONICAL"),
)

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
    return [Finding("SCHEMA_INVALID", _json_path(error.absolute_path)) for error in errors[:100]]


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


def _definition_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    kind = candidate["view_kind"]
    definition = candidate["definition"]
    assert isinstance(definition, Mapping)
    if kind == "UNRESOLVED":
        findings.add(Finding("VIEW_KIND_UNRESOLVED", "$.view_kind"))
    elif kind in {"DATABASE_VIEW", "MATERIALIZED_VIEW"} and definition["dialect_profile_ref"] is None:
        findings.add(Finding("SQL_DIALECT_PROFILE_REQUIRED", "$.definition.dialect_profile_ref"))
    return findings


def _validation_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    validation = candidate["validation"]
    assert isinstance(validation, Mapping)
    state = validation["state"]
    reports = validation["validation_report_refs"]
    receipt = validation["fixture_receipt_ref"]
    if state == "ERROR":
        return {Finding("VALIDATION_RECORDED_ERROR", "$.validation.state")}
    if state == "NOT_VALIDATED":
        if reports or receipt is not None:
            return {Finding("NOT_VALIDATED_REFERENCES_INCOHERENT", "$.validation")}
        return {Finding("VIEW_NOT_VALIDATED", "$.validation.state")}
    if state == "PARTIAL":
        return {Finding("VALIDATION_PARTIAL", "$.validation.state")}
    if not reports or receipt is None:
        return {Finding("VALIDATION_EVIDENCE_REQUIRED", "$.validation")}
    return set()


def _materialization_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    kind = candidate["view_kind"]
    materialization = candidate["materialization"]
    assert isinstance(materialization, Mapping)
    mode = materialization["refresh_mode"]
    freshness = materialization["freshness_profile_ref"]
    if kind == "DATABASE_VIEW" and (mode != "ON_QUERY" or freshness is not None):
        findings.add(Finding("DATABASE_VIEW_REFRESH_INCOHERENT", "$.materialization"))
    elif kind == "MATERIALIZED_VIEW":
        if mode not in {"SCHEDULED", "EVENT_DRIVEN", "MANUAL"}:
            findings.add(Finding("MATERIALIZED_VIEW_REFRESH_INCOHERENT", "$.materialization.refresh_mode"))
        elif freshness is None:
            findings.add(Finding("MATERIALIZED_VIEW_FRESHNESS_REQUIRED", "$.materialization.freshness_profile_ref"))
    return findings


def _mutation_findings(candidate: Mapping[str, Any]) -> set[Finding]:
    mutation = candidate["mutation"]
    semantics = candidate["semantic_dependencies"]
    disclosure = candidate["disclosure"]
    assert isinstance(mutation, Mapping)
    assert isinstance(semantics, Mapping)
    assert isinstance(disclosure, Mapping)
    posture = mutation["posture"]
    predicate = mutation["predicate_ref"]
    guard = mutation["check_option_mode"]
    policy = mutation["mutation_policy_ref"]

    if posture == "UNRESOLVED":
        if predicate is not None or policy is not None or guard != "UNRESOLVED":
            return {Finding("UNRESOLVED_MUTATION_INCOHERENT", "$.mutation")}
        return {Finding("MUTATION_POSTURE_UNRESOLVED", "$.mutation.posture")}
    if posture == "READ_ONLY":
        if predicate is not None or policy is not None or guard != "NOT_APPLICABLE":
            return {Finding("READ_ONLY_MUTATION_FIELDS_INCOHERENT", "$.mutation")}
        return set()
    if posture == "DIRECT_MUTATION_PROHIBITED":
        if predicate is not None or guard != "NOT_APPLICABLE" or policy is None:
            return {Finding("MUTATION_PROHIBITION_INCOHERENT", "$.mutation")}
        return set()

    findings: set[Finding] = set()
    if predicate is None or policy is None or guard not in GUARD_MODES:
        findings.add(Finding("UPDATABLE_GUARD_REQUIRED", "$.mutation"))
    elif predicate != semantics["filter_predicate_ref"]:
        findings.add(Finding("VIEW_PREDICATE_GUARD_MISMATCH", "$.mutation.predicate_ref"))
    if disclosure["intended_use"] == "PUBLIC_CANDIDATE":
        findings.add(Finding("PUBLIC_UPDATABLE_VIEW_DENIED", "$.mutation.posture"))
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(set(schema_findings))))
    assert isinstance(candidate, Mapping)

    findings: set[Finding] = set()
    if not _is_utc(candidate["assessed_at"]):
        findings.add(Finding("ASSESSED_AT_NOT_UTC", "$.assessed_at"))
    for parent, field, code in CANONICAL_ARRAY_PATHS:
        container = candidate[parent]
        assert isinstance(container, Mapping)
        if not _canonical_strings(container[field]):
            findings.add(Finding(code, f"$.{parent}.{field}"))

    findings.update(_definition_findings(candidate))
    validation_findings = _validation_findings(candidate)
    findings.update(validation_findings)
    if "VALIDATION_RECORDED_ERROR" not in {item.code for item in validation_findings}:
        findings.update(_materialization_findings(candidate))
        findings.update(_mutation_findings(candidate))
        disclosure = candidate["disclosure"]
        assert isinstance(disclosure, Mapping)
        if disclosure["intended_use"] == "PUBLIC_CANDIDATE" and not disclosure["review_record_refs"]:
            findings.add(Finding("PUBLIC_DISCLOSURE_REVIEW_REQUIRED", "$.disclosure.review_record_refs"))

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
        result = validate_candidate(materialize_case(manifest, raw_case))
        expected = raw_case.get("expected")
        if not isinstance(expected, Mapping):
            raise JsonInputError("fixture case expected result must be an object")
        if result.outcome != expected.get("outcome") or result.codes != expected.get("codes"):
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
