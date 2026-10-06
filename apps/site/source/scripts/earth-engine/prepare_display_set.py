#!/usr/bin/env python3
"""Validate private Earth Engine Drive exports and prepare an immutable R2 display set.

Inputs and outputs stay under --data-root, outside the Site repository. A reviewer
must write an explicit approval record for each layer. Invalid layers are held
independently and never appear in the manifest.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import rasterio
from PIL import Image
from rasterio.features import geometry_mask
from rasterio.warp import Resampling, reproject, transform_bounds, transform_geom
from rasterio.windows import Window

PREFIX = "earth-engine-context/v1"
ORIGIN = 20037508.342789244
# Start at zoom 0 so installed layers stay visible at the Explorer's regional
# minimum zoom (4) and in Globe views; MapLibre never under-zooms raster tiles.
MIN_ZOOM = 0
SAMPLE = {"type": "Polygon", "coordinates": [[[-99.5, 38.2], [-99.3, 38.2], [-99.3, 38.4], [-99.5, 38.4], [-99.5, 38.2]]]}
LAYERS = {
    "ee-cdl": {"source": "USDA/NASS/CDL", "bands": 1, "unit": "USDA CDL class code", "resampling": "nearest", "maxZoom": 12, "coverage": 0.995, "period": "2024 harvest year", "resolution": 30, "attribution": "USDA NASS Cropland Data Layer", "legend": "USDA 2024 CDL crop classes · official class colors"},
    "ee-chirps": {"source": "UCSB-CHG/CHIRPS/DAILY", "bands": 2, "unit": "mm", "resampling": "native", "maxZoom": 8, "coverage": 0.99, "period": "2024 calendar year", "resolution": 5566, "attribution": "UCSB Climate Hazards Center · CHIRPS", "legend": "Annual precipitation · mm; 0–1200 display ramp"},
    "ee-terraclimate": {"source": "IDAHO_EPSCOR/TERRACLIMATE", "bands": 2, "unit": "unitless PDSI", "resampling": "native", "maxZoom": 8, "coverage": 0.99, "period": "2024 calendar year", "resolution": 4638, "attribution": "University of Idaho / UC Merced · TerraClimate", "legend": "Annual mean PDSI · −5 to +5 display ramp"},
    "ee-sentinel2": {"source": "COPERNICUS/S2_SR_HARMONIZED", "bands": 4, "unit": "surface reflectance", "resampling": "bilinear", "maxZoom": 12, "coverage": 0.95, "period": "2024 calendar year", "resolution": 30, "attribution": "Contains modified Copernicus Sentinel data 2024 · European Union / ESA", "legend": "Natural color · SCL screened annual median"},
    "ee-3dep": {"source": "USGS/3DEP/10m_collection", "bands": 1, "unit": "meters", "resampling": "bilinear", "maxZoom": 12, "coverage": 0.995, "period": "Mixed acquisition dates · source mosaic", "resolution": 30, "attribution": "USGS 3D Elevation Program", "legend": "Elevation · meters; 200–1300 display ramp"},
}
SOURCE_YEARS = {"ee-cdl": (2008, 2024), "ee-chirps": (1981, 2025),
                "ee-terraclimate": (1958, 2024), "ee-sentinel2": (2019, 2025)}

LANDSAT_MISSIONS = {"ee-landsat4": ("LT04", 1982, 1993), "ee-landsat5": ("LT05", 1984, 2012),
                    "ee-landsat7": ("LE07", 1999, 2024), "ee-landsat8": ("LC08", 2013, 2025),
                    "ee-landsat9": ("LC09", 2021, 2025)}
for layer_id, (mission, first_year, last_year) in LANDSAT_MISSIONS.items():
    number = int(layer_id.removeprefix("ee-landsat"))
    LAYERS[layer_id] = {"source": f"LANDSAT/{mission}/C02/T1_L2", "bands": 4, "unit": "surface reflectance",
                        "resampling": "bilinear", "maxZoom": 12, "coverage": 0.95, "period": "annual source composite",
                        "resolution": 30, "attribution": f"USGS Landsat {number} Collection 2",
                        "legend": "Natural color · QA screened annual median"}
    SOURCE_YEARS[layer_id] = (first_year, last_year)
# Confirmed from ANm and ANd image projection metadata, 2026-10-06; not inferred from TerraClimate.
PRISM_GRID = (0.041666666667, 0, -125.0208333333335, 0, -0.041666666667, 49.9375000000005)
for layer_id, collection, first_year in (("ee-prism-monthly", "ANm", 1895), ("ee-prism-daily", "ANd", 1981)):
    LAYERS[layer_id] = {"source": f"OREGONSTATE/PRISM/{collection}", "bands": 2, "unit": "mm", "resampling": "native",
                        "maxZoom": 8, "coverage": 0.99, "period": "annual source composite", "resolution": 4638,
                        "attribution": "PRISM Climate Group / Oregon State University",
                        "legend": "Annual precipitation · mm; 0–1200 display ramp"}
    SOURCE_YEARS[layer_id] = (first_year, 2025)
DAILY_LAYERS = {"ee-chirps", "ee-prism-daily"}
MONTHLY_LAYERS = {"ee-terraclimate", "ee-prism-monthly"}
RGB_LAYERS = {"ee-sentinel2", *LANDSAT_MISSIONS}
HIGH_RESOLUTION_LAYERS = {"ee-cdl", "ee-3dep", *RGB_LAYERS}


def check_source_year(layer_id: str, year: int) -> None:
    if type(year) is not int or layer_id not in LAYERS or (year != 2024 if layer_id == "ee-3dep" else not SOURCE_YEARS[layer_id][0] <= year <= SOURCE_YEARS[layer_id][1]):
        raise ValueError("unsupported source year; terrain retains its mixed-date 2024 baseline")


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def dump(path: Path, value: object) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def expected_days(year: int) -> int:
    return (date(year + 1, 1, 1) - date(year, 1, 1)).days


def review(path: Path, layer_id: str, year: int, boundary_hash: str, palette_hash: str) -> dict:
    check_source_year(layer_id, year)
    record = json.loads(path.read_text())
    spec = LAYERS[layer_id]
    required = ("sourceImageIds", "sourceInventoryTaskId", "sourceInventorySha256", "sampleTaskId", "statewideTaskId", "sampleGeoTiffSha256", "statewideGeoTiffSha256", "masks", "terms", "processingParameters", "reviewer", "approvedAt", "limits")
    if record.get("status") != "APPROVED_VISUAL_CONTEXT" or record.get("layerId") != layer_id or record.get("source") != spec["source"]:
        raise ValueError("review status, layer or source mismatch")
    if any(not record.get(key) for key in required) or not isinstance(record["sourceImageIds"], list) or not all(isinstance(value, str) and value for value in record["sourceImageIds"]):
        raise ValueError("review provenance is incomplete")
    expected_images = 1 if layer_id == "ee-cdl" else expected_days(year) if layer_id in DAILY_LAYERS else 12 if layer_id in MONTHLY_LAYERS else None
    if expected_images and len(record["sourceImageIds"]) != expected_images:
        raise ValueError("source image ID count does not match the complete period")
    if len(set(record["sourceImageIds"])) != len(record["sourceImageIds"]):
        raise ValueError("source image IDs contain duplicates")
    ids = set(record["sourceImageIds"])
    if layer_id == "ee-cdl" and ids != {f"USDA/NASS/CDL/{year}"}:
        raise ValueError(f"CDL source is not the exact {year} annual image")
    if layer_id == "ee-chirps":
        days = (date(year, 1, 1) + timedelta(days=offset) for offset in range(expected_days(year)))
        if ids != {"UCSB-CHG/CHIRPS/DAILY/" + day.strftime("%Y%m%d") for day in days}:
            raise ValueError(f"CHIRPS source inventory does not cover every {year} day")
    if layer_id == "ee-terraclimate" and ids != {f"IDAHO_EPSCOR/TERRACLIMATE/{year}{month:02d}" for month in range(1, 13)}:
        raise ValueError(f"TerraClimate source inventory does not cover every {year} month")
    if layer_id in ("ee-prism-monthly", "ee-prism-daily"):
        if record.get("nativeGridChecked") is not True or record.get("periodBasis") != "source-system-index":
            raise ValueError("PRISM native grid and source-label period review missing")
        if layer_id == "ee-prism-monthly":
            expected_ids = {f"{spec['source']}/{year}{month:02d}" for month in range(1, 13)}
        else:
            expected_ids = {spec["source"] + "/" + (date(year, 1, 1) + timedelta(days=offset)).strftime("%Y%m%d") for offset in range(expected_days(year))}
        if ids != expected_ids:
            raise ValueError(f"PRISM source inventory does not cover every {year} period")
    if layer_id == "ee-sentinel2" and (not ids or not all(value.startswith(f"COPERNICUS/S2_SR_HARMONIZED/{year}") for value in ids)):
        raise ValueError(f"Sentinel-2 source inventory is not entirely from {year}")
    if layer_id in LANDSAT_MISSIONS:
        mission = LANDSAT_MISSIONS[layer_id][0]
        pattern = re.compile(re.escape(spec["source"]) + "/" + mission + r"_\d{6}_(\d{8})")
        for identity in ids:
            match = pattern.fullmatch(identity)
            try:
                acquired = datetime.strptime(match[1], "%Y%m%d").date() if match else None
            except ValueError:
                acquired = None
            if acquired is None or acquired.year != year:
                raise ValueError(f"Landsat source inventory has a wrong mission, collection or date for {year}")
    if layer_id == "ee-3dep" and (not ids or not all(value.startswith("USGS/3DEP/10m_collection/") for value in ids)):
        raise ValueError("3DEP source inventory contains another collection")
    if not all(record.get(key) is True for key in ("samplePassed", "statewidePassed", "driveCapacityChecked", "termsChecked")):
        raise ValueError("sample, statewide, Drive or terms review incomplete")
    if record.get("boundarySha256") != boundary_hash or record.get("units") != spec["unit"] or record.get("resampling") != spec["resampling"]:
        raise ValueError("boundary, units or resampling mismatch")
    if layer_id == "ee-cdl" and record.get("paletteSha256") != palette_hash:
        raise ValueError("CDL palette hash mismatch")
    if layer_id == "ee-cdl" and year != 2024 and record.get("historicalClassKeyChecked") is not True:
        raise ValueError("historical CDL class meanings and palette require explicit review")
    if layer_id == "ee-3dep" and (not record.get("acquisitionDateReview") or not record.get("verticalDatumReview")):
        raise ValueError("3DEP date or vertical datum review missing")
    for key in ("sampleGeoTiffSha256", "statewideGeoTiffSha256", "sourceInventorySha256"):
        if not isinstance(record[key], str) or len(record[key]) != 64 or any(c not in "0123456789abcdef" for c in record[key]):
            raise ValueError(f"invalid {key}")
    return record


def read_boundary(path: Path) -> dict:
    value = json.loads(path.read_text())
    if value.get("type") != "Feature" or value.get("properties", {}).get("STATEFP") != "20":
        raise ValueError("expected a single TIGER Kansas feature with STATEFP=20")
    geometry = value.get("geometry")
    if not isinstance(geometry, dict) or geometry.get("type") not in ("Polygon", "MultiPolygon"):
        raise ValueError("Kansas boundary geometry missing")
    return geometry


def check_grid(src, layer_id: str) -> None:
    spec = LAYERS[layer_id]
    if src.count != spec["bands"]:
        raise ValueError(f"expected {spec['bands']} GeoTIFF bands")
    if src.nodata != (65535 if layer_id == "ee-cdl" else -9999):
        raise ValueError("unexpected nodata value")
    if src.crs is None:
        raise ValueError("missing CRS")
    if layer_id in HIGH_RESOLUTION_LAYERS:
        t = src.transform
        if src.crs.to_epsg() != 5070 or abs(t.a - 30) > 1e-6 or abs(t.e + 30) > 1e-6 or abs(t.b) > 1e-8 or abs(t.d) > 1e-8:
            raise ValueError("high-resolution product is not on the documented 30 m EPSG:5070 grid")
        if abs((t.c + 1200000) / 30 - round((t.c + 1200000) / 30)) > 1e-5 or abs((2400000 - t.f) / 30 - round((2400000 - t.f) / 30)) > 1e-5:
            raise ValueError("30 m grid origin is shifted")
    elif layer_id.startswith("ee-prism-"):
        t = src.transform
        step, _, left, _, negative_step, top = PRISM_GRID
        if src.crs.to_epsg() != 4269 or abs(t.a - step) > 1e-10 or abs(t.e - negative_step) > 1e-10 or abs(t.b) > 1e-9 or abs(t.d) > 1e-9 \
                or abs((t.c - left) / step - round((t.c - left) / step)) > 1e-5 \
                or abs((top - t.f) / step - round((top - t.f) / step)) > 1e-5:
            raise ValueError("PRISM product was not retained on its verified native NAD83 grid")
    else:
        expected = 0.05 if layer_id == "ee-chirps" else 1 / 24
        top_origin = 50 if layer_id == "ee-chirps" else 90
        if src.crs.to_epsg() != 4326 or abs(src.transform.a - expected) > 1e-7 or abs(src.transform.e + expected) > 1e-7 \
                or abs(src.transform.b) > 1e-9 or abs(src.transform.d) > 1e-9 \
                or abs((src.transform.c + 180) / expected - round((src.transform.c + 180) / expected)) > 1e-5 \
                or abs((top_origin - src.transform.f) / expected - round((top_origin - src.transform.f) / expected)) > 1e-5:
            raise ValueError("climate product was not retained at its native grid")


def coverage(src, geometry: dict, layer_id: str, sample: bool, year: int) -> float:
    local = transform_geom("EPSG:4326", src.crs, geometry)
    all_bounds = rasterio.features.bounds(local)
    tolerance = max(abs(src.transform.a), abs(src.transform.e)) * 2
    if src.bounds.left > all_bounds[0] + tolerance or src.bounds.bottom > all_bounds[1] + tolerance or src.bounds.right < all_bounds[2] - tolerance or src.bounds.top < all_bounds[3] - tolerance:
        raise ValueError("GeoTIFF bounds do not cover the requested area")
    total = valid = 0
    low = math.inf
    high = -math.inf
    expected_count = expected_days(year) if layer_id in DAILY_LAYERS else 12 if layer_id in MONTHLY_LAYERS else None
    for _, window in src.block_windows(1):
        transform = src.window_transform(window)
        inside = geometry_mask([local], out_shape=(int(window.height), int(window.width)), transform=transform, invert=True)
        amount = int(inside.sum())
        if not amount:
            continue
        data = src.read(window=window)
        primary = data[0]
        good = inside & np.isfinite(primary) & (primary != src.nodata)
        if layer_id in RGB_LAYERS:
            good &= np.all(np.isfinite(data[:3]) & (data[:3] != src.nodata), axis=0) & (data[3] >= 1) & np.isfinite(data[3]) & (data[3] == np.floor(data[3]))
        if expected_count is not None:
            good &= data[1] == expected_count
        if good.any():
            observed = data[:3, good] if layer_id in RGB_LAYERS else primary[good]
            low = min(low, float(observed.min()))
            high = max(high, float(observed.max()))
        total += amount
        valid += int(good.sum())
    if total == 0:
        raise ValueError("no Kansas pixels in GeoTIFF")
    fraction = valid / total
    minimum = 0.95 if sample else LAYERS[layer_id]["coverage"]
    if fraction < minimum:
        raise ValueError(f"pixel coverage {fraction:.2%} below {minimum:.1%}")
    ranges = {"ee-cdl": (0, 254), "ee-chirps": (0, 5000), "ee-terraclimate": (-20, 20), "ee-sentinel2": (-0.2, 1.5), "ee-3dep": (-100, 4500)}
    bound = (-0.2, 1.5) if layer_id in RGB_LAYERS else (0, 5000) if layer_id.startswith("ee-prism-") else ranges[layer_id]
    if low < bound[0] or high > bound[1]:
        raise ValueError(f"pixel values {low:g}–{high:g} outside reviewed {bound} range")
    return fraction


def tile_bounds(z: int, x: int, y: int) -> tuple[float, float, float, float]:
    width = 2 * ORIGIN / (2 ** z)
    left = -ORIGIN + x * width
    top = ORIGIN - y * width
    return left, top - width, left + width, top


def tile_range(bounds: tuple[float, float, float, float], z: int) -> tuple[range, range]:
    left, bottom, right, top = bounds
    size = 2 * ORIGIN / (2 ** z)
    x0 = max(0, int(math.floor((left + ORIGIN) / size)))
    x1 = min(2 ** z - 1, int(math.floor((right + ORIGIN) / size)))
    y0 = max(0, int(math.floor((ORIGIN - top) / size)))
    y1 = min(2 ** z - 1, int(math.floor((ORIGIN - bottom) / size)))
    return range(x0, x1 + 1), range(y0, y1 + 1)


def hex_rgb(value: str) -> np.ndarray:
    return np.array([int(value[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.uint8)


def colorize(data: np.ndarray, good: np.ndarray, layer_id: str, palette: dict) -> np.ndarray:
    rgba = np.zeros((256, 256, 4), dtype=np.uint8)
    if layer_id == "ee-cdl":
        for value in np.unique(data[0][good]):
            item = palette["classes"].get(str(int(value)))
            if item is None:
                raise ValueError(f"CDL class {value} has no official catalog color")
            rgba[:, :, :3][good & (data[0] == value)] = hex_rgb(item["color"])
    elif layer_id in RGB_LAYERS:
        colors = np.clip(data[:3].transpose(1, 2, 0) / 0.3, 0, 1) ** (1 / 1.2)
        rgba[:, :, :3][good] = np.round(colors[good] * 255).astype(np.uint8)
    else:
        # Keep identical to EARTH_ENGINE_DISPLAY_RAMPS in app/earth-engine-data.ts.
        ramps = {
            "ee-chirps": ([0, 600, 1200], ["#fff4c2", "#79c9bc", "#235ca8"]),
            "ee-prism-monthly": ([0, 600, 1200], ["#fff4c2", "#79c9bc", "#235ca8"]),
            "ee-prism-daily": ([0, 600, 1200], ["#fff4c2", "#79c9bc", "#235ca8"]),
            "ee-terraclimate": ([-5, 0, 5], ["#a63603", "#f6eedb", "#0868ac"]),
            "ee-3dep": ([200, 600, 900, 1300], ["#28594e", "#c4c98a", "#a67e54", "#efe7d4"]),
        }
        stops, colors = ramps[layer_id]
        for channel in range(3):
            rgba[:, :, channel][good] = np.round(np.interp(data[0][good], stops, [hex_rgb(color)[channel] for color in colors])).astype(np.uint8)
    rgba[:, :, 3][good] = 255
    return rgba


def render_tiles(src, layer_id: str, set_dir: Path, set_id: str, geometry: dict, palette: dict, year: int) -> dict:
    spec = LAYERS[layer_id]
    projected_boundary = transform_geom("EPSG:4326", "EPSG:3857", geometry)
    boundary_bounds = rasterio.features.bounds(projected_boundary)
    indexes = {}
    for z in range(MIN_ZOOM, spec["maxZoom"] + 1):
        xs, ys = tile_range(boundary_bounds, z)
        entries = {}
        for x in xs:
            for y in ys:
                left, bottom, right, top = tile_bounds(z, x, y)
                transform = rasterio.transform.from_bounds(left, bottom, right, top, 256, 256)
                fill = 65535 if layer_id == "ee-cdl" else -9999
                dtype = "uint16" if layer_id == "ee-cdl" else "float32"
                data = np.full((src.count, 256, 256), fill, dtype=dtype)
                for band in range(src.count):
                    reproject(source=rasterio.band(src, band + 1), destination=data[band], src_nodata=src.nodata, dst_transform=transform,
                              dst_crs="EPSG:3857", dst_nodata=fill,
                              resampling=Resampling.nearest if layer_id == "ee-cdl" or band == src.count - 1 and src.count in (2, 4) else Resampling.bilinear,
                              init_dest_nodata=True)
                good = np.isfinite(data[0]) & (data[0] != fill)
                good &= geometry_mask([projected_boundary], out_shape=(256, 256), transform=transform, invert=True)
                if layer_id in RGB_LAYERS:
                    good &= np.all(np.isfinite(data[:3]) & (data[:3] != fill), axis=0) & (data[3] >= 1) & np.isfinite(data[3]) & (data[3] == np.floor(data[3]))
                elif layer_id in DAILY_LAYERS:
                    good &= data[1] == expected_days(year)
                elif layer_id in MONTHLY_LAYERS:
                    good &= data[1] == 12
                # Include transparent tiles across the declared Kansas bounds.
                # MapLibre may request a tile within that box but outside the
                # irregular state polygon; it must not appear to be a missing
                # approved tile or hide the whole layer.
                image = colorize(data, good, layer_id, palette)
                output = io.BytesIO()
                Image.fromarray(image).save(output, format="PNG", optimize=True)
                raw = output.getvalue()
                if len(raw) > 2_000_000:
                    raise ValueError("tile exceeds serving limit")
                tile = set_dir / PREFIX / "sets" / set_id / "tiles" / layer_id / str(z) / str(x) / f"{y}.png"
                tile.parent.mkdir(parents=True, exist_ok=True)
                tile.write_bytes(raw)
                entries[f"{x}/{y}"] = hashlib.sha256(raw).hexdigest()
        if not entries:
            raise ValueError(f"no rendered tiles at zoom {z}")
        index = set_dir / PREFIX / "sets" / set_id / "indexes" / layer_id / f"{z}.json"
        index_hash = dump(index, {"tiles": entries})
        if index.stat().st_size > 4_000_000:
            raise ValueError(f"tile index at zoom {z} exceeds serving limit")
        coordinates = [tuple(map(int, key.split("/"))) for key in entries]
        indexes[str(z)] = {"sha256": index_hash, "count": len(entries), "minX": min(item[0] for item in coordinates), "maxX": max(item[0] for item in coordinates), "minY": min(item[1] for item in coordinates), "maxY": max(item[1] for item in coordinates)}
    return indexes


def prepare(args) -> int:
    year = args.year
    if type(year) is not int or not 1895 <= year <= 2025:
        raise ValueError("year must be a supported source year, 1895–2025")
    root = args.data_root.resolve()
    repository = Path(__file__).resolve().parents[2]
    if root == repository or repository in root.parents:
        raise ValueError("private raster data store must be outside the Site repository")
    boundary_path = root / "kansas_tiger2018.geojson"
    boundary = read_boundary(boundary_path)
    boundary_hash = sha256(boundary_path)
    palette_path = Path(__file__).with_name("cdl_2024_palette.json")
    palette = json.loads(palette_path.read_text())
    palette_hash = sha256(palette_path)
    approved = []
    held = {}
    for layer_id in LAYERS:
        if layer_id == "ee-3dep" and year != 2024:
            continue  # Mixed-date terrain is held in the baseline set, never relabeled as an annual product.
        if layer_id != "ee-3dep" and not SOURCE_YEARS[layer_id][0] <= year <= SOURCE_YEARS[layer_id][1]:
            continue
        folder = root / "exports" / layer_id if year == 2024 else root / "exports" / str(year) / layer_id
        try:
            record_path = folder / "review.json"
            record = review(record_path, layer_id, year, boundary_hash, palette_hash)
            inventory_path = folder / "source_ids.csv"
            if sha256(inventory_path) != record["sourceInventorySha256"]:
                raise ValueError("source image inventory hash mismatch")
            with inventory_path.open(newline="") as handle:
                inventory = [row["source_image_id"] for row in csv.DictReader(handle)]
            if len(inventory) != len(record["sourceImageIds"]) or set(inventory) != set(record["sourceImageIds"]):
                raise ValueError("review image IDs differ from the Earth Engine inventory")
            sample, statewide = folder / "sample.tif", folder / "statewide.tif"
            if sha256(sample) != record["sampleGeoTiffSha256"] or sha256(statewide) != record["statewideGeoTiffSha256"]:
                raise ValueError("GeoTIFF hash mismatch")
            with rasterio.open(sample) as src:
                check_grid(src, layer_id)
                sample_coverage = coverage(src, SAMPLE, layer_id, True, year)
            with rasterio.open(statewide) as src:
                check_grid(src, layer_id)
                statewide_coverage = coverage(src, boundary, layer_id, False, year)
            approved.append((layer_id, record, record_path, statewide, sample_coverage, statewide_coverage))
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            held[layer_id] = str(error)
    if not approved:
        print(json.dumps({"approved": [], "held": held}, indent=2))
        return 2
    identity = "|".join(["v1"] + ([] if year == 2024 else [str(year)]) + [boundary_hash, palette_hash] + [f"{item[0]}:{item[1]['statewideGeoTiffSha256']}:{sha256(item[2])}" for item in approved])
    set_id = f"ks-{year}-" + hashlib.sha256(identity.encode()).hexdigest()[:20]
    set_dir = root / "display-sets" / set_id
    if set_dir.exists():
        raise ValueError("immutable display-set directory already exists; review the existing result")
    layers = []
    for layer_id, record, record_path, statewide, sample_coverage, statewide_coverage in approved:
        try:
            with rasterio.open(statewide) as src:
                indexes = render_tiles(src, layer_id, set_dir, set_id, boundary, palette, year)
            spec = LAYERS[layer_id]
            period = f"{year} harvest year" if layer_id == "ee-cdl" else spec["period"] if layer_id == "ee-3dep" else f"{year} calendar year"
            attribution = f"Contains modified Copernicus Sentinel data {year} · European Union / ESA" if layer_id == "ee-sentinel2" else spec["attribution"]
            legend = f"USDA {year} CDL crop classes · official class colors" if layer_id == "ee-cdl" else spec["legend"]
            layers.append({"id": layer_id, "status": "approved", "source": spec["source"], "period": period, "resolutionMeters": spec["resolution"],
                           "attribution": attribution, "limits": record["limits"], "legend": legend,
                           "geotiffSha256": record["statewideGeoTiffSha256"], "reviewSha256": sha256(record_path), "tileIndexes": indexes})
            print(f"APPROVED {layer_id}: sample {sample_coverage:.2%}, statewide {statewide_coverage:.2%}, {sum(item['count'] for item in indexes.values())} tiles")
        except (OSError, ValueError) as error:
            held[layer_id] = str(error)
            print(f"HELD {layer_id}: {error}")
    if not layers:
        print(json.dumps({"approved": [], "held": held}, indent=2))
        return 2
    manifest = {"schema": "kfm-earth-engine-context/v1", "setId": set_id, "boundary": "Kansas · TIGER/2018/States · STATEFP 20",
                "approvedAt": datetime.now(timezone.utc).isoformat(), "reviewState": "APPROVED_VISUAL_CONTEXT", "admission": "NOT_ADMITTED",
                "evidence": "NOT_CLAIM_EVIDENCE", "layers": layers}
    manifest_path = set_dir / PREFIX / "sets" / set_id / "manifest.json"
    manifest_hash = dump(manifest_path, manifest)
    dump(set_dir / PREFIX / "active.json", {"schema": "kfm-earth-engine-context-pointer/v1", "setId": set_id, "manifestSha256": manifest_hash})
    dump(set_dir / "preparation.json", {"setId": set_id, "year": year, "approved": [item["id"] for item in layers], "held": held, "manifestSha256": manifest_hash,
                                         "installation": "Upload immutable sets/ objects first; switch active.json only after readback and owner-only visual review."})
    print(json.dumps({"setId": set_id, "approved": [item["id"] for item in layers], "held": held, "path": str(set_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", required=True, type=Path, help="External private KFM data root, never a Git checkout")
    parser.add_argument("--year", type=int, default=2024, help="Annual imagery year; 2024 retains the legacy external export layout")
    raise SystemExit(prepare(parser.parse_args()))
