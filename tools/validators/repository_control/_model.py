"""Shared types and deterministic state helpers for repository-control validation."""

from __future__ import annotations

import argparse
import copy
import fnmatch
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

OUTCOMES = {
    "PASS", "EXPECTED_READINESS_HOLD", "REGRESSION",
    "NOT_APPLICABLE", "SKIPPED_EXPLICIT", "UNKNOWN",
}
CLAIM_STATES = {"IDLE", "ACTIVE", "HELD", "TERMINAL"}
PR_STATES = {"OPEN", "CLOSED_UNMERGED", "MERGED"}
OPERATIONS = {"create", "update", "delete", "rename", "workflow", "issue_only", "modify_control_logic"}
PERMISSIONS = (
    "modify_control_logic", "ready_transition", "rebase", "force_push", "merge",
    "source_activation", "proof_construction", "release", "deployment", "publication",
)
CONTROL_PREFIXES = (
    "control_plane/repository_control_state.",
    "contracts/governance/repository_control_state.",
    "schemas/contracts/v1/governance/repository_control_state.",
    "schemas/contracts/v1/governance/ci_outcome.",
    "tools/validators/repository_control/",
    "tests/validators/test_repository_control.py",
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
    pass


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
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


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
    return isinstance(value, str) and len(value) == 40 and all(c in "0123456789abcdef" for c in value)


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


