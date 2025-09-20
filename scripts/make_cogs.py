#!/usr/bin/env python3
"""
make_cogs.py — Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)

Features
--------
• Scans dirs/globs or takes explicit files; supports *.tif/*.tiff.
• Parallel conversion with --jobs, idempotent unless --force.
• Prefers GDAL (gdal_translate -of COG); falls back to rio-cogeo when GDAL is absent.
• Sensible defaults:
    - Compression: ZSTD (fast+small), tiles 512x512, internal overviews (OVERVIEWS=AUTO)
    - Overview resampling: GAUSS (good continuous rasters) or NEAREST/CUBIC per flag
    - FLOAT rasters → PREDICTOR=2 hint to improve compression
• Sidecars: .sha256 and .meta.json (command + inputs + size)
• Optional COG validation via rio-cogeo --validate
• Emits a manifest JSON for reproducibility (MCP/CI)

Examples
--------
  # Convert all .tif under a dir recursively
  python scripts/make_cogs.py --inp data/processed --recursive --pattern "*.tif" \
      --out data/cogs --jobs 8

  # Single files
  python scripts/make_cogs.py --files data/processed/map1.tif data/processed/dem.tif \
      --out data/cogs

  # Validate with rio-cogeo after creation
  python scripts/make_cogs.py --inp data/processed --out data/cogs --validate
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

VALID_EXT = {".tif", ".tiff"}
GDAL_TRANSLATE = shutil.which("gdal_translate")
GDALINFO = shutil.which("gdalinfo")
RIO = shutil.which("rio")  # rio-cogeo

DEFAULT_COMP = "ZSTD"          # 'DEFLATE' or 'LZW' are ok alternatives
DEFAULT_BLOCK = "512"          # tile size
DEFAULT_OVR_RESAMPLING = "GAUSS"  # good for continuous rasters; use NEAREST for categorical


# ------------------------------
# Small I/O & hash helpers
# ------------------------------

def sha256(p: Path, *, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def write_sidecars(dst: Path, inputs: List[Path], cmdline: List[str]) -> None:
    # checksum
    dst.with_suffix(dst.suffix + ".sha256").write_text(sha256(dst) + "\n", encoding="utf-8")
    # meta
    meta = {
        "output": str(dst),
        "size": dst.stat().st_size,
        "inputs": [str(i) for i in inputs],
        "command": " ".join(cmdline),
    }
    dst.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2))


def list_inputs(roots: Iterable[Path], pattern: str, recursive: bool) -> List[Path]:
    files: List[Path] = []
    for root in roots:
        if root.is_file() and root.suffix.lower() in VALID_EXT:
            files.append(root.resolve())
            continue
        if root.is_dir():
            it = root.rglob(pattern) if recursive else root.glob(pattern)
            files.extend(p.resolve() for p in it if p.suffix.lower() in VALID_EXT)
    # stable unique
    seen, uniq = set(), []
    for f in files:
        if f not in seen:
            uniq.append(f)
            seen.add(f)
    return uniq


def has_float_data(src: Path) -> bool:
    """Best-effort: check if any band is FLOAT via gdalinfo -json (predictor=2 hint)."""
    if not GDALINFO:
        return False
    try:
        out = subprocess.check_output([GDALINFO, "-json", str(src)], text=True)
        info = json.loads(out)
        for b in info.get("bands", []):
            if "FLOAT" in str(b.get("type", "")).upper():
                return True
    except Exception:
        pass
    return False


# ------------------------------
# GDAL & rio-cogeo commands
# ------------------------------

def build_gdal_cmd(
    src: Path, dst: Path, *, compression: str, blocksize: str, resampling: str,
    threads: str, nodata: Optional[str], level: Optional[str]
) -> List[str]:
    cmd = [
        GDAL_TRANSLATE or "gdal_translate",
        "-of", "COG",
        "-co", f"COMPRESS={compression}",
        "-co", f"BLOCKSIZE={blocksize}",
        "-co", f"RESAMPLING={resampling}",
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
    ]
    # effort level (optional; supported by some drivers)
    if level:
        cmd += ["-co", f"LEVEL={level}"]

    if has_float_data(src):
        cmd += ["-co", "PREDICTOR=2"]

    if nodata is not None:
        cmd += ["-a_nodata", nodata]

    cmd += [str(src), str(dst)]
    return cmd


def try_gdal_translate(
    src: Path, dst: Path, *, compression: str, blocksize: str, resampling: str,
    threads: str, nodata: Optional[str], level: Optional[str]
) -> bool:
    if not GDAL_TRANSLATE:
        return False
    cmd = build_gdal_cmd(
        src, dst,
        compression=compression, blocksize=blocksize,
        resampling=resampling, threads=threads,
        nodata=nodata, level=level
    )
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)
    return True


def try_rio_cogeo(src: Path, dst: Path, *, resampling: str) -> bool:
    if not RIO:
        return False
    # NOTE: rio-cogeo profiles vary by version; 'deflate' is most portable.
    cmd = [
        RIO, "cogeo", "create",
        str(src), str(dst),
        "--cog-profile", "deflate",
        "--overview-resampling", resampling.lower(),
        "--web-optimized"
    ]
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)
    return True


# ------------------------------
# Conversion core
# ------------------------------

@dataclass
class Task:
    src: Path
    out_dir: Path
    force: bool
    compression: str
    blocksize: str
    resampling: str
    threads: str
    nodata: Optional[str]
    level: Optional[str]
    validate: bool


@dataclass
class Entry:
    src: str
    dst: Optional[str]
    ok: bool
    error: Optional[str] = None
    size: Optional[int] = None
    sha256: Optional[str] = None
    tool: Optional[str] = None
    duration_s: float = 0.0


def convert_one(task: Task) -> Entry:
    t0 = time.time()
    src = task.src
    dst = task.out_dir / src.name
    dst.parent.mkdir(parents=True, exist_ok=True)

    # Skip if exists and not forced
    if dst.exists() and not task.force:
        h = sha256(dst)
        return Entry(str(src), str(dst), True, None, dst.stat().st_size, h, "skip", time.time() - t0)

    # Try GDAL → rio-cogeo
    tool = None
    try:
        if try_gdal_translate(
            src, dst,
            compression=task.compression,
            blocksize=task.blocksize,
            resampling=task.resampling,
            threads=task.threads,
            nodata=task.nodata,
            level=task.level,
        ):
            tool = "gdal_translate"
        else:
            print("[WARN] gdal_translate not found; trying rio-cogeo")
            if try_rio_cogeo(src, dst, resampling=task.resampling):
                tool = "rio_cogeo"
            else:
                return Entry(str(src), None, False, "No COG tool available (need GDAL or rio-cogeo)", None, None, None, time.time() - t0)

        # Optional validation (best-effort)
        if task.validate and RIO:
            val_cmd = [RIO, "cogeo", "validate", str(dst)]
            print("[CMD]", " ".join(val_cmd))
            subprocess.check_call(val_cmd)

        # Sidecars
        write_sidecars(dst, [src], sys.argv)

        return Entry(str(src), str(dst), True, None, dst.stat().st_size, sha256(dst), tool, time.time() - t0)

    except subprocess.CalledProcessError as e:
        if dst.exists():
            with contextlib_silent(): dst.unlink()
        return Entry(str(src), str(dst), False, f"Subprocess: {e}", None, None, tool, time.time() - t0)
    except Exception as e:
        if dst.exists():
            with contextlib_silent(): dst.unlink()
        return Entry(str(src), str(dst), False, f"{type(e).__name__}: {e}", None, None, tool, time.time() - t0)


class contextlib_silent:
    def __enter__(self): return self
    def __exit__(self, *exc): return True


# ------------------------------
# CLI
# ------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--inp", type=Path, help="Input directory to scan")
    g.add_argument("--files", nargs="+", type=Path, help="Explicit files (*.tif/*.tiff)")

    p.add_argument("--out", type=Path, required=True, help="Output directory for COGs")
    p.add_argument("--pattern", default="*.tif", help='Glob pattern for --inp (default: "*.tif")')
    p.add_argument("--recursive", action="store_true", help="Recurse when scanning --inp")
    p.add_argument("--force", action="store_true", help="Overwrite existing outputs")
    p.add_argument("--jobs", type=int, default=4, help="Parallel workers (default: 4)")

    p.add_argument("--compression", default=DEFAULT_COMP, choices=["ZSTD", "DEFLATE", "LZW"], help="COG compression")
    p.add_argument("--blocksize", default=DEFAULT_BLOCK, help="Tile size (e.g., 256 or 512)")
    p.add_argument("--resampling", default=DEFAULT_OVR_RESAMPLING, choices=["NEAREST", "GAUSS", "CUBIC"], help="Overview resampling")
    p.add_argument("--threads", default="ALL_CPUS", help="NUM_THREADS for GDAL")
    p.add_argument("--nodata", default=None, help="Set nodata value (e.g., 0); omit to keep source")
    p.add_argument("--level", default="15", help="COG encoder effort/level (some drivers support this; default: 15)")
    p.add_argument("--validate", action="store_true", help="Validate COG with rio-cogeo if available")

    p.add_argument("--manifest", type=Path, default=Path("data/cogs/manifest.cogs.json"), help="Manifest JSON output")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    # Build file list
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

    out_dir: Path = args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build tasks
    tasks: List[Task] = [
        Task(
            src=src,
            out_dir=out_dir,
            force=bool(args.force),
            compression=str(args.compression),
            blocksize=str(args.blocksize),
            resampling=str(args.resampling).upper(),
            threads=str(args.threads),
            nodata=(str(args.nodata) if args.nodata is not None else None),
            level=(str(args.level) if args.level else None),
            validate=bool(args.validate),
        )
        for src in inputs
    ]

    # Run in parallel
    entries: List[Entry] = []
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=max(1, int(args.jobs))) as ex:
        futs = [ex.submit(convert_one, t) for t in tasks]
        for fut in cf.as_completed(futs):
            e = fut.result()
            entries.append(e)
            tag = "OK" if e.ok else "FAIL"
            name = Path(e.dst or e.src).name
            print(f"[{tag}] {name}  tool={e.tool or '-'}  {f'{e.size}B' if e.size else ''}  ({e.duration_s:.2f}s)")
            if e.error:
                print(f"      {e.error}", file=sys.stderr)

    # Manifest
    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_s": time.time() - t0,
        "out_dir": str(out_dir),
        "environment": {
            "gdal_translate": bool(GDAL_TRANSLATE),
            "gdalinfo": bool(GDALINFO),
            "rio": bool(RIO),
        },
        "entries": [asdict(e) for e in entries],
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
        f.write("\n")
    print(f"[RESULT] ok={sum(1 for e in entries if e.ok)}  fail={sum(1 for e in entries if not e.ok)}  wrote {args.manifest}")

    return 0 if all(e.ok for e in entries) else 1


if __name__ == "__main__":
    raise SystemExit(main())
