#!/usr/bin/env python3
"""Validate inactive, fixture-only SoilSupportRoleAssessment candidates."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/soil_support_role_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/domains/soil/soil_support_role_assessment/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "soil-support-role-assessment-fixture-only-v1"
FALSE_EFFECTS = {
    key: False
    for key in (
        "source_activated",
        "source_bytes_retained",
        "evidence_resolved",
        "policy_evaluated",
        "human_review_approved",
        "catalog_emitted",
        "promoted",
        "released",
        "published",
    )
}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
    "SOIL_SUPPORT_ROLE_ID_MISMATCH",
    "FIXTURE_MANIFEST_INVALID",
}
MATRIX = {
    "STATIC_SURVEY": {
        "families": {"SSURGO_SDA"},
        "role": "AUTHORITATIVE_SURVEY",
        "geometry": "MAP_UNIT_POLYGON",
        "claims": {"MAP_UNIT_IDENTITY", "PROPERTY_ESTIMATE"},
    },
    "GRIDDED_DERIVATIVE": {
        "families": {"GSSURGO_GNATSGO"},
        "role": "DERIVED_SURFACE",
        "geometry": "GRID_CELL",
        "claims": {"PROPERTY_ESTIMATE"},
    },
    "STATION_OBSERVATION": {
        "families": {"KANSAS_MESONET", "NRCS_SCAN", "NOAA_USCRN"},
        "role": "IN_SITU_OBSERVATION",
        "geometry": "STATION_POINT",
        "claims": {"POINT_MOISTURE_OBSERVATION"},
    },
    "SATELLITE_GRID": {
        "families": {"NASA_SMAP"},
        "role": "REMOTE_SENSING_OBSERVATION",
        "geometry": "GRID_CELL",
        "claims": {"GRID_MOISTURE_ESTIMATE"},
    },
}


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


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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
    except (OSError, UnicodeError):
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


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return f"soil-support-role:{digest[:24]}"


def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate))
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _canonical(values: Any) -> bool:
    return isinstance(values, list) and bool(values) and values == sorted(set(values))


def _datetime(value: Any) -> datetime | None:
    if value is None or not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for key in ("evidence_refs", "claim_classes", "limitations"):
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}"))

    support_type = candidate.get("support_type")
    rule = MATRIX.get(support_type, {})
    if candidate.get("source_family") not in rule.get("families", set()):
        findings.append(Finding("SOURCE_FAMILY_MISMATCH", "/source_family"))
    if candidate.get("authority_role") != rule.get("role"):
        findings.append(Finding("AUTHORITY_ROLE_MISMATCH", "/authority_role"))

    geometry = candidate.get("geometry_support")
    if isinstance(geometry, Mapping):
        if geometry.get("geometry_kind") != rule.get("geometry"):
            findings.append(Finding("GEOMETRY_SUPPORT_MISMATCH", "/geometry_support/geometry_kind"))
        if support_type == "STATION_OBSERVATION" and geometry.get("station_id") is None:
            findings.append(Finding("STATION_ID_REQUIRED", "/geometry_support/station_id"))
        if support_type in {"GRIDDED_DERIVATIVE", "SATELLITE_GRID"} and not isinstance(
            geometry.get("grid_resolution_m"), (int, float)
        ):
            findings.append(Finding("GRID_RESOLUTION_REQUIRED", "/geometry_support/grid_resolution_m"))

    claims = candidate.get("claim_classes")
    if isinstance(claims, list) and not set(claims).issubset(rule.get("claims", set())):
        findings.append(Finding("CLAIM_CLASS_NOT_SUPPORTED", "/claim_classes"))

    depth = candidate.get("depth_support")
    if isinstance(depth, Mapping):
        top, bottom = depth.get("top_cm"), depth.get("bottom_cm")
        if support_type in {"STATION_OBSERVATION", "SATELLITE_GRID"} and (
            not isinstance(top, (int, float))
            or not isinstance(bottom, (int, float))
            or top >= bottom
        ):
            findings.append(Finding("DEPTH_INTERVAL_INVALID", "/depth_support"))
        if support_type in {"STATIC_SURVEY", "GRIDDED_DERIVATIVE"} and (
            top is not None or bottom is not None
        ):
            findings.append(Finding("DEPTH_INTERVAL_NOT_ALLOWED", "/depth_support"))

    temporal = candidate.get("temporal_support")
    if isinstance(temporal, Mapping):
        observed = _datetime(temporal.get("observed_at"))
        retrieved = _datetime(temporal.get("retrieved_at"))
        start = _datetime(temporal.get("valid_from"))
        end = _datetime(temporal.get("valid_to"))
        if support_type in {"STATION_OBSERVATION", "SATELLITE_GRID"} and observed is None:
            findings.append(Finding("OBSERVED_AT_REQUIRED", "/temporal_support/observed_at"))
        if support_type in {"STATIC_SURVEY", "GRIDDED_DERIVATIVE"} and observed is not None:
            findings.append(
                Finding("NONOBSERVATIONAL_SUPPORT_HAS_OBSERVED_AT", "/temporal_support/observed_at")
            )
        if observed is not None and retrieved is not None and observed > retrieved:
            findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal_support"))
        if (start is None) != (end is None) or (
            start is not None and end is not None and start > end
        ):
            findings.append(Finding("VALID_TIME_INVALID", "/temporal_support"))
        if temporal.get("freshness_state") == "UNKNOWN":
            findings.append(Finding("FRESHNESS_UNRESOLVED", "/temporal_support/freshness_state"))

    measurement = candidate.get("measurement")
    if isinstance(measurement, Mapping) and support_type in {
        "STATION_OBSERVATION",
        "SATELLITE_GRID",
    }:
        if measurement.get("variable") != "VOLUMETRIC_WATER_CONTENT" or measurement.get(
            "unit"
        ) not in {"FRACTION", "PERCENT"}:
            findings.append(Finding("MEASUREMENT_SEMANTICS_MISMATCH", "/measurement"))

    if candidate.get("review_state") != "HOLD":
        findings.append(Finding("REVIEW_STATE_OVERCLAIM", "/review_state"))
    if candidate.get("public_use_allowed") is not False:
        findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("AUTHORITY_EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_assessment_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("assessment_id") != expected_id:
            findings.append(Finding("SOIL_SUPPORT_ROLE_ID_MISMATCH", "/assessment_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    if any(item.code in ERROR_CODES or item.code == "SCHEMA_INVALID" for item in ordered):
        return ValidationResult("ERROR", ordered)
    if all(item.code == "FRESHNESS_UNRESOLVED" for item in ordered):
        return ValidationResult("ABSTAIN", ordered)
    return ValidationResult("DENY", ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
        if part
    ]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    if isinstance(current, list):
        current[int(parts[-1])] = copy.deepcopy(value)
    else:
        current[parts[-1]] = copy.deepcopy(value)


def _fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None
        or findings
        or document.get("profile") != "kfm.soil.support-role-assessment-fixtures.v1"
        or not isinstance(document.get("defaults"), dict)
        or not isinstance(document.get("bases"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    defaults = copy.deepcopy(document["defaults"])
    base = document["bases"][case["base"]]
    defaults.update(copy.deepcopy(base))
    candidate = defaults
    for mutation in case.get("mutations", []):
        _set_pointer(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _fixture_document()
    output: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if (
            not isinstance(raw, dict)
            or not isinstance(raw.get("name"), str)
            or raw["name"] in names
        ):
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        output.append((raw, materialize_case(document, raw)))
    return output


def _serialize(result: ValidationResult, *, path: Path | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": SCOPE,
        "authority": {
            key: False
            for key in (
                "source_activation",
                "source_bytes",
                "evidence",
                "policy",
                "human_review",
                "catalog",
                "promotion",
                "release",
                "publication",
                "public_use",
            )
        },
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures() -> int:
    try:
        cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RecursionError):
        print(
            _serialize(
                ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),)),
                path=CASES,
            )
        )
        return 1
    ok = True
    for definition, candidate in cases:
        result = validate_payload(candidate)
        expected = tuple(
            Finding(item["code"], item["path"])
            for item in definition.get("expected_findings", [])
        )
        matches = result.outcome == definition.get("expected_outcome") and result.findings == expected
        print(
            json.dumps(
                {
                    "case": definition["name"],
                    "outcome": result.outcome,
                    "findings": [
                        {"code": item.code, "path": item.path} for item in result.findings
                    ],
                    "matches_expected": matches,
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        ok &= matches
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate an inactive SoilSupportRoleAssessment candidate."
    )
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures and args.file is not None:
        print("--fixtures cannot be combined with a file", file=sys.stderr)
        return 2
    if args.fixtures:
        return replay_fixtures()
    if args.file is None:
        print("a fixture file or --fixtures is required", file=sys.stderr)
        return 2
    result = validate_file(args.file)
    print(_serialize(result, path=args.file))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
