"""Issue #3390: integrated synthetic multi-clock and source-role rehearsal."""
from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from tools.validators.evidence import rehearse_drought_multiclock as replay


@pytest.fixture
def fixtures(tmp_path):
    for name in replay.FILES:
        shutil.copyfile(replay.FIXTURES / name, tmp_path / name)
    return tmp_path


def rewrite(root, name, change, *, rebind=True):
    path = root / name
    value = json.loads(path.read_bytes())
    change(value)
    path.write_text(json.dumps(value, indent=2) + "\n")
    if rebind and name != "bindings.json":
        binding_path = root / "bindings.json"
        binding = json.loads(binding_path.read_bytes())
        binding["input_sha256"][name] = replay.digest(path.read_bytes())
        binding_path.write_text(json.dumps(binding, indent=2) + "\n")


def test_integrated_matrix_replays_without_writing_inputs(fixtures):
    before = {p.name: p.read_bytes() for p in fixtures.iterdir()}
    first = replay.rehearse(fixtures)
    assert first == replay.rehearse(fixtures)
    assert before == {p.name: p.read_bytes() for p in fixtures.iterdir()}
    assert first["outcome"] == "PASS"
    assert first["predecessor_bytes_unchanged"] is True
    assert len(first["cases"]) == 27
    assert len(first["family_matrix"]) == 7
    assert {c["outcome"] for c in first["cases"].values()} == {
        "OBSERVED", "DERIVED", "CONFLICT", "STALE", "ABSTAIN", "ERROR", "PASS", "DENY"}
    assert all(value is False for value in first["authority"].values())
    unsigned = {k: v for k, v in first.items() if k != "report_sha256"}
    assert replay.digest(replay.canonical(unsigned)) == first["report_sha256"]


def test_report_retains_source_support_clock_precision_and_unknowns():
    report = replay.rehearse()
    _, objects = replay.load_inputs(replay.FIXTURES)
    original = {s["source_family"]: s for s in objects["observations.json"]["sources"]}
    for row in report["family_matrix"]:
        assert row["source"] == original[row["source_family"]]
        assert row["source"]["observation_end"].endswith(".123456Z")
        assert row["uncertainty"] == {"status": "NOT_PROVIDED", "value": None}
        assert row["rights"] == "UNKNOWN"
        assert row["live_cadence"] == row["live_authority"] == "NOT_ASSESSED"
    assert report["correction"]["source"]["retrieval_time"].endswith("+00:00")
    assert report["correction"]["uncertainty"] == {"status": "NOT_PROVIDED", "value": None}
    assert report["forecast"]["times"]["corrected_at"] is None
    assert report["forecast"]["source_role"] == "FORECAST"
    assert report["forecast"]["support_type"] == "PREDICTION"
    assert report["forecast"]["uncertainty"]["confidence"] == "UNKNOWN"
    assert "QUANTITATIVE_UNCERTAINTY_PROPAGATION" in report["remaining"]


def test_join_keeps_each_native_tuple_and_conflict_without_winner():
    report = replay.rehearse()
    cases = report["cases"]
    assert len(cases["derived_context"]["tuple_evidence_refs"]) == 2
    assert cases["conflict_no_winner"]["outcome"] == "CONFLICT"
    assert cases["recent_publication_old_observation"]["reason_codes"] == ["OBSERVATION_STALE"]
    assert cases["missing_not_zero"]["outcome"] == "ABSTAIN"
    assert cases["superseded_not_current"]["outcome"] == "ABSTAIN"
    assert cases["corrected_observation"]["claim_digest"] != report["correction"]["prior_claim_digest"]
    assert cases["causal_attribution"]["reason_codes"] == ["SCHEMA_INVALID"]


@pytest.mark.parametrize("field,value,code", [
    ("supersedes_ref", "source:synthetic:wrong-predecessor", "CORRECTION_BINDING_INVALID"),
    ("payload_digest", None, "CORRECTION_BINDING_INVALID"),
    ("support_id", "support:synthetic:wrong", "CORRECTION_SUPPORT_OR_CLOCK_CHANGED"),
    ("observation_end", "2026-08-20T12:30:00Z", "CORRECTION_SUPPORT_OR_CLOCK_CHANGED"),
])
def test_correction_cannot_rewrite_clock_support_or_identity(fixtures, field, value, code):
    if field == "payload_digest":
        value = json.loads((fixtures / "observations.json").read_bytes())["sources"][1][field]
    rewrite(fixtures, "correction.json", lambda d: d.update({field: value}))
    with pytest.raises(replay.RehearsalError, match=code):
        replay.rehearse(fixtures)


def test_replaced_input_fails_old_binding_before_replay(fixtures):
    rewrite(fixtures, "observations.json", lambda d: d["sources"][0].update(method="synthetic replacement"), rebind=False)
    with pytest.raises(replay.RehearsalError, match="INPUT_BINDING_MISMATCH"):
        replay.rehearse(fixtures)


@pytest.mark.parametrize("change,code", [
    (lambda d: d.update(synthetic=1), "SYNTHETIC_FIXTURE_REQUIRED"),
    (lambda d: d.update(successor_relation="CORRECTS_OBSERVATIONS"), "FORECAST_IS_NOT_OBSERVATION_CORRECTION"),
    (lambda d: d.update(successor_evaluated_at="2026-08-19T18:00:00Z"), "SUCCESSOR_CLOCKS_INVALID"),
    (lambda d: d.update(source_corrected_at="2026-08-23T18:00:00Z"), "CORRECTION_CLOCKS_INVALID"),
    (lambda d: d.update(predecessor_evaluated_at="2026-08-17T18:00:00"), "EXPLICIT_TIME_REQUIRED"),
    (lambda d: next(iter(d["uncertainty_by_source"].values())).update(status="KNOWN", value=0), "UNCERTAINTY_OVERCLAIM"),
])
def test_binding_overclaims_or_future_events_fail(fixtures, change, code):
    rewrite(fixtures, "bindings.json", change)
    with pytest.raises(replay.RehearsalError, match=code):
        replay.rehearse(fixtures)


def test_duplicate_family_or_erased_evidence_cannot_pass(fixtures):
    rewrite(fixtures, "observations.json", lambda d: d["sources"].__setitem__(0, copy.deepcopy(d["sources"][1])))
    with pytest.raises(replay.RehearsalError, match="SEVEN_FAMILIES_REQUIRED"):
        replay.rehearse(fixtures)


def test_publication_clock_cannot_replace_observation_clock(fixtures):
    def collapse(d):
        d["sources"][0]["observation_end"] = d["sources"][0]["publication_time"]
    rewrite(fixtures, "observations.json", collapse)
    with pytest.raises(replay.RehearsalError, match="OBSERVATION_CLOCKS_COLLAPSED"):
        replay.rehearse(fixtures)


@pytest.mark.parametrize("field,value", [("source_role", "OBSERVATION"), ("support_type", "DIRECT_MEASUREMENT")])
def test_forecast_cannot_be_cast_as_observation_even_with_valid_identity(fixtures, field, value):
    def change(d):
        d[field] = value
        d.update(replay.forecast.assign_identity(d))
    rewrite(fixtures, "forecast.json", change)
    with pytest.raises(replay.RehearsalError, match="FORECAST_POLARITY_MISMATCH"):
        replay.rehearse(fixtures)


def test_forecast_unknown_uncertainty_cannot_be_upgraded(fixtures):
    def change(d):
        d["uncertainty"]["confidence"] = "HIGH"
        d.update(replay.forecast.assign_identity(d))
    rewrite(fixtures, "forecast.json", change)
    with pytest.raises(replay.RehearsalError, match="FORECAST_POLARITY_MISMATCH"):
        replay.rehearse(fixtures)


def test_forecast_cutoff_cannot_collapse_into_issue_time(fixtures):
    def change(d):
        d["times"]["source_data_cutoff_at"] = d["times"]["issued_at"]
        d.update(replay.forecast.assign_identity(d))
    rewrite(fixtures, "forecast.json", change)
    with pytest.raises(replay.RehearsalError, match="FORECAST_CLOCKS_COLLAPSED"):
        replay.rehearse(fixtures)


def test_validity_cannot_collapse_into_observation_time(fixtures):
    def change(d):
        d["sources"][0]["valid_start"] = d["sources"][0]["observation_start"]
    rewrite(fixtures, "observations.json", change)
    with pytest.raises(replay.RehearsalError, match="OBSERVATION_CLOCKS_COLLAPSED"):
        replay.rehearse(fixtures)


def test_tuple_digest_is_bound_before_validation():
    _, objects = replay.load_inputs(replay.FIXTURES)
    value = replay.candidate([objects["observations.json"]["sources"][0]], "2026-08-17T18:00:00Z")
    value["sources"][0]["payload_digest"] = "sha256:" + "a" * 64
    with pytest.raises(replay.RehearsalError, match="CLAIM_DIGEST_BINDING_MISMATCH"):
        replay.observation_case({}, "tampered", value, "OBSERVED")


@pytest.mark.parametrize("payload,code", [
    ('{"synthetic":true,"synthetic":false}', "DUPLICATE_JSON_KEY"),
    ('{"value":NaN}', "NONFINITE_JSON"),
    ('{"value":1e999}', "NONFINITE_JSON"),
])
def test_unsafe_json_is_refused(fixtures, payload, code):
    (fixtures / "bindings.json").write_text(payload)
    with pytest.raises(replay.RehearsalError, match=code):
        replay.rehearse(fixtures)


def test_symlinked_input_is_not_read(fixtures):
    path = fixtures / "forecast.json"
    path.unlink()
    path.symlink_to(replay.FIXTURES / "forecast.json")
    with pytest.raises(ValueError, match="INPUT_SYMLINK_OR_SPECIAL"):
        replay.rehearse(fixtures)


def test_all_pass_validator_cannot_make_negative_matrix_pass():
    forged = replay.forecast.ValidationResult("PASS", ())
    with patch.object(replay.forecast, "validate_payload", return_value=forged):
        with pytest.raises(replay.RehearsalError, match="FORECAST_POLARITY_MISMATCH"):
            replay.rehearse()


def test_cli_errors_are_finite_and_do_not_disclose_paths(capsys):
    for error, outcome, status in [(replay.RehearsalError("INPUT_BINDING_MISMATCH"), "FAIL", 1),
                                    (OSError("/private/credential/source"), "ERROR", 2)]:
        with patch.object(replay, "rehearse", side_effect=error):
            assert replay.main(["--fixtures"]) == status
        captured = capsys.readouterr()
        report = json.loads(captured.out)
        assert report["outcome"] == outcome
        assert "private" not in captured.out and captured.err == ""


def test_cli_runs_under_actual_process_network_guard():
    env = {**os.environ, "KFM_NO_NETWORK": "1", "PYTHONDONTWRITEBYTECODE": "1",
           "PYTHONPATH": os.pathsep.join([str(replay.ROOT / "tools/ci/kfm_no_network"), str(replay.ROOT)])}
    guard = subprocess.run([sys.executable, "-c", "import sitecustomize; assert sitecustomize.GUARD_ACTIVE"],
                           cwd=replay.ROOT, env=env, capture_output=True, timeout=30)
    assert guard.returncode == 0, guard.stderr.decode()
    command = [sys.executable, "tools/validators/evidence/rehearse_drought_multiclock.py", "--fixtures"]
    results = [subprocess.run(command, cwd=replay.ROOT, env=env, capture_output=True, timeout=30) for _ in range(2)]
    assert all(result.returncode == 0 and result.stderr == b"" for result in results)
    assert results[0].stdout == results[1].stdout
    assert json.loads(results[0].stdout)["outcome"] == "PASS"
