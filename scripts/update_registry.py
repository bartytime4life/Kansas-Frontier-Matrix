#!/usr/bin/env python3
"""
update_registry.py — Kansas-Frontier-Matrix

Build a registry of layers from STAC Items, optionally validate, and (optionally)
inject the registry into web/app.config.json.

Usage:
  python scripts/update_registry.py \
    --stac-dir stac/items \
    --out scripts/badges/source_map.json \
    --app-config web/app.config.json \
    [--pretty] [--no-sha] [--validate] [--strict]

Validation levels:
  --validate  : run lightweight validations (non-fatal by default)
  --strict    : make validation failures fatal (exit 2)

Checks include:
  - Item shape: type=Feature, stac_version, id, assets
  - Datetime: start_datetime<=end_datetime (lexicographically ISO-8601), both present for time-aware layers
  - BBox: 4 or 6 numbers, min<max per axis
  - Assets: href present, recommended media types, local file hint + optional sha256
  - Collection/link presence (soft check)
"""

from __future__ import annotations
import argparse
import hashlib
import json
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Acceptable (recommended) media types (extensible)
RECOMMENDED_MEDIA_TYPES = {
    "image/tiff; application=geotiff",
    "image/tiff; application=geotiff; profile=cloud-optimized",
    "image/tiff; application=geotiff; profile=cloud-optimized; cloud-optimized=true",
    "image/tiff; application=geotiff; profile=cloud-optimized; type=COG",
    "application/geo+json",
    "application/vnd.mapbox-vector-tile",
    "application/json",  # allow generic for sidecars/manifests
}

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

@dataclass
class ValIssue:
    level: str   # "ERROR" or "WARN"
    path: str    # file or JSON pointer-ish
    msg: str

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
    assets: List[AssetRef] = []
    for k, a in (obj.get("assets") or {}).items():
        href = a.get("href")
        if not href:
            continue
        asset_sha = None
        if compute_sha:
            # Only try sha if href resolves locally
            asset_path = (path.parent / href).resolve()
            if asset_path.exists() and asset_path.is_file():
                asset_sha = sha256_file(asset_path)
        assets.append(AssetRef(
            key=k,
            href=href,
            type=(a.get("type") or a.get("roles") or None) if isinstance(a.get("type"), str) else a.get("type"),
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

def _ok_iso_order(a: Optional[str], b: Optional[str]) -> bool:
    if not a or not b:
        return True
    # ISO 8601 (Z-terminated) compares lexicographically correctly for order
    return a <= b

def _bbox_valid(b: Optional[List[float]]) -> bool:
    if not isinstance(b, list): return True  # allow missing; geometry may define extent
    if len(b) not in (4, 6): return False
    try:
        nums = [float(x) for x in b]
    except Exception:
        return False
    # xmin < xmax, ymin < ymax (ignore z)
    xmin, ymin = nums[0], nums[1]
    xmax, ymax = nums[2], nums[3]
    return (xmax > xmin) and (ymax > ymin)

def validate_item(path: Path, obj: Dict[str, Any]) -> List[ValIssue]:
    issues: List[ValIssue] = []
    J = lambda p, m, lvl="ERROR": issues.append(ValIssue(lvl, p, m))

    if not is_stac_item(obj):
        J(str(path), "Not a STAC Item (missing type=Feature/stac_version/assets)")
        return issues

    # Required-ish fields
    if not obj.get("id"):
        J(f"{path}#/id", "Missing id")
    if not obj.get("collection"):
        J(f"{path}#/collection", "Missing collection", "WARN")

    props = obj.get("properties") or {}
    sdt, edt = props.get("start_datetime"), props.get("end_datetime")

    # If either present, both should be and ordered
    if (sdt and not edt) or (edt and not sdt):
        J(f"{path}#/properties", "start_datetime/end_datetime should both be present when one exists", "WARN")
    if not _ok_iso_order(sdt, edt):
        J(f"{path}#/properties", f"Temporal range invalid (start>{'end'}): {sdt} > {edt}")

    bbox = obj.get("bbox")
    if bbox is not None and not _bbox_valid(bbox):
        J(f"{path}#/bbox", f"Invalid bbox {bbox}")

    assets = obj.get("assets") or {}
    if not assets:
        J(f"{path}#/assets", "No assets in Item")

    for k, a in assets.items():
        href = a.get("href")
        if not href:
            J(f"{path}#/assets/{k}", "Asset missing href")
            continue
        mtype = a.get("type")
        if mtype and isinstance(mtype, str):
            # Soft recommendation
            if (mtype not in RECOMMENDED_MEDIA_TYPES
                and not mtype.lower().startswith("image/tiff")
                and not mtype.lower().startswith("application/geo")):
                J(f"{path}#/assets/{k}", f"Non-recommended media type: {mtype}", "WARN")

        # Local file hint check (warn only)
        if not href.startswith("http"):
            # if path is resolvable relative to item file, good; else warn
            try:
                resolved = (path.parent / href).resolve()
                if not resolved.exists():
                    J(f"{path}#/assets/{k}", f"Local href not found: {href}", "WARN")
            except Exception:
                J(f"{path}#/assets/{k}", f"Local href could not be resolved: {href}", "WARN")

    # Link presence (soft)
    links = obj.get("links") or []
    if not any((l.get("rel") == "collection") for l in links):
        J(f"{path}#/links", "Missing link rel=collection", "WARN")
    if not any((l.get("rel") == "root") for l in links):
        J(f"{path}#/links", "Missing link rel=root", "WARN")

    return issues

def build_registry(stac_dir: Path, compute_sha: bool, do_validate: bool, strict: bool) -> Tuple[Dict[str, Any], List[ValIssue]]:
    records: List[ItemRecord] = []
    all_issues: List[ValIssue] = []

    for p in find_items(stac_dir):
        try:
            obj = load_json(p)
        except RuntimeError as e:
            all_issues.append(ValIssue("ERROR", str(p), f"{e}"))
            continue

        if do_validate:
            all_issues.extend(validate_item(p, obj))

        if not is_stac_item(obj):
            continue

        rec = build_item_record(p, obj, compute_sha=compute_sha)
        if rec.id:
            records.append(rec)
        else:
            all_issues.append(ValIssue("ERROR", str(p), "Item missing id (skipped)"))

    registry = {
        "version": 1,
        "stac_root": str(stac_dir.as_posix()),
        "count": len(records),
        "items": [asdict(r) for r in records],
        "validation": {
            "errors": sum(1 for i in all_issues if i.level == "ERROR"),
            "warnings": sum(1 for i in all_issues if i.level == "WARN"),
        }
    }
    if strict and registry["validation"]["errors"] > 0:
        # Exit code will be handled in main
        pass
    return registry, all_issues

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

def print_issues(issues: List[ValIssue]):
    if not issues:
        return
    for i in issues:
        print(f"[{i.level}] {i.path}: {i.msg}")

def main(argv: List[str]) -> int:
    ap = argparse.ArgumentParser(description="Build/refresh registry from STAC; validate; inject into app config.")
    ap.add_argument("--stac-dir", default="stac/items", type=Path, help="Directory of STAC Items")
    ap.add_argument("--out", default="scripts/badges/source_map.json", type=Path, help="Where to write registry JSON")
    ap.add_argument("--app-config", default=None, type=Path, help="Optional app config to update (web/app.config.json)")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON outputs")
    ap.add_argument("--no-sha", action="store_true", help="Skip computing sha256 for local asset files")
    ap.add_argument("--validate", action="store_true", help="Run lightweight validations")
    ap.add_argument("--strict", action="store_true", help="Treat validation errors as fatal (exit 2)")
    args = ap.parse_args(argv)

    registry, issues = build_registry(
        args.stac_dir, compute_sha=not args.no_sha, do_validate=args.validate, strict=args.strict
    )

    if args.validate:
        print_issues(issues)

    write_json(args.out, registry, pretty=args.pretty)
    print(f"Wrote registry to {args.out}")

    if args.app_config:
        inject_into_app_config(args.app_config, registry, pretty=args.pretty)
        print(f"Injected registry into {args.app_config}")

    if args.validate and args.strict and registry["validation"]["errors"] > 0:
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
