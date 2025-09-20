# pytest -q
# Kansas-Frontier-Matrix — repository smoke tests
# - Validates config json, STAC items/collections, and KML well-formedness
# - Designed to be robust: if optional files aren't present yet, the test is SKIPPED with a hint.

from __future__ import annotations
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET
import pytest


REPO = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def read_json(p: Path) -> dict:
    try:
        return json.loads(read_text(p))
    except json.JSONDecodeError as e:
        raise AssertionError(f"Invalid JSON in {p}:\n{e}") from e

def require_file(p: Path):
    if not p.exists():
        pytest.skip(f"Missing file: {p}")

# ---------------------------------------------------------------------------
# App config tests (web/app.config.json)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("config_path", [
    REPO / "web" / "app.config.json",
])
def test_app_config_json_loads(config_path: Path):
    require_file(config_path)
    cfg = read_json(config_path)

    # Top-level keys expected by web/app.js
    assert isinstance(cfg.get("style"), str), "Expected top-level 'style' (URL or style object)"
    assert isinstance(cfg.get("center"), list) and len(cfg["center"]) == 2, "Expected 'center' [lng,lat]"
    assert isinstance(cfg.get("zoom"), (int, float)), "Expected numeric 'zoom'"

    # Time window and default year
    time = cfg.get("time", {})
    assert isinstance(time, dict), "Expected 'time' dict"
    for k in ("min", "max"):
        assert isinstance(time.get(k), int), f"Expected 'time.{k}' as int"

    # defaultYear optional: if present, must be within [min,max]
    if "defaultYear" in cfg:
        y = cfg["defaultYear"]
        assert isinstance(y, int), "defaultYear must be an int"
        assert time["min"] <= y <= time["max"], "defaultYear must be within time range"

    # Layers sanity
    layers = cfg.get("layers", [])
    assert isinstance(layers, list) and layers, "Expected non-empty layers[]"
    ids = [l.get("id") for l in layers]
    assert all(isinstance(i, str) for i in ids), "All layers must have string 'id'"
    assert len(ids) == len(set(ids)), "Layer ids must be unique"

    for l in layers:
        assert l.get("type") in {"raster", "vector", "image"}, f"Layer {l.get('id')} has invalid type"
        # raster/vector require 'url' (image requires 'url' + 'coordinates')
        assert isinstance(l.get("url"), str), f"Layer {l.get('id')} must define 'url'"
        if l["type"] == "image":
            coords = l.get("coordinates")
            assert isinstance(coords, list) and len(coords) == 4, f"Image layer {l['id']} needs 4 coordinates"
        # optional start/end if time-aware
        if "start" in l: assert isinstance(l["start"], int)
        if "end" in l: assert isinstance(l["end"], int)

# ---------------------------------------------------------------------------
# STAC items & collections (basic conformance checks)
# ---------------------------------------------------------------------------

STAC_ITEMS = [
    REPO / "data" / "stac" / "items" / "ks_1m_dem.json",
    REPO / "data" / "stac" / "items" / "ks_1m_hillshade.json",
    REPO / "data" / "stac" / "items" / "usgs_1894_larned.json",
    REPO / "data" / "stac" / "items" / "treaties_1854.json",
    REPO / "data" / "stac" / "items" / "railroads_1900.json",
]

@pytest.mark.parametrize("item_path", STAC_ITEMS)
def test_stac_item_minimum(item_path: Path):
    if not item_path.exists():
        pytest.skip(f"STAC item not present yet: {item_path}")
    item = read_json(item_path)
    assert item.get("stac_version"), "Missing stac_version"
    assert item.get("type") == "Feature", "STAC Item must have type=Feature"
    assert isinstance(item.get("id"), str) and item["id"], "Missing id"
    assert "assets" in item and isinstance(item["assets"], dict) and item["assets"], "Missing assets"
    # bbox / geometry basic presence
    assert "bbox" in item, "Missing bbox"
    assert "geometry" in item and item["geometry"].get("type") in {"Polygon", "MultiPolygon"}, "Missing/invalid geometry"
    # links minimal
    assert "links" in item and isinstance(item["links"], list), "Missing links[]"


STAC_COLLECTIONS = [
    REPO / "data" / "stac" / "collections" / "elevation.json",
    REPO / "data" / "stac" / "collections" / "historic_topo.json",
    REPO / "data" / "stac" / "collections" / "vectors.json",
]

@pytest.mark.parametrize("collection_path", STAC_COLLECTIONS)
def test_stac_collection_minimum(collection_path: Path):
    if not collection_path.exists():
        pytest.skip(f"STAC collection not present yet: {collection_path}")
    col = read_json(collection_path)
    assert col.get("stac_version"), "Missing stac_version"
    assert col.get("type") == "Collection", "STAC Collection must have type=Collection"
    assert isinstance(col.get("id"), str) and col["id"], "Missing id"
    # extent
    extent = col.get("extent", {})
    assert "spatial" in extent and "temporal" in extent, "Collection extent must have spatial+temporal"
    # links minimal
    assert "links" in col and isinstance(col["links"], list), "Missing links[]"


# ---------------------------------------------------------------------------
# KML well-formedness
# ---------------------------------------------------------------------------

KMLS = [
    REPO / "data" / "earth" / "doc.kml",
    REPO / "data" / "earth" / "networklinks" / "ks_1m_hillshade.kml",
    REPO / "data" / "earth" / "networklinks" / "usgs_topo_1894.kml",
]

@pytest.mark.parametrize("kml_path", KMLS)
def test_kml_well_formed(kml_path: Path):
    if not kml_path.exists():
        pytest.skip(f"KML not present yet: {kml_path}")
    # Parse for well-formedness (no schema validation here)
    try:
        ET.parse(kml_path)
    except ET.ParseError as e:
        raise AssertionError(f"Malformed KML: {kml_path}\n{e}") from e


# ---------------------------------------------------------------------------
# Checksum file format
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("sha_path", [
    REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.sha256",
])
def test_sha256_file_format(sha_path: Path):
    if not sha_path.exists():
        pytest.skip(f"Checksum not present yet: {sha_path}")
    line = read_text(sha_path).strip()
    # Expect "<64hex><2spaces or tab>filename"
    m = re.match(r"^([A-Fa-f0-9]{64})\s{1,3}(.+)$", line)
    assert m, f"Checksum format invalid in {sha_path}: '{line}'"
    digest, fname = m.groups()
    assert fname.endswith(".tif"), "Checksum should reference the .tif COG"


# ---------------------------------------------------------------------------
# Optional: STAC cross-link sanity (items referenced from collections)
# ---------------------------------------------------------------------------

def _collect_linked_item_hrefs(collection: dict) -> set[str]:
    hrefs = set()
    for ln in collection.get("links", []):
        if ln.get("rel") == "item" and ln.get("href"):
            hrefs.add(ln["href"])
    return hrefs

@pytest.mark.parametrize("collection_path", STAC_COLLECTIONS)
def test_collection_links_item_files_exist(collection_path: Path):
    if not collection_path.exists():
        pytest.skip(f"STAC collection not present yet: {collection_path}")

    col = read_json(collection_path)
    hrefs = _collect_linked_item_hrefs(col)
    if not hrefs:
        pytest.skip(f"No item links declared in {collection_path.name}")

    # Resolve relative hrefs under collections/
    base = collection_path.parent  # .../stac/collections
    for href in hrefs:
        p = (base / ".." / "items" / Path(href).name).resolve()
        if not p.exists():
            pytest.skip(f"Linked item missing (ok during early scaffolding): {href}")
        read_json(p)  # must parse cleanly

