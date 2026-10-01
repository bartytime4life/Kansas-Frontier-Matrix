"""CPU preparation of exact-cell Crop-CASMA 1 km Kansas map tiles.

Nearest-neighbor reprojection changes only pixel placement; it never interpolates
numeric soil moisture. The smooth palette maps each original value to a color.
No-data cells stay transparent. Output remains an unreleased candidate.
"""
from __future__ import annotations

from hashlib import sha256
from math import asinh, floor, pi, radians, tan
from pathlib import Path
import argparse
import json

import numpy as np
from PIL import Image
import rasterio
from rasterio.enums import Resampling
from rasterio.vrt import WarpedVRT
from rasterio.windows import from_bounds
from pyproj import Transformer

WORLD = 20037508.342789244
KANSAS_BOUNDS = (-102.10, 36.95, -94.55, 40.05)
ZOOMS = range(4, 10)
MAX_TILES = 160
PALETTE = [(0, (110, 64, 42)), (0.1, (188, 113, 52)), (0.2, (233, 204, 99)),
           (0.3, (102, 185, 152)), (0.5, (39, 133, 180)), (1, (25, 70, 130))]
CHECKPOINTS = {"Dodge City": (-100.017, 37.752), "Wichita": (-97.336, 37.688),
               "Salina": (-97.611, 38.841), "Topeka": (-95.689, 39.048),
               "Kansas City": (-94.627, 39.114)}


def canonical_candidate_bytes(value: dict) -> bytes:
    """Match the Site verifier's JSON.stringify for integral float values."""
    def normalize(item):
        if type(item) is float and item.is_integer():
            return int(item)
        if isinstance(item, dict):
            return {key: normalize(child) for key, child in item.items()}
        if isinstance(item, (list, tuple)):
            return [normalize(child) for child in item]
        return item

    return json.dumps(normalize(value), sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def tile_range(zoom: int):
    west, south, east, north = KANSAS_BOUNDS
    n = 2 ** zoom
    x0, x1 = (floor((lon + 180) / 360 * n) for lon in (west, east))
    y0, y1 = (floor((1 - asinh(tan(radians(lat))) / pi) / 2 * n) for lat in (north, south))
    return range(x0, x1 + 1), range(y0, y1 + 1)


def tile_bounds(zoom: int, x: int, y: int):
    width = 2 * WORLD / (2 ** zoom)
    return (-WORLD + x * width, WORLD - (y + 1) * width,
            -WORLD + (x + 1) * width, WORLD - y * width)


def colorize(values: np.ma.MaskedArray) -> Image.Image:
    raw = np.asarray(values.filled(-9999), dtype=np.float32)
    valid = ~np.ma.getmaskarray(values) & np.isfinite(raw) & (raw >= 0) & (raw <= 1)
    if np.any((~np.ma.getmaskarray(values)) & ~valid):
        raise ValueError("OUT_OF_RANGE_SOURCE_VALUE")
    rgba = np.zeros((256, 256, 4), dtype=np.uint8)
    for channel in range(3):
        rgba[:, :, channel] = np.interp(raw, [stop[0] for stop in PALETTE], [stop[1][channel] for stop in PALETTE]).astype(np.uint8)
    rgba[:, :, 3] = np.where(valid, 255, 0).astype(np.uint8)
    return Image.fromarray(rgba)


def prepare(capture_dir: Path, destination: Path) -> dict:
    if destination.exists():
        raise ValueError("DESTINATION_EXISTS")
    manifest = json.loads((capture_dir / "manifest.json").read_text())
    if manifest.get("profile") != "kfm.crop-casma-capture/v1" or manifest.get("state") != "CAPTURED_CANDIDATE" or manifest.get("release_state") != "UNRELEASED":
        raise ValueError("CAPTURE_NOT_READY")
    source_bytes = (capture_dir / "source.tif").read_bytes()
    digest = "sha256:" + sha256(source_bytes).hexdigest()
    if digest != manifest.get("source_sha256"):
        raise ValueError("SOURCE_DIGEST_MISMATCH")
    destination.mkdir(mode=0o700, parents=False)
    tiles = []
    with rasterio.open(capture_dir / "source.tif") as src:
        if (str(src.crs) != "EPSG:5070" or src.count != 1 or src.dtypes[0] != "float32" or
                src.nodata != -9999 or src.res != (1000.0, 1000.0) or
                (src.width, src.height) != (659, 355) or
                tuple(round(value) for value in src.bounds) != tuple(manifest["bounds_5070"])):
            raise ValueError("SOURCE_GRID_INVALID")
        cells = src.read(1, masked=True)
        valid = cells.compressed()
        if not valid.size or not np.all(np.isfinite(valid)) or valid.min() < 0 or valid.max() > 1:
            raise ValueError("SOURCE_VALUES_INVALID")
        to_source = Transformer.from_crs("EPSG:4326", "EPSG:5070", always_xy=True)
        samples = {}
        for name, (lon, lat) in CHECKPOINTS.items():
            x5070, y5070 = to_source.transform(lon, lat)
            row, column = src.index(x5070, y5070)
            cell = cells[row, column]
            samples[name] = None if np.ma.is_masked(cell) else float(cell)
        with WarpedVRT(src, crs="EPSG:3857", resampling=Resampling.nearest, src_nodata=-9999, nodata=-9999) as vrt:
            for zoom in ZOOMS:
                xs, ys = tile_range(zoom)
                for x in xs:
                    for y in ys:
                        if len(tiles) >= MAX_TILES:
                            raise ValueError("TILE_LIMIT")
                        west, south, east, north = tile_bounds(zoom, x, y)
                        window = from_bounds(west, south, east, north, transform=vrt.transform)
                        array = vrt.read(1, window=window, out_shape=(256, 256), resampling=Resampling.nearest, masked=True)
                        if not np.any(~np.ma.getmaskarray(array)):
                            continue
                        path = destination / "tiles" / str(zoom) / str(x) / f"{y}.png"
                        path.parent.mkdir(parents=True, exist_ok=True)
                        colorize(array).save(path, format="PNG", optimize=False)
                        raw = path.read_bytes()
                        tiles.append({"z": zoom, "x": x, "y": y, "sha256": "sha256:" + sha256(raw).hexdigest(), "bytes": len(raw)})
        summary = {"profile": "kfm.crop-casma-tiles/v1", "state": "PREPARED_CANDIDATE", "release_state": "UNRELEASED",
            "source_id": "usda-nass-crop-casma-1km", "day": manifest["day"], "layer": manifest["layer"],
            "source_sha256": digest, "source_crs": "EPSG:5070", "tile_crs": "EPSG:3857",
            "source_resolution_m": 1000, "source_nodata": -9999, "numeric_unit": "m3/m3",
            "numeric_resampling": "nearest", "color_interpolation": "palette only",
            "valid_cells": int(valid.size), "min": float(valid.min()), "max": float(valid.max()),
            "coverage_checkpoints_m3_m3": samples,
            "coverage_state": "PARTIAL_AT_CHECKPOINTS" if any(value is None for value in samples.values()) else "SAMPLED_ONLY",
            "bounds_wgs84": KANSAS_BOUNDS, "zooms": [min(ZOOMS), max(ZOOMS)],
            "palette": PALETTE, "tiles": tiles}
    identity = canonical_candidate_bytes(summary)
    summary["candidate_id"] = "sha256:" + sha256(identity).hexdigest()
    (destination / "manifest.json").write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capture_dir", type=Path)
    parser.add_argument("destination", type=Path, help="new external candidate directory")
    args = parser.parse_args()
    result = prepare(args.capture_dir, args.destination)
    print(json.dumps({key: result[key] for key in ("state", "candidate_id", "valid_cells", "min", "max")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
