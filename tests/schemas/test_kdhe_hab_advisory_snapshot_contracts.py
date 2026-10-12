import hashlib
import json
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/hazards/kdhe_hab_advisory_snapshot.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/domains/hazards/kdhe_hab_advisory_snapshot"
SOURCE_DESCRIPTOR_PATH = (
    ROOT / "fixtures/contracts/v1/source/source_descriptor/valid/valid_kdhe_hab_inactive.json"
)


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _identity_key(doc: dict) -> str:
    return "|".join(
        [
            doc["source_id"],
            doc["source_product_id"],
            doc["source_surface_type"],
            doc["source_locator"],
            doc["water_body_name_native"].strip().lower(),
            ",".join(sorted(doc["county_names_native"])),
            doc["source_scope_native"],
            doc["zone_id"] or "-",
            doc["advisory_level_native"] or "-",
            doc["source_updated_at"] or "-",
            doc["content_digest"].lower(),
        ]
    )


def _snapshot_id(identity_key: str) -> str:
    return f"kdhe-hab:{hashlib.sha256(identity_key.encode('utf-8')).hexdigest()}"


@pytest.mark.parametrize("fixture", sorted((FIXTURE_ROOT / "valid").glob("valid_*.json")))
def test_valid_kdhe_hab_fixtures_pass_schema(fixture: Path) -> None:
    validator = load_validator(SCHEMA_PATH)
    doc = _load(fixture)
    errors = list(validator.iter_errors(doc))
    assert not errors, f"{fixture.name} should be valid but failed: {[e.message for e in errors]}"


@pytest.mark.parametrize("fixture", sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json")))
def test_invalid_kdhe_hab_fixtures_fail_schema(fixture: Path) -> None:
    validator = load_validator(SCHEMA_PATH)
    doc = _load(fixture)
    errors = list(validator.iter_errors(doc))
    assert errors, f"{fixture.name} should be invalid but passed"


@pytest.mark.parametrize("fixture", sorted((FIXTURE_ROOT / "valid").glob("valid_*.json")))
def test_snapshot_identity_is_deterministic(fixture: Path) -> None:
    doc = _load(fixture)
    identity_key = _identity_key(doc)
    assert doc["deterministic_identity_key"] == identity_key
    assert doc["advisory_snapshot_id"] == _snapshot_id(identity_key)


def test_lifted_and_superseded_lineage_is_preserved() -> None:
    hazard = _load(FIXTURE_ROOT / "valid" / "valid_hazard.json")
    lifted = _load(FIXTURE_ROOT / "valid" / "valid_lifted.json")

    assert hazard["normalized_state"] == "HAZARD"
    assert lifted["normalized_state"] == "LIFTED"
    assert lifted["supersedes_snapshot_id"] == hazard["advisory_snapshot_id"]


def test_source_unavailable_and_stale_states_do_not_clear_history() -> None:
    unavailable = _load(FIXTURE_ROOT / "valid" / "valid_source_unavailable.json")
    stale = _load(FIXTURE_ROOT / "valid" / "valid_stale_source.json")

    assert unavailable["normalized_state"] == "SOURCE_UNAVAILABLE"
    assert unavailable["supersedes_snapshot_id"] is not None
    assert unavailable["retrieval_status"] == "source_unavailable"

    assert stale["normalized_state"] == "STALE_SOURCE"
    assert stale["supersedes_snapshot_id"] is not None
    assert stale["freshness_status"] == "stale"


def test_duplicate_name_collision_fails_closed() -> None:
    duplicate_conflict = _load(FIXTURE_ROOT / "valid" / "valid_duplicate_name_conflict.json")

    assert duplicate_conflict["duplicate_name_collision"] is True
    assert duplicate_conflict["identity_resolution_status"] == "CONFLICT"
    assert duplicate_conflict["water_body_id"] is None
    assert duplicate_conflict["normalized_state"] == "IDENTITY_UNRESOLVED"


def test_zoned_advisory_preserves_zone_scope() -> None:
    zoned = _load(FIXTURE_ROOT / "valid" / "valid_zoned_warning.json")

    assert zoned["source_scope_native"] == "zone"
    assert zoned["scope_type"] == "zone"
    assert zoned["zone_id"] is not None
    assert zoned["geometry_ref"] is not None


def test_source_descriptor_candidate_is_inactive_and_kansas_connector_scoped() -> None:
    descriptor = _load(SOURCE_DESCRIPTOR_PATH)

    assert descriptor["source_id"] == "src:ks-kdhe-hab"
    assert descriptor["domain_scope"] == ["hazards"]
    assert descriptor["connectors"]["activation_state"] == "disabled"
    assert descriptor["connectors"]["connector_ref"].startswith("connectors/kansas/")
    assert descriptor["public_release"]["allowed"] is False
    assert descriptor["release_state"] == "not_released"


def test_publication_and_alerting_remain_denied_in_snapshot_contract() -> None:
    for fixture in sorted((FIXTURE_ROOT / "valid").glob("valid_*.json")):
        doc = _load(fixture)
        assert doc["publication_state"] == "denied"
        assert doc["alerts_allowed"] is False


def test_freshness_budget_is_fail_closed_for_volatile_safety_source() -> None:
    for fixture in sorted((FIXTURE_ROOT / "valid").glob("valid_*.json")):
        doc = _load(fixture)
        assert doc["freshness_budget_hours"] <= 24
