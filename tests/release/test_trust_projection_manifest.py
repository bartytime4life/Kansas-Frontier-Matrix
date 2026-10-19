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


def rebound(name: str, change) -> dict[str, object]:
    """A valid fixture with one change and a recomputed spec_hash, so only that change can fail it."""
    value = load("valid", name)
    change(value)
    value["spec_hash"] = MODULE.canonical_hash(value)
    return value


def codes(tmp_path: Path, value: object, raw: str | bytes | None = None) -> set[str]:
    target = tmp_path / "candidate.json"
    if raw is None:
        raw = json.dumps(value)
    target.write_bytes(raw.encode() if isinstance(raw, str) else raw)
    return {finding.code for finding in MODULE.validate(target).findings}


PACKET = "review_packet_reference.json"


def test_review_packet_revocation_is_read_in_any_utc_offset(tmp_path: Path) -> None:
    # Revoked at 06:00 UTC and evaluated at 12:00 UTC, so the packet is REVOKED however the instant is written.
    for revoked_at in ("2026-04-13T06:00:00Z", "2026-04-13T06:00:00+00:00", "2026-04-13T01:00:00-05:00", "2026-04-13t06:00:00z"):
        still_active = rebound(PACKET, lambda v, r=revoked_at: v.update(revoked_at=r))
        assert codes(tmp_path, still_active) == {"REVIEW_PACKET_STATUS_MISMATCH"}, revoked_at
        assert codes(tmp_path, rebound(PACKET, lambda v, r=revoked_at: v.update(revoked_at=r, status="REVOKED"))) == set(), revoked_at
    # Revocation is inclusive: revoked at the evaluation instant already applies.
    boundary = rebound(PACKET, lambda v: v.update(revoked_at="2026-04-13T07:00:00-05:00"))
    assert codes(tmp_path, boundary) == {"REVIEW_PACKET_STATUS_MISMATCH"}
    # A revocation after the evaluation instant does not yet apply.
    later = rebound(PACKET, lambda v: v.update(revoked_at="2026-04-13T08:00:00-05:00"))
    assert codes(tmp_path, later) == set()


def test_review_packet_times_accept_every_rfc3339_offset(tmp_path: Path) -> None:
    shifted = rebound(PACKET, lambda v: v.update(issued_at="2026-04-12T19:00:00-05:00", evaluated_at="2026-04-13t12:00:00z",
                                                expires_at="2026-04-14T05:30:00+05:30"))
    assert codes(tmp_path, shifted) == set()


def test_review_packet_lifecycle_rules(tmp_path: Path) -> None:
    assert codes(tmp_path, rebound(PACKET, lambda v: v.update(evaluated_at="2026-04-12T23:00:00Z"))) == {"REVIEW_PACKET_NOT_YET_ISSUED"}
    assert codes(tmp_path, rebound(PACKET, lambda v: v.update(expires_at="2026-04-13T00:00:00Z"))) == {"REVIEW_PACKET_TIME_INVALID"}
    # Expiry is inclusive: evaluated exactly at expires_at is EXPIRED.
    assert codes(tmp_path, rebound(PACKET, lambda v: v.update(evaluated_at="2026-04-14T00:00:00Z", status="EXPIRED"))) == set()


def test_unreadable_revocation_is_not_treated_as_never_revoked() -> None:
    # The date-time format check normally rejects these first; without it the rules still must not read them as absent.
    for revoked_at in ("yesterday", "2026-04-13T06:00:00", 5):
        value = rebound(PACKET, lambda v, r=revoked_at: v.update(revoked_at=r))
        assert MODULE.Finding("REVIEW_PACKET_TIME_INVALID", "/") in MODULE.semantic_findings(value), revoked_at


def test_instants_outside_the_utc_range_are_findings_not_crashes(tmp_path: Path) -> None:
    # Valid RFC 3339 that overflows when normalized to UTC.
    assert codes(tmp_path, rebound(PACKET, lambda v: v.update(issued_at="0001-01-01T00:00:00+00:01"))) == {"REVIEW_PACKET_TIME_INVALID"}
    late = rebound("time_slice_manifest.json", lambda v: v["valid_time"].update(end="9999-12-31T23:59:59-00:01"))
    assert codes(tmp_path, late) == {"TIME_SLICE_INTERVAL_INVALID"}


def test_sub_microsecond_instants_stay_distinct(tmp_path: Path) -> None:
    # datetime keeps only microseconds; RFC 3339 allows more digits, and these instants must not compare equal.
    active = rebound(PACKET, lambda v: v.update(evaluated_at="2026-04-13T12:00:00.0000001+00:00",
                                               revoked_at="2026-04-13T12:00:00.0000009+00:00"))
    assert codes(tmp_path, active) == set()
    revoked = rebound(PACKET, lambda v: v.update(evaluated_at="2026-04-13T12:00:00.0000009+00:00",
                                                revoked_at="2026-04-13T12:00:00.0000001+00:00"))
    assert codes(tmp_path, revoked) == {"REVIEW_PACKET_STATUS_MISMATCH"}
    reversed_slice = rebound("time_slice_manifest.json", lambda v: v["valid_time"].update(
        start="2026-04-13T12:00:00.0000009Z", end="2026-04-13T12:00:00.0000001Z"))
    assert codes(tmp_path, reversed_slice) == {"TIME_SLICE_INTERVAL_INVALID"}
    # The fraction is exact across offsets too: .5 at 07:00-05:00 equals .5000 at 12:00Z.
    assert MODULE._time("2026-04-13T07:00:00.5-05:00") == MODULE._time("2026-04-13T12:00:00.5000Z")


def test_time_slice_rules(tmp_path: Path) -> None:
    name = "time_slice_manifest.json"
    # Intervals compare instants: 14T04:00+05:00 is 13T23:00Z (inside), 13T20:00-05:00 is 14T01:00Z (after the end).
    assert codes(tmp_path, rebound(name, lambda v: v["valid_time"].update(start="2026-04-14T04:00:00+05:00"))) == set()
    assert codes(tmp_path, rebound(name, lambda v: v["valid_time"].update(start="2026-04-13T20:00:00-05:00"))) == {"TIME_SLICE_INTERVAL_INVALID"}
    assert codes(tmp_path, rebound(name, lambda v: v["assets"].append(dict(v["assets"][0])))) == {"TIME_SLICE_ASSET_DUPLICATE"}
    for status in ("CORRECTED", "WITHDRAWN"):
        assert codes(tmp_path, rebound(name, lambda v, s=status: v.update(status=s))) == {"TIME_SLICE_CORRECTION_REQUIRED"}
        assert codes(tmp_path, rebound(name, lambda v, s=status: v.update(status=s, correction_ref="correction:fixture:v1"))) == set()


def test_asset_integrity_outcome_is_derived_from_the_digests(tmp_path: Path) -> None:
    name = "asset_integrity_verified.json"
    other = "sha256:" + "5" * 64
    derived = {
        "MISSING_DECLARATION": {"expected_sha256": None},
        "INTERRUPTED": {"observed_sha256": None},
        "MISMATCH": {"observed_sha256": other},
    }
    for outcome, change in derived.items():
        assert codes(tmp_path, rebound(name, lambda v, c=change, o=outcome: v.update(c, outcome=o))) == set(), outcome
        assert codes(tmp_path, rebound(name, lambda v, c=change: v.update(c))) == {"ASSET_INTEGRITY_OUTCOME_MISMATCH"}, outcome
    assert codes(tmp_path, rebound(name, lambda v: v.update(byte_length=None))) == {"ASSET_VERIFIED_LENGTH_MISSING"}


def test_governance_change_decision_requirement(tmp_path: Path) -> None:
    name = "governance_change_record.json"
    for event in ("POLICY_UPDATED", "VOCABULARY_UPDATED", "WAIVER_ISSUED", "WAIVER_REVOKED"):
        assert codes(tmp_path, rebound(name, lambda v, e=event: v.update(event_type=e, decision_refs=[]))) == {"GOVERNANCE_DECISION_REF_REQUIRED"}, event
    assert codes(tmp_path, rebound(name, lambda v: v.update(event_type="MILESTONE_TRANSITION", decision_refs=[]))) == set()


def test_unreadable_inputs_are_named_findings(tmp_path: Path) -> None:
    assert codes(tmp_path, None, '{"a": 1, "a": 2}') == {"JSON_DUPLICATE_KEY"}
    assert codes(tmp_path, None, '{"a": NaN}') == {"JSON_NONFINITE_NUMBER"}
    assert codes(tmp_path, None, '{"a": 1e400}') == {"JSON_NONFINITE_NUMBER"}
    assert codes(tmp_path, None, '{"a": ') == {"JSON_INVALID"}
    # Excessive nesting and over-long integers used to escape as tracebacks.
    assert codes(tmp_path, None, '{"a": ' + "[" * 100_000 + "]" * 100_000 + "}") == {"JSON_INVALID"}
    assert codes(tmp_path, None, '{"a": ' + "9" * 5000 + "}") == {"JSON_INVALID"}
    assert codes(tmp_path, None, b'{"a": "\xff"}') == {"JSON_NOT_UTF8"}
    assert codes(tmp_path, None, "[]") == {"ROOT_NOT_OBJECT"}
    assert {f.code for f in MODULE.validate(tmp_path / "missing.json").findings} == {"INPUT_NOT_FILE"}


def test_cli_exit_codes(tmp_path: Path, capsys) -> None:
    good = tmp_path / "good.json"
    good.write_text(json.dumps(load("valid", PACKET)), encoding="utf-8")
    revoked = tmp_path / "revoked.json"
    revoked.write_text(json.dumps(rebound(PACKET, lambda v: v.update(revoked_at="2026-04-13T06:00:00+00:00"))), encoding="utf-8")
    assert MODULE.run([str(good)]) == 0
    assert MODULE.run([str(good), str(revoked)]) == 1
    assert MODULE.run(["--fixtures"]) == 0
    capsys.readouterr()
