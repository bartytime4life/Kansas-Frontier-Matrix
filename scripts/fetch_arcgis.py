#!/usr/bin/env python3
"""
Fetch ArcGIS ImageService/FeatureService layers to local files.

Usage:
  python scripts/fetch_arcgis.py --sources data/sources --out data/raw

Each JSON in --sources should look like:
{
  "id": "ks_hillshade",
  "title": "Kansas Elevation Hillshade",
  "type": "arcgis-imagery",            # or "arcgis-feature"
  "url": "https://example.com/ArcGIS/rest/services/.../ImageServer",
  "format": "geotiff",                 # geotiff|png|jpg (imagery) or geojson (feature)
  "bbox": [-102.05, 36.99, -94.59, 40.00],  # WGS84 bounds (Kansas approx); edit as needed
  "pixel_size": 30,                    # meters; used for export
  "crs": "EPSG:4326"
}
"""
from __future__ import annotations
import argparse, json, os, sys, pathlib, time
from typing import Dict, Any, List
import requests
from tqdm import tqdm

def list_sources(dirpath: str) -> List[pathlib.Path]:
    p = pathlib.Path(dirpath)
    return [q for q in p.glob("*.json") if q.is_file()]

def export_imagery(source: Dict[str, Any], outdir: pathlib.Path) -> None:
    url = source["url"].rstrip("/")
    fmt = source.get("format", "geotiff").lower()
    bbox = source["bbox"]
    pixel_size = source.get("pixel_size", 30)
    crs = source.get("crs", "EPSG:4326")
    outname = f"{source['id']}.{ 'tif' if fmt=='geotiff' else fmt }"
    outpath = outdir / outname

    export_url = f"{url}/exportImage"
    params = {
        "bbox": ",".join(map(str, bbox)),
        "bboxSR": 4326,
        "imageSR": 4326,
        "size": ",".join(map(str, _estimate_pixels(bbox, pixel_size))),
        "format": "tiff" if fmt == "geotiff" else fmt,
        "f": "image"
    }
    r = requests.get(export_url, params=params, timeout=120)
    r.raise_for_status()
    outdir.mkdir(parents=True, exist_ok=True)
    with open(outpath, "wb") as f:
        f.write(r.content)
    print(f"[OK] Imagery → {outpath}")

def _estimate_pixels(bbox, pixel_size_m):
    # rough estimate: assuming ~111km per degree latitude; scale lon by cos(lat)
    import math
    minx, miny, maxx, maxy = bbox
    lat_km = (maxy - miny) * 111_000.0
    midlat = 0.5*(miny+maxy)
    lon_km = (maxx - minx) * 111_000.0 * math.cos(math.radians(midlat))
    nx = max(1, int(lon_km / pixel_size_m))
    ny = max(1, int(lat_km / pixel_size_m))
    return nx, ny

def export_feature(source: Dict[str, Any], outdir: pathlib.Path) -> None:
    url = source["url"].rstrip("/")
    query_url = f"{url}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "f": "geojson"
    }
    r = requests.get(query_url, params=params, timeout=120)
    r.raise_for_status()
    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / f"{source['id']}.geojson"
    with open(outpath, "wb") as f:
        f.write(r.content)
    print(f"[OK] Features → {outpath}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", required=True, help="Folder of source JSON files")
    ap.add_argument("--out", required=True, help="Output folder")
    args = ap.parse_args()

    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    for src_path in list_sources(args.sources):
        src = json.loads(src_path.read_text(encoding="utf-8"))
        t = src["type"]
        if t == "arcgis-imagery":
            export_imagery(src, outdir)
        elif t == "arcgis-feature":
            export_feature(src, outdir)
        else:
            print(f"[SKIP] Unknown type: {t} in {src_path}")

if __name__ == "__main__":
    main()
