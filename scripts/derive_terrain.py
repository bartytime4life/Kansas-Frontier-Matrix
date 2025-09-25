#!/usr/bin/env python3
# scripts/derive_terrain.py
# -*- coding: utf-8 -*-
"""
Derive hillshade / slope / aspect from DEM GeoTIFFs (COGs fine).
- Prefers GDAL Python API; falls back to gdaldem/gdal_translate.
- Parallel, idempotent, reproducible (SHA256 + manifest).
- Smart defaults for scale (meters vs degrees), nodata handling, and COG options.
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
    from osgeo import gdal, osr  # type: ignore
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

def _sha256(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

def _iter_dems(inputs: Sequence[str]) -> List[Path]:
    """
    Expand folders/globs/files into a sorted list of .tif/.tiff DEM paths.
    """
    out: List[Path] = []
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
                if f.resolve() not in seen:
                    seen.add(f.resolve())
                    out.append(f)
    return sorted(out, key=lambda x: x.as_posix())

def _human(n: float) -> str:
    if n <= 0:
        return "0B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(n, 1024)))
    i = max(0, min(i, len(units) - 1))
    return f"{n / (1024 ** i):.2f}{units[i]}"

def _log(msg: str) -> None:
    print(msg, file=sys.stderr)

def _atomic_move(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    os.replace(src, dst)

# --------------------------
# Product sets
# --------------------------
ALL_PRODUCTS = ("hillshade", "slope", "aspect")

def _parse_products(s: str) -> List[str]:
    want = []
    for tok in (x.strip().lower() for x in s.split(",")):
        if not tok:
            continue
        if tok not in ALL_PRODUCTS:
            raise argparse.ArgumentTypeError(f"Unknown product '{tok}'. Choose from: {', '.join(ALL_PRODUCTS)}")
        want.append(tok)
    return list(dict.fromkeys(want))  # dedupe, preserve order

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
    threads: str
    overwrite: bool
    src_nodata: Optional[float]
    dst_nodata: Optional[float]
    slope_percent: bool
    aspect_trig: bool
    aspect_zero_for_flat: bool

@dataclass
class Task:
    dem: str
    outdir: str
    params: DeriveParams
    products: List[str]

@dataclass
class OneOut:
    path: str
    ok: bool
    sha256: Optional[str] = None
    size: Optional[int] = None
    error: Optional[str] = None

@dataclass
class Result:
    dem: str
    outputs: dict
    duration_s: float

# --------------------------
# Scale / CRS helpers
# --------------------------
def _detect_scale_for_dem(dem: Path, fallback: Optional[float]) -> Optional[float]:
    """
    Return a reasonable --scale default:
      - 1.0 for projected meters
      - ~111120 for degrees (WGS84-ish)
      - fallback if detection fails (may be None)
    """
    if fallback is not None:
        return fallback
    try:
        if _HAS_GDAL:
            ds = gdal.Open(str(dem), gdal.GA_ReadOnly)
            if ds is None:
                return fallback
            wkt = ds.GetProjection()
            sref = osr.SpatialReference()
            if wkt and sref.ImportFromWkt(wkt) == 0:
                if sref.IsProjected():
                    # Check linear units: assume meters if close to 1
                    lin_units = sref.GetLinearUnits() or 1.0
                    if 0.9 <= lin_units <= 1.1:
                        return 1.0
                    # If in feet, approximate meters-per-unit; leave scale=1 (assume elevations match units)
                    return 1.0
                if sref.IsGeographic():
                    return 111120.0
        # Fallback heuristic: filename hint
        name = dem.name.lower()
        if any(k in name for k in ("_wgs84", "_4326", "epsg4326")):
            return 111120.0
        return 1.0
    except Exception:
        return fallback

# --------------------------
# GDAL API implementations
# --------------------------
def _demproc_api(dem: Path, product: str, dst_tmp: Path, p: DeriveParams) -> None:
    src_ds = gdal.Open(str(dem), gdal.GA_ReadOnly)
    if src_ds is None:
        raise RuntimeError("GDAL failed to open source DEM")

    # nodata handling via warp options inside DEMProcessing is limited;
    # rely on -compute_edges and later set dst nodata via Translate to COG
    kwargs = dict(
        zFactor=p.zfactor,
        scale=(p.scale if p.scale is not None else 0.0),
        algorithm=(p.alg if p.alg else None),
        computeEdges=True,
    )

    if product == "hillshade":
        opts = gdal.DEMProcessingOptions(
            azimuth=p.azimuth, altitude=p.altitude,
            multiDirectional=p.multidir,
            **kwargs
        )
        mode = "hillshade"
    elif product == "slope":
        opts = gdal.DEMProcessingOptions(
            slopeFormat=("percent" if p.slope_percent else None),
            **kwargs
        )
        mode = "slope"
    elif product == "aspect":
        opts = gdal.DEMProcessingOptions(
            trigonometric=p.aspect_trig,
            zeroForFlat=p.aspect_zero_for_flat,
            **kwargs
        )
        mode = "aspect"
    else:
        raise ValueError(f"Unsupported product: {product}")

    out = gdal.DEMProcessing(str(dst_tmp), src_ds, mode, options=opts)
    if out is None:
        raise RuntimeError(f"DEMProcessing returned None for {product}")

def _to_cog(src: Path, dst: Path, *, resampling: str, threads: str, dst_nodata: Optional[float], overwrite: bool) -> None:
    """
    Convert GTiff -> COG (GDAL API preferred, else gdal_translate).
    """
    creation = [
        f"NUM_THREADS={threads}",
        f"RESAMPLING={resampling}",
        "OVERVIEWS=AUTO",
        "OVERVIEW_RESAMPLING=AVERAGE",
        "COMPRESS=DEFLATE",
        "PREDICTOR=2",
        "ZLEVEL=6",
        "BLOCKSIZE=512",
        "BIGTIFF=IF_SAFER",
    ]
    if _HAS_GDAL:
        try:
            translate_opts = gdal.TranslateOptions(
                format="COG",
                creationOptions=creation,
                noData=dst_nodata if dst_nodata is not None else None,
            )
            gdal.Translate(str(dst), str(src), options=translate_opts)
            return
        except Exception:
            pass

    gt = _which("gdal_translate")
    if not gt:
        raise RuntimeError("gdal_translate not found for COG fallback")
    args = [gt, str(src), str(dst), "-of", "COG"]
    for co in creation:
        args += ["-co", co]
    if dst_nodata is not None:
        args += ["-a_nodata", str(dst_nodata)]

    if not overwrite and dst.exists():
        tmp2 = dst.with_suffix(".cog.tmp.tif")
        args[-1] = str(tmp2)
        subprocess.run(args, check=True, text=True)
        _atomic_move(tmp2, dst)
    else:
        subprocess.run(args, check=True, text=True)

# --------------------------
# CLI fallback implementations
# --------------------------
def _demproc_cli(dem: Path, product: str, dst_tmp: Path, p: DeriveParams) -> None:
    gdaldem = _which("gdaldem")
    if not gdaldem:
        raise RuntimeError("gdaldem not found and GDAL bindings unavailable")

    args = [gdaldem, product]
    if product == "hillshade":
        args += ["-az", str(p.azimuth), "-alt", str(p.altitude), "-z", str(p.zfactor)]
        if p.scale is not None: args += ["-s", str(p.scale)]
        if p.multidir: args.append("-multidirectional")
        if p.alg: args += ["-alg", p.alg]
    elif product == "slope":
        args += ["-z", str(p.zfactor)]
        if p.scale is not None: args += ["-s", str(p.scale)]
        if p.slope_percent: args.append("-p")
        if p.alg: args += ["-alg", p.alg]
    elif product == "aspect":
        if p.aspect_trig: args.append("-trigonometric")
        if p.aspect_zero_for_flat: args.append("-zero_for_flat")
        args += ["-z", str(p.zfactor)]
        if p.scale is not None: args += ["-s", str(p.scale)]
        if p.alg: args += ["-alg", p.alg]
    else:
        raise ValueError(f"Unsupported product: {product}")
    args += ["-compute_edges", str(dem), str(dst_tmp)]
    subprocess.run(args, check=True, text=True)

# --------------------------
# Hooks to repo (meta/validate)
# --------------------------
def _try_meta(output: Path, dem: Path, stage: str, params: DeriveParams) -> None:
    wm = Path(__file__).with_name("write_meta.py")
    if not wm.exists():
        return
    try:
        extras = [
            f"stage={stage}",
            f"azimuth={params.azimuth}",
            f"altitude={params.altitude}",
            f"zfactor={params.zfactor}",
            f"scale={'' if params.scale is None else params.scale}",
            f"multidir={str(params.multidir).lower()}",
            f"alg={params.alg or 'default'}",
            f"slope_percent={str(params.slope_percent).lower()}",
            f"aspect_trig={str(params.aspect_trig).lower()}",
            f"aspect_zero_for_flat={str(params.aspect_zero_for_flat).lower()}",
        ]
        subprocess.run([sys.executable, str(wm), str(output), "--inputs", str(dem), "--extra", *extras],
                       check=True, text=True)
    except Exception as e:
        _log(f"[WARN] meta sidecar skipped for {output.name}: {e}")

def _try_validate_cog(output: Path) -> None:
    val = Path(__file__).with_name("validate_cogs.py")
    if not val.exists() or output.suffix.lower() not in {".tif", ".tiff"}:
        return
    try:
        subprocess.run([sys.executable, str(val), str(output.parent), "--pattern", output.name, "--quiet"],
                       check=False, text=True)
    except Exception as e:
        _log(f"[WARN] COG validate skipped for {output.name}: {e}")

# --------------------------
# One DEM pipeline
# --------------------------
def _derive_one(dem: Path, outdir: Path, products: List[str], params: DeriveParams) -> Result:
    t0 = time.time()
    outdir.mkdir(parents=True, exist_ok=True)

    # Smart default for scale if not provided explicitly
    scale = _detect_scale_for_dem(dem, params.scale)
    p = params if scale == params.scale else DeriveParams(**{**params.__dict__, "scale": scale})

    base = dem.stem
    outs: dict = {}

    for product in products:
        tmp = outdir / f"{base}_{product}.tmp.tif"
        final = outdir / f"{base}_{product}.tif"

        # Idempotency per-product
        if final.exists() and not p.overwrite:
            outs[product] = OneOut(str(final), True, _sha256(final), final.stat().st_size)
            continue

        try:
            if _HAS_GDAL:
                _demproc_api(dem, product, tmp, p)
            else:
                _demproc_cli(dem, product, tmp, p)

            # If user wants COG, translate; else move tmp → final
            if p.cog:
                _to_cog(tmp, final, resampling=p.resampling, threads=p.threads,
                        dst_nodata=p.dst_nodata, overwrite=p.overwrite)
                tmp.unlink(missing_ok=True)
            else:
                # Set explicit dst nodata when asked (using gdal_translate -a_nodata)
                if p.dst_nodata is not None:
                    gt = _which("gdal_translate")
                    if gt:
                        tmp2 = tmp.with_suffix(".nd.tif")
                        subprocess.run([gt, "-a_nodata", str(p.dst_nodata), str(tmp), str(tmp2)],
                                       check=True, text=True)
                        tmp.unlink(missing_ok=True)
                        tmp = tmp2
                _atomic_move(tmp, final)

            sh = _sha256(final)
            (final.with_suffix(final.suffix + ".sha256")).write_text(sh + "\n", encoding="utf-8")
            outs[product] = OneOut(str(final), True, sh, final.stat().st_size)
            _try_meta(final, dem, product, p)
            if p.cog:
                _try_validate_cog(final)
        except subprocess.CalledProcessError as e:
            outs[product] = OneOut(str(final), False, None, None, f"Subprocess: {e}")
        except Exception as e:
            outs[product] = OneOut(str(final), False, None, None, f"{type(e).__name__}: {e}")

    return Result(
        dem=str(dem),
        outputs=outs,
        duration_s=time.time() - t0,
    )

# --------------------------
# Manifest
# --------------------------
def _write_manifest(results: List[Result], manifest: Path, argv: Sequence[str]) -> None:
    manifest.parent.mkdir(parents=True, exist_ok=True)
    env = {
        "gdal_bindings": _HAS_GDAL,
        "gdaldem_cli": bool(_which("gdaldem")),
        "gdal_translate_cli": bool(_which("gdal_translate")),
    }
    obj = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "argv": list(argv),
        "environment": env,
        "entries": [asdict(r) for r in results],
    }
    manifest.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

# --------------------------
# CLI
# --------------------------
def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="derive_terrain.py",
        description="Derive hillshade/slope/aspect from DEM GeoTIFFs (COGs fine).",
    )
    ap.add_argument("inputs", nargs="+", help="DEM files, folders, or globs (e.g., data/raw/**/*.tif)")
    ap.add_argument("--out", type=Path, default=Path("data/processed/terrain"),
                    help="Output folder (default: data/processed/terrain)")
    ap.add_argument("--products", type=_parse_products, default=ALL_PRODUCTS,
                    help="Comma-separated products to build (hillshade,slope,aspect)")
    ap.add_argument("--jobs", type=int, default=4, help="Parallel workers (default: 4)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")

    # Lighting / algorithm (hillshade)
    ap.add_argument("--azimuth", type=float, default=315.0, help="Hillshade light azimuth (default: 315)")
    ap.add_argument("--altitude", type=float, default=45.0, help="Hillshade light altitude (default: 45)")
    ap.add_argument("--zfactor", type=float, default=1.0, help="Vertical exaggeration factor")
    ap.add_argument("--scale", type=float, default=None,
                    help="Ground units per pixel: 1 for meters; ~111120 for degrees (auto-detected if omitted)")
    ap.add_argument("--multidir", action="store_true", help="Multi-directional hillshade")
    ap.add_argument("--alg", type=str, default="Horn", help="Algorithm (Horn|ZevenbergenThorne)")

    # Output formatting / COG
    ap.add_argument("--cog", action="store_true", help="Write Cloud-Optimized GeoTIFFs")
    ap.add_argument("--resampling", type=str, default="AVERAGE",
                    choices=["NEAREST","AVERAGE","GAUSS","CUBIC","CUBICSPLINE","LANCZOS","MODE","RMS","BILINEAR","MIN","MAX","MED"],
                    help="Overview resampling when building COGs")
    ap.add_argument("--threads", default="ALL_CPUS", help='NUM_THREADS for COG creation (e.g., "ALL_CPUS" or "8")')

    # Nodata + variants
    ap.add_argument("--src-nodata", type=float, default=None, help="Source nodata (best-effort hint)")
    ap.add_argument("--dst-nodata", type=float, default=None, help="Output nodata (sets COG nodata)")
    ap.add_argument("--slope-percent", action="store_true", help="Slope in percent (instead of degrees)")
    ap.add_argument("--aspect-trigonometric", action="store_true", help="Aspect trigonometric (0°=East, CCW)")
    ap.add_argument("--aspect-zero-for-flat", action="store_true", help="Aspect: output 0 for flat")

    # Manifest
    ap.add_argument("--manifest", type=Path, default=Path("data/processed/terrain/manifest.derive_terrain.json"),
                    help="Manifest JSON output")
    return ap.parse_args(argv)

def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)

    dems = _iter_dems(args.inputs)
    if not dems:
        _log("[WARN] No DEM files found.")
        return 1

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
        threads=str(args.threads),
        overwrite=bool(args.overwrite),
        src_nodata=(None if args.src_nodata is None else float(args.src_nodata)),
        dst_nodata=(None if args.dst_nodata is None else float(args.dst_nodata)),
        slope_percent=bool(args.slope_percent),
        aspect_trig=bool(args.aspect_trigonometric),
        aspect_zero_for_flat=bool(args.aspect_zero_for_flat),
    )

    results: List[Result] = []
    t0 = time.time()
    outdir = args.out

    with cf.ThreadPoolExecutor(max_workers=max(1, int(args.jobs))) as ex:
        futs = [ex.submit(_derive_one, dem, outdir, list(args.products), params) for dem in dems]
        for fut in cf.as_completed(futs):
            res = fut.result()
            results.append(res)
            flags = "/".join(f"{k}:{'OK' if v.ok else 'FAIL'}" for k, v in res.outputs.items())
            _log(f"[{flags}] {Path(res.dem).name}  ({res.duration_s:.2f}s)")
            for k, v in res.outputs.items():
                if not v.ok and v.error:
                    _log(f"   -> {k}: {Path(v.path).name}: {v.error}")

    _write_manifest(results, args.manifest, sys.argv)

    failed = sum(1 for r in results for v in r.outputs.values() if not v.ok)
    _log(f"[RESULT] processed={len(results)}  failures={failed}  elapsed={time.time() - t0:.2f}s")
    return 0 if failed == 0 else 3

if __name__ == "__main__":
    raise SystemExit(main())
