"""Schema and semantic boundaries for the GMD 3 announcement candidate."""

from __future__ import annotations

import json
import socket
import urllib.request
from pathlib import Path
from unittest import mock

import pytest


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DESCRIPTOR_PATH = (
    ROOT
    / "fixtures/contracts/v1/source/source_descriptor/valid/"
    "valid_ku_news_gmd3_aem_announcement_2026_05_11.json"
)
SOURCE_DESCRIPTOR_SCHEMA_PATH = (
    ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
)
CAMPAIGN_SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/domains/geology/"
    "aem_survey_campaign.schema.json"
)
FIXTURE_ROOT = ROOT / "fixtures/domains/geology/aem_survey_campaign"
VALID_FIXTURE_PATH = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

SCHEMA_INVALID_FIXTURES = (
    "invalid_acquisition_claim.json",
    "invalid_campaign_state_completed.json",
    "invalid_correction_ref_scheme.json",
    "invalid_downstream_stage_field.json",
    "invalid_false_release_state.json",
    "invalid_missing_supporting_reference.json",
    "invalid_non_fixture_reference.json",
    "invalid_required_limitation_missing.json",
    "invalid_silent_supersession.json",
    "invalid_unscoped_planning_field.json",
)
SEMANTIC_ONLY_INVALID_FIXTURES = ("invalid_self_supersession.json",)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_validator(path: Path):
    from tools.validators._common.jsonschema_runner import load_validator

    return load_validator(path)


@pytest.fixture(autouse=True)
def _no_network():
    denied = RuntimeError(
        "network access is forbidden in GMD 3 AEM candidate tests"
    )
    patchers = (
        mock.patch.object(socket.socket, "connect", side_effect=denied),
        mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
        mock.patch.object(socket, "create_connection", side_effect=denied),
        mock.patch.object(socket, "getaddrinfo", side_effect=denied),
        mock.patch.object(urllib.request, "urlopen", side_effect=denied),
    )
    for patcher in patchers:
        patcher.start()
    yield
    for patcher in patchers:
        patcher.stop()


def test_source_descriptor_fixture_passes_source_descriptor_schema():
    validator = _get_validator(SOURCE_DESCRIPTOR_SCHEMA_PATH)
    errors = list(validator.iter_errors(_load(SOURCE_DESCRIPTOR_PATH)))
    assert not errors, "\n".join(error.message for error in errors)


def test_source_descriptor_is_document_specific_candidate_only():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert descriptor["source_id"] == (
        "src:ku-news-gmd3-aem-announcement-2026-05-11"
    )
    assert descriptor["source_role"] == "citation_source"
    assert descriptor["authority_rank"] == "candidate_only"
    assert descriptor["connectors"]["activation_state"] == "disabled"
    assert descriptor["public_release"]["allowed"] is False
    assert descriptor["review_state"] == "needs_review"
    assert descriptor["release_state"] == "not_released"


def test_valid_campaign_candidate_passes_schema_and_semantics():
    validator = _get_validator(CAMPAIGN_SCHEMA_PATH)
    document = _load(VALID_FIXTURE_PATH)
    errors = list(validator.iter_errors(document))
    assert not errors, "\n".join(error.message for error in errors)

    from tools.validators.domains.geology.validate_aem_campaign import (
        validate_file,
    )

    assert validate_file(VALID_FIXTURE_PATH) == []


def test_valid_campaign_candidate_is_time_scoped_and_sparse():
    document = _load(VALID_FIXTURE_PATH)
    assert document["announcement_reported_state"] == "planned"
    assert document["announcement_published_on"] == "2026-05-11"
    assert document["current_campaign_state"] == "unknown"
    assert document["acquisition_evidence_state"] == "not_bound_to_profile"
    assert document["claim_scope"] == "campaign_announcement"
    assert document["release_state"] == "not_released"
    forbidden = {
        "campaign_state",
        "acquisition_state",
        "survey_counties",
        "planned_target_depth",
        "product_id",
        "raw_source_ref",
        "processing_software_version",
        "inversion_software_version",
        "resistivity_units",
        "vertical_datum",
        "uncertainty",
        "footprint_geometry_ref",
    }
    assert not forbidden.intersection(document)


@pytest.mark.parametrize("name", SCHEMA_INVALID_FIXTURES)
def test_schema_invalid_candidate_is_rejected(name):
    validator = _get_validator(CAMPAIGN_SCHEMA_PATH)
    errors = list(
        validator.iter_errors(_load(INVALID_FIXTURE_DIR / name))
    )
    assert errors, f"{name} unexpectedly passed candidate schema validation"


@pytest.mark.parametrize(
    "name",
    SCHEMA_INVALID_FIXTURES + SEMANTIC_ONLY_INVALID_FIXTURES,
)
def test_every_invalid_candidate_is_rejected_by_semantic_validator(name):
    from tools.validators.domains.geology.validate_aem_campaign import (
        validate_file,
    )

    findings = validate_file(INVALID_FIXTURE_DIR / name)
    assert findings, f"{name} unexpectedly passed semantic validation"


@pytest.mark.parametrize("name", SEMANTIC_ONLY_INVALID_FIXTURES)
def test_cross_field_semantic_case_is_schema_valid_but_denied(name):
    validator = _get_validator(CAMPAIGN_SCHEMA_PATH)
    document = _load(INVALID_FIXTURE_DIR / name)
    assert not list(validator.iter_errors(document))

    from tools.validators.domains.geology.validate_aem_campaign import (
        validate_file,
    )

    findings = validate_file(INVALID_FIXTURE_DIR / name)
    assert [finding.code for finding in findings] == [
        "AEM_SELF_SUPERSESSION_DENIED"
    ]
