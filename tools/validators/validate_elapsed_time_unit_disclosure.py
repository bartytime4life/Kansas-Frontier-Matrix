"""Validate fixture-only elapsed-time unit disclosure candidates.

The validator checks explicit temporal-unit declarations and safe local
invariants. It does not execute SQL, inspect timestamps, calculate metrics,
resolve evidence, decide policy or review, release, or publish.
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

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/elapsed_time_unit_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/elapsed_time_unit_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"ASSESSMENT_INCOMPLETE", "ENGINE_PARITY_UNRESOLVED", "REFERENCE_UNRESOLVED", "TIMEZONE_ASSUMPTION_UNRESOLVED"}
ERROR_CODES = {"ASSESSMENT_ERROR"}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_METRIC_RECOMPUTATION",
    "NO_PUBLICATION_AUTHORITY",
    "NO_QUERY_EXECUTION",
]
FIXED_UNIT_NANOSECONDS = {
    "NANOSECOND": 1,
    "MICROSECOND": 1_000,
    "MILLISECOND": 1_000_000,
    "SECOND": 1_000_000_000,
    "MINUTE": 60_000_000_000,
    "HOUR": 3_600_000_000_000,
    "DAY": 86_400_000_000_000,
    "WEEK": 604_800_000_000_000,
}
CALENDAR_UNITS = {"CALENDAR_MONTH", "CALENDAR_YEAR"}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
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
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
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


def _reference_unresolved(value: object) -> bool:
    return isinstance(value, Mapping) and value.get("resolution") == "UNRESOLVED"


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/recorded_at"))

    assessment_state = candidate["assessment_state"]
    if assessment_state == "INCOMPLETE":
        findings.add(Finding("ASSESSMENT_INCOMPLETE", "/assessment_state"))
    elif assessment_state == "ERROR":
        findings.add(Finding("ASSESSMENT_ERROR", "/assessment_state"))

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(candidate["evidence_bundle_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/evidence_bundle_refs"))

    temporal = candidate["temporal_inputs"]
    conversion = candidate["conversion"]
    disclosure = candidate["public_disclosure"]
    assert isinstance(temporal, Mapping)
    assert isinstance(conversion, Mapping)
    assert isinstance(disclosure, Mapping)

    if temporal["start_timestamp_field"] == temporal["end_timestamp_field"]:
        findings.add(Finding("TIMESTAMP_FIELD_COLLISION", "/temporal_inputs"))

    for value, field in (
        (candidate["query_run"], "/query_run/resolution"),
        (candidate["method_definition"], "/method_definition/resolution"),
        (temporal["timezone_profile"], "/temporal_inputs/timezone_profile/resolution"),
        (conversion["engine_profile"], "/conversion/engine_profile/resolution"),
    ):
        if _reference_unresolved(value):
            findings.add(Finding("REFERENCE_UNRESOLVED", field))

    if temporal["timezone_assumption"] == "UNRESOLVED":
        findings.add(Finding("TIMEZONE_ASSUMPTION_UNRESOLVED", "/temporal_inputs/timezone_assumption"))

    boundary_semantics = temporal["boundary_semantics"]
    boundary_profile = temporal["boundary_profile"]
    if boundary_semantics == "INSTANT_DIFFERENCE":
        if boundary_profile is not None:
            findings.add(Finding("BOUNDARY_PROFILE_UNEXPECTED", "/temporal_inputs/boundary_profile"))
    elif boundary_profile is None:
        findings.add(Finding("BOUNDARY_PROFILE_REQUIRED", "/temporal_inputs/boundary_profile"))
    elif _reference_unresolved(boundary_profile):
        findings.add(Finding("REFERENCE_UNRESOLVED", "/temporal_inputs/boundary_profile/resolution"))

    extraction_unit = conversion["extraction_unit"]
    displayed_unit = conversion["displayed_unit"]
    numerator = conversion["conversion_numerator"]
    denominator = conversion["conversion_denominator"]
    assert isinstance(extraction_unit, str)
    assert isinstance(displayed_unit, str)
    assert isinstance(numerator, int)
    assert isinstance(denominator, int)

    if math.gcd(numerator, denominator) != 1:
        findings.add(Finding("CONVERSION_FRACTION_NOT_REDUCED", "/conversion"))

    has_calendar_unit = extraction_unit in CALENDAR_UNITS or displayed_unit in CALENDAR_UNITS
    if has_calendar_unit:
        if boundary_semantics != "CALENDAR_BOUNDARY_COUNT":
            findings.add(Finding("CALENDAR_UNIT_BOUNDARY_SEMANTICS_REQUIRED", "/temporal_inputs/boundary_semantics"))
        if extraction_unit != displayed_unit:
            findings.add(Finding("CALENDAR_UNIT_CONVERSION_DENIED", "/conversion"))
        elif numerator != 1 or denominator != 1:
            findings.add(Finding("CALENDAR_IDENTITY_CONVERSION_REQUIRED", "/conversion"))
    else:
        extraction_ns = FIXED_UNIT_NANOSECONDS[extraction_unit]
        displayed_ns = FIXED_UNIT_NANOSECONDS[displayed_unit]
        if numerator * displayed_ns != denominator * extraction_ns:
            findings.add(Finding("UNIT_CONVERSION_MISMATCH", "/conversion"))

    if conversion["rounding_mode"] == "NONE" and conversion["decimal_places"] != 0:
        findings.add(Finding("ROUNDING_DECLARATION_MISMATCH", "/conversion/decimal_places"))
    if conversion["negative_interval_policy"] == "ABSOLUTE_VALUE":
        findings.add(Finding("ABSOLUTE_VALUE_DIRECTION_LOSS", "/conversion/negative_interval_policy"))
    if conversion["null_interval_policy"] == "DROP":
        findings.add(Finding("NULL_INTERVAL_DROP_DENIED", "/conversion/null_interval_policy"))

    parity_state = conversion["parity_state"]
    parity_fixture_ref = conversion["parity_fixture_ref"]
    if parity_state == "UNRESOLVED":
        findings.add(Finding("ENGINE_PARITY_UNRESOLVED", "/conversion/parity_state"))
    elif parity_state == "MISMATCH":
        findings.add(Finding("ENGINE_PARITY_MISMATCH", "/conversion/parity_state"))
    elif parity_state == "SYNTHETIC_PARITY" and parity_fixture_ref is None:
        findings.add(Finding("PARITY_FIXTURE_MISSING", "/conversion/parity_fixture_ref"))
    elif parity_state == "SINGLE_ENGINE_DECLARED" and parity_fixture_ref is not None:
        findings.add(Finding("PARITY_FIXTURE_UNEXPECTED", "/conversion/parity_fixture_ref"))

    if not _canonical_strings(disclosure["review_record_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/public_disclosure/review_record_refs"))
    if not _canonical_strings(disclosure["release_manifest_refs"]):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/public_disclosure/release_manifest_refs"))
    if candidate["intended_use"] == "PUBLIC_METRIC_SUPPORT_CANDIDATE":
        if not disclosure["review_record_refs"] or not disclosure["release_manifest_refs"]:
            findings.add(Finding("PUBLIC_CANDIDATE_REFERENCE_MISSING", "/public_disclosure"))
        for field in (
            "extraction_unit_visible",
            "conversion_rule_visible",
            "timezone_assumption_visible",
            "boundary_semantics_visible",
            "rounding_visible",
        ):
            if disclosure[field] is not True:
                findings.add(Finding("PUBLIC_DISCLOSURE_INCOMPLETE", f"/public_disclosure/{field}"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if codes & ERROR_CODES:
        outcome = "ERROR"
    elif not codes:
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
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only elapsed-time unit disclosures.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
