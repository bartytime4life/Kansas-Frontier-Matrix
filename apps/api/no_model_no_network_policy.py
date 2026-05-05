"""No-model, no-network policy evaluator and Focus mock.

This module is payload-only decision logic (no live model calls, no network I/O).
"""

FINITE_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def evaluate_policy(request: dict) -> dict:
    """Evaluate request under no-model, no-network policy gates."""
    if not isinstance(request, dict):
        return {"outcome": "ERROR", "reason": "INVALID_REQUEST"}

    question = str(request.get("question", "")).strip()
    if not question:
        return {"outcome": "ABSTAIN", "reason": "EMPTY_QUERY"}

    if request.get("network_required") is True:
        return {"outcome": "DENY", "reason": "NO_NETWORK_POLICY"}

    if request.get("model_required") is True:
        return {"outcome": "DENY", "reason": "NO_MODEL_POLICY"}

    if request.get("evidence_resolved") is not True:
        return {"outcome": "ABSTAIN", "reason": "MISSING_EVIDENCE"}

    return {"outcome": "ANSWER", "reason": "POLICY_ALLOW"}


def focus_mock(request: dict) -> dict:
    """Return one of ANSWER/ABSTAIN/DENY/ERROR only."""
    result = evaluate_policy(request)
    outcome = result.get("outcome", "ERROR")
    if outcome not in FINITE_OUTCOMES:
        return {"outcome": "ERROR", "reason": "NON_FINITE_OUTCOME"}
    return {"outcome": outcome, "reason": result.get("reason", "UNSPECIFIED")}
