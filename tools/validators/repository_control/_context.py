"""Prepared pull-request context validation and scope comparison."""

from __future__ import annotations

import fnmatch
from typing import Any, Mapping

from tools.validators.repository_control._model import (
    CONTROL_PREFIXES, OPERATIONS, PR_STATES, Finding, InputError, _list, _sha, _time,
)

def _context(raw: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "repository", "default_branch", "base_sha", "head_sha", "head_branch", "pr_number",
        "pr_state", "merge_commit_sha", "changed_paths", "requested_operations",
        "active_review_prs", "now",
    }
    missing = sorted(required - set(raw))
    if missing:
        raise InputError(f"context missing: {', '.join(missing)}")
    context = dict(raw)
    if not all(isinstance(context[k], str) and context[k] for k in ("repository", "default_branch", "head_branch")):
        raise InputError("repository, default_branch, and head_branch must be non-empty")
    if not _sha(context["base_sha"]) or not _sha(context["head_sha"]):
        raise InputError("base_sha and head_sha must be lowercase 40-hex")
    if not isinstance(context["pr_number"], int) or isinstance(context["pr_number"], bool) or context["pr_number"] <= 0:
        raise InputError("pr_number must be positive")
    if context["pr_state"] not in PR_STATES:
        raise InputError("pr_state is unsupported")
    if context["pr_state"] == "MERGED" and not _sha(context["merge_commit_sha"]):
        raise InputError("MERGED context requires merge_commit_sha")
    if context["pr_state"] != "MERGED" and context["merge_commit_sha"] is not None:
        raise InputError("merge_commit_sha must be null unless MERGED")
    if any(not isinstance(p, str) or not p for p in context["changed_paths"]):
        raise InputError("changed_paths must contain non-empty strings")
    if any(op not in OPERATIONS for op in context["requested_operations"]):
        raise InputError("requested_operations is invalid")
    if any(not isinstance(n, int) or isinstance(n, bool) or n <= 0 for n in context["active_review_prs"]):
        raise InputError("active_review_prs is invalid")
    context["now"] = _time(context["now"], "context.now")
    return context


def _scope_findings(state: Mapping[str, Any], context: Mapping[str, Any]) -> list[Finding]:
    claim = state["claim"]
    findings: list[Finding] = []
    if context["base_sha"] != state["base"]["current_main_sha"]:
        findings.append(Finding("STATE_STALE_BASE_SHA", "base SHA differs from the pinned main SHA"))
    if context["head_branch"] != claim["active_branch"]:
        findings.append(Finding("BRANCH_OUT_OF_SCOPE", "head branch differs from the active claim"))
    if sorted(context["active_review_prs"]) != sorted(claim["active_review_prs"]):
        findings.append(Finding("ACTIVE_PR_SET_MISMATCH", "active PR set differs from the state"))
    if context["pr_number"] not in claim["active_review_prs"]:
        findings.append(Finding("PR_NOT_ACTIVE", "PR is absent from the active claim"))
    if any(not any(fnmatch.fnmatchcase(path, pattern) for pattern in claim["allowed_paths"]) for path in context["changed_paths"]):
        findings.append(Finding("PATH_OUT_OF_SCOPE", "changed path is outside the allowed set"))
    if not set(context["requested_operations"]).issubset(claim["allowed_operations"]):
        findings.append(Finding("OPERATION_OUT_OF_SCOPE", "requested operation is outside the allowed set"))
    if claim["expires_at"] is not None and context["now"] >= _time(claim["expires_at"], "claim.expires_at"):
        findings.append(Finding("CLAIM_EXPIRED", "active claim expired"))
    control_changed = any(any(path == prefix or path.startswith(prefix) for prefix in CONTROL_PREFIXES) for path in context["changed_paths"])
    if control_changed and ("modify_control_logic" not in claim["allowed_operations"] or not state["permissions"]["modify_control_logic"]):
        findings.append(Finding("CONTROL_LOGIC_CHANGE_NOT_AUTHORIZED", "control logic changed without explicit permission"))
    return findings


