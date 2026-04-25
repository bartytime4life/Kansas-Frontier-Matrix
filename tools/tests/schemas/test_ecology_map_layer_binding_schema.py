```python
from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


SCHEMA_REF = Path("schemas/ecology/ecology_map_layer_binding.schema.json")


def load_schema(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(instance: dict) -> list[str]:
    schema = load_schema(SCHEMA_REF)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(p) for p in e.path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(instance), key=lambda i: list(i.path))
    ]


def valid_layer() -> dict:
    return {
        "layer_id": "kfm.ecology.vegetation.ndvi_change.v1",
        "candidate_id": "eco_index.example",
        "evidence_bundle_id": "kfm.evidence.ecology.eco_index.example",
        "drawer_id": "kfm.drawer.ecology.eco_index.example",
        "render_type": "raster",
        "time_enabled": True,
        "default_visibility": True,
        "source_ref": "maplibre://sources/ecology/ndvi_change",
        "style_layer_ref": "maplibre://layers/ecology/ndvi_change",
        "spec_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "status": "active"
    }


def test_valid_layer_passes() -> None:
    errors = validate(valid_layer())
    assert errors == []


def test_missing_required_field_fails() -> None:
    value = valid_layer()
    value.pop("evidence_bundle_id")

    errors = validate(value)

    assert errors
    assert any("evidence_bundle_id" in e for e in errors)


def test_invalid_spec_hash_fails() -> None:
    value = valid_layer()
    value["spec_hash"] = "not-a-sha256"

    errors = validate(value)

    assert errors
    assert any("does not match" in e for e in errors)


def test_invalid_render_type_fails() -> None:
    value = valid_layer()
    value["render_type"] = "magic"

    errors = validate(value)

    assert errors
    assert any("is not one of" in e for e in errors)


def test_3d_tiles_requires_cesium_block() -> None:
    value = valid_layer()
    value["render_type"] = "3d_tiles"

    errors = validate(value)

    assert errors
    assert any("cesium" in e for e in errors)


def test_3d_tiles_requires_justification() -> None:
    value = valid_layer()
    value["render_type"] = "3d_tiles"
    value["cesium"] = {"enabled": True}

    errors = validate(value)

    assert errors
    assert any("justification" in e for e in errors)


def test_3d_tiles_requires_enabled_true() -> None:
    value = valid_layer()
    value["render_type"] = "3d_tiles"
    value["cesium"] = {
        "enabled": False,
        "justification": "3D needed"
    }

    errors = validate(value)

    assert errors
    assert any("const" in e or "True" in e for e in errors)


def test_valid_3d_tiles_passes() -> None:
    value = valid_layer()
    value["render_type"] = "3d_tiles"
    value["cesium"] = {
        "enabled": True,
        "justification": "Terrain context required"
    }

    errors = validate(value)

    assert errors == []


def test_invalid_schema_raises(tmp_path: Path) -> None:
    bad_schema = tmp_path / "bad.schema.json"
    bad_schema.write_text(json.dumps({"type": 123}), encoding="utf-8")

    with pytest.raises(SchemaError):
        Draft202012Validator.check_schema(load_schema(bad_schema))
```
