#!/usr/bin/env python3
"""
KFM Ecology HLS / Landsat ingest scaffold.

Supports:
- no-network scene manifest ingest
- optional local STAC Item ingest
- optional local QA mask summary override
- optional asset copy/download placeholder mode

This script emits:
- ingest_manifest.json
- qa_summary.json
- tileset_metadata.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPORTED_SENSORS = {
    "HLS",
    "Landsat-8",
    "Landsat-9",
    "Sentinel-2"
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
        raise ValueError(f"missing required fields: {', '.join(missing)}")


def pct(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        raise ValueError("percentage denominator must be > 0")
    return round((numerator / denominator) * 100.0, 4)


def scene_from_stac_item(stac_item: dict[str, Any]) -> dict[str, Any]:
    props = stac_item.get("properties", {})
    assets = stac_item.get("assets", {})

    source_uris = []
    for asset in assets.values():
        href = asset.get("href")
        if href:
            source_uris.append(href)

    if not source_uris:
        raise ValueError("STAC item contains no asset hrefs")

    return {
        "source_uris": source_uris,
        "sensor": props.get("platform", props.get("kfm:sensor", "HLS")),
        "collection_version": props.get("collection", props.get("kfm:collection_version", "unknown")),
        "bbox": stac_item.get("bbox"),
        "time_start": props.get("start_datetime", props.get("datetime")),
        "time_end": props.get("end_datetime", props.get("datetime")),
        "qa": props.get(
            "kfm:qa",
            {
                "total_pixels": 1,
                "masked_pixels": 0,
                "aerosol_flagged_pixels": 0,
                "total_30m_pixels": 1,
                "valid_30m_pixels": 1
            },
        ),
        "tiles": props.get(
            "kfm:tiles",
            {
                "expected_tile_count": 1,
                "produced_tile_count": 1,
                "minzoom": 6,
                "maxzoom": 12
            },
        ),
        "provisional": bool(props.get("kfm:provisional", False)),
        "allowed_fields": props.get(
            "kfm:allowed_fields",
            ["class", "confidence", "time_start", "time_end"],
        ),
        "evidence_bundle_url": props.get(
            "kfm:evidence_bundle",
            "kfm://evidence/ecology/pending",
        ),
    }


def copy_local_assets(source_uris: list[str], asset_out_dir: Path) -> list[str]:
    copied: list[str] = []
    asset_out_dir.mkdir(parents=True, exist_ok=True)

    for uri in source_uris:
        if not uri.startswith("file://"):
            copied.append(uri)
            continue

        src = Path(uri.removeprefix("file://"))
        if not src.exists():
            copied.append(uri)
            continue

        dst = asset_out_dir / src.name

        if src.is_file():
            shutil.copy2(src, dst)
            copied.append(f"file://{dst}")
        else:
            copied.append(uri)

    return copied


def build_ingest_manifest(scene: dict[str, Any], *, source_uris: list[str]) -> dict[str, Any]:
    sensor = scene["sensor"]
    if sensor not in SUPPORTED_SENSORS:
        raise ValueError(
            f"unsupported sensor: {sensor}; expected one of {sorted(SUPPORTED_SENSORS)}"
        )

    spec_basis = {
        "source_uris": source_uris,
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


def build_qa_summary(scene: dict[str, Any], qa_override: dict[str, Any] | None = None) -> dict[str, Any]:
    qa = qa_override or scene["qa"]

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

    return {
        "schema_version": "v1",
        "object_type": "EcologyTilesetMetadata",
        "scheme": "xyz",
        "bounds": scene["bbox"],
        "minzoom": int(tiles.get("minzoom", 6)),
        "maxzoom": int(tiles.get("maxzoom", 12)),
        "time_start": scene["time_start"],
        "time_end": scene["time_end"],
        "expected_tile_count": int(tiles["expected_tile_count"]),
        "produced_tile_count": int(tiles["produced_tile_count"]),
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


def load_scene(args: argparse.Namespace) -> dict[str, Any]:
    if args.scene_manifest:
        return load_json(args.scene_manifest)

    if args.stac_item:
        return scene_from_stac_item(load_json(args.stac_item))

    raise ValueError("one of --scene-manifest or --stac-item is required")


def run(
    *,
    scene_manifest: Path | None,
    stac_item: Path | None,
    qa_mask: Path | None,
    out_dir: Path,
    download_assets: bool,
    asset_out_dir: Path | None,
) -> dict[str, str]:
    args = argparse.Namespace(scene_manifest=scene_manifest, stac_item=stac_item)
    scene = load_scene(args)

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

    source_uris = list(scene["source_uris"])

    if download_assets:
        if not asset_out_dir:
            raise ValueError("--asset-out-dir is required when --download-assets is used")
        source_uris = copy_local_assets(source_uris, asset_out_dir)

    qa_override = load_json(qa_mask) if qa_mask else None

    ingest_manifest = build_ingest_manifest(scene, source_uris=source_uris)
    qa_summary = build_qa_summary(scene, qa_override=qa_override)
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
        description="Build KFM Ecology ingest artifacts from local HLS/Landsat fixture or STAC metadata."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--scene-manifest", type=Path)
    source.add_argument("--stac-item", type=Path)

    parser.add_argument("--qa-mask", type=Path)
    parser.add_argument("--download-assets", action="store_true")
    parser.add_argument("--asset-out-dir", type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)

    args = parser.parse_args()

    try:
        outputs = run(
            scene_manifest=args.scene_manifest,
            stac_item=args.stac_item,
            qa_mask=args.qa_mask,
            out_dir=args.out_dir,
            download_assets=args.download_assets,
            asset_out_dir=args.asset_out_dir,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(outputs, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
