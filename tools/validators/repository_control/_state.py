"""Strict repository-control state validation."""

from __future__ import annotations

from typing import Any, Mapping

from tools.validators.repository_control._model import (
    CLAIM_STATES, OPERATIONS, PERMISSIONS, Finding, InputError, _list, _obj, _sha, _time,
    compute_state_digest,
)

def validate_state_shape(state: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    required = {
        "schema_version", "state_id", "repository", "projection_status", "base", "claim",
        "authorization", "permissions", "settings_snapshot", "authority_boundary",
        "digest_spec", "state_digest",
    }
    missing = sorted(required - set(state))
    extra = sorted(set(state) - required)
    if missing:
        return [Finding("STATE_REQUIRED_FIELD_MISSING", ", ".join(missing))]
    if extra:
        findings.append(Finding("STATE_UNKNOWN_FIELD", ", ".join(extra)))
    if state.get("schema_version") != "1.0.0":
        findings.append(Finding("STATE_SCHEMA_VERSION_UNSUPPORTED", "schema_version must be 1.0.0"))
    if not isinstance(state.get("state_id"), str) or not state["state_id"]:
        findings.append(Finding("STATE_ID_INVALID", "state_id must be non-empty"))
    if not isinstance(state.get("repository"), str) or state["repository"].count("/") != 1:
        findings.append(Finding("STATE_REPOSITORY_INVALID", "repository must use owner/name"))

    try:
        base = _obj(state, "base")
        if not isinstance(base.get("default_branch"), str) or not base["default_branch"]:
            raise InputError("base.default_branch must be non-empty")
        if not _sha(base.get("current_main_sha")):
            raise InputError("base.current_main_sha must be lowercase 40-hex")
        _time(base.get("observed_at"), "base.observed_at")
        prs = _list(base, "open_pull_requests")
        if any(not isinstance(n, int) or isinstance(n, bool) or n <= 0 for n in prs) or len(prs) != len(set(prs)):
            raise InputError("base.open_pull_requests must contain unique positive integers")
    except InputError as exc:
        findings.append(Finding("STATE_BASE_INVALID", str(exc)))

    claim_state: Any = None
    try:
        claim = _obj(state, "claim")
        claim_state = claim.get("state")
        if claim_state not in CLAIM_STATES:
            raise InputError("claim.state is unsupported")
        prs = _list(claim, "active_review_prs")
        paths = _list(claim, "allowed_paths")
        ops = _list(claim, "allowed_operations")
        if any(not isinstance(n, int) or isinstance(n, bool) or n <= 0 for n in prs) or len(prs) != len(set(prs)):
            raise InputError("claim.active_review_prs must contain unique positive integers")
        if any(not isinstance(p, str) or not p for p in paths) or len(paths) != len(set(paths)):
            raise InputError("claim.allowed_paths must contain unique non-empty strings")
        if any(op not in OPERATIONS for op in ops) or len(ops) != len(set(ops)):
            raise InputError("claim.allowed_operations is invalid")
        if claim.get("expires_at") is not None:
            _time(claim["expires_at"], "claim.expires_at")
        if not isinstance(claim.get("terminal_condition"), str) or not claim["terminal_condition"]:
            raise InputError("claim.terminal_condition must be non-empty")
        if claim_state == "ACTIVE" and not all((claim.get("claim_id"), claim.get("active_branch"), prs, paths, ops)):
            raise InputError("ACTIVE claim requires id, branch, PRs, paths, and operations")
    except InputError as exc:
        findings.append(Finding("STATE_CLAIM_INVALID", str(exc)))

    try:
        auth = _obj(state, "authorization")
        refs = _list(auth, "evidence_refs")
        if not refs or any(not isinstance(ref, str) or not ref for ref in refs):
            raise InputError("authorization.evidence_refs must be non-empty")
        if auth.get("issued_at") is not None:
            _time(auth["issued_at"], "authorization.issued_at")
        if claim_state == "ACTIVE" and not (auth.get("authorizing_actor") and auth.get("issued_at")):
            raise InputError("ACTIVE claim requires authorizing_actor and issued_at")
    except InputError as exc:
        findings.append(Finding("STATE_AUTHORIZATION_INVALID", str(exc)))

    try:
        permissions = _obj(state, "permissions")
        if set(permissions) != set(PERMISSIONS) or any(not isinstance(permissions[k], bool) for k in PERMISSIONS):
            raise InputError("permissions must contain only registered boolean keys")
        if claim_state in {"IDLE", "HELD", "TERMINAL"} and any(permissions.values()):
            raise InputError("non-ACTIVE claim must not grant permissions")
    except InputError as exc:
        findings.append(Finding("STATE_PERMISSIONS_INVALID", str(exc)))

    try:
        settings = _obj(state, "settings_snapshot")
        if settings.get("status") not in {"CONFIRMED", "NEEDS_VERIFICATION"}:
            raise InputError("settings_snapshot.status is unsupported")
        _time(settings.get("observed_at"), "settings_snapshot.observed_at")
        if not _list(settings, "evidence_refs"):
            raise InputError("settings_snapshot.evidence_refs must be non-empty")
    except InputError as exc:
        findings.append(Finding("STATE_SETTINGS_INVALID", str(exc)))

    spec = state.get("digest_spec")
    if not isinstance(spec, dict) or spec.get("specification") != "KFM-REPOSITORY-CONTROL-1" or spec.get("algorithm") != "sha256" or spec.get("excluded_fields") != ["state_digest"]:
        findings.append(Finding("STATE_DIGEST_SPEC_INVALID", "unsupported digest specification"))
    digest = state.get("state_digest")
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        findings.append(Finding("STATE_DIGEST_FORMAT_INVALID", "state_digest must be lowercase 64-hex"))
    elif compute_state_digest(state) != digest:
        findings.append(Finding("STATE_DIGEST_MISMATCH", "canonical digest mismatch"))
    if not isinstance(state.get("authority_boundary"), str) or not state["authority_boundary"]:
        findings.append(Finding("STATE_AUTHORITY_BOUNDARY_MISSING", "authority_boundary must be non-empty"))
    return findings


