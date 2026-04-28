from __future__ import annotations

from .results import DecisionResult


def apply_obligations(*, result: DecisionResult, supported: set[str]) -> tuple[str, ...]:
    """Return enforced obligations that are recognized by the caller.

    Unknown obligations are ignored so callers can explicitly choose what they
    support while retaining deterministic behavior.
    """
    return tuple(ob for ob in result.obligations if ob in supported)
