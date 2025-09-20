#!/usr/bin/env python3
# scripts/derive_terrain.py
"""
Derive hillshade / slope / aspect from DEM GeoTIFFs (COGs fine).
- Prefers GDAL Python API; falls back to gdaldem/gdal_translate.
- Parallel, idempotent, reproducible (SHA256 + manifest).
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import math
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

def _which(cmd: str) -> Optional[str]:
    from shutil import which
    return which(cmd)

def _sha256(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def _iter_dems(inputs: Sequence[str]) -> Iterable[Path]:
    """
    Expand folders/globs/files into a sorted list of .tif/.tiff DEM paths.
    """
    seen = set()
    for pat in inputs:
        p = Path(pat)
        if p.is_dir():
            it = list(p.rglob("*.tif")) + list(p.rglob("*.tiff"))
        elif any(ch in pat for ch in "*?[]"):
            it = list(Path().glob(pat))
        else:
            it = [p] if p.is_file() else []
        for f in it:
            if f.is_file() and f.suffix.lower() in (".tif", ".tiff"):
                if f not in seen:
                    seen.add(f)
                    yield f

def _human(n: float) -> str:
    if n <= 0:
        return "0B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(n, 1024)))
    i = max(0, min(i, len(units) - 1))
    return f"{n / (1024 ** i):.2f}{units[i]}"

def _log(msg: str) -> None:
    print(msg, file=sys.stderr)

# --------------------------
# Tasks / Results
# --------------------------

@dataclass
class DeriveParams:
    azimuth: float
    altitude: float
    zfactor: float
    scale: Optional[float]
    multidir: bool
    alg: str
    cog: bool
    resampling: str
    overwrite: bool

@dataclass
class Task:
    dem: str
    outdir: str
    params: DeriveParams

@dataclass
class OneOut:
    path: str
    ok: bool
    sha256: Optional[str] = None
    error: Optional[str] = None

@dataclass
class Result:
    dem: str
    hillshade: OneOut
    slope: OneOut
    aspect: OneOut
    duration_s: float

# --------------------------
# GDAL API implementations
# --------------------------

def _demproc_api(dem: Path, product: str, dst_tmp: Path, params: DeriveParams) -> None:
    """
    product in {"hillshade","slope","aspect"}
    """
    src_ds = gdal.Open(str(dem), gdal.GA_ReadOnly)
    if src_ds is None:
        raise RuntimeError("GDAL failed to open source DEM")

    if product == "hillshade":
        opts = gdal.DEMProcessingOptions(
            azimuth=params.azimuth,
            altitude=params.altitude,
            zFactor=params.zfactor,
            scale=(params.scale if params.scale is not None else 0.0),
            multiDirectional=params.multidir,
            algorithm=params.alg if params.alg else None,
            computeEdges=True,
        )
    elif product == "slope":
        opts = gdal.DEMProcessingOptions(
            zFactor=params.zfactor,
            scale=(params.scale if params.scale is not None else 0.0),
            slopeFormat=None,  # default: degrees
            algorithm=params.alg if params.alg else None,
            computeEdges=True,
        )
    elif product == "aspect":
        opts = gdal.DEMProcessingOptions(
            zFactor=params.zfactor,
            scale=(params.scale if params.scale is not None else 0.0),
            algorithm=params.alg if params.alg else None,
            computeEdges=True,
        )
    else:
        raise ValueError(f"Unsupported product: {product}")

    out = gdal.DEMProcessing(str(dst_tmp), src_ds, product, options=opts)
    if out is None:
        raise RuntimeError(f"DEMProcessing returned None for {product}")

def _to_cog(src: Path, dst: Path, *, resampling: str, overwrite: bool) -> None:
    """
    Convert GTiff -> COG (GDAL API preferred, else gdal_translate).
    """
    if _HAS_GDAL:
        try:
            opts = gdal.TranslateOptions(
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
            gdal.Translate(str(dst), str(src), options=opts)
            return
        except Exception:
            pass

    gt = _which("gdal_translate")
    if not gt:
        raise RuntimeError("gdal_translate not found for COG fallback")
    args = [
        gt, "-of", "COG",
        "-co", "NUM_THREADS=ALL_CPUS",
        "-co", f"RESAMPLING={resampling}",
        "-co", "LEVEL=7",
        "-co", "COMPRESS=DEFLATE",
        "-co", "PREDICTOR=2",
        "-co", "OVERVIEWS=IGNORE_EXISTING",
        str(src), str(dst),
    ]
    if not overwrite and dst.exists():
        tmp2 = dst.with_suffix(".cog.tmp.tif")
        args[-1] = str(tmp2)
        subprocess.run(args, check=True)
        tmp2.replace(dst)
    else:
        subprocess.run(args, check=True)

# --------------------------
# CLI fallback implementations
# --------------------------

def _demproc_cli(dem: Path, product: str, dst_tmp: Path, params: DeriveParams) -> None:
    """
    Use gdaldem to compute product.
    """
    gdaldem = _which("gdaldem")
    if not gdaldem:
        raise RuntimeError("gdaldem not found and GDAL bindings unavailable")

    args = [gdaldem, product]

    if product == "hillshade":
        args += ["-az", str(params.azimuth), "-alt", str(params.altitude), "-z", str(params.zfactor)]
        if params.scale is not None:
            args += ["-s", str(params.scale)]
        if params.multidir:
            args += ["-multidirectional"]
        if params.alg:
            args += ["-alg", params.alg]
        args += ["-compute_edges", str(dem), str(dst_tmp)]

    elif product == "slope":
        args += ["-z", str(params.zfactor)]
        if params.scale is not None:
            args += ["-s", str(params.scale)]
        if params.alg:
            args += ["-alg", params.alg]
        args += ["-compute_edges", str(dem), str(dst_tmp)]

    elif product == "aspect":
        args += ["-z", str(params.zfactor)]
        if params.scale is not None:
            args += ["-s", str(params.scale)]
        if params.alg:
            args += ["-alg", params.alg]
        args += ["-compute_edges", str(dem), str(dst_tmp)]
    else:
        raise ValueError(f"Unsupported product: {product}")

    subprocess.run(args, check=True)

# --------------------------
# One DEM pipeline
# --------------------------

def _derive_one(dem: Path, outdir: Path, params: DeriveParams) -> Result:
    t0 = time.time()
    outdir.mkdir(parents=True, exist_ok=True)

    base = dem.stem
    # temporary non-COG GTiffs first
    hill_tmp = outdir / f"{base}_hillshade.tmp.tif"
    slp_tmp  = outdir / f"{base}_slope.tmp.tif"
    asp_tmp  = outdir / f"{base}_aspect.tmp.tif"

    # final outputs
    hill = outdir / f"{base}_hillshade.tif"
    slp  = outdir / f"{base}_slope.tif"
    asp  = outdir / f"{base}_aspect.tif"

    # Idempotency: if all three exist and no overwrite, short-circuit
    if (hill.exists() and slp.exists() and asp.exists()) and not params.overwrite:
        return Result(
            dem=str(dem),
            hillshade=OneOut(str(hill), True, _sha256(hill)),
            slope=OneOut(str(slp), True, _sha256(slp)),
            aspect=OneOut(str(asp), True, _sha256(asp)),
            duration_s=time.time() - t0,
        )

    def _compute(product: str, tmp: Path, final: Path) -> OneOut:
        try:
            if _HAS_GDAL:
                _demproc_api(dem, product, tmp, params)
            else:
                _demproc_cli(dem, product, tmp, params)

            if params.cog:
                _to_cog(tmp, final, resampling=params.resampling, overwrite=params.overwrite)
                if tmp.exists():
                    tmp.unlink()
            else:
                # move tmp -> final
                if final.exists() and not params.overwrite:
                    tmp.unlink(missing_ok=True)  # nothing to do
                else:
                    tmp.replace(final)

            sh = _sha256(final)
            (final.with_suffix(final.suffix + ".sha256")).write_text(sh + "\n", encoding="utf-8")
            return OneOut(str(final), True, sh)
        except subprocess.CalledProcessError as e:
            return OneOut(str(final), False, None, f"Subprocess: {e}")
        except Exception as e:
            return OneOut(str(final), False, None, f"{type(e).__name__}: {e}")

    h = _compute("hillshade", hill_tmp, hill)
    s = _compute("slope",     slp_tmp,  slp)
    a = _compute("aspect",    asp_tmp,  asp)

    return Result(
        dem=str(dem),
        hillshade=h,
        slope=s,
        aspect=a,
        duration_s=time.time() - t0,
    )

# --------------------------
# Manifest
# --------------------------

def _write_manifest(results: List[Result], manifest: Path, argv: Sequence[str]) -> None:
    manifest.parent.mkdir(parents=True, exist_ok=True)
    obj = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "argv": list(argv),
        "entries": [asdict(r) for r in results],
        "environment": {
            "gdal_bindings": _HAS_GDAL,
            "gdaldem_cli": bool(_which("gdaldem")),
            "gdal_translate_cli": bool(_which("gdal_translate")),
        },
    }
    with manifest.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")

# --------------------------
# CLI
# --------------------------

def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="derive_terrain.py",
        description="Derive hillshade/slope/aspect from DEM GeoTIFFs (COGs fine).",
    )
    ap.add_argument("inputs", nargs="+", help="DEM files, folders, or globs (e.g., data/raw/**/*.tif)")
    ap.add_argument("--out", type=Path, default=Path("data/processed/terrain"), help="Output folder")
    ap.add_argument("--jobs", type=int, default=4, help="Parallel workers (default: 4)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")

    # Lighting / algorithm (hillshade)
    ap.add_argument("--azimuth", type=float, default=315.0, help="Light azimuth (default: 315)")
    ap.add_argument("--altitude", type=float, default=45.0, help="Light altitude (default: 45)")
    ap.add_argument("--zfactor", type=float, default=1.0, help="Vertical exaggeration factor")
    ap.add_argument("--scale", type=float, default=None, help="Scale (pixels per elevation unit)")

    ap.add_argument("--multidir", action="store_true", help="Multi-directional hillshade")
    ap.add_argument("--alg", type=str, default="Horn", help="Algorithm (Horn|ZevenbergenThorne)")

    # Output formatting / COG
    ap.add_argument("--cog", action="store_true", help="Write Cloud-Optimized GeoTIFFs")
    ap.add_argument("--resampling", type=str, default="NEAREST", help="COG resampling (NEAREST|BILINEAR|CUBIC|...)")

    # Manifest
    ap.add_argument("--manifest", type=Path, default=Path("data/processed/terrain/manifest.derive_terrain.json"),
                    help="Manifest JSON output")

    return ap.parse_args(argv)

def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)

    dems = list(_iter_dems(args.inputs))
    if not dems:
        _log("[WARN] No DEM files found.")
        return 1

    # Environment check
    _log(f"[INFO] GDAL bindings: {'YES' if _HAS_GDAL else 'NO'}; "
         f"gdaldem: {'YES' if _which('gdaldem') else 'NO'}; "
         f"gdal_translate: {'YES' if _which('gdal_translate') else 'NO'}")
    if not _HAS_GDAL and not _which("gdaldem"):
        _log("[ERROR] Neither GDAL Python bindings nor gdaldem CLI found. Install GDAL.")
        return 2

    params = DeriveParams(
        azimuth=float(args.azimuth),
        altitude=float(args.altitude),
        zfactor=float(args.zfactor),
        scale=(None if args.scale is None else float(args.scale)),
        multidir=bool(args.multidir),
        alg=str(args.alg),
        cog=bool(args.cog),
        resampling=str(args.resampling).upper(),
        overwrite=bool(args.overwrite),
    )

    results: List[Result] = []
    t0 = time.time()
    outdir = args.out

    with cf.ThreadPoolExecutor(max_workers=max(1, int(args.jobs))) as ex:
        futs = [ex.submit(_derive_one, dem, outdir, params) for dem in dems]
        for fut in cf.as_completed(futs):
            res = fut.result()
            results.append(res)
            ok_h = "OK" if res.hillshade.ok else "FAIL"
            ok_s = "OK" if res.slope.ok else "FAIL"
            ok_a = "OK" if res.aspect.ok else "FAIL"
            _log(f"[{ok_h}/{ok_s}/{ok_a}] {Path(res.dem).name}  ({res.duration_s:.2f}s)")
            for x in (res.hillshade, res.slope, res.aspect):
                if not x.ok and x.error:
                    _log(f"   -> {Path(x.path).name}: {x.error}")

    _write_manifest(results, args.manifest, sys.argv)

    failed = sum((not r.hillshade.ok) + (not r.slope.ok) + (not r.aspect.ok) for r in results)
    _log(f"[RESULT] processed={len(results)}  failures={failed}  elapsed={time.time() - t0:.2f}s")
    return 0 if failed == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
