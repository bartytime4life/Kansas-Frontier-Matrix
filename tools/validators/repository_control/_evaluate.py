"""Repository-control evaluation and registered CI outcome emission."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from tools.validators.repository_control._context import parse_context, scope_findings
from tools.validators.repository_control._model import (
    AUTHORITY_BOUNDARY,
    Evaluation,
    Finding,
    InputError,
    _digest,
    _sha,
    _time,
    compute_state_digest,
)
from tools.validators.repository_control._state import validate_state_shape


def _platform_evaluation(
    state: Mapping[str, Any],
    context: Mapping[str, Any],
) -> Evaluation | None:
    """Evaluate merge-readiness evidence after state/scope/permission checks pass."""

    settings = state["settings_snapshot"]
    if settings["status"] != "CONFIRMED":
        return Evaluation(
            "UNKNOWN",
            "REPOSITORY_SETTINGS_UNVERIFIED",
            "Scope matches, but repository settings remain unverified.",
            evidence_kind="READINESS_EVIDENCE",
        )

    platform = context.get("platform_merge_evidence")
    if not isinstance(platform, dict) or platform.get("status") != "CONFIRMED":
        return Evaluation(
            "UNKNOWN",
            "PLATFORM_MERGE_EVIDENCE_UNVERIFIED",
            "Merge permission is true, but current PR review/check/mergeability evidence is missing or unverified.",
            evidence_kind="READINESS_EVIDENCE",
        )

    if platform["is_draft"]:
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "PR_IS_DRAFT",
            "The pull request remains draft and is not eligible for merge evaluation.",
            evidence_kind="READINESS_EVIDENCE",
        )

    required_approvals = settings["required_approvals"]
    if platform["approval_count"] < required_approvals:
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "REQUIRED_APPROVALS_MISSING",
            "The observed approving-review count is below the verified repository requirement.",
            evidence_kind="READINESS_EVIDENCE",
        )

    if (
        settings["require_conversation_resolution"]
        and platform["unresolved_conversation_count"] > 0
    ):
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "UNRESOLVED_CONVERSATIONS",
            "Required conversation resolution is not complete.",
            evidence_kind="READINESS_EVIDENCE",
        )

    checks = {item["name"]: item for item in platform["status_checks"]}
    for required_name in settings["required_status_checks"]:
        observed = checks.get(required_name)
        if observed is None:
            return Evaluation(
                "EXPECTED_READINESS_HOLD",
                "REQUIRED_STATUS_CHECK_MISSING",
                f"Required status check is not present: {required_name}",
                evidence_kind="READINESS_EVIDENCE",
            )
        outcome = observed["outcome_class"]
        if outcome == "REGRESSION":
            return Evaluation(
                "REGRESSION",
                "REQUIRED_STATUS_CHECK_REGRESSION",
                f"Required status check reports REGRESSION: {required_name}",
                (
                    Finding(
                        "REQUIRED_STATUS_CHECK_REGRESSION",
                        f"{required_name} reported REGRESSION",
                    ),
                ),
            )
        if outcome == "UNKNOWN":
            return Evaluation(
                "UNKNOWN",
                "REQUIRED_STATUS_CHECK_UNKNOWN",
                f"Required status check cannot be classified safely: {required_name}",
                evidence_kind="READINESS_EVIDENCE",
            )
        if outcome != "PASS":
            return Evaluation(
                "EXPECTED_READINESS_HOLD",
                "REQUIRED_STATUS_CHECK_NOT_PASSING",
                f"Required status check is not a declared PASS: {required_name} ({outcome})",
                evidence_kind="READINESS_EVIDENCE",
            )

    if platform["mergeability"] == "CONFLICTING":
        return Evaluation(
            "REGRESSION",
            "PR_MERGE_CONFLICT",
            "The pull request is currently conflicting with the base branch.",
        )
    if platform["mergeability"] == "UNKNOWN":
        return Evaluation(
            "UNKNOWN",
            "PR_MERGEABILITY_UNKNOWN",
            "The pull request mergeability state is not known.",
            evidence_kind="READINESS_EVIDENCE",
        )

    return None


def evaluate(state: Mapping[str, Any], raw_context: Mapping[str, Any]) -> Evaluation:
    invalid = validate_state_shape(state)
    if invalid:
        return Evaluation(
            "REGRESSION",
            invalid[0].code,
            "Repository-control state is invalid.",
            tuple(invalid),
        )

    try:
        context = parse_context(raw_context)
    except InputError as exc:
        finding = Finding("CONTEXT_INVALID", str(exc))
        return Evaluation(
            "REGRESSION",
            finding.code,
            "Pull-request context is invalid.",
            (finding,),
        )

    if context["repository"] != state["repository"]:
        return Evaluation(
            "REGRESSION",
            "REPOSITORY_MISMATCH",
            "Context repository differs from state.",
        )
    if context["default_branch"] != state["base"]["default_branch"]:
        return Evaluation(
            "REGRESSION",
            "DEFAULT_BRANCH_MISMATCH",
            "Default branch differs from state.",
        )
    if context["applicable"] is False:
        return Evaluation(
            "NOT_APPLICABLE",
            "SCOPE_NOT_APPLICABLE",
            str(context["not_applicable_reason"]),
            blocks_merge=False,
            evidence_kind="NEITHER",
        )
    if context["explicit_skip_reason"] is not None:
        return Evaluation(
            "SKIPPED_EXPLICIT",
            "PRECONDITION_NOT_MET",
            str(context["explicit_skip_reason"]),
            blocks_merge=True,
            evidence_kind="NEITHER",
        )

    if state["projection_status"] == "SUPERSEDED":
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "STATE_PROJECTION_SUPERSEDED",
            "The repository-control projection is superseded and cannot authorize work.",
            evidence_kind="READINESS_EVIDENCE",
        )

    claim = state["claim"]
    permissions = state["permissions"]

    if context["pr_state"] == "MERGED":
        findings: list[Finding] = []
        if claim["state"] != "ACTIVE":
            findings.append(
                Finding("CLAIM_NOT_ACTIVE", "merged PR observed without an ACTIVE claim")
            )
        else:
            findings.extend(scope_findings(state, context))
        if not permissions["merge"]:
            findings.append(
                Finding(
                    "MERGE_PERMISSION_FALSE",
                    "merged PR observed while merge permission was false",
                )
            )
        if findings:
            return Evaluation(
                "REGRESSION",
                "TERMINAL_STATE_DIVERGENCE",
                "GitHub terminal state advanced beyond declared authority.",
                tuple(findings),
            )
        platform_result = _platform_evaluation(state, context)
        if platform_result is not None:
            return platform_result
        return Evaluation(
            "PASS",
            "TERMINAL_STATE_CONSISTENT",
            "Merged terminal state matches the active claim and confirmed platform evidence.",
            blocks_merge=False,
        )

    if context["pr_state"] == "CLOSED_UNMERGED":
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "PR_CLOSED_UNMERGED",
            "PR closed unmerged; reconcile before claim reuse.",
            blocks_merge=False,
            evidence_kind="READINESS_EVIDENCE",
        )
    if claim["state"] != "ACTIVE":
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            f"CLAIM_{claim['state']}",
            f"Claim is {claim['state']}; no PR is authorized.",
            evidence_kind="READINESS_EVIDENCE",
        )

    findings = scope_findings(state, context)
    if findings:
        return Evaluation(
            "REGRESSION",
            findings[0].code,
            "Scope or freshness validation failed.",
            tuple(findings),
        )
    if not permissions["merge"]:
        return Evaluation(
            "EXPECTED_READINESS_HOLD",
            "MERGE_PERMISSION_FALSE",
            "Scope passed, but merge permission is false.",
            evidence_kind="READINESS_EVIDENCE",
        )

    platform_result = _platform_evaluation(state, context)
    if platform_result is not None:
        return platform_result
    return Evaluation(
        "PASS",
        "DECLARED_SCOPE_AND_PLATFORM_VALID",
        "State, digest, scope, verified settings, and current platform evidence passed.",
        blocks_merge=False,
    )


def _outcome_time(state: Mapping[str, Any], context: Mapping[str, Any]) -> str:
    value = context.get("now")
    if isinstance(value, str):
        try:
            return _time(value, "context.now").isoformat().replace("+00:00", "Z")
        except InputError:
            pass
    base = state.get("base")
    if isinstance(base, dict) and isinstance(base.get("observed_at"), str):
        try:
            return _time(base["observed_at"], "base.observed_at").isoformat().replace(
                "+00:00", "Z"
            )
        except InputError:
            pass
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def make_outcome(
    state: Mapping[str, Any],
    context: Mapping[str, Any],
    evaluation: Evaluation,
    workflow: str = "repository-control",
    job: str = "evaluate",
) -> dict[str, Any]:
    refs: list[str] = []
    for section in (
        state.get("authorization"),
        state.get("settings_snapshot"),
        context,
        context.get("platform_merge_evidence"),
    ):
        if isinstance(section, dict) and isinstance(section.get("evidence_refs"), list):
            refs.extend(
                ref for ref in section["evidence_refs"] if isinstance(ref, str) and ref
            )
    platform = context.get("platform_merge_evidence")
    if isinstance(platform, dict):
        for check in platform.get("status_checks", []):
            if isinstance(check, dict) and isinstance(check.get("evidence_refs"), list):
                refs.extend(
                    ref for ref in check["evidence_refs"] if isinstance(ref, str) and ref
                )

    digest = state.get("state_digest")
    if not _digest(digest):
        digest = compute_state_digest(state)
    head_sha = context.get("head_sha") if _sha(context.get("head_sha")) else "0" * 40
    return {
        "schema_version": "1.0.0",
        "repository": str(
            context.get("repository") or state.get("repository") or "unknown/unknown"
        ),
        "head_sha": head_sha,
        "workflow": workflow,
        "job": job,
        "outcome_class": evaluation.outcome_class,
        "reason_code": evaluation.reason_code,
        "summary": evaluation.summary,
        "findings": [
            {"code": finding.code, "message": finding.message}
            for finding in evaluation.findings
        ],
        "evidence_refs": list(dict.fromkeys(refs))
        or ["repository-control-state:unresolved"],
        "authority_boundary": AUTHORITY_BOUNDARY,
        "blocks_merge": evaluation.blocks_merge,
        "evidence_kind": evaluation.evidence_kind,
        "generated_at": _outcome_time(state, context),
        "state_digest": digest,
    }
