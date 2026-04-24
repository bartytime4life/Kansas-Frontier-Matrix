```python
from __future__ import annotations

import json
from pathlib import Path

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def test_schema_rejects_additional_properties(tmp_path: Path) -> None:
    candidate = {
        "index_id": "kfm.eco_index.invalid.extra_property",
        "geom_id": "HUC12:102600080305",
        "geometry_type": "huc12",
        "time_bucket": "2024_growing_season",
        "spec_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "domains": ["hydrology"],
        "join_keys": {
            "watershed_id": "102600080305"
        },
        "evidence_refs": [
            {
                "domain": "hydrology",
                "evidence_ref": "kfm:evidence:hydrology:huc12:102600080305"
            }
        ],
        "status": "valid",
        "unexpected_field": "must fail"
    }

    input_path = tmp_path / "extra_property.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("Additional properties are not allowed" in error.message for error in result.errors)


def test_schema_rejects_bad_spec_hash_pattern(tmp_path: Path) -> None:
    candidate = {
        "index_id": "kfm.eco_index.invalid.bad_spec_hash",
        "geom_id": "HUC12:102600080305",
        "geometry_type": "huc12",
        "time_bucket": "2024_growing_season",
        "spec_hash": "not-a-sha256",
        "domains": ["hydrology"],
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
    }

    input_path = tmp_path / "bad_spec_hash.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("does not match" in error.message for error in result.errors)


def test_schema_rejects_invalid_status_enum(tmp_path: Path) -> None:
    candidate = {
        "index_id": "kfm.eco_index.invalid.status",
        "geom_id": "HUC12:102600080305",
        "geometry_type": "huc12",
        "time_bucket": "2024_growing_season",
        "spec_hash": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "domains": ["hydrology"],
        "join_keys": {
            "watershed_id": "102600080305"
        },
        "evidence_refs": [
            {
                "domain": "hydrology",
                "evidence_ref": "kfm:evidence:hydrology:huc12:102600080305"
            }
        ],
        "status": "approved_by_vibes"
    }

    input_path = tmp_path / "bad_status.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("is not one of" in error.message for error in result.errors)
```
