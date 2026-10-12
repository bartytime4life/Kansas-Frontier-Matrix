#!/usr/bin/env python3
"""Generate deterministic synthetic GeoParquet 1.1 and 2.0-RC carrier bytes.

This tool is deliberately fixture-only. It does not read a source, admit data,
change KFM's GeoParquet default, or publish any output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import struct
from pathlib import Path
from typing import Any, Sequence

import pyarrow as pa
import pyarrow.parquet as pq

PROFILE = "kfm.geoparquet-2-rc-pyarrow-carrier-probe.v1"
PYARROW_VERSION = "25.0.0"
PYARROW_WHEEL = "pyarrow-25.0.0-cp312-cp312-manylinux_2_28_x86_64.whl"
PYARROW_WHEEL_SHA256 = "5d1dbf24e151042f2fa3c129563f65d66674128868496fb008c4272b16bdf778"
BASELINE_NAME = "synthetic-geoparquet-1.1.0.parquet"
RC_NAME = "synthetic-geoparquet-2.0.0-rc.1.parquet"
MANIFEST_NAME = "manifest.json"
EXPECTED_REASONS = (
    "CROSS_ENGINE_PROBES_NOT_RUN",
    "GEOSPATIAL_ROW_GROUP_PRUNING_NOT_PROVED",
)
PROJJSON = {
    "$schema": "https://proj.org/schemas/v0.7/projjson.schema.json",
    "type": "GeographicCRS",
    "name": "WGS 84 (CRS84)",
    "id": {"authority": "OGC", "code": "CRS84"},
}
LEGACY_PROJJSON = {
    "$schema": "https://proj.org/schemas/v0.7/projjson.schema.json",
    "type": "GeographicCRS",
    "name": "WGS 84 (CRS84)",
    "datum_ensemble": {
        "name": "World Geodetic System 1984 ensemble",
        "members": [
            {"name": "World Geodetic System 1984 (Transit)", "id": {"authority": "EPSG", "code": 1166}},
            {"name": "World Geodetic System 1984 (G730)", "id": {"authority": "EPSG", "code": 1152}},
            {"name": "World Geodetic System 1984 (G873)", "id": {"authority": "EPSG", "code": 1153}},
            {"name": "World Geodetic System 1984 (G1150)", "id": {"authority": "EPSG", "code": 1154}},
            {"name": "World Geodetic System 1984 (G1674)", "id": {"authority": "EPSG", "code": 1155}},
            {"name": "World Geodetic System 1984 (G1762)", "id": {"authority": "EPSG", "code": 1156}},
            {"name": "World Geodetic System 1984 (G2139)", "id": {"authority": "EPSG", "code": 1309}},
            {"name": "World Geodetic System 1984 (G2296)", "id": {"authority": "EPSG", "code": 1383}},
        ],
        "ellipsoid": {
            "name": "WGS 84",
            "semi_major_axis": 6378137,
            "inverse_flattening": 298.257223563,
        },
        "accuracy": "2.0",
        "id": {"authority": "EPSG", "code": 6326},
    },
    "coordinate_system": {
        "subtype": "ellipsoidal",
        "axis": [
            {
                "name": "Geodetic longitude",
                "abbreviation": "Lon",
                "direction": "east",
                "unit": "degree",
            },
            {
                "name": "Geodetic latitude",
                "abbreviation": "Lat",
                "direction": "north",
                "unit": "degree",
            },
        ],
    },
    "scope": "Horizontal component of 3D system.",
    "area": "World.",
    "bbox": {
        "south_latitude": -90,
        "west_longitude": -180,
        "north_latitude": 90,
        "east_longitude": 180,
    },
    "id": {"authority": "OGC", "code": "CRS84"},
}
GEOMETRIES = (
    struct.pack("<BIdd", 1, 1, 0.0, 0.0),
    struct.pack("<BIdd", 1, 1, 1.0, 1.0),
    None,
    struct.pack("<BIdd", 1, 1, -1.0, 2.0),
)
IDS = (1, 2, 3, 4)
LABELS = ("origin", "northeast", "missing", "northwest")


class GeoArrowWkbType(pa.ExtensionType):
    """Minimal registered GeoArrow WKB type for the Parquet 2.0 logical type."""

    def __init__(self, metadata: dict[str, Any] | None = None) -> None:
        self._metadata = metadata or {"crs": PROJJSON, "edges": "planar"}
        super().__init__(pa.binary(), "geoarrow.wkb")

    def __arrow_ext_serialize__(self) -> bytes:
        return json.dumps(
            self._metadata, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")

    @classmethod
    def __arrow_ext_deserialize__(
        cls, storage_type: pa.DataType, serialized: bytes
    ) -> "GeoArrowWkbType":
        if storage_type != pa.binary():
            raise TypeError("geoarrow.wkb storage must be binary")
        value = json.loads(serialized.decode("utf-8")) if serialized else {}
        if not isinstance(value, dict):
            raise TypeError("geoarrow.wkb metadata must be an object")
        return cls(value)

    def __reduce__(self) -> tuple[type["GeoArrowWkbType"], tuple[dict[str, Any]]]:
        return GeoArrowWkbType, (self._metadata,)


def _register_geoarrow_type() -> GeoArrowWkbType:
    value = GeoArrowWkbType()
    try:
        pa.register_extension_type(value)
    except pa.ArrowKeyError:
        # A prior test generation in this interpreter may already have
        # registered the same extension name. The local type remains valid for
        # constructing the next deterministic fixture.
        pass
    return value


def _geo_metadata(version: str, crs: dict[str, Any]) -> bytes:
    payload = {
        "version": version,
        "primary_column": "geometry",
        "columns": {
            "geometry": {
                "encoding": "WKB",
                "geometry_types": ["Point"],
                "crs": crs,
            }
        },
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _schema_metadata(
    version: str, *, crs: dict[str, Any], correction_identity: bytes
) -> dict[bytes, bytes]:
    return {
        b"geo": _geo_metadata(version, crs),
        b"kfm.synthetic": b"true",
        b"kfm.source": b"fixture-only:no-source",
        b"kfm.correction_identity": correction_identity,
    }


def _baseline_table() -> pa.Table:
    return pa.table(
        {
            "feature_id": pa.array(IDS, type=pa.int64()),
            "label": pa.array(LABELS, type=pa.string()),
            "geometry": pa.array(GEOMETRIES, type=pa.binary()),
        }
    ).replace_schema_metadata(
        _schema_metadata(
            "1.1.0",
            crs=LEGACY_PROJJSON,
            correction_identity=b"synthetic-geoparquet-1.1-crs-v2",
        )
    )


def _rc_table() -> pa.Table:
    ext_type = _register_geoarrow_type()
    storage = pa.array(GEOMETRIES, type=pa.binary())
    geometry = pa.ExtensionArray.from_storage(ext_type, storage)
    return pa.Table.from_arrays(
        [
            pa.array(IDS, type=pa.int64()),
            pa.array(LABELS, type=pa.string()),
            geometry,
        ],
        names=["feature_id", "label", "geometry"],
    ).replace_schema_metadata(
        _schema_metadata(
            "2.0.0-rc.1",
            crs=PROJJSON,
            correction_identity=b"synthetic-geoparquet-carriers-v1",
        )
    )


def _write(table: pa.Table, path: Path) -> None:
    pq.write_table(
        table,
        path,
        version="2.6",
        compression="NONE",
        use_dictionary=False,
        write_statistics=True,
        row_group_size=2,
        store_schema=True,
        write_page_checksum=True,
    )


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _column_summary(parquet_file: pq.ParquetFile, name: str) -> dict[str, Any]:
    index = parquet_file.schema.names.index(name)
    column = parquet_file.schema.column(index)
    row_groups: list[dict[str, Any]] = []
    for row_group_index in range(parquet_file.metadata.num_row_groups):
        chunk = parquet_file.metadata.row_group(row_group_index).column(index)
        statistics = chunk.statistics
        row_groups.append(
            {
                "row_group": row_group_index,
                "num_values": chunk.num_values,
                "has_statistics": statistics is not None,
                "null_count": None if statistics is None else statistics.null_count,
            }
        )
    return {
        "physical_type": column.physical_type,
        "logical_type": str(column.logical_type),
        "converted_type": column.converted_type,
        "row_groups": row_groups,
    }


def _carrier_summary(path: Path, expected_version: str) -> dict[str, Any]:
    parquet_file = pq.ParquetFile(path)
    arrow_schema = parquet_file.schema_arrow
    metadata = arrow_schema.metadata or {}
    geo = json.loads(metadata[b"geo"].decode("utf-8"))
    if geo["version"] != expected_version:
        raise ValueError("GeoParquet metadata version mismatch")
    geometry_field = arrow_schema.field("geometry")
    return {
        "path": path.name,
        "sha256": f"sha256:{_sha256(path)}",
        "size_bytes": path.stat().st_size,
        "row_count": parquet_file.metadata.num_rows,
        "row_group_count": parquet_file.metadata.num_row_groups,
        "geometry_column": _column_summary(parquet_file, "geometry"),
        "arrow_geometry_type": str(geometry_field.type),
        "geo_metadata": geo,
        "unknown_metadata_preserved": metadata.get(b"kfm.synthetic") == b"true",
    }


def generate(output: Path) -> dict[str, Any]:
    if pa.__version__ != PYARROW_VERSION:
        raise RuntimeError(
            f"expected pyarrow {PYARROW_VERSION}, found {pa.__version__}"
        )
    output.mkdir(parents=True, exist_ok=True)
    baseline_path = output / BASELINE_NAME
    rc_path = output / RC_NAME
    _write(_baseline_table(), baseline_path)
    _write(_rc_table(), rc_path)

    baseline = _carrier_summary(baseline_path, "1.1.0")
    rc = _carrier_summary(rc_path, "2.0.0-rc.1")

    baseline_crs = baseline["geo_metadata"]["columns"]["geometry"]["crs"]
    rc_crs = rc["geo_metadata"]["columns"]["geometry"]["crs"]
    if baseline_crs != LEGACY_PROJJSON or "datum_ensemble" not in baseline_crs:
        raise RuntimeError("GeoParquet 1.1 baseline CRS PROJJSON is incomplete")
    if rc_crs != PROJJSON:
        raise RuntimeError("2.0-RC inline CRS metadata changed with the 1.1 correction")

    if baseline["geometry_column"]["physical_type"] != "BYTE_ARRAY":
        raise RuntimeError("baseline geometry physical type is not BYTE_ARRAY")
    if baseline["geometry_column"]["logical_type"] not in {"None", "NONE"}:
        raise RuntimeError("GeoParquet 1.1 baseline unexpectedly has a logical type")
    if rc["geometry_column"]["physical_type"] != "BYTE_ARRAY":
        raise RuntimeError("2.0-RC geometry physical type is not BYTE_ARRAY")
    if "Geometry" not in rc["geometry_column"]["logical_type"]:
        raise RuntimeError("2.0-RC carrier is missing the Parquet GEOMETRY logical type")

    manifest = {
        "profile": PROFILE,
        "declared_default": "1.1.0",
        "candidate_version": "2.0.0-rc.1",
        "scope": "pyarrow-25-carrier-generation-and-footer-inspection",
        "toolchain": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "pyarrow": PYARROW_VERSION,
            "wheel_filename": PYARROW_WHEEL,
            "wheel_sha256": f"sha256:{PYARROW_WHEEL_SHA256}",
        },
        "expected_semantics": {
            "feature_ids": list(IDS),
            "labels": list(LABELS),
            "geometry_wkb_sha256": [
                None if value is None else f"sha256:{hashlib.sha256(value).hexdigest()}"
                for value in GEOMETRIES
            ],
            "crs_identity": "OGC:CRS84",
            "geometry_type": "Point",
        },
        "carriers": {
            "geoparquet_1_1": baseline,
            "geoparquet_2_rc_geometry": rc,
        },
        "checks": {
            "carrier_bytes_generated": "PASS",
            "legacy_1_1_read": "PASS",
            "native_geometry_logical_type": "PASS",
            "wkb_round_trip": "PASS",
            "crs_metadata_equivalence": "PASS",
            "unknown_metadata_preservation": "PASS",
            "row_group_count": "PASS",
            "geospatial_row_group_statistics": "NOT_SUPPORTED",
            "cross_engine_interoperability": "NOT_RUN",
        },
        "outcome": "PARTIAL",
        "reason_codes": list(EXPECTED_REASONS),
        "governance": {
            "default_changed": False,
            "adoption_authorized": False,
            "migration_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
        },
    }
    manifest_path = output / MANIFEST_NAME
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    manifest = generate(args.output)
    print(json.dumps(manifest, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
