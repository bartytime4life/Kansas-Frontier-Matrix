"""Roads/Rail/Trade public generalization receipts stay held until generalization exists.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): Public generalization receipt presence tests.

generalize_for_public.py holds with PUBLIC_GENERALIZATION_NOT_IMPLEMENTED and
public_generalization_required.rego is a default-deny scaffold, so no receipt can
exist. Either changing fails this hold, so receipt tests must land with them.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
POLICY = "policy/domains/roads-rail-trade/public_generalization_required.rego"
PACKAGE = "kfm.generated.policy.domains.roads_rail_trade.public_generalization_required"
STAGE = "pipelines/domains/roads-rail-trade/generalize_for_public.py"
STAGE_REASON = "PUBLIC_GENERALIZATION_NOT_IMPLEMENTED"


def _rules(relative: str) -> list[str]:
    lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def test_public_generalization_policy_is_still_a_default_deny_scaffold() -> None:
    rules = _rules(POLICY)
    assert rules == [f"package {PACKAGE}", "default allow := false"], (
        "PUBLIC_GENERALIZATION_RECEIPT_NOT_IMPLEMENTED: public_generalization_required.rego now has rules. Replace this hold with tests "
        "that exercise each rule on allowed and denied inputs."
    )


def test_generalize_for_public_stage_still_holds() -> None:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / STAGE)], capture_output=True, text=True, check=False, timeout=10,
    )
    assert completed.returncode == 2, "PUBLIC_GENERALIZATION_RECEIPT_NOT_IMPLEMENTED: the stage no longer holds; write the real tests for it."
    assert json.loads(completed.stdout)["reason_code"] == STAGE_REASON
