"""Roads/Rail/Trade route designation separation stays held until its policy has rules.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): Route membership and designation separation tests (negative-state rule applies).

route_designation_separation.rego is a default-deny scaffold. The hold fails
with ROUTE_DESIGNATION_SEPARATION_NOT_IMPLEMENTED as soon as the policy gains rules.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
POLICY = "policy/domains/roads-rail-trade/route_designation_separation.rego"
PACKAGE = "kfm.generated.policy.domains.roads_rail_trade.route_designation_separation"


def _rules(relative: str) -> list[str]:
    lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def test_route_designation_policy_is_still_a_default_deny_scaffold() -> None:
    rules = _rules(POLICY)
    assert rules == [f"package {PACKAGE}", "default allow := false"], (
        "ROUTE_DESIGNATION_SEPARATION_NOT_IMPLEMENTED: route_designation_separation.rego now has rules. Replace this hold with tests "
        "that exercise each rule on allowed and denied inputs."
    )
