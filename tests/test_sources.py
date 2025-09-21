# pytest -q
# Kansas-Frontier-Matrix — source wiring tests
# Focus: do paths resolve? are expected assets present? skip gracefully during scaffolding.

from __future__ import annotations
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional
import hashlib
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

def is_remote(href: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*://", href, re.I))

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
# Web: app.config.json → layer.url sanity + local existence (when applicable)
# ---------------------------------------------------------------------

CFG = REPO / "web" / "app.config.json"

def _resolve_web_url(u: str) -> Optional[Path]:
    """
    Handle local relative URLs like "./tiles/..." or "./vectors/..." from web/.
    Remote URLs return None (skip).
    """
    if is_remote(u):
        return None
    if u.startswith("./"):
        clean = u.split("?")[0]
        # If tiled template, check the directory before {z}
        if "{z}" in clean and "{x}" in clean and "{y}" in clean:
            base = clean.split("/{z}")[0].lstrip("./")
            return (REPO / "web" / base)
        return (REPO / "web" / clean.lstrip("./"))
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
            continue  # remote or non-local scheme → skip file existence

        if p.is_dir():
            assert p.exists(), f"Tiles directory not found for {lid}: {p}"
        else:
            exists_or_skip(p, reason=f"Layer {lid} file not present (ok during early scaffolding)")

# ---------------------------------------------------------------------
# STAC Items: asset hrefs that are relative should resolve on disk
# ---------------------------------------------------------------------

STAC_ITEMS = [
    REPO / "data" / "stac" / "items" / "dem" / "ks_1m_dem_2018_2020.json",
    REPO / "data" / "stac" / "items" / "hillshade" / "ks_hillshade_2018_2020.json",
    REPO / "data" / "stac" / "items" / "overlays" / "usgs_topo_larned_1894.json",
    REPO / "data" / "stac" / "items" / "vectors" / "treaties_1854.json",
    REPO / "data" / "stac" / "items" / "vectors" / "railroads_1900.json",
]

def _resolve_stac_href(item_path: Path, href: str) -> Optional[Path]:
    """
    Resolve common STAC asset href patterns:
    - absolute repo-relative like "data/..." → REPO / href
    - relative like "../../cogs/..." → item_path.parent / href
    Remote URLs are ignored (return None).
    """
    if is_remote(href):
        return None
    hp = Path(href)
    if str(hp).startswith("data/"):
        return (REPO / hp).resolve()
    return (item_path.parent / hp).resolve()

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
        target = _resolve_stac_href(item_path, href)
        if target is None:
            continue  # remote
        exists_or_skip(target, reason=f"STAC asset {name} unresolved (ok during scaffolding)")

# ---------------------------------------------------------------------
# KML NetworkLinks: href targets exist (relative), with repo fallbacks
# ---------------------------------------------------------------------

KMLS = [
    REPO / "data" / "earth" / "doc.kml",
    REPO / "data" / "earth" / "networklinks" / "ks_1m_hillshade.kml",
    REPO / "data" / "earth" / "networklinks" / "usgs_topo_1894.kml",
]

def _iter_kml_hrefs(p: Path):
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    root = ET.parse(p).getroot()
    for href_el in root.findall(".//kml:href", ns):
        if href_el.text:
            yield href_el.text.strip()

def _resolve_kml_href(kml_path: Path, href: str) -> Optional[Path]:
    if is_remote(href):
        return None
    hp = Path(href)
    # First: resolve relative to the KML file
    candidate = (kml_path.parent / hp).resolve()
    if candidate.exists():
        return candidate
    # Fallback for portable KMZ wiring: "overlays/<name>.kmz" lives in repo "data/kml/<name>.kmz"
    if hp.parts and hp.parts[0] == "overlays" and hp.suffix.lower() == ".kmz":
        alt = (REPO / "data" / "kml" / hp.name).resolve()
        if alt.exists():
            return alt
    # Fallback for "../kml/<name>.kmz" already absolute-ish from doc.kml
    if ".." in hp.parts and hp.suffix.lower() == ".kmz":
        alt2 = (REPO / "data" / "kml" / hp.name).resolve()
        if alt2.exists():
            return alt2
    return candidate  # return best-effort path (exists_or_skip will skip if missing)

@pytest.mark.parametrize("kml_path", KMLS)
def test_kml_link_targets_exist(kml_path: Path):
    if not kml_path.exists():
        pytest.skip(f"KML not present yet: {kml_path}")
    for href in _iter_kml_hrefs(kml_path):
        target = _resolve_kml_href(kml_path, href)
        if target is None:
            continue
        exists_or_skip(target, reason=f"KML Link target missing: {href}")

# ---------------------------------------------------------------------
# Checksum verification: if both files present, contents must match hash
# ---------------------------------------------------------------------

CHECKSUM_PAIRS = [
    (
        REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.tif",
        REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.tif.sha256",
    ),
    (
        REPO / "data" / "cogs" / "hillshade" / "ks_hillshade_2018_2020.tif",
        REPO / "data" / "cogs" / "hillshade" / "ks_hillshade_2018_2020.tif.sha256",
    ),
    (
        REPO / "data" / "cogs" / "overlays" / "usgs_topo_larned_1894.tif",
        REPO / "data" / "cogs" / "overlays" / "usgs_topo_larned_1894.tif.sha256",
    ),
]

@pytest.mark.parametrize("tif,sha", CHECKSUM_PAIRS)
def test_checksum_matches(tif: Path, sha: Path):
    if not tif.exists() or not sha.exists():
        pytest.skip("COG or checksum not present yet")
    line = sha.read_text(encoding="utf-8").strip()
    m = re.match(r"^([A-Fa-f0-9]{64})\s+(.+)$", line)
    assert m, f"Invalid checksum file format in {sha}"
    listed_digest, listed_name = m.groups()
    assert Path(listed_name).name == tif.name, "Checksum line does not reference the expected .tif"

    h = hashlib.sha256()
    with tif.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    assert h.hexdigest() == listed_digest.lower(), "Checksum does not match file contents"
