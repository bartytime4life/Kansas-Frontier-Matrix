"""Tests for the fixture-only ReviewShareLink validator."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = REPO_ROOT / "tools/validators/review/review_share_link/validate_review_share_link.py"
VALID = REPO_ROOT / "fixtures/review/review_share_link/valid"
INVALID = REPO_ROOT / "fixtures/review/review_share_link/invalid"

SPEC = importlib.util.spec_from_file_location("kfm_review_share_link", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _load(directory: Path, name: str) -> dict[str, object]:
    value = json.loads((directory / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _rehash(payload: dict[str, object]) -> None:
    payload["spec_hash"] = MODULE.canonical_spec_hash(payload)


def test_active_fixture_is_valid_and_deterministic() -> None:
    payload = _load(VALID, "active.json")
    first = MODULE.validate_payload(payload)
    second = MODULE.validate_payload(copy.deepcopy(payload))
    assert first == second
    assert first.ok
    assert payload["state"] == "ACTIVE"
    assert payload["decision"] == {"outcome": "ALLOW", "reasons": []}


def test_expired_fixture_is_a_valid_deny() -> None:
    payload = _load(VALID, "expired.json")
    assert MODULE.validate_payload(payload).ok
    assert payload["decision"] == {"outcome": "DENY", "reasons": ["LINK_EXPIRED"]}


def test_revoked_fixture_is_a_valid_deny_and_precedes_expiry() -> None:
    payload = _load(VALID, "revoked.json")
    assert MODULE.validate_payload(payload).ok
    assert MODULE.expected_state(payload) == "REVOKED"


def test_unsafe_context_can_only_be_represented_as_a_valid_deny() -> None:
    payload = _load(VALID, "unsafe_context_denied.json")
    result = MODULE.validate_payload(payload)
    assert result.ok
    assert payload["decision"] == {"outcome": "DENY", "reasons": ["UNSAFE_CONTEXT_REF"]}


def test_unsafe_context_cannot_remain_allowed() -> None:
    payload = _load(VALID, "active.json")
    payload["context"]["manifest_ref"] = "https://example.invalid/data/raw/manifest.json"
    _rehash(payload)
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("DECISION_REASONS_MISMATCH", "/decision/reasons") in result.findings
    assert MODULE.Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome") in result.findings


def test_decision_mismatch_is_rejected() -> None:
    payload = _load(INVALID, "decision_mismatch.json")
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome") in result.findings


def test_plaintext_token_field_is_schema_denied() -> None:
    payload = _load(VALID, "active.json")
    payload["token"] = "Ab3kP9LmQ2"
    _rehash(payload)
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("SCHEMA_INVALID", "/") in result.findings


def test_state_must_match_evaluation_time() -> None:
    payload = _load(VALID, "active.json")
    payload["evaluated_at"] = "2026-04-19T00:00:00Z"
    _rehash(payload)
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("STATE_MISMATCH", "/state") in result.findings
    assert MODULE.Finding("DECISION_REASONS_MISMATCH", "/decision/reasons") in result.findings


def test_expiry_must_follow_creation() -> None:
    payload = _load(VALID, "active.json")
    payload["expires_at"] = payload["created_at"]
    payload["state"] = "EXPIRED"
    payload["decision"] = {"outcome": "DENY", "reasons": ["LINK_EXPIRED"]}
    _rehash(payload)
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("EXPIRY_NOT_AFTER_CREATED", "/expires_at") in result.findings


def test_spec_hash_mismatch_is_rejected() -> None:
    payload = _load(VALID, "active.json")
    payload["audience"] = "steward"
    result = MODULE.validate_payload(payload)
    assert MODULE.Finding("SPEC_HASH_MISMATCH", "/spec_hash") in result.findings
