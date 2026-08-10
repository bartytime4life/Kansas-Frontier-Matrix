"""Validate fixture-only measurement scale operation assessments.

The proposed matrix is a conservative fixture profile. This module does not
inspect values, infer scale class, compute statistics, render legends, decide
policy or review, release, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/measurement_scale_operation_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/measurement_scale_operation_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"ASSESSMENT_INCOMPLETE", "ASSESSMENT_UNKNOWN", "MIXED_OR_CUSTOM_REQUIRES_REVIEW", "SCALE_DEFINITION_UNRESOLVED"}

ALL_OPERATIONS = {
    "CATEGORICAL_LEGEND", "ORDERED_LEGEND", "SEQUENTIAL_COLOR_RAMP", "DIVERGING_COLOR_RAMP",
    "RANK", "MODE", "MEDIAN", "MEAN", "SUM", "DIFFERENCE", "RATIO", "MIN_MAX",
    "PROPORTIONAL_SYMBOL", "QUANTILE_CLASSIFICATION",
}
ALLOWED = {
    "NOMINAL": {"CATEGORICAL_LEGEND", "MODE"},
    "ORDINAL": {"CATEGORICAL_LEGEND", "ORDERED_LEGEND", "SEQUENTIAL_COLOR_RAMP", "RANK", "MODE", "MEDIAN", "MIN_MAX", "QUANTILE_CLASSIFICATION"},
    "INTERVAL": {"CATEGORICAL_LEGEND", "ORDERED_LEGEND", "SEQUENTIAL_COLOR_RAMP", "DIVERGING_COLOR_RAMP", "RANK", "MODE", "MEDIAN", "MEAN", "DIFFERENCE", "MIN_MAX", "QUANTILE_CLASSIFICATION"},
    "RATIO": ALL_OPERATIONS,
}
EXPECTED_METADATA = {
    "NOMINAL": (False, False, "NOT_APPLICABLE"),
    "ORDINAL": (True, False, "NOT_APPLICABLE"),
    "INTERVAL": (True, True, "ABSENT"),
    "RATIO": (True, True, "PRESENT"),
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (list(error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    measurement = candidate["measurement"]
    assessment = candidate["assessment"]
    requested = candidate["requested_operations"]
    assert isinstance(measurement, Mapping) and isinstance(assessment, Mapping) and isinstance(requested, list)

    for field, value in (("requested_operations", requested), ("permitted_operations", assessment.get("permitted_operations")), ("denied_operations", assessment.get("denied_operations")), ("obligations", assessment.get("obligations")), ("review_record_refs", assessment.get("review_record_refs"))):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/{'assessment/' if field != 'requested_operations' else ''}{field}"))

    definition = measurement.get("scale_definition")
    if isinstance(definition, Mapping) and definition.get("resolution") == "UNRESOLVED":
        findings.add(Finding("SCALE_DEFINITION_UNRESOLVED", "/measurement/scale_definition/resolution"))

    scale = measurement.get("scale_class")
    state = assessment.get("state")
    if state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("ASSESSMENT_UNKNOWN", "/assessment/state"))

    if scale in {"MIXED", "CUSTOM"}:
        findings.add(Finding("MIXED_OR_CUSTOM_REQUIRES_REVIEW", "/measurement/scale_class"))
        if state == "COMPLETE":
            findings.add(Finding("MIXED_OR_CUSTOM_COMPLETE_DENIED", "/assessment/state"))
    else:
        expected = EXPECTED_METADATA[str(scale)]
        actual = (measurement.get("ordering_meaningful"), measurement.get("equal_intervals"), measurement.get("true_zero"))
        if actual != expected:
            findings.add(Finding("MEASUREMENT_METADATA_INCOHERENT", "/measurement"))
        if scale in {"INTERVAL", "RATIO"} and measurement.get("unit_ref") is None:
            findings.add(Finding("NUMERIC_UNIT_REQUIRED", "/measurement/unit_ref"))

    if state == "COMPLETE" and scale in ALLOWED:
        allowed = ALLOWED[str(scale)]
        expected_permitted = sorted(set(requested) & allowed)
        expected_denied = sorted(set(requested) - allowed)
        if assessment.get("permitted_operations") != expected_permitted or assessment.get("denied_operations") != expected_denied:
            findings.add(Finding("OPERATION_PARTITION_MISMATCH", "/assessment"))
        obligations = assessment.get("obligations")
        if expected_denied and (not isinstance(obligations, list) or "UNSUPPORTED_OPERATION_BLOCKED" not in obligations):
            findings.add(Finding("DENIED_OPERATION_OBLIGATION_REQUIRED", "/assessment/obligations"))

    if candidate.get("intended_use") in {"PUBLIC_MAP", "POLICY_CONTEXT"} and state == "COMPLETE" and not assessment.get("review_record_refs"):
        findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/assessment/review_record_refs"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest() -> list[tuple[str, str, list[str]]]:
    manifest, findings = load_json_object(FIXTURE_PATH)
    if manifest is None or findings:
        raise ValueError("fixture manifest is unreadable")
    results: list[tuple[str, str, list[str]]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        result = validate_candidate(materialize_fixture_case(manifest, entry))
        expected = entry["expected"]
        assert isinstance(expected, Mapping)
        name = str(entry["name"])
        if result.outcome != expected["outcome"] or result.codes != expected["codes"]:
            raise AssertionError(f"{name}: expected {expected}, got {result.outcome} {result.codes}")
        results.append((name, result.outcome, result.codes))
    return results


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        for name, outcome, codes in validate_fixture_manifest():
            print(json.dumps({"case": name, "codes": codes, "outcome": outcome}, sort_keys=True, separators=(",", ":")))
        return 0
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        candidate, findings = load_json_object(path)
        result = ValidationResult("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
        print(json.dumps({"file": path.name, "codes": result.codes, "outcome": result.outcome}, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.outcome == "PASS" else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
