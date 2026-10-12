#!/usr/bin/env python3
"""Validate Soil public-safe smoke fixtures without external dependencies.

The validator intentionally implements only the frozen Soil smoke profile.  It
does not resolve references, contact services, or inspect data outside the
candidate file.
"""

from __future__ import annotations

import sys
from pathlib import Path
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
        "support_type",
        "source_descriptor_ref",
        "evidence_refs",
        "spatial_support",
        "depth_interval_cm",
        "measurement",
        "governance",
    }
)
ALLOWED_SUPPORT_TYPES = frozenset(
    {
        "static_survey",
        "station_observation",
        "satellite_grid",
        "modeled_derivative",
    }
)
ALLOWED_SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "county_fips"})
ALLOWED_DEPTH_INTERVAL_FIELDS = frozenset({"top", "bottom"})
ALLOWED_MEASUREMENT_FIELDS = frozenset({"property", "value", "unit"})
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


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one already-decoded Soil candidate."""

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

    support_type = candidate.get("support_type")
    if not isinstance(support_type, str) or support_type not in ALLOWED_SUPPORT_TYPES:
        add_finding(findings, "SUPPORT_TYPE_INVALID", "$.support_type")

    if not is_nonempty_string(candidate.get("source_descriptor_ref")):
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_MISSING",
            "$.source_descriptor_ref",
        )

    evidence_refs = candidate.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or any(not is_nonempty_string(value) for value in evidence_refs)
    ):
        add_finding(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
    else:
        find_undeclared_fields(
            findings,
            spatial_support,
            ALLOWED_SPATIAL_SUPPORT_FIELDS,
            "UNDECLARED_SPATIAL_SUPPORT_FIELD",
            "$.spatial_support",
        )
        for key in spatial_support:
            if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
                add_finding(
                    findings,
                    "PRECISE_LOCATION_FIELD_FORBIDDEN",
                    f"$.spatial_support.{key}",
                )

        if spatial_support.get("kind") != "generalized_county":
            add_finding(
                findings,
                "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
                "$.spatial_support.kind",
            )
        county_fips = spatial_support.get("county_fips")
        if (
            not isinstance(county_fips, str)
            or len(county_fips) != 5
            or not county_fips.isdigit()
        ):
            add_finding(
                findings,
                "COUNTY_FIPS_INVALID",
                "$.spatial_support.county_fips",
            )

    depth_interval = candidate.get("depth_interval_cm")
    if not isinstance(depth_interval, dict):
        add_finding(findings, "DEPTH_INTERVAL_INVALID", "$.depth_interval_cm")
    else:
        find_undeclared_fields(
            findings,
            depth_interval,
            ALLOWED_DEPTH_INTERVAL_FIELDS,
            "UNDECLARED_DEPTH_INTERVAL_FIELD",
            "$.depth_interval_cm",
        )
        top = depth_interval.get("top")
        bottom = depth_interval.get("bottom")
        if not is_finite_number(top) or not is_finite_number(bottom):
            add_finding(
                findings,
                "DEPTH_INTERVAL_NON_NUMERIC",
                "$.depth_interval_cm",
            )
        elif top < 0 or bottom <= top:
            add_finding(findings, "DEPTH_INTERVAL_INVALID", "$.depth_interval_cm")

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
        if measurement.get("property") != "volumetric_water_content":
            add_finding(
                findings,
                "MEASUREMENT_PROPERTY_INVALID",
                "$.measurement.property",
            )
        value = measurement.get("value")
        if not is_finite_number(value) or not 0 <= value <= 1:
            add_finding(
                findings,
                "MEASUREMENT_VALUE_OUT_OF_RANGE",
                "$.measurement.value",
            )
        if measurement.get("unit") != "m3/m3":
            add_finding(findings, "MEASUREMENT_UNIT_INVALID", "$.measurement.unit")

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
                add_finding(
                    findings,
                    "GOVERNANCE_STATE_INVALID",
                    f"$.governance.{key}",
                )

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    """Decode and validate a bounded UTF-8 JSON fixture."""

    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate one or more frozen Soil public-safe JSON fixtures.",
        scope="soil-public-safe-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
