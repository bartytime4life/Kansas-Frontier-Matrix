from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.registry.ecology_map_layer_registry import (
    LayerRegistryError,
    active_layer_bindings,
    get_layer_entry,
    load_layer_binding,
    load_registry,
    resolve_binding_path,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "layer_id",
            "candidate_id",
            "evidence_bundle_id",
            "drawer_id",
            "render_type",
            "time_enabled",
            "default_visibility",
            "source_ref",
            "style_layer_ref",
            "spec_hash",
            "status",
        ],
        "properties": {
            "layer_id": {"type": "string"},
            "candidate_id": {"type": "string"},
            "evidence_bundle_id": {"type": "string"},
            "drawer_id": {"type": "string"},
            "render_type": {
                "type": "string",
                "enum": ["raster", "vector", "timeseries", "3d_tiles"],
            },
            "time_enabled": {"type": "boolean"},
            "default_visibility": {"type": "boolean"},
            "source_ref": {"type": "string"},
            "style_layer_ref": {"type": "string"},
            "spec_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
            "status": {
                "type": "string",
                "enum": ["active", "inactive", "deprecated", "review_required"],
            },
        },
    }


def binding(
    *,
    layer_id: str = "kfm.ecology.vegetation.ndvi_change.v1",
    spec_hash: str = SPEC_HASH,
    status: str = "active",
) -> dict:
    return {
        "layer_id": layer_id,
        "candidate_id": "eco_index.example",
        "evidence_bundle_id": "kfm.evidence.ecology.eco_index.example",
        "drawer_id": "kfm.drawer.ecology.eco_index.example",
        "render_type": "raster",
        "time_enabled": True,
        "default_visibility": True,
        "source_ref": "maplibre://sources/ecology/ndvi_change",
        "style_layer_ref": "maplibre://layers/ecology/ndvi_change",
        "spec_hash": spec_hash,
        "status": status,
    }


def registry(*, binding_ref: str = "bindings/ndvi.binding.json") -> dict:
    return {
        "registry_id": "kfm.registry.ecology.map_layers",
        "layers": [
            {
                "layer_id": "kfm.ecology.vegetation.ndvi_change.v1",
                "binding_ref": binding_ref,
                "status": "active",
                "spec_hash": SPEC_HASH,
            }
        ],
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_load_registry_accepts_valid_registry(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    write_json(registry_path, registry())

    loaded = load_registry(registry_path)

    assert loaded["registry_id"] == "kfm.registry.ecology.map_layers"
    assert len(loaded["layers"]) == 1


def test_load_registry_rejects_non_object(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    write_json(registry_path, [])

    with pytest.raises(LayerRegistryError, match="JSON document must be an object"):
        load_registry(registry_path)


def test_load_registry_rejects_missing_layers_array(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    write_json(registry_path, {"registry_id": "kfm.registry.ecology.map_layers"})

    with pytest.raises(LayerRegistryError, match="registry.layers must be an array"):
        load_registry(registry_path)


def test_resolve_binding_path_relative_to_registry() -> None:
    registry_path = Path("data/registry/ecology/map_layers/registry.json")

    resolved = resolve_binding_path(
        registry_path=registry_path,
        binding_ref="bindings/ndvi.binding.json",
    )

    assert resolved == Path("data/registry/ecology/map_layers/bindings/ndvi.binding.json")


def test_get_layer_entry_finds_layer() -> None:
    value = registry()

    entry = get_layer_entry(
        registry=value,
        layer_id="kfm.ecology.vegetation.ndvi_change.v1",
    )

    assert entry["spec_hash"] == SPEC_HASH


def test_get_layer_entry_missing_layer_fails() -> None:
    with pytest.raises(LayerRegistryError, match="layer not found"):
        get_layer_entry(
            registry=registry(),
            layer_id="kfm.ecology.missing",
        )


def test_load_layer_binding_success(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"
    binding_path = tmp_path / "bindings" / "ndvi.binding.json"

    write_json(registry_path, registry())
    write_json(schema_path, schema())
    write_json(binding_path, binding())

    loaded = load_layer_binding(
        registry_path=registry_path,
        layer_id="kfm.ecology.vegetation.ndvi_change.v1",
        schema_path=schema_path,
    )

    assert loaded["candidate_id"] == "eco_index.example"
    assert loaded["evidence_bundle_id"] == "kfm.evidence.ecology.eco_index.example"


def test_load_layer_binding_missing_binding_file_fails(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"

    write_json(registry_path, registry())
    write_json(schema_path, schema())

    with pytest.raises(LayerRegistryError, match="binding file missing"):
        load_layer_binding(
            registry_path=registry_path,
            layer_id="kfm.ecology.vegetation.ndvi_change.v1",
            schema_path=schema_path,
        )


def test_load_layer_binding_schema_invalid_fails(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"
    binding_path = tmp_path / "bindings" / "ndvi.binding.json"

    bad_binding = binding()
    bad_binding.pop("evidence_bundle_id")

    write_json(registry_path, registry())
    write_json(schema_path, schema())
    write_json(binding_path, bad_binding)

    with pytest.raises(LayerRegistryError, match="binding schema invalid"):
        load_layer_binding(
            registry_path=registry_path,
            layer_id="kfm.ecology.vegetation.ndvi_change.v1",
            schema_path=schema_path,
        )


def test_load_layer_binding_layer_id_mismatch_fails(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"
    binding_path = tmp_path / "bindings" / "ndvi.binding.json"

    write_json(registry_path, registry())
    write_json(schema_path, schema())
    write_json(binding_path, binding(layer_id="kfm.ecology.other"))

    with pytest.raises(LayerRegistryError, match="binding layer_id does not match"):
        load_layer_binding(
            registry_path=registry_path,
            layer_id="kfm.ecology.vegetation.ndvi_change.v1",
            schema_path=schema_path,
        )


def test_load_layer_binding_spec_hash_mismatch_fails(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"
    binding_path = tmp_path / "bindings" / "ndvi.binding.json"

    write_json(registry_path, registry())
    write_json(schema_path, schema())
    write_json(
        binding_path,
        binding(
            spec_hash="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        ),
    )

    with pytest.raises(LayerRegistryError, match="binding spec_hash does not match"):
        load_layer_binding(
            registry_path=registry_path,
            layer_id="kfm.ecology.vegetation.ndvi_change.v1",
            schema_path=schema_path,
        )


def test_active_layer_bindings_returns_only_active(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"

    write_json(schema_path, schema())

    write_json(
        tmp_path / "bindings" / "active.binding.json",
        binding(layer_id="kfm.ecology.vegetation.ndvi_change.v1"),
    )
    write_json(
        tmp_path / "bindings" / "inactive.binding.json",
        binding(layer_id="kfm.ecology.vegetation.inactive.v1", status="inactive"),
    )

    write_json(
        registry_path,
        {
            "registry_id": "kfm.registry.ecology.map_layers",
            "layers": [
                {
                    "layer_id": "kfm.ecology.vegetation.ndvi_change.v1",
                    "binding_ref": "bindings/active.binding.json",
                    "status": "active",
                    "spec_hash": SPEC_HASH,
                },
                {
                    "layer_id": "kfm.ecology.vegetation.inactive.v1",
                    "binding_ref": "bindings/inactive.binding.json",
                    "status": "inactive",
                    "spec_hash": SPEC_HASH,
                },
            ],
            "generated_at": "2026-04-24T00:00:00Z",
        },
    )

    bindings = active_layer_bindings(
        registry_path=registry_path,
        schema_path=schema_path,
    )

    assert len(bindings) == 1
    assert bindings[0]["layer_id"] == "kfm.ecology.vegetation.ndvi_change.v1"
