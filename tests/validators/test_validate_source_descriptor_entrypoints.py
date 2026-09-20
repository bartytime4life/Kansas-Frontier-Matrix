"""Direct tests for SourceDescriptor schema and validator-path convergence."""

from __future__ import annotations

import json
from copy import deepcopy
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator


ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION_SCHEMA = (
    ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
)
DECLARED_SCHEMA = (
    ROOT / "schemas/contracts/v1/sources/source_descriptor.schema.json"
)
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/source/source_descriptor"
ENTRYPOINTS = (
    ROOT / "tools/validators/validate_source_descriptor.py",
    ROOT / "tools/validators/sources/validate_source_descriptor.py",
)

DASC_PROFILES = json.loads(
    (FIXTURE_ROOT / "dasc_item_profiles.json").read_text(encoding="utf-8")
)["profiles"]


@pytest.mark.parametrize("profile", DASC_PROFILES, ids=lambda p: p["source_id"])
def test_dasc_item_schema_and_denial_boundary(profile: dict) -> None:
    """Metadata fixture consistency only; no network or production ingestion proof."""
    slug = profile["source_id"].removeprefix("src:dasc-").replace("-", "_")
    descriptor = json.loads((FIXTURE_ROOT / "valid" / f"valid_dasc_{slug}.json").read_text())
    validator = load_validator(IMPLEMENTATION_SCHEMA)
    assert not list(validator.iter_errors(descriptor))
    assert descriptor["source_head"]["content_identity"]["content_sha256"] == profile["raw_metadata_sha256"]
    assert descriptor["connectors"]["activation_state"] == "disabled"
    assert descriptor["public_release"]["allowed"] is False
    assert descriptor["release_state"] == "not_released"
    assert profile["public_fields"] == []
    assert profile["pagination"]["full_capture_tested"] is False
    metadata = profile["metadata"]
    fields = {field["name"]: field["type"] for field in metadata["fields"]}
    assert fields[metadata["objectIdField"]] == "esriFieldTypeOID"
    assert metadata["extent"]["spatialReference"]["latestWkid"] == 3857
    assert metadata["advancedQueryCapabilities"]["supportsPagination"] is True
    assert metadata["advancedQueryCapabilities"]["supportsOrderBy"] is True
    assert profile["pagination"]["page_size"] <= metadata["maxRecordCount"]
    assert set(profile["acquisition_fields"]) <= set(fields)
    west, south, east, north = profile["item_extent_wgs84"]
    overlaps_kansas = west < -94.5 and east > -102.1 and south < 40.1 and north > 36.9
    if slug == "parcels_rejected":
        assert not overlaps_kansas
        assert profile["scope"] == "REJECTED_SCOPE"
        assert profile["acquisition_fields"] == []
        assert profile["probe"]["performed"] is False
        assert descriptor["review_state"] == "rejected"
    else:
        assert overlaps_kansas
        assert descriptor["review_state"] == "needs_review"
        probe = profile["probe"]
        ids = [oid for page in probe["observed_ids"] for oid in page]
        assert len(ids) == 4 and len(set(ids)) == 4
        assert ids == sorted(ids)
        assert probe["exceeded_transfer_limit"] == [True, True]
        assert probe["geometry"] is False
        assert probe["fields"] == [metadata["objectIdField"]]
    # Expected-negative mutations must fail the existing schema, not a new policy.
    for mutation in ("release", "activate", "missing_identity"):
        bad = deepcopy(descriptor)
        if mutation == "release":
            bad["public_release"]["allowed"] = True
        elif mutation == "activate":
            bad["connectors"]["activation_state"] = "live_active"
        else:
            del bad["source_id"]
        assert list(validator.iter_errors(bad)), mutation


def test_dasc_field_meanings_do_not_collapse() -> None:
    profiles = {p["source_id"]: p for p in DASC_PROFILES}
    huc = profiles["src:dasc-huc12"]
    huc_fields = {f["name"]: f for f in huc["metadata"]["fields"]}
    assert huc_fields["huc12"]["type"] == "esriFieldTypeString"
    assert huc_fields["huc12"]["length"] == 12
    assert "huc12num" not in huc["acquisition_fields"]
    streams = profiles["src:dasc-streams"]
    assert streams["metadata"]["objectIdField"] == "FID"  # not the separate OBJECTID attribute
    assert "STRAHLER" in streams["acquisition_fields"]
    assert profiles["src:dasc-plss"]["acquisition_fields"] == ["OBJECTID", "T_R"]


def _fixtures(kind: str) -> list[Path]:
    return sorted((FIXTURE_ROOT / kind).glob("*.json"))


def _run(entrypoint: Path, *arguments: object, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(entrypoint), *(str(value) for value in arguments)],
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_declared_schema_is_a_bounded_alias() -> None:
    schema = json.loads(DECLARED_SCHEMA.read_text(encoding="utf-8"))

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == (
        "kfm://schemas/contracts/v1/sources/source_descriptor.schema.json"
    )
    assert schema["$ref"] == (
        "https://schemas.kfm.local/contracts/v1/source/"
        "source_descriptor.schema.json"
    )
    assert "properties" not in schema
    assert "additionalProperties" not in schema
    assert schema["x-kfm"]["canonical_implementation_schema"] == (
        "schemas/contracts/v1/source/source_descriptor.schema.json"
    )
    assert schema["x-kfm"]["fixtures_root"] == (
        "fixtures/contracts/v1/source/source_descriptor/"
    )
    assert schema["x-kfm"]["validator"] == (
        "tools/validators/sources/validate_source_descriptor.py"
    )


def test_declared_and_implementation_schemas_have_identical_fixture_polarity() -> None:
    valid = _fixtures("valid")
    invalid = _fixtures("invalid")
    assert valid
    assert invalid

    implementation = load_validator(IMPLEMENTATION_SCHEMA)
    declared = load_validator(DECLARED_SCHEMA)

    for fixture in valid:
        candidate = json.loads(fixture.read_text(encoding="utf-8"))
        assert not list(implementation.iter_errors(candidate)), fixture
        assert not list(declared.iter_errors(candidate)), fixture

    for fixture in invalid:
        candidate = json.loads(fixture.read_text(encoding="utf-8"))
        assert list(implementation.iter_errors(candidate)), fixture
        assert list(declared.iter_errors(candidate)), fixture


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_fixture_mode_is_cwd_independent(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    result = _run(entrypoint, "--fixtures", cwd=tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK " in result.stdout
    assert "EXPECTED_FAIL " in result.stdout
    assert not any(line.startswith("FAIL ") for line in result.stdout.splitlines())


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_entrypoints_require_an_explicit_input(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    result = _run(entrypoint, cwd=tmp_path)

    assert result.returncode == 2
    assert result.stdout == ""
    assert "No files provided" in result.stderr


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_entrypoints_match_explicit_file_polarity(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    valid = _fixtures("valid")[0]
    invalid = _fixtures("invalid")[0]

    valid_result = _run(entrypoint, valid, cwd=tmp_path)
    invalid_result = _run(entrypoint, invalid, cwd=tmp_path)

    assert valid_result.returncode == 0, valid_result.stdout + valid_result.stderr
    assert valid_result.stdout.startswith("OK ")
    assert invalid_result.returncode == 1
    assert invalid_result.stdout.startswith("FAIL ")
