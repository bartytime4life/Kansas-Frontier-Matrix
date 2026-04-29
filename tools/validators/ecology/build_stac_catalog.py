#!/usr/bin/env python3
"""
Build a minimal STAC Catalog for KFM Ecology collections.

Example:
  python tools/validators/ecology/build_stac_catalog.py \
    --catalog-id kfm-ecology-catalog \
    --title "KFM Ecology STAC Catalog" \
    --description "Governed KFM Ecology catalog with receipt-backed collections." \
    --collection /tmp/stac_collection.json \
    --out /tmp/stac_catalog.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def collection_link(collection: dict[str, Any]) -> dict[str, Any]:
    collection_id = collection.get("id")
    if not collection_id:
        raise ValueError("STAC collection is missing id")

    return {
        "rel": "child",
        "href": f"kfm://catalog/stac/collections/{collection_id}",
        "type": "application/json",
        "title": str(collection.get("title", collection_id)),
    }


def build_catalog(
    *,
    catalog_id: str,
    title: str,
    description: str,
    collections: list[dict[str, Any]],
) -> dict[str, Any]:
    if not collections:
        raise ValueError("at least one STAC collection is required")

    links: list[dict[str, Any]] = [
        {
            "rel": "self",
            "href": "kfm://catalog/stac",
            "type": "application/json",
            "title": title,
        }
    ]

    for collection in collections:
        if collection.get("type") != "Collection":
            raise ValueError(
                f"collection {collection.get('id', '<missing-id>')} has invalid type"
            )

        links.append(collection_link(collection))

    return {
        "stac_version": "1.0.0",
        "type": "Catalog",
        "id": catalog_id,
        "title": title,
        "description": description,
        "links": links,
        "kfm:domain": "ecology",
        "kfm:collection_count": len(collections),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a minimal STAC Catalog for KFM Ecology collections."
    )
    parser.add_argument("--catalog-id", required=True)
    parser.add_argument("--title", default="KFM Ecology STAC Catalog")
    parser.add_argument(
        "--description",
        default="Governed KFM Ecology STAC catalog with receipt-backed collections.",
    )
    parser.add_argument(
        "--collection",
        action="append",
        type=Path,
        default=[],
        help="Path to a STAC Collection JSON file. May be provided multiple times.",
    )
    parser.add_argument("--out", required=True, type=Path)

    args = parser.parse_args()

    if not args.collection:
        print("ERROR: at least one --collection is required", file=sys.stderr)
        return 1

    collections = [load_json(path) for path in args.collection]

    try:
        catalog = build_catalog(
            catalog_id=args.catalog_id,
            title=args.title,
            description=args.description,
            collections=collections,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(catalog, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(catalog, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
