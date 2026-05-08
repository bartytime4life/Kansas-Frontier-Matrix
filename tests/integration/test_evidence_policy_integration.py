from __future__ import annotations
import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")


import json
from pathlib import Path

from packages.evidence.evidence_ref_resolver import resolve_evidence_ref
from packages.policy import build_policy_input
from packages.policy.decision_engine import StaticDecisionEngine


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_REF_SCHEMA_PATH = ROOT / "schemas/contracts/v1/evidence/evidence_ref.schema.json"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_published_evidence_flows_to_answer_decision() -> None:
    evidence_result = resolve_evidence_ref(
        evidence_ref=_fixture("evidence_ref_published.json"),
        schema_path=EVIDENCE_REF_SCHEMA_PATH,
        expected_digest="sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    )

    policy_input = build_policy_input(
        request_id="req-integration-answer",
        payload={"claim_id": "kfm:claim:hydrology:huc12:102600080305"},
        release_state=evidence_result.release_state,
        evidence_renderable=evidence_result.render,
    )

    engine = StaticDecisionEngine(decision="ANSWER", reasons=["ALLOWED_PUBLIC_EVIDENCE"])
    decision = engine.evaluate(policy_input)

    assert evidence_result.render is True
    assert evidence_result.decision == "cite"
    assert decision.decision == "ANSWER"
    assert "EVIDENCE_NOT_RENDERABLE" not in decision.reasons


def test_raw_evidence_forces_fail_closed_abstain() -> None:
    evidence_result = resolve_evidence_ref(
        evidence_ref=_fixture("evidence_ref_raw.json"),
        schema_path=EVIDENCE_REF_SCHEMA_PATH,
    )

    policy_input = build_policy_input(
        request_id="req-integration-abstain",
        payload={"claim_id": "kfm:claim:hydrology:huc12:102600080305"},
        release_state=evidence_result.release_state,
        evidence_renderable=evidence_result.render,
    )

    engine = StaticDecisionEngine(decision="ANSWER", reasons=["WOULD_HAVE_ANSWERED"])
    decision = engine.evaluate(policy_input)

    assert evidence_result.render is False
    assert evidence_result.error_code == "EVREF_RELEASE_STATE_NOT_APPROVED"
    assert decision.decision == "ABSTAIN"
    assert "EVIDENCE_NOT_RENDERABLE" in decision.reasons


def test_unknown_engine_decision_normalizes_to_error() -> None:
    evidence_result = resolve_evidence_ref(
        evidence_ref=_fixture("evidence_ref_published.json"),
        schema_path=EVIDENCE_REF_SCHEMA_PATH,
    )

    policy_input = build_policy_input(
        request_id="req-integration-error",
        payload={"claim_id": "kfm:claim:hydrology:huc12:102600080305"},
        release_state=evidence_result.release_state,
        evidence_renderable=evidence_result.render,
    )

    engine = StaticDecisionEngine(decision="allow", reasons=["NON_FINITE_DECISION"])
    decision = engine.evaluate(policy_input)

    assert evidence_result.render is True
    assert decision.decision == "ERROR"
    assert "NON_FINITE_DECISION" in decision.reasons
