#!/usr/bin/env python3
"""Normalize one synthetic Kansas Mesonet soil fixture without source access.

This fixture-only boundary preserves station identity, observation depth, native
cadence, station health, source timezone, quality flags, rights/consent posture,
generalized spatial support, and caller-supplied provenance. It performs no
network access, lifecycle writes, evidence resolution, policy evaluation,
promotion, release, publication, alerting, or agronomic interpretation.
"""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass
from datetime import datetime
from typing import Any

OUTCOMES = frozenset({"NORMALIZED_FIXTURE", "HOLD", "DENY", "ERROR"})
PRECISE_LOCATION_FIELDS = frozenset(
    {
        "bbox",
        "centroid",
        "easting",
        "lat",
        "latitude",
        "lng",
        "lon",
        "longitude",
        "northing",
        "x",
        "y",
    }
)
ERROR_CODES = frozenset(
    {"CANDIDATE_NOT_OBJECT", "OBSERVATION_INVALID", "RIGHTS_INVALID", "STATION_INVALID"}
)
HOLD_CODES = frozenset({"STATION_HEALTH_HOLD"})


@dataclass(frozen=True, order=True)
class Finding:
    """Stable, value-free finding safe for deterministic test output."""

    code: str
    path: str


@dataclass(frozen=True)
class NormalizationResult:
    """Bounded result; a normalized fixture is not a released observation."""

    outcome: str
    reason_code: str
    candidate: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "NORMALIZED_FIXTURE" and self.candidate is not None


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _canonical_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z") or "T" not in value:
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    offset = parsed.utcoffset()
    return parsed.tzinfo is not None and offset is not None and offset.total_seconds() == 0


def _canonical_strings(value: object, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (bool(value) or not nonempty)
        and all(_nonempty_string(item) for item in value)
        and value == sorted(set(value))
    )


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _unknown_fields(candidate: dict[object, object], allowed: set[str]) -> list[object]:
    return sorted(
        (field for field in candidate if field not in allowed),
        key=lambda field: (type(field).__name__, repr(field)),
    )


def _validate_station(findings: set[Finding], station: object) -> None:
    if not isinstance(station, dict):
        _add(findings, "STATION_INVALID", "/station")
        return

    allowed = {"station_id", "station_health", "spatial_support"}
    for field in _unknown_fields(station, allowed):
        _add(findings, "STATION_FIELD_UNKNOWN", f"/station/{field}")

    if not _nonempty_string(station.get("station_id")):
        _add(findings, "STATION_ID_MISSING", "/station/station_id")
    if station.get("station_health") != "HEALTHY_FIXTURE":
        _add(findings, "STATION_HEALTH_HOLD", "/station/station_health")

    support = station.get("spatial_support")
    if not isinstance(support, dict):
        _add(findings, "SPATIAL_SUPPORT_INVALID", "/station/spatial_support")
        return
    for field in support:
        if isinstance(field, str) and field.casefold() in PRECISE_LOCATION_FIELDS:
            _add(
                findings,
                "PRECISE_LOCATION_FIELD_FORBIDDEN",
                f"/station/spatial_support/{field}",
            )
    for field in _unknown_fields(support, {"kind", "county_fips"}):
        _add(
            findings,
            "SPATIAL_SUPPORT_FIELD_UNKNOWN",
            f"/station/spatial_support/{field}",
        )
    if support.get("kind") != "generalized_county":
        _add(findings, "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", "/station/spatial_support/kind")
    county_fips = support.get("county_fips")
    if not (
        isinstance(county_fips, str)
        and len(county_fips) == 5
        and county_fips.isdigit()
    ):
        _add(findings, "COUNTY_FIPS_INVALID", "/station/spatial_support/county_fips")


def _validate_observation(findings: set[Finding], observation: object) -> None:
    if not isinstance(observation, dict):
        _add(findings, "OBSERVATION_INVALID", "/observation")
        return

    allowed = {
        "aggregation_receipt_ref",
        "depth_cm",
        "measure",
        "native_cadence_minutes",
        "observed_at",
        "output_cadence_minutes",
        "qc_flags",
        "source_timezone",
        "unit",
        "value",
    }
    for field in _unknown_fields(observation, allowed):
        _add(findings, "OBSERVATION_FIELD_UNKNOWN", f"/observation/{field}")

    if observation.get("measure") != "volumetric_water_content":
        _add(findings, "MEASURE_UNSUPPORTED", "/observation/measure")
    if observation.get("unit") != "m3/m3":
        _add(findings, "UNIT_UNSUPPORTED", "/observation/unit")

    depth = observation.get("depth_cm")
    if not _finite_number(depth) or float(depth) < 0:
        _add(findings, "DEPTH_INVALID", "/observation/depth_cm")
    value = observation.get("value")
    if not _finite_number(value) or not 0 <= float(value) <= 1:
        _add(findings, "VALUE_OUT_OF_RANGE", "/observation/value")
    if not _canonical_utc(observation.get("observed_at")):
        _add(findings, "OBSERVATION_TIME_NOT_UTC", "/observation/observed_at")
    if not _nonempty_string(observation.get("source_timezone")):
        _add(findings, "SOURCE_TIMEZONE_MISSING", "/observation/source_timezone")
    if not _canonical_strings(observation.get("qc_flags"), nonempty=True):
        _add(findings, "QC_FLAGS_NOT_CANONICAL", "/observation/qc_flags")

    native = observation.get("native_cadence_minutes")
    output = observation.get("output_cadence_minutes")
    if not _finite_number(native) or float(native) <= 0:
        _add(findings, "NATIVE_CADENCE_INVALID", "/observation/native_cadence_minutes")
    if not _finite_number(output) or float(output) <= 0:
        _add(findings, "OUTPUT_CADENCE_INVALID", "/observation/output_cadence_minutes")
    if _finite_number(native) and _finite_number(output) and float(native) != float(output):
        if not _nonempty_string(observation.get("aggregation_receipt_ref")):
            _add(
                findings,
                "CADENCE_COLLAPSE_WITHOUT_RECEIPT",
                "/observation/output_cadence_minutes",
            )
    elif observation.get("aggregation_receipt_ref") is not None:
        _add(
            findings,
            "UNNEEDED_AGGREGATION_RECEIPT",
            "/observation/aggregation_receipt_ref",
        )


def _validate_rights(findings: set[Finding], rights: object) -> None:
    if not isinstance(rights, dict):
        _add(findings, "RIGHTS_INVALID", "/rights")
        return
    if set(rights) != {"operator_consent_state", "rights_state"}:
        _add(findings, "RIGHTS_FIELDS_INVALID", "/rights")
    if rights.get("rights_state") != "fixture_only":
        _add(findings, "RIGHTS_NOT_FIXTURE_ONLY", "/rights/rights_state")
    if rights.get("operator_consent_state") != "fixture_only":
        _add(
            findings,
            "OPERATOR_CONSENT_NOT_FIXTURE_ONLY",
            "/rights/operator_consent_state",
        )


def _validate_governance(findings: set[Finding], governance: object) -> None:
    expected = {
        "promotion_eligible": False,
        "public_use_allowed": False,
        "release_state": "not_released",
        "review_state": "fixture_only",
    }
    if not isinstance(governance, dict):
        _add(findings, "GOVERNANCE_INVALID", "/governance")
        return
    if set(governance) != set(expected):
        _add(findings, "GOVERNANCE_FIELDS_INVALID", "/governance")
    for field, expected_value in expected.items():
        if governance.get(field) != expected_value:
            _add(findings, "GOVERNANCE_STATE_INVALID", f"/governance/{field}")


def _classify(findings: tuple[Finding, ...]) -> tuple[str, str]:
    if not findings:
        return "NORMALIZED_FIXTURE", "MESONET_FIXTURE_NORMALIZED"
    codes = {finding.code for finding in findings}
    if codes & ERROR_CODES:
        return "ERROR", "MESONET_FIXTURE_INPUT_ERROR"
    if codes <= HOLD_CODES:
        return "HOLD", "MESONET_STATION_HEALTH_UNRESOLVED"
    return "DENY", "MESONET_FIXTURE_NORMALIZATION_DENIED"


def normalize_fixture(candidate: object) -> NormalizationResult:
    """Return a deterministic, non-authoritative normalization result."""

    if not isinstance(candidate, dict):
        findings = (Finding("CANDIDATE_NOT_OBJECT", "/"),)
        return NormalizationResult(
            outcome="ERROR",
            reason_code="MESONET_FIXTURE_INPUT_ERROR",
            candidate=None,
            findings=findings,
        )

    findings: set[Finding] = set()
    allowed = {
        "evidence_refs",
        "governance",
        "object_type",
        "observation",
        "record_id",
        "rights",
        "run_receipt_ref",
        "schema_version",
        "source_descriptor_ref",
        "source_role",
        "station",
        "support_type",
    }
    for field in _unknown_fields(candidate, allowed):
        _add(findings, "TOP_LEVEL_FIELD_UNKNOWN", f"/{field}")
    if candidate.get("object_type") != "SyntheticMesonetSoilObservation":
        _add(findings, "OBJECT_TYPE_INVALID", "/object_type")
    if candidate.get("schema_version") != "1.0.0":
        _add(findings, "SCHEMA_VERSION_INVALID", "/schema_version")
    if not _nonempty_string(candidate.get("record_id")):
        _add(findings, "RECORD_ID_MISSING", "/record_id")
    if candidate.get("source_role") != "fixture_only":
        _add(findings, "SOURCE_ROLE_NOT_FIXTURE_ONLY", "/source_role")
    if candidate.get("support_type") != "station_soil_moisture":
        _add(findings, "SUPPORT_TYPE_COLLAPSE", "/support_type")
    if not _nonempty_string(candidate.get("source_descriptor_ref")):
        _add(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "/source_descriptor_ref")
    if not _nonempty_string(candidate.get("run_receipt_ref")):
        _add(findings, "RUN_RECEIPT_REF_MISSING", "/run_receipt_ref")
    if not _canonical_strings(candidate.get("evidence_refs"), nonempty=True):
        _add(findings, "EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs")

    _validate_station(findings, candidate.get("station"))
    _validate_observation(findings, candidate.get("observation"))
    _validate_rights(findings, candidate.get("rights"))
    _validate_governance(findings, candidate.get("governance"))

    ordered = tuple(sorted(findings))
    outcome, reason_code = _classify(ordered)
    normalized = None
    if not ordered:
        normalized = copy.deepcopy(candidate)
        normalized["normalization_state"] = "fixture_only_normalized"
    return NormalizationResult(
        outcome=outcome,
        reason_code=reason_code,
        candidate=normalized,
        findings=ordered,
    )
