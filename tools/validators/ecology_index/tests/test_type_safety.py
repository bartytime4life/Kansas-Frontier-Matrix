from __future__ import annotations

import json
from pathlib import Path

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def test_domains_string_does_not_raise_internal_error(tmp_path: Path) -> None:
    candidate = {
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
    }

    input_path = tmp_path / "domains_string.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)


def test_join_keys_string_does_not_raise_internal_error(tmp_path: Path) -> None:
    candidate = {
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
    }

    input_path = tmp_path / "join_keys_string.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any(
        error.code == "ECO_INDEX_HUC12_WATERSHED_REQUIRED"
        for error in result.errors
    )


def test_evidence_refs_string_does_not_raise_internal_error(tmp_path: Path) -> None:
    candidate = {
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
    }

    input_path = tmp_path / "evidence_refs_string.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any(error.code == "ECO_INDEX_EVIDENCE_REQUIRED" for error in result.errors)


def test_invalid_schema_fails_before_validation(tmp_path: Path) -> None:
    schema_path = tmp_path / "bad_schema.json"
    input_path = tmp_path / "candidate.json"

    write_json(
        schema_path,
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": 123
        },
    )

    write_json(
        input_path,
        {
            "index_id": "kfm.eco_index.valid.example",
            "geom_id": "GRID:KS_10KM_204",
            "time_bucket": "2024_annual",
            "spec_hash": "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
            "domains": ["vegetation"],
            "join_keys": {
                "layer_id": "kfm.ecology.vegetation.ndvi_change.v1"
            },
            "evidence_refs": [
                {
                    "domain": "vegetation",
                    "evidence_ref": "kfm:evidence:vegetation:example"
                }
            ],
            "status": "valid"
        },
    )

    try:
        validate_file(input_path=input_path, schema_ref=str(schema_path))
    except Exception as exc:
        assert exc.__class__.__name__ == "SchemaError"
    else:
        raise AssertionError("Expected invalid schema to raise SchemaError")
