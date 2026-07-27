"""Repository-control evaluation and registered CI outcome emission."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from tools.validators.repository_control._context import _context, _scope_findings
from tools.validators.repository_control._model import (
    AUTHORITY_BOUNDARY, Evaluation, Finding, InputError, _sha,
)
from tools.validators.repository_control._state import validate_state_shape

def evaluate(state: Mapping[str, Any], raw_context: Mapping[str, Any]) -> Evaluation:
    invalid = validate_state_shape(state)
    if invalid:
        return Evaluation("REGRESSION", invalid[0].code, "Repository-control state is invalid.", tuple(invalid))
    if raw_context.get("applicable") is False:
        return Evaluation("NOT_APPLICABLE", "SCOPE_NOT_APPLICABLE", str(raw_context.get("not_applicable_reason") or "Check does not apply."), blocks_merge=False, evidence_kind="NEITHER")
    if raw_context.get("explicit_skip_reason") is not None:
        reason = raw_context["explicit_skip_reason"]
        if not isinstance(reason, str) or not reason:
            return Evaluation("REGRESSION", "SKIP_REASON_INVALID", "explicit_skip_reason must be non-empty.")
        return Evaluation("SKIPPED_EXPLICIT", "PRECONDITION_NOT_MET", reason, blocks_merge=False, evidence_kind="NEITHER")
    try:
        context = _context(raw_context)
    except InputError as exc:
        finding = Finding("CONTEXT_INVALID", str(exc))
        return Evaluation("REGRESSION", finding.code, "Pull-request context is invalid.", (finding,))
    if context["repository"] != state["repository"]:
        return Evaluation("REGRESSION", "REPOSITORY_MISMATCH", "Context repository differs from state.")
    if context["default_branch"] != state["base"]["default_branch"]:
        return Evaluation("REGRESSION", "DEFAULT_BRANCH_MISMATCH", "Default branch differs from state.")

    claim = state["claim"]
    permissions = state["permissions"]
    settings = state["settings_snapshot"]
    if context["pr_state"] == "MERGED":
        findings = [] if claim["state"] == "ACTIVE" else [Finding("CLAIM_NOT_ACTIVE", "merged PR observed without an ACTIVE claim")]
        if claim["state"] == "ACTIVE":
            findings.extend(_scope_findings(state, context))
        if not permissions["merge"]:
            findings.append(Finding("MERGE_PERMISSION_FALSE", "merged PR observed while merge permission was false"))
        if findings:
            return Evaluation("REGRESSION", "TERMINAL_STATE_DIVERGENCE", "GitHub terminal state advanced beyond declared authority.", tuple(findings))
        if settings["status"] != "CONFIRMED":
            return Evaluation("UNKNOWN", "REPOSITORY_SETTINGS_UNVERIFIED", "Terminal scope matches, but repository settings remain unverified.", evidence_kind="READINESS_EVIDENCE")
        return Evaluation("PASS", "TERMINAL_STATE_CONSISTENT", "Merged terminal state matches the active claim and verified settings.", blocks_merge=False)
    if context["pr_state"] == "CLOSED_UNMERGED":
        return Evaluation("EXPECTED_READINESS_HOLD", "PR_CLOSED_UNMERGED", "PR closed unmerged; reconcile before claim reuse.", blocks_merge=False, evidence_kind="READINESS_EVIDENCE")
    if claim["state"] != "ACTIVE":
        return Evaluation("EXPECTED_READINESS_HOLD", f"CLAIM_{claim['state']}", f"Claim is {claim['state']}; no PR is authorized.", evidence_kind="READINESS_EVIDENCE")
    findings = _scope_findings(state, context)
    if findings:
        return Evaluation("REGRESSION", findings[0].code, "Scope or freshness validation failed.", tuple(findings))
    if permissions["merge"] and settings["status"] != "CONFIRMED":
        return Evaluation("UNKNOWN", "REPOSITORY_SETTINGS_UNVERIFIED", "Scope matches, but repository settings remain unverified.", evidence_kind="READINESS_EVIDENCE")
    if not permissions["merge"]:
        return Evaluation("EXPECTED_READINESS_HOLD", "MERGE_PERMISSION_FALSE", "Scope passed, but merge permission is false.", evidence_kind="READINESS_EVIDENCE")
    return Evaluation("PASS", "DECLARED_SCOPE_VALID", "State, digest, scope, and settings evidence passed.", blocks_merge=False)


def make_outcome(state: Mapping[str, Any], context: Mapping[str, Any], evaluation: Evaluation, workflow: str = "repository-control", job: str = "evaluate") -> dict[str, Any]:
    refs: list[str] = []
    for section in (state.get("authorization"), state.get("settings_snapshot")):
        if isinstance(section, dict) and isinstance(section.get("evidence_refs"), list):
            refs.extend(ref for ref in section["evidence_refs"] if isinstance(ref, str) and ref)
    now = context.get("now") if isinstance(context.get("now"), str) else datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": "1.0.0",
        "repository": str(context.get("repository") or state.get("repository") or "unknown/unknown"),
        "head_sha": context.get("head_sha") if _sha(context.get("head_sha")) else "0" * 40,
        "workflow": workflow,
        "job": job,
        "outcome_class": evaluation.outcome_class,
        "reason_code": evaluation.reason_code,
        "summary": evaluation.summary,
        "evidence_refs": list(dict.fromkeys(refs)) or ["repository-control-state:unresolved"],
        "authority_boundary": AUTHORITY_BOUNDARY,
        "blocks_merge": evaluation.blocks_merge,
        "evidence_kind": evaluation.evidence_kind,
        "generated_at": now,
        "state_digest": str(state.get("state_digest") or "0" * 64),
    }


