```python
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.validators.ecology_index", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_cli_domains_string_returns_validation_failure(tmp_path: Path) -> None:
    input_path = tmp_path / "domains_string.json"

    write_json(
        input_path,
        {
            "index_id": "kfm.eco_index.invalid.domains_string",
            "geom_id": "HUC12:102600080305",
            "geometry_type": "huc12",
            "time_bucket": "2024_growing_season",
            "spec_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "domains": "hydrology",
            "join_keys": {
                "watershed_id": "102600080305"
            },
            "evidence_refs": [
                {
                    "domain": "hydrology",
                    "evidence_ref": "kfm:evidence:hydrology:huc12:102600080305"
                }
            ],
            "status": "valid"
        },
    )

    result = run_cli("--input", str(input_path), "--schema", SCHEMA_REF)

    assert result.returncode == 1
    assert "ECO_INDEX_SCHEMA_INVALID" in result.stderr
    assert "internal validator error:" not in result.stderr


def test_cli_join_keys_string_returns_validation_failure(tmp_path: Path) -> None:
    input_path = tmp_path / "join_keys_string.json"

    write_json(
        input_path,
        {
            "index_id": "kfm.eco_index.invalid.join_keys_string",
            "geom_id": "HUC12:102600080305",
            "geometry_type": "huc12",
            "time_bucket": "2024_growing_season",
            "spec_hash": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            "domains": ["hydrology"],
            "join_keys": "watershed_id=102600080305",
            "evidence_refs": [
                {
                    "domain": "hydrology",
                    "evidence_ref": "kfm:evidence:hydrology:huc12:102600080305"
                }
            ],
            "status": "valid"
        },
    )

    result = run_cli("--input", str(input_path), "--schema", SCHEMA_REF)

    assert result.returncode == 1
    assert "ECO_INDEX_SCHEMA_INVALID" in result.stderr
    assert "internal validator error:" not in result.stderr


def test_cli_evidence_refs_string_returns_validation_failure(tmp_path: Path) -> None:
    input_path = tmp_path / "evidence_refs_string.json"

    write_json(
        input_path,
        {
            "index_id": "kfm.eco_index.invalid.evidence_refs_string",
            "geom_id": "GRID:KS_10KM_204",
            "geometry_type": "grid",
            "time_bucket": "2024_annual",
            "spec_hash": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
            "domains": ["vegetation"],
            "join_keys": {
                "layer_id": "kfm.ecology.vegetation.ndvi_change.v1"
            },
            "evidence_refs": "kfm:evidence:vegetation:example",
            "status": "valid"
        },
    )

    result = run_cli("--input", str(input_path), "--schema", SCHEMA_REF)

    assert result.returncode == 1
    assert "ECO_INDEX_SCHEMA_INVALID" in result.stderr
    assert "internal validator error:" not in result.stderr
```
