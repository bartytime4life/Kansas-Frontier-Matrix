#!/usr/bin/env python3
"""
KMZ GroundOverlay packer (robust edition)

- Wraps one or more *georeferenced* rasters as KML GroundOverlays inside a KMZ.
- Computes LatLonBox from the raster's native CRS → WGS84 (EPSG:4326).
- No hard-coded fallbacks; if a raster lacks CRS/bounds, fail fast (or accept --bounds).
- Lightweight stand-in for full quadtree regionation (one overlay per input file).
  For large areas or performance, tile externally and call this on each tile set.

Requirements:
  - rasterio (reads geotransform/CRS)
  - pyproj (CRS transform)

Examples:
  python scripts/pack_kmz.py --inp data/cogs/hillshade --pattern "*.tif" \
         --out earth --kmz Kansas_Terrain.kmz

  python scripts/pack_kmz.py --files data/cogs/overlays/usgs_1894_larned.tif \
         --out earth --kmz usgs_larned_1894.kmz

  # If a single image truly has no CRS, pass explicit bounds (N S E W):
  python scripts/pack_kmz.py --files img.tif --bounds 40.0 36.99 -94.59 -102.05 \
         --out earth --kmz fallback.kmz
"""
from __future__ import annotations

import argparse
import logging
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Tuple
from xml.sax.saxutils import escape

import rasterio
from pyproj import CRS, Transformer

KML_TPL = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <name>{title}</name>
  {overlays}
</Document>
</kml>
""".strip()

OVL_TPL = """
<GroundOverlay>
  <name>{name}</name>
  <Icon><href>{href}</href></Icon>
  <LatLonBox>
    <north>{north}</north><south>{south}</south>
    <east>{east}</east><west>{west}</west>
  </LatLonBox>
</GroundOverlay>
""".strip()

VALID_EXT = {".tif", ".tiff", ".png", ".jpg", ".jpeg"}


@dataclass
class Overlay:
    src_path: Path
    north: float
    south: float
    east: float
    west: float


def _find_files(
    roots: Iterable[Path], pattern: str, recursive: bool
) -> Iterable[Path]:
    for root in roots:
        if root.is_file():
            if root.suffix.lower() in VALID_EXT:
                yield root
            continue
        if recursive:
            yield from (p for p in root.rglob(pattern) if p.suffix.lower() in VALID_EXT)
        else:
            yield from (p for p in root.glob(pattern) if p.suffix.lower() in VALID_EXT)


def _bounds_to_wgs84(ds: rasterio.io.DatasetReader) -> Tuple[float, float, float, float]:
    """
    Return (north, south, east, west) in EPSG:4326 by transforming dataset corner coords.
    """
    if ds.bounds is None:
        raise ValueError("Dataset has no meaningful bounds")
    if ds.crs is None:
        raise ValueError("Dataset has no CRS; cannot compute LatLonBox")

    src_crs = CRS.from_wkt(ds.crs.to_wkt()) if not isinstance(ds.crs, CRS) else ds.crs
    dst_crs = CRS.from_epsg(4326)
    transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

    # dataset.bounds: left, bottom, right, top in source CRS
    left, bottom, right, top = ds.bounds
    # Transform the 4 corners
    xs = [left, right, right, left]
    ys = [bottom, bottom, top, top]
    lon, lat = transformer.transform(xs, ys)

    north = max(lat)
    south = min(lat)
    east = max(lon)
    west = min(lon)

    # Clamp to valid WGS84 ranges just in case
    north = min(north, 90.0)
    south = max(south, -90.0)
    east = min(east, 180.0)
    west = max(west, -180.0)

    if south >= north or west >= east:
        raise ValueError(
            f"Transformed bounds invalid: N{north} S{south} E{east} W{west}"
        )
    return north, south, east, west


def _overlay_from_raster(path: Path, forced_bounds: Optional[Tuple[float, float, float, float]] = None) -> Overlay:
    if forced_bounds:
        n, s, e, w = forced_bounds
        return Overlay(src_path=path, north=n, south=s, east=e, west=w)

    with rasterio.open(path) as ds:
        n, s, e, w = _bounds_to_wgs84(ds)
        return Overlay(src_path=path, north=n, south=s, east=e, west=w)


def build_kmz(
    overlays: Iterable[Overlay],
    out_dir: Path,
    kmz_name: str,
    kml_title: Optional[str] = None,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    kmz_name = kmz_name if kmz_name.lower().endswith(".kmz") else f"{kmz_name}.kmz"
    kmz_path = out_dir / kmz_name

    overlays_xml_parts = []
    assets: list[Path] = []
    for ov in overlays:
        href = f"files/{ov.src_path.name}"
        overlays_xml_parts.append(
            OVL_TPL.format(
                name=escape(ov.src_path.stem),
                href=escape(href),
                north=f"{ov.north:.10f}",
                south=f"{ov.south:.10f}",
                east=f"{ov.east:.10f}",
                west=f"{ov.west:.10f}",
            )
        )
        assets.append(ov.src_path)

    kml = KML_TPL.format(
        title=escape(kml_title or kmz_name), overlays="\n  ".join(overlays_xml_parts)
    )

    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("doc.kml", kml)
        for a in assets:
            z.write(a, arcname=f"files/{a.name}")

    return kmz_path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pack georeferenced rasters as GroundOverlays into a KMZ."
    )
    g_in = p.add_mutually_exclusive_group(required=True)
    g_in.add_argument("--inp", type=Path, help="Directory to scan for rasters")
    g_in.add_argument(
        "--files", nargs="+", type=Path, help="Explicit list of raster files"
    )

    p.add_argument(
        "--pattern",
        default="*.tif",
        help='Glob pattern when using --inp (default: "*.tif")',
    )
    p.add_argument(
        "--recursive", action="store_true", help="Recurse when scanning --inp"
    )

    p.add_argument(
        "--bounds",
        nargs=4,
        type=float,
        metavar=("NORTH", "SOUTH", "EAST", "WEST"),
        help="Explicit WGS84 bounds (applied to ALL inputs; use only when rasters lack CRS)",
    )
    p.add_argument("--out", type=Path, required=True, help="Output directory")
    p.add_argument("--kmz", default="overlays.kmz", help="Output KMZ filename")
    p.add_argument(
        "--title",
        default=None,
        help="KML <Document><name>; defaults to KMZ name",
    )
    p.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase log verbosity"
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=logging.WARNING - (10 * min(args.verbose, 2)),
        format="%(levelname)s: %(message)s",
    )

    # Collect inputs
    if args.files:
        files = [f for f in (Path(f) for f in args.files) if f.exists()]
    else:
        if not args.inp.exists():
            logging.error("Input path does not exist: %s", args.inp)
            return 2
        files = list(_find_files([args.inp], pattern=args.pattern, recursive=bool(args.recursive)))

    if not files:
        logging.error("No input rasters found.")
        return 2

    forced_bounds: Optional[Tuple[float, float, float, float]] = None
    if args.bounds:
        n, s, e, w = args.bounds
        if not (s < n and w < e):
            logging.error("Invalid --bounds ordering: expected NORTH>SOUTH and EAST>WEST.")
            return 2
        forced_bounds = (n, s, e, w)

    overlays: list[Overlay] = []
    errors = 0
    for f in files:
        try:
            overlays.append(_overlay_from_raster(f, forced_bounds=forced_bounds))
            logging.info("Prepared overlay: %s", f.name)
        except Exception as ex:
            errors += 1
            logging.warning("Skipping %s: %s", f, ex)

    if not overlays:
        logging.error("No valid overlays prepared (all inputs failed).")
        return 2

    kmz_path = build_kmz(overlays, args.out, args.kmz, kml_title=args.title)
    print(f"[OK] KMZ → {kmz_path}")
    if errors:
        print(f"[WARN] {errors} file(s) were skipped due to errors.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
