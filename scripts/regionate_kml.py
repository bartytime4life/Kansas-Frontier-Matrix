#!/usr/bin/env python3
# scripts/regionate_kml.py
"""
Regionation-aware KMZ GroundOverlay packer

What it does
------------
• Wraps one or more *georeferenced* rasters as KML GroundOverlays inside a KMZ.
• Computes LatLonBox by transforming dataset bounds to WGS84 (EPSG:4326).
• Adds optional <Region><Lod> to each overlay for lightweight *regionation*
  (Google Earth only requests tiles when their on-screen size exceeds minLodPixels).
• Fails fast when CRS/bounds are missing (or accept --bounds fallback).
• No tiling/resampling — one overlay per input file (ideal when inputs are already tiles/COGs).
• No external deps beyond: rasterio, pyproj (as in your original design).

Typical uses
------------
- You have a directory of COG tiles for a large map and want a doc.kml (or KMZ) that
  regionates visibility with Lod thresholds.
- For very large areas / performance, generate tiles externally, then run this tool.

Examples
--------
# Pack all COGs in a folder (recursive), regionation with minLodPixels=128
python scripts/regionate_kml.py --inp data/cogs/hillshade --recursive --pattern "*.tif" \
       --out earth --kmz Kansas_Terrain.kmz --min-lod 128

# Explicit list (mixed tif/png/jpg accepted)
python scripts/regionate_kml.py --files data/cogs/o_01.tif data/cogs/o_02.tif \
       --out earth --kmz overlays.kmz

# Single image without CRS — use explicit bounds (N S E W)
python scripts/regionate_kml.py --files img.tif --bounds 40.0 36.99 -94.59 -102.05 \
       --out earth --kmz fallback.kmz

Notes
-----
- This does NOT change pixel data nor reproject imagery. It only reads metadata to
  compute the GroundOverlay's LatLonBox and optional Region/Lod.
- If you need quadtree tiling or dynamic network links, keep using your external tiler
  and then call this on each output level/folder — the added Lod still helps culling.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple
from xml.sax.saxutils import escape

import rasterio
from pyproj import CRS, Transformer

VALID_EXT = {".tif", ".tiff", ".png", ".jpg", ".jpeg"}

KML_DOC_TPL = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <name>{title}</name>
  {overlays}
</Document>
</kml>
""".strip()

# Regionation-aware GroundOverlay (Region+Lod are optional)
KML_OVL_TPL = """
<GroundOverlay>
  <name>{name}</name>
  <Icon><href>{href}</href></Icon>
  <LatLonBox>
    <north>{north}</north>
    <south>{south}</south>
    <east>{east}</east>
    <west>{west}</west>
    {rotation}
  </LatLonBox>
  {region}
</GroundOverlay>
""".strip()

KML_REGION_TPL = """
<Region>
  <LatLonAltBox>
    <north>{north}</north>
    <south>{south}</south>
    <east>{east}</east>
    <west>{west}</west>
  </LatLonAltBox>
  <Lod>
    <minLodPixels>{min_lod}</minLodPixels>
    <maxLodPixels>{max_lod}</maxLodPixels>
  </Lod>
</Region>
""".strip()


# -----------------------------------------------------------------------------
# Data structures
# -----------------------------------------------------------------------------

@dataclass
class Overlay:
    src: Path
    north: float
    south: float
    east: float
    west: float


# -----------------------------------------------------------------------------
# Utils
# -----------------------------------------------------------------------------

def _sha256(p: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def _find_files(roots: Iterable[Path], pattern: str, recursive: bool) -> Iterable[Path]:
    for root in roots:
        if root.is_file():
            if root.suffix.lower() in VALID_EXT:
                yield root
            continue
        if not root.exists():
            continue
        it = root.rglob(pattern) if recursive else root.glob(pattern)
        for p in it:
            if p.suffix.lower() in VALID_EXT and p.is_file():
                yield p


def _ds_bounds_wgs84(ds: rasterio.io.DatasetReader) -> Tuple[float, float, float, float]:
    """Return (north, south, east, west) in EPSG:4326 from dataset bounds."""
    if ds.bounds is None:
        raise ValueError("dataset has no bounds")
    if ds.crs is None:
        raise ValueError("dataset has no CRS; cannot compute WGS84 bounds")

    src_crs = CRS.from_wkt(ds.crs.to_wkt()) if not isinstance(ds.crs, CRS) else ds.crs
    dst_crs = CRS.from_epsg(4326)
    tr = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

    left, bottom, right, top = ds.bounds
    xs = [left, right, right, left]
    ys = [bottom, bottom, top, top]
    lon, lat = tr.transform(xs, ys)

    north = min(90.0, max(lat))
    south = max(-90.0, min(lat))
    east = min(180.0, max(lon))
    west = max(-180.0, min(lon))

    if not (south < north and west < east):
        raise ValueError(f"invalid transformed bounds: N{north} S{south} E{east} W{west}")
    return north, south, east, west


def overlay_from_raster(path: Path, forced_bounds: Optional[Tuple[float, float, float, float]]) -> Overlay:
    if forced_bounds:
        n, s, e, w = forced_bounds
        return Overlay(src=path, north=n, south=s, east=e, west=w)
    with rasterio.open(path) as ds:
        n, s, e, w = _ds_bounds_wgs84(ds)
        return Overlay(src=path, north=n, south=s, east=e, west=w)


# -----------------------------------------------------------------------------
# KML assembly
# -----------------------------------------------------------------------------

def _region_xml(n: float, s: float, e: float, w: float, min_lod: Optional[int], max_lod: Optional[int]) -> str:
    if min_lod is None and max_lod is None:
        return ""  # no Region/Lod
    # Google Earth defaults: maxLodPixels=-1 means "no upper limit"
    minp = 0 if min_lod is None else int(min_lod)
    maxp = -1 if max_lod is None else int(max_lod)
    return KML_REGION_TPL.format(north=f"{n:.10f}", south=f"{s:.10f}",
                                 east=f"{e:.10f}", west=f"{w:.10f}",
                                 min_lod=minp, max_lod=maxp)


def _overlay_xml(ov: Overlay, href: str, *, rotation: Optional[float],
                 min_lod: Optional[int], max_lod: Optional[int]) -> str:
    rot_xml = f"<rotation>{rotation:.6f}</rotation>" if rotation not in (None, 0.0) else ""
    region = _region_xml(ov.north, ov.south, ov.east, ov.west, min_lod, max_lod)
    return KML_OVL_TPL.format(
        name=escape(ov.src.stem),
        href=escape(href),
        north=f"{ov.north:.10f}",
        south=f"{ov.south:.10f}",
        east=f"{ov.east:.10f}",
        west=f"{ov.west:.10f}",
        rotation=rot_xml,
        region=region,
    )


def build_kmz(
    overlays: Sequence[Overlay],
    out_dir: Path,
    kmz_name: str,
    *,
    title: Optional[str],
    prefix: str,
    min_lod: Optional[int],
    max_lod: Optional[int],
    rotation: Optional[float],
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    kmz_name = kmz_name if kmz_name.lower().endswith(".kmz") else f"{kmz_name}.kmz"
    kmz_path = out_dir / kmz_name

    parts: List[str] = []
    assets: List[Path] = []
    for ov in overlays:
        href = f"{prefix}/{ov.src.name}"
        parts.append(_overlay_xml(ov, href, rotation=rotation, min_lod=min_lod, max_lod=max_lod))
        assets.append(ov.src)

    kml = KML_DOC_TPL.format(title=escape(title or kmz_name), overlays="\n  ".join(parts))
    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("doc.kml", kml)
        for a in assets:
            z.write(a, arcname=f"{prefix}/{a.name}")

    # Sidecars
    (kmz_path.with_suffix(kmz_path.suffix + ".sha256")).write_text(_sha256(kmz_path) + "\n", encoding="utf-8")
    meta = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kmz": kmz_path.name,
        "size": kmz_path.stat().st_size,
        "assets": [a.name for a in assets],
        "argv": sys.argv,
    }
    (kmz_path.with_suffix(".meta.json")).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return kmz_path


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Wrap georeferenced rasters as regionation-aware GroundOverlays into a KMZ."
    )
    g_in = p.add_mutually_exclusive_group(required=True)
    g_in.add_argument("--inp", type=Path, help="Directory to scan for rasters")
    g_in.add_argument("--files", nargs="+", type=Path, help="Explicit list of raster files")

    p.add_argument("--pattern", default="*.tif", help='Glob pattern for --inp (default: "*.tif")')
    p.add_argument("--recursive", action="store_true", help="Recurse when scanning --inp")

    p.add_argument(
        "--bounds", nargs=4, type=float, metavar=("NORTH", "SOUTH", "EAST", "WEST"),
        help="Explicit WGS84 bounds for ALL inputs (only when rasters lack CRS)"
    )
    p.add_argument("--out", type=Path, required=True, help="Output directory")
    p.add_argument("--kmz", default="overlays.kmz", help="Output KMZ filename")
    p.add_argument("--title", default=None, help="KML <Document><name> (defaults to KMZ name)")
    p.add_argument("--prefix", default="files", help="Asset subfolder inside KMZ (default: files)")

    # Regionation / Lod
    p.add_argument("--min-lod", type=int, default=None,
                   help="Region/Lod minLodPixels (e.g., 64, 128). If unset, no Region is written.")
    p.add_argument("--max-lod", type=int, default=None,
                   help="Region/Lod maxLodPixels (set -1 for unlimited). If unset and --min-lod set, defaults to -1.")
    p.add_argument("--rotation", type=float, default=None, help="Optional LatLonBox rotation (degrees)")

    p.add_argument("-v", "--verbose", action="count", default=0, help="Increase logging verbosity")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=logging.WARNING - (10 * min(args.verbose, 2)),
        format="%(levelname)s: %(message)s",
    )

    # Collect inputs
    if args.files:
        files = [Path(f) for f in args.files if Path(f).exists()]
    else:
        root = args.inp
        if not root.exists():
            logging.error("Input path does not exist: %s", root)
            return 2
        files = list(_find_files([root], pattern=args.pattern, recursive=bool(args.recursive)))

    if not files:
        logging.error("No input rasters found.")
        return 2

    # Bounds fallback (for ALL inputs)
    forced_bounds: Optional[Tuple[float, float, float, float]] = None
    if args.bounds:
        n, s, e, w = args.bounds
        if not (s < n and w < e):
            logging.error("Invalid --bounds ordering: expected NORTH>SOUTH and EAST>WEST.")
            return 2
        forced_bounds = (n, s, e, w)

    # Prepare overlays
    overlays: List[Overlay] = []
    skipped = 0
    for f in files:
        try:
            ov = overlay_from_raster(f, forced_bounds)
            overlays.append(ov)
            logging.info("Prepared overlay: %s", f.name)
        except Exception as ex:
            logging.warning("Skipping %s: %s", f, ex)
            skipped += 1

    if not overlays:
        logging.error("No valid overlays prepared (all inputs failed).")
        return 2

    # Build KMZ
    kmz_path = build_kmz(
        overlays,
        args.out,
        args.kmz,
        title=args.title,
        prefix=args.prefix,
        min_lod=args.min_lod,
        max_lod=args.max_lod if args.max_lod is not None else (-1 if args.min_lod is not None else None),
        rotation=args.rotation,
    )
    print(f"[OK] KMZ → {kmz_path} (overlays: {len(overlays)})")
    if skipped:
        print(f"[WARN] {skipped} file(s) were skipped due to errors.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
