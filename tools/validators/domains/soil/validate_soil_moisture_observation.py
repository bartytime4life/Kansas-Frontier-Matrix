#!/usr/bin/env python3
"""Validate one fixture-first SoilMoistureObservation without network access."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/soil/soil_moisture_observation.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/soil/soil_moisture_observation"
MAX_FILE_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "soil-moisture-observation-fixture-profile-only"

SUPPORT_PROFILES = {
    "station_soil_moisture": {
        "source_role": "IN_SITU_OBSERVATION",
        "key_family": "STATION",
        "spatial_support": "POINT_STATION",
        "depth_kinds": {"SENSOR_DEPTH"},
    },
    "reference_station_soil_climate": {
        "source_role": "REFERENCE_OBSERVATION",
        "key_family": "STATION",
        "spatial_support": "POINT_STATION",
        "depth_kinds": {"SENSOR_DEPTH"},
    },
    "satellite_soil_moisture_grid": {
        "source_role": "SATELLITE_RETRIEVAL",
        "key_family": "GRID_CELL",
        "spatial_support": "GRID_CELL",
        "depth_kinds": {"SURFACE_LAYER", "ROOT_ZONE_LAYER"},
    },
}
NEGATIVE_REASONS = {
    "ABSTAIN": {
        "MISSING_REQUIRED_CONTEXT",
        "STALE_OR_INSUFFICIENT_SUPPORT",
        "UNRESOLVED_EVIDENCE",
    },
    "DENY": {
        "PRIVATE_OPERATIONAL_SENSOR",
        "SENSITIVE_LOCATION",
        "SUPPORT_TYPE_COLLAPSE",
    },
    "ERROR": {"OPERATIONAL_ERROR"},
}


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats an object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    packet_outcome: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def operational_error(self) -> bool:
        return any(
            item.code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE"))
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
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
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
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
        return None, [Finding("INPUT_READ_ERROR", "/")]
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
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("observation_id", None)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def expected_observation_id(candidate: Mapping[str, Any]) -> str:
    return "soil-moisture:" + canonical_spec_hash(candidate).removeprefix("sha256:")[:24]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _canonical_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo == timezone.utc else None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if candidate.get("spec_hash") != canonical_spec_hash(candidate):
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("observation_id") != expected_observation_id(candidate):
            findings.append(Finding("OBSERVATION_ID_MISMATCH", "/observation_id"))
    except (TypeError, ValueError, RecursionError):
        findings.append(Finding("IDENTITY_COMPUTATION_ERROR", "/"))

    support_type = candidate.get("support_type")
    profile = SUPPORT_PROFILES.get(support_type)
    source = _mapping(candidate.get("source"))
    subject = _mapping(candidate.get("subject"))
    measurement = _mapping(candidate.get("measurement"))
    depth = _mapping(measurement.get("depth_support"))
    assessment = _mapping(candidate.get("assessment"))
    time = _mapping(candidate.get("time"))

    if profile:
        if source.get("source_role") != profile["source_role"]:
            findings.append(Finding("SOURCE_ROLE_SUPPORT_MISMATCH", "/source/source_role"))
        if source.get("source_native_key_family") != profile["key_family"]:
            findings.append(
                Finding("SOURCE_KEY_FAMILY_SUPPORT_MISMATCH", "/source/source_native_key_family")
            )
        if subject.get("spatial_support") != profile["spatial_support"]:
            findings.append(
                Finding("SPATIAL_SUPPORT_TYPE_MISMATCH", "/subject/spatial_support")
            )
        if depth.get("kind") not in profile["depth_kinds"]:
            findings.append(Finding("DEPTH_SUPPORT_TYPE_MISMATCH", "/measurement/depth_support/kind"))

    if support_type in {"station_soil_moisture", "reference_station_soil_climate"}:
        if depth.get("kind") == "SENSOR_DEPTH" and not isinstance(
            depth.get("depth_cm"), (int, float)
        ):
            findings.append(Finding("STATION_DEPTH_REQUIRED", "/measurement/depth_support/depth_cm"))
        if subject.get("resolution_m") is not None:
            findings.append(Finding("STATION_GRID_RESOLUTION_FORBIDDEN", "/subject/resolution_m"))
        if subject.get("public_geometry_rule") == "GENERALIZED_GRID":
            findings.append(
                Finding("STATION_GRID_GEOMETRY_RULE_FORBIDDEN", "/subject/public_geometry_rule")
            )
    elif support_type == "satellite_soil_moisture_grid":
        if depth.get("depth_cm") is not None:
            findings.append(
                Finding("SATELLITE_SENSOR_DEPTH_FORBIDDEN", "/measurement/depth_support/depth_cm")
            )
        if not isinstance(subject.get("resolution_m"), (int, float)):
            findings.append(Finding("SATELLITE_RESOLUTION_REQUIRED", "/subject/resolution_m"))
        if subject.get("public_geometry_rule") == "EXACT_PUBLIC_STATION":
            findings.append(
                Finding("SATELLITE_STATION_GEOMETRY_RULE_FORBIDDEN", "/subject/public_geometry_rule")
            )

    for values, code, field in (
        (_array(measurement.get("qc_flags")), "QC_FLAGS_NOT_CANONICAL", "/measurement/qc_flags"),
        (_array(assessment.get("reason_codes")), "REASON_CODES_NOT_CANONICAL", "/assessment/reason_codes"),
        (_array(assessment.get("evidence_refs")), "EVIDENCE_REFS_NOT_CANONICAL", "/assessment/evidence_refs"),
        (_array(assessment.get("limitations")), "LIMITATIONS_NOT_CANONICAL", "/assessment/limitations"),
    ):
        if not _canonical_strings(values):
            findings.append(Finding(code, field))

    observed = _parse_utc(time.get("observed_at"))
    retrieved = _parse_utc(time.get("retrieved_at"))
    valid_start = _parse_utc(time.get("valid_start"))
    valid_end = (
        _parse_utc(time.get("valid_end")) if time.get("valid_end") is not None else None
    )
    source_published = (
        _parse_utc(time.get("source_published_at"))
        if time.get("source_published_at") is not None
        else None
    )
    for value, field in (
        (observed, "/time/observed_at"),
        (retrieved, "/time/retrieved_at"),
        (valid_start, "/time/valid_start"),
    ):
        if value is None:
            findings.append(Finding("UTC_TIMESTAMP_REQUIRED", field))
    if time.get("valid_end") is not None and valid_end is None:
        findings.append(Finding("UTC_TIMESTAMP_REQUIRED", "/time/valid_end"))
    if time.get("source_published_at") is not None and source_published is None:
        findings.append(Finding("UTC_TIMESTAMP_REQUIRED", "/time/source_published_at"))
    if observed and retrieved and retrieved < observed:
        findings.append(Finding("RETRIEVAL_PRECEDES_OBSERVATION", "/time/retrieved_at"))
    if valid_start and valid_end and valid_end <= valid_start:
        findings.append(Finding("VALID_WINDOW_NOT_ORDERED", "/time/valid_end"))

    outcome = assessment.get("outcome")
    value = measurement.get("normalized_value")
    reason_set = {
        item for item in _array(assessment.get("reason_codes")) if isinstance(item, str)
    }
    evidence = _array(assessment.get("evidence_refs"))

    if outcome == "ANSWER":
        if not isinstance(value, (int, float)):
            findings.append(Finding("ANSWER_VALUE_REQUIRED", "/measurement/normalized_value"))
        if "OBSERVATION_SUPPORTED" not in reason_set:
            findings.append(Finding("ANSWER_REASON_REQUIRED", "/assessment/reason_codes"))
        if not evidence:
            findings.append(Finding("ANSWER_EVIDENCE_REQUIRED", "/assessment/evidence_refs"))
        if subject.get("public_geometry_rule") in {"HIDDEN", "DENIED"}:
            findings.append(Finding("ANSWER_PUBLIC_GEOMETRY_UNAVAILABLE", "/subject/public_geometry_rule"))
    elif outcome in NEGATIVE_REASONS:
        if value is not None:
            findings.append(Finding("NEGATIVE_OUTCOME_VALUE_FORBIDDEN", "/measurement/normalized_value"))
        if not (reason_set & NEGATIVE_REASONS[outcome]):
            findings.append(Finding(f"{outcome}_REASON_REQUIRED", "/assessment/reason_codes"))
        if outcome != "ERROR" and not evidence:
            findings.append(Finding("NEGATIVE_OUTCOME_EVIDENCE_REQUIRED", "/assessment/evidence_refs"))
        if outcome == "DENY" and subject.get("public_geometry_rule") not in {"HIDDEN", "DENIED"}:
            findings.append(Finding("DENY_GEOMETRY_RULE_REQUIRED", "/subject/public_geometry_rule"))

    governance = _mapping(candidate.get("governance"))
    for key in (
        "source_activated",
        "evidence_resolved",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "public_use_allowed",
    ):
        if governance.get(key) is not False:
            findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", f"/governance/{key}"))
    if governance.get("release_manifest_ref") is not None:
        findings.append(
            Finding("INACTIVE_PROFILE_RELEASE_REF_FORBIDDEN", "/governance/release_manifest_ref")
        )
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    assessment = candidate.get("assessment")
    packet_outcome = assessment.get("outcome") if isinstance(assessment, dict) else None
    return ValidationResult(
        tuple(sorted(set(findings))),
        packet_outcome if isinstance(packet_outcome, str) else None,
    )


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": (
                "PASS"
                if result.ok
                else "ERROR"
                if result.operational_error
                else "FAIL"
            ),
            "packet_outcome": result.packet_outcome,
            "scope": SCOPE,
            "authority": {
                "network_fetch": False,
                "source_activation": False,
                "evidence_resolution": False,
                "policy_evaluation": False,
                "promotion": False,
                "release": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 2
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.json"))
    if not valid or not invalid or not isinstance(manifest, dict):
        return 2
    passed = True
    for path in valid:
        result = validate_file(path)
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_file(path)
        print(_serialize(path, result))
        expected = sorted(manifest.get(path.name, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": path.name,
                        "expected_codes": expected,
                        "actual_codes": actual,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-first SoilMoistureObservation."
    )
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    if not args.path:
        parser.error("path is required unless --fixtures is used")
    path = Path(args.path)
    result = validate_file(path)
    print(_serialize(path, result))
    if result.ok:
        return 0
    return 2 if result.operational_error else 1


if __name__ == "__main__":
    raise SystemExit(main())
