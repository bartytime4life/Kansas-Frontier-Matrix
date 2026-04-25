```python
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "tools.registry.ecology_map_layer_registry_cli",
            *args,
        ],
        check=False,
        text=True,
        capture_output=True,
    )


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
        "spec_hash": SPEC_HASH,
        "status": status,
    }


def registry() -> dict:
    return {
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
    }


def setup_registry(tmp_path: Path) -> tuple[Path, Path]:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"

    write_json(schema_path, schema())
    write_json(registry_path, registry())
    write_json(
        tmp_path / "bindings" / "active.binding.json",
        binding(layer_id="kfm.ecology.vegetation.ndvi_change.v1"),
    )
    write_json(
        tmp_path / "bindings" / "inactive.binding.json",
        binding(
            layer_id="kfm.ecology.vegetation.inactive.v1",
            status="inactive",
        ),
    )

    return registry_path, schema_path


def test_cli_lists_active_bindings(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
    )

    assert result.returncode == 0
    assert "active bindings: 1" in result.stdout
    assert result.stderr == ""


def test_cli_resolves_layer_binding(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
        "--layer-id",
        "kfm.ecology.vegetation.ndvi_change.v1",
    )

    assert result.returncode == 0
    assert "binding: kfm.ecology.vegetation.ndvi_change.v1" in result.stdout
    assert result.stderr == ""


def test_cli_writes_resolved_binding(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)
    out_path = tmp_path / "out" / "binding.json"

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
        "--layer-id",
        "kfm.ecology.vegetation.ndvi_change.v1",
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert out_path.exists()

    written = json.loads(out_path.read_text(encoding="utf-8"))
    assert written["layer_id"] == "kfm.ecology.vegetation.ndvi_change.v1"


def test_cli_writes_active_bindings_list(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)
    out_path = tmp_path / "out" / "active_bindings.json"

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert out_path.exists()

    written = json.loads(out_path.read_text(encoding="utf-8"))
    assert isinstance(written, list)
    assert len(written) == 1
    assert written[0]["layer_id"] == "kfm.ecology.vegetation.ndvi_change.v1"


def test_cli_missing_registry_exits_two(tmp_path: Path) -> None:
    schema_path = tmp_path / "schema.json"
    write_json(schema_path, schema())

    result = run_cli(
        "--registry",
        str(tmp_path / "missing_registry.json"),
        "--schema",
        str(schema_path),
    )

    assert result.returncode == 2
    assert "missing registry:" in result.stderr


def test_cli_missing_schema_exits_three(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    write_json(registry_path, registry())

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(tmp_path / "missing_schema.json"),
    )

    assert result.returncode == 3
    assert "missing schema:" in result.stderr


def test_cli_invalid_registry_exits_one(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"
    schema_path = tmp_path / "schema.json"

    write_json(registry_path, {"registry_id": "kfm.registry.ecology.map_layers"})
    write_json(schema_path, schema())

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
    )

    assert result.returncode == 1
    assert "invalid registry:" in result.stderr
    assert "registry.layers must be an array" in result.stderr


def test_cli_missing_layer_exits_one(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
        "--layer-id",
        "kfm.ecology.missing",
    )

    assert result.returncode == 1
    assert "invalid registry:" in result.stderr
    assert "layer not found" in result.stderr


def test_cli_invalid_binding_schema_exits_one(tmp_path: Path) -> None:
    registry_path, schema_path = setup_registry(tmp_path)

    bad_binding = binding(layer_id="kfm.ecology.vegetation.ndvi_change.v1")
    bad_binding.pop("evidence_bundle_id")
    write_json(tmp_path / "bindings" / "active.binding.json", bad_binding)

    result = run_cli(
        "--registry",
        str(registry_path),
        "--schema",
        str(schema_path),
    )

    assert result.returncode == 1
    assert "invalid registry:" in result.stderr
    assert "binding schema invalid" in result.stderr
```
