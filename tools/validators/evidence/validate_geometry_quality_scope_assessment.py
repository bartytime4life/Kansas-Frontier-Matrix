#!/usr/bin/env python3
"""Validate inactive fixture-only geometry quality scope assessments."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/evidence/geometry_quality_scope_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/evidence/geometry_quality_scope_assessment/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "geometry-quality-scope-assessment-fixture-only-v1"
IDENTITY_PREFIX = "geometry-quality-scope:"
SOURCE_IDEA = "KFM-P18-INV-052"
QUALITY_RANK = {
    "SUB_METER": 0,
    "METER": 1,
    "TEN_METER": 2,
    "HUNDRED_METER": 3,
    "KILOMETER_OR_COARSER": 4,
}
ABSTAIN_CODES = {
    "ACCURACY_CLASS_UNKNOWN",
    "ACQUISITION_METHOD_UNKNOWN",
    "OBSERVATION_METHOD_UNRESOLVED",
    "PRECISION_CLASS_UNKNOWN",
    "PROVENANCE_UNRESOLVED",
    "QUALITY_SCOPE_UNKNOWN",
    "QUALITY_WITHHELD",
}
ERROR_CODES = {
    "ASSESSMENT_ID_MISMATCH",
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "FIXTURE_MANIFEST_INVALID",
    "INPUT_SYMLINK_DENIED",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_INVALID",
    "SCHEMA_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
}
FALSE_AUTHORITY = {
    "coordinates": False,
    "feature_identity": False,
    "reference_resolution": False,
    "accuracy_measurement": False,
    "precision_measurement": False,
    "transform": False,
    "fitness": False,
    "evidence": False,
    "policy": False,
    "human_review": False,
    "lifecycle": False,
    "release": False,
    "publication": False,
    "public_use": False,
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
        return self.outcome == "PASS"


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _bad_number(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_bad_number,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(identity_subject(candidate))).hexdigest()


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    return IDENTITY_PREFIX + canonical_spec_hash(candidate).removeprefix("sha256:")[:24]


def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate))
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def expected_summary(candidate: Mapping[str, Any]) -> dict[str, int]:
    records = candidate.get("quality_records")
    if not isinstance(records, list):
        records = []
    mappings = [record for record in records if isinstance(record, Mapping)]
    return {
        "record_count": len(records),
        "dataset_record_count": sum(record.get("subject_kind") == "DATASET" for record in mappings),
        "feature_record_count": sum(record.get("subject_kind") == "FEATURE" for record in mappings),
        "resolved_accuracy_count": sum(record.get("accuracy_class") not in {"UNKNOWN", "WITHHELD"} for record in mappings),
        "resolved_precision_count": sum(record.get("precision_class") not in {"UNKNOWN", "WITHHELD"} for record in mappings),
    }


def _time(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0 else None


def _record_key(record: Mapping[str, Any]) -> tuple[str, str]:
    return str(record.get("subject_kind")), str(record.get("subject_ref_digest"))


def _expected_accuracy_effect(input_class: object, output_class: object) -> str | None:
    if output_class == "UNKNOWN" or input_class == "UNKNOWN":
        return "UNKNOWN"
    if output_class == "WITHHELD":
        return "WITHHELD"
    if input_class not in QUALITY_RANK or output_class not in QUALITY_RANK:
        return None
    return "UNCHANGED" if QUALITY_RANK[output_class] == QUALITY_RANK[input_class] else "DEGRADED"


def _expected_precision_effect(input_class: object, output_class: object) -> str | None:
    if output_class == "UNKNOWN" or input_class == "UNKNOWN":
        return "UNKNOWN"
    if output_class == "WITHHELD":
        return "WITHHELD"
    if input_class not in QUALITY_RANK or output_class not in QUALITY_RANK:
        return None
    return "UNCHANGED" if QUALITY_RANK[output_class] == QUALITY_RANK[input_class] else "COARSENED"


def _derivation_findings(record: Mapping[str, Any], path: str) -> list[Finding]:
    findings: list[Finding] = []
    derivation = record.get("derivation")
    if not isinstance(derivation, Mapping):
        return findings
    kind = derivation.get("kind")
    input_ref = derivation.get("input_quality_ref")
    input_accuracy = derivation.get("input_accuracy_class")
    input_precision = derivation.get("input_precision_class")
    receipt_ref = derivation.get("transform_receipt_ref")
    accuracy_effect = derivation.get("accuracy_effect")
    precision_effect = derivation.get("precision_effect")
    output_accuracy = record.get("accuracy_class")
    output_precision = record.get("precision_class")

    if kind == "NONE":
        if any(value is not None for value in (input_ref, input_accuracy, input_precision, receipt_ref)) or accuracy_effect != "NOT_APPLICABLE" or precision_effect != "NOT_APPLICABLE":
            findings.append(Finding("NONE_DERIVATION_FIELDS_PRESENT", path))
        return findings

    if input_ref is None or input_accuracy is None or input_precision is None:
        findings.append(Finding("DERIVATION_INPUT_REQUIRED", path))
    if receipt_ref is None:
        findings.append(Finding("DERIVATION_RECEIPT_REQUIRED", path + "/transform_receipt_ref"))

    if kind == "WITHHELD":
        if output_accuracy != "WITHHELD" or output_precision != "WITHHELD":
            findings.append(Finding("WITHHELD_OUTPUT_REQUIRED", path))
    elif kind in {"REPROJECTED", "GENERALIZED", "AGGREGATED"}:
        if record.get("acquisition_method") not in {"DERIVED", "GENERALIZED_PUBLIC"}:
            findings.append(Finding("DERIVATION_METHOD_INCOHERENT", path.replace("/derivation", "/acquisition_method")))
        if input_accuracy in QUALITY_RANK and output_accuracy in QUALITY_RANK and QUALITY_RANK[output_accuracy] < QUALITY_RANK[input_accuracy]:
            findings.append(Finding("ACCURACY_IMPROVEMENT_UNSUPPORTED", path.replace("/derivation", "/accuracy_class")))
        if input_precision in QUALITY_RANK and output_precision in QUALITY_RANK and QUALITY_RANK[output_precision] < QUALITY_RANK[input_precision]:
            findings.append(Finding("PRECISION_IMPROVEMENT_UNSUPPORTED", path.replace("/derivation", "/precision_class")))

    expected_accuracy = _expected_accuracy_effect(input_accuracy, output_accuracy)
    expected_precision = _expected_precision_effect(input_precision, output_precision)
    if expected_accuracy is not None and accuracy_effect != expected_accuracy:
        findings.append(Finding("ACCURACY_EFFECT_MISMATCH", path + "/accuracy_effect"))
    if expected_precision is not None and precision_effect != expected_precision:
        findings.append(Finding("PRECISION_EFFECT_MISMATCH", path + "/precision_effect"))
    return findings


def _assessment_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    if _time(candidate.get("assessed_at")) is None:
        findings.add(Finding("ASSESSED_AT_NOT_UTC", "/assessed_at"))
    records = candidate.get("quality_records")
    if not isinstance(records, list):
        return []
    mappings = [record for record in records if isinstance(record, Mapping)]
    keys = [_record_key(record) for record in mappings]
    if len(mappings) != len(records) or keys != sorted(set(keys)):
        findings.add(Finding("QUALITY_RECORDS_NOT_CANONICAL", "/quality_records"))
    if candidate.get("summary") != expected_summary(candidate):
        findings.add(Finding("SUMMARY_MISMATCH", "/summary"))

    dataset_records = [record for record in mappings if record.get("subject_kind") == "DATASET"]
    feature_records = [record for record in mappings if record.get("subject_kind") == "FEATURE"]
    scope = candidate.get("quality_scope")
    if isinstance(scope, Mapping):
        mode = scope.get("mode")
        profile_ref = scope.get("dataset_quality_profile_ref")
        feature_count = candidate.get("feature_count")
        if mode == "UNKNOWN":
            if profile_ref is not None or records:
                findings.add(Finding("UNKNOWN_SCOPE_MUST_BE_EMPTY", "/quality_scope"))
            else:
                findings.add(Finding("QUALITY_SCOPE_UNKNOWN", "/quality_scope/mode"))
        elif mode == "DATASET_INHERITED":
            if profile_ref is None:
                findings.add(Finding("DATASET_PROFILE_REQUIRED", "/quality_scope/dataset_quality_profile_ref"))
            if len(dataset_records) != 1 or feature_records:
                findings.add(Finding("DATASET_INHERITANCE_RECORD_PATTERN_INVALID", "/quality_records"))
        elif mode == "FEATURE_EXPLICIT":
            if profile_ref is not None:
                findings.add(Finding("DATASET_PROFILE_UNEXPECTED", "/quality_scope/dataset_quality_profile_ref"))
            if dataset_records or len(feature_records) != feature_count:
                findings.add(Finding("FEATURE_COVERAGE_MISMATCH", "/quality_records"))
        elif mode == "MIXED_OVERRIDE":
            if profile_ref is None:
                findings.add(Finding("DATASET_PROFILE_REQUIRED", "/quality_scope/dataset_quality_profile_ref"))
            if len(dataset_records) != 1:
                findings.add(Finding("MIXED_DATASET_RECORD_REQUIRED", "/quality_records"))
            if not feature_records or not isinstance(feature_count, int) or len(feature_records) >= feature_count:
                findings.add(Finding("MIXED_OVERRIDE_REQUIRED", "/quality_records"))

    for index, record in enumerate(mappings):
        base = f"/quality_records/{index}"
        if record.get("geometry_revision") != candidate.get("geometry_revision"):
            findings.add(Finding("GEOMETRY_REVISION_MISMATCH", base + "/geometry_revision"))
        if record.get("subject_kind") == "DATASET" and record.get("subject_ref_digest") != candidate.get("geometry_artifact_digest"):
            findings.add(Finding("DATASET_SUBJECT_DIGEST_MISMATCH", base + "/subject_ref_digest"))
        accuracy = record.get("accuracy_class")
        precision = record.get("precision_class")
        if accuracy == "UNKNOWN":
            findings.add(Finding("ACCURACY_CLASS_UNKNOWN", base + "/accuracy_class"))
        if precision == "UNKNOWN":
            findings.add(Finding("PRECISION_CLASS_UNKNOWN", base + "/precision_class"))
        if (accuracy == "WITHHELD") != (precision == "WITHHELD"):
            findings.add(Finding("WITHHELD_DIMENSIONS_MISMATCH", base))
        elif accuracy == "WITHHELD":
            findings.add(Finding("QUALITY_WITHHELD", base))
        if record.get("acquisition_method") == "UNKNOWN":
            findings.add(Finding("ACQUISITION_METHOD_UNKNOWN", base + "/acquisition_method"))
        if record.get("observation_method_ref") is None:
            findings.add(Finding("OBSERVATION_METHOD_UNRESOLVED", base + "/observation_method_ref"))
        if record.get("provenance_ref") is None:
            findings.add(Finding("PROVENANCE_UNRESOLVED", base + "/provenance_ref"))
        findings.update(_derivation_findings(record, base + "/derivation"))
    return sorted(findings)


def _recommendation(findings: Sequence[Finding]) -> str:
    if not findings:
        return "READY_FOR_FITNESS_REVIEW"
    if all(finding.code in ABSTAIN_CODES for finding in findings):
        return "HOLD"
    return "DENY"


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if findings:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    findings = _assessment_findings(candidate)
    if candidate.get("recommendation") != _recommendation(findings):
        findings.append(Finding("RECOMMENDATION_MISMATCH", "/recommendation"))
    if candidate.get("spec_hash") != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_assessment_id(candidate):
        findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    if any(finding.code in ERROR_CODES for finding in ordered):
        return ValidationResult("ERROR", ordered)
    if all(finding.code in ABSTAIN_CODES for finding in ordered):
        return ValidationResult("ABSTAIN", ordered)
    return ValidationResult("DENY", ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/") if part]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    if not parts:
        raise ValueError("root replacement is not supported")
    leaf = parts[-1]
    if isinstance(current, list):
        current[int(leaf)] = copy.deepcopy(value)
    else:
        current[leaf] = copy.deepcopy(value)


def _fixture_document(path: Path = CASES) -> dict[str, Any]:
    document, findings = _read(path)
    if (
        document is None
        or findings
        or document.get("profile") != "kfm.evidence.geometry-quality-scope-assessment-fixtures.v1"
        or document.get("source_idea_id") != SOURCE_IDEA
        or not isinstance(document.get("base"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], definition: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(document["base"])
    for mutation in definition.get("mutations", []):
        _set(candidate, mutation["path"], mutation["value"])
    if definition.get("summary_mode", "DERIVE") == "DERIVE":
        candidate["summary"] = expected_summary(candidate)
    elif definition.get("summary_mode") != "KEEP":
        raise ValueError("unknown summary mode")
    candidate["recommendation"] = _recommendation(_assessment_findings(candidate))
    if definition.get("recommendation_mode") == "MISMATCH":
        candidate["recommendation"] = "HOLD" if candidate["recommendation"] != "HOLD" else "DENY"
    candidate = assign_identity(candidate)
    identity_mode = definition.get("identity_mode", "RECOMPUTE")
    if identity_mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif identity_mode == "MISMATCH_ID":
        candidate["assessment_id"] = IDENTITY_PREFIX + "0" * 24
    elif identity_mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases(path: Path = CASES) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _fixture_document(path)
    output: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names:
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        output.append((raw, materialize_case(document, raw)))
    return output


def _serialize(result: ValidationResult, *, path: Path | None = None, case: str | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "scope": SCOPE,
        "authority": FALSE_AUTHORITY,
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures(path: Path = CASES) -> int:
    try:
        cases = load_fixture_cases(path)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError):
        print(_serialize(ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),))))
        return 1
    failed = False
    outcomes: set[str] = set()
    for definition, candidate in cases:
        result = validate_payload(candidate)
        actual = {"outcome": result.outcome, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}
        expected = {"outcome": definition["expected_outcome"], "findings": definition["expected_findings"]}
        print(_serialize(result, case=definition["name"]))
        failed |= actual != expected
        outcomes.add(result.outcome)
    failed |= outcomes != {"PASS", "ABSTAIN", "DENY", "ERROR"}
    if not failed:
        print(f"CONFIRMED: {len(cases)} geometry quality scope cases passed exact polarity.")
    return 1 if failed else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.print_usage()
            return 2
        return replay_fixtures()
    if not args.files:
        parser.print_usage()
        return 2
    failed = False
    for path in args.files:
        result = validate_file(path)
        print(_serialize(result, path=path))
        failed |= not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
