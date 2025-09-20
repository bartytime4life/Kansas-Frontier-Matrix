# pytest -q
# Kansas-Frontier-Matrix — STAC-focused tests
# Deeper checks for Items & Collections beyond basic parsing.
# Skips gracefully when files are not yet present during scaffolding.

from __future__ import annotations
import json
import math
import re
from pathlib import Path
import pytest

REPO = Path(__file__).resolve().parents[1]
ITEMS_DIR = REPO / "data" / "stac" / "items"
COLLS_DIR = REPO / "data" / "stac" / "collections"

SEMVER = re.compile(r"^\d+\.\d+\.\d+")
ISO_DT = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
)

# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------

def read_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))

def list_json(dirpath: Path) -> list[Path]:
    return sorted([p for p in (dirpath.glob("*.json") if dirpath.exists() else []) if p.is_file()])

def approx(a: float, b: float, eps: float = 1e-9) -> bool:
    return abs(a - b) <= eps

def bbox_from_polygon(coords: list) -> tuple[float, float, float, float]:
    """
    Compute bbox (minx, miny, maxx, maxy) from Polygon or MultiPolygon coordinates.
    """
    xs, ys = [], []
    def collect(ring):
        for (x, y) in ring:
            xs.append(float(x)); ys.append(float(y))
    # Polygon: [ [ [x,y], ... ] , ...holes ]
    # MultiPolygon: [ [ [ [x,y], ... ] ], ... ]
    if isinstance(coords, list) and coords and isinstance(coords[0], list):
        if coords and coords and isinstance(coords[0][0], list) and coords[0] and isinstance(coords[0][0][0], (int, float)):
            # Polygon
            for ring in coords:
                collect(ring)
        else:
            # MultiPolygon
            for poly in coords:
                for ring in poly:
                    collect(ring)
    return (min(xs), min(ys), max(xs), max(ys))

def iso_or_none(s: str | None) -> bool:
    return (s is None) or bool(ISO_DT.match(s))

# --------------------------------------------------------------------------------------
# Dynamic discovery (so new items/collections are picked up automatically)
# --------------------------------------------------------------------------------------

ALL_ITEMS = list_json(ITEMS_DIR)
ALL_COLLS = list_json(COLLS_DIR)

# If none exist yet, mark the whole module as skipped to avoid noise
pytestmark = pytest.mark.skipif(
    not (ALL_ITEMS or ALL_COLLS),
    reason="No STAC files present yet (scaffolding stage)"
)

# --------------------------------------------------------------------------------------
# Collections — conformance-ish checks
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("p", ALL_COLLS)
def test_collection_core(p: Path):
    col = read_json(p)
    assert col.get("type") == "Collection", f"{p.name}: type must be 'Collection'"
    assert SEMVER.match(col.get("stac_version", "")), f"{p.name}: invalid or missing stac_version"
    assert isinstance(col.get("id"), str) and col["id"], f"{p.name}: missing id"

    # extent
    extent = col.get("extent") or {}
    spatial = extent.get("spatial") or {}
    temporal = extent.get("temporal") or {}
    assert "bbox" in spatial and isinstance(spatial["bbox"], list) and spatial["bbox"], f"{p.name}: extent.spatial.bbox required"
    assert "interval" in temporal and isinstance(temporal["interval"], list) and temporal["interval"], f"{p.name}: extent.temporal.interval required"

    # links presence
    assert isinstance(col.get("links"), list), f"{p.name}: links[] required"
    # self/root/parent should exist (not strictly required by spec, but good practice)
    rels = {ln.get("rel") for ln in col["links"]}
    for r in ("self", "root", "parent"):
        assert r in rels, f"{p.name}: expected a '{r}' link"

    # item_assets mapping (if present) must be dict of asset defs
    ia = col.get("item_assets")
    if ia is not None:
        assert isinstance(ia, dict), f"{p.name}: item_assets must be a dict"
        for k, v in ia.items():
            assert isinstance(k, str) and isinstance(v, dict), f"{p.name}: item_assets['{k}'] must be dict"
            assert "type" in v and "roles" in v, f"{p.name}: item_assets['{k}'] should declare type and roles"

# --------------------------------------------------------------------------------------
# Items — conformance-ish checks
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("p", ALL_ITEMS)
def test_item_core(p: Path):
    item = read_json(p)

    # Structural
    assert item.get("type") == "Feature", f"{p.name}: STAC Item must be type=Feature"
    assert SEMVER.match(item.get("stac_version", "")), f"{p.name}: invalid or missing stac_version"
    assert isinstance(item.get("id"), str) and item["id"], f"{p.name}: missing id"
    # filename stem = id (convention; helpful for humans)
    assert p.stem == item["id"], f"{p.name}: id should match filename stem"

    # bbox & geometry
    assert isinstance(item.get("bbox"), list) and len(item["bbox"]) == 4, f"{p.name}: bbox must be [minx,miny,maxx,maxy]"
    geom = item.get("geometry") or {}
    assert geom.get("type") in {"Polygon", "MultiPolygon"}, f"{p.name}: geometry must be Polygon or MultiPolygon"
    assert isinstance(geom.get("coordinates"), list) and geom["coordinates"], f"{p.name}: geometry coordinates must be non-empty"

    # geometry should fit inside bbox (tolerance)
    bx = item["bbox"]
    gx = bbox_from_polygon(geom["coordinates"])
    eps = 1e-6
    assert bx[0] <= gx[0] + eps and bx[1] <= gx[1] + eps and bx[2] + eps >= gx[2] and bx[3] + eps >= gx[3], \
        f"{p.name}: bbox should enclose geometry (bbox={bx}, geom_bbox={gx})"

    # links sanity
    links = item.get("links") or []
    assert isinstance(links, list), f"{p.name}: links must be a list"
    link_rels = {ln.get("rel") for ln in links}
    for r in ("self", "root", "parent"):
        assert r in link_rels, f"{p.name}: expected a '{r}' link"

    # properties: allow either datetime OR (start_datetime and/or end_datetime)
    props = item.get("properties") or {}
    dt = props.get("datetime")
    sdt = props.get("start_datetime")
    edt = props.get("end_datetime")
    assert dt or sdt or edt, f"{p.name}: must have datetime or start/end datetime"
    assert iso_or_none(dt), f"{p.name}: properties.datetime must be ISO8601 Z"
    assert iso_or_none(sdt), f"{p.name}: properties.start_datetime must be ISO8601 Z"
    assert iso_or_none(edt), f"{p.name}: properties.end_datetime must be ISO8601 Z"
    if sdt and edt:
        assert sdt <= edt, f"{p.name}: start_datetime must be <= end_datetime"

    # proj:epsg may be at top-level or inside properties depending on authoring;
    # warn if missing but do not fail (historic scans may be unprojected/assumed WGS84)
    proj_epsg = item.get("proj:epsg") or props.get("proj:epsg")
    if proj_epsg is not None:
        assert isinstance(proj_epsg, int), f"{p.name}: proj:epsg should be an integer code"

    # assets present with basic media types & roles
    assets = item.get("assets") or {}
    assert isinstance(assets, dict) and assets, f"{p.name}: assets must be non-empty dict"
    for name, a in assets.items():
        assert isinstance(a, dict), f"{p.name}: asset '{name}' must be a dict"
        assert "href" in a and isinstance(a["href"], str) and a["href"], f"{p.name}: asset '{name}' must have href"
        # media type recommended
        assert "type" in a and isinstance(a["type"], str) and a["type"], f"{p.name}: asset '{name}' should have media type"
        # roles recommended
        roles = a.get("roles")
        assert roles is None or isinstance(roles, list), f"{p.name}: asset '{name}' roles should be a list"

        # If it's a GeoTIFF, ensure the media type hints COG (best practice)
        if a["href"].lower().endswith((".tif", ".tiff")):
            # do not hard-fail: just nudge toward COG profile in type string
            assert "geotiff" in a["type"].lower(), f"{p.name}: asset '{name}' TIFF should declare geotiff media type"
            # Optional: COG profile hint
            # (no assert; teams sometimes omit 'profile=cloud-optimized')

# --------------------------------------------------------------------------------------
# Cross-check: items referenced by collections (if any 'item' links present)
# --------------------------------------------------------------------------------------

def _collect_linked_items_from_collection(col: dict) -> list[str]:
    hrefs = []
    for ln in col.get("links", []):
        if ln.get("rel") == "item" and isinstance(ln.get("href"), str):
            hrefs.append(ln["href"])
    return hrefs

@pytest.mark.parametrize("p", ALL_COLLS)
def test_collection_item_links_point_to_items_folder(p: Path):
    col = read_json(p)
    hrefs = _collect_linked_items_from_collection(col)
    if not hrefs:
        pytest.skip(f"{p.name}: no 'item' links declared (ok if collection is empty)")

    # Normalize to items/ by filename; allow relative paths in link
    items_dir = ITEMS_DIR
    for href in hrefs:
        target = items_dir / Path(href).name
        assert target.exists(), f"{p.name}: linked item not found at {target}"
        # And the file itself must be a valid STAC Item (parse reuses core test)
        itm = read_json(target)
        assert itm.get("type") == "Feature", f"{target.name}: must be a STAC Item (Feature)"
        assert SEMVER.match(itm.get("stac_version", "")), f"{target.name}: missing/invalid stac_version"

