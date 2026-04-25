from __future__ import annotations

import json
from pathlib import Path

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"
FIXTURE_ROOT = Path("tools/validators/ecology_index/fixtures")


def test_valid_fixture_writes_passing_receipt(tmp_path: Path) -> None:
    receipt_out = tmp_path / "valid_receipt.json"

    result = validate_file(
        input_path=FIXTURE_ROOT / "valid" / "huc12_vegetation_soil_hydrology.json",
        schema_ref=SCHEMA_REF,
        receipt_out=receipt_out,
    )

    assert result.ok
    assert receipt_out.exists()

    receipt = json.loads(receipt_out.read_text(encoding="utf-8"))

    assert receipt["receipt_type"] == "validator_result"
    assert receipt["validator"] == "tools/validators/ecology_index"
    assert receipt["schema_ref"] == SCHEMA_REF
    assert receipt["input_ref"].endswith(
        "tools/validators/ecology_index/fixtures/valid/huc12_vegetation_soil_hydrology.json"
    )
    assert receipt["decision"] == "pass"
    assert receipt["errors"] == []
    assert receipt["warnings"] == []
    assert receipt["spec_hash"] == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert "generated_at" in receipt


def test_invalid_fixture_writes_failing_receipt(tmp_path: Path) -> None:
    receipt_out = tmp_path / "invalid_receipt.json"

    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "huc12_missing_watershed_id.json",
        schema_ref=SCHEMA_REF,
        receipt_out=receipt_out,
    )

    assert not result.ok
    assert receipt_out.exists()

    receipt = json.loads(receipt_out.read_text(encoding="utf-8"))

    assert receipt["receipt_type"] == "validator_result"
    assert receipt["validator"] == "tools/validators/ecology_index"
    assert receipt["schema_ref"] == SCHEMA_REF
    assert receipt["decision"] == "fail"
    assert receipt["warnings"] == []
    assert receipt["spec_hash"] == "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"

    assert receipt["errors"] == [
        {
            "code": "ECO_INDEX_HUC12_WATERSHED_REQUIRED",
            "message": "geometry_type huc12 requires join_keys.watershed_id",
        }
    ]


def test_receipt_parent_directory_is_created(tmp_path: Path) -> None:
    receipt_out = tmp_path / "nested" / "receipts" / "receipt.json"

    result = validate_file(
        input_path=FIXTURE_ROOT / "valid" / "air_station_vegetation.json",
        schema_ref=SCHEMA_REF,
        receipt_out=receipt_out,
    )

    assert result.ok
    assert receipt_out.exists()
    assert receipt_out.parent.exists()
