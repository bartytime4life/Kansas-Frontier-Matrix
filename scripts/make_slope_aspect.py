#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_slope_aspect.py — Build slope and/or aspect COG(s) from DEMs using GDAL.

Examples
--------
# Single DEM → derivatives/<name>_{slope,aspect}.tif
python scripts/make_slope_aspect.py data/.../pawnee_1m_dem_cog.tif --slope --aspect --validate

# Batch over a folder
python scripts/make_slope_aspect.py data/sources/dem/processed/lidar --pattern "*_dem_cog.tif" --slope --jobs 8
"""
from __future__ import annotations

import argparse, shutil, subprocess, sys, os
from pathlib import Path
from typing import List, Optional

HERE = Path(__file__).resolve().parent
GDALDEM = shutil.which("gdaldem")
GDALINFO = shutil.which("gdalinfo")

def sh(cmd: List[str], **kwargs) -> None:
    kwargs.setdefault("check", True)
    kwargs.setdefault("text", True)
    print("➜", " ".join(map(str, cmd)))
    subprocess.run(cmd, **kwargs)

def atomic_parent(p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)

def list_inputs(src: Path, pattern: str) -> List[Path]:
    if src.is_file():
        return [src]
    return sorted([p for p in src.rglob(pattern) if p.is_file()])

def base_name(src: Path) -> str:
    name = src.stem
    for suf in ("_dem_cog", "_dem", "_cog"):
        if name.endswith(suf):
            name = name[: -len(suf)]
            break
    return name

def out_path(src: Path, out_root: Optional[Path], kind: str) -> Path:
    return (out_root or src.parent / "derivatives") / f"{base_name(src)}_{kind}.tif"

def quick_info(p: Path) -> None:
    if not GDALINFO:
        return
    try:
        out = subprocess.check_output([GDALINFO, "-stats", str(p)], text=True)
        print("\n".join(out.splitlines()[:25]))
    except Exception:
        pass

def try_validate(p: Path) -> None:
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

def build_slope(
    dem: Path, out: Path, *, scale: float, z: float, percent: bool,
    compute_edges: bool, alg: str, threads: str, ovr_resampling: str, dry: bool
) -> None:
    if not GDALDEM:
        raise RuntimeError("gdaldem not found in PATH")
    atomic_parent(out)
    args = [
        GDALDEM, "slope", str(dem), str(out),
        "-of", "COG",
        "-s", str(scale),
        "-z", str(z),
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=2",
        "-co", "ZLEVEL=6",
        "-co", "BLOCKSIZE=512",
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
        "-co", f"OVERVIEW_RESAMPLING={ovr_resampling}",
        "-co", "BIGTIFF=IF_SAFER",
    ]
    if percent:
        args.append("-p")  # slope in percent
    if compute_edges:
        args.append("-compute_edges")
    if alg:
        args += ["-alg", alg]  # e.g., ZevenbergenThorne (if supported)
    if dry:
        print("➜ (dry-run)", " ".join(args)); return
    sh(args)

def build_aspect(
    dem: Path, out: Path, *, trigonometric: bool, zero_for_flat: bool,
    compute_edges: bool, threads: str, ovr_resampling: str, dry: bool
) -> None:
    if not GDALDEM:
        raise RuntimeError("gdaldem not found in PATH")
    atomic_parent(out)
    args = [
        GDALDEM, "aspect", str(dem), str(out),
        "-of", "COG",
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=2",
        "-co", "ZLEVEL=6",
        "-co", "BLOCKSIZE=512",
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
        "-co", f"OVERVIEW_RESAMPLING={ovr_resampling}",
        "-co", "BIGTIFF=IF_SAFER",
    ]
    if trigonometric:
        args.append("-trigonometric")  # 0° East, CCW; else 0° North, CW (GDAL default)
    if zero_for_flat:
        args.append("-zero_for_flat")
    if compute_edges:
        args.append("-compute_edges")
    if dry:
        print("➜ (dry-run)", " ".join(args)); return
    sh(args)

def main() -> int:
    ap = argparse.ArgumentParser(description="Create slope/aspect COG(s) from DEM(s).")
    ap.add_argument("src", type=Path, help="DEM file or directory")
    ap.add_argument("--pattern", default="*.tif", help="Glob when src is a directory")
    ap.add_argument("--out-root", type=Path, help="Output root (default <dem_dir>/derivatives)")
    ap.add_argument("--slope", action="store_true", help="Compute slope")
    ap.add_argument("--aspect", action="store_true", help="Compute aspect")
    ap.add_argument("--scale", type=float, default=1.0, help="Ground units per pixel (1=m; ~111120 for degrees)")
    ap.add_argument("--z", type=float, default=1.0, help="Z-factor for slope")
    ap.add_argument("--percent", action="store_true", help="Slope in percent instead of degrees")
    ap.add_argument("--compute-edges", action="store_true", help="Use -compute_edges (both ops)")
    ap.add_argument("--alg", default="", help="Slope algorithm (e.g., ZevenbergenThorne; if supported)")
    ap.add_argument("--trigonometric", action="store_true", help="Aspect: 0°=East, CCW")
    ap.add_argument("--zero-for-flat", action="store_true", help="Aspect: output 0 for flat areas")
    ap.add_argument("--threads", default="ALL_CPUS", help='NUM_THREADS for COG creation')
    ap.add_argument("--ovr-resampling", default="AVERAGE",
                    choices=["NEAREST","AVERAGE","GAUSS","CUBIC","CUBICSPLINE","LANCZOS","MODE","RMS","BILINEAR","MIN","MAX","MED"],
                    help="Overview resampling")
    ap.add_argument("--validate", action="store_true", help="Validate outputs as COGs (best-effort)")
    ap.add_argument("--dry-run", action="store_true", help="Plan only; no writes")
    args = ap.parse_args()

    if not (args.slope or args.aspect):
        args.slope = True  # sensible default

    inputs = list_inputs(args.src, args.pattern)
    if not inputs:
        print(f"[ERR] no inputs found: {args.src} ({args.pattern})", file=sys.stderr)
        return 2

    failures = 0
    for dem in inputs:
        if args.slope:
            out = out_path(dem, args.out_root, "slope")
            try:
                build_slope(
                    dem, out, scale=args.scale, z=args.z, percent=args.percent,
                    compute_edges=args.compute_edges, alg=args.alg,
                    threads=args.threads, ovr_resampling=args.ovr_resampling, dry=args.dry_run
                )
                if not args.dry_run:
                    quick_info(out)
                    if args.validate: try_validate(out)
                    try_meta(out, dem, stage="slope", scale=args.scale, z=args.z, percent=str(args.percent).lower(), alg=args.alg or "default")
                print(f"[OK] slope → {out}")
            except Exception as e:
                failures += 1
                print(f"[FAIL] slope {dem.name}: {e}", file=sys.stderr)

        if args.aspect:
            out = out_path(dem, args.out_root, "aspect")
            try:
                build_aspect(
                    dem, out, trigonometric=args.trigonometric, zero_for_flat=args.zero_for_flat,
                    compute_edges=args.compute_edges, threads=args.threads, ovr_resampling=args.ovr_resampling, dry=args.dry_run
                )
                if not args.dry_run:
                    quick_info(out)
                    if args.validate: try_validate(out)
                    try_meta(out, dem, stage="aspect", trigonometric=str(args.trigonometric).lower(), zero_for_flat=str(args.zero_for_flat).lower())
                print(f"[OK] aspect → {out}")
            except Exception as e:
                failures += 1
                print(f"[FAIL] aspect {dem.name}: {e}", file=sys.stderr)

    if failures:
        print(f"\n[WARN] {failures} job(s) failed", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
