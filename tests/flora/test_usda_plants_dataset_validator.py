import json
from pathlib import Path

from tools.validators.flora.usda_plants_dataset_validator import validate_dataset

FIXTURE_DIR = Path("tests/fixtures/flora/usda_plants")


def _load(name: str) -> dict:
    return json.loads((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def test_valid_fixture_passes() -> None:
    result = validate_dataset(_load("valid_minimal.json"))
    assert result["result"] == "pass"
    assert result["reason_codes"] == []


def test_missing_author_fails() -> None:
    result = validate_dataset(_load("invalid_missing_author.json"))
    assert result["result"] == "fail"
    assert "field.scientific_name.missing_author" in result["reason_codes"]


def test_bad_fips_fails() -> None:
    result = validate_dataset(_load("invalid_bad_fips.json"))
    assert result["result"] == "fail"
    assert any(code.startswith("field.county_fips.invalid") for code in result["reason_codes"])


def test_spec_hash_mismatch_fails() -> None:
    payload = _load("valid_minimal.json")
    payload["properties"]["kfm:spec_hash"] = "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    result = validate_dataset(payload)
    assert result["result"] == "fail"
    assert "field.spec_hash.mismatch" in result["reason_codes"]
