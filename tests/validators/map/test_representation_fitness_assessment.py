import json
from pathlib import Path

from tools.validators.map.validate_representation_fitness_assessment import evaluate, expected_id

CASES = Path("fixtures/contracts/v1/map/representation_fitness_assessment/cases.json")


def cases():
    return json.loads(CASES.read_text(encoding="utf-8"))["cases"]


def test_fixture_matrix():
    for case in cases():
        outcome, _ = evaluate(case["candidate"])
        assert outcome == case["expected"], case["name"]


def test_ids_are_deterministic():
    for case in cases():
        assert case["candidate"]["assessment_id"] == expected_id(case["candidate"])


def test_temporal_mismatch_holds():
    candidate = json.loads(json.dumps(cases()[0]["candidate"]))
    candidate["temporal"]["requested_at"] = "2026-08-08T12:00:00Z"
    candidate["outcome"] = "HOLD"
    candidate["assessment_id"] = expected_id(candidate)
    outcome, findings = evaluate(candidate)
    assert outcome == "HOLD"
    assert "TEMPORAL_SUPPORT_MISMATCH" in findings


def test_synthetic_without_reality_boundary_errors():
    candidate = json.loads(json.dumps(next(c["candidate"] for c in cases() if c["name"] == "context_synthetic")))
    candidate["reality_boundary_ref"] = None
    candidate["assessment_id"] = expected_id(candidate)
    outcome, findings = evaluate(candidate)
    assert outcome == "ERROR"
    assert "REALITY_BOUNDARY_REQUIRED" in findings


def test_authority_overreach_errors():
    candidate = json.loads(json.dumps(cases()[0]["candidate"]))
    candidate["effects"]["public_use_authorized"] = True
    candidate["assessment_id"] = expected_id(candidate)
    outcome, findings = evaluate(candidate)
    assert outcome == "ERROR"
    assert "AUTHORITY_EFFECT_FORBIDDEN" in findings
