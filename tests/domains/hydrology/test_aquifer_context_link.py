"""Bounded, offline AquiferContextLink shape and polarity checks.

These tests enforce type separation only. They do not resolve either endpoint,
close evidence, decide policy, approve release, or transfer Geology authority.
"""

from __future__ import annotations

import json
import socket
import urllib.request
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators.domains.hydrology import validate_aquifer_context_link


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/aquifer_context_link.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hydrology/aquifer_context_link"
NETWORK_DENIAL = "network access is forbidden in Hydrology domain tests"


def _deny_network(*_args: object, **_kwargs: object) -> None:
    raise AssertionError(NETWORK_DENIAL)


@pytest.fixture(autouse=True)
def deny_network(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(socket.socket, "connect", _deny_network)
    monkeypatch.setattr(socket, "create_connection", _deny_network)
    monkeypatch.setattr(socket, "getaddrinfo", _deny_network)
    monkeypatch.setattr(urllib.request, "urlopen", _deny_network)


def test_fixture_polarity_is_enforced() -> None:
    assert validate_aquifer_context_link.run(
        SCHEMA_PATH,
        FIXTURE_ROOT,
        ["--fixtures"],
    ) == 0


@pytest.mark.parametrize(
    "fixture_name",
    [
        "invalid_measurement_payload.json",
        "invalid_geology_geometry.json",
        "invalid_endpoint_type.json",
        "invalid_subject_id_type_mismatch.json",
    ],
)
def test_link_rejects_collapsed_responsibilities(fixture_name: str) -> None:
    validator = load_validator(SCHEMA_PATH)
    fixture = json.loads(
        (FIXTURE_ROOT / "invalid" / fixture_name).read_text(encoding="utf-8")
    )
    assert list(validator.iter_errors(fixture))


def test_link_carries_only_typed_endpoint_references() -> None:
    fixture = json.loads(
        (FIXTURE_ROOT / "valid/valid_observation_link.json").read_text(
            encoding="utf-8"
        )
    )
    assert fixture["hydrology_subject"]["object_type"] == "AquiferObservation"
    assert fixture["geology_endpoint"] == {
        "owner_domain": "geology",
        "object_type": "HydrostratigraphicUnit",
        "id": "kfm:geology:hydrostratigraphic-unit:synthetic-001",
    }
    assert "measurement_value" not in fixture
    assert "aquifer_geometry" not in fixture


def test_network_guard_fails_closed() -> None:
    with pytest.raises(AssertionError, match=NETWORK_DENIAL):
        urllib.request.urlopen("https://example.invalid")
