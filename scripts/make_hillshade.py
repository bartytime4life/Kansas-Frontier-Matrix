#!/usr/bin/env python3
"""
scripts/make_hillshade.py
=========================

Generate hillshade rasters from DEM GeoTIFFs.

Design goals
------------
- Prefer GDAL Python API if available; otherwise fall back to gdaldem/gdal_translate CLIs.
- Safe, idempotent, parallelizable; emits SHA256 and manifest JSON for MCP traceability.
- Optionally writes Cloud-Optimized GeoTIFFs (COG).

Examples
--------
# Basic: make hillshade for all DEMs into data/processed/hillshade/
python scripts/make_hillshade.py data/raw/**/*.tif --dest data/processed/hillshade

# Multi-directional, COG output, 8 workers
python scripts/make_hillshade.py data/raw/**/*.tif --dest data/processed/hillshade \
  --multidir --cog --jobs 8

# Custom lighting
python scripts/make_hillshade.py dem.tif --azimuth 315 --altitude 45 --zfactor 1.0

Notes
-----
- Requires GDAL (Python bindings *or* CLI tools on PATH).
- This script does not reproject; ensure your DEM units & CRS are appropriate (z-factor may be needed).
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

# --------------------------
# Optional GDAL bindings
# --------------------------
_HAS_GDAL = False
try:
    from osgeo import gdal  # type: ignore

    gdal.UseExceptions()
    _HAS_GDAL = True
except Exception:
    _HAS_GDAL = False


# --------------------------
# Small helpers
# --------------------------

def _iter_paths(patterns: Iterable[str]) -> Iterable[Path]:
    for pat in patterns:
        p = Path(pat)
        if p.is_dir():
            yield from sorted(p.rglob("*.tif"))
            yield from sorted(p.rglob("*.tiff"))
        else:
            # Glob expansion by pathlib
            if any(ch in pat for ch in "*?[]"):
                for m in sorted(Path().glob(pat)):
                    if m.suffix.lower() in (".tif", ".tiff"):
                        yield m
            else:
                if p.is_file() and p.suffix.lower() in (".tif", ".tiff"):
                    yield p


def _sha256(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _suffix_with(src: Path, suffix: str) -> Path:
    return src.with_name(src.stem + suffix).with_suffix(".tif")


def _which(cmd: str) -> Optional[str]:
    from shutil import which
    return which(cmd)


# --------------------------
# Output planning
# --------------------------

@dataclass
class Task:
    src: str
    dst: str
    cog: bool
    azimuth: float
    altitude: float
    zfactor: float
    scale: Optional[float]
    multidir: bool
    alg: str
    resampling: str
    overwrite: bool


@dataclass
class Result:
    src: str
    dst: str
    ok: bool
    duration_s: float
    src_sha256: Optional[str] = None
    dst_sha256: Optional[str] = None
    error: Optional[str] = None
    cog: Optional[bool] = None
    params: Optional[dict] = None


# --------------------------
# GDAL API implementation
# --------------------------

def _hillshade_gdal_api(task: Task) -> None:
    """Use GDAL Python API to produce a (temporary) GTiff hillshade. COG handled separately."""
    src_ds = gdal.Open(task.src, gdal.GA_ReadOnly)
    if src_ds is None:
        raise RuntimeError("GDAL failed to open source")

    opts = gdal.DEMProcessingOptions(
        azimuth=task.azimuth,
        altitude=task.altitude,
        zFactor=task.zfactor,
        scale=task.scale if task.scale is not None else 0.0,
        multiDirectional=task.multidir,
        algorithm=task.alg if task.alg else None,
    )
    # Write to temporary file first
    tmp = Path(task.dst).with_suffix(".tmp.tif")
    try:
        out_ds = gdal.DEMProcessing(str(tmp), src_ds, "hillshade", options=opts)
        if out_ds is None:
            raise RuntimeError("DEMProcessing returned None")
        out_ds = None
        # Move tmp to destination if not COG; COG will reconvert below
        if not task.cog:
            tmp.replace(task.dst)
        else:
            # Convert to COG
            _to_cog(tmp, Path(task.dst), resampling=task.resampling, overwrite=task.overwrite)
            if tmp.exists():
                tmp.unlink()
    finally:
        try:
            src_ds = None
        except Exception:
            pass


def _to_cog(src: Path, dst: Path, *, resampling: str, overwrite: bool) -> None:
    """Translate GTiff to COG using GDAL translate (API or CLI)."""
    # Prefer GDAL Python API if available and build supports COG
    if _HAS_GDAL:
        try:
            # Some GDAL builds accept "COG", others need gdal.Translate with creation options
            translate_opts = gdal.TranslateOptions(
                format="COG",
                creationOptions=[
                    "NUM_THREADS=ALL_CPUS",
                    f"RESAMPLING={resampling}",
                    "LEVEL=7",
                    "COMPRESS=DEFLATE",
                    "PREDICTOR=2",
                    "OVERVIEWS=IGNORE_EXISTING",
                ],
            )
            gdal.Translate(str(dst), str(src), options=translate_opts)
            return
        except Exception:
            # Fall back to CLI
            pass

    # CLI fallback
    gdal_translate = _which("gdal_translate")
    if not gdal_translate:
        raise RuntimeError("gdal_translate not found (required for COG fallback)")

    args = [
        gdal_translate,
        "-of", "COG",
        "-co", "NUM_THREADS=ALL_CPUS",
        "-co", f"RESAMPLING={resampling}",
        "-co", "LEVEL=7",
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=2",
        "-co", "OVERVIEWS=IGNORE_EXISTING",
        str(src),
        str(dst),
    ]
    if not overwrite and Path(dst).exists():
        # Respect overwrite off: write to tmp and move if not exists (race-safe enough for local runs)
        tmp = dst.with_suffix(".cog.tmp.tif")
        args[-1] = str(tmp)
        subprocess.run(args, check=True)
        tmp.replace(dst)
    else:
        subprocess.run(args, check=True)


# --------------------------
# CLI fallback implementations
# --------------------------

def _hillshade_cli(task: Task) -> None:
    """Use gdaldem and possibly gdal_translate/gdaladdo for COG."""
    gdaldem = _which("gdaldem")
    if not gdaldem:
        raise RuntimeError("gdaldem not found on PATH and GDAL Python bindings unavailable.")

    tmp = Path(task.dst).with_suffix(".tmp.tif") if task.cog else Path(task.dst)

    args = [
        gdaldem, "hillshade",
        "-az", str(task.azimuth),
        "-alt", str(task.altitude),
        "-z", str(task.zfactor),
    ]
    if task.scale is not None:
        args += ["-s", str(task.scale)]
    if task.multidir:
        args += ["-multidirectional"]
    if task.alg:
        args += ["-alg", task.alg]

    args += [task.src, str(tmp)]
    subprocess.run(args, check=True)

    if task.cog:
        _to_cog(tmp, Path(task.dst), resampling=task.resampling, overwrite=task.overwrite)
        if tmp.exists():
            tmp.unlink()


# --------------------------
# Runner
# --------------------------

def _make_one(task: Task) -> Result:
    t0 = time.time()
    src_p = Path(task.src)
    dst_p = Path(task.dst)
    dst_p.parent.mkdir(parents=True, exist_ok=True)
    params = {
        "azimuth": task.azimuth,
        "altitude": task.altitude,
        "zfactor": task.zfactor,
        "scale": task.scale,
        "multidir": task.multidir,
        "alg": task.alg,
        "cog": task.cog,
        "resampling": task.resampling,
    }

    # Idempotency shortcut
    if dst_p.exists() and not task.overwrite:
        try:
            return Result(
                src=str(src_p),
                dst=str(dst_p),
                ok=True,
                duration_s=time.time() - t0,
                src_sha256=_sha256(src_p),
                dst_sha256=_sha256(dst_p),
                cog=task.cog,
                params=params,
            )
        except Exception:
            # fall through to recompute
            pass

    try:
        if _HAS_GDAL:
            _hillshade_gdal_api(task)
        else:
            _hillshade_cli(task)

        res = Result(
            src=str(src_p),
            dst=str(dst_p),
            ok=True,
            duration_s=time.time() - t0,
            src_sha256=_sha256(src_p),
            dst_sha256=_sha256(dst_p),
            cog=task.cog,
            params=params,
        )
        # Sidecar hashes
        (dst_p.with_suffix(dst_p.suffix + ".sha256")).write_text(res.dst_sha256 + "\n", encoding="utf-8")
        return res
    except subprocess.CalledProcessError as e:
        return Result(str(src_p), str(dst_p), False, time.time() - t0, error=f"Subprocess: {e}", cog=task.cog, params=params)
    except Exception as e:
        return Result(str(src_p), str(dst_p), False, time.time() - t0, error=f"{type(e).__name__}: {e}", cog=task.cog, params=params)


def _build_tasks(
    inputs: Sequence[str],
    dest_dir: Path,
    *,
    suffix: str,
    cog: bool,
    azimuth: float,
    altitude: float,
    zfactor: float,
    scale: Optional[float],
    multidir: bool,
    alg: str,
    resampling: str,
    overwrite: bool,
) -> List[Task]:
    tasks: List[Task] = []
    for src in _iter_paths(inputs):
        out_name = src.stem + suffix + ".tif"
        dst = dest_dir / out_name
        tasks.append(Task(
            src=str(src),
            dst=str(dst),
            cog=cog,
            azimuth=azimuth,
            altitude=altitude,
            zfactor=zfactor,
            scale=scale,
            multidir=multidir,
            alg=alg,
            resampling=resampling,
            overwrite=overwrite,
        ))
    return tasks


def _write_manifest(results: List[Result], manifest: Path, argv: Sequence[str]) -> None:
    manifest.parent.mkdir(parents=True, exist_ok=True)
    obj = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "argv": list(argv),
        "entries": [asdict(r) for r in results],
    }
    with manifest.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


# --------------------------
# CLI
# --------------------------

def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="make_hillshade.py",
        description="Generate hillshade rasters from DEM GeoTIFFs (GDAL API preferred; CLI fallback).",
    )
    ap.add_argument("inputs", nargs="+", help="DEM files, directories, or globs (e.g., data/raw/**/*.tif)")
    ap.add_argument("--dest", type=Path, default=Path("data/processed/hillshade"), help="Output directory.")
    ap.add_argument("--suffix", type=str, default="_hillshade", help="Suffix for output filename (default: _hillshade)")
    ap.add_argument("--jobs", type=int, default=4, help="Parallel workers (default: 4)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")

    # Lighting / algorithm
    ap.add_argument("--azimuth", type=float, default=315.0, help="Light azimuth in degrees (default: 315)")
    ap.add_argument("--altitude", type=float, default=45.0, help="Light altitude in degrees (default: 45)")
    ap.add_argument("--zfactor", type=float, default=1.0, help="Vertical scaling factor (default: 1.0)")
    ap.add_argument("--scale", type=float, default=None, help="Scale: number of pixels per elevation unit (gdaldem -s)")
    ap.add_argument("--multidir", action="store_true", help="Use multi-directional hillshade")
    ap.add_argument("--alg", type=str, default="Horn", help="Slope algorithm (Horn|ZevenbergenThorne)")

    # Output formatting / COG
    ap.add_argument("--cog", action="store_true", help="Write Cloud-Optimized GeoTIFFs (COG)")
    ap.add_argument("--resampling", type=str, default="NEAREST", help="COG resampling (NEAREST|BILINEAR|CUBIC|...)")
    ap.add_argument("--manifest", type=Path, default=Path("data/processed/hillshade/manifest.hillshade.json"), help="Manifest JSON output")

    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)

    # Plan tasks
    tasks = _build_tasks(
        inputs=args.inputs,
        dest_dir=args.dest,
        suffix=args.suffix,
        cog=bool(args.cog),
        azimuth=float(args.azimuth),
        altitude=float(args.altitude),
        zfactor=float(args.zfactor),
        scale=(None if args.scale is None else float(args.scale)),
        multidir=bool(args.multidir),
        alg=str(args.alg),
        resampling=str(args.resampling).upper(),
        overwrite=bool(args.overwrite),
    )
    if not tasks:
        print("[WARN] No input DEMs found.", file=sys.stderr)
        return 1

    print(f"[INFO] GDAL bindings: {'YES' if _HAS_GDAL else 'NO'}; CLI fallback: {'YES' if _which('gdaldem') else 'NO'}")
    if not _HAS_GDAL and not _which("gdaldem"):
        print("[ERROR] Neither GDAL Python bindings nor gdaldem CLI found. Install GDAL.", file=sys.stderr)
        return 2

    # Run
    results: List[Result] = []
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=max(1, int(args.jobs))) as ex:
        futs = [ex.submit(_make_one, t) for t in tasks]
        for fut in cf.as_completed(futs):
            res = fut.result()
            results.append(res)
            status = "OK" if res.ok else "FAIL"
            print(f"[{status}] {Path(res.dst).name}  ({res.duration_s:.2f}s)")
            if res.error:
                print(f"       {res.error}", file=sys.stderr)

    # Manifest + summary
    _write_manifest(results, args.manifest, sys.argv)
    ok = sum(1 for r in results if r.ok)
    bad = len(results) - ok
    print(f"[RESULT] {ok} succeeded, {bad} failed in {time.time() - t0:.2f}s")
    return 0 if bad == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
