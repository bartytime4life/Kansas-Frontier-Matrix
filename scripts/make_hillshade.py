#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_hillshade.py — Build hillshade COG(s) from DEMs using GDAL.

Features
--------
- Single file OR batch over a directory (glob pattern)
- Uses `gdaldem hillshade` → COG directly (fast, internal overviews)
- Tunables: azimuth, altitude, z-factor, scale, multi-directional, edges
- Threaded COG build (NUM_THREADS), overview resampling control
- Safe output naming & folders (derivatives/)
- Optional: validate with rio-cogeo/gdalinfo, write meta sidecars

Examples
--------
# Single DEM → hillshade COG next to it (derivatives/<name>_hillshade.tif)
python scripts/make_hillshade.py data/sources/dem/processed/lidar/pawnee/pawnee_1m_dem_cog.tif

# Batch: all county DEMs under folder
python scripts/make_hillshade.py data/sources/dem/processed/lidar --pattern "*_dem_cog.tif" --jobs 8 --validate

# Custom lighting + z-factor (meters DEM, geographic CRS)
python scripts/make_hillshade.py dem.tif --az 315 --alt 45 --z 1.0 --scale 111120

Notes
-----
- `--scale` is ground units per pixel: 1 for projected meters; ~111120 for degrees.
- `--multidir` yields nicer relief in many cases (slightly heavier compute).
- Requires: gdaldem (and gdal_translate for some fallbacks). Validation is optional.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

HERE = Path(__file__).resolve().parent

GDALDEM = shutil.which("gdaldem")
GDALINFO = shutil.which("gdalinfo")

def sh(cmd: List[str], **kwargs) -> None:
    kwargs.setdefault("check", True)
    kwargs.setdefault("text", True)
    print("➜", " ".join(map(str, cmd)))
    subprocess.run(cmd, **kwargs)

def atomic_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def default_out_path(src: Path, out_root: Optional[Path]) -> Path:
    name = src.stem
    # strip common DEM suffixes
    for suf in ("_dem_cog", "_dem", "_cog"):
        if name.endswith(suf):
            name = name[: -len(suf)]
            break
    base = (out_root or src.parent / "derivatives")
    return base / f"{name}_hillshade.tif"

def list_inputs(src: Path, pattern: str) -> List[Path]:
    if src.is_file():
        return [src]
    return sorted([p for p in src.rglob(pattern) if p.is_file()])

def build_hillshade(
    dem: Path,
    out: Path,
    *,
    az: float,
    alt: float,
    z: float,
    scale: float,
    compute_edges: bool,
    multidir: bool,
    threads: str,
    ovr_resampling: str,
    dry: bool,
) -> None:
    if not GDALDEM:
        raise RuntimeError("gdaldem not found in PATH")

    atomic_parent(out)
    args = [
        GDALDEM, "hillshade", str(dem), str(out),
        "-of", "COG",
        "-az", str(az),
        "-alt", str(alt),
        "-z", str(z),
        "-s", str(scale),
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=2",
        "-co", "ZLEVEL=6",
        "-co", "BLOCKSIZE=512",
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
        "-co", f"OVERVIEW_RESAMPLING={ovr_resampling}",
        "-co", "BIGTIFF=IF_SAFER",
    ]
    if compute_edges:
        args.append("-compute_edges")
    if multidir:
        args.append("-multidirectional")

    if dry:
        print("➜ (dry-run)", " ".join(args))
        return
    sh(args)

def quick_info(p: Path) -> None:
    if not GDALINFO:
        return
    try:
        out = subprocess.check_output([GDALINFO, "-stats", str(p)], text=True)
        head = "\n".join(out.splitlines()[:25])
        print(head)
    except Exception:
        pass

def try_validate(p: Path) -> None:
    # Best-effort: leverage our upgraded validator if present.
    val = HERE / "validate_cogs.py"
    if val.exists():
        try:
            sh([sys.executable, str(val), str(p.parent), "--pattern", p.name, "--quiet"])
        except Exception as e:
            print(f"[WARN] validation skipped: {e}")

def try_meta(p: Path, dem: Path, **kv) -> None:
    wm = HERE / "write_meta.py"
    if wm.exists():
        try:
            extras = [f"{k}={v}" for k, v in kv.items()]
            sh([sys.executable, str(wm), str(p), "--inputs", str(dem), "--extra", *extras])
        except Exception as e:
            print(f"[WARN] meta sidecars skipped: {e}")

def main() -> int:
    ap = argparse.ArgumentParser(description="Create hillshade COG(s) from DEM(s).")
    ap.add_argument("src", type=Path, help="DEM file or directory")
    ap.add_argument("--pattern", default="*.tif", help="Glob for batch when src is a directory")
    ap.add_argument("--out-root", type=Path, help="Optional output root (defaults to <dem_dir>/derivatives)")
    ap.add_argument("--az", type=float, default=315.0, help="Azimuth (degrees from north)")
    ap.add_argument("--alt", type=float, default=45.0, help="Altitude (sun elevation degrees)")
    ap.add_argument("--z", type=float, default=1.0, help="Z-factor")
    ap.add_argument("--scale", type=float, default=1.0, help="Ground units per pixel (1=m; ~111120 for degrees)")
    ap.add_argument("--compute-edges", action="store_true", help="Use gdaldem -compute_edges")
    ap.add_argument("--multidir", action="store_true", help="Use multidirectional shading")
    ap.add_argument("--threads", default="ALL_CPUS", help='NUM_THREADS for COG creation (e.g., "ALL_CPUS")')
    ap.add_argument("--ovr-resampling", default="AVERAGE",
                    choices=["NEAREST","AVERAGE","GAUSS","CUBIC","CUBICSPLINE","LANCZOS","MODE","RMS","BILINEAR","MIN","MAX","MED"],
                    help="Overview resampling")
    ap.add_argument("--validate", action="store_true", help="Validate outputs as COGs (best-effort)")
    ap.add_argument("--dry-run", action="store_true", help="Plan only; no writes")
    args = ap.parse_args()

    inputs = list_inputs(args.src, args.pattern)
    if not inputs:
        print(f"[ERR] no inputs found: {args.src} ({args.pattern})", file=sys.stderr)
        return 2

    print(f"[INFO] {len(inputs)} input(s)")
    failures = 0
    for dem in inputs:
        out = default_out_path(dem, args.out_root)
        print(f"\n[BUILD] {dem} → {out}")
        try:
            build_hillshade(
                dem, out,
                az=args.az, alt=args.alt, z=args.z, scale=args.scale,
                compute_edges=args.compute_edges, multidir=args.multidir,
                threads=args.threads, ovr_resampling=args.ovr_resampling,
                dry=args.dry_run,
            )
            if not args.dry_run:
                quick_info(out)
                if args.validate:
                    try_validate(out)
                try_meta(out, dem,
                         stage="hillshade",
                         azimuth=args.az, altitude=args.alt, z=args.z,
                         scale=args.scale, multidir=str(args.multidir).lower())
            print(f"[OK] hillshade → {out}")
        except subprocess.CalledProcessError as e:
            failures += 1
            print(f"[FAIL] {dem.name}: {e}", file=sys.stderr)
        except Exception as e:
            failures += 1
            print(f"[FAIL] {dem.name}: {e}", file=sys.stderr)

    if failures:
        print(f"\n[WARN] {failures} job(s) failed", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
