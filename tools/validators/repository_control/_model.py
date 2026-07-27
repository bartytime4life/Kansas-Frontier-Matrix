"""Shared types and deterministic state helpers for repository-control validation."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

OUTCOMES = {
    "PASS",
    "EXPECTED_READINESS_HOLD",
    "REGRESSION",
    "NOT_APPLICABLE",
    "SKIPPED_EXPLICIT",
    "UNKNOWN",
}
CLAIM_STATES = {"IDLE", "ACTIVE", "HELD", "TERMINAL"}
PR_STATES = {"OPEN", "CLOSED_UNMERGED", "MERGED"}
OPERATIONS = {
    "create",
    "update",
    "delete",
    "rename",
    "workflow",
    "issue_only",
    "modify_control_logic",
}
PERMISSIONS = (
    "modify_control_logic",
    "ready_transition",
    "rebase",
    "force_push",
    "merge",
    "source_activation",
    "proof_construction",
    "release",
    "deployment",
    "publication",
)
SETTINGS_STATUSES = {"CONFIRMED", "NEEDS_VERIFICATION"}
DRAFT_MERGE_BEHAVIORS = {
    "BLOCKED_WHILE_DRAFT",
    "ALLOWED_WHILE_DRAFT",
    "NEEDS_VERIFICATION",
}
MERGEABILITY = {"MERGEABLE", "CONFLICTING", "UNKNOWN"}
PROJECTION_STATUSES = {"PROPOSED", "CONFIRMED", "SUPERSEDED"}
CANONICALIZATION_TEXT = (
    "Recursively sort object keys lexicographically, preserve array order, encode as UTF-8 compact JSON "
    "with no insignificant whitespace, and omit only the top-level state_digest field."
)
CONTROL_PREFIXES = (
    "control_plane/repository_control_state.",
    "contracts/governance/repository_control_state.",
    "schemas/contracts/v1/governance/repository_control_state.",
    "schemas/contracts/v1/governance/repository_control_context.",
    "schemas/contracts/v1/governance/ci_outcome.",
    "tools/validators/repository_control/",
    "tests/validators/test_repository_control.py",
    "tests/fixtures/governance/repository_control/",
    ".github/workflows/repository-control.",
)
AUTHORITY_BOUNDARY = (
    "Bounded executable readiness evidence only; this evaluator does not grant authority, "
    "prove GitHub settings, submit review, merge, activate sources, construct proof, "
    "release, deploy, or publish."
)


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


@dataclass(frozen=True)
class Evaluation:
    outcome_class: str
    reason_code: str
    summary: str
    findings: tuple[Finding, ...] = ()
    blocks_merge: bool = True
    evidence_kind: str = "EXECUTABLE_PROOF"


class InputError(ValueError):
    """Raised when a state or prepared context is not structurally usable."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InputError(f"cannot parse {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise InputError(f"{path}: root must be an object")
    return value


def canonical_bytes(value: Mapping[str, Any]) -> bytes:
    data = copy.deepcopy(dict(value))
    data.pop("state_digest", None)
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def compute_state_digest(state: Mapping[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(state)).hexdigest()


def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise InputError(f"{field} must be an RFC 3339 timestamp")
    text = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise InputError(f"{field} must be an RFC 3339 timestamp") from exc
    if parsed.tzinfo is None:
        raise InputError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def _sha(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(c in "0123456789abcdef" for c in value)
    )


def _digest(value: Any) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


def _obj(parent: Mapping[str, Any], key: str) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        raise InputError(f"{key} must be an object")
    return value


def _list(parent: Mapping[str, Any], key: str) -> list[Any]:
    value = parent.get(key)
    if not isinstance(value, list):
        raise InputError(f"{key} must be an array")
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], field: str) -> None:
    missing = sorted(expected - set(value))
    extra = sorted(set(value) - expected)
    if missing:
        raise InputError(f"{field} missing keys: {', '.join(missing)}")
    if extra:
        raise InputError(f"{field} has unsupported keys: {', '.join(extra)}")


def _unique_strings(values: Any, field: str, *, allow_empty: bool = True) -> list[str]:
    if not isinstance(values, list):
        raise InputError(f"{field} must be an array")
    if not allow_empty and not values:
        raise InputError(f"{field} must be non-empty")
    if any(not isinstance(value, str) or not value for value in values):
        raise InputError(f"{field} must contain non-empty strings")
    if len(values) != len(set(values)):
        raise InputError(f"{field} must not contain duplicates")
    return list(values)


def _unique_positive_ints(values: Any, field: str) -> list[int]:
    if not isinstance(values, list):
        raise InputError(f"{field} must be an array")
    if any(
        not isinstance(value, int) or isinstance(value, bool) or value <= 0
        for value in values
    ):
        raise InputError(f"{field} must contain positive integers")
    if len(values) != len(set(values)):
        raise InputError(f"{field} must not contain duplicates")
    return list(values)


def _safe_repo_path(value: Any, field: str) -> str:
    """Validate a repository-relative POSIX file path without normalizing it."""

    if not isinstance(value, str) or not value:
        raise InputError(f"{field} must be a non-empty repository-relative path")
    if value.startswith("/") or value.endswith("/") or "\\" in value or "//" in value:
        raise InputError(f"{field} must be a normalized repository-relative POSIX path")
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise InputError(f"{field} must not contain control characters")
    segments = value.split("/")
    if any(segment in {"", ".", ".."} for segment in segments):
        raise InputError(f"{field} must not contain empty, dot, or parent segments")
    if any(character in value for character in "*?["):
        raise InputError(f"{field} must not contain wildcard characters")
    return value


def _safe_path_pattern(value: Any, field: str) -> str:
    """Accept only exact paths or an explicit trailing ``/**`` recursive prefix."""

    if not isinstance(value, str) or not value:
        raise InputError(f"{field} must be a non-empty path pattern")
    if value.endswith("/**"):
        base = value[:-3]
        _safe_repo_path(base, field)
        return value
    if any(character in value for character in "*?["):
        raise InputError(
            f"{field} supports only exact paths or a trailing '/**' recursive prefix"
        )
    return _safe_repo_path(value, field)


def path_matches(path: str, pattern: str) -> bool:
    if pattern.endswith("/**"):
        base = pattern[:-3]
        return path == base or path.startswith(base + "/")
    return path == pattern
