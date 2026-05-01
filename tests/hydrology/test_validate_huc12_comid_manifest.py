from __future__ import annotations

from pathlib import Path

from tools.validators.hydrology import validate_huc12_comid_manifest as validator

FIXTURE_ROOT = Path("tests/fixtures/hydrology/huc12_comid_manifest")
SCHEMA = Path("schemas/hydrology/huc12_comid_manifest.schema.json")


def test_valid_manifest_passes() -> None:
    result = validator.validate(
        FIXTURE_ROOT / "valid/manifest.json",
        SCHEMA,
        FIXTURE_ROOT / "valid",
    )
    assert result["ok"] is True
    assert result["errors"] == []
    assert result["manifest_id"] == "huc12@wbd-2026-01::sha256:abcdef123456"
    assert result["timeslice_id"] == "huc12::wbd-2026-01::20260101-20261231"


def test_bad_digest_fails() -> None:
    result = validator.validate(
        FIXTURE_ROOT / "invalid/bad_digest.json",
        SCHEMA,
        FIXTURE_ROOT / "valid",
    )
    assert result["ok"] is False
    assert any(error.startswith("crosswalk_digest:mismatch") for error in result["errors"])


def test_bad_huc12_fails_schema() -> None:
    result = validator.validate(
        FIXTURE_ROOT / "invalid/bad_huc12.json",
        SCHEMA,
        FIXTURE_ROOT / "valid",
    )
    assert result["ok"] is False
    assert any(error.startswith("schema:huc12:") for error in result["errors"])
