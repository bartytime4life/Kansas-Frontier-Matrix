"""Tests for SourceProbeEnvelope profile anti-collapse rules."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/source_probe/validate_source_probe_envelope.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/source/source_probe_envelope"
SPEC = importlib.util.spec_from_file_location("kfm_source_probe_envelope", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(kind: str, name: str) -> dict[str, object]:
    value = json.loads((FIXTURES / kind / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_all_valid_profiles_pass() -> None:
    expected = {
        "nass_aggregate_changed.json": "NASS_AGGREGATE",
        "edna_detection_signal.json": "EDNA_MONITORING",
        "kgs_bedrock_changed.json": "KGS_GEOLOGY",
        "loc_deferred_hold.json": "LOC_CHRONICLING_AMERICA",
    }
    for name, profile in expected.items():
        path = FIXTURES / "valid" / name
        assert load("valid", name)["profile"] == profile
        assert MODULE.validate(path).ok, name


def test_invalid_profiles_fail_with_specific_codes() -> None:
    expected = {
        "nass_field_level.json": {"NASS_GEOGRAPHY_TOO_PRECISE", "NASS_FIELD_LEVEL_CLAIM_DENIED"},
        "edna_population_inference.json": {"EDNA_POPULATION_INFERENCE_DENIED"},
        "kgs_resource_inference.json": {"KGS_RESOURCE_INFERENCE_DENIED"},
        "loc_activated.json": {"LOC_ACTIVATION_DENIED", "LOC_PROFILE_MUST_HOLD"},
    }
    for name, codes in expected.items():
        result = MODULE.validate(FIXTURES / "invalid" / name)
        assert not result.ok, name
        assert codes.issubset({finding.code for finding in result.findings}), name


def test_loc_hold_is_valid_shape_but_not_activation() -> None:
    value = load("valid", "loc_deferred_hold.json")
    assert value["materiality"]["status"] == "HOLD"
    assert value["profile_data"]["source_activation"] is False
    assert value["governance"]["publication_allowed"] is False


def test_spec_hash_change_fails_closed(tmp_path: Path) -> None:
    value = load("valid", "nass_aggregate_changed.json")
    value["profile_data"]["row_count"] = 129
    target = tmp_path / "tampered.json"
    target.write_text(json.dumps(value), encoding="utf-8")
    result = MODULE.validate(target)
    assert MODULE.Finding("SPEC_HASH_MISMATCH", "/spec_hash") in result.findings


def rebound(name: str, change) -> dict[str, object]:
    """A valid fixture with one change and a recomputed spec_hash, so only that change can fail it."""
    value = load("valid", name)
    change(value)
    value["spec_hash"] = MODULE.canonical_hash(value)
    return value


def codes(tmp_path: Path, value: object, raw: str | None = None) -> set[str]:
    target = tmp_path / "candidate.json"
    target.write_text(raw if raw is not None else json.dumps(value), encoding="utf-8")
    return {finding.code for finding in MODULE.validate(target).findings}


def test_open_profile_data_values_of_any_type_are_findings_not_crashes(tmp_path: Path) -> None:
    # The schema leaves profile_data open, so these reach the semantic rules with unhashable values.
    cases = {
        "EDNA_CONTROLS_INVALID": ("edna_detection_signal.json", lambda v: v["profile_data"]["controls"].update(positive_control=["PASS"])),
        "EDNA_INTERPRETATION_INVALID": ("edna_detection_signal.json", lambda v: v["profile_data"].update(interpretation={"x": 1})),
        "KGS_GEOLOGY_KIND_INVALID": ("kgs_bedrock_changed.json", lambda v: v["profile_data"].update(geology_kind=["BEDROCK"])),
        "LOC_RIGHTS_CARE_NOT_HELD": ("loc_deferred_hold.json", lambda v: v["profile_data"].update(rights_state={})),
    }
    for code, (name, change) in cases.items():
        assert codes(tmp_path, rebound(name, change)) == {code}, code


def test_nass_rows_digest_must_be_lowercase_hex(tmp_path: Path) -> None:
    for digest in ("sha256:" + "Z" * 64, "sha256:" + "A" * 64, "sha256:" + "a" * 63, "SHA256:" + "a" * 64):
        value = rebound("nass_aggregate_changed.json", lambda v, d=digest: v["profile_data"].update(canonical_rows_sha256=d))
        assert codes(tmp_path, value) == {"NASS_CONTENT_DIGEST_MISSING"}, digest
    assert codes(tmp_path, rebound("nass_aggregate_changed.json", lambda v: None)) == set()


def test_edna_control_outcomes_decide_materiality(tmp_path: Path) -> None:
    def edna(controls: dict[str, str], status: str, **data: object) -> dict[str, object]:
        def change(v):
            v["profile_data"]["controls"] = controls
            v["profile_data"].update(data)
            v["materiality"]["status"] = status
        return rebound("edna_detection_signal.json", change)

    passing = {"positive_control": "PASS", "negative_control": "PASS"}
    failed = {"positive_control": "PASS", "negative_control": "FAIL"}
    unknown = {"positive_control": "UNKNOWN", "negative_control": "PASS"}
    assert codes(tmp_path, edna(failed, "HOLD")) == {"EDNA_FAILED_CONTROL_NOT_DENIED"}
    assert codes(tmp_path, edna(failed, "DENY")) == set()
    assert codes(tmp_path, edna(unknown, "CHANGED")) == {"EDNA_INCOMPLETE_EVIDENCE_NOT_HELD"}
    assert codes(tmp_path, edna(passing, "CHANGED", chain_of_custody_complete=False)) == {"EDNA_INCOMPLETE_EVIDENCE_NOT_HELD"}
    assert codes(tmp_path, edna(passing, "CHANGED", interpretation="INCONCLUSIVE")) == {"EDNA_INCOMPLETE_EVIDENCE_NOT_HELD"}
    assert codes(tmp_path, edna(unknown, "HOLD")) == set()
    # A failed control outranks incomplete evidence: DENY, not HOLD, is then the required status.
    assert codes(tmp_path, edna(failed, "DENY", chain_of_custody_complete=False)) == set()


def test_unreadable_inputs_are_named_findings(tmp_path: Path) -> None:
    valid = json.dumps(load("valid", "nass_aggregate_changed.json"))
    cases = {
        "JSON_DUPLICATE_KEY": '{"a": 1, "a": 2}',
        "JSON_NONFINITE_NUMBER": valid.replace('"row_count": 128', '"row_count": NaN'),
        "JSON_INVALID": '{"a": ',
        "ROOT_NOT_OBJECT": "[]",
    }
    for code, raw in cases.items():
        assert codes(tmp_path, None, raw) == {code}, code
    # Overflowing floats, excessive nesting and over-long integers used to escape as tracebacks.
    assert codes(tmp_path, None, '{"a": 1e400}') == {"JSON_NONFINITE_NUMBER"}
    assert codes(tmp_path, None, '{"a": ' + "[" * 100_000 + "]" * 100_000 + "}") == {"JSON_INVALID"}
    assert codes(tmp_path, None, '{"a": ' + "9" * 5000 + "}") == {"JSON_INVALID"}
    utf8 = tmp_path / "latin1.json"
    utf8.write_bytes(b'{"a": "\xff"}')
    assert {f.code for f in MODULE.validate(utf8).findings} == {"JSON_NOT_UTF8"}
    assert {f.code for f in MODULE.validate(tmp_path / "missing.json").findings} == {"INPUT_NOT_FILE"}
    link = tmp_path / "link.json"
    link.symlink_to(utf8)
    assert {f.code for f in MODULE.validate(link).findings} == {"INPUT_SYMLINK_DENIED"}


def test_cli_exit_codes(tmp_path: Path, capsys) -> None:
    good = tmp_path / "good.json"
    good.write_text(json.dumps(load("valid", "nass_aggregate_changed.json")), encoding="utf-8")
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(load("invalid", "nass_field_level.json")), encoding="utf-8")
    assert MODULE.run([str(good)]) == 0
    assert MODULE.run([str(good), str(bad)]) == 1
    assert MODULE.run(["--fixtures"]) == 0
    lines = [json.loads(line) for line in capsys.readouterr().out.splitlines()]
    # good alone, then good and bad in sorted order (bad.json first), then the eight fixtures.
    assert [line["outcome"] for line in lines[:3]] == ["PASS", "FAIL", "PASS"]
    assert len(lines) == 3 + 8


def test_fixture_replay_fails_when_a_fixture_has_the_wrong_polarity(tmp_path: Path, monkeypatch, capsys) -> None:
    for kind, source in (("valid", "valid/nass_aggregate_changed.json"), ("invalid", "valid/kgs_bedrock_changed.json")):
        (tmp_path / kind).mkdir()
        (tmp_path / kind / "case.json").write_bytes((FIXTURES / source).read_bytes())
    monkeypatch.setattr(MODULE, "FIXTURES", tmp_path)
    assert MODULE.fixture_profile() == 1, "a passing 'invalid' fixture must fail the replay"
    (tmp_path / "invalid" / "case.json").unlink()
    assert MODULE.fixture_profile() == 1, "an empty polarity directory must fail the replay"
    capsys.readouterr()
