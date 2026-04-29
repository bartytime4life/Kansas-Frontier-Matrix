#!/usr/bin/env python3
"""
Generate a minimal STAC Item for a KFM Ecology time-slice tileset.

This emits a public-safe, no-network STAC-like Item suitable for CI dry runs
and catalog closure checks.

Example:
  python tools/validators/ecology/generate_stac_item.py \
    --item-id kfm-ecology-example-pass \
    --collection kfm-ecology-timeslices \
    --tileset-metadata tests/fixtures/ecology/timeslice/pass/tileset_metadata.json \
    --evidence-bundle kfm://evidence/ecology/example-pass-timeslice \
    --promotion-decision kfm://promotion/ecology/example-pass \
    --asset tileset=kfm://tileset/ecology/example-pass \
    --out /tmp/stac_item.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


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


def parse_asset(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError(f"asset must use key=href form, got: {value}")

    key, href = value.split("=", 1)
    key = key.strip()
    href = href.strip()

    if not key:
        raise argparse.ArgumentTypeError("asset key cannot be empty")
    if not href:
        raise argparse.ArgumentTypeError("asset href cannot be empty")

    return key, href


def bbox_to_polygon(bounds: list[float]) -> dict[str, Any]:
    if len(bounds) != 4:
        raise ValueError("bounds must have exactly 4 values: [minx, miny, maxx, maxy]")

    minx, miny, maxx, maxy = bounds

    return {
        "type": "Polygon",
        "coordinates": [
            [
                [minx, miny],
                [maxx, miny],
                [maxx, maxy],
                [minx, maxy],
                [minx, miny],
            ]
        ],
    }


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_assets(asset_pairs: list[tuple[str, str]]) -> dict[str, Any]:
    assets: dict[str, Any] = {}

    for key, href in asset_pairs:
        assets[key] = {
            "href": href,
            "roles": ["data"],
            "type": "application/octet-stream",
        }

    return assets


def build_stac_item(
    *,
    item_id: str,
    collection: str,
    tileset_metadata: dict[str, Any],
    evidence_bundle: str,
    promotion_decision: str,
    asset_pairs: list[tuple[str, str]],
    created_at: str | None = None,
) -> dict[str, Any]:
    bounds = tileset_metadata.get("bounds")
    if not isinstance(bounds, list):
        raise ValueError("tileset_metadata.bounds must be an array")

    time_start = tileset_metadata.get("time_start")
    time_end = tileset_metadata.get("time_end")
    if not time_start:
        raise ValueError("tileset_metadata.time_start is required")

    properties: dict[str, Any] = {
        "datetime": time_start,
        "start_datetime": time_start,
        "end_datetime": time_end or time_start,
        "created": created_at or utc_now(),
        "kfm:domain": "ecology",
        "kfm:evidence_bundle": evidence_bundle,
        "kfm:promotion_decision": promotion_decision,
        "kfm:spec_hash": tileset_metadata.get("kfm", {}).get("spec_hash"),
        "kfm:provisional": bool(tileset_metadata.get("provisional", False)),
        "kfm:expected_tile_count": tileset_metadata.get("expected_tile_count"),
        "kfm:produced_tile_count": tileset_metadata.get("produced_tile_count"),
        "kfm:allowed_fields": tileset_metadata.get("allowed_fields", []),
    }

    item: dict[str, Any] = {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": item_id,
        "collection": collection,
        "bbox": bounds,
        "geometry": bbox_to_polygon(bounds),
        "properties": properties,
        "links": [
            {
                "rel": "collection",
                "href": f"kfm://catalog/stac/collection/{collection}",
                "type": "application/json",
            },
            {
                "rel": "derived_from",
                "href": evidence_bundle,
                "type": "application/json",
                "title": "KFM EvidenceBundle",
            },
            {
                "rel": "via",
                "href": promotion_decision,
                "type": "application/json",
                "title": "KFM PromotionDecision",
            },
        ],
        "assets": build_assets(asset_pairs),
    }

    item["properties"]["kfm:item_hash"] = sha256_json(
        {
            "id": item_id,
            "collection": collection,
            "bbox": bounds,
            "time_start": time_start,
            "time_end": time_end,
            "evidence_bundle": evidence_bundle,
            "promotion_decision": promotion_decision,
            "assets": item["assets"],
        }
    )

    return item


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a minimal STAC Item for a KFM Ecology time-slice tileset."
    )
    parser.add_argument("--item-id", required=True)
    parser.add_argument("--collection", required=True)
    parser.add_argument("--tileset-metadata", required=True, type=Path)
    parser.add_argument("--evidence-bundle", required=True)
    parser.add_argument("--promotion-decision", required=True)
    parser.add_argument("--asset", action="append", type=parse_asset, default=[])
    parser.add_argument("--created-at")
    parser.add_argument("--out", required=True, type=Path)

    args = parser.parse_args()

    if not args.asset:
        print("ERROR: at least one --asset key=href is required", file=sys.stderr)
        return 1

    tileset_metadata = load_json(args.tileset_metadata)

    try:
        item = build_stac_item(
            item_id=args.item_id,
            collection=args.collection,
            tileset_metadata=tileset_metadata,
            evidence_bundle=args.evidence_bundle,
            promotion_decision=args.promotion_decision,
            asset_pairs=args.asset,
            created_at=args.created_at,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(item, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(item, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
