"""Cross-version EvidenceTemporalPostureAssessment replay and recovery proof."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

from tools.release import temporal_replay as replay


@pytest.fixture
def fixture(tmp_path):
    root = tmp_path / "fixture"
    shutil.copytree(replay.FIXTURES, root)
    return root


def mutate(root, name, operation):
    path = root / name
    value = json.loads(path.read_bytes())
    operation(value)
    path.write_text(json.dumps(value, indent=2) + "\n")


def test_legacy_replay_successor_receipt_and_both_recovery_branches(fixture):
    before = replay.tree_bytes(fixture)
    report = replay.replay(fixture)
    assert replay.tree_bytes(fixture) == before
    assert report["outcome"] == "PASS"
    assert report["legacy_dual_read"] == "PASS"
    assert report["cross_family_false_acceptance"] is False
    assert report["common_and_evidence_chronology_distinct"] is True
    assert report["clock_fields_preserved"] == list(replay.CLOCKS)
    assert not any(report["authority"].values())
    assert report["branches"]["rollback"]["alias"]["release_id"] == replay.PREDECESSOR
    assert report["branches"]["withdrawal"]["alias"]["status"] == "WITHDRAWN"
    assert report["branches"]["withdrawal"]["alias"]["release_id"] is None
    for branch in report["branches"].values():
        assert branch["outcome"] == "PASS"
        assert branch["history_byte_identical"] is branch["plan_read_only"] is True
        assert branch["invalidations"] == list(replay.rollback.INVALIDATIONS)
    assert report == replay.replay(fixture)
    digest = report.pop("report_sha256")
    assert digest == replay.rollback.digest_bytes(replay.rollback.canonical(report))


def test_actual_restored_bytes_keep_fractional_precision_offsets_and_unknowns(fixture, monkeypatch):
    original = replay.rollback.rehearse
    observed = []
    expected = (fixture / "legacy.json").read_bytes()

    def inspect(root, scenario, *, apply=False):
        result = original(root, scenario, apply=apply)
        if apply:
            raw = (root / "releases" / replay.PREDECESSOR / "evidence.json").read_bytes()
            assert raw == expected
            clocks = json.loads(raw)["times"]
            assert clocks["observed_at"].endswith(".123456Z")
            assert clocks["source_updated_at"].endswith("+00:00")
            assert clocks["corrected_at"] is None
            observed.append(scenario["operation"])
        return result

    monkeypatch.setattr(replay.rollback, "rehearse", inspect)
    replay.replay(fixture)
    assert observed == ["ROLLBACK", "WITHDRAWAL"]


@pytest.mark.parametrize("change", [
    lambda value: value.update(source_schema_id=replay.COMMON_SCHEMA_ID),
    lambda value: value.update(common_translation=True),
    lambda value: value.update(common_translation=0),
    lambda value: value["predecessor"].update(sha256="sha256:" + "0" * 64),
    lambda value: value["successor"].update(record_ref="kfm:temporal-authority:synthetic-wrong"),
])
def test_receipt_tamper_fails_before_recovery(fixture, monkeypatch, change):
    mutate(fixture, "successor-receipt.json", change)
    monkeypatch.setattr(replay, "install_workspace", lambda *_: pytest.fail("invalid receipt reached recovery"))
    with pytest.raises(replay.ReplayError, match="SUCCESSOR_RECEIPT_BINDING_MISMATCH"):
        replay.replay(fixture)


def test_valid_but_changed_record_is_not_accepted_by_old_receipt(fixture):
    mutate(fixture, "successor.json", lambda value: value.update(authority_id="fixture:synthetic:other"))
    with pytest.raises(replay.ReplayError, match="SUCCESSOR_RECEIPT_BINDING_MISMATCH"):
        replay.replay(fixture)


def test_collapsed_clocks_and_revision_ids_fail_closed(fixture):
    original = (fixture / "successor.json").read_bytes()
    mutate(fixture, "successor.json", lambda value: value.update(times={key: "2026-08-08T00:10:00Z" for key in replay.CLOCKS}))
    with pytest.raises(replay.ReplayError, match="CLOCK_COVERAGE_INCOMPLETE"):
        replay.replay(fixture)
    (fixture / "successor.json").write_bytes(original)
    old = json.loads((fixture / "legacy.json").read_bytes())
    mutate(fixture, "successor.json", lambda value: value.update(envelope_id=old["envelope_id"]))
    with pytest.raises(replay.ReplayError, match="REVISION_ID_COLLAPSE"):
        replay.replay(fixture)


def test_common_correction_cannot_use_evidence_after_release_chronology(fixture):
    mutate(fixture, "common-v2.json", lambda value: value["time"].update(corrected_at="2026-08-08T00:12:00Z"))
    with pytest.raises(replay.ReplayError, match="COMMON_REPLAY_INVALID"):
        replay.replay(fixture)


def test_missing_withdrawal_reference_is_refused(fixture):
    mutate(fixture, "withdrawn.json", lambda value: value.pop("withdrawal_ref"))
    with pytest.raises(replay.ReplayError, match="EVIDENCE_REPLAY_INVALID"):
        replay.replay(fixture)


def test_non_synthetic_input_never_reaches_workspace_creation(fixture, monkeypatch):
    mutate(fixture, "case.json", lambda value: value.update(synthetic=False))
    monkeypatch.setattr(replay, "install_workspace", lambda *_: pytest.fail("non-synthetic input reached recovery"))
    with pytest.raises(replay.ReplayError, match="SYNTHETIC_FIXTURE_REQUIRED"):
        replay.replay(fixture)


def test_recovery_builder_refuses_an_existing_store_without_writes(fixture, tmp_path):
    root = tmp_path / "existing-store"
    root.mkdir()
    sentinel = root / "existing.json"
    sentinel.write_bytes(b'{"keep":"original"}\n')
    before = replay.tree_bytes(root)
    raw, _ = replay.load_fixture(fixture)
    with pytest.raises(replay.ReplayError, match="ISOLATED_EMPTY_WORKSPACE_REQUIRED"):
        replay.install_workspace(root, raw)
    assert replay.tree_bytes(root) == before


def test_future_release_or_correction_cannot_be_replayed_early(fixture):
    mutate(fixture, "case.json", lambda value: value.update(evaluated_at="2026-08-08T00:09:00Z"))
    with pytest.raises(replay.ReplayError, match="REPLAY_EVENT_AFTER_AS_OF"):
        replay.replay(fixture)


@pytest.mark.parametrize("instant", [123, "2026-08-08T00:20:00", "not-an-instant"])
def test_replay_requires_a_parseable_timezone_aware_instant(fixture, instant):
    mutate(fixture, "case.json", lambda value: value.update(evaluated_at=instant))
    with pytest.raises(replay.ReplayError, match="EXPLICIT_TIME_REQUIRED"):
        replay.replay(fixture)


def test_operator_readback_does_not_trust_helper_pass(fixture, monkeypatch):
    original = replay.rollback.rehearse

    def wrong_alias(root, scenario, *, apply=False):
        result = original(root, scenario, apply=apply)
        if apply:
            replay.rollback.write_json(root / "published/current.json", {"status": "ACTIVE", "release_id": replay.SUCCESSOR})
        return result

    monkeypatch.setattr(replay.rollback, "rehearse", wrong_alias)
    with pytest.raises(replay.ReplayError, match="RECOVERY_READBACK_MISMATCH"):
        replay.replay(fixture)


def test_correction_clock_readback_must_match_the_applied_record(fixture, monkeypatch):
    original = replay.rollback.rehearse

    def wrong_correction(root, scenario, *, apply=False):
        result = original(root, scenario, apply=apply)
        if apply:
            path = root / "corrections" / (scenario["correction"]["correction_id"] + ".json")
            mutate(root, path.relative_to(root), lambda value: value.update(decided_at="2099-01-01T00:00:00Z"))
        return result

    monkeypatch.setattr(replay.rollback, "rehearse", wrong_correction)
    with pytest.raises(replay.ReplayError, match="RECOVERY_READBACK_MISMATCH"):
        replay.replay(fixture)


def test_external_consumers_remain_unknown_with_explicit_removal_hold(fixture):
    report = replay.replay(fixture)
    inventory = report["consumer_inventory"]
    assert inventory["legacy_removal"] == "HOLD_EXTERNAL_INVENTORY_REQUIRED"
    assert {entry["scope"] for entry in inventory["external"]} == set(replay.EXTERNAL_SCOPES)
    assert all(entry["status"] == "NOT_INSPECTED" and entry["record_count"] is None and entry["sha256"] is None
               for entry in inventory["external"])
    assert len(inventory["first_party"]) == len(replay.CONSUMERS)


def test_duplicate_input_and_symlinked_fixture_are_refused(fixture):
    path = fixture / "case.json"
    original = path.read_bytes()
    path.write_bytes(original.replace(b'"synthetic": true', b'"synthetic": true, "synthetic": true'))
    with pytest.raises(replay.ReplayError, match="DUPLICATE_JSON_KEY"):
        replay.replay(fixture)
    path.write_bytes(original)
    target = fixture / "successor.json"
    target.unlink()
    target.symlink_to("legacy.json")
    with pytest.raises(ValueError, match="INPUT_SYMLINK_OR_SPECIAL"):
        replay.replay(fixture)


def test_cli_replays_deterministically_under_process_no_network_guard():
    env = os.environ.copy()
    env.update(KFM_NO_NETWORK="1", PYTHONDONTWRITEBYTECODE="1",
               PYTHONPATH=os.pathsep.join([str(replay.ROOT / "tools/ci/kfm_no_network"), str(replay.ROOT)]))
    source = "import sitecustomize,runpy,sys; assert sitecustomize.GUARD_ACTIVE; sys.argv=['temporal_replay','--fixtures']; runpy.run_path('tools/release/temporal_replay.py',run_name='__main__')"
    results = [subprocess.run([sys.executable, "-c", source], cwd=replay.ROOT, env=env,
                              capture_output=True, text=True, timeout=30) for _ in range(2)]
    assert all(result.returncode == 0 for result in results), results[0].stderr
    assert results[0].stdout == results[1].stdout
    assert json.loads(results[0].stdout)["outcome"] == "PASS"


def test_cli_reports_finite_fixture_failure(fixture, monkeypatch, capsys):
    mutate(fixture, "case.json", lambda value: value.update(synthetic=False))
    original = replay.load_fixture
    monkeypatch.setattr(replay, "load_fixture", lambda _: original(fixture))
    assert replay.main(["--fixtures"]) == 1
    assert json.loads(capsys.readouterr().out) == {
        "profile": replay.PROFILE, "outcome": "FAIL", "reason_code": "SYNTHETIC_FIXTURE_REQUIRED"}


def test_cli_unavailable_input_does_not_expose_raw_exception(monkeypatch, capsys):
    def unavailable(_):
        raise OSError("PRIVATE_PATH_SENTINEL")

    monkeypatch.setattr(replay, "load_fixture", unavailable)
    assert replay.main(["--fixtures"]) == 2
    output = capsys.readouterr()
    assert output.err == ""
    assert json.loads(output.out) == {
        "profile": replay.PROFILE, "outcome": "ERROR", "reason_code": "FIXTURE_REPLAY_UNAVAILABLE"}
