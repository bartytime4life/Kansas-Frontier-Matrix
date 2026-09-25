#!/usr/bin/env python3
"""Assemble every high-resolution Drive shard on the external private data store.

Place all files from one completed Earth Engine task in exports/<layer>/shards/.
This refuses overlaps, shifted grids and mixed band layouts. The independent
Kansas coverage check in prepare_display_set.py remains required for approval.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import rasterio
from rasterio.transform import Affine
from rasterio.windows import Window

from prepare_display_set import check_grid, dump, sha256


def aligned(value: float, step: float) -> int:
    result = value / step
    if abs(result - round(result)) > 1e-5:
        raise ValueError("shard is shifted from the 30 m display grid")
    return round(result)


def overlaps(left: tuple[int, int, int, int], right: tuple[int, int, int, int]) -> bool:
    return left[0] < right[2] and right[0] < left[2] and left[1] < right[3] and right[1] < left[3]


def assemble(root: Path, layer: str) -> None:
    if layer not in ("ee-cdl", "ee-sentinel2", "ee-3dep"):
        raise ValueError("only the three 30 m products use Drive shards")
    folder = root.resolve() / "exports" / layer
    shards = sorted((folder / "shards").glob("*.tif"))
    if not shards:
        raise ValueError("no Drive GeoTIFF shards found")
    extents = []
    layouts = []
    for path in shards:
        with rasterio.open(path) as src:
            check_grid(src, layer)
            extents.append((src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top))
            layouts.append((src.count, src.dtypes, src.nodata, str(src.crs)))
    if len(set(layouts)) != 1:
        raise ValueError("shards disagree on band count, type, nodata or CRS")
    left = min(item[0] for item in extents)
    bottom = min(item[1] for item in extents)
    right = max(item[2] for item in extents)
    top = max(item[3] for item in extents)
    width, height = aligned(right - left, 30), aligned(top - bottom, 30)
    rectangles = []
    for item in extents:
        rectangle = (aligned(item[0] - left, 30), aligned(top - item[3], 30), aligned(item[2] - left, 30), aligned(top - item[1], 30))
        if any(overlaps(rectangle, previous) for previous in rectangles):
            raise ValueError("Drive GeoTIFF shards overlap; check for duplicate exports")
        rectangles.append(rectangle)
    output = folder / "statewide.tif"
    if output.exists():
        raise ValueError("statewide.tif exists; preserve the previous review result")
    partial = folder / "statewide.partial.tif"
    if partial.exists():
        raise ValueError("partial assembly exists; inspect it before retrying")
    with rasterio.open(shards[0]) as first:
        profile = first.profile.copy()
    profile.update(driver="GTiff", width=width, height=height, transform=Affine(30, 0, left, 0, -30, top),
                   tiled=True, blockxsize=512, blockysize=512, compress="DEFLATE", predictor=2 if layer == "ee-cdl" else 3,
                   BIGTIFF="YES", interleave="band")
    try:
        with rasterio.open(partial, "w", **profile) as dst:
            # Unwritten shard gaps must remain nodata, never implicit zero pixels.
            for _, window in dst.block_windows(1):
                dst.write(np.full((dst.count, int(window.height), int(window.width)), dst.nodata, dtype=dst.dtypes[0]), window=window)
            for path, (x0, y0, x1, y1) in zip(shards, rectangles):
                with rasterio.open(path) as src:
                    if x1 - x0 != src.width or y1 - y0 != src.height:
                        raise ValueError("shard dimensions disagree with their geographic bounds")
                    for _, window in src.block_windows(1):
                        dest = Window(x0 + window.col_off, y0 + window.row_off, window.width, window.height)
                        dst.write(src.read(window=window), window=dest)
        with rasterio.open(partial) as combined:
            check_grid(combined, layer)
        partial.rename(output)
    except Exception:
        partial.unlink(missing_ok=True)
        raise
    metadata = {"schema": "kfm-earth-engine-shard-assembly/v1", "layer": layer, "outputSha256": sha256(output),
                "width": width, "height": height, "shards": [{"file": path.name, "sha256": sha256(path), "bounds": list(extent)} for path, extent in zip(shards, extents)]}
    dump(folder / "assembly.json", metadata)
    print(json.dumps({"layer": layer, "shardCount": len(shards), "width": width, "height": height,
                      "outputSha256": metadata["outputSha256"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", required=True, type=Path)
    parser.add_argument("--layer", choices=("ee-cdl", "ee-sentinel2", "ee-3dep"), required=True)
    args = parser.parse_args()
    assemble(args.data_root, args.layer)
