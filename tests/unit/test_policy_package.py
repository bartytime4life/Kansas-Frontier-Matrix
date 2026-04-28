from __future__ import annotations

from packages.policy import (
    StaticDecisionEngine,
    apply_obligations,
    build_policy_input,
    normalize_decision_result,
)


def test_normalize_decision_result_fail_closed_unknown_decision() -> None:
    result = normalize_decision_result({"decision": "allow", "reasons": ["X"]})

    assert result.decision == "ERROR"
    assert result.reasons == ("X",)


def test_static_decision_engine_abstains_when_evidence_not_renderable() -> None:
    policy_input = build_policy_input(
        request_id="req-1",
        payload={"request_id": "req-1"},
        evidence_renderable=False,
    )

    engine = StaticDecisionEngine(decision="ANSWER", reasons=["SAFE"])
    result = engine.evaluate(policy_input)

    assert result.decision == "ABSTAIN"
    assert "EVIDENCE_NOT_RENDERABLE" in result.reasons


def test_apply_obligations_returns_supported_subset() -> None:
    result = normalize_decision_result(
        {
            "decision": "DENY",
            "obligations": ["REQUIRE_REVIEW", "REDACT_SOURCE_COORDS"],
        }
    )

    enforced = apply_obligations(
        result=result,
        supported={"REQUIRE_REVIEW"},
    )

    assert enforced == ("REQUIRE_REVIEW",)
