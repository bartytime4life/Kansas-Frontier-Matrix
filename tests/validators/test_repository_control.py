from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.repository_control.validate_repository_control import (
    compute_state_digest,
    evaluate,
    make_outcome,
    validate_state_shape,
)

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "control_plane/repository_control_state.yaml"
FIXTURES = ROOT / "tests/fixtures/governance/repository_control"
STATE_SCHEMA = ROOT / "schemas/contracts/v1/governance/repository_control_state.schema.json"
OUTCOME_SCHEMA = ROOT / "schemas/contracts/v1/governance/ci_outcome.schema.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def synthetic_context() -> dict:
    return {
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "default_branch": "main",
        "base_sha": "9f4a7218e9f29592cce3d15fb6a2b43185ac3d82",
        "head_sha": "1" * 40,
        "head_branch": "agent/test-repository-control",
        "pr_number": 9999,
        "pr_state": "OPEN",
        "merge_commit_sha": None,
        "changed_paths": ["docs/example.md"],
        "requested_operations": ["update"],
        "active_review_prs": [9999],
        "now": "2026-07-26T12:00:00Z",
    }


def active_state(context: dict, *, merge: bool = False, allowed_paths: list[str] | None = None) -> dict:
    state = load(STATE_PATH)
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
        "allowed_paths": allowed_paths or list(context["changed_paths"]),
        "allowed_operations": list(context["requested_operations"]),
        "expires_at": "2026-08-01T00:00:00Z",
        "terminal_condition": "pull_request_reaches_terminal_state",
    }
    state["authorization"] = {
        "authorizing_actor": "fixture-owner",
        "evidence_refs": list(context.get("evidence_refs") or ["fixture://repository-control"]),
        "issued_at": context["now"],
    }
    state["permissions"]["merge"] = merge
    state["settings_snapshot"]["observed_at"] = context["now"]
    state["state_digest"] = compute_state_digest(state)
    return state


def test_tracked_state_is_schema_and_digest_valid() -> None:
    state = load(STATE_PATH)
    schema = load(STATE_SCHEMA)
    assert not validate_state_shape(state)
    assert compute_state_digest(state) == state["state_digest"]
    assert not list(Draft202012Validator(schema).iter_errors(state))


def test_digest_mutation_fails_closed() -> None:
    state = load(STATE_PATH)
    state["base"]["current_main_sha"] = "0" * 40
    assert [item.code for item in validate_state_shape(state)] == ["STATE_DIGEST_MISMATCH"]


def test_held_projection_is_expected_readiness_hold() -> None:
    result = evaluate(load(STATE_PATH), synthetic_context())
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "EXPECTED_READINESS_HOLD", "CLAIM_HELD", True,
    )


def test_active_scope_with_merge_false_is_hold() -> None:
    context = synthetic_context()
    result = evaluate(active_state(context), context)
    assert (result.outcome_class, result.reason_code) == (
        "EXPECTED_READINESS_HOLD", "MERGE_PERMISSION_FALSE",
    )


def test_path_outside_claim_is_regression() -> None:
    context = synthetic_context()
    context["changed_paths"] = ["policy/unauthorized.rego"]
    result = evaluate(active_state(context, allowed_paths=["docs/**"]), context)
    assert (result.outcome_class, result.reason_code) == ("REGRESSION", "PATH_OUT_OF_SCOPE")


def test_merge_with_unverified_settings_is_unknown() -> None:
    context = synthetic_context()
    result = evaluate(active_state(context, merge=True), context)
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "UNKNOWN", "REPOSITORY_SETTINGS_UNVERIFIED", True,
    )


def test_pr_1679_is_terminal_state_divergence() -> None:
    context = load(FIXTURES / "context_pr_1679_terminal_divergence.json")
    result = evaluate(active_state(context), context)
    assert result.reason_code == "TERMINAL_STATE_DIVERGENCE"
    assert "MERGE_PERMISSION_FALSE" in {item.code for item in result.findings}


def test_pr_1738_is_terminal_state_divergence() -> None:
    context = load(FIXTURES / "context_pr_1738_terminal_divergence.json")
    result = evaluate(active_state(context), context)
    assert result.reason_code == "TERMINAL_STATE_DIVERGENCE"
    assert "MERGE_PERMISSION_FALSE" in {item.code for item in result.findings}


def test_control_logic_change_requires_explicit_permission() -> None:
    context = synthetic_context()
    context["changed_paths"] = ["tools/validators/repository_control/validate_repository_control.py"]
    context["requested_operations"] = ["update", "modify_control_logic"]
    state = active_state(context)
    state["permissions"]["modify_control_logic"] = False
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert result.reason_code == "CONTROL_LOGIC_CHANGE_NOT_AUTHORIZED"


def test_emitted_outcome_matches_schema() -> None:
    context = synthetic_context()
    state = active_state(context)
    evaluation = evaluate(state, context)
    outcome = make_outcome(state, context, evaluation)
    assert not list(Draft202012Validator(load(OUTCOME_SCHEMA)).iter_errors(outcome))
    assert outcome["outcome_class"] == "EXPECTED_READINESS_HOLD"


def test_not_applicable_and_explicit_skip_are_distinct() -> None:
    state = load(STATE_PATH)
    na = evaluate(state, {"applicable": False, "not_applicable_reason": "fixture scope"})
    skipped = evaluate(state, {"explicit_skip_reason": "fixture precondition"})
    assert (na.outcome_class, skipped.outcome_class) == ("NOT_APPLICABLE", "SKIPPED_EXPLICIT")
