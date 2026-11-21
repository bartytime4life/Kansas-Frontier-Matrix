"""Roads/Rail/Trade transport graph rollback stays held until graph projection exists.

Planned intent (docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md): Transport graph projection rollback tests.

project_to_graph.py holds with GRAPH_PROJECTION_NOT_IMPLEMENTED and
graph_projection_non_canonical.rego is a default-deny scaffold, so there is no
projection to roll back. Either changing fails this hold.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
POLICY = "policy/domains/roads-rail-trade/graph_projection_non_canonical.rego"
PACKAGE = "kfm.generated.policy.domains.roads_rail_trade.graph_projection_non_canonical"
STAGE = "pipelines/domains/roads-rail-trade/project_to_graph.py"
STAGE_REASON = "GRAPH_PROJECTION_NOT_IMPLEMENTED"


def _rules(relative: str) -> list[str]:
    lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def test_graph_projection_policy_is_still_a_default_deny_scaffold() -> None:
    rules = _rules(POLICY)
    assert rules == [f"package {PACKAGE}", "default allow := false"], (
        "TRANSPORT_GRAPH_ROLLBACK_NOT_IMPLEMENTED: graph_projection_non_canonical.rego now has rules. Replace this hold with tests "
        "that exercise each rule on allowed and denied inputs."
    )


def test_project_to_graph_stage_still_holds() -> None:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / STAGE)], capture_output=True, text=True, check=False, timeout=10,
    )
    assert completed.returncode == 2, "TRANSPORT_GRAPH_ROLLBACK_NOT_IMPLEMENTED: the stage no longer holds; write the real tests for it."
    assert json.loads(completed.stdout)["reason_code"] == STAGE_REASON
