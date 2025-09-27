#!/usr/bin/env python3
# scripts/convert.py
# Kansas-Frontier-Matrix — raster/vector converter for web-ready artifacts (COG/GeoJSON)
# - Raster → COG (WGS84/EPSG:4326 by default), with internal tiling & overviews
# - Vector → GeoJSON (WGS84/EPSG:4326 by default)
# - Writes SHA256 sidecar for each output
#
# Usage examples:
#   Raster → COG:
#     python scripts/convert.py raster-to-cog data/raw/maps/soil_1967.tif data/cogs/overlays/soil_1967.tif
#     python scripts/convert.py raster-to-cog --dst-crs EPSG:4326 --web-optimized --overview-level 5 IN.tif OUT.tif
#
#   Vector → GeoJSON:
#     python scripts/convert.py vector-to-geojson data/raw/parcels_1930s.shp data/processed/parcels_1930s.json
#     python scripts/convert.py vector-to-geojson --dst-crs EPSG:4326 IN.gpkg:layername OUT.json
#
# Returns non-zero on failure.

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

import click
from tqdm import tqdm

# Raster stack
import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
from rio_cogeo.profiles import cog_profiles
from rio_cogeo.cogeo import cog_translate

# Vector stack
import fiona
from fiona.transform import transform_geom
from fiona.errors import DriverError


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sha256_sidecar(out_path: Path, digest: str) -> None:
    side = out_path.with_suffix(out_path.suffix + ".sha256")
    side.write_text(f"{digest}  {out_path.name}\n", encoding="utf-8")


def infer_overview_level(width: int, height: int) -> int:
    # Reasonable heuristic: build overviews until min dimension < 512
    # (you can override with --overview-level)
    levels = 0
    w, h = width, height
    while max(w, h) > 512:
        levels += 1
        w //= 2
        h //= 2
    return max(levels, 1)


def ensure_parent(out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)


# ----------------------------- Raster → COG ----------------------------- #

def _reproject_to_tmp(src: rasterio.io.DatasetReader, dst_crs: str) -> Tuple[str, dict]:
    """Reproject a raster to temp GTiff in memory-backed file (on disk path)."""
    transform, width, height = calculate_default_transform(
        src.crs, dst_crs, src.width, src.height, *src.bounds
    )
    kwargs = src.meta.copy()
    kwargs.update({
        "crs": dst_crs,
        "transform": transform,
        "width": width,
        "height": height,
        "driver": "GTiff",
        "tiled": True,
        "blockxsize": 512,
        "blockysize": 512,
        "compress": "DEFLATE",
        "predictor": 2 if kwargs.get("count", 1) == 1 else 3
    })

    tmp_path = str(Path(os.getenv("TMPDIR", "/tmp")) / f"_kfm_reproj_{os.getpid()}_{os.urandom(4).hex()}.tif")
    with rasterio.open(tmp_path, "w", **kwargs) as dst:
        for b in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, b),
                destination=rasterio.band(dst, b),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.bilinear,
            )
    return tmp_path, kwargs


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    """KFM converter: rasters→COG, vectors→GeoJSON (EPSG:4326), plus SHA256 sidecars."""
    pass


@cli.command("raster-to-cog")
@click.argument("src_raster", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("out_cog", type=click.Path(dir_okay=False, path_type=Path))
@click.option("--dst-crs", default="EPSG:4326", show_default=True, help="Target CRS for reprojection.")
@click.option("--web-optimized", is_flag=True, help="Use 'webp' COG profile (good for basemaps/overlays).")
@click.option("--overview-level", type=int, default=None, help="Number of overviews (auto if not set).")
@click.option("--nodata", type=float, default=None, help="Set NODATA value on output.")
@click.option("--resampling", type=click.Choice([e.name for e in Resampling]), default="bilinear", show_default=True)
def raster_to_cog_cmd(src_raster: Path, out_cog: Path, dst_crs: str,
                      web_optimized: bool, overview_level: Optional[int],
                      nodata: Optional[float], resampling: str):
    """Convert a raster to COG (Cloud-Optimized GeoTIFF)."""

    ensure_parent(out_cog)

    with rasterio.open(src_raster) as src:
        src_crs = src.crs.to_string() if src.crs else None
        # Reproject if needed
        if not src_crs or src_crs.upper() != dst_crs.upper():
            click.echo(f"[raster] Reprojecting {src_raster.name} from {src_crs} → {dst_crs}", err=True)
            reproj_path, reproj_meta = _reproject_to_tmp(src, dst_crs)
            reproj = rasterio.open(reproj_path)
            to_close = [reproj]
        else:
            reproj = src
            to_close = []

        try:
            # Choose COG profile
            profile_name = "webp" if web_optimized else "deflate"
            profile = cog_profiles.get(profile_name)

            # Overviews
            if overview_level is None:
                overview_level = infer_overview_level(reproj.width, reproj.height)

            # nodata
            nodata_value = nodata
            if nodata_value is None and reproj.nodata is not None:
                nodata_value = reproj.nodata

            # Translate to COG
            click.echo(f"[raster] Creating COG → {out_cog} (profile={profile_name}, overviews={overview_level})", err=True)
            cog_translate(
                reproj,
                str(out_cog),
                profile,
                nodata=nodata_value,
                overview_level=overview_level,
                overview_resampling=Resampling[resampling],
                web_optimized=False,  # we set internal tiling in profile; 'web_optimized' already covered by profile choice
                config={
                    "GDAL_TIFF_INTERNAL_MASK": "YES",
                    "GDAL_NUM_THREADS": "ALL_CPUS",
                },
            )
        finally:
            for ds in to_close:
                ds.close()
            # cleanup temp
            if to_close:
                Path(reproj.name).unlink(missing_ok=True)

    digest = sha256_file(out_cog)
    write_sha256_sidecar(out_cog, digest)
    click.echo(f"[raster] Done. SHA256={digest[:16]}…  {out_cog}")


# ----------------------------- Vector → GeoJSON ----------------------------- #

def _parse_ds_layer(path_or_layer: str) -> Tuple[str, Optional[str]]:
    """
    Accept 'file' or 'file:layer' syntax for multi-layer datasources (e.g., GPKG).
    Returns (ds_path, layer_name_or_None).
    """
    p = Path(path_or_layer)
    if p.exists():
        return str(p), None
    # try file:layer
    if ":" in path_or_layer:
        ds, lyr = path_or_layer.split(":", 1)
        if Path(ds).exists():
            return ds, lyr
    return path_or_layer, None


@cli.command("vector-to-geojson")
@click.argument("src_vector", type=str)
@click.argument("out_geojson", type=click.Path(dir_okay=False, path_type=Path))
@click.option("--dst-crs", default="EPSG:4326", show_default=True, help="Target CRS for reprojection.")
@click.option("--indent", type=int, default=2, show_default=True, help="Pretty-print JSON indent.")
def vector_to_geojson_cmd(src_vector: str, out_geojson: Path, dst_crs: str, indent: int):
    """Convert vector data (SHP/GPKG/etc.) to GeoJSON (EPSG:4326 by default)."""

    ds_path, layer = _parse_ds_layer(src_vector)
    ensure_parent(out_geojson)

    try:
        with fiona.open(ds_path, layer=layer) as src:
            src_crs = src.crs_wkt or src.crs
            click.echo(f"[vector] Reading {ds_path}{(':'+layer) if layer else ''} (features={len(src)})", err=True)

            # Prepare output schema & CRS
            out_driver = "GeoJSON"
            out_crs = dst_crs

            with fiona.Env():
                with fiona.open(
                    out_geojson,
                    "w",
                    driver=out_driver,
                    crs=out_crs,
                    schema=src.schema,
                ) as dst:
                    for feat in tqdm(src, desc="[vector] Reprojecting"):
                        geom = feat.get("geometry")
                        if geom:
                            geom = transform_geom(src_crs, out_crs, geom, antimeridian_cutting=True, precision=9)
                        feat["geometry"] = geom
                        dst.write(feat)

    except DriverError as e:
        click.echo(f"[vector] ERROR: {e}", err=True)
        sys.exit(2)

    # Optionally, compact/pretty JSON rewrite (Fiona writes minimal)
    try:
        data = json.loads(out_geojson.read_text(encoding="utf-8"))
        out_geojson.write_text(json.dumps(data, ensure_ascii=False, indent=indent), encoding="utf-8")
    except Exception:
        pass

    digest = sha256_file(out_geojson)
    write_sha256_sidecar(out_geojson, digest)
    click.echo(f"[vector] Done. SHA256={digest[:16]}…  {out_geojson}")


if __name__ == "__main__":
    cli()
