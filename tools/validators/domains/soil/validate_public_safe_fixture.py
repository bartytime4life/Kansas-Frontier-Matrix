#!/usr/bin/env python3
"""Validate Soil public-safe smoke fixtures without external dependencies.

The validator intentionally implements only the frozen Soil smoke profile.  It
does not resolve references, contact services, or inspect data outside the
candidate file.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


MAX_FIXTURE_BYTES = 1_000_000
MAX_JSON_INTEGER_DIGITS = 512
MAX_DOCUMENT_DEPTH = 64
MAX_DOCUMENT_NODES = 4_096

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


@dataclass(frozen=True, order=True)
class Finding:
    """A stable machine-readable finding."""

    code: str
    path: str


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_finite_number(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def _key_sort_value(value: object) -> tuple[str, str]:
    return (type(value).__name__, repr(value))


def _find_undeclared_fields(
    findings: set[Finding],
    candidate: dict[Any, Any],
    allowed_fields: frozenset[str],
    code: str,
    parent_path: str,
) -> None:
    for key in sorted(candidate.keys(), key=_key_sort_value):
        if key not in allowed_fields:
            _add(findings, code, f"{parent_path}.{key}")


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted findings for one already-decoded Soil candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    _find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )

    support_type = candidate.get("support_type")
    if not isinstance(support_type, str) or support_type not in ALLOWED_SUPPORT_TYPES:
        _add(findings, "SUPPORT_TYPE_INVALID", "$.support_type")

    if not _is_nonempty_string(candidate.get("source_descriptor_ref")):
        _add(
            findings,
            "SOURCE_DESCRIPTOR_REF_MISSING",
            "$.source_descriptor_ref",
        )

    evidence_refs = candidate.get("evidence_refs")
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or any(not _is_nonempty_string(value) for value in evidence_refs)
    ):
        _add(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, dict):
        _add(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
    else:
        _find_undeclared_fields(
            findings,
            spatial_support,
            ALLOWED_SPATIAL_SUPPORT_FIELDS,
            "UNDECLARED_SPATIAL_SUPPORT_FIELD",
            "$.spatial_support",
        )
        for key in sorted(spatial_support.keys(), key=_key_sort_value):
            if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
                _add(
                    findings,
                    "PRECISE_LOCATION_FIELD_FORBIDDEN",
                    f"$.spatial_support.{key}",
                )

        if spatial_support.get("kind") != "generalized_county":
            _add(
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
            _add(findings, "COUNTY_FIPS_INVALID", "$.spatial_support.county_fips")

    depth_interval = candidate.get("depth_interval_cm")
    if not isinstance(depth_interval, dict):
        _add(findings, "DEPTH_INTERVAL_INVALID", "$.depth_interval_cm")
    else:
        _find_undeclared_fields(
            findings,
            depth_interval,
            ALLOWED_DEPTH_INTERVAL_FIELDS,
            "UNDECLARED_DEPTH_INTERVAL_FIELD",
            "$.depth_interval_cm",
        )
        top = depth_interval.get("top")
        bottom = depth_interval.get("bottom")
        if not _is_finite_number(top) or not _is_finite_number(bottom):
            _add(
                findings,
                "DEPTH_INTERVAL_NON_NUMERIC",
                "$.depth_interval_cm",
            )
        elif top < 0 or bottom <= top:
            _add(findings, "DEPTH_INTERVAL_INVALID", "$.depth_interval_cm")

    measurement = candidate.get("measurement")
    if not isinstance(measurement, dict):
        _add(findings, "MEASUREMENT_INVALID", "$.measurement")
    else:
        _find_undeclared_fields(
            findings,
            measurement,
            ALLOWED_MEASUREMENT_FIELDS,
            "UNDECLARED_MEASUREMENT_FIELD",
            "$.measurement",
        )
        if measurement.get("property") != "volumetric_water_content":
            _add(
                findings,
                "MEASUREMENT_PROPERTY_INVALID",
                "$.measurement.property",
            )
        value = measurement.get("value")
        if not _is_finite_number(value) or not 0 <= value <= 1:
            _add(
                findings,
                "MEASUREMENT_VALUE_OUT_OF_RANGE",
                "$.measurement.value",
            )
        if measurement.get("unit") != "m3/m3":
            _add(findings, "MEASUREMENT_UNIT_INVALID", "$.measurement.unit")

    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        _add(findings, "GOVERNANCE_INVALID", "$.governance")
    else:
        _find_undeclared_fields(
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
                _add(
                    findings,
                    "GOVERNANCE_STATE_INVALID",
                    f"$.governance.{key}",
                )

    return sorted(findings)


def _parse_bounded_int(raw_value: str) -> int:
    digits = raw_value.lstrip("-")
    if len(digits) > MAX_JSON_INTEGER_DIGITS:
        raise ValueError("JSON integer exceeds the configured digit limit")
    return int(raw_value)


def _parse_finite_float(raw_value: str) -> float:
    value = float(raw_value)
    if not math.isfinite(value):
        raise ValueError("JSON number is not finite")
    return value


def _reject_json_constant(_raw_value: str) -> None:
    raise ValueError("non-standard JSON numeric constant")


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    candidate: dict[str, object] = {}
    for key, value in pairs:
        if key in candidate:
            raise ValueError("duplicate JSON object key")
        candidate[key] = value
    return candidate


def _json_structure_is_bounded(candidate: object) -> bool:
    pending = [(candidate, 0)]
    visited = 0
    while pending:
        value, depth = pending.pop()
        visited += 1
        if visited > MAX_DOCUMENT_NODES or depth > MAX_DOCUMENT_DEPTH:
            return False
        if isinstance(value, dict):
            if len(value) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((child, depth + 1) for child in value.values())
        elif isinstance(value, list):
            if len(value) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((child, depth + 1) for child in value)
    return True


def _read_bounded_regular_file(path: Path) -> bytes:
    flags = os.O_RDONLY
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NONBLOCK", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)

    descriptor = os.open(path, flags)
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise OSError("fixture input must be a regular file")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            return stream.read(MAX_FIXTURE_BYTES + 1)
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def validate_file(path: Path | str) -> list[Finding]:
    """Decode and validate a bounded UTF-8 JSON fixture."""

    fixture_path = Path(path)
    try:
        raw_bytes = _read_bounded_regular_file(fixture_path)
        if len(raw_bytes) > MAX_FIXTURE_BYTES:
            return [Finding("FIXTURE_TOO_LARGE", "$")]
        raw_candidate = raw_bytes.decode("utf-8")
        candidate = json.loads(
            raw_candidate,
            parse_int=_parse_bounded_int,
            parse_float=_parse_finite_float,
            parse_constant=_reject_json_constant,
            object_pairs_hook=_reject_duplicate_keys,
        )
        if not _json_structure_is_bounded(candidate):
            return [Finding("FIXTURE_JSON_INVALID", "$")]
    except (OSError, UnicodeError, ValueError, RecursionError):
        return [Finding("FIXTURE_JSON_INVALID", "$")]
    return validate_candidate(candidate)


def _serialize(path: Path, findings: list[Finding]) -> str:
    payload = {
        "file": str(path),
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in sorted(findings)
        ],
        "scope": "soil-public-safe-fixture",
        "status": "FAIL" if findings else "PASS",
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one or more frozen Soil public-safe JSON fixtures."
    )
    parser.add_argument("files", nargs="*", type=Path, help="fixture JSON file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if not args.files:
        print("at least one fixture file is required", file=sys.stderr)
        return 2

    any_findings = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = validate_file(path)
        any_findings = any_findings or bool(findings)
        print(_serialize(path, findings))
    return 1 if any_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
