"""
tests/schemas/test_drought_separation_contracts.py

Anti-collapse boundary and governance tests for the DroughtObservation and
DroughtDeclaration object families.

These tests verify:
  1. DroughtObservation and DroughtDeclaration schemas cannot be substituted for one another.
  2. No validator derives Kansas legal stages from USDM D0-D4 polygon categories.
  3. Observation, legal-effective, publication, retrieval, and supersession time semantics
     are distinct and explicit.
  4. Exact positive and single-fault negative fixtures run without network access.
  5. Evidence/source bindings fail closed (unbound geometry or source → schema rejection).
  6. Current legal stage remains UNKNOWN unless supported by an unsuperseded official
     declaration source (unresolved/abstain legal instrument → stage must be 'unknown').
  7. Object-type discriminator fields prevent cross-family substitution.
  8. Forbidden fields (legal_stage on Observation; usdm_derived, observation_stage on
     Declaration) are rejected by the schema.
  9. additionalProperties: false — undeclared fields are rejected.

None of these tests activate a connector, fetch from a live endpoint, or
produce catalog, release, or publication objects.
"""

import json
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]

OBS_SCHEMA_PATH = (
    ROOT / "schemas/contracts/v1/domains/hazards/drought_observation.schema.json"
)
DECL_SCHEMA_PATH = (
    ROOT / "schemas/contracts/v1/domains/hazards/drought_declaration.schema.json"
)
REL_SCHEMA_PATH = (
    ROOT / "schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json"
)

OBS_FIXTURE_DIR = ROOT / "fixtures/domains/hazards/drought_observation"
DECL_FIXTURE_DIR = ROOT / "fixtures/domains/hazards/drought_declaration"
REL_FIXTURE_DIR = ROOT / "fixtures/domains/hazards/drought_obs_decl_relationship"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Schema file existence
# ---------------------------------------------------------------------------


def test_drought_observation_schema_exists():
    assert OBS_SCHEMA_PATH.exists(), (
        f"DroughtObservation schema missing: {OBS_SCHEMA_PATH}"
    )


def test_drought_declaration_schema_exists():
    assert DECL_SCHEMA_PATH.exists(), (
        f"DroughtDeclaration schema missing: {DECL_SCHEMA_PATH}"
    )


def test_drought_relationship_schema_exists():
    assert REL_SCHEMA_PATH.exists(), (
        f"DroughtObsDeclarationRelationship schema missing: {REL_SCHEMA_PATH}"
    )


# ---------------------------------------------------------------------------
# Anti-collapse: schemas cannot be substituted for one another
# ---------------------------------------------------------------------------


def test_observation_and_declaration_schemas_have_distinct_titles():
    """Observation and declaration schemas must have distinct titles (anti-collapse)."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    decl_schema = _load(DECL_SCHEMA_PATH)
    assert obs_schema["title"] != decl_schema["title"], (
        "DroughtObservation and DroughtDeclaration schemas must have distinct titles."
    )


def test_observation_schema_requires_observation_object_type():
    """DroughtObservation schema must const-restrict object_type to 'DroughtObservation'."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    assert obs_schema["properties"]["object_type"]["const"] == "DroughtObservation"


def test_declaration_schema_requires_declaration_object_type():
    """DroughtDeclaration schema must const-restrict object_type to 'DroughtDeclaration'."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    assert decl_schema["properties"]["object_type"]["const"] == "DroughtDeclaration"


def test_observation_schema_rejects_declaration_object_type():
    """A document with object_type='DroughtDeclaration' must fail the observation schema."""
    validator = load_validator(OBS_SCHEMA_PATH)
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    doc["object_type"] = "DroughtDeclaration"
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "Observation schema must reject object_type='DroughtDeclaration'."
    )


def test_declaration_schema_rejects_observation_object_type():
    """A document with object_type='DroughtObservation' must fail the declaration schema."""
    validator = load_validator(DECL_SCHEMA_PATH)
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    doc["object_type"] = "DroughtObservation"
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "Declaration schema must reject object_type='DroughtObservation'."
    )


def test_observation_valid_fixture_fails_declaration_schema():
    """A valid DroughtObservation fixture must be rejected by the DroughtDeclaration schema."""
    validator = load_validator(DECL_SCHEMA_PATH)
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "DroughtObservation fixture must not be accepted by DroughtDeclaration schema."
    )


def test_declaration_valid_fixture_fails_observation_schema():
    """A valid DroughtDeclaration fixture must be rejected by the DroughtObservation schema."""
    validator = load_validator(OBS_SCHEMA_PATH)
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "DroughtDeclaration fixture must not be accepted by DroughtObservation schema."
    )


# ---------------------------------------------------------------------------
# Valid fixture tests
# ---------------------------------------------------------------------------


def test_observation_valid_fixture_passes():
    """The canonical DroughtObservation valid fixture must pass schema validation."""
    validator = load_validator(OBS_SCHEMA_PATH)
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    errors = list(validator.iter_errors(doc))
    assert not errors, (
        "DroughtObservation valid fixture failed:\n"
        + "\n".join(e.message for e in errors)
    )


def test_declaration_valid_fixture_passes():
    """The canonical DroughtDeclaration valid fixture must pass schema validation."""
    validator = load_validator(DECL_SCHEMA_PATH)
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    errors = list(validator.iter_errors(doc))
    assert not errors, (
        "DroughtDeclaration valid fixture failed:\n"
        + "\n".join(e.message for e in errors)
    )


def test_relationship_valid_fixture_passes():
    """The canonical DroughtObsDeclarationRelationship valid fixture must pass schema validation."""
    validator = load_validator(REL_SCHEMA_PATH)
    doc = _load(REL_FIXTURE_DIR / "valid/valid_1.json")
    errors = list(validator.iter_errors(doc))
    assert not errors, (
        "DroughtObsDeclarationRelationship valid fixture failed:\n"
        + "\n".join(e.message for e in errors)
    )


# ---------------------------------------------------------------------------
# Negative fixture tests (observation)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("fixture_name", [
    "invalid_1_observation_carries_legal_stage.json",
    "invalid_2_unbound_geometry.json",
    "invalid_3_unknown_severity_vocabulary.json",
    "invalid_4_declaration_derived.json",
    "invalid_5_undeclared_fields.json",
    "invalid_6_wrong_object_type.json",
    "invalid_7_missing_source_ref.json",
])
def test_observation_invalid_fixture_fails(fixture_name: str):
    """Each single-fault DroughtObservation negative fixture must fail schema validation."""
    validator = load_validator(OBS_SCHEMA_PATH)
    path = OBS_FIXTURE_DIR / "invalid" / fixture_name
    assert path.exists(), f"Invalid observation fixture not found: {path}"
    doc = _load(path)
    errors = list(validator.iter_errors(doc))
    assert errors, (
        f"DroughtObservation invalid fixture must fail but passed: {fixture_name}"
    )


# ---------------------------------------------------------------------------
# Negative fixture tests (declaration)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("fixture_name", [
    "invalid_1_declaration_derived_from_usdm.json",
    "invalid_2_carries_observation_stage.json",
    "invalid_3_missing_legal_instrument.json",
    "invalid_4_mismatched_effective_time.json",
    "invalid_5_silent_supersession.json",
    "invalid_6_wrong_object_type.json",
    "invalid_7_abstain_but_stage_asserted.json",
])
def test_declaration_invalid_fixture_fails(fixture_name: str):
    """Each single-fault DroughtDeclaration negative fixture must fail schema validation."""
    validator = load_validator(DECL_SCHEMA_PATH)
    path = DECL_FIXTURE_DIR / "invalid" / fixture_name
    assert path.exists(), f"Invalid declaration fixture not found: {path}"
    doc = _load(path)
    errors = list(validator.iter_errors(doc))
    assert errors, (
        f"DroughtDeclaration invalid fixture must fail but passed: {fixture_name}"
    )


# ---------------------------------------------------------------------------
# Negative fixture tests (relationship)
# ---------------------------------------------------------------------------


def test_relationship_invalid_derivation_claimed_fails():
    """A relationship record with derivation_claimed=true must fail schema validation."""
    validator = load_validator(REL_SCHEMA_PATH)
    path = REL_FIXTURE_DIR / "invalid/invalid_1_derivation_claimed.json"
    assert path.exists(), f"Invalid relationship fixture not found: {path}"
    doc = _load(path)
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "Relationship record with derivation_claimed=true must be rejected."
    )


# ---------------------------------------------------------------------------
# Anti-collapse hard invariants
# ---------------------------------------------------------------------------


def test_observation_schema_forbids_legal_stage_field():
    """DroughtObservation schema must forbid the 'legal_stage' field (not{} rule)."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    assert "legal_stage" in obs_schema["properties"], (
        "Observation schema must define 'legal_stage' as a forbidden property."
    )
    assert "not" in obs_schema["properties"]["legal_stage"], (
        "Observation schema must use 'not: {}' to forbid 'legal_stage'."
    )


def test_declaration_schema_forbids_usdm_derived_field():
    """DroughtDeclaration schema must forbid the 'usdm_derived' field (not{} rule)."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    assert "usdm_derived" in decl_schema["properties"], (
        "Declaration schema must define 'usdm_derived' as a forbidden property."
    )
    assert "not" in decl_schema["properties"]["usdm_derived"], (
        "Declaration schema must use 'not: {}' to forbid 'usdm_derived'."
    )


def test_declaration_schema_forbids_observation_stage_field():
    """DroughtDeclaration schema must forbid the 'observation_stage' field (not{} rule)."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    assert "observation_stage" in decl_schema["properties"], (
        "Declaration schema must define 'observation_stage' as a forbidden property."
    )
    assert "not" in decl_schema["properties"]["observation_stage"], (
        "Declaration schema must use 'not: {}' to forbid 'observation_stage'."
    )


def test_observation_schema_has_additional_properties_false():
    """DroughtObservation schema must set additionalProperties: false."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    assert obs_schema.get("additionalProperties") is False, (
        "DroughtObservation schema must set additionalProperties: false to reject undeclared fields."
    )


def test_declaration_schema_has_additional_properties_false():
    """DroughtDeclaration schema must set additionalProperties: false."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    assert decl_schema.get("additionalProperties") is False, (
        "DroughtDeclaration schema must set additionalProperties: false to reject undeclared fields."
    )


def test_declaration_schema_severity_enum_excludes_usdm_categories():
    """DroughtDeclaration declaration_stage must not include D0-D4 values."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    stage_enum = decl_schema["properties"]["declaration_stage"]["enum"]
    usdm_categories = {"D0", "D1", "D2", "D3", "D4", "None"}
    overlap = usdm_categories & set(stage_enum)
    assert not overlap, (
        f"DroughtDeclaration declaration_stage enum must not include USDM categories. "
        f"Found forbidden values: {overlap}"
    )


def test_observation_valid_fixture_has_no_legal_stage():
    """Valid DroughtObservation fixture must contain no legal stage fields."""
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    assert "legal_stage" not in doc, (
        "DroughtObservation valid fixture must not contain 'legal_stage'."
    )
    assert "declaration_stage" not in doc, (
        "DroughtObservation valid fixture must not contain 'declaration_stage'."
    )


def test_declaration_valid_fixture_has_no_usdm_severity():
    """Valid DroughtDeclaration fixture must contain no USDM severity fields."""
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    assert "source_native_severity" not in doc, (
        "DroughtDeclaration valid fixture must not contain 'source_native_severity'."
    )
    assert "usdm_derived" not in doc, (
        "DroughtDeclaration valid fixture must not contain 'usdm_derived'."
    )
    assert "observation_stage" not in doc, (
        "DroughtDeclaration valid fixture must not contain 'observation_stage'."
    )


def test_declaration_unknown_stage_when_instrument_unresolved():
    """When legal_instrument_resolution_status is 'unresolved', declaration_stage must be 'unknown'."""
    validator = load_validator(DECL_SCHEMA_PATH)
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    doc["legal_instrument_ref"] = None
    doc["legal_instrument_resolution_status"] = "unresolved"
    doc["declaration_stage"] = "emergency"
    errors = list(validator.iter_errors(doc))
    assert errors, (
        "Declaration with unresolved legal instrument must not assert a non-unknown stage."
    )

    doc["declaration_stage"] = "unknown"
    errors = list(validator.iter_errors(doc))
    assert not errors, (
        "Declaration with unresolved legal instrument and stage='unknown' should be valid."
    )


def test_relationship_derivation_claimed_must_always_be_false():
    """Relationship schema must const-restrict derivation_claimed to false."""
    rel_schema = _load(REL_SCHEMA_PATH)
    assert rel_schema["properties"]["derivation_claimed"]["const"] is False, (
        "derivation_claimed must be const: false in DroughtObsDeclarationRelationship schema."
    )


def test_valid_observation_fixture_no_network_required():
    """DroughtObservation valid fixture must declare no_network_required."""
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    assert doc["_fixture_meta"]["network_status"] == "no_network_required"


def test_valid_declaration_fixture_no_network_required():
    """DroughtDeclaration valid fixture must declare no_network_required."""
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    assert doc["_fixture_meta"]["network_status"] == "no_network_required"


def test_valid_observation_fixture_no_sensitive_data():
    doc = _load(OBS_FIXTURE_DIR / "valid/valid_1.json")
    assert doc["_fixture_meta"]["sensitive_data"] is False


def test_valid_declaration_fixture_no_sensitive_data():
    doc = _load(DECL_FIXTURE_DIR / "valid/valid_1.json")
    assert doc["_fixture_meta"]["sensitive_data"] is False


def test_observation_schema_has_separate_time_fields():
    """Observation schema must define separate observed_at, retrieved_at, and publication_time."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    props = obs_schema["properties"]
    assert "observed_at" in props, "Observation schema must have 'observed_at'."
    assert "retrieved_at" in props, "Observation schema must have 'retrieved_at'."
    assert "publication_time" in props, "Observation schema must have 'publication_time'."
    # These are distinct concepts — verify they are not aliased
    assert props["observed_at"] != props["retrieved_at"]
    assert props["observed_at"] != props["publication_time"]


def test_declaration_schema_has_separate_time_fields():
    """Declaration schema must define separate effective_at, rescinded_at, and retrieved_at."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    props = decl_schema["properties"]
    assert "effective_at" in props, "Declaration schema must have 'effective_at'."
    assert "rescinded_at" in props, "Declaration schema must have 'rescinded_at'."
    assert "retrieved_at" in props, "Declaration schema must have 'retrieved_at'."
    assert props["effective_at"] != props["retrieved_at"]


def test_observation_schema_anti_collapse_annotation():
    """DroughtObservation schema must carry the anti-collapse annotation."""
    obs_schema = _load(OBS_SCHEMA_PATH)
    anti_collapse = obs_schema.get("x-kfm", {}).get("anti_collapse_rule", "")
    assert "D0" in anti_collapse or "anti" in anti_collapse.lower() or "separate" in anti_collapse.lower(), (
        "DroughtObservation schema must carry an anti_collapse_rule annotation."
    )


def test_declaration_schema_anti_collapse_annotation():
    """DroughtDeclaration schema must carry the anti-collapse annotation."""
    decl_schema = _load(DECL_SCHEMA_PATH)
    anti_collapse = decl_schema.get("x-kfm", {}).get("anti_collapse_rule", "")
    assert "D0" in anti_collapse or "anti" in anti_collapse.lower() or "separate" in anti_collapse.lower(), (
        "DroughtDeclaration schema must carry an anti_collapse_rule annotation."
    )
