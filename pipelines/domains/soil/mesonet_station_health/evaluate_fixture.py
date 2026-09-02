#!/usr/bin/env python3
"""Evaluate synthetic Kansas Mesonet station health without source access.

The evaluator consumes fixture-only normalized station records. It performs no
network access, lifecycle writes, source activation, evidence resolution, policy
approval, promotion, release, publication, alerting, or agronomic interpretation.
"""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass
from datetime import datetime
from typing import Any

OUTCOMES = frozenset({"HEALTHY_FIXTURE", "HOLD", "DENY", "ERROR"})
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


@dataclass(frozen=True, order=True)
class Finding:
    """Stable finding that does not echo source values."""

    code: str
    path: str


@dataclass(frozen=True)
class EvaluationResult:
    """Bounded result for one synthetic batch."""

    outcome: str
    reason_code: str
    assessment: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.assessment is not None and not self.findings


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _canonical_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z") or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    offset = parsed.utcoffset()
    if parsed.tzinfo is None or offset is None or offset.total_seconds() != 0:
        return None
    return parsed


def _canonical_strings(value: object, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (bool(value) or not nonempty)
        and all(_nonempty_string(item) for item in value)
        and value == sorted(set(value))
    )


def _unknown_fields(candidate: dict[object, object], allowed: set[str]) -> list[object]:
    return sorted(
        (field for field in candidate if field not in allowed),
        key=lambda field: (type(field).__name__, repr(field)),
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


def _validate_rights(findings: set[Finding], rights: object) -> None:
    expected = {
        "rights_state": "fixture_only",
        "operator_consent_state": "fixture_only",
    }
    if not isinstance(rights, dict):
        _add(findings, "RIGHTS_INVALID", "/rights")
        return
    if set(rights) != set(expected):
        _add(findings, "RIGHTS_FIELDS_INVALID", "/rights")
    for field, expected_value in expected.items():
        if rights.get(field) != expected_value:
            _add(findings, "RIGHTS_STATE_INVALID", f"/rights/{field}")


def _validate_thresholds(findings: set[Finding], thresholds: object) -> None:
    required = {
        "expected_interval_minutes",
        "degraded_after_multiplier",
        "minimum_coverage_fraction",
        "maximum_degraded_fraction",
        "max_untriaged_anomalies",
        "z_score_abs_threshold",
        "relative_jump_fraction_threshold",
    }
    if not isinstance(thresholds, dict):
        _add(findings, "THRESHOLDS_INVALID", "/thresholds")
        return
    for field in _unknown_fields(thresholds, required):
        _add(findings, "THRESHOLD_UNKNOWN", f"/thresholds/{field}")
    for field in sorted(required - set(thresholds)):
        _add(findings, "THRESHOLD_MISSING", f"/thresholds/{field}")

    positive = (
        "expected_interval_minutes",
        "degraded_after_multiplier",
        "z_score_abs_threshold",
    )
    for field in positive:
        value = thresholds.get(field)
        if not _finite_number(value) or float(value) <= 0:
            _add(findings, "THRESHOLD_INVALID", f"/thresholds/{field}")

    for field in ("minimum_coverage_fraction", "maximum_degraded_fraction"):
        value = thresholds.get(field)
        if not _finite_number(value) or not 0 <= float(value) <= 1:
            _add(findings, "THRESHOLD_INVALID", f"/thresholds/{field}")
    if thresholds.get("maximum_degraded_fraction") == 0:
        _add(
            findings,
            "THRESHOLD_INVALID",
            "/thresholds/maximum_degraded_fraction",
        )

    max_untriaged = thresholds.get("max_untriaged_anomalies")
    if (
        not isinstance(max_untriaged, int)
        or isinstance(max_untriaged, bool)
        or max_untriaged < 0
    ):
        _add(
            findings,
            "THRESHOLD_INVALID",
            "/thresholds/max_untriaged_anomalies",
        )

    relative = thresholds.get("relative_jump_fraction_threshold")
    if not _finite_number(relative) or float(relative) < 0:
        _add(
            findings,
            "THRESHOLD_INVALID",
            "/thresholds/relative_jump_fraction_threshold",
        )


def _validate_spatial_support(
    findings: set[Finding], support: object, station_index: int
) -> None:
    base = f"/stations/{station_index}/spatial_support"
    if not isinstance(support, dict):
        _add(findings, "SPATIAL_SUPPORT_INVALID", base)
        return
    for field in support:
        if isinstance(field, str) and field.casefold() in PRECISE_LOCATION_FIELDS:
            _add(findings, "PRECISE_LOCATION_FIELD_FORBIDDEN", f"{base}/{field}")
    for field in _unknown_fields(support, {"kind", "county_fips"}):
        _add(findings, "SPATIAL_SUPPORT_FIELD_UNKNOWN", f"{base}/{field}")
    if support.get("kind") != "generalized_county":
        _add(findings, "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", f"{base}/kind")
    county_fips = support.get("county_fips")
    if not (
        isinstance(county_fips, str)
        and len(county_fips) == 5
        and county_fips.isdigit()
    ):
        _add(findings, "COUNTY_FIPS_INVALID", f"{base}/county_fips")


def _validate_sample(
    findings: set[Finding],
    sample: object,
    station_index: int,
    sample_index: int,
    evaluated_at: datetime,
) -> None:
    base = f"/stations/{station_index}/samples/{sample_index}"
    if not isinstance(sample, dict):
        _add(findings, "SAMPLE_INVALID", base)
        return
    allowed = {
        "observed_at",
        "value",
        "z_score",
        "relative_jump_fraction",
        "triage_state",
        "qc_flags",
    }
    for field in _unknown_fields(sample, allowed):
        _add(findings, "SAMPLE_FIELD_UNKNOWN", f"{base}/{field}")
    for field in sorted(allowed - set(sample)):
        _add(findings, "SAMPLE_FIELD_MISSING", f"{base}/{field}")

    observed = _canonical_utc(sample.get("observed_at"))
    if observed is None:
        _add(findings, "SAMPLE_TIME_INVALID", f"{base}/observed_at")
    elif observed > evaluated_at:
        _add(findings, "SAMPLE_TIME_IN_FUTURE", f"{base}/observed_at")

    value = sample.get("value")
    if not _finite_number(value) or not 0 <= float(value) <= 1:
        _add(findings, "SAMPLE_VALUE_OUT_OF_RANGE", f"{base}/value")

    if not _finite_number(sample.get("z_score")):
        _add(findings, "Z_SCORE_INVALID", f"{base}/z_score")
    relative = sample.get("relative_jump_fraction")
    if not _finite_number(relative) or float(relative) < 0:
        _add(
            findings,
            "RELATIVE_JUMP_INVALID",
            f"{base}/relative_jump_fraction",
        )
    if sample.get("triage_state") not in {"CLEAR", "TRIAGED", "UNTRIAGED"}:
        _add(findings, "TRIAGE_STATE_INVALID", f"{base}/triage_state")
    if not _canonical_strings(sample.get("qc_flags"), nonempty=True):
        _add(findings, "QC_FLAGS_NOT_CANONICAL", f"{base}/qc_flags")


def _validate_station(
    findings: set[Finding],
    station: object,
    station_index: int,
    evaluated_at: datetime,
) -> None:
    base = f"/stations/{station_index}"
    if not isinstance(station, dict):
        _add(findings, "STATION_INVALID", base)
        return
    allowed = {
        "station_id",
        "source_timezone",
        "spatial_support",
        "last_reported_at",
        "samples",
    }
    for field in _unknown_fields(station, allowed):
        _add(findings, "STATION_FIELD_UNKNOWN", f"{base}/{field}")
    for field in sorted(allowed - set(station)):
        _add(findings, "STATION_FIELD_MISSING", f"{base}/{field}")

    if not _nonempty_string(station.get("station_id")):
        _add(findings, "STATION_ID_INVALID", f"{base}/station_id")
    if not _nonempty_string(station.get("source_timezone")):
        _add(findings, "SOURCE_TIMEZONE_INVALID", f"{base}/source_timezone")

    last_reported = _canonical_utc(station.get("last_reported_at"))
    if last_reported is None:
        _add(findings, "LAST_REPORTED_TIME_INVALID", f"{base}/last_reported_at")
    elif last_reported > evaluated_at:
        _add(findings, "LAST_REPORTED_IN_FUTURE", f"{base}/last_reported_at")

    _validate_spatial_support(findings, station.get("spatial_support"), station_index)

    samples = station.get("samples")
    if not isinstance(samples, list) or not samples:
        _add(findings, "SAMPLES_INVALID", f"{base}/samples")
        return
    for sample_index, sample in enumerate(samples):
        _validate_sample(
            findings,
            sample,
            station_index,
            sample_index,
            evaluated_at,
        )


def _candidate_findings(candidate: dict[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    allowed = {
        "object_type",
        "schema_version",
        "assessment_id",
        "evaluated_at",
        "source_descriptor_ref",
        "run_receipt_ref",
        "evidence_refs",
        "thresholds",
        "stations",
        "rights",
        "governance",
    }
    for field in _unknown_fields(candidate, allowed):
        _add(findings, "TOP_LEVEL_FIELD_UNKNOWN", f"/{field}")
    for field in sorted(allowed - set(candidate)):
        _add(findings, "TOP_LEVEL_FIELD_MISSING", f"/{field}")

    if candidate.get("object_type") != "SyntheticMesonetStationHealthBatch":
        _add(findings, "OBJECT_TYPE_INVALID", "/object_type")
    if candidate.get("schema_version") != "1.0.0":
        _add(findings, "SCHEMA_VERSION_INVALID", "/schema_version")
    if not _nonempty_string(candidate.get("assessment_id")):
        _add(findings, "ASSESSMENT_ID_INVALID", "/assessment_id")
    if not _nonempty_string(candidate.get("source_descriptor_ref")):
        _add(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "/source_descriptor_ref")
    if not _nonempty_string(candidate.get("run_receipt_ref")):
        _add(findings, "RUN_RECEIPT_REF_MISSING", "/run_receipt_ref")
    if not _canonical_strings(candidate.get("evidence_refs"), nonempty=True):
        _add(findings, "EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs")

    evaluated_at = _canonical_utc(candidate.get("evaluated_at"))
    if evaluated_at is None:
        _add(findings, "EVALUATED_AT_INVALID", "/evaluated_at")

    _validate_thresholds(findings, candidate.get("thresholds"))
    _validate_rights(findings, candidate.get("rights"))
    _validate_governance(findings, candidate.get("governance"))

    stations = candidate.get("stations")
    if not isinstance(stations, list) or not stations:
        _add(findings, "STATIONS_INVALID", "/stations")
    elif evaluated_at is not None:
        station_ids: list[str] = []
        for index, station in enumerate(stations):
            _validate_station(findings, station, index, evaluated_at)
            if isinstance(station, dict) and isinstance(station.get("station_id"), str):
                station_ids.append(station["station_id"])
        if station_ids != sorted(station_ids) or len(station_ids) != len(set(station_ids)):
            _add(findings, "STATION_IDS_NOT_CANONICAL", "/stations")

    return tuple(sorted(findings))


def _classify_invalid(findings: tuple[Finding, ...]) -> tuple[str, str]:
    structural_codes = {
        "CANDIDATE_NOT_OBJECT",
        "EVALUATED_AT_INVALID",
        "STATIONS_INVALID",
        "STATION_INVALID",
        "SAMPLES_INVALID",
    }
    if any(finding.code in structural_codes for finding in findings):
        return "ERROR", "MESONET_HEALTH_INPUT_ERROR"
    return "DENY", "MESONET_HEALTH_INPUT_DENIED"


def _station_result(
    station: dict[str, Any],
    evaluated_at: datetime,
    thresholds: dict[str, Any],
) -> dict[str, Any]:
    last_reported = _canonical_utc(station["last_reported_at"])
    assert last_reported is not None
    age_minutes = max(0.0, (evaluated_at - last_reported).total_seconds() / 60.0)
    stale_after = (
        float(thresholds["expected_interval_minutes"])
        * float(thresholds["degraded_after_multiplier"])
    )
    stale = age_minutes >= stale_after

    reason_codes: set[str] = set()
    if stale:
        reason_codes.add("STALE_REPORT")

    anomaly_count = 0
    untriaged_count = 0
    for sample in station["samples"]:
        z_outlier = abs(float(sample["z_score"])) > float(
            thresholds["z_score_abs_threshold"]
        )
        relative_outlier = float(sample["relative_jump_fraction"]) >= float(
            thresholds["relative_jump_fraction_threshold"]
        )
        if z_outlier:
            reason_codes.add("Z_SCORE_OUTLIER")
        if relative_outlier:
            reason_codes.add("RELATIVE_JUMP")
        if z_outlier or relative_outlier:
            anomaly_count += 1
            if sample["triage_state"] == "UNTRIAGED":
                untriaged_count += 1
                reason_codes.add("UNTRIAGED_ANOMALY")

    if untriaged_count:
        state = "ANOMALOUS_UNTRIAGED"
    elif anomaly_count:
        state = "ANOMALOUS_TRIAGED"
    elif stale:
        state = "DEGRADED"
    else:
        state = "HEALTHY"

    return {
        "station_id": station["station_id"],
        "spatial_support": copy.deepcopy(station["spatial_support"]),
        "station_state": state,
        "age_minutes": round(age_minutes, 6),
        "anomaly_count": anomaly_count,
        "untriaged_anomaly_count": untriaged_count,
        "reason_codes": sorted(reason_codes),
    }


def evaluate_fixture(candidate: object) -> EvaluationResult:
    """Evaluate one synthetic batch and return a finite non-release result."""

    if not isinstance(candidate, dict):
        finding = Finding("CANDIDATE_NOT_OBJECT", "/")
        return EvaluationResult(
            outcome="ERROR",
            reason_code="MESONET_HEALTH_INPUT_ERROR",
            assessment=None,
            findings=(finding,),
        )

    findings = _candidate_findings(candidate)
    if findings:
        outcome, reason_code = _classify_invalid(findings)
        return EvaluationResult(
            outcome=outcome,
            reason_code=reason_code,
            assessment=None,
            findings=findings,
        )

    evaluated_at = _canonical_utc(candidate["evaluated_at"])
    assert evaluated_at is not None
    thresholds = candidate["thresholds"]
    station_results = [
        _station_result(station, evaluated_at, thresholds)
        for station in candidate["stations"]
    ]

    total = len(station_results)
    degraded = sum(
        1 for station in station_results if "STALE_REPORT" in station["reason_codes"]
    )
    fresh = total - degraded
    anomalous = sum(1 for station in station_results if station["anomaly_count"] > 0)
    untriaged = sum(
        station["untriaged_anomaly_count"] for station in station_results
    )
    coverage = fresh / total
    degraded_fraction = degraded / total

    decision_reasons: set[str] = set()
    if coverage < float(thresholds["minimum_coverage_fraction"]):
        decision_reasons.add("COVERAGE_BELOW_MINIMUM")
    if degraded_fraction >= float(thresholds["maximum_degraded_fraction"]):
        decision_reasons.add("ROSTER_DEGRADED_THRESHOLD")
    if untriaged > int(thresholds["max_untriaged_anomalies"]):
        decision_reasons.add("UNTRIAGED_ANOMALIES_PRESENT")

    outcome = "HOLD" if decision_reasons else "HEALTHY_FIXTURE"
    reason_code = (
        "MESONET_HEALTH_REVIEW_REQUIRED"
        if decision_reasons
        else "MESONET_HEALTH_FIXTURE_ACCEPTED"
    )

    assessment = {
        "object_type": "MesonetStationHealthAssessment",
        "schema_version": "1.0.0",
        "assessment_id": candidate["assessment_id"],
        "evaluated_at": candidate["evaluated_at"],
        "source_descriptor_ref": candidate["source_descriptor_ref"],
        "run_receipt_ref": candidate["run_receipt_ref"],
        "evidence_refs": copy.deepcopy(candidate["evidence_refs"]),
        "thresholds": copy.deepcopy(thresholds),
        "summary": {
            "total_stations": total,
            "fresh_stations": fresh,
            "degraded_stations": degraded,
            "anomalous_stations": anomalous,
            "untriaged_anomalies": untriaged,
            "coverage_fraction": round(coverage, 6),
            "degraded_fraction": round(degraded_fraction, 6),
        },
        "stations": station_results,
        "decision": {
            "outcome": outcome,
            "reason_codes": sorted(decision_reasons),
        },
        "rights": copy.deepcopy(candidate["rights"]),
        "governance": copy.deepcopy(candidate["governance"]),
    }
    return EvaluationResult(
        outcome=outcome,
        reason_code=reason_code,
        assessment=assessment,
        findings=(),
    )
