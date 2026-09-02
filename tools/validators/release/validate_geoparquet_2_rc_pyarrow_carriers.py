#!/usr/bin/env python3
"""Validate actual synthetic GeoParquet 1.1 and 2.0-RC carrier bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq
from jsonschema import Draft202012Validator

from tools.experiments.geoparquet.generate_pyarrow_25_carriers import GeoArrowWkbType

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/release/geoparquet_2_rc_pyarrow_carrier_probe.schema.json"
PROFILE = "kfm.geoparquet-2-rc-pyarrow-carrier-probe.v1"
WHEEL = "sha256:5d1dbf24e151042f2fa3c129563f65d66674128868496fb008c4272b16bdf778"
EXPECTED_REASONS = (
    "CROSS_ENGINE_PROBES_NOT_RUN",
    "GEOSPATIAL_ROW_GROUP_PRUNING_NOT_PROVED",
)
IDS = [1, 2, 3, 4]
WKB = [
    struct.pack("<BIdd", 1, 1, 0.0, 0.0),
    struct.pack("<BIdd", 1, 1, 1.0, 1.0),
    None,
    struct.pack("<BIdd", 1, 1, -1.0, 2.0),
]


@dataclass(frozen=True)
class Result:
    outcome: str
    reason_codes: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {"outcome": self.outcome, "reason_codes": list(self.reason_codes)}


def _register() -> None:
    try:
        pa.register_extension_type(GeoArrowWkbType())
    except pa.ArrowKeyError:
        pass


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _digest(path: Path) -> str:
    return f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def _crs(value: Any) -> str | None:
    if value == "OGC:CRS84":
        return value
    if isinstance(value, Mapping):
        ident = value.get("id")
        if isinstance(ident, Mapping) and ident.get("authority") == "OGC" and ident.get("code") == "CRS84":
            return "OGC:CRS84"
    return None


def _storage(table: pa.Table) -> list[bytes | None]:
    array = table.column("geometry").combine_chunks()
    return (array.storage if isinstance(array, pa.ExtensionArray) else array).to_pylist()


def _column(file: pq.ParquetFile) -> dict[str, Any]:
    index = file.schema.names.index("geometry")
    column = file.schema.column(index)
    groups = []
    for number in range(file.metadata.num_row_groups):
        chunk = file.metadata.row_group(number).column(index)
        stats = chunk.statistics
        groups.append({
            "row_group": number,
            "num_values": chunk.num_values,
            "has_statistics": stats is not None,
            "null_count": None if stats is None else stats.null_count,
        })
    return {
        "physical_type": column.physical_type,
        "logical_type": str(column.logical_type),
        "converted_type": column.converted_type,
        "row_groups": groups,
    }


def _metadata(file: pq.ParquetFile) -> tuple[dict[str, Any], Mapping[bytes, bytes]]:
    metadata = file.schema_arrow.metadata or {}
    geo = json.loads(metadata[b"geo"].decode("utf-8"))
    if not isinstance(geo, dict):
        raise TypeError("geo metadata must be an object")
    return geo, metadata


def _declared(entry: Mapping[str, Any], path: Path, file: pq.ParquetFile) -> bool:
    geo, metadata = _metadata(file)
    return (
        entry["sha256"] == _digest(path)
        and entry["size_bytes"] == path.stat().st_size
        and entry["geometry_column"] == _column(file)
        and entry["arrow_geometry_type"] == str(file.schema_arrow.field("geometry").type)
        and entry["geo_metadata"] == geo
        and entry["unknown_metadata_preserved"] == (metadata.get(b"kfm.synthetic") == b"true")
    )


def validate(root: Path, manifest_path: Path) -> Result:
    reasons: list[str] = []
    _register()
    try:
        schema = _json(SCHEMA)
        Draft202012Validator.check_schema(schema)
        manifest = _json(manifest_path)
        schema_errors = list(Draft202012Validator(schema).iter_errors(manifest))
        if schema_errors:
            schema_reasons = {"SCHEMA_INVALID"}
            for error in schema_errors:
                error_path = list(error.absolute_path)
                if error_path and error_path[0] == "governance":
                    schema_reasons.add("GOVERNANCE_BOUNDARY_VIOLATION")
                if error_path == ["outcome"]:
                    schema_reasons.add("DECLARED_OUTCOME_MISMATCH")
            return Result("ERROR", tuple(sorted(schema_reasons)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return Result("ERROR", ("INPUT_UNAVAILABLE",))

    if manifest["profile"] != PROFILE:
        reasons.append("PROFILE_INVALID")
    if pa.__version__ != "25.0.0" or manifest["toolchain"]["pyarrow"] != "25.0.0":
        reasons.append("PYARROW_VERSION_MISMATCH")
    if manifest["toolchain"]["wheel_sha256"] != WHEEL:
        reasons.append("PYARROW_WHEEL_DIGEST_MISMATCH")
    if manifest["declared_default"] != "1.1.0":
        reasons.append("DECLARED_DEFAULT_CHANGED")
    if manifest["candidate_version"] != "2.0.0-rc.1":
        reasons.append("CANDIDATE_VERSION_MISMATCH")
    if any(value is not False for value in manifest["governance"].values()):
        reasons.append("GOVERNANCE_BOUNDARY_VIOLATION")

    carriers = manifest["carriers"]
    entries = (carriers["geoparquet_1_1"], carriers["geoparquet_2_rc_geometry"])
    paths = tuple(root / entry["path"] for entry in entries)
    if not all(path.is_file() for path in paths):
        return Result("ERROR", tuple(sorted(set([*reasons, "CARRIER_MISSING"]))))

    try:
        if any(entry["sha256"] != _digest(path) for entry, path in zip(entries, paths)):
            reasons.append("CARRIER_DIGEST_MISMATCH")
        files = tuple(pq.ParquetFile(path) for path in paths)
        tables = tuple(pq.read_table(path) for path in paths)
    except Exception:
        return Result("ERROR", tuple(sorted(set([*reasons, "CARRIER_UNREADABLE"]))))

    baseline, rc = files
    baseline_col = baseline.schema.column(baseline.schema.names.index("geometry"))
    rc_col = rc.schema.column(rc.schema.names.index("geometry"))
    if baseline_col.physical_type != "BYTE_ARRAY" or str(baseline_col.logical_type) not in {"None", "NONE"}:
        reasons.append("BASELINE_TYPE_MISMATCH")
    if rc_col.physical_type != "BYTE_ARRAY" or "Geometry" not in str(rc_col.logical_type):
        reasons.append("RC_GEOMETRY_LOGICAL_TYPE_MISSING")
    if not all(_declared(entry, path, file) for entry, path, file in zip(entries, paths, files)):
        reasons.append("CARRIER_DECLARATION_MISMATCH")
    if any(
        entry["geo_metadata"] != _metadata(file)[0]
        for entry, file in zip(entries, files)
    ):
        reasons.append("CARRIER_METADATA_DECLARATION_MISMATCH")
    if any(file.metadata.num_row_groups != 2 for file in files):
        reasons.append("ROW_GROUP_LAYOUT_MISMATCH")
    if any(table.column("feature_id").to_pylist() != IDS for table in tables):
        reasons.append("IDENTITY_MISMATCH")
    if any(_storage(table) != WKB for table in tables):
        reasons.append("WKB_MISMATCH")

    baseline_geo, _ = _metadata(baseline)
    rc_geo, _ = _metadata(rc)
    if baseline_geo.get("version") != "1.1.0" or rc_geo.get("version") != "2.0.0-rc.1":
        reasons.append("GEOPARQUET_VERSION_METADATA_MISMATCH")
    crs_values = [geo["columns"]["geometry"].get("crs") for geo in (baseline_geo, rc_geo)]
    if [_crs(value) for value in crs_values] != ["OGC:CRS84", "OGC:CRS84"]:
        reasons.append("CRS_SEMANTIC_CONFLICT")

    checks = manifest["checks"]
    if checks["geospatial_row_group_statistics"] != "NOT_SUPPORTED":
        reasons.append("GEOSPATIAL_STATISTICS_STATUS_MISMATCH")
    if checks["cross_engine_interoperability"] != "NOT_RUN":
        reasons.append("CROSS_ENGINE_STATUS_MISMATCH")
    if manifest["outcome"] != "PARTIAL":
        reasons.append("DECLARED_OUTCOME_MISMATCH")
    if tuple(manifest["reason_codes"]) != EXPECTED_REASONS:
        reasons.append("DECLARED_REASON_CODES_MISMATCH")

    return Result("ERROR", tuple(sorted(set(reasons)))) if reasons else Result("PARTIAL", EXPECTED_REASONS)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv)
    result = validate(args.root, args.manifest)
    print(json.dumps(result.as_dict(), sort_keys=True, separators=(",", ":")))
    return 0 if result.outcome == "PARTIAL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
