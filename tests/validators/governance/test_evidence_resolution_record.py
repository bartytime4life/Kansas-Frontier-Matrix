import json
from pathlib import Path

from tools.validators.governance.validate_evidence_resolution_record import derive, expected_record_id

CASES = Path("fixtures/contracts/v1/governance/evidence_resolution_record/cases.json")


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
