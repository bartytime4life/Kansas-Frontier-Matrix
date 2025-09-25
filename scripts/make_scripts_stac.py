#!/usr/bin/env python3
"""
make_scripts_stac.py — emit a STAC Catalog/Collection/Items for scripts/

Outputs:
  scripts/catalog.json
  scripts/collections/scripts.json
  scripts/items/<name>.json
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
STAC_ROOT = SCRIPTS  # keep the STAC right inside scripts/
COLL_ID = "kfm-scripts"
COLL_TITLE = "Kansas Frontier Matrix — Helper Scripts"
WORLD_BBOX = [-180.0, -90.0, 180.0, 90.0]
OPEN_START = "2020-01-01T00:00:00Z"  # arbitrary, adjust if you prefer
OPEN_END = None

def rel_repo(p: Path) -> str:
    return str(p.resolve().relative_to(REPO)).replace("\\", "/")

def iso_mtime(p: Path) -> str:
    ts = p.stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def catalog_obj() -> Dict[str, Any]:
    return {
        "stac_version": "1.0.0",
        "type": "Catalog",
        "id": "kfm-scripts-catalog",
        "title": "Kansas Frontier Matrix — Scripts Catalog",
        "description": "A minimal STAC Catalog exposing the helper scripts used in the KFM stack.",
        "links": [
            {"rel": "self", "href": "catalog.json", "type": "application/json"},
            {"rel": "child", "href": "collections/scripts.json", "type": "application/json", "title": COLL_TITLE},
            {"rel": "root", "href": "catalog.json", "type": "application/json"}
        ]
    }

def collection_obj() -> Dict[str, Any]:
    return {
        "stac_version": "1.0.0",
        "type": "Collection",
        "id": COLL_ID,
        "title": COLL_TITLE,
        "description": "Helper CLI scripts (fetch/convert/derive/validate/package) for the Kansas-Frontier-Matrix stack.",
        "license": "MIT",
        "extent": {
            "spatial": {"bbox": [WORLD_BBOX]},
            "temporal": {"interval": [[OPEN_START, OPEN_END]]}
        },
        "links": [
            {"rel": "self", "href": "scripts.json", "type": "application/json"},
            {"rel": "root", "href": "../catalog.json", "type": "application/json"}
        ],
        "providers": [
            {"name": "Kansas-Frontier-Matrix", "roles": ["host", "processor"], "url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix"}
        ],
        "keywords": ["scripts", "automation", "GDAL", "COG", "STAC", "KML/KMZ", "validation"]
    }

def item_for_script(path: Path) -> Dict[str, Any]:
    iid = path.stem
    dt = iso_mtime(path)
    media = "text/x-python" if path.suffix.lower() == ".py" else "application/javascript"
    return {
        "stac_version": "1.0.0",
        "type": "Feature",
        "id": iid,
        "collection": COLL_ID,
        "properties": {"datetime": dt},
        "geometry": None,
        "bbox": WORLD_BBOX,
        "assets": {
            "code": {
                "href": rel_repo(path),
                "type": media,
                "roles": ["data"],
                "title": path.name
            }
        },
        "links": [
            {"rel": "collection", "href": "../collections/scripts.json", "type": "application/json"},
            {"rel": "root", "href": "../catalog.json", "type": "application/json"}
        ]
    }

def discover_scripts() -> List[Path]:
    keep = []
    for ext in (".py", ".js"):
        for p in sorted(SCRIPTS.glob(f"*{ext}")):
            # exclude the generator itself and non-script helpers (e.g., 'scripts' runner we keep)
            keep.append(p)
    return keep

def main() -> int:
    if not SCRIPTS.exists():
        print(f"[ERR] scripts/ not found at {SCRIPTS}", file=sys.stderr)
        return 2

    # write catalog & collection
    write_json(STAC_ROOT / "catalog.json", catalog_obj())
    write_json(STAC_ROOT / "collections" / "scripts.json", collection_obj())

    # items
    items_dir = STAC_ROOT / "items"
    count = 0
    for script in discover_scripts():
        item = item_for_script(script)
        write_json(items_dir / f"{script.stem}.json", item)
        count += 1

    print(f"[OK] STAC for scripts → {STAC_ROOT} (items: {count})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
