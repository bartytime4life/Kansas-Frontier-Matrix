"""Bounded, offline checks for the proposed Hydrology EvidenceBundle alias.

These tests establish only local JSON Schema shape and fixture polarity. They do
not resolve EvidenceRefs, prove evidence closure, admit sources, apply policy,
approve release, or establish Hydrology truth.
"""

from __future__ import annotations

import socket
import urllib.request
from pathlib import Path

import pytest

from tools.validators.domains.hydrology import validate_evidence_bundle


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hydrology/evidence_bundle"
VALID_FIXTURE = FIXTURE_ROOT / "valid/valid_1.json"
INVALID_FIXTURE = FIXTURE_ROOT / "invalid/invalid_1.json"
EXPECTED_ERROR = FIXTURE_ROOT / "invalid/invalid_1.expected_error.txt"
NETWORK_DENIAL = "network access is forbidden in Hydrology domain tests"


def _deny_network(*_args: object, **_kwargs: object) -> None:
    raise AssertionError(NETWORK_DENIAL)


@pytest.fixture(autouse=True)
def deny_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fail before any socket, DNS, or URL request can leave the test process."""

    monkeypatch.setattr(socket.socket, "connect", _deny_network)
    monkeypatch.setattr(socket, "create_connection", _deny_network)
    monkeypatch.setattr(socket, "getaddrinfo", _deny_network)
    monkeypatch.setattr(urllib.request, "urlopen", _deny_network)


def _run_fixture(path: Path) -> int:
    return validate_evidence_bundle.run(
        SCHEMA_PATH,
        FIXTURE_ROOT,
        [str(path)],
    )


def test_evidence_bundle_valid_fixture_is_accepted(capsys: pytest.CaptureFixture[str]) -> None:
    assert _run_fixture(VALID_FIXTURE) == 0
    assert capsys.readouterr().out == f"OK {VALID_FIXTURE}\n"


def test_evidence_bundle_invalid_fixture_is_rejected(capsys: pytest.CaptureFixture[str]) -> None:
    expected_error = EXPECTED_ERROR.read_text(encoding="utf-8").strip()

    assert _run_fixture(INVALID_FIXTURE) == 1

    output = capsys.readouterr().out
    assert output.startswith(f"FAIL {INVALID_FIXTURE}: ")
    assert expected_error in output


def test_network_guard_fails_closed_for_socket_and_url_calls() -> None:
    with pytest.raises(AssertionError, match=NETWORK_DENIAL):
        socket.create_connection(("example.invalid", 443))

    with pytest.raises(AssertionError, match=NETWORK_DENIAL):
        urllib.request.urlopen("https://example.invalid")
