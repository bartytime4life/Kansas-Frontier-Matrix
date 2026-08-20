#!/usr/bin/env python3
"""Validate the bounded PyArrow-to-GDAL GeoParquet consumer result packet."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

from tools.experiments.geoparquet.run_gdal_3_13_2_consumer_probe import (
    COORDINATES,
    GDAL_VERSION,
    GEOMETRY_TYPES,
    IDS,
    IMAGE_REFERENCE,
    LABELS,
    PARTIAL_REASONS,
    PROFILE,
    PYARROW_WHEEL_SHA256,
    SOURCE_PROFILE,
)

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/release/geoparquet_2_rc_gdal_consumer_probe.schema.json"
ALLOWED_ERROR_REASONS = {
    "GDAL_IMAGE_UNAVAILABLE",
    "GDAL_IMAGE_IDENTITY_MISMATCH",
    "GDAL_VERSION_UNAVAILABLE",
    "GDAL_VERSION_MISMATCH",
}


@dataclass(frozen=True)
class Result:
    outcome: str
    reason_codes: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {"outcome": self.outcome, "reason_codes": list(self.reason_codes)}


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _digest(path: Path) -> str:
    return f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def _crs84(value: Any) -> bool:
    if value == "OGC:CRS84":
        return True
    if not isinstance(value, Mapping):
        return False
    identifier = value.get("id")
    return (
        isinstance(identifier, Mapping)
        and identifier.get("authority") == "OGC"
        and identifier.get("code") == "CRS84"
    )


def _expected_reason_codes(packet: Mapping[str, Any]) -> tuple[str, ...] | None:
    outcome = packet["outcome"]
    carriers = packet["carriers"]
    baseline = carriers["geoparquet_1_1"]["read_status"]
    candidate = carriers["geoparquet_2_rc_geometry"]["read_status"]
    driver = packet["checks"]["parquet_driver"]

    if outcome == "ERROR":
        reasons = tuple(packet["reason_codes"])
        return reasons if len(reasons) == 1 and reasons[0] in ALLOWED_ERROR_REASONS else None
    if "FAIL" in {baseline, candidate}:
        reasons = []
        if baseline == "FAIL":
            reasons.append("GDAL_1_1_SEMANTIC_MISMATCH")
        if candidate == "FAIL":
            reasons.append("GDAL_2_RC_GEOMETRY_SEMANTIC_MISMATCH")
        return tuple(reasons) if outcome == "FAIL" else None
    if driver == "NOT_SUPPORTED":
        return (
            *PARTIAL_REASONS,
            "GDAL_PARQUET_DRIVER_UNAVAILABLE",
        ) if outcome == "HOLD" else None
    if "NOT_SUPPORTED" in {baseline, candidate}:
        reasons = list(PARTIAL_REASONS)
        if baseline == "NOT_SUPPORTED":
            reasons.append("GDAL_1_1_READ_NOT_SUPPORTED")
        if candidate == "NOT_SUPPORTED":
            reasons.append("GDAL_2_RC_GEOMETRY_READ_NOT_SUPPORTED")
        return tuple(reasons) if outcome == "HOLD" else None
    return PARTIAL_REASONS if outcome == "PARTIAL" and {baseline, candidate} == {"PASS"} else None


def _command_is_bounded(command: Sequence[str], path: str) -> bool:
    required = {
        "docker",
        "run",
        "--network",
        "none",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        IMAGE_REFERENCE,
        "ogr2ogr",
        "-t_srs",
        "OGC:CRS84",
        f"/probe/{path}",
    }
    return required.issubset(command)


def validate(root: Path, packet_path: Path) -> Result:
    reasons: list[str] = []
    try:
        schema = _json(SCHEMA)
        Draft202012Validator.check_schema(schema)
        packet = _json(packet_path)
        schema_errors = list(Draft202012Validator(schema).iter_errors(packet))
        if schema_errors:
            schema_reasons = {"SCHEMA_INVALID"}
            for error in schema_errors:
                path = list(error.absolute_path)
                if path and path[0] == "governance":
                    schema_reasons.add("GOVERNANCE_BOUNDARY_VIOLATION")
                if path == ["outcome"]:
                    schema_reasons.add("DECLARED_OUTCOME_MISMATCH")
                if path[:2] == ["toolchain", "image_reference"]:
                    schema_reasons.add("GDAL_IMAGE_IDENTITY_MISMATCH")
            return Result("ERROR", tuple(sorted(schema_reasons)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return Result("ERROR", ("INPUT_UNAVAILABLE",))

    if packet["profile"] != PROFILE:
        reasons.append("PROFILE_INVALID")
    if any(value is not False for value in packet["governance"].values()):
        reasons.append("GOVERNANCE_BOUNDARY_VIOLATION")

    source_ref = packet["source_carrier_manifest"]
    source_path = root / source_ref["path"]
    try:
        if source_ref["sha256"] != _digest(source_path):
            reasons.append("SOURCE_MANIFEST_DIGEST_MISMATCH")
        source = _json(source_path)
    except (OSError, UnicodeError, json.JSONDecodeError):
        return Result("ERROR", tuple(sorted(set([*reasons, "SOURCE_MANIFEST_UNAVAILABLE"]))))

    if (
        source.get("profile") != SOURCE_PROFILE
        or source.get("outcome") != "PARTIAL"
        or source.get("declared_default") != "1.1.0"
        or source.get("candidate_version") != "2.0.0-rc.1"
        or source.get("toolchain", {}).get("pyarrow") != "25.0.0"
        or source.get("toolchain", {}).get("wheel_sha256") != PYARROW_WHEEL_SHA256
    ):
        reasons.append("SOURCE_CARRIER_PROFILE_MISMATCH")

    source_carriers = source.get("carriers", {})
    for key in ("geoparquet_1_1", "geoparquet_2_rc_geometry"):
        source_entry = source_carriers.get(key)
        packet_entry = packet["carriers"][key]
        if not isinstance(source_entry, Mapping):
            reasons.append("SOURCE_CARRIER_MISSING")
            continue
        name = source_entry.get("path")
        if not isinstance(name, str) or Path(name).name != name:
            reasons.append("SOURCE_CARRIER_PATH_INVALID")
            continue
        path = root / name
        try:
            actual_digest = _digest(path)
        except OSError:
            reasons.append("SOURCE_CARRIER_MISSING")
            continue
        if (
            source_entry.get("sha256") != actual_digest
            or packet_entry["sha256"] != actual_digest
            or packet_entry["path"] != name
        ):
            reasons.append("CARRIER_DIGEST_MISMATCH")
        if not _command_is_bounded(packet_entry["command"], name):
            reasons.append("GDAL_COMMAND_BOUNDARY_MISMATCH")
        if packet_entry["read_status"] == "PASS" and (
            packet_entry["row_count"] != 4
            or packet_entry["feature_ids"] != IDS
            or packet_entry["labels"] != LABELS
            or packet_entry["geometry_types"] != GEOMETRY_TYPES
            or packet_entry["coordinates"] != COORDINATES
        ):
            reasons.append("GDAL_CONSUMER_SEMANTIC_MISMATCH")

    try:
        baseline = source_carriers["geoparquet_1_1"]
        candidate = source_carriers["geoparquet_2_rc_geometry"]
        if (
            baseline["geometry_column"]["physical_type"] != "BYTE_ARRAY"
            or baseline["geometry_column"]["logical_type"] != "None"
            or candidate["geometry_column"]["physical_type"] != "BYTE_ARRAY"
            or candidate["geometry_column"]["logical_type"] != "Geometry(crs=)"
        ):
            reasons.append("SOURCE_LOGICAL_TYPE_MISMATCH")
        for entry in (baseline, candidate):
            crs = entry["geo_metadata"]["columns"]["geometry"].get("crs")
            if not _crs84(crs):
                reasons.append("SOURCE_CRS_MISMATCH")
    except (KeyError, TypeError):
        reasons.append("SOURCE_CARRIER_PROFILE_MISMATCH")

    toolchain = packet["toolchain"]
    if packet["checks"]["gdal_distribution_authenticated"] == "PASS":
        if (
            toolchain["image_id"] is None
            or not toolchain["repo_digests"]
            or toolchain["gdal_version_output"] is None
            or re.match(r"^GDAL 3\.13\.2(?:,|$)", toolchain["gdal_version_output"]) is None
            or toolchain["gdal"] != GDAL_VERSION
        ):
            reasons.append("GDAL_IMAGE_IDENTITY_MISMATCH")

    expected_reasons = _expected_reason_codes(packet)
    if expected_reasons is None:
        reasons.append("DECLARED_OUTCOME_MISMATCH")
    elif tuple(packet["reason_codes"]) != expected_reasons:
        reasons.append("DECLARED_REASON_CODES_MISMATCH")

    checks = packet["checks"]
    if packet["outcome"] == "PARTIAL" and not all(
        checks[key] == "PASS"
        for key in (
            "gdal_distribution_authenticated",
            "parquet_driver",
            "legacy_1_1_consumer_read",
            "rc_geometry_consumer_read",
            "crs84_same_crs_transform",
            "pyarrow_to_gdal_consumer_read",
        )
    ):
        reasons.append("DECLARED_OUTCOME_MISMATCH")

    if reasons:
        return Result("ERROR", tuple(sorted(set(reasons))))
    return Result(packet["outcome"], tuple(packet["reason_codes"]))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args(argv)
    result = validate(args.root, args.packet)
    print(json.dumps(result.as_dict(), sort_keys=True, separators=(",", ":")))
    return 0 if result.outcome in {"PARTIAL", "HOLD"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
