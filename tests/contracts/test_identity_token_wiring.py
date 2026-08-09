from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/identity_token.schema.json"
EXPECTED_KINDS = ["run", "source", "decision", "review", "bundle", "actor"]


def _schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_identity_token_declared_surfaces_exist() -> None:
    schema = _schema()
    metadata = schema["x-kfm"]

    assert metadata["status"] == "PROPOSED"
    for field in ("contract_doc", "fixtures_root", "validator"):
        declared = REPO_ROOT / metadata[field]
        assert declared.exists(), f"declared IdentityToken surface is missing: {metadata[field]}"


def test_identity_token_fixture_lanes_are_non_vacuous_and_json() -> None:
    fixture_root = REPO_ROOT / _schema()["x-kfm"]["fixtures_root"]

    for lane in ("valid", "invalid"):
        fixtures = sorted((fixture_root / lane).glob("*.json"))
        assert fixtures, f"IdentityToken {lane} fixture lane is empty"
        for fixture in fixtures:
            parsed = json.loads(fixture.read_text(encoding="utf-8"))
            assert isinstance(parsed, dict), f"fixture must be a JSON object: {fixture}"


def test_identity_token_kind_vocabulary_does_not_drift_silently() -> None:
    schema = _schema()
    assert schema["properties"]["kind"]["enum"] == EXPECTED_KINDS


def test_declared_validator_targets_the_declared_schema_and_fixtures() -> None:
    schema = _schema()
    metadata = schema["x-kfm"]
    validator_source = (REPO_ROOT / metadata["validator"]).read_text(encoding="utf-8")

    assert "schemas/contracts/v1/common/identity_token.schema.json" in validator_source
    assert "fixtures/contracts/v1/common/identity_token" in validator_source
    assert "tools.validators._common.jsonschema_runner import run" in validator_source
