#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mosaic_lidar_county.py — Fetch 1m LiDAR tiles for a county, build a VRT, and COG-translate.

Improvements
------------
- CLI args (county OR explicit CSV), dry-run, retries/timeouts, nodata controls
- Parallel/resumable downloads (aria2c if present; otherwise curl with retries)
- Deterministic tile list; skips already-downloaded files; verifies non-empty files
- Robust VRT build (bilinear, optional src/dst nodata), logs VRT stats
- COG translate profile tuned for DEMs (DEFLATE, tiling, predictor, overviews)
- Optional registry + meta sidecars (calls write_meta.py if present)
- Clear exit codes for CI, structured logging

Usage
-----
# Typical (looks for data/sources/dem/tile_indexes/<county>_1m_tiles.csv)
python scripts/mosaic_lidar_county.py --county pawnee

# Explicit CSV + output root
python scripts/mosaic_lidar_county.py --tiles data/sources/dem/tile_indexes/pawnee_1m_tiles.csv \
  --out-root data/sources/dem/processed/lidar/pawnee

# Dry-run (show plan only)
python scripts/mosaic_lidar_county.py --county pawnee --dry-run

# Faster downloads via aria2c if installed
python scripts/mosaic_lidar_county.py --county pawnee --jobs 8
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

CURL = shutil.which("curl")
ARIA2 = shutil.which("aria2c")
GDAL_TRANSLATE = shutil.which("gdal_translate")
GDALBUILDVRT = shutil.which("gdalbuildvrt")
GDALINFO = shutil.which("gdalinfo")

def sh(cmd: list[str], **kwargs) -> None:
    kwargs.setdefault("check", True)
    kwargs.setdefault("text", True)
    print("➜", " ".join(map(str, cmd)))
    subprocess.run(cmd, **kwargs)

def shell_exists() -> Tuple[bool, List[str]]:
    missing = []
    for name, exe in [("curl", CURL), ("gdalbuildvrt", GDALBUILDVRT), ("gdal_translate", GDAL_TRANSLATE)]:
        if not exe:
            missing.append(name)
    return (len(missing) == 0), missing

def read_urls(csv_path: Path) -> List[str]:
    if not csv_path.exists():
        raise FileNotFoundError(f"tile CSV not found: {csv_path}")
    urls: List[str] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        # Accept common headers: url, href, link
        candidates = [h for h in ["url", "href", "link"] if h in (rdr.fieldnames or [])]
        if not candidates:
            raise ValueError(f"CSV must contain a url-like column (found headers: {rdr.fieldnames})")
        col = candidates[0]
        for row in rdr:
            u = (row.get(col) or "").strip()
            if u:
                urls.append(u)
    # Dedup while preserving order
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped

def ensure_dirs(*ps: Path) -> None:
    for p in ps:
        p.mkdir(parents=True, exist_ok=True)

def filesize_ok(p: Path, min_bytes: int = 1024) -> bool:
    try:
        return p.exists() and p.stat().st_size >= min_bytes
    except Exception:
        return False

def download_all(urls: List[str], raw_dir: Path, jobs: int, retries: int, dry: bool) -> None:
    ensure_dirs(raw_dir)
    if not urls:
        print("[INFO] no URLs to download.")
        return

    if ARIA2:
        # aria2 handles resume, parallel segments, and retries well
        urllist = raw_dir / "_urls.txt"
        urllist.write_text("\n".join(urls) + "\n", encoding="utf-8")
        cmd = [
            ARIA2, "--continue=true", "--auto-file-renaming=false",
            "--max-concurrent-downloads", str(max(1, jobs)),
            "--retry-wait=2", "--max-tries", str(retries),
            "--summary-interval=0",
            "--dir", str(raw_dir),
            "--input-file", str(urllist),
        ]
        if dry:
            print("➜ (dry-run) aria2c", " ".join(cmd[1:]))
            return
        sh(cmd)
        return

    # Fallback: curl loop (resume + retries)
    if not CURL:
        raise RuntimeError("No downloader available (aria2c nor curl).")
    for u in urls:
        dest = raw_dir / Path(u).name
        if filesize_ok(dest):
            print(f"[SKIP] {dest.name} (exists, {dest.stat().st_size:,} bytes)")
            continue
        cmd = [CURL, "-fL", "--retry", str(retries), "--retry-delay", "2", "-C", "-", u, "-o", str(dest)]
        if dry:
            print("➜ (dry-run)", " ".join(cmd))
            continue
        sh(cmd)

def write_tilelist(raw_dir: Path, county: str) -> Path:
    # Deterministic list (sorted by filename)
    tiles = sorted([p for p in raw_dir.glob("*.tif") if p.is_file()], key=lambda p: p.name)
    if not tiles:
        raise FileNotFoundError(f"No .tif tiles found under {raw_dir}")
    tile_txt = Path(tempfile.gettempdir()) / f"{county}_tiles.txt"
    with tile_txt.open("w", encoding="utf-8") as f:
        for t in tiles:
            f.write(str(t) + "\n")
    return tile_txt

def build_vrt(tile_txt: Path, vrt_out: Path, resampling: str, src_nodata: str | None, dst_nodata: str | None, dry: bool) -> None:
    if not GDALBUILDVRT:
        raise RuntimeError("gdalbuildvrt not found.")
    args = [GDALBUILDVRT, "-r", resampling]
    if src_nodata:
        args += ["-srcnodata", src_nodata]
    if dst_nodata:
        args += ["-vrtnodata", dst_nodata]
    args += ["-input_file_list", str(tile_txt), str(vrt_out)]
    if dry:
        print("➜ (dry-run)", " ".join(args)); return
    ensure_dirs(vrt_out.parent)
    sh(args)
    if GDALINFO:
        # quick stats line
        try:
            out = subprocess.check_output([GDALINFO, "-stats", str(vrt_out)], text=True)
            first = "\n".join(out.splitlines()[:25])
            print(first)
        except Exception:
            pass

def translate_cog(vrt: Path, cog_out: Path, threads: str, resampling_ovr: str, dry: bool) -> None:
    if not GDAL_TRANSLATE:
        raise RuntimeError("gdal_translate not found.")
    ensure_dirs(cog_out.parent)
    # DEM-friendly profile; BigTIFF on; external overviews ignored → force internal build
    # Note: GDAL COG driver builds overviews internally according to config.
    args = [
        GDAL_TRANSLATE, str(vrt), str(cog_out),
        "-of", "COG",
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=3",            # floating DEMs benefit
        "-co", "ZLEVEL=6",
        "-co", "BLOCKSIZE=512",          # 512x512 tends to balance IO
        "-co", "BIGTIFF=YES",
        "-co", f"NUM_THREADS={threads}",
        "-co", f"RESAMPLING={resampling_ovr}",
        "-co", "OVERVIEWS=AUTO",
        "-co", "OVERVIEW_RESAMPLING=AVERAGE",  # safe for DEM browses
        "-co", "ADD_ALPHA=IF_NECESSARY",
    ]
    if dry:
        print("➜ (dry-run)", " ".join(args)); return
    sh(args)

def try_registry_and_meta(cog_out: Path, county: str) -> None:
    # Best-effort: update registry and write meta (if scripts exist)
    try:
        upd = HERE / "update_registry.py"
        if upd.exists():
            sh([sys.executable, str(upd), str(cog_out), f"ks_lidar_county_{county}"])
        else:
            print("[INFO] registry updater not present; skipping.")
    except Exception as e:
        print(f"[WARN] registry update skipped: {e}")

    try:
        wm = HERE / "write_meta.py"
        if wm.exists():
            sh([sys.executable, str(wm), str(cog_out),
                "--inputs", str(cog_out.with_suffix(".vrt")),  # likely same folder
                "--extra", f"county={county}", "stage=lidar_mosaic"])
        else:
            print("[INFO] write_meta.py not present; skipping meta sidecars.")
    except Exception as e:
        print(f"[WARN] meta sidecars skipped: {e}")

def main() -> int:
    ap = argparse.ArgumentParser(description="Mosaic county 1m LiDAR tiles → VRT → COG")
    ap.add_argument("--county", help='County slug, e.g. "pawnee" (infers CSV path).')
    ap.add_argument("--tiles", type=Path, help="Explicit CSV of tile URLs (url|href|link column).")
    ap.add_argument("--raw-dir", type=Path, help="Directory for downloaded tiles.")
    ap.add_argument("--out-root", type=Path, help="Output root directory for VRT/COG.")
    ap.add_argument("--jobs", type=int, default=4, help="Parallel download jobs (aria2c only).")
    ap.add_argument("--retries", type=int, default=5, help="Download retries.")
    ap.add_argument("--resampling", default="bilinear", choices=["nearest","bilinear","cubic","cubicspline","lanczos"],
                    help="VRT resampling.")
    ap.add_argument("--src-nodata", help="Source nodata value (e.g., -9999).")
    ap.add_argument("--dst-nodata", help="VRT nodata value (e.g., -9999).")
    ap.add_argument("--ovr-resampling", default="AVERAGE",
                    choices=["NEAREST","AVERAGE","GAUSS","CUBIC","CUBICSPLINE","LANCZOS","MODE","RMS","BILINEAR","MIN","MAX","MED"],
                    help="Overview resampling for COG builder.")
    ap.add_argument("--threads", default="ALL_CPUS", help='NUM_THREADS for GDAL (e.g., "ALL_CPUS" or "8").')
    ap.add_argument("--dry-run", action="store_true", help="Plan only; no actions.")
    args = ap.parse_args()

    if not args.county and not args.tiles:
        ap.error("Provide --county or --tiles")

    ok, missing = shell_exists()
    if not ok:
        print(f"[ERR] missing required tools: {', '.join(missing)}", file=sys.stderr)
        return 2

    if args.county:
        county = args.county.strip().lower()
        tile_csv = args.tiles or ROOT / f"data/sources/dem/tile_indexes/{county}_1m_tiles.csv"
        raw_dir = args.raw_dir or ROOT / f"data/raw/lidar/{county}"
        out_root = args.out_root or ROOT / f"data/sources/dem/processed/lidar/{county}"
        vrt_out = out_root / f"{county}_1m.vrt"
        cog_out = out_root / f"{county}_1m_dem_cog.tif"
    else:
        # infer names from CSV file stem
        county = Path(args.tiles).stem.replace("_1m_tiles", "") if args.tiles else "county"
        tile_csv = args.tiles
        raw_dir = args.raw_dir or ROOT / f"data/raw/lidar/{county}"
        out_root = args.out_root or ROOT / f"data/sources/dem/processed/lidar/{county}"
        vrt_out = out_root / f"{county}_1m.vrt"
        cog_out = out_root / f"{county}_1m_dem_cog.tif"

    ensure_dirs(raw_dir, out_root)

    print(f"[INFO] County: {county}")
    print(f"[INFO] CSV:    {tile_csv}")
    print(f"[INFO] Raw:    {raw_dir}")
    print(f"[INFO] Out:    {out_root}")

    # URLs
    urls = read_urls(tile_csv)
    print(f"[INFO] {len(urls)} tile URL(s) found.")

    # Downloads
    download_all(urls, raw_dir, jobs=max(1, args.jobs), retries=max(1, args.retries), dry=args.dry_run)

    # Tile list
    try:
        tile_txt = write_tilelist(raw_dir, county)
    except FileNotFoundError as e:
        print(f"[ERR] {e}", file=sys.stderr)
        return 3

    # Build VRT
    try:
        build_vrt(tile_txt, vrt_out, args.resampling, args.src_nodata, args.dst_nodata, args.dry_run)
    except subprocess.CalledProcessError as e:
        print(f"[ERR] gdalbuildvrt failed: {e}", file=sys.stderr); return 4
    except Exception as e:
        print(f"[ERR] VRT step failed: {e}", file=sys.stderr); return 4

    # Translate to COG
    try:
        translate_cog(vrt_out, cog_out, args.threads, args.ovr_resampling, args.dry_run)
    except subprocess.CalledProcessError as e:
        print(f"[ERR] gdal_translate failed: {e}", file=sys.stderr); return 5
    except Exception as e:
        print(f"[ERR] COG translate failed: {e}", file=sys.stderr); return 5

    if not args.dry_run:
        try_registry_and_meta(cog_out, county)

    print(f"[OK] COG built → {cog_out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
