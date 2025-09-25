#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_terrain_pack.py — Build hillshade + slope + aspect COG(s) from DEM(s).
Delegates to sibling scripts to keep behavior consistent.
"""
from __future__ import annotations

import argparse, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def run(cmd):
    print("➜", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True, text=True)

def main() -> int:
    ap = argparse.ArgumentParser(description="Create terrain pack (hillshade, slope, aspect) from DEM(s).")
    ap.add_argument("src", type=Path, help="DEM file or directory")
    ap.add_argument("--pattern", default="*.tif", help="Glob when src is a directory")
    ap.add_argument("--out-root", type=Path, help="Output root (defaults to <dem_dir>/derivatives)")
    # Hillshade
    ap.add_argument("--az", type=float, default=315.0)
    ap.add_argument("--alt", type=float, default=45.0)
    ap.add_argument("--hz", dest="z_hs", type=float, default=1.0, help="Z-factor for hillshade")
    ap.add_argument("--scale", type=float, default=1.0, help="Ground units per pixel (DEM units)")
    ap.add_argument("--multidir", action="store_true")
    ap.add_argument("--compute-edges", action="store_true")
    # Slope/Aspect
    ap.add_argument("--z", type=float, default=1.0, help="Z-factor for slope")
    ap.add_argument("--percent", action="store_true", help="Slope in percent (not degrees)")
    ap.add_argument("--alg", default="", help="Slope algorithm (e.g., ZevenbergenThorne)")
    ap.add_argument("--trigonometric", action="store_true", help="Aspect trigonometric")
    ap.add_argument("--zero-for-flat", action="store_true", help="Aspect zero_for_flat")
    # Common COG opts
    ap.add_argument("--threads", default="ALL_CPUS")
    ap.add_argument("--ovr-resampling", default="AVERAGE",
                    choices=["NEAREST","AVERAGE","GAUSS","CUBIC","CUBICSPLINE","LANCZOS","MODE","RMS","BILINEAR","MIN","MAX","MED"])
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # Hillshade
    run([
        sys.executable, str(HERE / "make_hillshade.py"), str(args.src),
        "--pattern", args.pattern,
        "--ovr-resampling", args.ovr_resampling,
        "--threads", args.threads,
        "--az", str(args.az), "--alt", str(args.alt), "--z", str(args.z_hs),
        "--scale", str(args.scale),
        *(["--multidir"] if args.multidir else []),
        *(["--compute-edges"] if args.compute_edges else []),
        *(["--validate"] if args.validate else []),
        *(["--dry-run"] if args.dry-run else []),
        *(["--out-root", str(args.out_root)] if args.out_root else []),
    ])

    # Slope + Aspect
    run([
        sys.executable, str(HERE / "make_slope_aspect.py"), str(args.src),
        "--pattern", args.pattern,
        "--ovr-resampling", args.ovr_resampling,
        "--threads", args.threads,
        "--scale", str(args.scale),
        "--z", str(args.z),
        *(["--percent"] if args.percent else []),
        *(["--alg", args.alg] if args.alg else []),
        *(["--compute-edges"] if args.compute_edges else []),
        *(["--trigonometric"] if args.trigonometric else []),
        *(["--zero-for-flat"] if args.zero_for_flat else []),
        "--slope", "--aspect",
        *(["--validate"] if args.validate else []),
        *(["--dry-run"] if args.dry-run else []),
        *(["--out-root", str(args.out_root)] if args.out_root else []),
    ])

    print("[OK] terrain pack complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())
