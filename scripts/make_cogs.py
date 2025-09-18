#!/usr/bin/env python3
"""
Convert GeoTIFFs in --inp to Cloud-Optimized GeoTIFFs (COGs) in --out.
"""
from __future__ import annotations
import argparse, pathlib, subprocess, os

def to_cog(src: pathlib.Path, dst: pathlib.Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "gdal_translate",
        "-of", "COG",
        "-co", "COMPRESS=LZW",
        "-co", "BLOCKSIZE=512",
        str(src), str(dst)
    ]
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    inp = pathlib.Path(args.inp)
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for tif in inp.glob("*.tif"):
        to_cog(tif, out / tif.name)

if __name__ == "__main__":
    main()
