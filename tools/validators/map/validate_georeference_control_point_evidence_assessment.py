#!/usr/bin/env python3
"""Validate inactive, fixture-only GCP evidence assessment candidates.

PASS means internally coherent and ready for human review only. The validator
does not resolve references, open imagery, verify coordinates, evaluate GCP
distribution or transform quality, decide policy, or authorize public use.
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
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/map/georeference_control_point_evidence_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/map/georeference_control_point_evidence_assessment/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "georeference-control-point-evidence-assessment-fixture-only-v1"
IDENTITY_PREFIX = "gcp-evidence-assessment:"
ABSTAIN_CODES = {
    "COORDINATE_SOURCE_UNRESOLVED",
    "MARKER_SCALE_UNKNOWN",
    "MATCHING_REVIEW_UNRESOLVED",
    "MATCHING_UNRESOLVED",
    "POINT_CONTRAST_UNKNOWN",
    "POINT_MATCH_UNRESOLVED",
    "POINT_VISIBILITY_PARTIAL",
    "POINT_VISIBILITY_UNKNOWN",
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
    "reference_resolution": False,
    "imagery_access": False,
    "coordinate_accuracy": False,
    "distribution_decision": False,
    "transform_quality_decision": False,
    "policy": False,
    "human_review": False,
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
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


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
    points = candidate.get("control_points")
    if not isinstance(points, list):
        return {
            "clear_visibility_count": 0,
            "acceptable_contrast_count": 0,
            "adequate_scale_count": 0,
            "verified_match_count": 0,
        }
    return {
        "clear_visibility_count": sum(point.get("visibility") == "CLEAR" for point in points if isinstance(point, Mapping)),
        "acceptable_contrast_count": sum(point.get("contrast") in {"HIGH", "ADEQUATE"} for point in points if isinstance(point, Mapping)),
        "adequate_scale_count": sum(point.get("marker_scale") == "ADEQUATE" for point in points if isinstance(point, Mapping)),
        "verified_match_count": sum(point.get("match_status") == "VERIFIED" for point in points if isinstance(point, Mapping)),
    }


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _assessment_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    if not _is_utc(candidate.get("evaluated_at")):
        findings.add(Finding("EVALUATED_AT_NOT_UTC", "/evaluated_at"))

    points = candidate.get("control_points")
    if not isinstance(points, list):
        return [Finding("CONTROL_POINTS_INVALID", "/control_points")]
    if candidate.get("control_point_count") != len(points):
        findings.add(Finding("CONTROL_POINT_COUNT_MISMATCH", "/control_point_count"))
    ids = [point.get("id") for point in points if isinstance(point, Mapping)]
    if len(ids) != len(points) or ids != sorted(set(ids)):
        findings.add(Finding("POINT_IDS_NOT_CANONICAL", "/control_points"))
    if candidate.get("summary") != expected_summary(candidate):
        findings.add(Finding("SUMMARY_MISMATCH", "/summary"))

    evidence_refs = candidate.get("evidence_refs")
    if not _canonical_strings(evidence_refs):
        findings.add(Finding("EVIDENCE_REFERENCES_NOT_CANONICAL", "/evidence_refs"))
    evidence_set = set(evidence_refs) if isinstance(evidence_refs, list) else set()

    source = candidate.get("coordinate_source")
    if isinstance(source, Mapping):
        method = source.get("method")
        status = source.get("status")
        evidence_ref = source.get("evidence_ref")
        if method == "UNKNOWN" or status == "UNKNOWN":
            findings.add(Finding("COORDINATE_SOURCE_UNRESOLVED", "/coordinate_source"))
        if status == "INVALID":
            findings.add(Finding("COORDINATE_SOURCE_INVALID", "/coordinate_source/status"))
        if status == "VERIFIED":
            if method == "UNKNOWN":
                findings.add(Finding("COORDINATE_SOURCE_STATUS_INCOHERENT", "/coordinate_source"))
            if source.get("reference_system_ref") is None:
                findings.add(Finding("VERIFIED_REFERENCE_SYSTEM_MISSING", "/coordinate_source/reference_system_ref"))
            if evidence_ref is None:
                findings.add(Finding("VERIFIED_SOURCE_EVIDENCE_MISSING", "/coordinate_source/evidence_ref"))
        if isinstance(evidence_ref, str) and evidence_ref not in evidence_set:
            findings.add(Finding("EVIDENCE_REFERENCE_UNBOUND", "/coordinate_source/evidence_ref"))

    matching = candidate.get("matching")
    if isinstance(matching, Mapping):
        method = matching.get("method")
        status = matching.get("status")
        evidence_ref = matching.get("evidence_ref")
        if method == "UNKNOWN" or status == "UNKNOWN":
            findings.add(Finding("MATCHING_UNRESOLVED", "/matching"))
        if method == "AUTOMATED_UNREVIEWED":
            findings.add(Finding("MATCHING_REVIEW_UNRESOLVED", "/matching/method"))
        if status == "INVALID":
            findings.add(Finding("MATCHING_INVALID", "/matching/status"))
        if status == "VERIFIED":
            if method in {"UNKNOWN", "AUTOMATED_UNREVIEWED"}:
                findings.add(Finding("MATCHING_STATUS_INCOHERENT", "/matching"))
            if matching.get("image_observation_set_ref") is None:
                findings.add(Finding("VERIFIED_MATCHING_INPUT_MISSING", "/matching/image_observation_set_ref"))
            if evidence_ref is None:
                findings.add(Finding("VERIFIED_MATCHING_EVIDENCE_MISSING", "/matching/evidence_ref"))
        if isinstance(evidence_ref, str) and evidence_ref not in evidence_set:
            findings.add(Finding("EVIDENCE_REFERENCE_UNBOUND", "/matching/evidence_ref"))

    for index, point in enumerate(points):
        if not isinstance(point, Mapping):
            continue
        base = f"/control_points/{index}"
        visibility = point.get("visibility")
        contrast = point.get("contrast")
        marker_scale = point.get("marker_scale")
        match_status = point.get("match_status")
        evidence_ref = point.get("evidence_ref")
        if visibility == "PARTIAL":
            findings.add(Finding("POINT_VISIBILITY_PARTIAL", base + "/visibility"))
        elif visibility == "OBSCURED":
            findings.add(Finding("POINT_VISIBILITY_OBSCURED", base + "/visibility"))
        elif visibility == "UNKNOWN":
            findings.add(Finding("POINT_VISIBILITY_UNKNOWN", base + "/visibility"))
        if contrast == "LOW":
            findings.add(Finding("POINT_CONTRAST_LOW", base + "/contrast"))
        elif contrast == "UNKNOWN":
            findings.add(Finding("POINT_CONTRAST_UNKNOWN", base + "/contrast"))
        if marker_scale == "INADEQUATE":
            findings.add(Finding("MARKER_SCALE_INADEQUATE", base + "/marker_scale"))
        elif marker_scale == "UNKNOWN":
            findings.add(Finding("MARKER_SCALE_UNKNOWN", base + "/marker_scale"))
        if match_status in {"UNVERIFIED", "UNKNOWN"}:
            findings.add(Finding("POINT_MATCH_UNRESOLVED", base + "/match_status"))
        declared_observation = any(
            value != "UNKNOWN"
            for value in (visibility, contrast, marker_scale, match_status)
        )
        if declared_observation and evidence_ref is None:
            findings.add(Finding("POINT_EVIDENCE_MISSING", base + "/evidence_ref"))
        if isinstance(evidence_ref, str) and evidence_ref not in evidence_set:
            findings.add(Finding("EVIDENCE_REFERENCE_UNBOUND", base + "/evidence_ref"))
    return sorted(findings)


def _recommendation(findings: Sequence[Finding]) -> str:
    if not findings:
        return "READY_FOR_REVIEW"
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
        or document.get("profile") != "kfm.map.georeference-control-point-evidence-assessment-fixtures.v1"
        or document.get("source_idea_ids") != ["KFM-P18-INV-317"]
        or not isinstance(document.get("base"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], definition: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(document["base"])
    for mutation in definition.get("mutations", []):
        _set(candidate, mutation["path"], mutation["value"])
    if definition.get("recompute_summary", True):
        candidate["control_point_count"] = len(candidate.get("control_points", []))
        candidate["summary"] = expected_summary(candidate)
    candidate["recommendation"] = _recommendation(_assessment_findings(candidate))
    if definition.get("recommendation_mode") == "MISMATCH":
        candidate["recommendation"] = "HOLD" if candidate["recommendation"] != "HOLD" else "DENY"
    elif definition.get("recommendation_mode", "DERIVE") != "DERIVE":
        raise ValueError("unknown recommendation mode")
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
        actual = {
            "outcome": result.outcome,
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        }
        expected = {
            "outcome": definition["expected_outcome"],
            "findings": definition["expected_findings"],
        }
        print(_serialize(result, case=definition["name"]))
        failed |= actual != expected
        outcomes.add(result.outcome)
    failed |= outcomes != {"PASS", "ABSTAIN", "DENY", "ERROR"}
    if not failed:
        print(f"CONFIRMED: {len(cases)} GCP evidence assessment cases passed exact polarity.")
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
