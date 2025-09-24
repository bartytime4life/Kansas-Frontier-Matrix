# pytest -q
# Validates web/app.config.json and web/layers.json against their JSON Schemas

from __future__ import annotations
import json
from pathlib import Path
import pytest

try:
    from jsonschema import Draft202012Validator
except Exception as e:  # pragma: no cover
    pytest.skip(f"jsonschema not installed: {e}", allow_module_level=True)

REPO = Path(__file__).resolve().parents[1]
APP_CFG = REPO / "web" / "app.config.json"
LAYERS = REPO / "web" / "layers.json"
APP_SCHEMA = REPO / "web" / "config" / "app.config.schema.json"
LAYERS_SCHEMA = REPO / "web" / "config" / "layers.schema.json"

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

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

def test_app_layers_ids_are_unique():
    if not APP_CFG.exists():
        pytest.skip("app.config.json missing")
    data = load_json(APP_CFG)
    ids = [ly["id"] for ly in data.get("layers", [])]
    assert len(ids) == len(set(ids)), "Duplicate layer IDs in app.config.json"
