#!/usr/bin/env python3
"""Validate the frozen synthetic station soil-moisture fixture profile.

This validator is deliberately narrower than the proposed
SoilMoistureObservation contract. It performs no source access, normalization,
policy decision, evidence resolution, promotion, or publication. It only checks
the deterministic fixture profile documented beside this module.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_finite_number,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)

MAX_READINGS = 256
SPEC_HASH_RE = re.compile(r"^sha256:[a-f0-9]{64}$")

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "record_id",
        "schema_version",
        "support_type",
        "source_descriptor_ref",
        "source_role",
        "evidence_refs",
        "spec_hash",
        "run_receipt_ref",
        "readings",
        "governance",
    }
)
ALLOWED_READING_FIELDS = frozenset(
    {
        "station_id",
        "spatial_support",
        "depth_cm",
        "measure",
        "value",
        "unit",
        "timestamp_iso",
        "source_timezone",
        "qc_flags",
    }
)
ALLOWED_SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "county_fips"})
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
EXPECTED_GOVERNANCE = {
    "rights_state": "fixture_only",
    "sensitivity_state": "public_safe_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "rollback_state": "fixture_only",
}


def _is_utc_timestamp(value: object) -> bool:
    """Return true only for a parseable ISO-8601 timestamp ending in ``Z``."""

    if not isinstance(value, str) or "T" not in value or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() == timedelta(0)


def _string_list_is_valid(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(is_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def reading_dedupe_key(reading: object) -> tuple[str, str, float | int, str] | None:
    """Return the frozen identity tuple when every key component is valid."""

    if not isinstance(reading, dict):
        return None
    station_id = reading.get("station_id")
    measure = reading.get("measure")
    depth_cm = reading.get("depth_cm")
    timestamp_iso = reading.get("timestamp_iso")
    if not (
        is_nonempty_string(station_id)
        and is_nonempty_string(measure)
        and is_finite_number(depth_cm)
        and _is_utc_timestamp(timestamp_iso)
    ):
        return None
    return station_id.strip(), measure.strip(), depth_cm, timestamp_iso


def _validate_spatial_support(
    findings: set[Finding], spatial_support: object, path: str
) -> None:
    if not isinstance(spatial_support, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", path)
        return

    find_undeclared_fields(
        findings,
        spatial_support,
        ALLOWED_SPATIAL_SUPPORT_FIELDS,
        "UNDECLARED_SPATIAL_SUPPORT_FIELD",
        path,
    )
    for key in spatial_support:
        if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
            add_finding(
                findings,
                "PRECISE_LOCATION_FIELD_FORBIDDEN",
                f"{path}.{key}",
            )
    if spatial_support.get("kind") != "generalized_county":
        add_finding(findings, "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", f"{path}.kind")
    county_fips = spatial_support.get("county_fips")
    if (
        not isinstance(county_fips, str)
        or len(county_fips) != 5
        or not county_fips.isdigit()
    ):
        add_finding(findings, "COUNTY_FIPS_INVALID", f"{path}.county_fips")


def _validate_reading(findings: set[Finding], reading: object, index: int) -> None:
    path = f"$.readings[{index}]"
    if not isinstance(reading, dict):
        add_finding(findings, "READING_NOT_OBJECT", path)
        return

    find_undeclared_fields(
        findings,
        reading,
        ALLOWED_READING_FIELDS,
        "UNDECLARED_READING_FIELD",
        path,
    )

    if not is_nonempty_string(reading.get("station_id")):
        add_finding(findings, "STATION_ID_MISSING", f"{path}.station_id")

    _validate_spatial_support(
        findings,
        reading.get("spatial_support"),
        f"{path}.spatial_support",
    )

    depth_cm = reading.get("depth_cm")
    if not is_finite_number(depth_cm) or depth_cm < 0:
        add_finding(findings, "DEPTH_CM_INVALID", f"{path}.depth_cm")

    if reading.get("measure") != "volumetric_water_content":
        add_finding(findings, "MEASURE_INVALID", f"{path}.measure")

    value = reading.get("value")
    if not is_finite_number(value) or not 0 <= value <= 1:
        add_finding(findings, "VALUE_OUT_OF_RANGE", f"{path}.value")

    if reading.get("unit") != "m3/m3":
        add_finding(findings, "UNIT_INVALID", f"{path}.unit")

    if not _is_utc_timestamp(reading.get("timestamp_iso")):
        add_finding(findings, "TIMESTAMP_NOT_CANONICAL_UTC", f"{path}.timestamp_iso")

    if not is_nonempty_string(reading.get("source_timezone")):
        add_finding(findings, "SOURCE_TIMEZONE_MISSING", f"{path}.source_timezone")

    if not _string_list_is_valid(reading.get("qc_flags")):
        add_finding(findings, "QC_FLAGS_INVALID", f"{path}.qc_flags")


def _validate_governance(findings: set[Finding], governance: object) -> None:
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_INVALID", "$.governance")
        return

    find_undeclared_fields(
        findings,
        governance,
        ALLOWED_GOVERNANCE_FIELDS,
        "UNDECLARED_GOVERNANCE_FIELD",
        "$.governance",
    )
    for field, expected in EXPECTED_GOVERNANCE.items():
        actual = governance.get(field)
        matches = actual is False if expected is False else actual == expected
        if not matches:
            add_finding(findings, "GOVERNANCE_STATE_INVALID", f"$.governance.{field}")


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one decoded synthetic fixture candidate."""

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
    if candidate.get("schema_version") != "v1":
        add_finding(findings, "SCHEMA_VERSION_INVALID", "$.schema_version")
    if candidate.get("support_type") != "station_observation":
        add_finding(findings, "SUPPORT_TYPE_INVALID", "$.support_type")
    if not is_nonempty_string(candidate.get("source_descriptor_ref")):
        add_finding(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")
    if candidate.get("source_role") != "fixture_only":
        add_finding(findings, "SOURCE_ROLE_INVALID", "$.source_role")
    if not _string_list_is_valid(candidate.get("evidence_refs")):
        add_finding(findings, "EVIDENCE_REFS_INVALID", "$.evidence_refs")

    spec_hash = candidate.get("spec_hash")
    if not isinstance(spec_hash, str) or not SPEC_HASH_RE.fullmatch(spec_hash):
        add_finding(findings, "SPEC_HASH_INVALID", "$.spec_hash")
    elif spec_hash == "sha256:" + ("0" * 64):
        add_finding(findings, "SPEC_HASH_PLACEHOLDER", "$.spec_hash")
    if not is_nonempty_string(candidate.get("run_receipt_ref")):
        add_finding(findings, "RUN_RECEIPT_REF_MISSING", "$.run_receipt_ref")

    readings = candidate.get("readings")
    if not isinstance(readings, list) or not readings:
        add_finding(findings, "READINGS_INVALID", "$.readings")
    elif len(readings) > MAX_READINGS:
        add_finding(findings, "READING_COUNT_EXCEEDED", "$.readings")
    else:
        seen: dict[tuple[str, str, float | int, str], int] = {}
        for index, reading in enumerate(readings):
            _validate_reading(findings, reading, index)
            dedupe_key = reading_dedupe_key(reading)
            if dedupe_key is None:
                continue
            prior_index = seen.get(dedupe_key)
            if prior_index is not None:
                add_finding(findings, "DUPLICATE_READING", f"$.readings[{index}]")
            else:
                seen[dedupe_key] = index

    _validate_governance(findings, candidate.get("governance"))
    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    """Decode bounded, duplicate-free UTF-8 JSON and apply the fixture profile."""

    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate frozen synthetic station soil-moisture fixtures.",
        scope="soil-moisture-station-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
