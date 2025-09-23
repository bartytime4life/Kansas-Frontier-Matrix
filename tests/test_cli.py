# pytest -q
# Kansas-Frontier-Matrix — repository smoke tests
# - Validates web config, STAC items/collections, KML well-formedness
# - Robust-by-design: if optional files aren't present yet, the test is SKIPPED with a hint.

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable, List, Set

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

def existing_only(paths: Iterable[Path]) -> List[Path]:
    return [p for p in paths if p.exists()]

def glob_paths(*globs: str) -> List[Path]:
    out: List[Path] = []
    for g in globs:
        out.extend(REPO.glob(g))
    # Deduplicate while preserving order
    seen = set()
    uniq = []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


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
    assert isinstance(cfg.get("style"), (str, dict)), "Expected top-level 'style' (URL or style object)"
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
        assert isinstance(l.get("url"), str), f"Layer {l.get('id')} must define 'url'"
        if l["type"] == "image":
            coords = l.get("coordinates")
            assert isinstance(coords, list) and len(coords) == 4, f"Image layer {l['id']} needs 4 coordinates"
        if "start" in l: assert isinstance(l["start"], int)
        if "end" in l: assert isinstance(l["end"], int)


# ---------------------------------------------------------------------------
# STAC items & collections (basic conformance checks)
# ---------------------------------------------------------------------------

# Candidate item paths used in this repo (search both themed and flat item layouts)
ITEM_GLOBS = [
    "stac/items/*.json",
    "stac/items/dem/*.json",
    "stac/items/hillshade/*.json",
    "stac/items/overlays/*.json",
    "stac/items/vectors/*.json",
]

# Specific items we expect as the project matures (skip if missing during scaffold)
EXPECTED_ITEM_BASENAMES = {
    "ks_1m_dem_2018_2020.json",
    "ks_hillshade_2018_2020.json",
    "usgs_topo_larned_1894.json",
    "treaties_1854.json",
    "railroads_1900.json",
}

@pytest.mark.parametrize("item_path", glob_paths(*ITEM_GLOBS))
def test_stac_item_minimum(item_path: Path):
    item = read_json(item_path)
    assert item.get("stac_version"), f"Missing stac_version in {item_path}"
    assert item.get("type") == "Feature", f"STAC Item must have type=Feature: {item_path}"
    assert isinstance(item.get("id"), str) and item["id"], f"Missing id in {item_path}"
    assert "assets" in item and isinstance(item["assets"], dict) and item["assets"], f"Missing assets in {item_path}"
    assert "bbox" in item, f"Missing bbox in {item_path}"
    geom = item.get("geometry", {})
    assert geom.get("type") in {"Polygon", "MultiPolygon"}, f"Missing/invalid geometry in {item_path}"
    assert "links" in item and isinstance(item["links"], list), f"Missing links[] in {item_path}"

def test_expected_items_present_or_skipped():
    # If none of the expected items exist yet, skip with a helpful message.
    candidates = {p.name for p in glob_paths(*ITEM_GLOBS)}
    missing = sorted(EXPECTED_ITEM_BASENAMES - candidates)
    if missing:
        pytest.skip(f"Expected STAC items not present yet (ok during scaffolding): {', '.join(missing)}")


# Collections
COLLECTION_PATHS = existing_only([
    REPO / "stac" / "collections" / "elevation.json",
    REPO / "stac" / "collections" / "historic_topo.json",
    REPO / "stac" / "collections" / "vectors.json",
])

@pytest.mark.parametrize("collection_path", COLLECTION_PATHS or [REPO / "stac" / "collections" / "elevation.json"])
def test_stac_collection_minimum(collection_path: Path):
    if not collection_path.exists():
        pytest.skip(f"STAC collection not present yet: {collection_path}")
    col = read_json(collection_path)
    assert col.get("stac_version"), "Missing stac_version"
    assert col.get("type") == "Collection", "STAC Collection must have type=Collection"
    assert isinstance(col.get("id"), str) and col["id"], "Missing id"
    extent = col.get("extent", {})
    assert "spatial" in extent and "temporal" in extent, "Collection extent must have spatial+temporal"
    assert "links" in col and isinstance(col["links"], list), "Missing links[]"


# Optional: verify that item files referenced by collections actually exist (if declared)
def _collect_linked_item_hrefs(collection: dict) -> Set[str]:
    hrefs: Set[str] = set()
    for ln in collection.get("links", []):
        if ln.get("rel") == "item" and ln.get("href"):
            hrefs.add(ln["href"])
    return hrefs

@pytest.mark.parametrize("collection_path", COLLECTION_PATHS or [REPO / "stac" / "collections" / "elevation.json"])
def test_collection_links_item_files_exist(collection_path: Path):
    if not collection_path.exists():
        pytest.skip(f"STAC collection not present yet: {collection_path}")

    col = read_json(collection_path)
    hrefs = _collect_linked_item_hrefs(col)
    if not hrefs:
        pytest.skip(f"No item links declared in {collection_path.name}")

    base = collection_path.parent  # .../stac/collections
    for href in hrefs:
        # Accept common relative forms:
        #  - "../items/<theme>/<file>.json"
        #  - "../items/<file>.json"
        #  - "<file>.json" (basename)
        h = Path(href)
        candidates = [
            (base / ".." / "items" / h.name).resolve(),
            (base / ".." / "items" / h).resolve(),
        ]
        found = False
        for c in candidates:
            if c.exists():
                read_json(c)  # must parse cleanly
                found = True
                break
        if not found:
            pytest.skip(f"Linked item missing (ok during early scaffolding): {href}")


# ---------------------------------------------------------------------------
# KML well-formedness
# ---------------------------------------------------------------------------

KML_GLOBS = [
    "data/earth/*.kml",
    "data/earth/networklinks/*.kml",
    "web/earth/*.kml",
    "web/earth/networklinks/*.kml",
]

@pytest.mark.parametrize("kml_path", glob_paths(*KML_GLOBS))
def test_kml_well_formed(kml_path: Path):
    if not kml_path.exists():
        pytest.skip(f"KML not present yet: {kml_path}")
    try:
        ET.parse(kml_path)  # well-formedness only
    except ET.ParseError as e:
        raise AssertionError(f"Malformed KML: {kml_path}\n{e}") from e


# ---------------------------------------------------------------------------
# Checksum file format (COGs)
# ---------------------------------------------------------------------------

# Support both naming styles:
#   - <name>.tif.sha256  (GNU coreutils sha256sum format)
#   - <name>.sha256      (sidecar, same directory as .tif)
CHECKSUM_TARGETS = [
    # DEM
    (REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.tif"),
    # Hillshade
    (REPO / "data" / "cogs" / "hillshade" / "ks_hillshade_2018_2020.tif"),
    # Overlay example
    (REPO / "data" / "cogs" / "overlays" / "usgs_topo_larned_1894.tif"),
]

def _candidate_sha_files(tif: Path) -> List[Path]:
    return [
        tif.with_suffix(tif.suffix + ".sha256"),    # <name>.tif.sha256
        tif.with_suffix("").with_suffix(".sha256"), # <name>.sha256
    ]

@pytest.mark.parametrize("tif_path", CHECKSUM_TARGETS)
def test_sha256_file_format(tif_path: Path):
    if not tif_path.exists():
        pytest.skip(f"COG not present yet: {tif_path}")
    sha_candidates = existing_only(_candidate_sha_files(tif_path))
    if not sha_candidates:
        pytest.skip(f"Checksum not present yet for {tif_path}")
    # Prefer the .tif.sha256 if both exist
    sha_path = sha_candidates[0] if sha_candidates[0].name.endswith(".tif.sha256") else sha_candidates[-1]

    line = read_text(sha_path).strip()
    # Expect "<64hex><spaces/tabs>filename"
    m = re.match(r"^([A-Fa-f0-9]{64})\s+(.+)$", line)
    assert m, f"Checksum format invalid in {sha_path}: '{line}'"
    digest, fname = m.groups()

    # The filename referenced in the checksum must match the .tif name
    assert fname == tif_path.name, f"Checksum should reference {tif_path.name}, got {fname}"

    # And the referenced .tif must exist
    assert tif_path.exists(), f"Referenced file does not exist: {tif_path}"
