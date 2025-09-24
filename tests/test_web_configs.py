# pytest -q
# Validates web/app.config.json and web/layers.json against their JSON Schemas
# Adds cross-file consistency checks + gentle MapLibre paint sanity.

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Set
import pytest

try:
    from jsonschema import Draft202012Validator
except Exception as e:  # pragma: no cover
    pytest.skip(f"jsonschema not installed: {e}", allow_module_level=True)

REPO = Path(__file__).resolve().parents[1]
WEB = REPO / "web"
APP_CFG = WEB / "app.config.json"
LAYERS = WEB / "layers.json"
APP_SCHEMA = WEB / "config" / "app.config.schema.json"
LAYERS_SCHEMA = WEB / "config" / "layers.schema.json"

HEX_COLOR = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")

# --------------------------- helpers ---------------------------

def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))

def _layer_index(layers: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for L in layers:
        lid = L.get("id")
        if isinstance(lid, str):
            out[lid] = L
    return out

def _is_iso_date_or_none(s):
    if s is None:
        return True
    if not isinstance(s, str):
        return False
    # YYYY-MM-DD
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", s))

def _check_paint_for_layer(l: Dict[str, Any]) -> List[str]:
    """
    Soft checks for paint keys by logical render type.
    We don't hard-enforce full MapLibre schema here—just catch common mistakes.
    Returns list of error strings (empty if OK).
    """
    errs: List[str] = []
    if l.get("type") != "geojson":
        return errs
    paint = l.get("paint") or {}
    render = l.get("render")
    # Allow "implicit" render via keys
    if not render:
        if "line" in paint:   render = "line"
        elif "fill" in paint: render = "fill"
        elif "circle" in paint: render = "circle"

    def _hex_ok(v) -> bool:
        return isinstance(v, str) and (HEX_COLOR.match(v) or v.startswith("rgb") or v.startswith("hsl"))

    if render == "line":
        ln = paint.get("line", {})
        if "line-color" in ln and not _hex_ok(ln["line-color"]):
            errs.append("line.line-color must be a CSS color (e.g., #RRGGBB).")
        if "line-width" in ln and not isinstance(ln["line-width"], (int, float)):
            errs.append("line.line-width must be a number.")
        if "stroke-color" in ln:
            errs.append("Use 'line-color' (not 'stroke-color') for line layers.")
    elif render == "fill":
        fl = paint.get("fill", {})
        if "fill-color" in fl and not _hex_ok(fl["fill-color"]):
            errs.append("fill.fill-color must be a CSS color (e.g., #RRGGBB).")
        if "stroke-color" in fl:
            errs.append("Use 'fill-outline-color' (not 'stroke-color') for fill layers.")
    elif render == "circle":
        ci = paint.get("circle", {})
        if "circle-color" in ci and not _hex_ok(ci["circle-color"]):
            errs.append("circle.circle-color must be a CSS color.")
        if "circle-radius" in ci and not isinstance(ci["circle-radius"], (int, float)):
            errs.append("circle.circle-radius must be a number.")
    # If no render and no paint -> fine (style from defaults or app)
    return errs

# --------------------------- schema validation ---------------------------

@pytest.mark.parametrize("cfg_path,schema_path", [
    (APP_CFG, APP_SCHEMA),
    (LAYERS, LAYERS_SCHEMA),
])
def test_configs_validate(cfg_path: Path, schema_path: Path):
    if not cfg_path.exists():
        pytest.skip(f"{cfg_path} missing (scaffold stage)")
    if not schema_path.exists():
        pytest.skip(f"{schema_path} missing (schema not added)")
    cfg = load_json(cfg_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(cfg), key=lambda e: e.path)
    if errors:
        msg = "\n".join([f"- {'/'.join(map(str, e.path))}: {e.message}" for e in errors])
        pytest.fail(f"Schema validation failed for {cfg_path}:\n{msg}")

# --------------------------- intra-file sanity ---------------------------

def test_app_layers_ids_are_unique():
    if not APP_CFG.exists():
        pytest.skip("app.config.json missing")
    data = load_json(APP_CFG)
    ids = [ly.get("id") for ly in data.get("layers", [])]
    ids = [i for i in ids if isinstance(i, str)]
    assert len(ids) == len(set(ids)), "Duplicate layer IDs in app.config.json"

def test_layers_file_ids_are_unique():
    if not LAYERS.exists():
        pytest.skip("layers.json missing")
    data = load_json(LAYERS)
    ids = [ly.get("id") for ly in data.get("layers", [])]
    ids = [i for i in ids if isinstance(i, str)]
    assert len(ids) == len(set(ids)), "Duplicate layer IDs in layers.json"

@pytest.mark.parametrize("cfg_path", [APP_CFG, LAYERS])
def test_common_field_ranges(cfg_path: Path):
    if not cfg_path.exists():
        pytest.skip(f"{cfg_path} missing")
    data = load_json(cfg_path)
    layers = data.get("layers", [])
    for L in layers:
        # opacity
        if "opacity" in L:
            op = L["opacity"]
            assert isinstance(op, (int, float)) and 0 <= op <= 1, f"{cfg_path.name}:{L.get('id')} opacity must be 0..1"
        # zooms
        for k in ("minzoom", "maxzoom"):
            if k in L and L[k] is not None:
                assert isinstance(L[k], int) and 0 <= L[k] <= 24, f"{cfg_path.name}:{L.get('id')} {k} must be int 0..24"
        if L.get("minzoom") is not None and L.get("maxzoom") is not None:
            assert L["minzoom"] <= L["maxzoom"], f"{cfg_path.name}:{L.get('id')} minzoom must be <= maxzoom"
        # time
        t = L.get("time") or {"start": L.get("start"), "end": L.get("end")}
        if t:
            s, e = t.get("start"), t.get("end")
            assert _is_iso_date_or_none(s), f"{cfg_path.name}:{L.get('id')} time.start must be YYYY-MM-DD or null"
            assert _is_iso_date_or_none(e), f"{cfg_path.name}:{L.get('id')} time.end must be YYYY-MM-DD or null"

# --------------------------- paint sanity ---------------------------

@pytest.mark.parametrize("cfg_path", [APP_CFG, LAYERS])
def test_geojson_paint_sanity(cfg_path: Path):
    if not cfg_path.exists():
        pytest.skip(f"{cfg_path} missing")
    data = load_json(cfg_path)
    errs: List[str] = []
    for L in data.get("layers", []):
        errs += [f"{cfg_path.name}:{L.get('id')} → {m}" for m in _check_paint_for_layer(L)]
    if errs:
        pytest.fail("Paint validation errors:\n" + "\n".join(f"- {e}" for e in errs))

# --------------------------- cross-file consistency ---------------------------

def test_cross_file_layer_consistency():
    if not (APP_CFG.exists() and LAYERS.exists()):
        pytest.skip("app.config.json or layers.json missing")
    app = load_json(APP_CFG)
    lay = load_json(LAYERS)

    app_idx = _layer_index(app.get("layers", []))
    lay_idx = _layer_index(lay.get("layers", []))

    # 1) No conflicting duplicate IDs with different 'type'
    conflicts: List[str] = []
    for lid in set(app_idx) & set(lay_idx):
        t1 = app_idx[lid].get("type")
        t2 = lay_idx[lid].get("type")
        if t1 != t2:
            conflicts.append(f"'{lid}' type mismatch: app={t1} vs layers={t2}")
    assert not conflicts, "Layer ID/type conflicts between app.config.json and layers.json:\n- " + "\n- ".join(conflicts) if conflicts else ""

    # 2) Recommend (soft) that raster layers have url, geojson layers have path
    soft_errs: List[str] = []
    def _soft(cond: bool, msg: str):  # collect soft errs → single assertion
        if not cond:
            soft_errs.append(msg)

    for lid, L in {**app_idx, **lay_idx}.items():
        typ = L.get("type")
        if typ == "raster":
            _soft("url" in L and isinstance(L["url"], str) and L["url"], f"{lid}: expected raster.url to be present")
        elif typ == "geojson":
            _soft("path" in L and isinstance(L["path"], str) and L["path"], f"{lid}: expected geojson.path to be present")
    if soft_errs:
        pytest.fail("Config wiring issues (expected url/path by type):\n" + "\n".join(f"- {e}" for e in soft_errs))

# --------------------------- minimal presence checks ---------------------------

def test_defaults_bounds_shape():
    # Small guard that defaults.bounds has 4 numbers (if present)
    missing = []
    for pth in (APP_CFG, LAYERS):
        if not pth.exists():
            continue
        data = load_json(pth)
        df = data.get("defaults") or {}
        if "bounds" in df:
            b = df["bounds"]
            ok = isinstance(b, list) and len(b) == 4 and all(isinstance(x, (int, float)) for x in b)
            if not ok:
                missing.append(f"{pth.name}: defaults.bounds must be [minx,miny,maxx,maxy]")
    if missing:
        pytest.fail("\n".join(missing))
