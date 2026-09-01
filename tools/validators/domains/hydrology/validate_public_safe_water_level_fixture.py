#!/usr/bin/env python3
"""Validate the frozen synthetic Hydrology water-level fixture profile."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
import sys
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
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
        "source_role",
        "source_descriptor_ref",
        "evidence_refs",
        "gauge_site_ref",
        "spatial_support",
        "temporal_scope",
        "measurement",
        "governance",
        "limitations",
    }
)
ALLOWED_SPATIAL_FIELDS = frozenset({"kind", "county_fips"})
ALLOWED_TEMPORAL_FIELDS = frozenset(
    {"aggregation_window", "observed_at", "source_time", "retrieved_at"}
)
ALLOWED_MEASUREMENT_FIELDS = frozenset(
    {
        "parameter_code",
        "value",
        "unit",
        "datum_ref",
        "qualifier",
        "provisional_status",
        "no_data",
    }
)
ALLOWED_PROVISIONAL_STATUSES = frozenset(
    {"provisional", "final", "corrected", "estimated", "ice_affected"}
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
FIXTURE_SOURCE_PREFIX = "fixture://sources/hydrology/"
FIXTURE_EVIDENCE_PREFIX = "fixture://evidence/hydrology/"
FIXTURE_GAUGE_PREFIX = "fixture://hydrology/gauge/generalized/"
FIXTURE_DATUM_PREFIX = "fixture://hydrology/datum/"
EXPECTED_GOVERNANCE = {
    "rights_state": "fixture_only",
    "sensitivity_state": "public_safe_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "rollback_state": "fixture_only",
}
REQUIRED_LIMITATIONS = frozenset(
    {
        "datum_specific",
        "not_a_flood_warning",
        "not_life_safety_guidance",
        "not_regulatory_context",
        "synthetic_fixture_only",
    }
)
_CANONICAL_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_CANONICAL_RESOURCE_IDENTIFIER = re.compile(
    r"\A(?=.{1,128}\Z)[a-z0-9]+(?:[._-][a-z0-9]+)*\Z"
)
_CANONICAL_EVIDENCE_SEGMENT = re.compile(
    r"\A(?=.{1,128}\Z)[A-Za-z0-9]+(?:[._:-][A-Za-z0-9]+)*\Z"
)


def _has_canonical_evidence_path(value: str) -> bool:
    suffix = value[len(FIXTURE_EVIDENCE_PREFIX) :]
    return (
        1 <= len(suffix) <= 256
        and all(
            _CANONICAL_EVIDENCE_SEGMENT.fullmatch(segment) is not None
            for segment in suffix.split("/")
        )
    )


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or _CANONICAL_UTC.fullmatch(value) is None:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one synthetic water-level candidate."""

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
    if candidate.get("object_family") != "WaterLevelObservation":
        add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
    if candidate.get("source_role") != "observed":
        add_finding(findings, "SOURCE_ROLE_INVALID", "$.source_role")

    source_descriptor_ref = candidate.get("source_descriptor_ref")
    if not is_nonempty_string(source_descriptor_ref):
        add_finding(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")
    elif not source_descriptor_ref.startswith(FIXTURE_SOURCE_PREFIX):
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_NOT_FIXTURE",
            "$.source_descriptor_ref",
        )
    elif _CANONICAL_RESOURCE_IDENTIFIER.fullmatch(
        source_descriptor_ref[len(FIXTURE_SOURCE_PREFIX) :]
    ) is None:
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_IDENTIFIER_INVALID",
            "$.source_descriptor_ref",
        )

    gauge_site_ref = candidate.get("gauge_site_ref")
    if not is_nonempty_string(gauge_site_ref):
        add_finding(findings, "GAUGE_SITE_REF_MISSING", "$.gauge_site_ref")
    elif not gauge_site_ref.startswith(FIXTURE_GAUGE_PREFIX):
        add_finding(
            findings,
            "GAUGE_SITE_REF_NOT_GENERALIZED_FIXTURE",
            "$.gauge_site_ref",
        )
    elif _CANONICAL_RESOURCE_IDENTIFIER.fullmatch(
        gauge_site_ref[len(FIXTURE_GAUGE_PREFIX) :]
    ) is None:
        add_finding(
            findings,
            "GAUGE_SITE_REF_IDENTIFIER_INVALID",
            "$.gauge_site_ref",
        )

    evidence_refs = candidate.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or any(not is_nonempty_string(value) for value in evidence_refs)
    ):
        add_finding(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")
    else:
        if any(not value.startswith(FIXTURE_EVIDENCE_PREFIX) for value in evidence_refs):
            add_finding(findings, "EVIDENCE_REF_NOT_FIXTURE", "$.evidence_refs")
        elif any(not _has_canonical_evidence_path(value) for value in evidence_refs):
            add_finding(findings, "EVIDENCE_REF_IDENTIFIER_INVALID", "$.evidence_refs")
        if len(evidence_refs) != len(set(evidence_refs)):
            add_finding(findings, "EVIDENCE_REFS_DUPLICATE", "$.evidence_refs")
        if evidence_refs != sorted(evidence_refs):
            add_finding(
                findings,
                "EVIDENCE_REFS_NOT_CANONICAL_ORDER",
                "$.evidence_refs",
            )

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
        if temporal.get("aggregation_window") != "instant":
            add_finding(
                findings,
                "AGGREGATION_WINDOW_INVALID",
                "$.temporal_scope.aggregation_window",
            )
        observed = _parse_utc(temporal.get("observed_at"))
        source_time = _parse_utc(temporal.get("source_time"))
        retrieved = _parse_utc(temporal.get("retrieved_at"))
        if observed is None:
            add_finding(findings, "OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at")
        if source_time is None:
            add_finding(findings, "SOURCE_TIME_INVALID", "$.temporal_scope.source_time")
        if retrieved is None:
            add_finding(findings, "RETRIEVAL_TIME_INVALID", "$.temporal_scope.retrieved_at")
        if observed is not None and source_time is not None and source_time < observed:
            add_finding(findings, "SOURCE_TIME_BEFORE_OBSERVED", "$.temporal_scope")
        if source_time is not None and retrieved is not None and retrieved < source_time:
            add_finding(findings, "RETRIEVAL_TIME_BEFORE_SOURCE", "$.temporal_scope")
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
        if measurement.get("parameter_code") != "00065":
            add_finding(findings, "PARAMETER_CODE_INVALID", "$.measurement.parameter_code")
        value = measurement.get("value")
        if not is_finite_number(value) or not -10_000 <= value <= 10_000:
            add_finding(findings, "MEASUREMENT_VALUE_OUT_OF_RANGE", "$.measurement.value")
        if measurement.get("unit") != "ft":
            add_finding(findings, "MEASUREMENT_UNIT_INVALID", "$.measurement.unit")
        datum_ref = measurement.get("datum_ref")
        if not is_nonempty_string(datum_ref):
            add_finding(findings, "DATUM_REF_MISSING", "$.measurement.datum_ref")
        elif not datum_ref.startswith(FIXTURE_DATUM_PREFIX):
            add_finding(findings, "DATUM_REF_NOT_FIXTURE", "$.measurement.datum_ref")
        elif _CANONICAL_RESOURCE_IDENTIFIER.fullmatch(
            datum_ref[len(FIXTURE_DATUM_PREFIX) :]
        ) is None:
            add_finding(
                findings,
                "DATUM_REF_IDENTIFIER_INVALID",
                "$.measurement.datum_ref",
            )
        if measurement.get("qualifier") != "synthetic":
            add_finding(findings, "QUALIFIER_INVALID", "$.measurement.qualifier")
        provisional_status = measurement.get("provisional_status")
        if not is_nonempty_string(provisional_status):
            add_finding(
                findings,
                "PROVISIONAL_STATUS_MISSING",
                "$.measurement.provisional_status",
            )
        elif provisional_status not in ALLOWED_PROVISIONAL_STATUSES:
            add_finding(
                findings,
                "PROVISIONAL_STATUS_INVALID",
                "$.measurement.provisional_status",
            )
        if measurement.get("no_data") is not False:
            add_finding(findings, "NO_DATA_STATE_INVALID", "$.measurement.no_data")

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
        description="Validate frozen synthetic Hydrology water-level fixtures.",
        scope="hydrology-public-safe-water-level-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
