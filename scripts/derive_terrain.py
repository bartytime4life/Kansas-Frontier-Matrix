#!/usr/bin/env python3
"""
Derive hillshade/slope/aspect from DEM COGs.
"""
from __future__ import annotations
import argparse, pathlib, subprocess

def run(cmd):
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)

def process_dem(dem: pathlib.Path, outdir: pathlib.Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    base = dem.stem
    # hillshade (gdaldem)
    run(["gdaldem", "hillshade", str(dem), str(outdir / f"{base}_hillshade.tif"), "-compute_edges"])
    # slope
    run(["gdaldem", "slope", str(dem), str(outdir / f"{base}_slope.tif"), "-compute_edges", "-s", "1.0"])
    # aspect
    run(["gdaldem", "aspect", str(dem), str(outdir / f"{base}_aspect.tif"), "-compute_edges"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dem", required=True, help="Folder of DEM COGs")
    ap.add_argument("--out", required=True, help="Output folder for derivatives")
    args = ap.parse_args()
    dem_dir = pathlib.Path(args.dem)
    out = pathlib.Path(args.out)
    for tif in dem_dir.glob("*.tif"):
        process_dem(tif, out)
if __name__ == "__main__":
    main()
