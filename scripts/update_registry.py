#!/usr/bin/env python3
"""
update_registry.py — Kansas-Frontier-Matrix
Build a registry of map layers/items from STAC and (optionally) inject into web/app.config.json.

Usage:
  python scripts/update_registry.py \
    --stac-dir stac/items \
    --out scripts/badges/source_map.json \
    --app-config web/app.config.json \
    [--pretty]

Notes:
- Assumes STAC Items live under stac/items/**.json.
- Registry entries include: id, title, collection, temporal range, bbox, asset list, and hrefs.
- If --app-config is provided, registry is written into app_config["metadata"]["registry"].

Fits the repo’s STAC→viewer flow (kgt render-config reads STAC to produce app.config.json). 
"""

from __future__ import annotations
import argparse
import hashlib
import json
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class AssetRef:
    key: str
    href: str
    type: Optional[str] = None
    title: Optional[str] = None
    sha256: Optional[str] = None


@dataclass
class ItemRecord:
    id: str
    title: Optional[str]
    collection: Optional[str]
    stac_path: str
    start_datetime: Optional[str] = None
    end_datetime: Optional[str] = None
    bbox: Optional[List[float]] = None
    geometry: Optional[Dict[str, Any]] = None
    assets: List[AssetRef] = field(default_factory=list)
    properties: Dict[str, Any] = field(default_factory=dict)


def load_json(p: Path) -> Dict[str, Any]:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Failed to parse JSON: {p} ({e})")


def sha256_file(path: Path) -> Optional[str]:
    try:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None


def find_items(stac_dir: Path) -> List[Path]:
    return sorted(stac_dir.rglob("*.json"))


def is_stac_item(obj: Dict[str, Any]) -> bool:
    # Minimal, but safe: STAC Item has "type": "Feature" and "stac_version"
    return (
        isinstance(obj, dict)
        and obj.get("type") == "Feature"
        and "stac_version" in obj
        and "assets" in obj
    )


def build_item_record(path: Path, obj: Dict[str, Any], compute_sha: bool) -> ItemRecord:
    props = obj.get("properties", {}) or {}
    bbox = obj.get("bbox")
    geom = obj.get("geometry")
    assets = []
    for k, a in (obj.get("assets") or {}).items():
        href = a.get("href")
        if not href:
            continue
        asset_sha = None
        # try to resolve href if it’s relative and compute sha256
        if compute_sha:
            asset_path = (path.parent / href).resolve()
            if asset_path.exists() and asset_path.is_file():
                asset_sha = sha256_file(asset_path)
        assets.append(AssetRef(
            key=k,
            href=href,
            type=a.get("type"),
            title=a.get("title"),
            sha256=asset_sha
        ))
    return ItemRecord(
        id=obj.get("id"),
        title=obj.get("title"),
        collection=obj.get("collection"),
        stac_path=str(path.as_posix()),
        start_datetime=props.get("start_datetime"),
        end_datetime=props.get("end_datetime"),
        bbox=bbox,
        geometry=geom,
        assets=assets,
        properties=props
    )


def build_registry(stac_dir: Path, compute_sha: bool) -> Dict[str, Any]:
    records: List[ItemRecord] = []
    for p in find_items(stac_dir):
        try:
            obj = load_json(p)
        except RuntimeError:
            continue
        if not is_stac_item(obj):
            continue
        rec = build_item_record(p, obj, compute_sha=compute_sha)
        if rec.id:
            records.append(rec)
    # Index by item id; allow multiple assets per id
    registry = {
        "version": 1,
        "stac_root": str(stac_dir.as_posix()),
        "count": len(records),
        "items": [asdict(r) for r in records],
    }
    return registry


def write_json(path: Path, data: Dict[str, Any], pretty: bool):
    path.parent.mkdir(parents=True, exist_ok=True)
    if pretty:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        path.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")


def inject_into_app_config(app_config_path: Path, registry: Dict[str, Any], pretty: bool):
    if not app_config_path.exists():
        raise FileNotFoundError(f"app config not found: {app_config_path}")
    app = load_json(app_config_path)
    meta = app.get("metadata") or {}
    meta["registry"] = registry
    app["metadata"] = meta
    write_json(app_config_path, app, pretty=pretty)


def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(description="Build/refresh layer registry from STAC and inject into app config.")
    ap.add_argument("--stac-dir", default="stac/items", type=Path, help="Directory of STAC Items")
    ap.add_argument("--out", default="scripts/badges/source_map.json", type=Path, help="Where to write registry JSON")
    ap.add_argument("--app-config", default=None, type=Path, help="Optional app config to update (web/app.config.json)")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON outputs")
    ap.add_argument("--no-sha", action="store_true", help="Skip computing sha256 for local asset files")
    args = ap.parse_args(argv)

    registry = build_registry(args.stac_dir, compute_sha=not args.no_sha)
    write_json(args.out, registry, pretty=args.pretty)
    if args.app_config:
        inject_into_app_config(args.app_config, registry, pretty=args.pretty)
        print(f"Injected registry into {args.app_config}")
    print(f"Wrote registry to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
