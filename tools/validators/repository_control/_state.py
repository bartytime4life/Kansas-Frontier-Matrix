"""Strict repository-control state validation."""

from __future__ import annotations

import re
from typing import Any, Mapping

from tools.validators.repository_control._model import (
    CANONICALIZATION_TEXT,
    CLAIM_STATES,
    DRAFT_MERGE_BEHAVIORS,
    OPERATIONS,
    PERMISSIONS,
    PROJECTION_STATUSES,
    SETTINGS_STATUSES,
    Finding,
    InputError,
    _digest,
    _exact_keys,
    _list,
    _obj,
    _safe_path_pattern,
    _sha,
    _time,
    _unique_positive_ints,
    _unique_strings,
    compute_state_digest,
)

TOP_LEVEL_KEYS = {
    "schema_version",
    "state_id",
    "repository",
    "projection_status",
    "base",
    "claim",
    "authorization",
    "permissions",
    "settings_snapshot",
    "authority_boundary",
    "digest_spec",
    "state_digest",
}
BASE_KEYS = {"default_branch", "current_main_sha", "observed_at", "open_pull_requests"}
CLAIM_KEYS = {
    "claim_id",
    "state",
    "active_branch",
    "active_review_prs",
    "allowed_paths",
    "allowed_operations",
    "expires_at",
    "terminal_condition",
}
AUTHORIZATION_KEYS = {"authorizing_actor", "evidence_refs", "issued_at"}
SETTINGS_KEYS = {
    "status",
    "observed_at",
    "evidence_refs",
    "required_pull_request",
    "required_approvals",
    "dismiss_stale_reviews",
    "require_conversation_resolution",
    "required_status_checks",
    "bypass_actors",
    "restrict_direct_push",
    "block_force_push",
    "block_deletion",
    "draft_merge_behavior",
}
DIGEST_KEYS = {"specification", "algorithm", "canonicalization", "excluded_fields"}
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
STATE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,127}$")


def _validate_base(state: Mapping[str, Any]) -> None:
    base = _obj(state, "base")
    _exact_keys(base, BASE_KEYS, "base")
    if not isinstance(base.get("default_branch"), str) or not base["default_branch"]:
        raise InputError("base.default_branch must be non-empty")
    if not _sha(base.get("current_main_sha")):
        raise InputError("base.current_main_sha must be lowercase 40-hex")
    _time(base.get("observed_at"), "base.observed_at")
    _unique_positive_ints(base.get("open_pull_requests"), "base.open_pull_requests")


def _validate_claim(state: Mapping[str, Any], projection_status: str) -> str:
    claim = _obj(state, "claim")
    _exact_keys(claim, CLAIM_KEYS, "claim")
    claim_state = claim.get("state")
    if claim_state not in CLAIM_STATES:
        raise InputError("claim.state is unsupported")

    prs = _unique_positive_ints(claim.get("active_review_prs"), "claim.active_review_prs")
    paths = _unique_strings(claim.get("allowed_paths"), "claim.allowed_paths")
    operations = _unique_strings(claim.get("allowed_operations"), "claim.allowed_operations")
    if any(operation not in OPERATIONS for operation in operations):
        raise InputError("claim.allowed_operations contains an unsupported operation")
    for index, pattern in enumerate(paths):
        _safe_path_pattern(pattern, f"claim.allowed_paths[{index}]")
    if claim.get("expires_at") is not None:
        _time(claim["expires_at"], "claim.expires_at")
    if not isinstance(claim.get("terminal_condition"), str) or not claim["terminal_condition"]:
        raise InputError("claim.terminal_condition must be non-empty")

    if claim_state == "ACTIVE":
        if projection_status != "CONFIRMED":
            raise InputError("ACTIVE claim requires projection_status CONFIRMED")
        if not isinstance(claim.get("claim_id"), str) or not claim["claim_id"]:
            raise InputError("ACTIVE claim requires claim_id")
        if not isinstance(claim.get("active_branch"), str) or not claim["active_branch"]:
            raise InputError("ACTIVE claim requires active_branch")
        if not prs or not paths or not operations:
            raise InputError("ACTIVE claim requires PRs, paths, and operations")
    return claim_state


def _validate_authorization(state: Mapping[str, Any], claim_state: str) -> None:
    authorization = _obj(state, "authorization")
    _exact_keys(authorization, AUTHORIZATION_KEYS, "authorization")
    refs = _unique_strings(
        authorization.get("evidence_refs"),
        "authorization.evidence_refs",
        allow_empty=False,
    )
    if authorization.get("issued_at") is not None:
        _time(authorization["issued_at"], "authorization.issued_at")
    actor = authorization.get("authorizing_actor")
    if actor is not None and (not isinstance(actor, str) or not actor):
        raise InputError("authorization.authorizing_actor must be null or non-empty")
    if claim_state == "ACTIVE" and not (actor and authorization.get("issued_at")):
        raise InputError("ACTIVE claim requires authorizing_actor and issued_at")
    if any(ref == "control_plane/repository_control_state.yaml" for ref in refs):
        raise InputError("authorization evidence must not cite the state file as its own authority")


def _validate_permissions(state: Mapping[str, Any], claim_state: str) -> None:
    permissions = _obj(state, "permissions")
    if set(permissions) != set(PERMISSIONS):
        raise InputError("permissions must contain only registered keys")
    if any(not isinstance(permissions[key], bool) for key in PERMISSIONS):
        raise InputError("permissions must contain boolean values")
    if claim_state in {"IDLE", "HELD", "TERMINAL"} and any(permissions.values()):
        raise InputError("non-ACTIVE claim must not grant permissions")


def _validate_settings(state: Mapping[str, Any]) -> None:
    settings = _obj(state, "settings_snapshot")
    _exact_keys(settings, SETTINGS_KEYS, "settings_snapshot")
    status = settings.get("status")
    if status not in SETTINGS_STATUSES:
        raise InputError("settings_snapshot.status is unsupported")
    _time(settings.get("observed_at"), "settings_snapshot.observed_at")
    _unique_strings(
        settings.get("evidence_refs"),
        "settings_snapshot.evidence_refs",
        allow_empty=False,
    )
    checks = _unique_strings(
        settings.get("required_status_checks"),
        "settings_snapshot.required_status_checks",
    )
    _unique_strings(settings.get("bypass_actors"), "settings_snapshot.bypass_actors")
    if settings.get("draft_merge_behavior") not in DRAFT_MERGE_BEHAVIORS:
        raise InputError("settings_snapshot.draft_merge_behavior is unsupported")

    nullable_booleans = (
        "required_pull_request",
        "dismiss_stale_reviews",
        "require_conversation_resolution",
        "restrict_direct_push",
        "block_force_push",
        "block_deletion",
    )
    for key in nullable_booleans:
        value = settings.get(key)
        if value is not None and not isinstance(value, bool):
            raise InputError(f"settings_snapshot.{key} must be boolean or null")
    approvals = settings.get("required_approvals")
    if approvals is not None and (
        not isinstance(approvals, int) or isinstance(approvals, bool) or approvals < 0
    ):
        raise InputError("settings_snapshot.required_approvals must be a non-negative integer or null")

    if status == "CONFIRMED":
        incomplete = [key for key in nullable_booleans if settings.get(key) is None]
        if approvals is None:
            incomplete.append("required_approvals")
        if settings.get("draft_merge_behavior") == "NEEDS_VERIFICATION":
            incomplete.append("draft_merge_behavior")
        if incomplete:
            raise InputError(
                "CONFIRMED settings snapshot has unresolved fields: " + ", ".join(incomplete)
            )
        if settings["required_pull_request"] is False and checks:
            raise InputError(
                "required_status_checks cannot be declared for PR enforcement when required_pull_request is false"
            )


def _validate_digest(state: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    digest_spec = state.get("digest_spec")
    if not isinstance(digest_spec, dict):
        return [Finding("STATE_DIGEST_SPEC_INVALID", "digest_spec must be an object")]
    try:
        _exact_keys(digest_spec, DIGEST_KEYS, "digest_spec")
    except InputError as exc:
        findings.append(Finding("STATE_DIGEST_SPEC_INVALID", str(exc)))
        return findings
    if (
        digest_spec.get("specification") != "KFM-REPOSITORY-CONTROL-1"
        or digest_spec.get("algorithm") != "sha256"
        or digest_spec.get("canonicalization") != CANONICALIZATION_TEXT
        or digest_spec.get("excluded_fields") != ["state_digest"]
    ):
        findings.append(
            Finding("STATE_DIGEST_SPEC_INVALID", "unsupported digest specification")
        )
        return findings
    digest = state.get("state_digest")
    if not _digest(digest):
        findings.append(
            Finding("STATE_DIGEST_FORMAT_INVALID", "state_digest must be lowercase 64-hex")
        )
    elif compute_state_digest(state) != digest:
        findings.append(Finding("STATE_DIGEST_MISMATCH", "canonical digest mismatch"))
    return findings


def validate_state_shape(state: Mapping[str, Any]) -> list[Finding]:
    """Return every deterministic structural failure without consulting the network."""

    findings: list[Finding] = []
    try:
        _exact_keys(state, TOP_LEVEL_KEYS, "state")
    except InputError as exc:
        return [Finding("STATE_TOP_LEVEL_INVALID", str(exc))]

    if state.get("schema_version") != "1.0.0":
        findings.append(
            Finding("STATE_SCHEMA_VERSION_UNSUPPORTED", "schema_version must be 1.0.0")
        )
    if not isinstance(state.get("state_id"), str) or not STATE_ID_RE.fullmatch(state["state_id"]):
        findings.append(Finding("STATE_ID_INVALID", "state_id does not match the registered grammar"))
    repository = state.get("repository")
    if not isinstance(repository, str) or not REPOSITORY_RE.fullmatch(repository):
        findings.append(Finding("STATE_REPOSITORY_INVALID", "repository must use owner/name"))
    projection_status = state.get("projection_status")
    if projection_status not in PROJECTION_STATUSES:
        findings.append(
            Finding("STATE_PROJECTION_STATUS_INVALID", "projection_status is unsupported")
        )

    claim_state: str | None = None
    validators = (
        ("STATE_BASE_INVALID", lambda: _validate_base(state)),
        (
            "STATE_CLAIM_INVALID",
            lambda: _validate_claim(state, projection_status),
        ),
    )
    for code, validator in validators:
        try:
            result = validator()
            if code == "STATE_CLAIM_INVALID":
                claim_state = result
        except InputError as exc:
            findings.append(Finding(code, str(exc)))

    if claim_state is not None:
        for code, validator in (
            ("STATE_AUTHORIZATION_INVALID", lambda: _validate_authorization(state, claim_state)),
            ("STATE_PERMISSIONS_INVALID", lambda: _validate_permissions(state, claim_state)),
        ):
            try:
                validator()
            except InputError as exc:
                findings.append(Finding(code, str(exc)))

    try:
        _validate_settings(state)
    except InputError as exc:
        findings.append(Finding("STATE_SETTINGS_INVALID", str(exc)))

    findings.extend(_validate_digest(state))
    if not isinstance(state.get("authority_boundary"), str) or not state["authority_boundary"]:
        findings.append(
            Finding("STATE_AUTHORITY_BOUNDARY_MISSING", "authority_boundary must be non-empty")
        )
    return findings
