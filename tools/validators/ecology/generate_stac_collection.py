#!/usr/bin/env python3
"""
Generate a minimal STAC Collection for KFM Ecology time-slice STAC Items.

Example:
  python tools/validators/ecology/generate_stac_collection.py \
    --collection-id kfm-ecology-timeslices \
    --title "KFM Ecology Time Slices" \
    --description "Governed ecology time-slice products with EvidenceBundle and PromotionDecision links." \
    --item /tmp/stac_item.json \
    --out /tmp/stac_collection.json
"""

from __future__ import annotations

import argparse
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


def merge_bbox(existing: list[float] | None, new: list[float]) -> list[float]:
    if len(new) != 4:
        raise ValueError("item bbox must contain 4 values")

    if existing is None:
        return [float(v) for v in new]

    return [
        min(existing[0], float(new[0])),
        min(existing[1], float(new[1])),
        max(existing[2], float(new[2])),
        max(existing[3], float(new[3])),
    ]


def min_datetime(values: list[str]) -> str | None:
    return sorted(values)[0] if values else None


def max_datetime(values: list[str]) -> str | None:
    return sorted(values)[-1] if values else None


def item_link(item: dict[str, Any]) -> dict[str, Any]:
    item_id = item.get("id")
    if not item_id:
        raise ValueError("STAC item is missing id")

    return {
        "rel": "item",
        "href": f"kfm://catalog/stac/items/{item_id}",
        "type": "application/geo+json",
        "title": item_id,
    }


def build_collection(
    *,
    collection_id: str,
    title: str,
    description: str,
    items: list[dict[str, Any]],
    created_at: str | None = None,
) -> dict[str, Any]:
    if not items:
        raise ValueError("at least one STAC item is required")

    bbox: list[float] | None = None
    start_values: list[str] = []
    end_values: list[str] = []

    links: list[dict[str, Any]] = [
        {
            "rel": "root",
            "href": "kfm://catalog/stac",
            "type": "application/json",
            "title": "KFM STAC Catalog",
        },
        {
            "rel": "self",
            "href": f"kfm://catalog/stac/collections/{collection_id}",
            "type": "application/json",
            "title": collection_id,
        },
    ]

    for item in items:
        if item.get("collection") != collection_id:
            raise ValueError(
                f"item {item.get('id', '<missing-id>')} collection mismatch: "
                f"expected {collection_id}, got {item.get('collection')}"
            )

        item_bbox = item.get("bbox")
        if not isinstance(item_bbox, list):
            raise ValueError(f"item {item.get('id', '<missing-id>')} missing bbox")

        bbox = merge_bbox(bbox, item_bbox)

        props = item.get("properties", {})
        if props.get("start_datetime"):
            start_values.append(str(props["start_datetime"]))
        elif props.get("datetime"):
            start_values.append(str(props["datetime"]))

        if props.get("end_datetime"):
            end_values.append(str(props["end_datetime"]))
        elif props.get("datetime"):
            end_values.append(str(props["datetime"]))

        links.append(item_link(item))

    assert bbox is not None

    start = min_datetime(start_values)
    end = max_datetime(end_values)

    return {
        "stac_version": "1.0.0",
        "type": "Collection",
        "id": collection_id,
        "title": title,
        "description": description,
        "license": "varies",
        "extent": {
            "spatial": {
                "bbox": [bbox]
            },
            "temporal": {
                "interval": [[start, end]]
            },
        },
        "links": links,
        "summaries": {
            "kfm:domain": ["ecology"],
            "kfm:item_count": [len(items)],
            "kfm:created": [created_at or utc_now()],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a minimal STAC Collection for KFM Ecology time-slice items."
    )
    parser.add_argument("--collection-id", required=True)
    parser.add_argument("--title", default="KFM Ecology Time Slices")
    parser.add_argument(
        "--description",
        default=(
            "Governed ecology time-slice products with EvidenceBundle, "
            "PromotionDecision, and receipt lineage."
        ),
    )
    parser.add_argument(
        "--item",
        action="append",
        type=Path,
        default=[],
        help="Path to a STAC Item JSON file. May be provided multiple times.",
    )
    parser.add_argument("--created-at")
    parser.add_argument("--out", required=True, type=Path)

    args = parser.parse_args()

    if not args.item:
        print("ERROR: at least one --item is required", file=sys.stderr)
        return 1

    items = [load_json(path) for path in args.item]

    try:
        collection = build_collection(
            collection_id=args.collection_id,
            title=args.title,
            description=args.description,
            items=items,
            created_at=args.created_at,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(collection, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(collection, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
