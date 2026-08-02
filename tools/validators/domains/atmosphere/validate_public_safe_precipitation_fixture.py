#!/usr/bin/env python3
"""Validate the frozen synthetic Atmosphere precipitation fixture profile."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
    MAX_DOCUMENT_DEPTH,
    MAX_DOCUMENT_NODES,
    MAX_FIXTURE_BYTES,
    MAX_JSON_INTEGER_DIGITS,
    Finding,
    add_finding,
    find_undeclared_fields,
    is_finite_number,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "record_id",
        "object_family",
        "knowledge_character",
        "source_descriptor_ref",
        "evidence_refs",
        "spatial_support",
        "temporal_scope",
        "measurement",
        "governance",
        "limitations",
    }
)
ALLOWED_SPATIAL_FIELDS = frozenset({"kind", "county_fips"})
ALLOWED_TEMPORAL_FIELDS = frozenset({"observed_at", "retrieved_at"})
ALLOWED_MEASUREMENT_FIELDS = frozenset(
    {"parameter", "value", "unit", "accumulation_minutes", "method"}
)
ALLOWED_GOVERNANCE_FIELDS = frozenset(
    {
        "rights_state",
        "sensitivity_state",
        "review_state",
        "release_state",
        "promotion_eligible",
        "rollback_state",
    }
)
FORBIDDEN_LOCATION_ALIASES = frozenset(
    {
        "lat",
        "latitude",
        "lon",
        "lng",
        "longitude",
        "x",
        "y",
        "bbox",
        "centroid",
        "easting",
        "northing",
    }
)
EXPECTED_GOVERNANCE = {
    "rights_state": "fixture_only",
    "sensitivity_state": "public_safe_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "rollback_state": "fixture_only",
}
REQUIRED_LIMITATIONS = frozenset(
    {"not_an_alert", "not_life_safety_guidance", "synthetic_fixture_only"}
)


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None else None


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one synthetic precipitation candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    if not is_nonempty_string(candidate.get("record_id")):
        add_finding(findings, "RECORD_ID_MISSING", "$.record_id")
    if candidate.get("object_family") != "PrecipitationObservation":
        add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
    if candidate.get("knowledge_character") != "OBSERVED_SENSOR":
        add_finding(findings, "KNOWLEDGE_CHARACTER_INVALID", "$.knowledge_character")
    if not is_nonempty_string(candidate.get("source_descriptor_ref")):
        add_finding(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")

    evidence_refs = candidate.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or any(not is_nonempty_string(value) for value in evidence_refs)
    ):
        add_finding(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")

    spatial = candidate.get("spatial_support")
    if not isinstance(spatial, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
    else:
        find_undeclared_fields(
            findings,
            spatial,
            ALLOWED_SPATIAL_FIELDS,
            "UNDECLARED_SPATIAL_SUPPORT_FIELD",
            "$.spatial_support",
        )
        for key in spatial:
            if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
                add_finding(
                    findings,
                    "PRECISE_LOCATION_FIELD_FORBIDDEN",
                    f"$.spatial_support.{key}",
                )
        if spatial.get("kind") != "generalized_county":
            add_finding(
                findings,
                "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
                "$.spatial_support.kind",
            )
        county_fips = spatial.get("county_fips")
        if (
            not isinstance(county_fips, str)
            or len(county_fips) != 5
            or not county_fips.isascii()
            or not county_fips.isdigit()
        ):
            add_finding(findings, "COUNTY_FIPS_INVALID", "$.spatial_support.county_fips")

    temporal = candidate.get("temporal_scope")
    if not isinstance(temporal, dict):
        add_finding(findings, "TEMPORAL_SCOPE_INVALID", "$.temporal_scope")
    else:
        find_undeclared_fields(
            findings,
            temporal,
            ALLOWED_TEMPORAL_FIELDS,
            "UNDECLARED_TEMPORAL_FIELD",
            "$.temporal_scope",
        )
        observed = _parse_utc(temporal.get("observed_at"))
        retrieved = _parse_utc(temporal.get("retrieved_at"))
        if observed is None:
            add_finding(findings, "OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at")
        if retrieved is None:
            add_finding(findings, "RETRIEVAL_TIME_INVALID", "$.temporal_scope.retrieved_at")
        if observed is not None and retrieved is not None and retrieved < observed:
            add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.temporal_scope")

    measurement = candidate.get("measurement")
    if not isinstance(measurement, dict):
        add_finding(findings, "MEASUREMENT_INVALID", "$.measurement")
    else:
        find_undeclared_fields(
            findings,
            measurement,
            ALLOWED_MEASUREMENT_FIELDS,
            "UNDECLARED_MEASUREMENT_FIELD",
            "$.measurement",
        )
        if measurement.get("parameter") != "precipitation_amount":
            add_finding(findings, "MEASUREMENT_PARAMETER_INVALID", "$.measurement.parameter")
        value = measurement.get("value")
        if not is_finite_number(value) or not 0 <= value <= 1_000:
            add_finding(findings, "MEASUREMENT_VALUE_OUT_OF_RANGE", "$.measurement.value")
        if measurement.get("unit") != "mm":
            add_finding(findings, "MEASUREMENT_UNIT_INVALID", "$.measurement.unit")
        accumulation = measurement.get("accumulation_minutes")
        if (
            not isinstance(accumulation, int)
            or isinstance(accumulation, bool)
            or not 1 <= accumulation <= 10_080
        ):
            add_finding(
                findings,
                "ACCUMULATION_PERIOD_INVALID",
                "$.measurement.accumulation_minutes",
            )
        if measurement.get("method") != "synthetic_gauge":
            add_finding(findings, "MEASUREMENT_METHOD_INVALID", "$.measurement.method")

    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_INVALID", "$.governance")
    else:
        find_undeclared_fields(
            findings,
            governance,
            ALLOWED_GOVERNANCE_FIELDS,
            "UNDECLARED_GOVERNANCE_FIELD",
            "$.governance",
        )
        for key, expected in EXPECTED_GOVERNANCE.items():
            actual = governance.get(key)
            matches = actual is False if expected is False else actual == expected
            if not matches:
                add_finding(findings, "GOVERNANCE_STATE_INVALID", f"$.governance.{key}")

    limitations = candidate.get("limitations")
    if (
        not isinstance(limitations, list)
        or any(not is_nonempty_string(value) for value in limitations)
        or set(limitations) != REQUIRED_LIMITATIONS
        or len(limitations) != len(REQUIRED_LIMITATIONS)
    ):
        add_finding(findings, "LIMITATIONS_INVALID", "$.limitations")

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate frozen synthetic Atmosphere precipitation fixtures.",
        scope="atmosphere-public-safe-precipitation-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
