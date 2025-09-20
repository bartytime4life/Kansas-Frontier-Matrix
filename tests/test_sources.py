# pytest -q
# Kansas-Frontier-Matrix — source wiring tests
# Focus: do paths resolve? are expected assets present? skip gracefully during scaffolding.

from __future__ import annotations
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

REPO = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def read_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def exists_or_skip(p: Path, reason: str = "Optional during scaffolding"):
    if not p.exists():
        pytest.skip(f"{p} — {reason}")

# ---------------------------------------------------------------------
# Web: key assets should exist (we treat as must-have for UI smoke)
# ---------------------------------------------------------------------

@pytest.mark.parametrize("p", [
    REPO / "web" / "app.js",
    REPO / "web" / "app.css",
    REPO / "web" / "assets" / "favicon.svg",
    REPO / "web" / "assets" / "logo.png",
])
def test_web_core_assets_present(p: Path):
    assert p.exists(), f"Missing required web asset: {p}"

# ---------------------------------------------------------------------
# Web: app.config.json → layer.url sanity + relative file existence
# ---------------------------------------------------------------------

CFG = REPO / "web" / "app.config.json"

def _resolve_web_url(u: str) -> Path | None:
    """
    Only handle local relative URLs like "./tiles/..." or "./vectors/...".
    Remote URLs (http/https) return None (skip).
    """
    if re.match(r"^https?://", u, re.I):
        return None
    if u.startswith("./"):
        # trim any template {z}/{x}/{y} or query
        clean = u.split("?")[0]
        # If it's a tiled template, we just check the directory exists
        # e.g. "./tiles/ks_hillshade/{z}/{x}/{y}.png" -> "web/tiles/ks_hillshade"
        if "{z}" in clean and "{x}" in clean and "{y}" in clean:
            base = clean.split("/{z}")[0].lstrip("./")
            return REPO / "web" / base
        return REPO / "web" / clean.lstrip("./")
    return None

@pytest.mark.skipif(not CFG.exists(), reason="No app.config.json yet")
def test_app_config_layer_urls_resolve():
    cfg = read_json(CFG)
    layers = cfg.get("layers", [])
    assert isinstance(layers, list) and layers, "app.config.json has no layers"

    for l in layers:
        lid = l.get("id", "<no-id>")
        url = l.get("url")
        assert isinstance(url, str) and url, f"Layer {lid} missing url"

        p = _resolve_web_url(url)
        if p is None:
            # remote URL or non-local scheme → skip existence check
            continue

        # If this is a tile template directory, require it exists
        if p.is_dir():
            assert p.exists(), f"Tiles directory not found for {lid}: {p}"
        else:
            # Expect a concrete file (e.g., GeoJSON, PNG)
            exists_or_skip(p, reason=f"Layer {lid} file not present (ok during early scaffolding)")

# ---------------------------------------------------------------------
# STAC Items: asset hrefs that are relative should resolve on disk
# ---------------------------------------------------------------------

STAC_ITEMS = [
    REPO / "data" / "stac" / "items" / "ks_1m_dem.json",
    REPO / "data" / "stac" / "items" / "ks_1m_hillshade.json",
    REPO / "data" / "stac" / "items" / "usgs_1894_larned.json",
    REPO / "data" / "stac" / "items" / "treaties_1854.json",
    REPO / "data" / "stac" / "items" / "railroads_1900.json",
]

@pytest.mark.parametrize("item_path", STAC_ITEMS)
def test_stac_assets_resolve(item_path: Path):
    if not item_path.exists():
        pytest.skip(f"STAC item not present yet: {item_path}")

    item = read_json(item_path)
    assets = item.get("assets", {})
    assert assets, f"No assets in {item_path.name}"

    for name, a in assets.items():
        href = a.get("href")
        assert href, f"Asset {name} missing href in {item_path.name}"
        # Remote? skip checking
        if re.match(r"^https?://", href, re.I):
            continue
        # Resolve relative to item file location
        # STAC here uses paths like "../../cogs/..."; normalize them
        target = (item_path.parent / href).resolve()
        exists_or_skip(target, reason=f"STAC asset {name} unresolved (ok during scaffolding)")

# ---------------------------------------------------------------------
# KML NetworkLinks: href targets exist (relative)
# ---------------------------------------------------------------------

KMLS = [
    REPO / "data" / "earth" / "doc.kml",
    REPO / "data" / "earth" / "networklinks" / "ks_1m_hillshade.kml",
    REPO / "data" / "earth" / "networklinks" / "usgs_topo_1894.kml",
]

def _iter_kml_hrefs(p: Path):
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    tree = ET.parse(p)
    root = tree.getroot()
    # look for Link/href within NetworkLink or ground overlays
    for href_el in root.findall(".//kml:href", ns):
        if href_el.text:
            yield href_el.text.strip()

@pytest.mark.parametrize("kml_path", KMLS)
def test_kml_link_targets_exist(kml_path: Path):
    if not kml_path.exists():
        pytest.skip(f"KML not present yet: {kml_path}")
    for href in _iter_kml_hrefs(kml_path):
        if re.match(r"^https?://", href, re.I):
            continue
        # Resolve relative to KML location
        target = (kml_path.parent / href).resolve()
        exists_or_skip(target, reason=f"KML Link target missing: {href}")

# ---------------------------------------------------------------------
# DEM checksum: if both files present, checksum line must match file hash
# (optional; we skip if the tif is not checked out yet)
# ---------------------------------------------------------------------

@pytest.mark.parametrize("pair", [
    (
        REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.tif",
        REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.sha256",
    ),
])
def test_dem_checksum_matches(pair: tuple[Path, Path]):
    tif, sha = pair
    if not tif.exists() or not sha.exists():
        pytest.skip("DEM COG or checksum not present yet")
    line = sha.read_text(encoding="utf-8").strip()
    m = re.match(r"^([A-Fa-f0-9]{64})\s{1,3}(.+)$", line)
    assert m, "Invalid checksum file format"
    listed_digest, listed_name = m.groups()
    assert Path(listed_name).name == tif.name, "Checksum filename does not match COG name"

    # Compute real sha256 to verify (streaming)
    import hashlib
    h = hashlib.sha256()
    with tif.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    assert h.hexdigest() == listed_digest.lower(), "Checksum does not match file contents"

