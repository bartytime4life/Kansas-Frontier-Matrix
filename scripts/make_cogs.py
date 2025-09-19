#!/usr/bin/env python3
"""
make_cog.py — Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)

Features
--------
• Recurses directories (or takes explicit files) with glob pattern.
• Uses GDAL gdal_translate + internal overviews; falls back to rio-cogeo if needed.
• Sensible defaults: ZSTD compression, 512x512 tiles, GAUSS/NEAREST overview resampling.
• Handles nodata/predictor hints (float DEMs → predictor=2).
• Skips existing outputs unless --force; writes checksum + provenance sidecars.
• Optional validation via rio-cogeo (if installed).
• Clean stdout logs; non-zero exit on failure.

Examples
--------
  # convert all .tif in a directory (non-recursive) to data/cogs/dem/
  python scripts/make_cog.py --inp data/processed/dem --out data/cogs/dem

  # recursive with pattern and validation
  python scripts/make_cog.py --inp data/processed --recursive --pattern "*.tif" \
      --out data/cogs --validate

  # explicit files
  python scripts/make_cog.py --files data/processed/overlays/usgs_1894_larned.tif \
      --out data/cogs/overlays
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

VALID_EXT = {".tif", ".tiff"}
GDAL_TRANSLATE = shutil.which("gdal_translate")
GDALINFO = shutil.which("gdalinfo")
RIO = shutil.which("rio")  # rio-cogeo
DEFAULT_COMP = "ZSTD"
DEFAULT_BLOCK = "512"
DEFAULT_OVR_RESAMPLING = "GAUSS"  # good for hillshade/continuous rasters; use NEAREST for categorical


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def list_inputs(roots: Iterable[Path], pattern: str, recursive: bool) -> List[Path]:
    files: List[Path] = []
    for root in roots:
        if root.is_file() and root.suffix.lower() in VALID_EXT:
            files.append(root.resolve())
            continue
        if root.is_dir():
            it = root.rglob(pattern) if recursive else root.glob(pattern)
            files.extend(p.resolve() for p in it if p.suffix.lower() in VALID_EXT)
    return files


def has_float_data(src: Path) -> bool:
    # Best-effort use gdalinfo to detect float data (for predictor)
    if not GDALINFO:
        return False
    try:
        out = subprocess.check_output([GDALINFO, "-json", str(src)], text=True)
        info = json.loads(out)
        bands = info.get("bands", [])
        for b in bands:
            dt = b.get("type", "").upper()
            if "FLOAT" in dt:
                return True
    except Exception:
        pass
    return False


def build_gdal_cmd(src: Path, dst: Path, compression: str, blocksize: str,
                   resampling: str, threads: str, nodata: Optional[str], web_optimized: bool) -> List[str]:
    # base translate to COG
    cmd = [
        GDAL_TRANSLATE or "gdal_translate",
        "-of", "COG",
        "-co", f"COMPRESS={compression}",
        "-co", f"BLOCKSIZE={blocksize}",
        "-co", f"RESAMPLING={resampling}",               # overview resampling inside COG
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
    ]
    # predictor for float DEMs helps compression
    if has_float_data(src):
        cmd += ["-co", "PREDICTOR=2"]

    if web_optimized:
        # add layout hints (overview levels auto; internal tiling handled by COG)
        cmd += ["-co", "LEVEL=15"]  # high ZSTD effort; harmless for DEFLATE

    if nodata is not None:
        cmd += ["-a_nodata", nodata]

    cmd += [str(src), str(dst)]
    return cmd


def run(cmd: List[str]) -> None:
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)


def try_gdal_translate(src: Path, dst: Path, compression: str, blocksize: str,
                       resampling: str, threads: str, nodata: Optional[str], web_optimized: bool) -> bool:
    if not GDAL_TRANSLATE:
        return False
    cmd = build_gdal_cmd(src, dst, compression, blocksize, resampling, threads, nodata, web_optimized)
    run(cmd)
    return True


def try_rio_cogeo(src: Path, dst: Path, resampling: str) -> bool:
    if not RIO:
        return False
    profile = "deflate" if DEFAULT_COMP != "ZSTD" else "deflate"  # rio-cogeo has stock profiles; ZSTD via env in newer versions
    cmd = [
        RIO, "cogeo", "create",
        str(src), str(dst),
        "--cog-profile", profile,
        "--overview-resampling", resampling.lower(),
        "--web-optimized"
    ]
    run(cmd)
    return True


def write_sidecars(dst: Path, inputs: List[Path], cmdline: List[str]) -> None:
    # checksum
    dst.with_suffix(dst.suffix + ".sha256").write_text(sha256(dst))
    # meta
    meta = {
        "output": str(dst),
        "size": dst.stat().st_size,
        "inputs": [str(i) for i in inputs],
        "command": " ".join(cmdline),
    }
    dst.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))


def convert_one(src: Path, out_dir: Path, force: bool, compression: str, blocksize: str,
                resampling: str, threads: str, nodata: Optional[str], web_optimized: bool,
                validate: bool) -> Tuple[Optional[Path], Optional[str]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / src.name
    if dst.exists() and not force:
        print(f"[SKIP] exists: {dst}")
        return dst, None

    # Attempt GDAL; fall back to rio-cogeo
    try:
        used_cmd = None
        if try_gdal_translate(src, dst, compression, blocksize, resampling, threads, nodata, web_optimized):
            used_cmd = "gdal_translate"
        else:
            print("[WARN] gdal_translate not found; trying rio-cogeo")
            if try_rio_cogeo(src, dst, resampling):
                used_cmd = "rio_cogeo"
            else:
                return None, "No COG tool available (need GDAL or rio-cogeo)"

        # Validation (optional)
        if validate and RIO:
            val_cmd = [RIO, "cogeo", "validate", str(dst)]
            run(val_cmd)

        write_sidecars(dst, [src], sys.argv)
        print(f"[OK] COG → {dst}")
        return dst, None
    except subprocess.CalledProcessError as e:
        # cleanup partial
        if dst.exists():
            try:
                dst.unlink()
            except Exception:
                pass
        return None, f"conversion failed: {e}"
    except Exception as e:
        if dst.exists():
            try:
                dst.unlink()
            except Exception:
                pass
        return None, f"error: {e}"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--inp", type=Path, help="Input directory to scan")
    g.add_argument("--files", nargs="+", type=Path, help="Explicit files")

    p.add_argument("--out", type=Path, required=True, help="Output directory")
    p.add_argument("--pattern", default="*.tif", help='Glob pattern (default: "*.tif")')
    p.add_argument("--recursive", action="store_true", help="Recurse when scanning --inp")
    p.add_argument("--force", action="store_true", help="Overwrite existing outputs")
    p.add_argument("--compression", default=DEFAULT_COMP, choices=["ZSTD", "DEFLATE", "LZW"], help="COG compression")
    p.add_argument("--blocksize", default=DEFAULT_BLOCK, help="Tile size (e.g., 256 or 512)")
    p.add_argument("--resampling", default=DEFAULT_OVR_RESAMPLING, choices=["NEAREST", "GAUSS", "CUBIC"], help="Overview resampling")
    p.add_argument("--threads", default="ALL_CPUS", help="NUM_THREADS to pass to GDAL")
    p.add_argument("--nodata", default=None, help="Set nodata value (e.g., 0); leave unset to keep source")
    p.add_argument("--web-optimized", action="store_true", help="Add web-tiling friendly hints")
    p.add_argument("--validate", action="store_true", help="Validate COG with rio-cogeo if available")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.files:
        inputs = [Path(f) for f in args.files]
    else:
        if not args.inp.exists():
            print(f"[ERR] Input path does not exist: {args.inp}", file=sys.stderr)
            return 2
        inputs = list_inputs([args.inp], args.pattern, args.recursive)

    if not inputs:
        print("[ERR] No input rasters found.", file=sys.stderr)
        return 2

    failures = 0
    for src in inputs:
        dst, err = convert_one(
            src=src,
            out_dir=args.out,
            force=args.force,
            compression=args.compression,
            blocksize=args.blocksize,
            resampling=args.resampling,
            threads=args.threads,
            nodata=args.nodata,
            web_optimized=bool(args.web_optimized),
            validate=bool(args.validate),
        )
        if err:
            failures += 1
            print(f"[FAIL] {src}: {err}", file=sys.stderr)

    if failures:
        print(f"[WARN] {failures} file(s) failed.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
