"""Roads/Rail/Trade OSM/GNIS legal-status denial stays held until its policy has rules.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): OSM/GNIS legal-status denial.

legal_status_deny.rego is a default-deny scaffold, so there is no rule to test
yet. The hold fails with LEGAL_STATUS_DENY_NOT_IMPLEMENTED as soon as the policy
gains rules.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
POLICY = "policy/domains/roads-rail-trade/legal_status_deny.rego"
PACKAGE = "kfm.generated.policy.domains.roads_rail_trade.legal_status_deny"


def _rules(relative: str) -> list[str]:
    lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def test_legal_status_policy_is_still_a_default_deny_scaffold() -> None:
    rules = _rules(POLICY)
    assert rules == [f"package {PACKAGE}", "default allow := false"], (
        "LEGAL_STATUS_DENY_NOT_IMPLEMENTED: legal_status_deny.rego now has rules. Replace this hold with tests "
        "that exercise each rule on allowed and denied inputs."
    )
