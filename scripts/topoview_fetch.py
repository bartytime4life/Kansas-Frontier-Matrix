#!/usr/bin/env python3
"""
Topoview fetcher:
- Reads data/sources/usgs_topoview.json
- Queries TopoView API for historic topo GeoTIFFs within bbox/year range
- Downloads files into outputs.dir
- Writes README_topoview.txt index (url, year, scale, name)
- Optional: produce a simple STAC items file per map

Usage:
  python scripts/topoview_fetch.py --source data/sources/usgs_topoview.json
"""

from __future__ import annotations
import argparse, json, os, sys, time, hashlib
from pathlib import Path
from urllib.parse import urlencode
import requests
from tqdm import tqdm

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def fetch_json(url: str, params: dict) -> dict:
    # TopoView API expects GET with filters encoded; pagination supported via 'offset' param
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    return r.json()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="data/sources/usgs_topoview.json")
    p.add_argument("--max", type=int, default=None, help="cap results (for testing)")
    args = p.parse_args()

    src = json.loads(Path(args.source).read_text())
    api = src["endpoint"]["api"]
    q = src.get("query", {})
    out_dir = Path(src["outputs"]["dir"]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    readme_path = Path(src["outputs"]["readme"]).resolve()
    readme_path.parent.mkdir(parents=True, exist_ok=True)

    bbox = q.get("bbox") or src["spatial"]["bbox"]
    min_year = q.get("min_year", 1800)
    max_year = q.get("max_year", 2100)
    formats = q.get("formats", ["GeoTIFF"])
    max_results = q.get("max_results", 200)
    limit = min(max_results, args.max) if args.max else max_results

    # TopoView API params (4.1)
    base_params = {
        "bbox": ",".join(map(str, bbox)),
        "minYear": min_year,
        "maxYear": max_year,
        "limit": 100,
        "offset": 0,
        "output": "json"
    }

    records: list[dict] = []
    fetched = 0
    while fetched < limit:
        params = dict(base_params, offset=fetched)
        data = fetch_json(api, params)
        products = data.get("products", [])
        if not products:
            break
        for pdt in products:
            if "downloads" not in pdt:
                continue
            # pick GeoTIFF if present
            dl = next((d for d in pdt["downloads"] if d.get("format") in formats), None)
            if not dl:
                continue
            rec = {
                "name": pdt.get("name"),
                "year": pdt.get("year"),
                "scale": pdt.get("scale"),
                "download_url": dl.get("url"),
                "format": dl.get("format"),
                "bbox": pdt.get("bbox"),
                "series": pdt.get("series"),
                "product_id": pdt.get("productId")
            }
            records.append(rec)
        fetched += len(products)
        if len(products) < base_params["limit"]:
            break
        if fetched >= limit:
            break

    # Download
    lines = []
    for rec in tqdm(records, desc="Downloading TopoView", unit="map"):
        url = rec["download_url"]
        year = rec.get("year")
        scale = rec.get("scale")
        name = (rec.get("name") or "usgs_topo").replace(" ", "_")
        out_name = f"{name}_{year}_{scale}".replace("/", "_")
        # enforce .tif extension
        out_file = out_dir / f"{out_name}.tif"
        if out_file.exists():
            lines.append(f"{url}\t{out_file.name}\t{year}\t{scale}")
            continue
        with requests.get(url, stream=True, timeout=300) as r:
            r.raise_for_status()
            with out_file.open("wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
        # write checksum sidecar
        (out_dir / f"{out_name}.sha256").write_text(sha256(out_file))
        lines.append(f"{url}\t{out_file.name}\t{year}\t{scale}")

    # README index
    header = [
        "# USGS TopoView — Download Index",
        f"retrieved: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        f"viewer: {src['endpoint'].get('viewer','')}",
        f"bbox: {bbox}, years: {min_year}-{max_year}, formats: {formats}",
        "",
        "URL\tFILE\tYEAR\tSCALE"
    ]
    readme_path.write_text("\n".join(header + lines) + "\n")

    # patch provenance in source
    prov = src.get("provenance", {})
    prov["retrieved"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    src["provenance"] = prov
    Path(args.source).write_text(json.dumps(src, indent=2))

    print(f"Downloaded {len(lines)} maps → {out_dir}")
    print(f"Wrote {readme_path}")

if __name__ == "__main__":
    sys.exit(main())
