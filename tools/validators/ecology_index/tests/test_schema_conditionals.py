```python
from __future__ import annotations

import json
from pathlib import Path

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def base_candidate() -> dict:
    return {
        "index_id": "kfm.eco_index.test.conditional",
        "geom_id": "HUC12:102600080305",
        "time_bucket": "2024_growing_season",
        "spec_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "domains": ["hydrology"],
        "evidence_refs": [
            {
                "domain": "hydrology",
                "evidence_ref": "kfm:evidence:hydrology:huc12:102600080305"
            }
        ],
        "status": "valid"
    }


def test_huc12_requires_join_keys_object(tmp_path: Path) -> None:
    candidate = base_candidate()
    candidate["geometry_type"] = "huc12"

    input_path = tmp_path / "huc12_missing_join_keys.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("'join_keys' is a required property" in error.message for error in result.errors)


def test_huc12_requires_watershed_id(tmp_path: Path) -> None:
    candidate = base_candidate()
    candidate["geometry_type"] = "huc12"
    candidate["join_keys"] = {
        "station_id": "MESONET:ELL"
    }

    input_path = tmp_path / "huc12_missing_watershed_id.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("'watershed_id' is a required property" in error.message for error in result.errors)


def test_fauna_requires_taxon_or_obs(tmp_path: Path) -> None:
    candidate = base_candidate()
    candidate["geometry_type"] = "grid"
    candidate["geom_id"] = "GRID:KS_10KM_204"
    candidate["domains"] = ["fauna"]
    candidate["evidence_refs"] = [
        {
            "domain": "fauna",
            "evidence_ref": "kfm:evidence:fauna:example"
        }
    ]
    candidate["join_keys"] = {
        "landcover_class": "grassland"
    }

    input_path = tmp_path / "fauna_missing_taxon_or_obs.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("is not valid under any of the given schemas" in error.message for error in result.errors)


def test_soil_requires_soil_or_station_id(tmp_path: Path) -> None:
    candidate = base_candidate()
    candidate["geometry_type"] = "grid"
    candidate["geom_id"] = "GRID:KS_10KM_205"
    candidate["domains"] = ["soil"]
    candidate["evidence_refs"] = [
        {
            "domain": "soil",
            "evidence_ref": "kfm:evidence:soil:example"
        }
    ]
    candidate["join_keys"] = {
        "landcover_class": "grassland"
    }

    input_path = tmp_path / "soil_missing_soil_or_station.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("is not valid under any of the given schemas" in error.message for error in result.errors)


def test_vegetation_requires_layer_or_landcover(tmp_path: Path) -> None:
    candidate = base_candidate()
    candidate["geometry_type"] = "grid"
    candidate["geom_id"] = "GRID:KS_10KM_206"
    candidate["domains"] = ["vegetation"]
    candidate["evidence_refs"] = [
        {
            "domain": "vegetation",
            "evidence_ref": "kfm:evidence:vegetation:example"
        }
    ]
    candidate["join_keys"] = {
        "station_id": "MESONET:ELL"
    }

    input_path = tmp_path / "vegetation_missing_layer_or_landcover.json"
    write_json(input_path, candidate)

    result = validate_file(input_path=input_path, schema_ref=SCHEMA_REF)

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SCHEMA_INVALID" for error in result.errors)
    assert any("is not valid under any of the given schemas" in error.message for error in result.errors)
```
