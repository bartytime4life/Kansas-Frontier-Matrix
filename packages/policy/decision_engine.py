from __future__ import annotations

from typing import Protocol

from .inputs import PolicyInput
from .results import DecisionResult, normalize_decision_result


class DecisionEngine(Protocol):
    """Protocol for policy evaluators used by runtime consumers."""

    def evaluate(self, policy_input: PolicyInput) -> DecisionResult:
        ...


class StaticDecisionEngine:
    """Deterministic adapter useful for local wiring and tests.

    This does not define policy law. It only adapts predeclared outcomes.
    """

    def __init__(self, *, decision: str, reasons: list[str] | None = None, obligations: list[str] | None = None) -> None:
        self._raw_result = {
            "decision": decision,
            "reasons": reasons or [],
            "obligations": obligations or [],
        }

    def evaluate(self, policy_input: PolicyInput) -> DecisionResult:
        raw_result = dict(self._raw_result)

        if not policy_input.evidence_renderable and raw_result.get("decision") == "ANSWER":
            raw_result["decision"] = "ABSTAIN"
            raw_result.setdefault("reasons", [])
            raw_result["reasons"] = [*raw_result["reasons"], "EVIDENCE_NOT_RENDERABLE"]

        return normalize_decision_result(raw_result)

    def as_dict(self) -> dict[str, object]:
        return dict(self._raw_result)
