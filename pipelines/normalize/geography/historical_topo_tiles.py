"""Deterministically prepare EPSG:3857 PNG tiles from a captured USGS GeoTIFF.

This transformation does not publish or approve the output. The Site checks
each staged tile digest and requires a separate owner review to activate it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from PIL import Image
import rasterio
from rasterio.enums import Resampling
from rasterio.transform import from_bounds
from rasterio.warp import reproject, transform_bounds

ORIGIN = 20_037_508.342789244
TILE = 256
MAX_TILES = 5000
MAX_TOTAL_BYTES = 500_000_000


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1 << 20):
            digest.update(chunk)
    return digest.hexdigest()


def tile_bounds(z: int, x: int, y: int) -> tuple[float, float, float, float]:
    width = 2 * ORIGIN / (2 ** z)
    west = -ORIGIN + x * width
    north = ORIGIN - y * width
    return west, north - width, west + width, north


def tile_range(bounds: tuple[float, float, float, float], z: int) -> tuple[range, range]:
    west, south, east, north = bounds
    width = 2 * ORIGIN / (2 ** z)
    x0 = max(0, math.floor((west + ORIGIN) / width))
    x1 = min(2 ** z - 1, math.ceil((east + ORIGIN) / width) - 1)
    y0 = max(0, math.floor((ORIGIN - north) / width))
    y1 = min(2 ** z - 1, math.ceil((ORIGIN - south) / width) - 1)
    return range(x0, x1 + 1), range(y0, y1 + 1)


def prepare(receipt_file: Path, output_root: Path) -> Path:
    receipt = json.loads(receipt_file.read_text(encoding="utf-8"))
    sheet, source = receipt["sheet"], receipt["geotiff"]
    if receipt.get("version") != 1 or sheet.get("state") != "KS":
        raise ValueError("capture is not a Kansas historical sheet")
    original = receipt_file.with_name(f"{sheet['scanId']}.tif")
    if not original.is_file() or original.stat().st_size != source["bytes"] or sha256(original) != source["sha256"]:
        raise ValueError("RAW GeoTIFF does not match the capture receipt")
    package_id = source["sha256"][:24]
    final = output_root / f"{sheet['scanId']}-{package_id}"
    work = output_root / f"{sheet['scanId']}-{package_id}.part"
    if final.exists() or work.exists():
        raise FileExistsError("package already exists; preserve it or choose a new output directory")
    output_root.mkdir(parents=True, exist_ok=True)
    work.mkdir()
    with rasterio.open(original) as src:
        if src.count < 3 or src.crs is None or src.transform.is_identity or src.width > 30_000 or src.height > 30_000:
            raise ValueError("GeoTIFF lacks bounded RGB georeferencing")
        geographic = transform_bounds(src.crs, "EPSG:4326", *src.bounds, densify_pts=21)
        if geographic[2] < -102.1 or geographic[0] > -94.5 or geographic[3] < 37 or geographic[1] > 40.1:
            raise ValueError("GeoTIFF does not intersect Kansas")
        mercator = transform_bounds(src.crs, "EPSG:3857", *src.bounds, densify_pts=21)
        metres_per_pixel = max((mercator[2] - mercator[0]) / src.width, (mercator[3] - mercator[1]) / src.height)
        max_zoom = max(0, min(16, math.ceil(math.log2(2 * ORIGIN / (TILE * metres_per_pixel)))))
        min_zoom = max(0, max_zoom - 5)
        mask = src.dataset_mask()
        records: dict[str, dict[str, int | str]] = {}
        total_bytes = 0
        for z in range(min_zoom, max_zoom + 1):
            xs, ys = tile_range(mercator, z)
            if len(xs) * len(ys) + len(records) > MAX_TILES:
                raise ValueError("sheet needs more than the bounded tile count")
            for x in xs:
                for y in ys:
                    bounds = tile_bounds(z, x, y)
                    transform = from_bounds(*bounds, TILE, TILE)
                    alpha = np.zeros((TILE, TILE), dtype=np.uint8)
                    reproject(mask, alpha, src_transform=src.transform, src_crs=src.crs,
                              dst_transform=transform, dst_crs="EPSG:3857", resampling=Resampling.nearest)
                    if not alpha.any():
                        continue
                    bands = []
                    for band in (1, 2, 3):
                        image = np.zeros((TILE, TILE), dtype=np.uint8)
                        reproject(rasterio.band(src, band), image, src_transform=src.transform, src_crs=src.crs,
                                  dst_transform=transform, dst_crs="EPSG:3857", resampling=Resampling.bilinear)
                        bands.append(image)
                    rgba = np.stack((*bands, alpha), axis=-1)
                    address = f"{z}/{x}/{y}"
                    target = work / "tiles" / f"{address}.png"
                    target.parent.mkdir(parents=True, exist_ok=True)
                    Image.fromarray(rgba).save(target, format="PNG", optimize=True)
                    size = target.stat().st_size
                    total_bytes += size
                    if size > 2_000_000 or total_bytes > MAX_TOTAL_BYTES:
                        raise ValueError("prepared tiles exceed the bounded package size")
                    records[address] = {"sha256": sha256(target), "bytes": size}
        if not records:
            raise ValueError("no georeferenced map tiles were produced")
        manifest = {"version": 1, "packageId": package_id, "sheet": sheet,
                    "geotiff": {**source, "crs": src.crs.to_wkt(), "transform": list(src.transform.to_gdal()),
                                "width": src.width, "height": src.height},
                    "bounds": list(geographic), "minZoom": min_zoom, "maxZoom": max_zoom,
                    "sourceRetrievedAt": receipt["retrievedAt"], "tiles": records,
                    "evidenceRole": "EXTERNAL_CONTEXT_ONLY"}
        (work / "manifest.json").write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    work.rename(final)
    return final


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(prepare(args.capture, args.output))


if __name__ == "__main__":
    main()
