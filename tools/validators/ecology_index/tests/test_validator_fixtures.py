from __future__ import annotations

from pathlib import Path

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"
FIXTURE_ROOT = Path("tools/validators/ecology_index/fixtures")


def test_valid_huc12_vegetation_soil_hydrology_passes() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "valid" / "huc12_vegetation_soil_hydrology.json",
        schema_ref=SCHEMA_REF,
    )

    assert result.ok
    assert result.errors == []


def test_valid_fauna_habitat_grid_passes() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "valid" / "fauna_habitat_grid.json",
        schema_ref=SCHEMA_REF,
    )

    assert result.ok
    assert result.errors == []


def test_valid_air_station_vegetation_passes() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "valid" / "air_station_vegetation.json",
        schema_ref=SCHEMA_REF,
    )

    assert result.ok
    assert result.errors == []


def test_missing_spec_hash_fails() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "missing_spec_hash.json",
        schema_ref=SCHEMA_REF,
    )

    assert not result.ok
    assert any(error.code == "ECO_INDEX_SPEC_HASH_REQUIRED" for error in result.errors)


def test_huc12_missing_watershed_id_fails() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "huc12_missing_watershed_id.json",
        schema_ref=SCHEMA_REF,
    )

    assert not result.ok
    assert any(error.code == "ECO_INDEX_HUC12_WATERSHED_REQUIRED" for error in result.errors)


def test_fauna_without_taxon_or_obs_fails() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "fauna_without_taxon_or_obs.json",
        schema_ref=SCHEMA_REF,
    )

    assert not result.ok
    assert any(error.code == "ECO_INDEX_TAXON_OR_OBS_REQUIRED" for error in result.errors)


def test_empty_evidence_refs_fails() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "evidence_refs_empty.json",
        schema_ref=SCHEMA_REF,
    )

    assert not result.ok
    assert any(error.code == "ECO_INDEX_EVIDENCE_REQUIRED" for error in result.errors)


def test_unknown_domain_fails() -> None:
    result = validate_file(
        input_path=FIXTURE_ROOT / "invalid" / "unknown_domain.json",
        schema_ref=SCHEMA_REF,
    )

    assert not result.ok
    assert any(error.code == "ECO_INDEX_UNKNOWN_DOMAIN" for error in result.errors)
