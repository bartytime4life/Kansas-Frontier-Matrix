"""Bounded, offline AquiferObservation shape and polarity checks.

These tests validate only the proposed local machine shape. They do not admit
sources, resolve evidence, apply policy, approve release, or establish
groundwater truth.
"""

from __future__ import annotations

import json
import socket
import urllib.request
from pathlib import Path

import pytest

from tools.validators.domains.hydrology import validate_aquifer_observation


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hydrology/aquifer_observation"
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
    assert validate_aquifer_observation.run(
        REPO_ROOT
        / "schemas/contracts/v1/domains/hydrology/aquifer_observation.schema.json",
        FIXTURE_ROOT,
        ["--fixtures"],
    ) == 0


def test_observation_is_valid_without_aquifer_context_link() -> None:
    fixture = json.loads(
        (FIXTURE_ROOT / "valid/valid_unlinked.json").read_text(encoding="utf-8")
    )
    assert "aquifer_context_link_refs" not in fixture
    assert fixture["object_type"] == "AquiferObservation"
    assert fixture["source_role"] == "observed"


def test_network_guard_fails_closed() -> None:
    with pytest.raises(AssertionError, match=NETWORK_DENIAL):
        socket.create_connection(("example.invalid", 443))
