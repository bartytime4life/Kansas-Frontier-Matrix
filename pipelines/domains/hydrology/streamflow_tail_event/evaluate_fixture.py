#!/usr/bin/env python3
"""Evaluate synthetic seasonal streamflow tails without source access."""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass
from datetime import datetime
from typing import Any

PRECISE_LOCATION_FIELDS = {
    "bbox", "centroid", "easting", "lat", "latitude", "lng", "lon",
    "longitude", "northing", "x", "y",
}
BLOCKING_QUALIFIERS = {"Eqp", "Ice", "SensorError"}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class EvaluationResult:
    outcome: str
    reason_code: str
    assessment: dict[str, Any] | None
    findings: tuple[Finding, ...] = ()

    @property
    def ok(self) -> bool:
        return self.assessment is not None and not self.findings


def _utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z") or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    offset = parsed.utcoffset()
    return parsed if offset is not None and offset.total_seconds() == 0 else None


def _number(value: object, *, minimum: float = 0.0) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and float(value) >= minimum
    )


def _strings(value: object, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (bool(value) or not nonempty)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
        and value == sorted(set(value))
    )


def _fail(outcome: str, reason: str, *findings: Finding) -> EvaluationResult:
    return EvaluationResult(outcome, reason, None, tuple(sorted(findings)))


def _validate_candidate(candidate: dict[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    required = {
        "object_type", "schema_version", "assessment_id", "evaluated_at", "site",
        "source_descriptor_ref", "run_receipt_ref", "evidence_refs", "thresholds",
        "baseline", "readings", "rights", "governance",
    }
    for field in sorted(required - set(candidate)):
        findings.add(Finding("FIELD_MISSING", f"/{field}"))
    for field in sorted(set(candidate) - required):
        findings.add(Finding("FIELD_UNKNOWN", f"/{field}"))
    if findings:
        return tuple(sorted(findings))

    if candidate["object_type"] != "SyntheticStreamflowTailBatch":
        findings.add(Finding("OBJECT_TYPE_INVALID", "/object_type"))
    if candidate["schema_version"] != "1.0.0":
        findings.add(Finding("SCHEMA_VERSION_INVALID", "/schema_version"))
    for field in ("assessment_id", "source_descriptor_ref", "run_receipt_ref"):
        if not isinstance(candidate[field], str) or not candidate[field].strip():
            findings.add(Finding("STRING_INVALID", f"/{field}"))
    evaluated_at = _utc(candidate["evaluated_at"])
    if evaluated_at is None:
        findings.add(Finding("TIME_INVALID", "/evaluated_at"))
    if not _strings(candidate["evidence_refs"], nonempty=True):
        findings.add(Finding("EVIDENCE_REFS_INVALID", "/evidence_refs"))

    site = candidate["site"]
    if not isinstance(site, dict):
        findings.add(Finding("SITE_INVALID", "/site"))
    else:
        if set(site) != {"site_id", "spatial_support", "regulation_context"}:
            findings.add(Finding("SITE_FIELDS_INVALID", "/site"))
        site_id = site.get("site_id")
        if not isinstance(site_id, str) or not site_id.isdigit() or not 8 <= len(site_id) <= 15:
            findings.add(Finding("SITE_ID_INVALID", "/site/site_id"))
        if site.get("regulation_context") not in {
            "unregulated_fixture", "regulated_context_limited"
        }:
            findings.add(Finding("REGULATION_CONTEXT_INVALID", "/site/regulation_context"))
        support = site.get("spatial_support")
        if not isinstance(support, dict):
            findings.add(Finding("SPATIAL_SUPPORT_INVALID", "/site/spatial_support"))
        else:
            for field in support:
                if isinstance(field, str) and field.casefold() in PRECISE_LOCATION_FIELDS:
                    findings.add(Finding(
                        "PRECISE_LOCATION_FIELD_FORBIDDEN",
                        f"/site/spatial_support/{field}",
                    ))
            if set(support) != {"kind", "huc12"}:
                findings.add(Finding("SPATIAL_SUPPORT_FIELDS_INVALID", "/site/spatial_support"))
            if support.get("kind") != "generalized_huc12":
                findings.add(Finding("SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", "/site/spatial_support/kind"))
            huc12 = support.get("huc12")
            if not isinstance(huc12, str) or len(huc12) != 12 or not huc12.isdigit():
                findings.add(Finding("HUC12_INVALID", "/site/spatial_support/huc12"))

    thresholds = candidate["thresholds"]
    expected_thresholds = {
        "recency_limit_hours", "persistence_count", "persistence_window_hours"
    }
    if not isinstance(thresholds, dict) or set(thresholds) != expected_thresholds:
        findings.add(Finding("THRESHOLDS_INVALID", "/thresholds"))
    else:
        for field in ("recency_limit_hours", "persistence_window_hours"):
            if not _number(thresholds[field], minimum=0.000001):
                findings.add(Finding("THRESHOLD_INVALID", f"/thresholds/{field}"))
        count = thresholds["persistence_count"]
        if not isinstance(count, int) or isinstance(count, bool) or count < 1:
            findings.add(Finding("THRESHOLD_INVALID", "/thresholds/persistence_count"))

    baseline = candidate["baseline"]
    if baseline is not None:
        fields = {"status", "day_of_year", "p05_cfs", "p95_cfs", "evidence_ref"}
        if not isinstance(baseline, dict) or set(baseline) != fields:
            findings.add(Finding("BASELINE_INVALID", "/baseline"))
        else:
            if baseline["status"] not in {"approved_fixture", "unapproved_fixture"}:
                findings.add(Finding("BASELINE_STATUS_INVALID", "/baseline/status"))
            day = baseline["day_of_year"]
            if not isinstance(day, int) or isinstance(day, bool) or not 1 <= day <= 366:
                findings.add(Finding("DAY_OF_YEAR_INVALID", "/baseline/day_of_year"))
            if not _number(baseline["p05_cfs"]) or not _number(baseline["p95_cfs"]):
                findings.add(Finding("PERCENTILE_INVALID", "/baseline"))
            elif float(baseline["p05_cfs"]) >= float(baseline["p95_cfs"]):
                findings.add(Finding("PERCENTILE_ORDER_INVALID", "/baseline"))
            if not isinstance(baseline["evidence_ref"], str) or not baseline["evidence_ref"].strip():
                findings.add(Finding("BASELINE_EVIDENCE_REF_MISSING", "/baseline/evidence_ref"))

    readings = candidate["readings"]
    if not isinstance(readings, list) or not readings:
        findings.add(Finding("READINGS_INVALID", "/readings"))
    elif evaluated_at is not None:
        times: list[datetime] = []
        for index, reading in enumerate(readings):
            base = f"/readings/{index}"
            if not isinstance(reading, dict) or set(reading) != {
                "observed_at", "discharge_cfs", "qualifiers"
            }:
                findings.add(Finding("READING_INVALID", base))
                continue
            observed = _utc(reading["observed_at"])
            if observed is None or observed > evaluated_at:
                findings.add(Finding("READING_TIME_INVALID", f"{base}/observed_at"))
            else:
                times.append(observed)
            if not _number(reading["discharge_cfs"]):
                findings.add(Finding("DISCHARGE_INVALID", f"{base}/discharge_cfs"))
            if not _strings(reading["qualifiers"]):
                findings.add(Finding("QUALIFIERS_INVALID", f"{base}/qualifiers"))
        if len(times) == len(readings) and times != sorted(times):
            findings.add(Finding("READINGS_NOT_CHRONOLOGICAL", "/readings"))

    if candidate["rights"] != {"rights_state": "fixture_only"}:
        findings.add(Finding("RIGHTS_STATE_INVALID", "/rights"))
    if candidate["governance"] != {
        "promotion_eligible": False,
        "public_use_allowed": False,
        "release_state": "not_released",
        "review_state": "fixture_only",
        "operational_alert_authority": False,
    }:
        findings.add(Finding("GOVERNANCE_STATE_INVALID", "/governance"))
    return tuple(sorted(findings))


def _assessment(
    candidate: dict[str, Any], outcome: str, reason: str, latest: float,
    age_hours: float, p05: float | None, p95: float | None,
    state: str, consecutive: int,
) -> dict[str, Any]:
    return {
        "object_type": "StreamflowTailEventAssessment",
        "schema_version": "1.0.0",
        "assessment_id": candidate["assessment_id"],
        "evaluated_at": candidate["evaluated_at"],
        "site": copy.deepcopy(candidate["site"]),
        "source_descriptor_ref": candidate["source_descriptor_ref"],
        "run_receipt_ref": candidate["run_receipt_ref"],
        "evidence_refs": copy.deepcopy(candidate["evidence_refs"]),
        "thresholds": copy.deepcopy(candidate["thresholds"]),
        "summary": {
            "latest_discharge_cfs": latest,
            "latest_age_hours": round(age_hours, 6),
            "p05_cfs": p05,
            "p95_cfs": p95,
            "candidate_state": state,
            "consecutive_tail_readings": consecutive,
        },
        "decision": {"outcome": outcome, "reason_code": reason},
        "rights": copy.deepcopy(candidate["rights"]),
        "governance": copy.deepcopy(candidate["governance"]),
    }


def _tail(value: float, p05: float, p95: float) -> str:
    if value < p05:
        return "LOW_FLOW"
    if value > p95:
        return "HIGH_FLOW"
    return "NONE"


def _consecutive(candidate: dict[str, Any], state: str, p05: float, p95: float) -> int:
    evaluated = _utc(candidate["evaluated_at"])
    assert evaluated is not None
    window = float(candidate["thresholds"]["persistence_window_hours"])
    count = 0
    for reading in reversed(candidate["readings"]):
        observed = _utc(reading["observed_at"])
        assert observed is not None
        if (evaluated - observed).total_seconds() / 3600.0 > window:
            break
        if _tail(float(reading["discharge_cfs"]), p05, p95) != state:
            break
        count += 1
    return count


def evaluate_fixture(candidate: object) -> EvaluationResult:
    """Evaluate one synthetic batch and return a finite non-release result."""

    if not isinstance(candidate, dict):
        return _fail(
            "ERROR", "STREAMFLOW_TAIL_INPUT_ERROR",
            Finding("CANDIDATE_NOT_OBJECT", "/"),
        )
    findings = _validate_candidate(candidate)
    if findings:
        denied = any(
            finding.code in {
                "PRECISE_LOCATION_FIELD_FORBIDDEN", "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
                "RIGHTS_STATE_INVALID", "GOVERNANCE_STATE_INVALID",
            }
            for finding in findings
        )
        return EvaluationResult(
            "DENY" if denied else "ERROR",
            "STREAMFLOW_TAIL_INPUT_DENIED" if denied else "STREAMFLOW_TAIL_INPUT_ERROR",
            None,
            findings,
        )

    evaluated = _utc(candidate["evaluated_at"])
    latest_time = _utc(candidate["readings"][-1]["observed_at"])
    assert evaluated is not None and latest_time is not None
    latest = float(candidate["readings"][-1]["discharge_cfs"])
    age = max(0.0, (evaluated - latest_time).total_seconds() / 3600.0)
    baseline = candidate["baseline"]

    if baseline is None:
        assessment = _assessment(candidate, "ABSTAIN", "PERCENTILES_MISSING", latest, age, None, None, "UNKNOWN", 0)
        return EvaluationResult("ABSTAIN", "PERCENTILES_MISSING", assessment)

    p05 = float(baseline["p05_cfs"])
    p95 = float(baseline["p95_cfs"])
    if baseline["status"] != "approved_fixture":
        assessment = _assessment(candidate, "DENY", "PERCENTILES_NOT_APPROVED", latest, age, p05, p95, "UNKNOWN", 0)
        return EvaluationResult("DENY", "PERCENTILES_NOT_APPROVED", assessment)
    if age > float(candidate["thresholds"]["recency_limit_hours"]):
        assessment = _assessment(candidate, "ABSTAIN", "DATA_STALE", latest, age, p05, p95, "UNKNOWN", 0)
        return EvaluationResult("ABSTAIN", "DATA_STALE", assessment)
    if set(candidate["readings"][-1]["qualifiers"]) & BLOCKING_QUALIFIERS:
        assessment = _assessment(candidate, "ABSTAIN", "SENSOR_QUALIFIER_PRESENT", latest, age, p05, p95, "UNKNOWN", 0)
        return EvaluationResult("ABSTAIN", "SENSOR_QUALIFIER_PRESENT", assessment)
    if candidate["site"]["regulation_context"] == "regulated_context_limited":
        assessment = _assessment(candidate, "ABSTAIN", "REGULATED_CONTEXT_LIMITED", latest, age, p05, p95, "UNKNOWN", 0)
        return EvaluationResult("ABSTAIN", "REGULATED_CONTEXT_LIMITED", assessment)

    state = _tail(latest, p05, p95)
    if state == "NONE":
        assessment = _assessment(candidate, "NO_EVENT", "WITHIN_SEASONAL_RANGE", latest, age, p05, p95, state, 0)
        return EvaluationResult("NO_EVENT", "WITHIN_SEASONAL_RANGE", assessment)

    consecutive = _consecutive(candidate, state, p05, p95)
    required = int(candidate["thresholds"]["persistence_count"])
    if consecutive < required:
        assessment = _assessment(candidate, "HOLD", "PERSISTENCE_NOT_MET", latest, age, p05, p95, state, consecutive)
        return EvaluationResult("HOLD", "PERSISTENCE_NOT_MET", assessment)

    reason = "PERSISTENT_LOW_FLOW" if state == "LOW_FLOW" else "PERSISTENT_HIGH_FLOW"
    assessment = _assessment(candidate, "ANSWER_CANDIDATE", reason, latest, age, p05, p95, state, consecutive)
    return EvaluationResult("ANSWER_CANDIDATE", reason, assessment)
