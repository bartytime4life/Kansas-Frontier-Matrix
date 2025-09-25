#!/usr/bin/env python3
"""
make_cogs.py — Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)

Features
--------
• Scans dirs/globs or takes explicit files; supports *.tif/*.tiff (and VRT passthrough).
• Parallel conversion with --jobs; idempotent unless --force/--repack.
• Prefers GDAL (gdal_translate -of COG); falls back to rio-cogeo when GDAL is absent.
• Sensible defaults:
    - COMPRESS=ZSTD, BLOCKSIZE=512, OVERVIEWS=AUTO, NUM_THREADS=ALL_CPUS, BIGTIFF=IF_SAFER
    - Overview resampling: GAUSS (continuous) or NEAREST/CUBIC via --resampling/--categorical
    - PREDICTOR=2 for non-RGB 8/16/32 rasters (can disable with --no-predictor)
• Optional JPEG mode (--jpeg) for 8-bit RGB (QUALITY=90 by default).
• Detects NoData from source (gdalinfo -json) when --nodata is not set.
• Atomic writes, .sha256 + .meta.json sidecars, and manifest JSON.
• Optional validation via rio-cogeo validate (--validate).

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

  # Preserve input tree under out/
  python scripts/make_cogs.py --inp data/processed --out data/cogs --mirror-tree

  # Use JPEG for RGB 8-bit rasters
  python scripts/make_cogs.py --inp data/processed --out data/cogs --jpeg --quality 90
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
import tempfile
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple, Dict, Any

VALID_EXT = {".tif", ".tiff", ".vrt"}
GDAL_TRANSLATE = shutil.which("gdal_translate")
GDALINFO = shutil.which("gdalinfo")
RIO = shutil.which("rio")  # rio-cogeo

DEFAULT_COMP = "ZSTD"          # Alternatives: DEFLATE, LZW
DEFAULT_BLOCK = "512"          # tile size
DEFAULT_OVR_RESAMPLING = "GAUSS"  # good for continuous rasters; NEAREST for categorical
DEFAULT_THREADS = "ALL_CPUS"
DEFAULT_LEVEL = "15"

# ------------------------------
# Small I/O & hash helpers
# ------------------------------

def sha256(p: Path, *, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

def write_sidecars(dst: Path, inputs: List[Path], cmdline: List[str], tool: str) -> None:
    dst.with_suffix(dst.suffix + ".sha256").write_text(sha256(dst) + "\n", encoding="utf-8")
    meta = {
        "output": str(dst),
        "size": dst.stat().st_size,
        "inputs": [str(i) for i in inputs],
        "command": " ".join(cmdline),
        "tool": tool,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
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
            for p in it:
                if p.suffix.lower() in VALID_EXT:
                    files.append(p.resolve())
    # stable unique
    seen, uniq = set(), []
    for f in files:
        if f not in seen:
            uniq.append(f)
            seen.add(f)
    return uniq

# ------------------------------
# gdalinfo helpers
# ------------------------------

def gdalinfo_json(src: Path) -> Optional[Dict[str, Any]]:
    if not GDALINFO:
        return None
    try:
        out = subprocess.check_output([GDALINFO, "-json", str(src)], text=True)
        return json.loads(out)
    except Exception:
        return None

def is_rgb_8bit(info: Optional[Dict[str, Any]]) -> bool:
    if not info:
        return False
    bands = info.get("bands") or []
    if len(bands) < 3:
        return False
    # 8-bit RGB if 3 bands uint8 with colorInterp like Red/Green/Blue
    interps = [str(b.get("colorInterpretation", "")).lower() for b in bands[:3]]
    types = [str(b.get("type", "")).upper() for b in bands[:3]]
    return all(t in ("BYTE", "UINT8") for t in types) and set(interps) >= {"red", "green", "blue"}

def any_float_or_int(info: Optional[Dict[str, Any]]) -> bool:
    if not info:
        return True  # conservative: assume yes → predictor=2
    for b in info.get("bands", []):
        typ = str(b.get("type", "")).upper()
        if any(k in typ for k in ("INT", "FLOAT")):
            return True
    return False

def get_nodata(info: Optional[Dict[str, Any]]) -> Optional[str]:
    if not info:
        return None
    for b in info.get("bands", []):
        if "noDataValue" in b:
            try:
                return str(b["noDataValue"])
            except Exception:
                return None
    return None

def already_cog(info: Optional[Dict[str, Any]]) -> bool:
    if not info:
        return False
    # GDAL >= 3.1 exposes "COG" driver metadata in json; fallback to rio validate if present
    drv = (info.get("driverShortName") or "").upper()
    if drv == "COG":
        return True
    return False

def rio_validate_ok(path: Path) -> bool:
    if not RIO:
        return False
    try:
        subprocess.check_output([RIO, "cogeo", "validate", str(path)])
        return True
    except Exception:
        return False

# ------------------------------
# GDAL & rio-cogeo commands
# ------------------------------

def build_gdal_cmd(
    src: Path, dst: Path, *,
    compression: str, blocksize: str, resampling: str,
    threads: str, nodata: Optional[str], level: Optional[str],
    predictor: bool, jpeg: bool, quality: int
) -> List[str]:
    # base COG options
    cmd = [
        GDAL_TRANSLATE or "gdal_translate",
        "-of", "COG",
        "-co", f"BLOCKSIZE={blocksize}",
        "-co", f"RESAMPLING={resampling}",
        "-co", f"NUM_THREADS={threads}",
        "-co", "OVERVIEWS=AUTO",
        "-co", "BIGTIFF=IF_SAFER",
    ]
    if level:
        cmd += ["-co", f"LEVEL={level}"]

    if jpeg:
        cmd += ["-co", "COMPRESS=JPEG", "-co", f"QUALITY={quality}"]
    else:
        cmd += ["-co", f"COMPRESS={compression}"]
        if predictor:
            cmd += ["-co", "PREDICTOR=2"]

    if nodata is not None:
        cmd += ["-a_nodata", nodata]

    cmd += [str(src), str(dst)]
    return cmd

def try_gdal_translate(
    src: Path, dst: Path, *,
    compression: str, blocksize: str, resampling: str,
    threads: str, nodata: Optional[str], level: Optional[str],
    predictor: bool, jpeg: bool, quality: int
) -> bool:
    if not GDAL_TRANSLATE:
        return False
    cmd = build_gdal_cmd(
        src, dst,
        compression=compression, blocksize=blocksize,
        resampling=resampling, threads=threads,
        nodata=nodata, level=level,
        predictor=predictor, jpeg=jpeg, quality=quality
    )
    print("[CMD]", " ".join(cmd))
    subprocess.check_call(cmd)
    return True

def try_rio_cogeo(src: Path, dst: Path, *, resampling: str) -> bool:
    if not RIO:
        return False
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
    repack: bool
    mirror_tree: bool
    dst_name_template: str
    compression: str
    blocksize: str
    resampling: str
    threads: str
    nodata: Optional[str]
    level: Optional[str]
    validate: bool
    predictor: bool
    jpeg: bool
    quality: int

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
    skipped_reason: Optional[str] = None

def dst_path_for(task: Task, src: Path) -> Path:
    stem = src.stem  # handle .tif/.tiff/.vrt → stem
    dst_name = task.dst_name_template.format(stem=stem)
    if not dst_name.lower().endswith(".tif"):
        dst_name += ".tif"
    if task.mirror_tree:
        # rebase src under out_dir preserving relative path below the common input root
        # heuristic: mirror from first directory after the common ancestor of input paths;
        # practical alternative: mirror from src.parent name only (simple & robust)
        return task.out_dir / src.parent.name / dst_name
    return task.out_dir / dst_name

class silent:
    def __enter__(self): return self
    def __exit__(self, *exc): return True

def convert_one(task: Task) -> Entry:
    t0 = time.time()
    src = task.src
    dst = dst_path_for(task, src)
    dst.parent.mkdir(parents=True, exist_ok=True)

    info = gdalinfo_json(src)
    # detect rgb 8bit, nodata, is cog
    is_rgb = is_rgb_8bit(info)
    nodata_detected = get_nodata(info)

    # Skip logic
    if dst.exists() and not task.force:
        # existing output — check if valid cog and skip
        if already_cog(gdalinfo_json(dst)) or rio_validate_ok(dst):
            return Entry(str(src), str(dst), True, None, dst.stat().st_size, sha256(dst), "skip", time.time() - t0, "exists:COG")
        # not a COG — unless repack/force, still keep it (idempotence)
        if not task.repack:
            return Entry(str(src), str(dst), True, None, dst.stat().st_size, sha256(dst), "skip", time.time() - t0, "exists:nonCOG")

    # If input is already COG and repack is not requested, short-circuit: copy to dst atomically
    if not task.repack and (already_cog(info) or rio_validate_ok(src)):
        # atomic copy
        tmp = dst.with_suffix(dst.suffix + ".tmp")
        tmp.write_bytes(src.read_bytes())
        tmp.replace(dst)
        write_sidecars(dst, [src], sys.argv, tool="copy")
        return Entry(str(src), str(dst), True, None, dst.stat().st_size, sha256(dst), "copy", time.time() - t0)

    # Use source nodata if not provided
    nodata = task.nodata if task.nodata is not None else nodata_detected

    tool = None
    tmp = dst.with_suffix(dst.suffix + ".tmp")
    try:
        if tmp.exists():
            tmp.unlink()

        # Choose predictor automatically for non-RGB
        use_predictor = (task.predictor and not is_rgb and not task.jpeg and task.compression in {"ZSTD", "DEFLATE", "LZW"})

        # JPEG only when we detect 8-bit RGB
        use_jpeg = (task.jpeg and is_rgb)
        if task.jpeg and not is_rgb:
            print(f"[WARN] {src.name}: --jpeg requested but raster not 8-bit RGB; using {task.compression} instead")

        if try_gdal_translate(
            src, tmp,
            compression=task.compression,
            blocksize=task.blocksize,
            resampling=task.resampling,
            threads=task.threads,
            nodata=nodata,
            level=task.level,
            predictor=use_predictor,
            jpeg=use_jpeg,
            quality=task.quality,
        ):
            tool = "gdal_translate"
        else:
            print("[WARN] gdal_translate not found; trying rio-cogeo")
            if try_rio_cogeo(src, tmp, resampling=task.resampling):
                tool = "rio_cogeo"
            else:
                return Entry(str(src), None, False, "No COG tool available (need GDAL or rio-cogeo)", None, None, None, time.time() - t0)

        # Optional validation (best-effort)
        if task.validate and RIO:
            val_cmd = [RIO, "cogeo", "validate", str(tmp)]
            print("[CMD]", " ".join(val_cmd))
            subprocess.check_call(val_cmd)

        # atomic move
        tmp.replace(dst)

        # Sidecars
        write_sidecars(dst, [src], sys.argv, tool=tool or "-")

        return Entry(str(src), str(dst), True, None, dst.stat().st_size, sha256(dst), tool, time.time() - t0)

    except subprocess.CalledProcessError as e:
        with silent(): tmp.exists() and tmp.unlink()
        return Entry(str(src), str(dst), False, f"Subprocess: {e}", None, None, tool, time.time() - t0)
    except Exception as e:
        with silent(): tmp.exists() and tmp.unlink()
        return Entry(str(src), str(dst), False, f"{type(e).__name__}: {e}", None, None, tool, time.time() - t0)

# ------------------------------
# CLI
# ------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs)")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--inp", type=Path, help="Input directory to scan")
    g.add_argument("--files", nargs="+", type=Path, help="Explicit files (*.tif/*.tiff/*.vrt)")

    p.add_argument("--out", type=Path, required=True, help="Output directory for COGs")
    p.add_argument("--pattern", default="*.tif", help='Glob pattern for --inp (default: "*.tif")')
    p.add_argument("--recursive", action="store_true", help="Recurse when scanning --inp")
    p.add_argument("--force", action="store_true", help="Overwrite/replace even if output COG exists")
    p.add_argument("--repack", action="store_true", help="Repack even if input/output already COG")
    p.add_argument("--jobs", type=int, default=os.cpu_count() or 4, help="Parallel workers (default: CPU count)")

    p.add_argument("--compression", default=DEFAULT_COMP, choices=["ZSTD", "DEFLATE", "LZW"], help="COG compression (ignored if --jpeg)")
    p.add_argument("--blocksize", default=DEFAULT_BLOCK, help="Tile size (e.g., 256 or 512)")
    p.add_argument("--resampling", default=DEFAULT_OVR_RESAMPLING, choices=["NEAREST", "GAUSS", "CUBIC"], help="Overview resampling")
    p.add_argument("--categorical", action="store_true", help="Shortcut: set resampling=NEAREST (categorical data)")
    p.add_argument("--threads", default=DEFAULT_THREADS, help="NUM_THREADS for GDAL (default: ALL_CPUS)")
    p.add_argument("--nodata", default=None, help="Set nodata value (e.g., 0); omit to keep source (auto-detect if possible)")
    p.add_argument("--level", default=DEFAULT_LEVEL, help="COG encoder effort/level (some drivers support this; default: 15)")
    p.add_argument("--no-predictor", dest="predictor", action="store_false", help="Disable PREDICTOR=2 hint")
    p.add_argument("--validate", action="store_true", help="Validate COG with rio-cogeo if available")

    p.add_argument("--jpeg", action="store_true", help="Use COMPRESS=JPEG for 8-bit RGB rasters (else falls back)")
    p.add_argument("--quality", type=int, default=90, help="JPEG QUALITY (default 90)")

    p.add_argument("--mirror-tree", action="store_true", help="Mirror input directory tree under --out")
    p.add_argument("--dst-name-template", default="{stem}.tif", help="Destination filename template (default '{stem}.tif')")

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
        pat = args.pattern
        inputs = list_inputs([args.inp], pat, args.recursive)

    if not inputs:
        print("[ERR] No input rasters found.", file=sys.stderr)
        return 2

    out_dir: Path = args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    resampling = "NEAREST" if args.categorical else str(args.resampling).upper()

    # Build tasks
    tasks: List[Task] = [
        Task(
            src=src,
            out_dir=out_dir,
            force=bool(args.force),
            repack=bool(args.repack),
            mirror_tree=bool(args.mirror_tree),
            dst_name_template=str(args.dst_name_template),
            compression=str(args.compression),
            blocksize=str(args.blocksize),
            resampling=resampling,
            threads=str(args.threads),
            nodata=(str(args.nodata) if args.nodata is not None else None),
            level=(str(args.level) if args.level else None),
            validate=bool(args.validate),
            predictor=bool(args.predictor),
            jpeg=bool(args.jpeg),
            quality=int(args.quality),
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
            extra = f"  tool={e.tool or '-'}"
            if e.skipped_reason:
                extra += f"  skip={e.skipped_reason}"
            print(f"[{tag}] {name}{extra}  {f'{e.size}B' if e.size else ''}  ({e.duration_s:.2f}s)")
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
