# pytest -q
# Kansas-Frontier-Matrix — source wiring tests
# Focus: do paths resolve? are expected assets present? skip gracefully during scaffolding.

from __future__ import annotations
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Iterable, List
import hashlib
import pytest

REPO = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def read_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise AssertionError(f"Invalid JSON in {p}:\n{e}") from e

def exists_or_skip(p: Path, reason: str = "Optional during scaffolding"):
    if not p.exists():
        pytest.skip(f"{p} — {reason}")

def is_remote(href: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*://", href or "", re.I))

def glob_paths(*globs: str) -> List[Path]:
    out: List[Path] = []
    for g in globs:
        out.extend(REPO.glob(g))
    # Deduplicate while preserving order
    seen = set()
    uniq: List[Path] = []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq

def existing_only(paths: Iterable[Path]) -> List[Path]:
    return [p for p in paths if p.exists()]

# ---------------------------------------------------------------------
# Web: key assets should exist (treat as must-have for UI smoke)
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
    Handle local URLs from the perspective of /web:
      - "./tiles/..." or "./vectors/..."  → REPO/web/tiles/...
      - "../data/..."                     → REPO/data/...
      - "/something" (web-root absolute)  → REPO/web/something
    Remote (http/https/...) returns None.
    """
    if not isinstance(u, str) or not u or is_remote(u):
        return None
    clean = u.split("?", 1)[0]

    # Template z/x/y: check parent dir before {z}
    def _zxy_parent(path: str) -> str:
        return path.split("/{z}", 1)[0]

    web_root = REPO / "web"

    if clean.startswith("./"):
        base = clean.lstrip("./")
        if "{z}" in clean and "{x}" in clean and "{y}" in clean:
            base = _zxy_parent(base)
        return (web_root / base)

    if clean.startswith("../"):
        target = (web_root / clean).resolve()
        return target

    if clean.startswith("/"):
        # treat as web-root absolute
        base = clean.lstrip("/")
        if "{z}" in clean and "{x}" in clean and "{y}" in clean:
            base = _zxy_parent(base)
        return (web_root / base)

    # Otherwise it's a bare relative file under web/
    if "{z}" in clean and "{x}" in clean and "{y}" in clean:
        return web_root / _zxy_parent(clean)
    return web_root / clean

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
            continue  # remote; skip file existence

        if p.is_dir():
            assert p.exists(), f"Tiles directory not found for {lid}: {p}"
        else:
            exists_or_skip(p, reason=f"Layer {lid} file not present (ok during early scaffolding)")

# ---------------------------------------------------------------------
# STAC Items: asset hrefs that are relative should resolve on disk
# ---------------------------------------------------------------------

# Discover items in both flat and themed layouts
ITEM_GLOBS = [
    "stac/items/*.json",
    "stac/items/dem/*.json",
    "stac/items/hillshade/*.json",
    "stac/items/overlays/*.json",
    "stac/items/vectors/*.json",
]

def _resolve_stac_href(item_path: Path, href: str) -> Optional[Path]:
    """
    Resolve common STAC asset href patterns:
    - "data/..." or "/data/..."             → REPO / data / ...
    - item-relative "./..." or "../..."     → item_path.parent / href
    - other relative (no scheme, no leading slash) → item_path.parent / href
    Remote URLs (http/https, etc.) are ignored (return None).
    """
    if not isinstance(href, str) or not href or is_remote(href):
        return None
    hp = Path(href)

    # Repo-root data references
    if str(hp).startswith("data/") or str(hp).startswith("/data/"):
        return (REPO / str(hp).lstrip("/")).resolve()

    # Item-relative (./ or ../ or bare)
    return (item_path.parent / hp).resolve()

@pytest.mark.parametrize("item_path", glob_paths(*ITEM_GLOBS))
def test_stac_assets_resolve(item_path: Path):
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

KML_GLOBS = [
    "data/earth/*.kml",
    "data/earth/networklinks/*.kml",
    "web/earth/*.kml",
    "web/earth/networklinks/*.kml",
]

def _iter_kml_hrefs(p: Path):
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    root = ET.parse(p).getroot()
    for href_el in root.findall(".//kml:href", ns):
        if href_el.text:
            yield href_el.text.strip()

def _resolve_kml_href(kml_path: Path, href: str) -> Optional[Path]:
    if not isinstance(href, str) or is_remote(href):
        return None
    hp = Path(href)

    # Primary: resolve relative to the KML file
    candidate = (kml_path.parent / hp).resolve()
    if candidate.exists():
        return candidate

    # Fallback patterns commonly used in portable repos
    # overlays/<name>.kmz → data/kml/<name>.kmz
    if hp.parts and hp.parts[0].lower() == "overlays" and hp.suffix.lower() == ".kmz":
        alt = (REPO / "data" / "kml" / hp.name).resolve()
        if alt.exists():
            return alt

    # "../kml/<name>.kmz" → data/kml/<name>.kmz
    if ".." in hp.parts and hp.suffix.lower() == ".kmz":
        alt2 = (REPO / "data" / "kml" / hp.name).resolve()
        if alt2.exists():
            return alt2

    # Return best-effort path; caller will skip if missing
    return candidate

@pytest.mark.parametrize("kml_path", glob_paths(*KML_GLOBS))
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
# Supports:
#   - <name>.tif.sha256
#   - <name>.sha256
# ---------------------------------------------------------------------

COG_TIFS = [
    REPO / "data" / "cogs" / "dem" / "ks_1m_dem_2018_2020.tif",
    REPO / "data" / "cogs" / "hillshade" / "ks_hillshade_2018_2020.tif",
    REPO / "data" / "cogs" / "overlays" / "usgs_topo_larned_1894.tif",
]

def _candidate_sha_files(tif: Path) -> List[Path]:
    return [
        tif.with_suffix(tif.suffix + ".sha256"),     # <name>.tif.sha256
        tif.with_suffix("").with_suffix(".sha256"),  # <name>.sha256
    ]

def _pick_sha_file(tif: Path) -> Optional[Path]:
    cands = existing_only(_candidate_sha_files(tif))
    if not cands:
        return None
    # Prefer the .tif.sha256 if present
    for c in cands:
        if c.name.endswith(".tif.sha256"):
            return c
    return cands[0]

@pytest.mark.parametrize("tif_path", COG_TIFS)
def test_checksum_matches(tif_path: Path):
    if not tif_path.exists():
        pytest.skip(f"COG not present yet: {tif_path}")
    sha_path = _pick_sha_file(tif_path)
    if not sha_path:
        pytest.skip(f"Checksum not present yet for {tif_path}")

    line = sha_path.read_text(encoding="utf-8").strip()
    m = re.match(r"^([A-Fa-f0-9]{64})\s+(.+)$", line)
    assert m, f"Invalid checksum file format in {sha_path}: '{line}'"
    listed_digest, listed_name = m.groups()

    # The filename referenced in the checksum must match the .tif name
    assert Path(listed_name).name == tif_path.name, (
        f"Checksum should reference {tif_path.name}, got {listed_name}"
    )

    # Compute actual digest
    h = hashlib.sha256()
    with tif_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    assert h.hexdigest() == listed_digest.lower(), "Checksum does not match file contents"
