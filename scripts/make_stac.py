#!/usr/bin/env python3
"""
make_stac.py — build tiny STAC collections/items from sources + discovered assets.

Assumptions:
- Collections: elevation (DEM/hillshade), historic_topo (rasters from overlays), vectors (geojson).
- Items: one per raster/geojson with asset href relative to repo.
"""
from __future__ import annotations
import argparse, json, re, sys, time
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA = REPO_ROOT / "data"
COGS = DATA / "cogs"
VECT = DATA / "processed" / "vectors"
STAC = DATA / "stac"

def load_sources(src_dir: Path) -> Dict[str, Any]:
    sources = {}
    for p in src_dir.glob("*.json"):
        try:
            sources[p.stem] = json.loads(p.read_text())
        except Exception:
            pass
    return sources

def rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT)).replace("\\", "/")

def write_json(path: Path, obj: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))

def collection(id_: str, desc: str, bbox, interval) -> Dict[str, Any]:
    return {
        "type": "Collection",
        "id": id_,
        "stac_version": "1.0.0",
        "description": desc,
        "license": "various",
        "extent": {
            "spatial": {"bbox": [bbox]},
            "temporal": {"interval": [[interval[0], interval[1]]]}
        }
    }

def item_raster(cid: str, rid: str, raster: Path, start=None, end=None, extra=None) -> Dict[str, Any]:
    start = start or None
    end = end or start
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": rid,
        "collection": cid,
        "properties": {"start_datetime": start, "end_datetime": end},
        "geometry": None,
        "bbox": None,
        "assets": {
            "data": {
                "href": rel(raster),
                "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                "roles": ["data"]
            },
            **(extra or {})
        },
        "links": [{"rel": "collection", "href": f"../collections/{cid}.json"}]
    }

def item_vector(cid: str, vid: str, vec: Path, start=None, end=None) -> Dict[str, Any]:
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": vid,
        "collection": cid,
        "properties": {"start_datetime": start, "end_datetime": end},
        "geometry": None,
        "bbox": None,
        "assets": {
            "data": {
                "href": rel(vec),
                "type": "application/geo+json",
                "roles": ["data"]
            }
        },
        "links": [{"rel": "collection", "href": f"../collections/{cid}.json"}]
    }

def infer_year(name: str) -> str | None:
    m = re.search(r"(18|19|20)\d{2}", name)
    return f"{m.group(0)}-01-01T00:00:00Z" if m else None

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default=str(DATA / "sources"))
    ap.add_argument("--out", default=str(STAC))
    args = ap.parse_args()

    out = Path(args.out)
    sources = load_sources(Path(args.sources))

    # Collections
    elev_bbox = [-102.1, 36.99, -94.6, 40.0]
    ks_interval = ["1800-01-01T00:00:00Z", "2100-12-31T23:59:59Z"]
    write_json(out / "collections" / "elevation.json", collection("elevation", "Kansas DEM & terrain", elev_bbox, ks_interval))
    write_json(out / "collections" / "historic_topo.json", collection("historic_topo", "USGS historic topo overlays", elev_bbox, ks_interval))
    write_json(out / "collections" / "vectors.json", collection("vectors", "Historical vectors (treaties, railroads...)", elev_bbox, ks_interval))

    # Items: rasters in cogs/*
    items: List[Dict[str, Any]] = []
    for sub in ["dem", "hillshade", "overlays", "landcover"]:
        pdir = COGS / sub
        if not pdir.exists(): continue
        for tif in sorted(pdir.glob("*.tif")):
            cid = "elevation" if sub in {"dem", "hillshade"} else "historic_topo"
            iid = tif.stem
            year = infer_year(tif.name)
            items.append((cid, iid, tif, year))

    for cid, iid, tif, year in items:
        extra = {}
        meta = tif.with_suffix(".meta.json")
        if meta.exists():
            extra["provenance"] = {"href": rel(meta), "type": "application/json", "roles": ["metadata"]}
        write_json(out / "items" / f"{iid}.json", item_raster(cid, iid, tif, start=year, end=year, extra=extra))

    # Items: vectors
    if VECT.exists():
        for gj in sorted(VECT.glob("*.geojson")):
            iid = gj.stem
            year = infer_year(gj.name)
            write_json(out / "items" / f"{iid}.json", item_vector("vectors", iid, gj, start=year, end=year))

    print(f"[OK] STAC collections/items written → {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
