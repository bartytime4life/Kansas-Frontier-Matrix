import json
from pathlib import Path

from packages.ingest.decision_engine import IngestDecisionEngine, canonical_json, sha256_canonical


FIXTURES = Path("packages/ingest/fixtures/decision_engine_cases.v1.json")


def test_decision_paths_and_artifacts():
    engine = IngestDecisionEngine()
    cases = json.loads(FIXTURES.read_text())
    for case in cases:
        out = engine.evaluate(case["input"], created_at="2026-01-01T00:00:00Z")
        assert out["IngestDecisionEnvelope.v1"]["decision"] == case["expected_decision"]
        assert out["IngestDecisionEnvelope.v1"]["deterministic"] is True
        assert out["DecisionValidatorReport.v1"]["object_type"] == "DecisionValidatorReport"
        if case["expected_decision"] == "INGEST":
            assert out["IngestIntent.v1"] is not None
            assert out["SkipDecisionRecord.v1"] is None
        elif case["expected_decision"] == "SKIP":
            assert out["SkipDecisionRecord.v1"] is not None


def test_canonical_hash_stability():
    data_a = {"b": 2, "a": 1}
    data_b = {"a": 1, "b": 2}
    assert canonical_json(data_a) == canonical_json(data_b)
    assert sha256_canonical(data_a) == sha256_canonical(data_b)


def test_conflicting_signal_fails_closed():
    engine = IngestDecisionEngine()
    payload = {
        "source_descriptor": {"source_id": "src.conflict"},
        "last_known_spec_hash": "sha256:same",
        "spec_hash_current": "sha256:same",
        "domain_policy_profile": {"rights_status": "open"},
        "materiality_ruleset": {"threshold": 1},
        "probe_metadata": {"summary_stats": {"delta": 10}},
    }
    out = engine.evaluate(payload, created_at="2026-01-01T00:00:00Z")
    assert out["DecisionValidatorReport.v1"]["valid"] is False
    assert "conflicting_signals" in out["DecisionValidatorReport.v1"]["errors"]
    assert out["IngestDecisionEnvelope.v1"]["decision"] == "ERROR"
