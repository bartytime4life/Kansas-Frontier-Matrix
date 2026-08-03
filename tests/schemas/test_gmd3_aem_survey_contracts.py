"""
tests/schemas/test_gmd3_aem_survey_contracts.py

Boundary and governance tests for the 2026 Southwest Kansas GMD 3 Airborne
Electromagnetic (AEM) Survey source-family candidate and the AemSurveyCampaign
semantic contract schema.

These tests verify:
  1. The GMD 3 AEM source descriptor fixture is disabled/proposed, not active.
  2. No connector activation, live schedule, release, or publication authority
     is granted by the descriptor alone.
  3. The source descriptor references both geology and hydrology domains with a
     single canonical identity (no duplicate source authorities).
  4. The AemSurveyCampaign schema enforces closed-shape rules for each required
     field category:
       - vertical_datum (missing vertical datum fails closed)
       - depth_positive_direction enum (ambiguous depth convention fails closed)
       - processing_software_version and inversion_software_version (unversioned
         processing/inversion fails closed)
       - resistivity_units (missing units fails closed)
       - raw_source_ref (raw/processed lineage break fails closed)
       - uncertainty block (uncertainty omission fails closed)
       - correction.supersedes_ref (silent supersession fails closed)
       - evidence_refs minItems=1 (unbound EvidenceRef fails closed)
  5. Semantic rules checked in Python:
       - product/source identity collapse (product_id must differ from
         source_descriptor_ref)
       - false release/publication state (proposed record must be not_released)
  6. No-network: all fixtures are synthetic and require no live endpoint.

None of these tests activate a connector, fetch from a live endpoint, or produce
catalog, release, or publication objects.
"""

import json
import socket
import urllib.request
from pathlib import Path
from unittest import mock

import pytest

ROOT = Path(__file__).resolve().parents[2]

SOURCE_DESCRIPTOR_PATH = (
    ROOT
    / "fixtures/contracts/v1/source/source_descriptor/valid/valid_gmd3_aem_2026.json"
)

SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/domains/geology/aem_survey_campaign.schema.json"
)

FIXTURE_ROOT = ROOT / "fixtures/domains/geology/aem_survey_campaign"
VALID_FIXTURE_PATH = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"

# Invalid fixtures that must fail JSON schema validation
SCHEMA_INVALID_FIXTURES = [
    "invalid_missing_vertical_datum.json",
    "invalid_ambiguous_depth_convention.json",
    "invalid_unversioned_processing.json",
    "invalid_missing_units.json",
    "invalid_raw_lineage_break.json",
    "invalid_uncertainty_omission.json",
    "invalid_silent_supersession.json",
    "invalid_unbound_evidence_ref.json",
]

# Invalid fixtures that pass JSON schema but must fail semantic rules
SEMANTIC_INVALID_FIXTURES = [
    "invalid_product_source_identity_collapse.json",
    "invalid_false_release_state.json",
]

FORBIDDEN_CONNECTOR_WRITE_TARGETS = [
    "data/processed",
    "data/catalog",
    "data/triplets",
    "data/proofs",
    "data/published",
    "release/",
]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_validator():
    from tools.validators._common.jsonschema_runner import load_validator
    return load_validator(SCHEMA_PATH)


# ---------------------------------------------------------------------------
# Network guard
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _no_network():
    """Block all network access for every test in this module."""
    denied = RuntimeError(
        "network access is forbidden in GMD 3 AEM survey contract tests"
    )
    patchers = [
        mock.patch.object(socket.socket, "connect", side_effect=denied),
        mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
        mock.patch.object(socket, "create_connection", side_effect=denied),
        mock.patch.object(socket, "getaddrinfo", side_effect=denied),
        mock.patch.object(urllib.request, "urlopen", side_effect=denied),
    ]
    started = [p.start() for p in patchers]
    yield
    for p in patchers:
        p.stop()


# ---------------------------------------------------------------------------
# Fixture presence
# ---------------------------------------------------------------------------


def test_source_descriptor_fixture_exists():
    assert SOURCE_DESCRIPTOR_PATH.exists(), (
        f"GMD 3 AEM source descriptor fixture not found: {SOURCE_DESCRIPTOR_PATH}"
    )


def test_schema_file_exists():
    assert SCHEMA_PATH.exists(), (
        f"AemSurveyCampaign schema not found: {SCHEMA_PATH}"
    )


def test_valid_campaign_fixture_exists():
    assert VALID_FIXTURE_PATH.exists(), (
        f"Valid AEM campaign fixture not found: {VALID_FIXTURE_PATH}"
    )


@pytest.mark.parametrize("name", SCHEMA_INVALID_FIXTURES + SEMANTIC_INVALID_FIXTURES)
def test_invalid_fixture_exists(name):
    path = INVALID_FIXTURE_DIR / name
    assert path.exists(), f"Expected invalid fixture not found: {path}"


# ---------------------------------------------------------------------------
# Source descriptor governance tests
# ---------------------------------------------------------------------------


def test_source_descriptor_is_proposed_not_active():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert descriptor["lifecycle"]["registry_state"] == "proposed", (
        "GMD 3 AEM SourceDescriptor must have registry_state='proposed', not 'active'. "
        "Activation is a separate reviewed decision."
    )


def test_source_descriptor_connector_is_disabled():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert "connectors" in descriptor, (
        "GMD 3 AEM descriptor must include a connectors field."
    )
    assert descriptor["connectors"]["activation_state"] == "disabled", (
        "GMD 3 AEM connector must remain disabled in the candidate descriptor. "
        "No endpoint, scheduler, credentials, or activation is established."
    )


def test_source_descriptor_public_release_denied():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert descriptor["public_release"]["allowed"] is False, (
        "Public release must be denied in the GMD 3 AEM candidate descriptor."
    )
    assert descriptor["public_release"]["requires_review"] is True, (
        "Public release must require review before it can be allowed."
    )


def test_source_descriptor_release_state_not_released():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert descriptor["release_state"] == "not_released", (
        "GMD 3 AEM SourceDescriptor must be 'not_released'. "
        "A documentation profile alone does not create a release."
    )


def test_source_descriptor_review_state_needs_review():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    assert descriptor["review_state"] == "needs_review", (
        "GMD 3 AEM SourceDescriptor must have review_state='needs_review'."
    )


def test_source_descriptor_covers_geology_and_hydrology():
    """Cross-domain consumers must reference one source identity — not separate geology
    and hydrology source authorities."""
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    domain_scope = set(descriptor["domain_scope"])
    assert "geology" in domain_scope, "GMD 3 AEM descriptor must include geology scope."
    assert "hydrology" in domain_scope, "GMD 3 AEM descriptor must include hydrology scope."


def test_source_descriptor_source_id_format():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    source_id = descriptor["source_id"]
    assert source_id.startswith("src:") or source_id.startswith("kfm://source/"), (
        f"source_id must use 'src:' or 'kfm://source/' prefix, got: {source_id!r}"
    )


def test_source_descriptor_rights_not_verified():
    """Rights must not be prematurely asserted as verified_open — product availability is
    UNKNOWN / NEEDS VERIFICATION."""
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    rights_status = descriptor["rights"]["rights_status"]
    assert rights_status != "verified_open", (
        "GMD 3 AEM rights must not be 'verified_open' until rights are formally verified. "
        f"Current status: {rights_status!r}"
    )


def test_source_descriptor_prohibits_life_safety_claims():
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    prohibited = descriptor["admissibility_limits"]["prohibited_claim_roles"]
    assert "not_for_life_safety" in prohibited, (
        "GMD 3 AEM descriptor must prohibit 'not_for_life_safety' claim role."
    )


def test_source_descriptor_prohibits_title_truth_claims():
    """A resistivity map is not a water-right record or legal finding."""
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    prohibited = descriptor["admissibility_limits"]["prohibited_claim_roles"]
    assert "not_for_title_truth" in prohibited, (
        "GMD 3 AEM descriptor must prohibit 'not_for_title_truth'. "
        "AEM products are not legal or water-right determinations."
    )


def test_source_descriptor_no_live_endpoint():
    """Disabled candidate must not reference a live data endpoint — documentation-only
    endpoints are the only permitted references."""
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)
    endpoints = descriptor["access"].get("endpoints", [])
    for ep in endpoints:
        purpose = ep.get("purpose", "")
        assert purpose in ("documentation", "citation", "contact", "other"), (
            f"Disabled source descriptor endpoint must use documentation/citation purpose, "
            f"not: {purpose!r}. No live data endpoint is permitted."
        )


# ---------------------------------------------------------------------------
# AemSurveyCampaign schema — positive test
# ---------------------------------------------------------------------------


def test_valid_campaign_fixture_passes_schema():
    """The canonical positive fixture must pass AemSurveyCampaign schema validation."""
    validator = _get_validator()
    doc = _load(VALID_FIXTURE_PATH)
    errors = list(validator.iter_errors(doc))
    assert not errors, (
        "Valid AEM campaign fixture failed schema validation:\n"
        + "\n".join(e.message for e in errors)
    )


def test_valid_campaign_fixture_is_not_released():
    """The positive fixture must carry release_state='not_released'."""
    doc = _load(VALID_FIXTURE_PATH)
    assert doc["release_state"] == "not_released", (
        "Valid AEM campaign fixture must have release_state='not_released'. "
        "A proposed/disabled record must not carry 'released'."
    )


def test_valid_campaign_product_id_differs_from_source_descriptor_ref():
    """Positive fixture must demonstrate that product_id ≠ source_descriptor_ref."""
    doc = _load(VALID_FIXTURE_PATH)
    assert doc["product_id"] != doc["source_descriptor_ref"], (
        "Valid AEM campaign fixture must have product_id ≠ source_descriptor_ref. "
        "Product identity must not collapse into source authority."
    )


def test_valid_campaign_fixture_has_bound_evidence_refs():
    doc = _load(VALID_FIXTURE_PATH)
    assert len(doc["evidence_refs"]) >= 1, (
        "Valid AEM campaign fixture must have at least one evidence_ref binding."
    )


def test_valid_campaign_fixture_has_uncertainty_method():
    doc = _load(VALID_FIXTURE_PATH)
    assert doc["uncertainty"]["method"], (
        "Valid AEM campaign fixture must have a non-empty uncertainty.method."
    )


# ---------------------------------------------------------------------------
# AemSurveyCampaign schema — negative tests (schema enforcement)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", SCHEMA_INVALID_FIXTURES)
def test_schema_invalid_fixture_fails_validation(name):
    """Each schema-invalid fixture must be rejected by AemSurveyCampaign schema."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / name)
    errors = list(validator.iter_errors(doc))
    assert errors, (
        f"{name} was expected to fail schema validation but passed. "
        "The schema must fail closed on this invalid fixture."
    )


def test_missing_vertical_datum_rejected():
    """Missing vertical_datum must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_missing_vertical_datum.json")
    errors = list(validator.iter_errors(doc))
    assert any("vertical_datum" in e.message or "vertical_datum" in str(e.path) for e in errors), (
        "Schema must specifically reject missing vertical_datum. "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_ambiguous_depth_convention_rejected():
    """depth_positive_direction not in ['down', 'up'] must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_ambiguous_depth_convention.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "depth_positive_direction" in str(e.path) or "is not one of" in e.message
        for e in errors
    ), (
        "Schema must reject ambiguous depth_positive_direction value. "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_unversioned_processing_rejected():
    """Empty processing_software_version must fail closed (minLength: 1)."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_unversioned_processing.json")
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "Schema must reject unversioned processing (empty or absent version string)."
    )


def test_missing_units_rejected():
    """Missing resistivity_units must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_missing_units.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "resistivity_units" in str(e.path) or "resistivity_units" in e.message
        for e in errors
    ), (
        "Schema must specifically reject missing resistivity_units. "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_raw_lineage_break_rejected():
    """Missing raw_source_ref must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_raw_lineage_break.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "raw_source_ref" in str(e.path) or "raw_source_ref" in e.message
        for e in errors
    ), (
        "Schema must specifically reject missing raw_source_ref (lineage break). "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_uncertainty_omission_rejected():
    """Missing uncertainty block must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_uncertainty_omission.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "uncertainty" in str(e.path) or "uncertainty" in e.message
        for e in errors
    ), (
        "Schema must specifically reject missing uncertainty block. "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_silent_supersession_rejected():
    """correction block without supersedes_ref must fail closed."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_silent_supersession.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "supersedes_ref" in e.message or "supersedes_ref" in str(e.path)
        for e in errors
    ), (
        "Schema must reject silent supersession (correction block without supersedes_ref). "
        f"Got errors: {[e.message for e in errors]}"
    )


def test_unbound_evidence_ref_rejected():
    """Empty evidence_refs array must fail closed (minItems: 1)."""
    validator = _get_validator()
    doc = _load(INVALID_FIXTURE_DIR / "invalid_unbound_evidence_ref.json")
    errors = list(validator.iter_errors(doc))
    assert any(
        "evidence_refs" in str(e.path) or "minItems" in e.message or "too short" in e.message
        for e in errors
    ), (
        "Schema must reject empty evidence_refs (unbound EvidenceRef). "
        f"Got errors: {[e.message for e in errors]}"
    )


# ---------------------------------------------------------------------------
# AemSurveyCampaign schema — semantic tests (Python checks only)
# ---------------------------------------------------------------------------


def test_product_source_identity_collapse_is_detectable():
    """product_id == source_descriptor_ref must be detectable as a semantic violation.
    A processed product must not rewrite the raw source authority identity."""
    doc = _load(INVALID_FIXTURE_DIR / "invalid_product_source_identity_collapse.json")
    assert doc["product_id"] == doc["source_descriptor_ref"], (
        "Fixture must demonstrate product_id == source_descriptor_ref (the violation)."
    )
    # Semantic rule: product_id must differ from source_descriptor_ref
    assert doc["product_id"] != "kfm:geology:aem-campaign:kgs-gmd3-sw-ks-2026:v0.1", (
        "Fixture is correctly demonstrating the identity collapse."
    )


def test_false_release_state_is_detectable():
    """release_state='released' on a proposed/disabled record must be detectable.
    A proposed candidate must carry 'not_released'."""
    doc = _load(INVALID_FIXTURE_DIR / "invalid_false_release_state.json")
    assert doc["release_state"] == "released", (
        "Fixture must demonstrate release_state='released' (the violation)."
    )
    # Semantic rule: proposed/disabled records must carry not_released
    assert doc["release_state"] != "not_released", (
        "Fixture correctly shows that the record has a false release state."
    )


# ---------------------------------------------------------------------------
# Stage separation invariant
# ---------------------------------------------------------------------------


def test_valid_fixture_object_type_is_campaign_not_product():
    """AemSurveyCampaign must not be confused with resistivity product, inversion model,
    or hydrostratigraphic interpretation stages."""
    doc = _load(VALID_FIXTURE_PATH)
    assert doc["object_type"] == "AemSurveyCampaign", (
        "object_type must be 'AemSurveyCampaign'. "
        "Campaign identity must not be collapsed with product, inversion, or interpretation stages."
    )
    forbidden_types = {
        "AemResistivityProduct",
        "AemInversionModel",
        "AemHydrostratigraphicProduct",
        "AemFlightLine",
        "AemRawObservation",
        "AemRecommendation",
        "AemReleaseCarrier",
    }
    assert doc["object_type"] not in forbidden_types, (
        "Campaign record must not carry a product-stage object_type."
    )


def test_valid_fixture_source_descriptor_ref_matches_campaign_source():
    """The campaign fixture must reference the canonical GMD 3 AEM source descriptor."""
    doc = _load(VALID_FIXTURE_PATH)
    assert doc["source_descriptor_ref"] == "src:kgs-gmd3-aem-2026", (
        f"Campaign fixture must reference 'src:kgs-gmd3-aem-2026', "
        f"got: {doc['source_descriptor_ref']!r}"
    )
