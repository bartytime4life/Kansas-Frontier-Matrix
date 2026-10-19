import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.governance.validate_evidence_resolution_record import derive, expected_record_id

ROOT = Path(__file__).resolve().parents[3]
CASES = Path("fixtures/contracts/v1/governance/evidence_resolution_record/cases.json")
VALIDATOR = ROOT / "tools/validators/governance/validate_evidence_resolution_record.py"
SCHEMA = Draft202012Validator(
    json.loads((ROOT / "schemas/contracts/v1/governance/evidence_resolution_record.schema.json").read_text(encoding="utf-8")),
    format_checker=FormatChecker(),
)


def _cases():
    return json.loads(CASES.read_text(encoding="utf-8"))["cases"]


def test_fixture_polarity():
    for case in _cases():
        decision, _ = derive(case["candidate"])
        assert decision == case["expected"], case["name"]


def test_record_id_is_deterministic():
    candidate = _cases()[0]["candidate"]
    assert candidate["record_id"] == expected_record_id(candidate)


def test_outcome_tamper_fails_closed():
    candidate = json.loads(json.dumps(_cases()[0]["candidate"]))
    candidate["outcome"] = "PARTIAL"
    candidate["record_id"] = expected_record_id(candidate)
    decision, findings = derive(candidate)
    assert decision == "ERROR"
    assert findings == ["OUTCOME_DRIFT"]


def test_nonresolved_bundle_is_denied():
    candidate = next(c["candidate"] for c in _cases() if c["name"] == "unresolved_with_bundle")
    decision, findings = derive(candidate)
    assert decision == "ERROR"
    assert "NONRESOLVED_BUNDLE_FORBIDDEN" in findings


def test_effect_overreach_is_denied():
    candidate = next(c["candidate"] for c in _cases() if c["name"] == "authority_overreach")
    decision, findings = derive(candidate)
    assert decision == "ERROR"
    assert "AUTHORITY_EFFECT_FORBIDDEN" in findings


def test_non_object_record_is_finite_error():
    for value in ([], None, 1, "record"):
        assert derive(value) == ("ERROR", ["RECORD_NOT_OBJECT"])


def test_unhashable_or_mixed_refs_are_finite_error():
    base = _cases()[0]["candidate"]
    mutations = (
        lambda c: c.__setitem__("requested_refs", [[1]]),
        lambda c: c.__setitem__("requested_refs", [1, "a"]),
        lambda c: c["resolutions"][0].__setitem__("evidence_ref", {}),
        lambda c: c["resolutions"][0].__setitem__("status", []),
    )
    for mutate in mutations:
        candidate = json.loads(json.dumps(base))
        mutate(candidate)
        decision, findings = derive(candidate)
        assert decision == "ERROR"
        assert findings


def _rebound(change, name="complete"):
    """A fixture with one change and a recomputed record_id, so only that change can fail it."""
    candidate = json.loads(json.dumps(next(c["candidate"] for c in _cases() if c["name"] == name)))
    change(candidate)
    candidate["record_id"] = expected_record_id(candidate)
    return candidate


def test_valid_fixtures_satisfy_the_closed_schema():
    for case in _cases():
        if case["expected"] != "ERROR":
            assert SCHEMA.is_valid(case["candidate"]), case["name"]


def test_fields_the_closed_schema_forbids_or_requires_are_refused():
    # The workflow runs no schema step, so these must fail in the validator itself.
    mutations = {
        "extra effect claims review": lambda c: c["effects"].update(review_approved=True),
        "extra top-level authority": lambda c: c.update(release_authorized=True),
        "extra row field": lambda c: c["resolutions"][0].update(published=True),
        "missing query_run_id": lambda c: c.pop("query_run_id"),
        "missing evaluated_at": lambda c: c.pop("evaluated_at"),
        "evaluated_at not a date-time": lambda c: c.update(evaluated_at="yesterday"),
        "missing reason_code": lambda c: c["resolutions"][0].pop("reason_code"),
        "lowercase reason_code": lambda c: c["resolutions"][0].update(reason_code="resolved"),
        "bundle_id not a string": lambda c: c["resolutions"][0].update(bundle_id=True),
        "integer refs": lambda c: (c.update(requested_refs=[1, 2]),
                                   c["resolutions"][0].update(evidence_ref=1), c["resolutions"][1].update(evidence_ref=2)),
        "empty query_run_id": lambda c: c.update(query_run_id=""),
    }
    for label, change in mutations.items():
        decision, findings = derive(_rebound(change))
        assert (decision, findings) == ("ERROR", ["SCHEMA_INVALID"]), label


def test_semantic_rules_name_their_defect():
    cases = {
        "RESOLUTIONS_NOT_SORTED_UNIQUE": lambda c: c["resolutions"].reverse(),
        "RESOLUTION_COVERAGE_MISMATCH": lambda c: c["resolutions"][1].update(evidence_ref="evidence:ks:c"),
        "RESOLVED_BUNDLE_REQUIRED": lambda c: c["resolutions"][0].update(bundle_digest="sha256:" + "A" * 64),
        "PROFILE_INVALID": lambda c: c.update(profile="kfm.governance.evidence-resolution-record.v2"),
    }
    for expected, change in cases.items():
        assert expected in derive(_rebound(change))[1], expected
    drifted = _rebound(lambda c: None)
    drifted["query_run_id"] = "kfm:query-run:other"
    assert derive(drifted) == ("ERROR", ["RECORD_ID_DRIFT"])


def test_mixed_statuses_derive_the_contract_outcome():
    def statuses(first, second, outcome):
        def change(c):
            for row, status in zip(c["resolutions"], (first, second)):
                row["status"] = status
                if status != "RESOLVED":
                    row.pop("bundle_id")
                    row.pop("bundle_digest")
                    row["reason_code"] = status
            c["outcome"] = outcome
        return _rebound(change)

    assert derive(statuses("RESOLVED", "DENIED", "PARTIAL")) == ("PARTIAL", [])
    assert derive(statuses("UNRESOLVED", "DENIED", "UNRESOLVED")) == ("UNRESOLVED", [])
    assert derive(statuses("DENIED", "DENIED", "DENIED")) == ("DENIED", [])


def _cli(*argv, cwd=None):
    result = subprocess.run([sys.executable, str(VALIDATOR), *map(str, argv)], cwd=cwd,
                            capture_output=True, text=True, check=False)
    return result.returncode, result.stdout


def test_cli_decisions_and_exit_codes(tmp_path):
    good = tmp_path / "good.json"
    good.write_text(json.dumps(_cases()[0]["candidate"]), encoding="utf-8")
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(_rebound(lambda c: c["effects"].update(review_approved=True))), encoding="utf-8")
    assert _cli(good) == (0, '{"decision": "COMPLETE", "findings": []}\n')
    assert _cli(bad) == (1, '{"decision": "ERROR", "findings": ["SCHEMA_INVALID"]}\n')
    unreadable = {
        "duplicate.json": '{"a": 1, "a": 2}',
        "nan.json": '{"a": NaN}',
        "truncated.json": '{"a": ',
        "deep.json": '{"a": ' + "[" * 100_000 + "]" * 100_000 + "}",
    }
    for name, content in unreadable.items():
        path = tmp_path / name
        path.write_text(content, encoding="utf-8")
        code, out = _cli(path)
        assert (code, json.loads(out)["findings"]) == (2, ["INPUT_ERROR"]), name
    assert _cli(tmp_path / "missing.json")[0] == 2


def test_cli_fixture_replay_does_not_depend_on_the_working_directory(tmp_path):
    code, out = _cli("--cases", cwd=tmp_path)
    assert code == 0
    assert len(out.splitlines()) == len(_cases())
