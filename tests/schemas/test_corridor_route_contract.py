"""Fixture-only tests for the CorridorRoute schema and validator."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json"
VALIDATOR_PATH = ROOT / "tools/validators/domains/roads-rail-trade/validate_corridor_route.py"
FIXTURES_ROOT = ROOT / "fixtures/domains/roads-rail-trade/corridor_route"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_validator_module():
    spec = importlib.util.spec_from_file_location("corridor_route_validator", VALIDATOR_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_schema_and_validator_exist():
    assert SCHEMA_PATH.exists()
    assert VALIDATOR_PATH.exists()


def test_schema_pairs_to_current_contract_and_uses_draft_2020_12():
    schema = _load(SCHEMA_PATH)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["title"] == "CorridorRoute"
    assert schema["x-kfm"]["contract_doc"] == "contracts/domains/roads-rail-trade/corridor_route.md"


def test_source_packet_minimum_fields_are_machine_required():
    schema = _load(SCHEMA_PATH)
    required = set(schema["required"])
    assert {
        "id",
        "route_name",
        "feature_class",
        "approximate_dates",
        "date_uncertainty",
        "geometry_accuracy",
        "source_uri",
        "license",
        "evidence_refs",
        "confidence",
        "representation_layer",
        "changed",
    } <= required


def test_route_identity_cannot_be_replaced_by_segment_or_embedded_geometry():
    schema = _load(SCHEMA_PATH)
    assert schema["properties"]["feature_class"]["const"] == "route"
    for field in ("segments", "segment_ids", "geometry"):
        assert schema["properties"][field]["not"] == {}


def test_live_legal_and_publication_authority_fields_are_forbidden():
    schema = _load(SCHEMA_PATH)
    for field in ("legal_designation_status", "live_routing_authority", "publication_approved"):
        assert schema["properties"][field]["not"] == {}
    assert schema["additionalProperties"] is False


def test_valid_historic_candidate_passes_schema_and_validator():
    path = FIXTURES_ROOT / "valid/valid_historic_candidate.json"
    document = _load(path)
    assert not list(load_validator(SCHEMA_PATH).iter_errors(document))
    module = _load_validator_module()
    assert module.validate_file(path) == "PASS"


def test_unresolved_candidate_is_schema_valid_but_abstains():
    path = FIXTURES_ROOT / "valid/valid_unresolved_evidence.json"
    document = _load(path)
    assert not list(load_validator(SCHEMA_PATH).iter_errors(document))
    module = _load_validator_module()
    assert module.validate_file(path) == "ABSTAIN"


def test_all_negative_fixtures_are_denied():
    module = _load_validator_module()
    paths = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    assert len(paths) == 8
    for path in paths:
        assert module.validate_file(path) == "DENY", path.name


def test_spec_hash_is_deterministic_and_excludes_fixture_metadata():
    module = _load_validator_module()
    path = FIXTURES_ROOT / "valid/valid_historic_candidate.json"
    document = _load(path)
    assert document["spec_hash"] == module.compute_spec_hash(document)
    changed_meta = copy.deepcopy(document)
    changed_meta["_fixture_meta"]["fault"] = "metadata changes do not alter governed content"
    assert module.compute_spec_hash(changed_meta) == document["spec_hash"]
    changed_content = copy.deepcopy(document)
    changed_content["route_name"] = "Different synthetic route"
    assert module.compute_spec_hash(changed_content) != document["spec_hash"]


def test_released_posture_requires_governance_closure():
    validator = load_validator(SCHEMA_PATH)
    document = _load(FIXTURES_ROOT / "valid/valid_historic_candidate.json")
    document["claim_status"] = "released"
    document["release_posture"] = "released"
    errors = list(validator.iter_errors(document))
    assert errors


def test_authoritative_representation_requires_role_appropriate_source():
    validator = load_validator(SCHEMA_PATH)
    document = _load(FIXTURES_ROOT / "valid/valid_historic_candidate.json")
    document["source_role"] = "context"
    errors = list(validator.iter_errors(document))
    assert errors


def test_public_generalization_rejects_sensitive_geometry():
    module = _load_validator_module()
    path = FIXTURES_ROOT / "invalid/invalid_public_sensitive_geometry.json"
    assert module.validate_file(path) == "DENY"


def test_fixture_suite_is_no_network_and_synthetic():
    paths = sorted(FIXTURES_ROOT.rglob("*.json"))
    assert paths
    for path in paths:
        meta = _load(path)["_fixture_meta"]
        assert meta["network_status"] == "no_network_required"
        assert meta["sensitive_data"] is False
        assert meta["synthetic"] is True


def test_cli_fixture_runner_passes_expected_outcomes():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS" in result.stdout
    assert "ABSTAIN" in result.stdout
    assert "DENY" in result.stdout
