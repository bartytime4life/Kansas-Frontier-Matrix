"""Roads/Rail/Trade operator-status temporal checks stay held until their policy has rules.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): Operator/status temporal tests.

operator_status_temporal.rego is a default-deny scaffold. The hold fails with
OPERATOR_STATUS_TEMPORAL_NOT_IMPLEMENTED as soon as the policy gains rules.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
POLICY = "policy/domains/roads-rail-trade/operator_status_temporal.rego"
PACKAGE = "kfm.generated.policy.domains.roads_rail_trade.operator_status_temporal"


def _rules(relative: str) -> list[str]:
    lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def test_operator_status_policy_is_still_a_default_deny_scaffold() -> None:
    rules = _rules(POLICY)
    assert rules == [f"package {PACKAGE}", "default allow := false"], (
        "OPERATOR_STATUS_TEMPORAL_NOT_IMPLEMENTED: operator_status_temporal.rego now has rules. Replace this hold with tests "
        "that exercise each rule on allowed and denied inputs."
    )
