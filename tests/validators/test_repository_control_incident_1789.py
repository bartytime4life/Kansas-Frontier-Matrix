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
    / "context_pr_1789_terminal_divergence.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def active_state(context: dict) -> dict:
    state = load(STATE_PATH)
    state["projection_status"] = "CONFIRMED"
    state["base"].update(
        current_main_sha=context["base_sha"],
        observed_at=context["now"],
        open_pull_requests=[context["pr_number"]],
    )
    state["claim"] = {
        "claim_id": f"fixture-pr-{context['pr_number']}",
        "state": "ACTIVE",
        "active_branch": context["head_branch"],
        "active_review_prs": [context["pr_number"]],
        "allowed_paths": list(context["changed_paths"]),
        "allowed_operations": list(context["requested_operations"]),
        "expires_at": "2026-08-01T00:00:00Z",
        "terminal_condition": "pull_request_reaches_terminal_state",
    }
    state["authorization"] = {
        "authorizing_actor": "fixture-owner",
        "evidence_refs": list(context["evidence_refs"]),
        "issued_at": context["now"],
    }
    state["permissions"]["modify_control_logic"] = False
    state["permissions"]["merge"] = False
    state["settings_snapshot"]["observed_at"] = context["now"]
    state["state_digest"] = compute_state_digest(state)
    return state


def test_tracked_projection_is_a_post_incident_held_checkpoint() -> None:
    state = load(STATE_PATH)
    assert state["base"]["current_main_sha"] == (
        "da3d73e08f79bc67f446ba1a98a7c77a630f9524"
    )
    assert state["base"]["open_pull_requests"] == []
    assert state["projection_status"] == "PROPOSED"
    assert state["claim"]["state"] == "HELD"
    assert state["permissions"]["merge"] is False
    assert "https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1791" in (
        state["authorization"]["evidence_refs"]
    )
    assert "https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1792" in (
        state["authorization"]["evidence_refs"]
    )


def test_pr_1789_is_terminal_state_divergence() -> None:
    context = load(FIXTURE_PATH)
    result = evaluate(active_state(context), context)
    finding_codes = {item.code for item in result.findings}

    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "REGRESSION",
        "TERMINAL_STATE_DIVERGENCE",
        True,
    )
    assert {
        "CONTROL_LOGIC_CHANGE_NOT_AUTHORIZED",
        "MERGE_PERMISSION_FALSE",
    }.issubset(finding_codes)
