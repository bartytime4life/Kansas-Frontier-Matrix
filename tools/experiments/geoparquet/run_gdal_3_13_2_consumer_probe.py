#!/usr/bin/env python3
"""Run one pinned GDAL consumer-read probe over the PyArrow carrier pair."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

PROFILE = "kfm.geoparquet-2-rc-gdal-consumer-probe.v1"
SOURCE_PROFILE = "kfm.geoparquet-2-rc-pyarrow-carrier-probe.v1"
SCOPE = "pyarrow-25-producer-to-gdal-3.13.2-consumer-read"
GDAL_VERSION = "3.13.2"
GDAL_SOURCE_TAG_COMMIT = "b40672525acf3f5c4f29d8541aa7dcff1e18eb92"
IMAGE_INDEX_SHA256 = (
    "sha256:6960891693c3463b8e2b498a915c7c9b10eeb93f155d5be14c2e3ffbede9fbb1"
)
IMAGE_PLATFORM_MANIFEST_SHA256 = (
    "sha256:6611b649465826c623869861447be58cd75962da2312d8ab656a1f4e32acf98d"
)
IMAGE_REFERENCE = (
    "ghcr.io/osgeo/gdal:alpine-normal-3.13.2@" + IMAGE_INDEX_SHA256
)
IMAGE_PLATFORM = "linux/amd64"
PYARROW_WHEEL_SHA256 = (
    "sha256:5d1dbf24e151042f2fa3c129563f65d66674128868496fb008c4272b16bdf778"
)
IDS = [1, 2, 3, 4]
LABELS = ["origin", "northeast", "missing", "northwest"]
GEOMETRY_TYPES = ["Point", "Point", None, "Point"]
COORDINATES = [[0.0, 0.0], [1.0, 1.0], None, [-1.0, 2.0]]
PARTIAL_REASONS = (
    "CROSS_ENGINE_MATRIX_INCOMPLETE",
    "GDAL_PRODUCER_ROUTE_NOT_RUN",
    "GEOSPATIAL_ROW_GROUP_PRUNING_NOT_PROVED",
)


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256_bytes(value: bytes) -> str:
    return f"sha256:{hashlib.sha256(value).hexdigest()}"


def _sha256(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


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


def _source(root: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = _json(manifest_path)
    if not isinstance(manifest, dict):
        raise ValueError("source carrier manifest must be an object")
    if manifest.get("profile") != SOURCE_PROFILE or manifest.get("outcome") != "PARTIAL":
        raise ValueError("source carrier profile or outcome mismatch")
    if manifest.get("declared_default") != "1.1.0":
        raise ValueError("GeoParquet 1.1.0 default was not preserved")
    if manifest.get("candidate_version") != "2.0.0-rc.1":
        raise ValueError("candidate version mismatch")
    toolchain = manifest.get("toolchain", {})
    if (
        toolchain.get("pyarrow") != "25.0.0"
        or toolchain.get("wheel_sha256") != PYARROW_WHEEL_SHA256
    ):
        raise ValueError("PyArrow toolchain mismatch")

    carriers = manifest.get("carriers", {})
    for key in ("geoparquet_1_1", "geoparquet_2_rc_geometry"):
        entry = carriers.get(key)
        if not isinstance(entry, dict):
            raise ValueError(f"missing source carrier: {key}")
        name = entry.get("path")
        if not isinstance(name, str) or Path(name).name != name:
            raise ValueError(f"unsafe source carrier path: {key}")
        path = root / name
        if not path.is_file() or entry.get("sha256") != _sha256(path):
            raise ValueError(f"source carrier digest mismatch: {key}")

    baseline = carriers["geoparquet_1_1"]
    candidate = carriers["geoparquet_2_rc_geometry"]
    if (
        baseline["geometry_column"].get("physical_type") != "BYTE_ARRAY"
        or baseline["geometry_column"].get("logical_type") != "None"
    ):
        raise ValueError("GeoParquet 1.1 physical/logical type mismatch")
    if (
        candidate["geometry_column"].get("physical_type") != "BYTE_ARRAY"
        or candidate["geometry_column"].get("logical_type") != "Geometry(crs=)"
    ):
        raise ValueError("GeoParquet 2.0-RC physical/logical type mismatch")
    for entry in (baseline, candidate):
        crs = entry["geo_metadata"]["columns"]["geometry"].get("crs")
        if not _crs84(crs):
            raise ValueError("source carrier CRS metadata is not OGC:CRS84")
    return manifest


def _run(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(command),
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _write_log(output: Path, name: str, value: str) -> None:
    (output / name).write_text(value, encoding="utf-8")


def _docker_run(root: Path) -> list[str]:
    return [
        "docker",
        "run",
        "--rm",
        "--platform",
        IMAGE_PLATFORM,
        "--network",
        "none",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--pids-limit",
        "128",
        "--memory",
        "512m",
        "--cpus",
        "1",
        "--user",
        "65532:65532",
        "--env",
        "HOME=/tmp",
        "--tmpfs",
        "/tmp:rw,noexec,nosuid,size=16m",
        "--volume",
        f"{root.resolve()}:/probe:ro",
        IMAGE_REFERENCE,
    ]


def _empty_carrier(entry: Mapping[str, Any], command: Sequence[str], stderr: str) -> dict[str, Any]:
    return {
        "path": entry["path"],
        "sha256": entry["sha256"],
        "command": list(command),
        "read_status": "NOT_SUPPORTED",
        "row_count": None,
        "feature_ids": [],
        "labels": [],
        "geometry_types": [],
        "coordinates": [],
        "stdout_sha256": _sha256_bytes(b""),
        "stderr_sha256": _sha256_bytes(stderr.encode("utf-8")),
    }


def _summary(
    entry: Mapping[str, Any],
    command: Sequence[str],
    completed: subprocess.CompletedProcess[str],
) -> dict[str, Any]:
    base = {
        "path": entry["path"],
        "sha256": entry["sha256"],
        "command": list(command),
        "read_status": "NOT_SUPPORTED" if completed.returncode else "FAIL",
        "row_count": None,
        "feature_ids": [],
        "labels": [],
        "geometry_types": [],
        "coordinates": [],
        "stdout_sha256": _sha256_bytes(completed.stdout.encode("utf-8")),
        "stderr_sha256": _sha256_bytes(completed.stderr.encode("utf-8")),
    }
    if completed.returncode:
        return base
    try:
        payload = json.loads(completed.stdout)
        features = payload["features"]
        if payload.get("type") != "FeatureCollection" or not isinstance(features, list):
            return base
        properties = [feature["properties"] for feature in features]
        geometries = [feature.get("geometry") for feature in features]
        feature_ids = [item["feature_id"] for item in properties]
        labels = [item["label"] for item in properties]
        geometry_types = [None if item is None else item.get("type") for item in geometries]
        coordinates = [None if item is None else item.get("coordinates") for item in geometries]
        base.update(
            {
                "row_count": len(features),
                "feature_ids": feature_ids,
                "labels": labels,
                "geometry_types": geometry_types,
                "coordinates": coordinates,
            }
        )
        if (
            len(features) == 4
            and feature_ids == IDS
            and labels == LABELS
            and geometry_types == GEOMETRY_TYPES
            and coordinates == COORDINATES
        ):
            base["read_status"] = "PASS"
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        pass
    return base


def _base_result(source: Mapping[str, Any], manifest_path: Path) -> dict[str, Any]:
    return {
        "profile": PROFILE,
        "declared_default": "1.1.0",
        "candidate_version": "2.0.0-rc.1",
        "scope": SCOPE,
        "source_carrier_manifest": {
            "path": "manifest.json",
            "sha256": _sha256(manifest_path),
            "profile": SOURCE_PROFILE,
            "outcome": "PARTIAL",
        },
        "toolchain": {
            "gdal": GDAL_VERSION,
            "gdal_version_output": None,
            "gdal_source_tag_commit": GDAL_SOURCE_TAG_COMMIT,
            "image_reference": IMAGE_REFERENCE,
            "image_index_sha256": IMAGE_INDEX_SHA256,
            "image_platform": IMAGE_PLATFORM,
            "image_platform_manifest_sha256": IMAGE_PLATFORM_MANIFEST_SHA256,
            "image_id": None,
            "repo_digests": [],
        },
        "carriers": {},
        "checks": {
            "gdal_distribution_authenticated": "ERROR",
            "parquet_driver": "ERROR",
            "legacy_1_1_consumer_read": "ERROR",
            "rc_geometry_consumer_read": "ERROR",
            "crs84_same_crs_transform": "ERROR",
            "pyarrow_to_gdal_consumer_read": "ERROR",
            "gdal_producer_route": "NOT_RUN",
            "geospatial_row_group_pruning": "NOT_RUN",
        },
        "outcome": "ERROR",
        "reason_codes": ["GDAL_IMAGE_UNAVAILABLE"],
        "governance": {
            "default_changed": False,
            "adoption_authorized": False,
            "migration_authorized": False,
            "release_authorized": False,
            "deployment_authorized": False,
            "publication_authorized": False,
        },
    }


def run(root: Path, manifest_path: Path, output: Path) -> dict[str, Any]:
    source = _source(root, manifest_path)
    output.mkdir(parents=True, exist_ok=True)
    result = _base_result(source, manifest_path)
    entries = source["carriers"]

    pull_command = ["docker", "pull", "--platform", IMAGE_PLATFORM, IMAGE_REFERENCE]
    pull = _run(pull_command)
    _write_log(output, "gdal-image-pull.stdout.txt", pull.stdout)
    _write_log(output, "gdal-image-pull.stderr.txt", pull.stderr)
    if pull.returncode:
        for key, entry in entries.items():
            result["carriers"][key] = _empty_carrier(entry, pull_command, pull.stderr)
        return result

    inspect_command = ["docker", "image", "inspect", IMAGE_REFERENCE]
    inspect = _run(inspect_command)
    _write_log(output, "gdal-image-inspect.json", inspect.stdout)
    _write_log(output, "gdal-image-inspect.stderr.txt", inspect.stderr)
    try:
        image = json.loads(inspect.stdout)[0]
        repo_digests = sorted(set(image.get("RepoDigests") or []))
        image_id = image["Id"]
        authenticated = (
            inspect.returncode == 0
            and image.get("Os") == "linux"
            and image.get("Architecture") == "amd64"
            and re.fullmatch(r"sha256:[0-9a-f]{64}", image_id) is not None
            and (
                IMAGE_INDEX_SHA256 in pull.stdout
                or IMAGE_INDEX_SHA256 in pull.stderr
                or any(value.endswith("@" + IMAGE_INDEX_SHA256) for value in repo_digests)
            )
        )
    except (IndexError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        authenticated = False
        repo_digests = []
        image_id = None
    result["toolchain"]["repo_digests"] = repo_digests
    result["toolchain"]["image_id"] = image_id
    if not authenticated:
        result["reason_codes"] = ["GDAL_IMAGE_IDENTITY_MISMATCH"]
        for key, entry in entries.items():
            result["carriers"][key] = _empty_carrier(entry, inspect_command, inspect.stderr)
        return result
    result["checks"]["gdal_distribution_authenticated"] = "PASS"

    base = _docker_run(root)
    version_command = [*base, "gdalinfo", "--version"]
    version = _run(version_command)
    _write_log(output, "gdal-version.stdout.txt", version.stdout)
    _write_log(output, "gdal-version.stderr.txt", version.stderr)
    version_output = version.stdout.strip() if version.returncode == 0 else None
    result["toolchain"]["gdal_version_output"] = version_output
    if version.returncode or version_output is None:
        result["reason_codes"] = ["GDAL_VERSION_UNAVAILABLE"]
        for key, entry in entries.items():
            result["carriers"][key] = _empty_carrier(entry, version_command, version.stderr)
        return result
    if re.match(r"^GDAL 3\.13\.2(?:,|$)", version_output) is None:
        result["reason_codes"] = ["GDAL_VERSION_MISMATCH"]
        for key, entry in entries.items():
            result["carriers"][key] = _empty_carrier(entry, version_command, version_output)
        return result

    formats_command = [*base, "ogrinfo", "--formats"]
    formats = _run(formats_command)
    _write_log(output, "gdal-formats.stdout.txt", formats.stdout)
    _write_log(output, "gdal-formats.stderr.txt", formats.stderr)
    if formats.returncode or "Parquet -vector-" not in formats.stdout:
        result["checks"].update(
            {
                "parquet_driver": "NOT_SUPPORTED",
                "legacy_1_1_consumer_read": "NOT_SUPPORTED",
                "rc_geometry_consumer_read": "NOT_SUPPORTED",
                "crs84_same_crs_transform": "NOT_SUPPORTED",
                "pyarrow_to_gdal_consumer_read": "NOT_SUPPORTED",
            }
        )
        result["outcome"] = "HOLD"
        result["reason_codes"] = [
            *PARTIAL_REASONS,
            "GDAL_PARQUET_DRIVER_UNAVAILABLE",
        ]
        for key, entry in entries.items():
            result["carriers"][key] = _empty_carrier(entry, formats_command, formats.stderr)
        return result
    result["checks"]["parquet_driver"] = "PASS"

    for key, entry in entries.items():
        command = [
            *base,
            "ogr2ogr",
            "-q",
            "-f",
            "GeoJSON",
            "-t_srs",
            "OGC:CRS84",
            "-lco",
            "RFC7946=YES",
            "/vsistdout/",
            f"/probe/{entry['path']}",
        ]
        completed = _run(command)
        _write_log(output, f"{key}.stdout.geojson", completed.stdout)
        _write_log(output, f"{key}.stderr.txt", completed.stderr)
        result["carriers"][key] = _summary(entry, command, completed)

    baseline_status = result["carriers"]["geoparquet_1_1"]["read_status"]
    candidate_status = result["carriers"]["geoparquet_2_rc_geometry"]["read_status"]
    result["checks"].update(
        {
            "legacy_1_1_consumer_read": baseline_status,
            "rc_geometry_consumer_read": candidate_status,
        }
    )
    statuses = {baseline_status, candidate_status}
    if statuses == {"PASS"}:
        result["checks"].update(
            {
                "crs84_same_crs_transform": "PASS",
                "pyarrow_to_gdal_consumer_read": "PASS",
            }
        )
        result["outcome"] = "PARTIAL"
        result["reason_codes"] = list(PARTIAL_REASONS)
    elif "FAIL" in statuses:
        result["checks"].update(
            {
                "crs84_same_crs_transform": "FAIL",
                "pyarrow_to_gdal_consumer_read": "FAIL",
            }
        )
        result["outcome"] = "FAIL"
        result["reason_codes"] = [
            code
            for key, code in (
                ("geoparquet_1_1", "GDAL_1_1_SEMANTIC_MISMATCH"),
                ("geoparquet_2_rc_geometry", "GDAL_2_RC_GEOMETRY_SEMANTIC_MISMATCH"),
            )
            if result["carriers"][key]["read_status"] == "FAIL"
        ]
    else:
        result["checks"].update(
            {
                "crs84_same_crs_transform": "NOT_SUPPORTED",
                "pyarrow_to_gdal_consumer_read": "NOT_SUPPORTED",
            }
        )
        result["outcome"] = "HOLD"
        result["reason_codes"] = [
            *PARTIAL_REASONS,
            *(
                ["GDAL_1_1_READ_NOT_SUPPORTED"]
                if baseline_status == "NOT_SUPPORTED"
                else []
            ),
            *(
                ["GDAL_2_RC_GEOMETRY_READ_NOT_SUPPORTED"]
                if candidate_status == "NOT_SUPPORTED"
                else []
            ),
        ]
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = run(args.root, args.manifest, args.output)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        print(f"GDAL consumer probe input error: {error}", file=sys.stderr)
        return 1
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["outcome"] in {"PARTIAL", "HOLD"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
