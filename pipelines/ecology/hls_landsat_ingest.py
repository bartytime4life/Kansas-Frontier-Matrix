#!/usr/bin/env python3
"""
KFM Ecology HLS / Landsat ingest scaffold.

No-network by default.

This script converts a prepared scene manifest into KFM time-slice ingest
artifacts that can be consumed by the existing governed pipeline:

  - ingest_manifest.json
  - qa_summary.json
  - tileset_metadata.json

It does NOT download imagery. It expects a local fixture/source manifest.

Example:
  python connectors/pipelines/ecology/hls_landsat_ingest.py \
    --scene-manifest tests/fixtures/ecology/timeslice/pass/scene_manifest.json \
    --out-dir /tmp/ecology-ingest
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPORTED_SENSORS = {
    "HLS",
    "Landsat-8",
    "Landsat-9",
    "Sentinel-2",
}


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256_json(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def require_fields(payload: dict[str, Any], fields: list[str]) -> None:
    missing = [field for field in fields if field not in payload]
    if missing:
        raise ValueError(f"scene manifest missing required fields: {', '.join(missing)}")


def pct(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        raise ValueError("percentage denominator must be > 0")
    return round((numerator / denominator) * 100.0, 4)


def build_ingest_manifest(scene: dict[str, Any]) -> dict[str, Any]:
    sensor = scene["sensor"]
    if sensor not in SUPPORTED_SENSORS:
        raise ValueError(
            f"unsupported sensor: {sensor}; expected one of {sorted(SUPPORTED_SENSORS)}"
        )

    spec_basis = {
        "source_uris": scene["source_uris"],
        "sensor": sensor,
        "collection_version": scene["collection_version"],
        "bbox": scene["bbox"],
        "time_start": scene["time_start"],
        "time_end": scene["time_end"],
    }

    return {
        **spec_basis,
        "schema_version": "v1",
        "object_type": "EcologyIngestManifest",
        "canonicalization_alg": "JCS@v1",
        "canonical_spec_hash": sha256_json(spec_basis),
        "created_at": utc_now(),
    }


def build_qa_summary(scene: dict[str, Any]) -> dict[str, Any]:
    qa = scene["qa"]

    total_pixels = int(qa["total_pixels"])
    masked_pixels = int(qa["masked_pixels"])
    aerosol_flagged_pixels = int(qa.get("aerosol_flagged_pixels", 0))
    total_30m_pixels = int(qa.get("total_30m_pixels", total_pixels))
    valid_30m_pixels = int(qa.get("valid_30m_pixels", total_30m_pixels - masked_pixels))

    return {
        "schema_version": "v1",
        "object_type": "EcologyQaSummary",
        "total_pixels": total_pixels,
        "masked_pixels": masked_pixels,
        "aerosol_flagged_pixels": aerosol_flagged_pixels,
        "total_30m_pixels": total_30m_pixels,
        "valid_30m_pixels": valid_30m_pixels,
        "masked_pct": pct(masked_pixels, total_pixels),
        "aerosol_flag_pct": pct(aerosol_flagged_pixels, total_pixels),
        "valid_30m_coverage_pct": pct(valid_30m_pixels, total_30m_pixels),
    }


def build_tileset_metadata(scene: dict[str, Any], ingest_manifest: dict[str, Any]) -> dict[str, Any]:
    tiles = scene["tiles"]

    expected_tile_count = int(tiles["expected_tile_count"])
    produced_tile_count = int(tiles["produced_tile_count"])

    return {
        "schema_version": "v1",
        "object_type": "EcologyTilesetMetadata",
        "scheme": "xyz",
        "bounds": scene["bbox"],
        "minzoom": int(tiles.get("minzoom", 6)),
        "maxzoom": int(tiles.get("maxzoom", 12)),
        "time_start": scene["time_start"],
        "time_end": scene["time_end"],
        "expected_tile_count": expected_tile_count,
        "produced_tile_count": produced_tile_count,
        "kfm": {
            "spec_hash": ingest_manifest["canonical_spec_hash"]
        },
        "evidence_bundle_url": scene.get(
            "evidence_bundle_url",
            "kfm://evidence/ecology/pending",
        ),
        "provisional": bool(scene.get("provisional", False)),
        "allowed_fields": scene.get(
            "allowed_fields",
            ["class", "confidence", "time_start", "time_end"],
        ),
    }


def run(scene_manifest: Path, out_dir: Path) -> dict[str, str]:
    scene = load_json(scene_manifest)

    require_fields(
        scene,
        [
            "source_uris",
            "sensor",
            "collection_version",
            "bbox",
            "time_start",
            "time_end",
            "qa",
            "tiles",
        ],
    )

    ingest_manifest = build_ingest_manifest(scene)
    qa_summary = build_qa_summary(scene)
    tileset_metadata = build_tileset_metadata(scene, ingest_manifest)

    ingest_path = out_dir / "ingest_manifest.json"
    qa_path = out_dir / "qa_summary.json"
    tileset_path = out_dir / "tileset_metadata.json"

    write_json(ingest_path, ingest_manifest)
    write_json(qa_path, qa_summary)
    write_json(tileset_path, tileset_metadata)

    return {
        "ingest_manifest": str(ingest_path),
        "qa_summary": str(qa_path),
        "tileset_metadata": str(tileset_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build KFM Ecology ingest artifacts from a local HLS/Landsat scene manifest."
    )
    parser.add_argument("--scene-manifest", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()

    try:
        outputs = run(args.scene_manifest, args.out_dir)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(outputs, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
