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


def test_implementation_schema_fixture_root_matches_executable_root() -> None:
    schema = json.loads(IMPLEMENTATION_SCHEMA.read_text(encoding="utf-8"))
    declared = schema["x-kfm"]["fixtures_root"]
    assert declared.endswith("/")
    assert (ROOT / declared).resolve() == FIXTURE_ROOT.resolve()
    assert FIXTURE_ROOT.is_dir()


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


@pytest.fixture(params=(IMPLEMENTATION_SCHEMA, DECLARED_SCHEMA), ids=("rich", "alias"))
def rights_validator(request):
    return load_validator(request.param)


@pytest.fixture
def unverified_rights_candidate():
    descriptor = json.loads(
        (FIXTURE_ROOT / "valid/valid_usdm_inactive.json").read_text()
    )
    descriptor["rights"]["last_verified_at"] = None
    descriptor["rights"]["verified_by"] = None
    return descriptor


@pytest.mark.parametrize(
    "status,review,activation",
    (("unknown", "needs_review", "disabled"), ("noassertion", "draft", "fixture_only")),
)
def test_unverified_rights_null_profile_passes_without_fabricated_review(
    rights_validator, unverified_rights_candidate, status, review, activation
):
    descriptor = unverified_rights_candidate
    descriptor["rights"]["rights_status"] = status
    descriptor["review_state"] = review
    descriptor["connectors"]["activation_state"] = activation
    assert not list(rights_validator.iter_errors(descriptor))


@pytest.mark.parametrize(
    "path,value",
    (
        (("rights", "rights_status"), "verified_open"),
        (("rights", "rights_status"), "verified_restricted"),
        (("rights", "rights_status"), "permission_required"),
        (("rights", "rights_status"), "denied"),
        (("rights", "redistribution_allowed"), "yes"),
        (("rights", "commercial_use_allowed"), "yes"),
        (("review_state",), "reviewed"),
        (("review_state",), "approved"),
        (("lifecycle", "registry_state"), "active"),
        (("release_state",), "candidate"),
        (("release_state",), "released"),
        (("connectors", "activation_state"), "live_candidate"),
        (("connectors", "activation_state"), "live_active"),
        (("public_release", "allowed"), True),
        (("public_release", "requires_review"), False),
    ),
)
def test_null_review_metadata_cannot_upgrade_candidate_posture(
    rights_validator, unverified_rights_candidate, path, value
):
    target = unverified_rights_candidate
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    errors = list(rights_validator.iter_errors(unverified_rights_candidate))
    assert any(tuple(error.absolute_path) == path for error in errors)


@pytest.mark.parametrize(
    "field,value",
    (("last_verified_at", "2026-07-28T00:00:00Z"), ("verified_by", "fixture reviewer")),
)
def test_partial_null_verification_pair_is_rejected(
    rights_validator, unverified_rights_candidate, field, value
):
    unverified_rights_candidate["rights"][field] = value
    errors = list(rights_validator.iter_errors(unverified_rights_candidate))
    assert any(list(error.absolute_path) == ["rights", field] for error in errors)


@pytest.mark.parametrize("field", ("last_verified_at", "verified_by"))
def test_unverified_fields_remain_required(
    rights_validator, unverified_rights_candidate, field
):
    del unverified_rights_candidate["rights"][field]
    errors = list(rights_validator.iter_errors(unverified_rights_candidate))
    assert any(
        list(error.absolute_path) == ["rights"] and error.validator == "required"
        for error in errors
    )


@pytest.mark.parametrize("remove_object", (True, False))
def test_null_profile_requires_explicit_connector_inactivity(
    rights_validator, unverified_rights_candidate, remove_object
):
    if remove_object:
        del unverified_rights_candidate["connectors"]
        expected_path = []
    else:
        del unverified_rights_candidate["connectors"]["activation_state"]
        expected_path = ["connectors"]
    errors = list(rights_validator.iter_errors(unverified_rights_candidate))
    assert any(
        list(error.absolute_path) == expected_path and error.validator == "required"
        for error in errors
    )


@pytest.mark.parametrize(
    "path", (("source_head", "observed_at"), ("lifecycle", "created_at"))
)
def test_other_datetime_fields_do_not_become_nullable(
    rights_validator, unverified_rights_candidate, path
):
    unverified_rights_candidate[path[0]][path[1]] = None
    errors = list(rights_validator.iter_errors(unverified_rights_candidate))
    assert any(tuple(error.absolute_path) == path for error in errors)


@pytest.mark.parametrize(
    "field,value", (("last_verified_at", "not-a-date"), ("verified_by", ""))
)
def test_non_null_verification_still_requires_valid_values(
    rights_validator, unverified_rights_candidate, field, value
):
    descriptor = unverified_rights_candidate
    descriptor["rights"].update(
        last_verified_at="2026-07-28T00:00:00Z",
        verified_by="synthetic fixture reviewer",
    )
    descriptor["rights"][field] = value
    errors = list(rights_validator.iter_errors(descriptor))
    assert any(list(error.absolute_path) == ["rights", field] for error in errors)


def test_legacy_non_null_unknown_rights_record_still_passes(
    rights_validator, unverified_rights_candidate
):
    unverified_rights_candidate["rights"].update(
        last_verified_at="2026-07-28T00:00:00Z",
        verified_by="synthetic fixture reviewer",
    )
    assert not list(rights_validator.iter_errors(unverified_rights_candidate))
