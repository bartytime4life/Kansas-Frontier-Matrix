from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


class LayerRegistryError(ValueError):
    pass


def load_json_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise LayerRegistryError(f"JSON document must be an object: {path}")

    return value


def validate_binding(
    *,
    binding: dict[str, Any],
    schema_path: Path,
) -> list[str]:
    schema = load_json_object(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(
            validator.iter_errors(binding),
            key=lambda item: list(item.path),
        )
    ]


def load_registry(path: Path) -> dict[str, Any]:
    registry = load_json_object(path)

    layers = registry.get("layers")
    if not isinstance(layers, list):
        raise LayerRegistryError("registry.layers must be an array")

    return registry


def resolve_binding_path(
    *,
    registry_path: Path,
    binding_ref: str,
) -> Path:
    binding_path = Path(binding_ref)

    if binding_path.is_absolute():
        return binding_path

    return registry_path.parent / binding_path


def get_layer_entry(
    *,
    registry: dict[str, Any],
    layer_id: str,
) -> dict[str, Any]:
    for layer in registry.get("layers", []):
        if isinstance(layer, dict) and layer.get("layer_id") == layer_id:
            return layer

    raise LayerRegistryError(f"layer not found: {layer_id}")


def load_layer_binding(
    *,
    registry_path: Path,
    layer_id: str,
    schema_path: Path,
) -> dict[str, Any]:
    registry = load_registry(registry_path)
    entry = get_layer_entry(registry=registry, layer_id=layer_id)

    binding_ref = entry.get("binding_ref")
    if not isinstance(binding_ref, str) or not binding_ref:
        raise LayerRegistryError(f"layer missing binding_ref: {layer_id}")

    binding_path = resolve_binding_path(
        registry_path=registry_path,
        binding_ref=binding_ref,
    )

    if not binding_path.exists():
        raise LayerRegistryError(f"binding file missing: {binding_path}")

    binding = load_json_object(binding_path)

    errors = validate_binding(
        binding=binding,
        schema_path=schema_path,
    )
    if errors:
        raise LayerRegistryError(
            "binding schema invalid: " + "; ".join(errors)
        )

    if binding.get("layer_id") != layer_id:
        raise LayerRegistryError("binding layer_id does not match registry entry")

    if entry.get("spec_hash") and binding.get("spec_hash") != entry.get("spec_hash"):
        raise LayerRegistryError("binding spec_hash does not match registry entry")

    return binding


def active_layer_bindings(
    *,
    registry_path: Path,
    schema_path: Path,
) -> list[dict[str, Any]]:
    registry = load_registry(registry_path)
    bindings: list[dict[str, Any]] = []

    for entry in registry["layers"]:
        if not isinstance(entry, dict):
            continue

        if entry.get("status") != "active":
            continue

        layer_id = entry.get("layer_id")
        if not isinstance(layer_id, str):
            continue

        bindings.append(
            load_layer_binding(
                registry_path=registry_path,
                layer_id=layer_id,
                schema_path=schema_path,
            )
        )

    return bindings
