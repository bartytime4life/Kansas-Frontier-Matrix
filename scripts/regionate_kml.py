#!/usr/bin/env python3
"""
Prototype KML packer: wraps one or more rasters as GroundOverlays in a KMZ.

This is a lightweight stand-in for full quadtree regionation; good enough for
quick Earth previews. For large areas, split rasters and extend this to add
<Region>/<Lod> elements per tile.
"""
from __future__ import annotations
import argparse, pathlib, zipfile
from xml.sax.saxutils import escape

KML_TPL = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
  <name>{title}</name>
  {overlays}
</Document>
</kml>
"""

OVL = """
<GroundOverlay>
  <name>{name}</name>
  <Icon><href>{href}</href></Icon>
  <LatLonBox>
    <north>{north}</north><south>{south}</south>
    <east>{east}</east><west>{west}</west>
  </LatLonBox>
</GroundOverlay>
"""

def make_kmz(inp: pathlib.Path, outdir: pathlib.Path, kmz_name: str):
    # Expect worldfile + bounds via gdal (tfw + .aux.xml) — for prototype, ask user
    # We will just embed the raster without georeferencing if bounds.json exists.
    overlays_xml = ""
    assets = []
    for tif in inp.glob("*.tif"):
        # try bounds file
        bnd = tif.with_suffix(".bounds.json")
        if bnd.exists():
            import json
            b = json.loads(bnd.read_text())
            north, south, east, west = b["north"], b["south"], b["east"], b["west"]
        else:
            # fallback to Kansas bbox (user should provide .bounds.json)
            north, south, east, west = 40.0, 36.99, -94.59, -102.05
        href = f"files/{tif.name}"
        overlays_xml += OVL.format(name=escape(tif.stem), href=href,
                                   north=north, south=south, east=east, west=west)
        assets.append(tif)
    kml = KML_TPL.format(title=escape(kmz_name), overlays=overlays_xml)
    outdir.mkdir(parents=True, exist_ok=True)
    kmz_path = outdir / kmz_name
    with zipfile.ZipFile(kmz_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("doc.kml", kml)
        for a in assets:
            z.write(a, arcname=f"files/{a.name}")
    print(f"[OK] KMZ → {kmz_path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--kmz", default="kansas_elevation.kmz")
    args = ap.parse_args()
    make_kmz(pathlib.Path(args.inp), pathlib.Path(args.out), args.kmz)

if __name__ == "__main__":
    main()
