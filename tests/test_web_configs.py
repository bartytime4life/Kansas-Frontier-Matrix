# pytest -q
# Validates web/app.config.json (+ optional web/layers.json) and their wiring.
# Adds cross-file checks, path sanity, legend↔paint alignment, and gentle MapLibre paint checks.

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple
import pytest

# --------------------------- paths ---------------------------

REPO = Path(__file__).resolve().parents[1]
WEB = REPO / "web"
APP_CFG = WEB / "app.config.json"
LAYERS = WEB / "layers.json"  # optional legacy
APP_SCHEMA = WEB / "config" / "app.config.schema.json"  # optional
LAYERS_SCHEMA = WEB / "config" / "layers.schema.json"   # optional

# --------------------------- regex/helpers ---------------------------

HEX_COLOR = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
ID_OK = re.compile(r"^[a-z0-9][a-z0-9_-]*$")  # prefer lowercase hyphen/underscore

def load_json(p: Path) -> Dict[str, Any]:
  return json.loads(p.read_text(encoding="utf-8"))

def is_color(s: Any) -> bool:
  return isinstance(s, str) and (HEX_COLOR.match(s) or s.startswith(("rgb", "hsl")))

def is_iso_date_or_none(s: Any) -> bool:
  if s is None: return True
  return isinstance(s, str) and bool(re.match(r"^\d{4}-\d{2}-\d{2}$", s))

def layer_index(layers: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
  return {L["id"]: L for L in layers if isinstance(L.get("id"), str)}

def infer_render(l: Dict[str, Any]) -> str | None:
  if l.get("type") != "geojson": return None
  p = l.get("paint") or {}
  if "line" in p: return "line"
  if "fill" in p: return "fill"
  if "circle" in p: return "circle"
  return None

def file_like_exists(root: Path, value: str) -> bool:
  """
  For local paths like './vectors/x.geojson' ensure the file exists under WEB.
  Skip http(s) URLs and tile templates containing {z}/{x}/{y}.
  """
  if not isinstance(value, str): return False
  if value.startswith(("http://", "https://")): return True  # not tested here
  if "{z}" in value and "{x}" in value and "{y}" in value:   # tile template
    # Best-effort: ensure folder exists up to the template prefix
    base = value.split("{z}")[0].lstrip("./")
    return (root / base).exists()
  # normal local file
  return (root / value.lstrip("./")).exists()

# --------------------------- jsonschema (optional) ---------------------------

try:
  from jsonschema import Draft202012Validator
  HAVE_SCHEMA = True
except Exception:
  HAVE_SCHEMA = False

@pytest.mark.parametrize("cfg_path,schema_path", [
  (APP_CFG, APP_SCHEMA),
  (LAYERS, LAYERS_SCHEMA),
])
def test_jsonschema_if_present(cfg_path: Path, schema_path: Path):
  if not HAVE_SCHEMA:
    pytest.skip("jsonschema not installed")
  if not cfg_path.exists() or not schema_path.exists():
    pytest.skip("config or schema missing (ok during scaffold)")
  cfg = load_json(cfg_path)
  schema = load_json(schema_path)
  validator = Draft202012Validator(schema)
  errors = sorted(validator.iter_errors(cfg), key=lambda e: (list(e.path), e.message))
  if errors:
    msg = "\n".join([f"- {'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in errors])
    pytest.fail(f"Schema validation failed for {cfg_path}:\n{msg}")

# --------------------------- core presence ---------------------------

def test_app_config_exists():
  assert APP_CFG.exists(), "web/app.config.json is required"

# --------------------------- ID / groups / duplicates ---------------------------

def test_layer_ids_unique_and_format():
  data = load_json(APP_CFG)
  layers = data.get("layers", [])
  ids = [L.get("id") for L in layers if isinstance(L.get("id"), str)]
  assert len(ids) == len(set(ids)), "Duplicate layer IDs in app.config.json"
  bad = [i for i in ids if not ID_OK.match(i)]
  assert not bad, f"Layer IDs should be lowercase/hyphen/underscore: {bad}"

def test_groups_are_declared_or_ungrouped():
  data = load_json(APP_CFG)
  groups = set(data.get("groups", []))
  for L in data.get("layers", []):
    g = L.get("group")
    assert isinstance(g, str) and g, f"Layer {L.get('id')} missing group"
    assert g in groups or g == "Ungrouped", f"Layer {L.get('id')} group '{g}' not in top-level groups"

# --------------------------- defaults sanity ---------------------------

def test_defaults_bounds_shape_if_present():
  df = (load_json(APP_CFG).get("defaults")) or {}
  if "bounds" in df:
    b = df["bounds"]
    ok = isinstance(b, list) and len(b) == 4 and all(isinstance(x, (int, float)) for x in b)
    assert ok, "defaults.bounds must be [minx,miny,maxx,maxy]"

# --------------------------- per-layer sanity ---------------------------

def test_per_layer_fields_and_paths():
  cfg = load_json(APP_CFG)
  root_time = cfg.get("time") or {}
  root_min = root_time.get("min")
  root_max = root_time.get("max")
  layers: List[Dict[str, Any]] = cfg.get("layers", [])

  errs: List[str] = []

  for L in layers:
    lid = L.get("id", "<missing>")
    typ = L.get("type")
    # type
    if typ not in ("raster", "geojson", "image"):
      errs.append(f"{lid}: type must be 'raster'|'geojson'|'image'")
    # visibility/opacity
    if "opacity" in L and not (isinstance(L["opacity"], (int, float)) and 0 <= L["opacity"] <= 1):
      errs.append(f"{lid}: opacity must be 0..1")
    # minzoom/maxzoom
    mn, mx = L.get("minzoom"), L.get("maxzoom")
    if mn is not None and not (isinstance(mn, int) and 0 <= mn <= 24):
      errs.append(f"{lid}: minzoom must be int 0..24")
    if mx is not None and not (isinstance(mx, int) and 0 <= mx <= 24):
      errs.append(f"{lid}: maxzoom must be int 0..24")
    if mn is not None and mx is not None and mn > mx:
      errs.append(f"{lid}: minzoom ({mn}) must be <= maxzoom ({mx})")
    # time window
    t = L.get("time") or {"start": L.get("start"), "end": L.get("end")}
    if t:
      s, e = t.get("start"), t.get("end")
      if not is_iso_date_or_none(s):
        errs.append(f"{lid}: time.start must be YYYY-MM-DD or null")
      if not is_iso_date_or_none(e):
        errs.append(f"{lid}: time.end must be YYYY-MM-DD or null")
      # Soft: layer time within global time if both given
      if is_iso_date_or_none(s) and is_iso_date_or_none(e) and is_iso_date_or_none(root_min) and is_iso_date_or_none(root_max):
        if s and root_min and s < root_min: errs.append(f"{lid}: time.start ({s}) < global time.min ({root_min})")
        if e and root_max and e > root_max: errs.append(f"{lid}: time.end ({e}) > global time.max ({root_max})")
    # urls/paths + existence (local)
    if typ in ("raster", "image"):
      url = L.get("url")
      if not (isinstance(url, str) and url):
        errs.append(f"{lid}: raster/image requires 'url'")
      elif "../" in url:
        errs.append(f"{lid}: url must be web-relative (no '../')")
      elif not file_like_exists(WEB, url):
        errs.append(f"{lid}: url/path not found (local check): {url}")
    elif typ == "geojson":
      path = L.get("path")
      if not (isinstance(path, str) and path):
        errs.append(f"{lid}: geojson requires 'path'")
      elif "../" in path:
        errs.append(f"{lid}: path must be web-relative (no '../')")
      elif not file_like_exists(WEB, path):
        errs.append(f"{lid}: path not found: {path}")
    # paint sanity (geojson)
    if typ == "geojson":
      paint = L.get("paint") or {}
      r = infer_render(L)
      if r == "line":
        ln = paint.get("line", {})
        if "line-color" in ln and not is_color(ln["line-color"]):
          errs.append(f"{lid}: line.line-color must be CSS color")
        if "stroke-color" in ln:
          errs.append(f"{lid}: use line-color (not stroke-color)")
      if r == "fill":
        fl = paint.get("fill", {})
        if "fill-color" in fl and not is_color(fl["fill-color"]):
          errs.append(f"{lid}: fill.fill-color must be CSS color")
        if "stroke-color" in fl:
          errs.append(f"{lid}: use fill-outline-color (not stroke-color)")
      if r == "circle":
        ci = paint.get("circle", {})
        if "circle-color" in ci and not is_color(ci["circle-color"]):
          errs.append(f"{lid}: circle.circle-color must be CSS color")
    # legend sanity (optional)
    legend = L.get("legend") or []
    for item in legend:
      t = item.get("type")
      if t not in ("line", "fill", "circle"):
        errs.append(f"{lid}: legend.type must be line|fill|circle")
      if "color" in item and not is_color(item["color"]):
        errs.append(f"{lid}: legend.color must be CSS color")

  if errs:
    pytest.fail("Config issues:\n" + "\n".join(f"- {e}" for e in errs))

# --------------------------- cross-file consistency (optional legacy) ---------------------------

def test_cross_file_consistency_if_layers_present():
  if not LAYERS.exists():
    pytest.skip("layers.json missing (ok)")
  app = load_json(APP_CFG)
  lay = load_json(LAYERS)
  ai, li = layer_index(app.get("layers", [])), layer_index(lay.get("layers", []))

  # Type conflicts
  conflicts = []
  for lid in (set(ai) & set(li)):
    if ai[lid].get("type") != li[lid].get("type"):
      conflicts.append(f"{lid}: type mismatch app={ai[lid].get('type')} vs layers={li[lid].get('type')}")
  assert not conflicts, "Layer ID/type conflicts:\n- " + "\n-
