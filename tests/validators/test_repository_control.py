from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.repository_control.validate_repository_control import (
    compute_state_digest,
    evaluate,
    make_outcome,
    parse_context,
    validate_state_shape,
)

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "control_plane/repository_control_state.yaml"
FIXTURES = ROOT / "tests/fixtures/governance/repository_control"
STATE_SCHEMA = ROOT / "schemas/contracts/v1/governance/repository_control_state.schema.json"
CONTEXT_SCHEMA = ROOT / "schemas/contracts/v1/governance/repository_control_context.schema.json"
OUTCOME_SCHEMA = ROOT / "schemas/contracts/v1/governance/ci_outcome.schema.json"
FORMAT_CHECKER = FormatChecker()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def synthetic_context() -> dict:
    return load(FIXTURES / "context_expected_hold.json")


def confirmed_settings(state: dict, *, required_checks: list[str] | None = None) -> None:
    state["settings_snapshot"] = {
        "status": "CONFIRMED",
        "observed_at": "2026-07-26T12:00:00Z",
        "evidence_refs": ["fixture://settings/confirmed"],
        "required_pull_request": True,
        "required_approvals": 1,
        "dismiss_stale_reviews": True,
        "require_conversation_resolution": True,
        "required_status_checks": required_checks or ["repository-control"],
        "bypass_actors": [],
        "restrict_direct_push": True,
        "block_force_push": True,
        "block_deletion": True,
        "draft_merge_behavior": "BLOCKED_WHILE_DRAFT",
    }


def unverified_settings(state: dict, *, observed_at: str) -> None:
    """Give synthetic active-claim tests an explicit unverified platform state."""

    state["settings_snapshot"] = {
        "status": "NEEDS_VERIFICATION",
        "observed_at": observed_at,
        "evidence_refs": ["fixture://settings/unverified"],
        "required_pull_request": None,
        "required_approvals": None,
        "dismiss_stale_reviews": None,
        "require_conversation_resolution": None,
        "required_status_checks": [],
        "bypass_actors": [],
        "restrict_direct_push": None,
        "block_force_push": None,
        "block_deletion": None,
        "draft_merge_behavior": "NEEDS_VERIFICATION",
    }


def platform_evidence(
    context: dict,
    *,
    checks: list[dict] | None = None,
    is_draft: bool = False,
    approvals: int = 1,
    unresolved: int = 0,
    ready_transition_observed: bool = False,
    mergeability: str = "MERGEABLE",
) -> dict:
    return {
        "status": "CONFIRMED",
        "observed_at": context["now"],
        "pr_number": context["pr_number"],
        "head_sha": context["head_sha"],
        "evidence_refs": ["fixture://platform/confirmed"],
        "is_draft": is_draft,
        "ready_transition_observed": ready_transition_observed,
        "approval_count": approvals,
        "unresolved_conversation_count": unresolved,
        "status_checks": checks
        or [
            {
                "name": "repository-control",
                "outcome_class": "PASS",
                "evidence_refs": ["fixture://check/repository-control"],
            }
        ],
        "mergeability": mergeability,
    }


def active_state(
    context: dict,
    *,
    merge: bool = False,
    allowed_paths: list[str] | None = None,
) -> dict:
    state = load(STATE_PATH)
    unverified_settings(state, observed_at=context["now"])
    state["projection_status"] = "CONFIRMED"
    state_open_prs = list(context["open_pull_requests"])
    if context["pr_state"] in {"MERGED", "CLOSED_UNMERGED"}:
        state_open_prs = sorted(set(state_open_prs + [context["pr_number"]]))
    state["base"].update(
        current_main_sha=context["base_sha"],
        observed_at=context["now"],
        open_pull_requests=state_open_prs,
    )
    state["claim"] = {
        "claim_id": f"fixture-pr-{context['pr_number']}",
        "state": "ACTIVE",
        "active_branch": context["head_branch"],
        "active_review_prs": [context["pr_number"]],
        "allowed_paths": allowed_paths
        if allowed_paths is not None
        else list(context["changed_paths"]),
        "allowed_operations": list(context["requested_operations"]),
        "expires_at": "2026-08-01T00:00:00Z",
        "terminal_condition": "pull_request_reaches_terminal_state",
    }
    state["authorization"] = {
        "authorizing_actor": "fixture-owner",
        "evidence_refs": list(
            context.get("evidence_refs") or ["fixture://repository-control"]
        ),
        "issued_at": context["now"],
    }
    state["permissions"]["merge"] = merge
    state["settings_snapshot"]["observed_at"] = context["now"]
    state["state_digest"] = compute_state_digest(state)
    return state


def non_active_state(context: dict, claim_state: str = "HELD") -> dict:
    state = load(STATE_PATH)
    state["base"].update(
        current_main_sha=context["base_sha"],
        observed_at=context["now"],
        open_pull_requests=list(context["open_pull_requests"]),
    )
    state["claim"]["state"] = claim_state
    state["settings_snapshot"]["observed_at"] = context["now"]
    state["state_digest"] = compute_state_digest(state)
    return state


def schema_errors(schema_path: Path, instance: dict) -> list:
    return list(
        Draft202012Validator(
            load(schema_path),
            format_checker=FORMAT_CHECKER,
        ).iter_errors(instance)
    )


def test_tracked_state_is_schema_and_digest_valid() -> None:
    state = load(STATE_PATH)
    assert state["schema_version"] == "2.0.0"
    assert state["digest_spec"]["specification"] == "KFM-REPOSITORY-CONTROL-2"
    assert not validate_state_shape(state)
    assert compute_state_digest(state) == state["state_digest"]
    assert not schema_errors(STATE_SCHEMA, state)


def test_all_context_fixtures_match_context_schema() -> None:
    for path in sorted(FIXTURES.glob("context_*.json")):
        context = load(path)
        assert not schema_errors(CONTEXT_SCHEMA, context), path
        parse_context(context)


def test_digest_mutation_fails_closed() -> None:
    state = load(STATE_PATH)
    state["base"]["current_main_sha"] = "0" * 40
    assert [item.code for item in validate_state_shape(state)] == [
        "STATE_DIGEST_MISMATCH"
    ]


def test_held_projection_is_expected_readiness_hold() -> None:
    result = evaluate(load(STATE_PATH), synthetic_context())
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "EXPECTED_READINESS_HOLD",
        "CLAIM_HELD",
        True,
    )


def test_non_active_observed_snapshot_does_not_self_stale_after_head_moves() -> None:
    state = load(STATE_PATH)
    context = synthetic_context()
    context["base_sha"] = "f" * 40

    result = evaluate(state, context)

    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "EXPECTED_READINESS_HOLD",
        "CLAIM_HELD",
        True,
    )


def test_active_claim_remains_bound_to_its_observed_base_snapshot() -> None:
    context = synthetic_context()
    state = active_state(context)
    context["base_sha"] = "f" * 40

    result = evaluate(state, context)

    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "REGRESSION",
        "OBSERVED_BASE_SHA_MISMATCH",
        True,
    )


def test_active_scope_with_merge_false_is_hold() -> None:
    context = synthetic_context()
    result = evaluate(active_state(context), context)
    assert (result.outcome_class, result.reason_code) == (
        "EXPECTED_READINESS_HOLD",
        "MERGE_PERMISSION_FALSE",
    )


def test_path_outside_claim_is_regression() -> None:
    context = load(FIXTURES / "context_path_out_of_scope.json")
    result = evaluate(active_state(context, allowed_paths=["docs/**"]), context)
    assert (result.outcome_class, result.reason_code) == (
        "REGRESSION",
        "PATH_OUT_OF_SCOPE",
    )


def test_unsupported_wildcard_pattern_fails_state_validation() -> None:
    context = synthetic_context()
    state = active_state(context, allowed_paths=["docs/*"])
    state["state_digest"] = compute_state_digest(state)
    codes = {item.code for item in validate_state_shape(state)}
    assert "STATE_CLAIM_INVALID" in codes


def test_parent_path_segment_fails_context_validation() -> None:
    context = synthetic_context()
    context["changed_paths"] = ["docs/../policy/unsafe.rego"]
    result = evaluate(active_state(synthetic_context()), context)
    assert (result.outcome_class, result.reason_code) == (
        "REGRESSION",
        "CONTEXT_INVALID",
    )


def test_active_claim_requires_confirmed_projection() -> None:
    context = synthetic_context()
    state = active_state(context)
    state["projection_status"] = "PROPOSED"
    state["state_digest"] = compute_state_digest(state)
    assert "STATE_CLAIM_INVALID" in {
        item.code for item in validate_state_shape(state)
    }


def test_confirmed_settings_cannot_hide_unknown_fields() -> None:
    context = synthetic_context()
    state = active_state(context, merge=True)
    state["settings_snapshot"]["status"] = "CONFIRMED"
    state["state_digest"] = compute_state_digest(state)
    assert "STATE_SETTINGS_INVALID" in {
        item.code for item in validate_state_shape(state)
    }


def test_held_claim_identity_fields_are_strictly_typed() -> None:
    for field, value in (("claim_id", 123), ("active_branch", [])):
        state = load(STATE_PATH)
        state["claim"][field] = value
        state["state_digest"] = compute_state_digest(state)
        assert "STATE_CLAIM_INVALID" in {
            item.code for item in validate_state_shape(state)
        }


def test_merge_with_unverified_settings_is_unknown() -> None:
    context = synthetic_context()
    result = evaluate(active_state(context, merge=True), context)
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "UNKNOWN",
        "REPOSITORY_SETTINGS_UNVERIFIED",
        True,
    )


def test_merge_with_missing_platform_evidence_is_unknown() -> None:
    context = synthetic_context()
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert (result.outcome_class, result.reason_code) == (
        "UNKNOWN",
        "PLATFORM_MERGE_EVIDENCE_UNVERIFIED",
    )


def test_confirmed_scope_settings_and_platform_can_pass() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(context)
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "PASS",
        "DECLARED_SCOPE_AND_PLATFORM_VALID",
        False,
    )
    assert not schema_errors(STATE_SCHEMA, state)
    assert not schema_errors(CONTEXT_SCHEMA, context)


def test_platform_evidence_must_bind_to_pr_and_head() -> None:
    cases = (
        (
            "pr_number",
            10000,
            "PLATFORM_MERGE_EVIDENCE_PR_MISMATCH",
        ),
        (
            "head_sha",
            "2" * 40,
            "PLATFORM_MERGE_EVIDENCE_HEAD_MISMATCH",
        ),
    )
    for field, value, reason_code in cases:
        context = synthetic_context()
        context["platform_merge_evidence"] = platform_evidence(context)
        context["platform_merge_evidence"][field] = value
        state = active_state(context, merge=True)
        confirmed_settings(state)
        state["state_digest"] = compute_state_digest(state)
        result = evaluate(state, context)
        assert (result.outcome_class, result.reason_code) == (
            "REGRESSION",
            reason_code,
        )


def test_platform_evidence_must_match_context_snapshot_time() -> None:
    for observed_at in ("2000-01-01T00:00:00Z", "2030-01-01T00:00:00Z"):
        context = synthetic_context()
        context["platform_merge_evidence"] = platform_evidence(context)
        context["platform_merge_evidence"]["observed_at"] = observed_at
        state = active_state(context, merge=True)
        confirmed_settings(state)
        state["state_digest"] = compute_state_digest(state)
        result = evaluate(state, context)
        assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
            "UNKNOWN",
            "PLATFORM_MERGE_EVIDENCE_NOT_CURRENT",
            True,
        )


def test_required_approval_shortfall_is_hold() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(context, approvals=0)
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert result.reason_code == "REQUIRED_APPROVALS_MISSING"


def test_required_status_regression_remains_regression() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(
        context,
        checks=[
            {
                "name": "repository-control",
                "outcome_class": "REGRESSION",
                "evidence_refs": ["fixture://check/regression"],
            }
        ]
    )
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert (result.outcome_class, result.reason_code) == (
        "REGRESSION",
        "REQUIRED_STATUS_CHECK_REGRESSION",
    )


def test_ready_transition_requires_explicit_permission() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(
        context,
        ready_transition_observed=True
    )
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert result.reason_code == "READY_TRANSITION_PERMISSION_FALSE"


def test_ready_transition_is_checked_for_authorized_terminal_merge() -> None:
    context = synthetic_context()
    context.update(
        pr_state="MERGED",
        merge_commit_sha="3" * 40,
        open_pull_requests=[],
    )
    context["platform_merge_evidence"] = platform_evidence(
        context,
        ready_transition_observed=True,
    )
    state = active_state(context, merge=True)
    confirmed_settings(state)
    state["state_digest"] = compute_state_digest(state)
    result = evaluate(state, context)
    assert (result.outcome_class, result.reason_code) == (
        "REGRESSION",
        "READY_TRANSITION_PERMISSION_FALSE",
    )


def test_ready_transition_is_regression_for_every_non_active_claim() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(
        context,
        ready_transition_observed=True,
    )
    for claim_state in ("IDLE", "HELD", "TERMINAL"):
        result = evaluate(non_active_state(context, claim_state), context)
        assert (result.outcome_class, result.reason_code) == (
            "REGRESSION",
            "READY_TRANSITION_PERMISSION_FALSE",
        )


def test_ready_transition_requires_current_bound_platform_evidence() -> None:
    cases = (
        ("head_sha", "2" * 40, "REGRESSION", "PLATFORM_MERGE_EVIDENCE_HEAD_MISMATCH"),
        (
            "observed_at",
            "2000-01-01T00:00:00Z",
            "UNKNOWN",
            "PLATFORM_MERGE_EVIDENCE_NOT_CURRENT",
        ),
    )
    for field, value, outcome_class, reason_code in cases:
        context = synthetic_context()
        context["platform_merge_evidence"] = platform_evidence(
            context,
            ready_transition_observed=True,
        )
        context["platform_merge_evidence"][field] = value
        result = evaluate(non_active_state(context), context)
        assert (result.outcome_class, result.reason_code) == (
            outcome_class,
            reason_code,
        )


def test_unverified_ready_transition_evidence_does_not_create_incident_fact() -> None:
    context = synthetic_context()
    context["platform_merge_evidence"] = platform_evidence(
        context,
        ready_transition_observed=True,
    )
    context["platform_merge_evidence"].update(
        status="NEEDS_VERIFICATION",
        is_draft=None,
        ready_transition_observed=True,
        approval_count=None,
        unresolved_conversation_count=None,
        mergeability="UNKNOWN",
    )
    result = evaluate(non_active_state(context), context)
    assert (result.outcome_class, result.reason_code) == (
        "EXPECTED_READINESS_HOLD",
        "CLAIM_HELD",
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


def test_terminal_divergence_precedes_non_applicability() -> None:
    context = load(FIXTURES / "context_pr_1789_terminal_divergence.json")
    context.update(
        applicable=False,
        not_applicable_reason="classification cannot suppress terminal divergence",
    )
    result = evaluate(active_state(context), context)
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "REGRESSION",
        "TERMINAL_STATE_DIVERGENCE",
        True,
    )


def test_terminal_divergence_precedes_explicit_skip_for_tracked_pr() -> None:
    context = load(FIXTURES / "context_pr_1789_terminal_divergence.json")
    context["explicit_skip_reason"] = "skip cannot suppress tracked terminal divergence"
    result = evaluate(active_state(context), context)
    assert (result.outcome_class, result.reason_code) == (
        "REGRESSION",
        "TERMINAL_STATE_DIVERGENCE",
    )


def test_untracked_merged_pr_is_terminal_state_divergence() -> None:
    # Before the regression fix, applicable:false could suppress an untracked
    # merged PR. After the fix, all merged events are evaluated before
    # applicability, so TERMINAL_STATE_DIVERGENCE is always returned.
    context = load(FIXTURES / "context_pr_1789_terminal_divergence.json")
    state = active_state(context)
    context.update(
        pr_number=1790,
        applicable=False,
        not_applicable_reason="untracked sibling PR",
    )
    result = evaluate(state, context)
    assert (result.outcome_class, result.reason_code, result.blocks_merge) == (
        "REGRESSION",
        "TERMINAL_STATE_DIVERGENCE",
        True,
    )


def test_control_logic_change_requires_explicit_permission() -> None:
    paths = (
        "tools/validators/repository_control/validate_repository_control.py",
        "tests/validators/test_repository_control_incident_1790.py",
    )
    for path in paths:
        context = synthetic_context()
        context["changed_paths"] = [path]
        context["requested_operations"] = ["update", "modify_control_logic"]
        state = active_state(context)
        state["permissions"]["modify_control_logic"] = False
        state["state_digest"] = compute_state_digest(state)
        result = evaluate(state, context)
        assert result.reason_code == "CONTROL_LOGIC_CHANGE_NOT_AUTHORIZED"


def test_emitted_outcome_matches_schema_and_carries_context_evidence() -> None:
    context = synthetic_context()
    state = active_state(context)
    evaluation = evaluate(state, context)
    outcome = make_outcome(state, context, evaluation)
    assert not schema_errors(OUTCOME_SCHEMA, outcome)
    assert outcome["outcome_class"] == "EXPECTED_READINESS_HOLD"
    assert "fixture://repository-control/expected-hold" in outcome["evidence_refs"]
    assert outcome["state_digest"] == state["state_digest"]
    assert "findings" in outcome


def test_not_applicable_and_explicit_skip_are_distinct_and_skip_blocks() -> None:
    state = load(STATE_PATH)
    na_context = synthetic_context()
    na_context.update(applicable=False, not_applicable_reason="fixture scope")
    skip_context = synthetic_context()
    skip_context["explicit_skip_reason"] = "fixture precondition"
    not_applicable = evaluate(state, na_context)
    skipped = evaluate(state, skip_context)
    assert (not_applicable.outcome_class, not_applicable.blocks_merge) == (
        "NOT_APPLICABLE",
        False,
    )
    assert (skipped.outcome_class, skipped.blocks_merge) == (
        "SKIPPED_EXPLICIT",
        True,
    )
