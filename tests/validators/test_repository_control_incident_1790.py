from __future__ import annotations

import json
from pathlib import Path

from tools.validators.repository_control.validate_repository_control import (
    compute_state_digest,
    evaluate,
)

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "control_plane/repository_control_state.yaml"
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/governance/repository_control"
    / "context_pr_1790_terminal_divergence.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def held_state(context: dict) -> dict:
    state = load(STATE_PATH)
    state["base"].update(
        current_main_sha=context["base_sha"],
        observed_at=context["now"],
        open_pull_requests=[context["pr_number"]],
    )
    state["claim"] = {
        "claim_id": None,
        "state": "HELD",
        "active_branch": None,
        "active_review_prs": [],
        "allowed_paths": [],
        "allowed_operations": [],
        "expires_at": None,
        "terminal_condition": "settings_audit_and_explicit_reconciliation_required",
    }
    state["authorization"] = {
        "authorizing_actor": None,
        "evidence_refs": list(context["evidence_refs"]),
        "issued_at": None,
    }
    state["settings_snapshot"]["observed_at"] = context["now"]
    state["state_digest"] = compute_state_digest(state)
    return state


def test_pr_1790_is_terminal_state_divergence_from_held_projection() -> None:
    context = load(FIXTURE_PATH)
    result = evaluate(held_state(context), context)
    finding_codes = {item.code for item in result.findings}

    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "REGRESSION",
        "TERMINAL_STATE_DIVERGENCE",
        True,
    )
    assert {"CLAIM_NOT_ACTIVE", "MERGE_PERMISSION_FALSE"}.issubset(finding_codes)
