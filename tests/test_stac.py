# pytest -q
# Kansas-Frontier-Matrix — STAC-focused tests (upgraded)
# Deeper checks for Items & Collections beyond basic parsing.
# Skips gracefully when files are not yet present during scaffolding.

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any, Iterable, List, Tuple, Optional
import pytest

REPO = Path(__file__).resolve().parents[1]
ITEMS_DIR = REPO / "stac" / "items"
COLLS_DIR = REPO / "stac" / "collections"

# e.g., "1.0.0"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

# RFC3339/ISO8601 (Zulu), allow optional fractional seconds
# Examples: "1894-06-01T00:00:00Z", "2018-01-02T03:04:05.123Z"
ISO_ZULU = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")

# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------

def read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        raise AssertionError(f"Missing JSON file: {p}") from e
    except json.JSONDecodeError as e:
        raise AssertionError(f"Invalid JSON in {p}:\n{e}") from e

def list_json(dirpath: Path, recursive: bool = False) -> List[Path]:
    if not dirpath.exists():
        return []
    pat = "**/*.json" if recursive else "*.json"
    return sorted([p for p in dirpath.glob(pat) if p.is_file()])

def iso_or_none(s: Optional[str]) -> bool:
    return (s is None) or (isinstance(s, str) and bool(ISO_ZULU.match(s)))

def _flatten_coords(coords: Any) -> Iterable[Tuple[float, float]]:
    """
    Flatten Polygon or MultiPolygon coordinate arrays into (x,y) tuples.
    Polygon:        [ [ [x,y], ... ], [hole...], ... ]
    MultiPolygon:   [ [ [ [x,y], ... ], ... ], ... ]
    """
    # MultiPolygon
    if (
        isinstance(coords, list)
        and coords
        and isinstance(coords[0], list)
        and coords[0]
        and isinstance(coords[0][0], list)
        and coords[0][0]
        and isinstance(coords[0][0][0], (list, tuple))
    ):
        for poly in coords:
            for ring in poly:
                for xy in ring:
                    if isinstance(xy, (list, tuple)) and len(xy) >= 2:
                        yield float(xy[0]), float(xy[1])
        return

    # Polygon
    if (
        isinstance(coords, list)
        and coords
        and isinstance(coords[0], list)
        and coords[0]
        and isinstance(coords[0][0], (list, tuple))
    ):
        for ring in coords:
            for xy in ring:
                if isinstance(xy, (list, tuple)) and len(xy) >= 2:
                    yield float(xy[0]), float(xy[1])
        return

    # Fallback (defensive): try to interpret any nested [x,y]
    def _walk(v: Any):
        if isinstance(v, (list, tuple)) and len(v) >= 2 and all(isinstance(t, (int, float)) for t in v[:2]):
            yield float(v[0]), float(v[1])
        elif isinstance(v, (list, tuple)):
            for sub in v:
                yield from _walk(sub)
    yield from _walk(coords)

def bbox_from_geometry(geom: dict) -> tuple[float, float, float, float]:
    coords = geom.get("coordinates")
    pts = list(_flatten_coords(coords))
    assert pts, "Geometry contains no numeric coordinates"
    xs, ys = zip(*pts)
    return (min(xs), min(ys), max(xs), max(ys))

def _normalize_collection_bbox(spatial_bbox: Any) -> list[list[float]]:
    """
    STAC allows bbox to be a single [minx,miny,maxx,maxy] or a list of such lists.
    Return as list-of-lists for uniform checks.
    """
    if isinstance(spatial_bbox, list):
        # single bbox
        if len(spatial_bbox) == 4 and all(isinstance(v, (int, float)) for v in spatial_bbox):
            b = list(map(float, spatial_bbox))
            return [b]
        # list-of-bbox
        if spatial_bbox and isinstance(spatial_bbox[0], list):
            out: list[list[float]] = []
            for b in spatial_bbox:
                if isinstance(b, list) and len(b) >= 4 and all(isinstance(v, (int, float)) for v in b[:4]):
                    out.append(list(map(float, b[:4])))
            return out
    return []

def _normalize_temporal_interval(interval: Any) -> list[list[Optional[str]]]:
    """
    STAC temporal interval is list of [start, end] values; values may be ISO8601 strings or null.
    Return as list-of-[start,end] with None or strings.
    """
    out: list[list[Optional[str]]] = []
    if isinstance(interval, list):
        for i in interval:
            if isinstance(i, list) and len(i) >= 2:
                s, e = i[0], i[1]
                s2 = s if s is None or isinstance(s, str) else None
                e2 = e if e is None or isinstance(e, str) else None
                out.append([s2, e2])
    return out

def _looks_like_cog_mediatype(m: str) -> bool:
    """
    Heuristics for GeoTIFF/COG mediatype hints commonly used in STAC.
    Accept any of:
      - "image/tiff; application=geotiff; profile=cloud-optimized"
      - "image/tiff; application=geotiff"
      - "image/geotiff"
      - "image/tiff" (nudge to geotiff in assert message)
    """
    m = (m or "").lower()
    return ("geotiff" in m) or m.startswith("image/geotiff") or m.startswith("image/tiff")

def approx_encloses(bbox_outer: list[float], bbox_inner: tuple[float, float, float, float], eps: float = 1e-9) -> bool:
    return (
        bbox_outer[0] <= bbox_inner[0] + eps and
        bbox_outer[1] <= bbox_inner[1] + eps and
        bbox_outer[2] + eps >= bbox_inner[2] and
        bbox_outer[3] + eps >= bbox_inner[3]
    )

def _load_collections_by_id() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in list_json(COLLS_DIR, recursive=False):
        col = read_json(p)
        cid = col.get("id")
        if isinstance(cid, str) and cid:
            out[cid] = col
    return out

# --------------------------------------------------------------------------------------
# Dynamic discovery (so new items/collections are picked up automatically)
# --------------------------------------------------------------------------------------

ALL_ITEMS = list_json(ITEMS_DIR, recursive=True)
ALL_COLLS = list_json(COLLS_DIR, recursive=False)

# If none exist yet, mark the whole module as skipped to avoid noise
pytestmark = pytest.mark.skipif(
    not (ALL_ITEMS or ALL_COLLS),
    reason="No STAC files present yet (scaffolding stage)"
)

# --------------------------------------------------------------------------------------
# Repo-wide invariants
# --------------------------------------------------------------------------------------

def test_item_ids_unique():
    if not ALL_ITEMS:
        pytest.skip("No items yet")
    ids = []
    for p in ALL_ITEMS:
        itm = read_json(p)
        iid = itm.get("id")
        assert isinstance(iid, str) and iid, f"{p.name}: missing id"
        ids.append(iid)
        assert p.stem == iid, f"{p.name}: id should match filename stem"
    assert len(ids) == len(set(ids)), "Duplicate STAC Item ids detected"

# --------------------------------------------------------------------------------------
# Collections — conformance-ish checks
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("p", ALL_COLLS)
def test_collection_core(p: Path):
    col = read_json(p)
    assert col.get("type") == "Collection", f"{p.name}: type must be 'Collection'"
    assert SEMVER.match(col.get("stac_version", "") or ""), f"{p.name}: invalid or missing stac_version"
    assert isinstance(col.get("id"), str) and col["id"], f"{p.name}: missing id"

    # extent
    extent = col.get("extent") or {}
    spatial = extent.get("spatial") or {}
    temporal = extent.get("temporal") or {}

    # spatial.bbox
    sb = _normalize_collection_bbox(spatial.get("bbox"))
    assert sb, f"{p.name}: extent.spatial.bbox required and must be [minx,miny,maxx,maxy] or list of such"
    for b in sb:
        assert len(b) >= 4, f"{p.name}: bbox must have at least 4 numbers"
        # b already cast to float in normalizer
        assert all(isinstance(v, float) for v in b[:4]), f"{p.name}: bbox values must be numeric"
        assert b[0] <= b[2] and b[1] <= b[3], f"{p.name}: bbox min must be <= max"

    # temporal.interval
    ti = _normalize_temporal_interval(temporal.get("interval"))
    assert ti, f"{p.name}: extent.temporal.interval required"
    for (s, e) in ti:
        assert iso_or_none(s), f"{p.name}: temporal.start must be ISO8601 Z or null"
        assert iso_or_none(e), f"{p.name}: temporal.end must be ISO8601 Z or null"
        if s and e:
            assert s <= e, f"{p.name}: temporal.start must be <= temporal.end"

    # links presence
    links = col.get("links")
    assert isinstance(links, list), f"{p.name}: links[] required"
    rels = {ln.get("rel") for ln in links}
    for r in ("self", "root", "parent"):
        assert r in rels, f"{p.name}: expected a '{r}' link"
    # if href present, ensure it's a non-empty string
    for ln in links:
        if "href" in ln:
            assert isinstance(ln["href"], str) and ln["href"], f"{p.name}: link.href must be a non-empty string"

    # recommended metadata (soft checks)
    if "license" in col:
        assert isinstance(col["license"], str) and col["license"], f"{p.name}: license, if present, must be non-empty string"
    if "keywords" in col:
        kw = col["keywords"]
        assert isinstance(kw, list) and all(isinstance(k, str) for k in kw), f"{p.name}: keywords must be list[str]"
    if "providers" in col:
        prov = col["providers"]
        assert isinstance(prov, list), f"{p.name}: providers must be a list"
        for i, pr in enumerate(prov):
            assert isinstance(pr, dict), f"{p.name}: providers[{i}] must be an object"
            if "name" in pr:
                assert isinstance(pr["name"], str) and pr["name"], f"{p.name}: providers[{i}].name must be string"
            if "roles" in pr:
                assert isinstance(pr["roles"], list) and all(isinstance(r, str) for r in pr["roles"]), f"{p.name}: providers[{i}].roles must be list[str]"

    # item_assets mapping (if present) must be dict of asset defs
    ia = col.get("item_assets")
    if ia is not None:
        assert isinstance(ia, dict), f"{p.name}: item_assets must be a dict"
        for k, v in ia.items():
            assert isinstance(k, str) and isinstance(v, dict), f"{p.name}: item_assets['{k}'] must be dict"
            assert "type" in v and "roles" in v, f"{p.name}: item_assets['{k}'] should declare type and roles"
            assert isinstance(v["type"], str) and v["type"], f"{p.name}: item_assets['{k}'].type must be string"
            assert isinstance(v["roles"], list) and all(isinstance(r, str) for r in v["roles"]), f"{p.name}: item_assets['{k}'].roles must be list[str]"

# --------------------------------------------------------------------------------------
# Items — conformance-ish checks
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("p", ALL_ITEMS)
def test_item_core(p: Path):
    item = read_json(p)

    # Structural
    assert item.get("type") == "Feature", f"{p.name}: STAC Item must be type=Feature"
    assert SEMVER.match(item.get("stac_version", "") or ""), f"{p.name}: invalid or missing stac_version"
    assert isinstance(item.get("id"), str) and item["id"], f"{p.name}: missing id"
    # filename stem = id (convention; helpful for humans)
    assert p.stem == item["id"], f"{p.name}: id should match filename stem"

    # bbox & geometry
    assert isinstance(item.get("bbox"), list) and len(item["bbox"]) >= 4, f"{p.name}: bbox must be [minx,miny,maxx,maxy]"
    item_bbox = list(map(float, item["bbox"][:4]))
    assert item_bbox[0] <= item_bbox[2] and item_bbox[1] <= item_bbox[3], f"{p.name}: bbox min must be <= max"

    geom = item.get("geometry") or {}
    assert geom.get("type") in {"Polygon", "MultiPolygon"}, f"{p.name}: geometry must be Polygon or MultiPolygon"
    assert isinstance(geom.get("coordinates"), list) and geom["coordinates"], f"{p.name}: geometry coordinates must be non-empty"

    # geometry should fit inside bbox (tolerance)
    geom_bbox = bbox_from_geometry(geom)
    assert approx_encloses(item_bbox, geom_bbox), \
        f"{p.name}: bbox should enclose geometry (bbox={item_bbox}, geom_bbox={geom_bbox})"

    # links sanity
    links = item.get("links") or []
    assert isinstance(links, list), f"{p.name}: links must be a list"
    link_rels = {ln.get("rel") for ln in links}
    for r in ("self", "root", "parent"):
        assert r in link_rels, f"{p.name}: expected a '{r}' link"
    for ln in links:
        if "href" in ln:
            assert isinstance(ln["href"], str) and ln["href"], f"{p.name}: link.href must be a non-empty string"

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

    # proj:* (optional sanity)
    proj_epsg = item.get("proj:epsg") or props.get("proj:epsg")
    if proj_epsg is not None:
        assert isinstance(proj_epsg, int), f"{p.name}: proj:epsg should be an integer code"
    for opt_key in ("proj:bbox", "proj:shape", "proj:transform"):
        if opt_key in item or opt_key in props:
            val = (item.get(opt_key) if opt_key in item else props.get(opt_key))
            assert val is not None, f"{p.name}: {opt_key} present but null"

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
        assert roles is None or (isinstance(roles, list) and all(isinstance(r, str) for r in roles)), f"{p.name}: asset '{name}' roles should be a list[str]"

        # If it's a GeoTIFF, ensure the media type hints GeoTIFF/COG best practice
        href_l = a["href"].lower()
        if href_l.endswith((".tif", ".tiff")):
            m = a["type"]
            assert _looks_like_cog_mediatype(m), (
                f"{p.name}: asset '{name}' TIFF should declare a GeoTIFF media type "
                f"(e.g., 'image/tiff; application=geotiff; profile=cloud-optimized')"
            )

    # If "collection" is declared, it should match an existing collection id
    if "collection" in item:
        assert isinstance(item["collection"], str) and item["collection"], f"{p.name}: collection must be a non-empty string when present"
        all_colls = _load_collections_by_id()
        assert item["collection"] in all_colls, f"{p.name}: collection='{item['collection']}' does not match any collections in {COLLS_DIR}"

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
    for href in hrefs:
        target = ITEMS_DIR / Path(href).name
        assert target.exists(), f"{p.name}: linked item not found at {target}"
        itm = read_json(target)
        assert itm.get("type") == "Feature", f"{target.name}: must be a STAC Item (Feature)"
        assert SEMVER.match(itm.get("stac_version", "") or ""), f"{target.name}: missing/invalid stac_version"
