"""Prepared pull-request context validation and scope comparison."""

from __future__ import annotations

from typing import Any, Mapping

from tools.validators.repository_control._model import (
    CONTROL_PREFIXES,
    MERGEABILITY,
    OPERATIONS,
    OUTCOMES,
    PR_STATES,
    SETTINGS_STATUSES,
    Finding,
    InputError,
    _exact_keys,
    _safe_repo_path,
    _sha,
    _time,
    _unique_positive_ints,
    _unique_strings,
    path_matches,
)

CONTEXT_REQUIRED = {
    "repository",
    "default_branch",
    "base_sha",
    "head_sha",
    "head_branch",
    "pr_number",
    "pr_state",
    "merge_commit_sha",
    "changed_paths",
    "requested_operations",
    "open_pull_requests",
    "active_review_prs",
    "now",
}
CONTEXT_OPTIONAL = {
    "scenario_id",
    "evidence_refs",
    "applicable",
    "not_applicable_reason",
    "explicit_skip_reason",
    "platform_merge_evidence",
}
PLATFORM_KEYS = {
    "status",
    "observed_at",
    "pr_number",
    "head_sha",
    "evidence_refs",
    "is_draft",
    "ready_transition_observed",
    "approval_count",
    "unresolved_conversation_count",
    "status_checks",
    "mergeability",
}
STATUS_CHECK_KEYS = {"name", "outcome_class", "evidence_refs"}


def _platform(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise InputError("platform_merge_evidence must be an object or null")
    _exact_keys(value, PLATFORM_KEYS, "platform_merge_evidence")
    status = value.get("status")
    if status not in SETTINGS_STATUSES:
        raise InputError("platform_merge_evidence.status is unsupported")
    _time(value.get("observed_at"), "platform_merge_evidence.observed_at")
    pr_number = value.get("pr_number")
    if (
        not isinstance(pr_number, int)
        or isinstance(pr_number, bool)
        or pr_number <= 0
    ):
        raise InputError("platform_merge_evidence.pr_number must be positive")
    if not _sha(value.get("head_sha")):
        raise InputError("platform_merge_evidence.head_sha must be lowercase 40-hex")
    _unique_strings(
        value.get("evidence_refs"),
        "platform_merge_evidence.evidence_refs",
        allow_empty=False,
    )
    checks = value.get("status_checks")
    if not isinstance(checks, list):
        raise InputError("platform_merge_evidence.status_checks must be an array")
    seen_names: set[str] = set()
    normalized_checks: list[dict[str, Any]] = []
    for index, check in enumerate(checks):
        if not isinstance(check, dict):
            raise InputError(f"platform_merge_evidence.status_checks[{index}] must be an object")
        _exact_keys(check, STATUS_CHECK_KEYS, f"platform_merge_evidence.status_checks[{index}]")
        name = check.get("name")
        if not isinstance(name, str) or not name:
            raise InputError(f"platform_merge_evidence.status_checks[{index}].name must be non-empty")
        if name in seen_names:
            raise InputError("platform_merge_evidence.status_checks must have unique names")
        seen_names.add(name)
        if check.get("outcome_class") not in OUTCOMES:
            raise InputError(
                f"platform_merge_evidence.status_checks[{index}].outcome_class is unsupported"
            )
        _unique_strings(
            check.get("evidence_refs"),
            f"platform_merge_evidence.status_checks[{index}].evidence_refs",
            allow_empty=False,
        )
        normalized_checks.append(dict(check))

    for key in ("is_draft", "ready_transition_observed"):
        item = value.get(key)
        if item is not None and not isinstance(item, bool):
            raise InputError(f"platform_merge_evidence.{key} must be boolean or null")
    for key in ("approval_count", "unresolved_conversation_count"):
        item = value.get(key)
        if item is not None and (
            not isinstance(item, int) or isinstance(item, bool) or item < 0
        ):
            raise InputError(
                f"platform_merge_evidence.{key} must be a non-negative integer or null"
            )
    if value.get("mergeability") not in MERGEABILITY:
        raise InputError("platform_merge_evidence.mergeability is unsupported")
    if status == "CONFIRMED":
        incomplete = [
            key
            for key in (
                "is_draft",
                "ready_transition_observed",
                "approval_count",
                "unresolved_conversation_count",
            )
            if value.get(key) is None
        ]
        if value.get("mergeability") == "UNKNOWN":
            incomplete.append("mergeability")
        if incomplete:
            raise InputError(
                "CONFIRMED platform evidence has unresolved fields: " + ", ".join(incomplete)
            )
    result = dict(value)
    result["status_checks"] = normalized_checks
    return result


def parse_context(raw: Mapping[str, Any]) -> dict[str, Any]:
    missing = sorted(CONTEXT_REQUIRED - set(raw))
    extra = sorted(set(raw) - CONTEXT_REQUIRED - CONTEXT_OPTIONAL)
    if missing:
        raise InputError(f"context missing: {', '.join(missing)}")
    if extra:
        raise InputError(f"context has unsupported fields: {', '.join(extra)}")

    context = dict(raw)
    if not all(
        isinstance(context[key], str) and context[key]
        for key in ("repository", "default_branch", "head_branch")
    ):
        raise InputError("repository, default_branch, and head_branch must be non-empty")
    if context["repository"].count("/") != 1:
        raise InputError("repository must use owner/name")
    if not _sha(context["base_sha"]) or not _sha(context["head_sha"]):
        raise InputError("base_sha and head_sha must be lowercase 40-hex")
    if (
        not isinstance(context["pr_number"], int)
        or isinstance(context["pr_number"], bool)
        or context["pr_number"] <= 0
    ):
        raise InputError("pr_number must be positive")
    if context["pr_state"] not in PR_STATES:
        raise InputError("pr_state is unsupported")
    if context["pr_state"] == "MERGED" and not _sha(context["merge_commit_sha"]):
        raise InputError("MERGED context requires merge_commit_sha")
    if context["pr_state"] != "MERGED" and context["merge_commit_sha"] is not None:
        raise InputError("merge_commit_sha must be null unless MERGED")

    changed_paths = _unique_strings(context["changed_paths"], "changed_paths")
    for index, path in enumerate(changed_paths):
        _safe_repo_path(path, f"changed_paths[{index}]")
    operations = _unique_strings(context["requested_operations"], "requested_operations")
    if any(operation not in OPERATIONS for operation in operations):
        raise InputError("requested_operations contains an unsupported operation")
    context["open_pull_requests"] = _unique_positive_ints(
        context["open_pull_requests"], "open_pull_requests"
    )
    context["active_review_prs"] = _unique_positive_ints(
        context["active_review_prs"], "active_review_prs"
    )
    context["now"] = _time(context["now"], "context.now")
    context["changed_paths"] = changed_paths
    context["requested_operations"] = operations

    evidence_refs = context.get("evidence_refs", [])
    context["evidence_refs"] = _unique_strings(evidence_refs, "evidence_refs")
    applicable = context.get("applicable", True)
    if not isinstance(applicable, bool):
        raise InputError("applicable must be boolean")
    context["applicable"] = applicable
    not_applicable_reason = context.get("not_applicable_reason")
    if not_applicable_reason is not None and (
        not isinstance(not_applicable_reason, str) or not not_applicable_reason
    ):
        raise InputError("not_applicable_reason must be null or non-empty")
    explicit_skip_reason = context.get("explicit_skip_reason")
    if explicit_skip_reason is not None and (
        not isinstance(explicit_skip_reason, str) or not explicit_skip_reason
    ):
        raise InputError("explicit_skip_reason must be null or non-empty")
    if not applicable and not not_applicable_reason:
        raise InputError("applicable=false requires not_applicable_reason")
    if not applicable and explicit_skip_reason is not None:
        raise InputError("context cannot be both not applicable and explicitly skipped")
    context["not_applicable_reason"] = not_applicable_reason
    context["explicit_skip_reason"] = explicit_skip_reason
    context["platform_merge_evidence"] = _platform(
        context.get("platform_merge_evidence")
    )
    return context


def scope_findings(state: Mapping[str, Any], context: Mapping[str, Any]) -> list[Finding]:
    claim = state["claim"]
    findings: list[Finding] = []
    if context["base_sha"] != state["base"]["current_main_sha"]:
        findings.append(
            Finding("STATE_STALE_BASE_SHA", "base SHA differs from the pinned main SHA")
        )
    expected_open_prs = set(state["base"]["open_pull_requests"])
    if context["pr_state"] in {"MERGED", "CLOSED_UNMERGED"}:
        expected_open_prs.discard(context["pr_number"])
    if set(context["open_pull_requests"]) != expected_open_prs:
        findings.append(
            Finding(
                "STATE_STALE_OPEN_PR_SET",
                "observed open pull-request set differs from the pinned base snapshot",
            )
        )
    if context["head_branch"] != claim["active_branch"]:
        findings.append(
            Finding("BRANCH_OUT_OF_SCOPE", "head branch differs from the active claim")
        )
    if sorted(context["active_review_prs"]) != sorted(claim["active_review_prs"]):
        findings.append(
            Finding("ACTIVE_PR_SET_MISMATCH", "active PR set differs from the state")
        )
    if context["pr_number"] not in claim["active_review_prs"]:
        findings.append(Finding("PR_NOT_ACTIVE", "PR is absent from the active claim"))
    if any(
        not any(path_matches(path, pattern) for pattern in claim["allowed_paths"])
        for path in context["changed_paths"]
    ):
        findings.append(
            Finding("PATH_OUT_OF_SCOPE", "changed path is outside the allowed set")
        )
    if not set(context["requested_operations"]).issubset(claim["allowed_operations"]):
        findings.append(
            Finding(
                "OPERATION_OUT_OF_SCOPE",
                "requested operation is outside the allowed set",
            )
        )
    if claim["expires_at"] is not None and context["now"] >= _time(
        claim["expires_at"], "claim.expires_at"
    ):
        findings.append(Finding("CLAIM_EXPIRED", "active claim expired"))
    control_changed = any(
        any(path == prefix or path.startswith(prefix) for prefix in CONTROL_PREFIXES)
        for path in context["changed_paths"]
    )
    if control_changed and (
        "modify_control_logic" not in claim["allowed_operations"]
        or not state["permissions"]["modify_control_logic"]
    ):
        findings.append(
            Finding(
                "CONTROL_LOGIC_CHANGE_NOT_AUTHORIZED",
                "control logic changed without explicit permission",
            )
        )
    return findings
