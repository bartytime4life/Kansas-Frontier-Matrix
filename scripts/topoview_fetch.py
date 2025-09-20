#!/usr/bin/env python3
"""
Topoview fetcher (robust edition)

What it does
------------
- Reads a source config (default: data/sources/usgs_topoview.json)
- Calls the USGS TopoView API (v4.x) with bbox/year filters and pagination
- Filters by formats/scales/series (if provided)
- Downloads rasters (streamed) to a target directory
- Writes a README index and a machine-readable manifest for MPC/CI
- Optionally emits one STAC Item per map into a target stac/ directory

Config shape (example)
----------------------
{
  "endpoint": {
    "api":    "https://topoviewapi.usgs.gov/4.1/products",
    "viewer": "https://ngmdb.usgs.gov/topoview/"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.59, 40.00]        # WGS84 (west, south, east, north)
  },
  "query": {
    "min_year": 1870,
    "max_year": 1950,
    "formats": ["GeoTIFF"],                        # match 'downloads[].format'
    "series": ["US Topo", "Historic Topographic"], # optional, substring match
    "scales": [24000, 62500],                      # optional, numeric/int or string
    "max_results": 200                             # cap API enumeration
  },
  "outputs": {
    "dir":    "data/raw/topoview",                 # download directory
    "readme": "data/raw/topoview/README_topoview.txt"
  }
}

Usage
-----
  # default source path, standard flow
  python scripts/topoview_fetch.py

  # explicit source, cap to 25 results, write STAC items
  python scripts/topoview_fetch.py --source data/sources/usgs_topoview.json \
         --max 25 --stac-dir data/stac/topoview

Notes
-----
- This script is dependency-light: requests, tqdm (optional if --no-progress).
- It does *not* reproject or regionate rasters. Use your COG/regionation pipeline elsewhere.
- API behavior can vary; we keep the request conservative and robust.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

import requests
from requests.adapters import HTTPAdapter, Retry

try:
    from tqdm import tqdm
    HAS_TQDM = True
except Exception:
    HAS_TQDM = False

Json = Dict[str, Any]
PathLike = Union[str, os.PathLike[str]]

# ------------------------------------------------------------------------------
# HTTP session (retries/backoff)
# ------------------------------------------------------------------------------

def build_session(
    *,
    user_agent: Optional[str] = None,
    retries: int = 4,
    backoff: float = 0.4,
    timeout: float = 60.0,
) -> requests.Session:
    sess = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=16, pool_maxsize=32)
    sess.mount("http://", adapter)
    sess.mount("https://", adapter)
    sess.headers.update({
        "Accept": "application/json, */*;q=0.1",
        "User-Agent": user_agent or "kfm-topoview/1.0",
    })
    # shim a default timeout
    orig = sess.request
    def _req(method, url, **kw):
        if "timeout" not in kw:
            kw["timeout"] = timeout
        return orig(method, url, **kw)
    sess.request = _req  # type: ignore[assignment]
    return sess


# ------------------------------------------------------------------------------
# Small I/O helpers
# ------------------------------------------------------------------------------

def read_json(path: PathLike) -> Json:
    return json.loads(Path(path).read_text(encoding="utf-8"))

def write_json(path: PathLike, obj: Mapping[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")

def sha256_file(path: PathLike, *, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

def sidecar_sha(path: PathLike, sha: str) -> None:
    Path(f"{path}.sha256").write_text(sha + "\n", encoding="utf-8")

def safe_name(s: str) -> str:
    s = re.sub(r"\s+", "_", s.strip())
    return "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in s)


# ------------------------------------------------------------------------------
# TopoView querying
# ------------------------------------------------------------------------------

@dataclass
class SourceConfig:
    api: str
    viewer: Optional[str]
    bbox: List[float]
    min_year: int
    max_year: int
    formats: List[str]
    series: Optional[List[str]]
    scales: Optional[List[Union[int, str]]]
    max_results: int
    out_dir: Path
    readme: Path

    @classmethod
    def from_file(cls, path: PathLike) -> "SourceConfig":
        src = read_json(path)
        api = src["endpoint"]["api"]
        viewer = src["endpoint"].get("viewer")
        bbox = src.get("query", {}).get("bbox") or src["spatial"]["bbox"]
        q = src.get("query", {})
        min_year = int(q.get("min_year", 1800))
        max_year = int(q.get("max_year", 2100))
        formats = list(q.get("formats", ["GeoTIFF"]))
        series = q.get("series")  # optional list
        scales = q.get("scales")  # optional list (ints/strings)
        max_results = int(q.get("max_results", 200))
        out_dir = Path(src["outputs"]["dir"]).resolve()
        readme = Path(src["outputs"]["readme"]).resolve()
        return cls(api, viewer, bbox, min_year, max_year, formats, series, scales, max_results, out_dir, readme)


@dataclass
class Product:
    name: str
    year: Optional[int]
    scale: Optional[Union[int, str]]
    download_url: str
    fmt: str
    bbox: Optional[List[float]]
    series: Optional[str]
    product_id: Optional[str]


def _fetch_page(sess: requests.Session, api: str, params: Dict[str, Any]) -> Json:
    r = sess.get(api, params=params)
    # Some errors are returned as JSON with HTTP 200
    ctype = r.headers.get("Content-Type", "")
    if "application/json" in ctype:
        obj = r.json()
        if isinstance(obj, dict) and obj.get("error"):
            raise RuntimeError(obj.get("error"))
        if r.status_code >= 400:
            raise RuntimeError(obj)
        return obj
    r.raise_for_status()
    return r.json()


def iter_products(
    sess: requests.Session,
    cfg: SourceConfig,
    *,
    limit: Optional[int] = None,
) -> Iterable[Product]:
    """
    Iterate products from TopoView with paging. We keep the query conservative (bbox & year range),
    and then filter locally by formats/series/scales.
    """
    base_params = {
        "bbox": ",".join(map(str, cfg.bbox)),
        "minYear": cfg.min_year,
        "maxYear": cfg.max_year,
        "limit": 100,          # API page size; we page with offset
        "offset": 0,
        "output": "json"
    }
    fetched = 0
    cap = limit if limit is not None else cfg.max_results

    while fetched < cap:
        params = dict(base_params, offset=fetched)
        data = _fetch_page(sess, cfg.api, params)
        prods = data.get("products", [])
        if not prods:
            break

        for pdt in prods:
            # Filter by downloads format
            dls = [d for d in pdt.get("downloads", []) if d.get("format") in cfg.formats]
            if not dls:
                continue

            # Optional filters: series / scales
            if cfg.series:
                s = (pdt.get("series") or "").lower()
                if not any(sr.lower() in s for sr in cfg.series):
                    continue
            if cfg.scales:
                pscale = pdt.get("scale")
                # normalize both sides to ints if possible
                def _norm(x):
                    try:
                        return int(str(x).replace(",", ""))
                    except Exception:
                        return str(x)
                pscale_n = _norm(pscale)
                if not any(_norm(s) == pscale_n for s in cfg.scales):
                    continue

            # Pick first matching format (prefer GeoTIFF if present)
            dl = None
            for prefer in ("GeoTIFF",) + tuple(f for f in cfg.formats if f != "GeoTIFF"):
                dl = next((d for d in dls if d.get("format") == prefer), None) or dl
            if not dl:
                continue

            yield Product(
                name=pdt.get("name") or "usgs_topo",
                year=pdt.get("year"),
                scale=pdt.get("scale"),
                download_url=dl.get("url"),
                fmt=dl.get("format"),
                bbox=pdt.get("bbox"),
                series=pdt.get("series"),
                product_id=pdt.get("productId"),
            )

        fetched += len(prods)
        if len(prods) < base_params["limit"]:
            break
        if fetched >= cap:
            break


# ------------------------------------------------------------------------------
# Download + index + stac
# ------------------------------------------------------------------------------

def download_file(sess: requests.Session, url: str, dst: Path, *, overwrite: bool, show_progress: bool) -> Tuple[bool, Optional[str]]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and not overwrite:
        sha = sha256_file(dst)
        sidecar_sha(dst, sha)
        return True, sha

    with sess.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length", "0") or 0)

        if HAS_TQDM and show_progress:
            bar = tqdm(total=total, unit="B", unit_scale=True, desc=dst.name)
        else:
            bar = None

        try:
            with dst.open("wb") as f:
                for chunk in r.iter_content(chunk_size=1 << 20):
                    if chunk:
                        f.write(chunk)
                        if bar:
                            bar.update(len(chunk))
        finally:
            if bar:
                bar.close()

    sha = sha256_file(dst)
    sidecar_sha(dst, sha)
    return True, sha


def stac_item_for_product(p: Product, cfg: SourceConfig, local_path: Path) -> Json:
    """
    Minimal STAC Item for a TopoView map (raster asset).
    """
    west, south, east, north = (p.bbox or cfg.bbox)
    dt_year = p.year if isinstance(p.year, int) else None
    iso = f"{dt_year:04d}-01-01T00:00:00Z" if dt_year else None
    item_id = f"usgs-topoview-{safe_name(p.product_id or p.name)}"

    geom = {
        "type": "Polygon",
        "coordinates": [[
            [west, south],
            [east, south],
            [east, north],
            [west, north],
            [west, south]
        ]]
    }

    assets = {
        "source": {
            "href": str(local_path),
            "type": "image/tiff; application=geotiff",
            "roles": ["data", "source"],
            "title": p.name
        }
    }

    item = {
        "stac_version": "1.0.0",
        "type": "Feature",
        "id": item_id,
        "geometry": geom,
        "bbox": [west, south, east, north],
        "properties": {
            "datetime": iso,
            "usgs:series": p.series,
            "usgs:scale": p.scale,
            "usgs:product_id": p.product_id
        },
        "assets": assets,
        "links": [
            {"rel": "via", "href": p.download_url, "title": "Original download URL"},
            {"rel": "about", "href": cfg.viewer or "", "title": "TopoView viewer"}
        ],
        "license": "US-PD",
        "providers": [
            {"name": "USGS", "roles": ["producer", "licensor"], "url": "https://www.usgs.gov/"},
        ]
    }
    return item


# ------------------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------------------

@dataclass
class Summary:
    total_products: int
    downloaded: int
    skipped: int
    failures: int
    elapsed_s: float

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fetch USGS TopoView maps by bbox and year.")
    p.add_argument("--source", default="data/sources/usgs_topoview.json",
                   help="Path to source config JSON (default: data/sources/usgs_topoview.json)")
    p.add_argument("--max", type=int, default=None, help="Cap results for testing")
    p.add_argument("--stac-dir", type=Path, default=None, help="If set, write one STAC Item per map here")
    p.add_argument("--retries", type=int, default=4, help="HTTP retries (default 4)")
    p.add_argument("--timeout", type=float, default=60.0, help="HTTP timeout seconds (default 60)")
    p.add_argument("--user-agent", default=None, help="Custom User-Agent string")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    p.add_argument("--no-progress", action="store_true", help="Disable tqdm progress bars")
    p.add_argument("--manifest", type=Path, default=Path("data/raw/topoview/manifest.topoview.json"),
                   help="Manifest JSON output path")
    return p.parse_args()


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args()
    t0 = time.time()

    # Load config
    cfg = SourceConfig.from_file(args.source)

    # Prepare output dirs
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    cfg.readme.parent.mkdir(parents=True, exist_ok=True)
    if args.stac_dir:
        args.stac_dir.mkdir(parents=True, exist_ok=True)

    # Session
    sess = build_session(user_agent=args.user_agent, retries=args.retries, timeout=args.timeout)

    # Enumerate products
    products = list(iter_products(sess, cfg, limit=args.max))
    total = len(products)

    if total == 0:
        print("[WARN] No products matched filters.")
        return 1

    # Download loop
    lines: List[str] = []
    downloaded = 0
    skipped = 0
    failures = 0
    stac_paths: List[str] = []

    iterator: Iterable[Product]
    if HAS_TQDM and not args.no_progress:
        iterator = tqdm(products, desc="Downloading TopoView", unit="map")
    else:
        iterator = products

    for rec in iterator:
        # Compose output filename: <safe-name>_<year>_<scale>.tif
        name = safe_name(rec.name or "usgs_topo")
        year = rec.year or "NA"
        scale = rec.scale or "NA"
        # Some scales may include slashes or commas; safe_name covers that
        out_name = f"{name}_{year}_{scale}.tif"
        out_file = cfg.out_dir / out_name

        try:
            ok, sha = download_file(sess, rec.download_url, out_file,
                                    overwrite=bool(args.overwrite),
                                    show_progress=False if (HAS_TQDM and not args.no_progress) else False)
            if ok:
                downloaded += 0 if out_file.exists() and not args.overwrite else 1
                if out_file.exists() and not args.overwrite:
                    skipped += 1
                lines.append(f"{rec.download_url}\t{out_file.name}\t{rec.year}\t{rec.scale}")
                # STAC item
                if args.stac_dir:
                    item = stac_item_for_product(rec, cfg, out_file)
                    item_path = args.stac_dir / (item["id"] + ".json")
                    write_json(item_path, item)
                    stac_paths.append(str(item_path))
        except Exception as e:
            failures += 1
            print(f"[FAIL] {rec.download_url} → {out_file.name}: {e}", file=sys.stderr)

    # README index
    header = [
        "# USGS TopoView — Download Index",
        f"retrieved: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        f"viewer: {cfg.viewer or ''}",
        f"bbox: {cfg.bbox}, years: {cfg.min_year}-{cfg.max_year}, formats: {cfg.formats}",
        "",
        "URL\tFILE\tYEAR\tSCALE"
    ]
    Path(cfg.readme).write_text("\n".join(header + lines) + "\n", encoding="utf-8")

    # Update simple provenance back into the source file
    src_obj = read_json(args.source)
    prov = src_obj.get("provenance", {})
    prov["retrieved"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    src_obj["provenance"] = prov
    write_json(args.source, src_obj)

    # Manifest
    summary = Summary(
        total_products=total,
        downloaded=downloaded,
        skipped=skipped,
        failures=failures,
        elapsed_s=time.time() - t0
    )
    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": asdict(summary),
        "source": str(args.source),
        "out_dir": str(cfg.out_dir),
        "readme": str(cfg.readme),
        "stac_dir": str(args.stac_dir) if args.stac_dir else None,
        "stac_items": stac_paths,
        "environment": {
            "requests": requests.__version__,
            "tqdm": HAS_TQDM,
        }
    }
    write_json(args.manifest, manifest)

    print(f"[RESULT] total={total}  downloaded={downloaded}  skipped={skipped}  fail={failures}  wrote {cfg.readme}")
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
