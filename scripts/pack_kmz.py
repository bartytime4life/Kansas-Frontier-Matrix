#!/usr/bin/env python3
"""
No-op helper retained for symmetry; regionate_kml already writes KMZ.
This could later optimize images (jpeg/png) and embed region LOD trees.
"""
from __future__ import annotations
import argparse, pathlib

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kml", required=True, help="KML dir (ignored for now)")
    ap.add_argument("--out", required=True, help="Output dir")
    args = ap.parse_args()
    print("[INFO] pack_kmz: nothing to do (KMZ already built).")

if __name__ == "__main__":
    main()
