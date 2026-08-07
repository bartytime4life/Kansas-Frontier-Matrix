"""Tests for release trust projection manifests."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/release/validate_trust_projection_manifest.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/release/trust_projection_manifest"
SPEC = importlib.util.spec_from_file_location("kfm_trust_projection_manifest", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(kind: str, name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / kind / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_all_valid_projection_types_pass() -> None:
    for name in [
        "asset_integrity_verified.json",
        "time_slice_manifest.json",
        "review_packet_reference.json",
        "governance_change_record.json",
    ]:
        assert MODULE.validate(FIXTURES / "valid" / name).ok, name


def test_invalid_projection_types_fail_closed() -> None:
    expected = {
        "asset_mismatch_marked_verified.json": {"ASSET_INTEGRITY_OUTCOME_MISMATCH"},
        "time_slice_missing_rollback.json": {"SCHEMA_INVALID"},
        "review_packet_approval_authority.json": {"SCHEMA_INVALID"},
        "governance_change_missing_decision.json": {"GOVERNANCE_DECISION_REF_REQUIRED"},
    }
    for name, codes in expected.items():
        result = MODULE.validate(FIXTURES / "invalid" / name)
        assert not result.ok, name
        assert codes.issubset({finding.code for finding in result.findings}), name


def test_integrity_verified_is_digest_equality_not_release_authority() -> None:
    value = load("valid", "asset_integrity_verified.json")
    assert value["expected_sha256"] == value["observed_sha256"]
    assert value["outcome"] == "VERIFIED"
    assert value["governance"] == {
        "fixture_only": True,
        "lifecycle_write": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "publication_authorized": False,
    }


def test_review_packet_is_read_only_and_expires() -> None:
    value = load("valid", "review_packet_reference.json")
    assert value["access_mode"] == "READ_ONLY"
    assert value["approval_authority"] is False
    value["evaluated_at"] = "2026-04-15T00:00:00Z"
    value["status"] = "ACTIVE"
    value["spec_hash"] = MODULE.canonical_hash(value)
    target = FIXTURES / "invalid" / "_temporary_status_test.json"
    try:
        target.write_text(json.dumps(value), encoding="utf-8")
        result = MODULE.validate(target)
        assert MODULE.Finding("REVIEW_PACKET_STATUS_MISMATCH", "/status") in result.findings
    finally:
        target.unlink(missing_ok=True)
