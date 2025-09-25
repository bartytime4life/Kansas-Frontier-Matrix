#!/usr/bin/env python3
"""
make_stac.py — build small STAC collections & items from repo assets.

What it does
------------
- Creates collections:
    * elevation         → DEM/Hillshade (data/cogs/dem, data/cogs/hillshade)
    * historic_topo     → overlays/landcover rasters (data/cogs/overlays, data/cogs/landcover)
    * vectors           → geojson vectors (data/processed/vectors)
- Creates one STAC Item per raster/vector with repo-relative hrefs.
- Ensures bbox is present (valid) and temporal rule is satisfied (datetime or start/end).
- Optionally populate checksum/size from sidecars / file stats.

Usage
-----
  # default (Kansas bbox/interval)
  python scripts/make_stac.py

  # override bbox/interval
  python scripts/make_stac.py \
    --bbox -102.05 36.99 -94.59 40.00 \
    --interval 1800-01-01T00:00:00Z 2100-12-31T23:59:59Z

Notes
-----
- Pure stdlib. Sidecar checksum: reads "<file>.sha256" or "<file>.<ext>.sha256".
- This script does not compute geometry; bbox is sufficient for most viewers/validators.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# --- repo paths ----------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]
DATA = REPO_ROOT / "data"
COGS = DATA / "cogs"
VECT = DATA / "processed" / "vectors"
STAC = REPO_ROOT / "stac"          # canonical top-level STAC tree

# Kansas defaults (can override via CLI)
KS_BBOX_DEFAULT = (-102.05, 36.99, -94.59, 40.00)
KS_INTERVAL_DEFAULT = ("1800-01-01T00:00:00Z", "2100-12-31T23:59:59Z")


# --- small IO helpers ----------------------------------------------
def rel_repo(p: Path) -> str:
    """repo-relative POSIX path string"""
    return str(p.resolve().relative_to(REPO_ROOT)).replace("\\", "/")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_text_first_line(p: Path) -> Optional[str]:
    try:
        s = p.read_text(encoding="utf-8").strip()
        if not s:
            return None
        return s.splitlines()[0]
    except FileNotFoundError:
        return None


def parse_sha256_sidecar(file_path: Path) -> Optional[str]:
    """
    Accept formats:
      "<hex>"
      "<hex>  <filename>"
      "SHA256 (<filename>) = <hex>"
    """
    cands = [
        file_path.with_suffix(file_path.suffix + ".sha256"),
        file_path.with_suffix("").with_suffix(".sha256"),
    ]
    for side in cands:
        line = read_text_first_line(side)
        if not line:
            continue
        s = line.strip()
        if s.lower().startswith("sha256"):
            parts = s.split("=", 1)
            if len(parts) == 2:
                hexpart = parts[1].strip()
                if len(hexpart) == 64 and all(c in "0123456789abcdefABCDEF" for c in hexpart):
                    return hexpart.lower()
        token = s.split()[0]
        if len(token) == 64 and all(c in "0123456789abcdefABCDEF" for c in token):
            return token.lower()
    return None


# --- STAC builders -------------------------------------------------
def collection_obj(
    id_: str,
    title: str,
    desc: str,
    bbox: Tuple[float, float, float, float],
    interval: Tuple[str, str],
    license_str: str = "various",
) -> Dict[str, Any]:
    west, south, east, north = bbox
    start, end = interval
    return {
        "stac_version": "1.0.0",
        "type": "Collection",
        "id": id_,
        "title": title,
        "description": desc,
        "license": license_str,
        "extent": {
            "spatial": {"bbox": [[west, south, east, north]]},
            "temporal": {"interval": [[start, end]]},
        },
        "links": [],
    }


def raster_item_obj(
    cid: str,
    iid: str,
    raster: Path,
    *,
    bbox: Tuple[float, float, float, float],
    dt: Optional[str],
    start: Optional[str],
    end: Optional[str],
    sidecar_meta: Optional[Path] = None,
) -> Dict[str, Any]:
    west, south, east, north = bbox
    # Temporal rule: either datetime or start+end
    props: Dict[str, Any] = {}
    if dt:
        props["datetime"] = dt
    else:
        props["start_datetime"] = start
        props["end_datetime"] = end

    # Asset
    asset: Dict[str, Any] = {
        "href": rel_repo(raster),
        "type": "image/tiff; application=geotiff; profile=cloud-optimized",
        "roles": ["data"],
    }
    # Optional checksum/size
    try:
        size = os.path.getsize(raster)
        asset["file:size"] = int(size)
    except Exception:
        pass
    hexsum = parse_sha256_sidecar(raster)
    if hexsum:
        asset["checksum:sha256"] = hexsum

    # Optional provenance link
    extra_assets: Dict[str, Any] = {}
    if sidecar_meta and sidecar_meta.exists():
        extra_assets["provenance"] = {
            "href": rel_repo(sidecar_meta),
            "type": "application/json",
            "roles": ["metadata"],
            "title": f"{raster.name} metadata",
        }

    item = {
        "stac_version": "1.0.0",
        "type": "Feature",
        "id": iid,
        "collection": cid,
        "properties": props,
        "geometry": None,             # viewers OK; bbox present below
        "bbox": [west, south, east, north],
        "assets": {"data": asset, **extra_assets},
        "links": [
            {"rel": "collection", "href": f"../collections/{cid}.json", "type": "application/json"},
            {"rel": "root", "href": "../catalog.json", "type": "application/json"},
        ],
    }
    return item


def vector_item_obj(
    cid: str,
    iid: str,
    vec: Path,
    *,
    bbox: Tuple[float, float, float, float],
    dt: Optional[str],
    start: Optional[str],
    end: Optional[str],
) -> Dict[str, Any]:
    west, south, east, north = bbox
    props: Dict[str, Any] = {}
    if dt:
        props["datetime"] = dt
    else:
        props["start_datetime"] = start
        props["end_datetime"] = end

    item = {
        "stac_version": "1.0.0",
        "type": "Feature",
        "id": iid,
        "collection": cid,
        "properties": props,
        "geometry": None,
        "bbox": [west, south, east, north],
        "assets": {
            "data": {
                "href": rel_repo(vec),
                "type": "application/geo+json",
                "roles": ["data"],
            }
        },
        "links": [
            {"rel": "collection", "href": f"../collections/{cid}.json", "type": "application/json"},
            {"rel": "root", "href": "../catalog.json", "type": "application/json"},
        ],
    }
    return item


# --- utilities -----------------------------------------------------
YEAR_RX = re.compile(r"(18|19|20)\d{2}")

def infer_year_dt(name: str) -> Optional[str]:
    m = YEAR_RX.search(name)
    return f"{m.group(0)}-01-01T00:00:00Z" if m else None


def discover_rasters() -> List[Tuple[str, Path]]:
    """Return list of (collection_id, raster_path)."""
    out: List[Tuple[str, Path]] = []
    # elevation
    for sub in ("dem", "hillshade"):
        d = COGS / sub
        if d.exists():
            for tif in sorted(d.glob("*.tif")):
                out.append(("elevation", tif))
    # historic_topo (overlays / landcover)
    for sub in ("overlays", "landcover"):
        d = COGS / sub
        if d.exists():
            for tif in sorted(d.glob("*.tif")):
                out.append(("historic_topo", tif))
    return out


def discover_vectors() -> List[Tuple[str, Path]]:
    """Return list of (collection_id, vector_path)."""
    out: List[Tuple[str, Path]] = []
    if VECT.exists():
        for gj in sorted(VECT.glob("*.geojson")):
            out.append(("vectors", gj))
    return out


# --- main ----------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="Build minimal STAC from repo assets.")
    ap.add_argument("--out", default=str(STAC), help="STAC root directory (default: stac/)")
    ap.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"),
                    help="Override bbox (default: Kansas)")
    ap.add_argument("--interval", nargs=2, metavar=("START_ISO", "END_ISO"),
                    help="Override temporal interval (default: Kansas wide)")
    args = ap.parse_args()

    stac_root = Path(args.out).resolve()
    bbox = tuple(args.bbox) if args.bbox else KS_BBOX_DEFAULT  # type: ignore[assignment]
    interval = tuple(args.interval) if args.interval else KS_INTERVAL_DEFAULT  # type: ignore[assignment]

    # Collections
    write_json(
        stac_root / "collections" / "elevation.json",
        collection_obj(
            "elevation",
            "Kansas Elevation & Terrain",
            "DEM, hillshade, and terrain products for Kansas.",
            bbox, interval,
        ),
    )
    write_json(
        stac_root / "collections" / "historic_topo.json",
        collection_obj(
            "historic_topo",
            "USGS Historic Topographic Overlays",
            "Georeferenced USGS historical topographic sheets and thematic rasters for Kansas.",
            bbox, interval,
        ),
    )
    write_json(
        stac_root / "collections" / "vectors.json",
        collection_obj(
            "vectors",
            "Historical Vectors (treaties, rails, trails, etc.)",
            "Vector datasets (GeoJSON) used in the Kansas Frontier Matrix.",
            bbox, interval,
        ),
    )

    # Items: rasters
    for cid, tif in discover_rasters():
        iid = tif.stem
        dt = infer_year_dt(tif.name)
        start = dt
        end = dt
        meta = tif.with_suffix(".meta.json")  # optional
        item = raster_item_obj(
            cid, iid, tif,
            bbox=bbox,
            dt=dt, start=start, end=end,
            sidecar_meta=meta if meta.exists() else None,
        )
        write_json(stac_root / "items" / f"{iid}.json", item)

    # Items: vectors
    for cid, gj in discover_vectors():
        iid = gj.stem
        dt = infer_year_dt(gj.name)
        start = dt
        end = dt
        item = vector_item_obj(cid, iid, gj, bbox=bbox, dt=dt, start=start, end=end)
        write_json(stac_root / "items" / f"{iid}.json", item)

    print(f"[OK] STAC collections/items written → {stac_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
