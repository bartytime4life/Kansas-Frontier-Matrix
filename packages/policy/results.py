from __future__ import annotations

from dataclasses import dataclass
from typing import Any

FINITE_DECISIONS = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


@dataclass(frozen=True)
class DecisionResult:
    decision: str
    reasons: tuple[str, ...] = ()
    obligations: tuple[str, ...] = ()


def normalize_decision_result(raw_result: dict[str, Any]) -> DecisionResult:
    """Normalize engine-specific output into a finite decision result.

    Unknown or missing outcomes fail closed to ``ERROR``.
    """
    raw_decision = str(raw_result.get("decision", "ERROR")).upper()
    decision = raw_decision if raw_decision in FINITE_DECISIONS else "ERROR"

    reasons = tuple(
        str(reason)
        for reason in raw_result.get("reasons", [])
        if isinstance(reason, (str, int, float, bool))
    )
    obligations = tuple(
        str(obligation)
        for obligation in raw_result.get("obligations", [])
        if isinstance(obligation, (str, int, float, bool))
    )

    return DecisionResult(decision=decision, reasons=reasons, obligations=obligations)
