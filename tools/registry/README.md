# tools/registry

Utilities in this directory validate and resolve ecology map-layer registry entries before they are consumed by downstream runtime surfaces.

## Files

- `ecology_map_layer_registry.py`: library helpers to load a registry, resolve layer bindings, and validate bindings against a JSON schema.
- `ecology_map_layer_registry_cli.py`: CLI wrapper for running the same checks in local workflows and CI.
- `README.ecology_map_layers.md`: domain-focused notes for ecology map-layer bindings.
- `tests/`: unit and CLI tests for fail-closed behavior.

## Behavior guarantees

- Registry files must be JSON objects with a `layers` array.
- Every `layers[]` entry must include non-empty `layer_id`, `status`, and `binding_ref` strings.
- Active layers are resolved by `binding_ref`, then validated against the supplied schema.
- Binding `layer_id` must match the registry entry.
- If the registry entry includes `spec_hash`, the binding `spec_hash` must match.
- Any schema or consistency failure raises `LayerRegistryError` and returns a non-zero CLI exit code.

## CLI

```bash
python -m tools.registry.ecology_map_layer_registry_cli \
  --registry data/registry/ecology/map_layers/registry.json \
  --schema schemas/ecology/ecology_map_layer_binding.schema.json
```

Resolve one layer and write the validated binding:

```bash
python -m tools.registry.ecology_map_layer_registry_cli \
  --registry data/registry/ecology/map_layers/registry.json \
  --schema schemas/ecology/ecology_map_layer_binding.schema.json \
  --layer-id kfm.ecology.vegetation.ndvi_change.v1 \
  --out /tmp/ndvi.binding.json
```

## Exit codes

- `0`: success
- `1`: invalid registry/binding input
- `2`: missing registry path
- `3`: missing/invalid schema path
- `5`: unexpected internal error
