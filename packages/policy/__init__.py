"""Shared helpers for consuming policy decisions in runtime code.

This package is intentionally subordinate to repository-authoritative policy
assets under ``policy/``.
"""

from .decision_engine import DecisionEngine, StaticDecisionEngine
from .inputs import PolicyInput, build_policy_input
from .obligations import apply_obligations
from .results import DecisionResult, normalize_decision_result

__all__ = [
    "DecisionEngine",
    "DecisionResult",
    "PolicyInput",
    "StaticDecisionEngine",
    "apply_obligations",
    "build_policy_input",
    "normalize_decision_result",
]
