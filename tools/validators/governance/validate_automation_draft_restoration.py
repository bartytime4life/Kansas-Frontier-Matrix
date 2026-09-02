#!/usr/bin/env python3
"""Validate a bounded KFM automation draft-restoration dispatch.

The validator has three finite modes:

* proposal preflight before any GitHub read;
* exact live pull-request and ready-event binding before mutation; and
* post-action verification for restored-draft or closed-unmerged state.

It reads only caller-provided JSON files, performs no network access, and never
echoes pull-request bodies or free-form proposal reasons.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Sequence

PROFILE = "kfm.automation.draft-restoration.v1"
CONTROL_ISSUE = 4024
DRAFT_ONLY_MARKER = "<!-- KFM_AUTOMATION_DRAFT_ONLY -->"
FALLBACK = "CLOSE_UNMERGED"
MAX_INPUT_BYTES = 1_048_576
MAX_BODY_BYTES = 65_536
MAX_EVENTS = 10_000
MAX_EVENT_AGE = timedelta(hours=4)
MAX_FUTURE_SKEW = timedelta(minutes=5)
AUTHORITY_BOUNDARY = (
    "A PASS authorizes one exact attempt to restore one marker-bound open pull "
    "request to draft and, only if that attempt fails while the exact binding "
    "remains open and unmerged, close that pull request. It grants no ready, "
    "review, approval, merge, release, deployment, publication, source, or "
    "repository-settings authority."
)

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})/[A-Za-z0-9._-]{1,100}$")
LOGIN_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
APP_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,99})$")
INCIDENT_RE = re.compile(r"^[a-z0-9][a-z0-9._:-]{2,191}$")
BRANCH_RE = re.compile(r"^(?:automation|fix)/[A-Za-z0-9][A-Za-z0-9._/-]{2,126}$")
NODE_ID_RE = re.compile(r"^[A-Za-z0-9_=-]{8,256}$")
RFC3339_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]+)?(?:Z|[+-][0-9]{2}:[0-9]{2})$"
)
TRANSITION_EVENTS = frozenset(
    {"ready_for_review", "converted_to_draft", "merged", "closed", "reopened"}
)

PROPOSAL_KEYS = frozenset(
    {
        "profile",
        "incident_id",
        "repository",
        "control_issue",
        "pr_number",
        "expected_base_ref",
        "expected_base_sha",
        "expected_head_branch",
        "expected_head_sha",
        "ready_event_at",
        "ready_actor",
        "ready_performed_via_app",
        "draft_only_marker",
        "restore_to_draft",
        "close_on_restore_failure",
        "fallback",
        "merge_allowed",
        "release_allowed",
        "deploy_allowed",
        "publish_allowed",
        "settings_change_allowed",
        "reason",
    }
)


class InputError(ValueError):
    """Raised when a bounded input cannot be interpreted safely."""


@dataclass(frozen=True)
class Result:
    outcome: str
    reason_codes: tuple[str, ...]
    fetch_eligible: bool = False
    write_eligible: bool = False
    pr_number: int | None = None
    expected_base_sha: str | None = None
    expected_head_sha: str | None = None
    expected_head_branch: str | None = None
    pr_node_id: str | None = None

    @property
    def exit_code(self) -> int:
        return {"PASS": 0, "NO_ACTION": 0, "DENY": 1, "ERROR": 2}[self.outcome]

    def as_dict(self) -> dict[str, Any]:
        return {
            "authority_boundary": AUTHORITY_BOUNDARY,
            "expected_base_sha": self.expected_base_sha,
            "expected_head_branch": self.expected_head_branch,
            "expected_head_sha": self.expected_head_sha,
            "fetch_eligible": self.fetch_eligible,
            "outcome": self.outcome,
            "pr_node_id": self.pr_node_id,
            "pr_number": self.pr_number,
            "reason_codes": list(self.reason_codes),
            "schema_version": "kfm.automation.draft-restoration-result.v1",
            "write_eligible": self.write_eligible,
        }


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise InputError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _finite_constant(value: str) -> Any:
    raise InputError(f"non-finite JSON number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise InputError(f"non-finite JSON number: {value}")
    return parsed


def load_json(path: Path) -> Any:
    try:
        metadata = path.lstat()
        if path.is_symlink() or not stat.S_ISREG(metadata.st_mode):
            raise InputError("input must be a regular non-symlink file")
        if metadata.st_size <= 0 or metadata.st_size > MAX_INPUT_BYTES:
            raise InputError("input is empty or exceeds the byte ceiling")
        raw = path.read_bytes()
        if len(raw) != metadata.st_size or b"\x00" in raw:
            raise InputError("input changed during read or contains NUL")
        text = raw.decode("utf-8")
        return json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_finite_constant,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, InputError) as exc:
        raise InputError(type(exc).__name__) from exc


def _parse_time(value: Any, field: str) -> datetime:
    if (
        not isinstance(value, str)
        or not value
        or len(value) > 64
        or RFC3339_RE.fullmatch(value) is None
    ):
        raise InputError(f"{field} must be a bounded RFC 3339 timestamp")
    normalized = value[:-1] + "+00:00" if value[-1:] in {"Z", "z"} else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise InputError(f"{field} must be an RFC 3339 timestamp") from exc
    if parsed.tzinfo is None:
        raise InputError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _is_bounded_string(value: Any, minimum: int, maximum: int) -> bool:
    return isinstance(value, str) and minimum <= len(value) <= maximum


def _proposal_errors(value: Any) -> list[str]:
    if not isinstance(value, dict):
        return ["PROPOSAL_ROOT_INVALID"]
    errors: list[str] = []
    if set(value) != PROPOSAL_KEYS:
        errors.append("PROPOSAL_KEYS_INVALID")
        return errors
    if value["profile"] != PROFILE:
        errors.append("PROFILE_INVALID")
    if not isinstance(value["incident_id"], str) or INCIDENT_RE.fullmatch(value["incident_id"]) is None:
        errors.append("INCIDENT_ID_INVALID")
    repository = value["repository"]
    if not isinstance(repository, str) or REPOSITORY_RE.fullmatch(repository) is None:
        errors.append("REPOSITORY_INVALID")
        owner = None
    else:
        owner = repository.split("/", 1)[0]
    if value["control_issue"] != CONTROL_ISSUE:
        errors.append("CONTROL_ISSUE_INVALID")
    if not _is_int(value["pr_number"]) or value["pr_number"] <= 0:
        errors.append("PR_NUMBER_INVALID")
    if value["expected_base_ref"] != "main":
        errors.append("BASE_REF_INVALID")
    if not isinstance(value["expected_base_sha"], str) or SHA_RE.fullmatch(value["expected_base_sha"]) is None:
        errors.append("BASE_SHA_INVALID")
    branch = value["expected_head_branch"]
    if (
        not isinstance(branch, str)
        or BRANCH_RE.fullmatch(branch) is None
        or ".." in branch
        or "//" in branch
        or any(part.startswith(".") for part in branch.split("/"))
    ):
        errors.append("HEAD_BRANCH_INVALID")
    if not isinstance(value["expected_head_sha"], str) or SHA_RE.fullmatch(value["expected_head_sha"]) is None:
        errors.append("HEAD_SHA_INVALID")
    try:
        _parse_time(value["ready_event_at"], "ready_event_at")
    except InputError:
        errors.append("READY_EVENT_TIME_INVALID")
    actor = value["ready_actor"]
    if not isinstance(actor, str) or LOGIN_RE.fullmatch(actor) is None or owner is None or actor != owner:
        errors.append("READY_ACTOR_INVALID")
    app = value["ready_performed_via_app"]
    if app is not None and (not isinstance(app, str) or APP_RE.fullmatch(app) is None):
        errors.append("READY_APP_INVALID")
    if value["draft_only_marker"] != DRAFT_ONLY_MARKER:
        errors.append("DRAFT_MARKER_INVALID")
    constants = {
        "restore_to_draft": True,
        "close_on_restore_failure": True,
        "fallback": FALLBACK,
        "merge_allowed": False,
        "release_allowed": False,
        "deploy_allowed": False,
        "publish_allowed": False,
        "settings_change_allowed": False,
    }
    if any(value[field] != expected for field, expected in constants.items()):
        errors.append("TERMINAL_LIMITS_INVALID")
    if not _is_bounded_string(value["reason"], 1, 512):
        errors.append("REASON_INVALID")
    return sorted(set(errors))


def validate_proposal(value: Any) -> Result:
    errors = _proposal_errors(value)
    if errors:
        return Result("ERROR", tuple(errors))
    assert isinstance(value, dict)
    return Result(
        "PASS",
        ("PROPOSAL_VALID",),
        fetch_eligible=True,
        pr_number=value["pr_number"],
        expected_base_sha=value["expected_base_sha"],
        expected_head_sha=value["expected_head_sha"],
        expected_head_branch=value["expected_head_branch"],
    )


def _live_identity(proposal: dict[str, Any], live: Any) -> tuple[Result | None, dict[str, Any] | None]:
    common = {
        "pr_number": proposal["pr_number"],
        "expected_base_sha": proposal["expected_base_sha"],
        "expected_head_sha": proposal["expected_head_sha"],
        "expected_head_branch": proposal["expected_head_branch"],
    }
    if not isinstance(live, dict):
        return Result("ERROR", ("LIVE_PR_ROOT_INVALID",), **common), None
    number = live.get("number")
    base = live.get("base")
    head = live.get("head")
    author = live.get("user")
    if number != proposal["pr_number"]:
        return Result("DENY", ("LIVE_PR_NUMBER_MISMATCH",), **common), None
    if not isinstance(base, dict) or not isinstance(head, dict) or not isinstance(author, dict):
        return Result("ERROR", ("LIVE_PR_SHAPE_INVALID",), **common), None
    head_repo = head.get("repo")
    if not isinstance(head_repo, dict):
        return Result("DENY", ("HEAD_REPOSITORY_UNAVAILABLE",), **common), None
    checks = (
        (base.get("ref") == proposal["expected_base_ref"], "BASE_REF_MISMATCH"),
        (base.get("sha") == proposal["expected_base_sha"], "BASE_SHA_MISMATCH"),
        (head.get("ref") == proposal["expected_head_branch"], "HEAD_BRANCH_MISMATCH"),
        (head.get("sha") == proposal["expected_head_sha"], "HEAD_SHA_MISMATCH"),
        (head_repo.get("full_name") == proposal["repository"], "HEAD_REPOSITORY_MISMATCH"),
        (author.get("login") == proposal["ready_actor"], "PR_AUTHOR_MISMATCH"),
    )
    failures = tuple(reason for passed, reason in checks if not passed)
    if failures:
        return Result("DENY", failures, **common), None
    node_id = live.get("node_id")
    if not isinstance(node_id, str) or NODE_ID_RE.fullmatch(node_id) is None:
        return Result("ERROR", ("PR_NODE_ID_INVALID",), **common), None
    body = live.get("body")
    if not isinstance(body, str):
        return Result("DENY", ("PR_BODY_INVALID",), **common), None
    try:
        body_bytes = body.encode("utf-8")
    except UnicodeError:
        return Result("DENY", ("PR_BODY_INVALID",), **common), None
    if len(body_bytes) > MAX_BODY_BYTES:
        return Result("DENY", ("PR_BODY_TOO_LARGE",), **common), None
    marker_count = body.count(DRAFT_ONLY_MARKER)
    if marker_count == 0:
        return Result("NO_ACTION", ("DRAFT_ONLY_MARKER_REMOVED",), **common), None
    if marker_count != 1:
        return Result("DENY", ("DRAFT_ONLY_MARKER_NONCANONICAL",), **common), None
    return None, {"node_id": node_id, "live": live, **common}


def _flatten_events(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise InputError("events root must be an array or paginated arrays")
    flattened: list[Any] = []
    for item in value:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    if len(flattened) > MAX_EVENTS:
        raise InputError("event count exceeds the ceiling")
    if any(not isinstance(item, dict) for item in flattened):
        raise InputError("every event must be an object")
    return flattened


def _app_slug(event: dict[str, Any]) -> str | None:
    app = event.get("performed_via_github_app")
    if app is None:
        return None
    if not isinstance(app, dict):
        raise InputError("performed_via_github_app must be null or an object")
    slug = app.get("slug")
    if not isinstance(slug, str) or APP_RE.fullmatch(slug) is None:
        raise InputError("GitHub App slug is invalid")
    return slug


def validate_live(
    proposal_value: Any,
    live: Any,
    events_value: Any,
    *,
    now: datetime,
) -> Result:
    preflight = validate_proposal(proposal_value)
    if preflight.outcome != "PASS":
        return preflight
    assert isinstance(proposal_value, dict)
    proposal = proposal_value
    identity_result, identity = _live_identity(proposal, live)
    if identity_result is not None:
        return identity_result
    assert identity is not None and isinstance(live, dict)
    common = {
        "pr_number": proposal["pr_number"],
        "expected_base_sha": proposal["expected_base_sha"],
        "expected_head_sha": proposal["expected_head_sha"],
        "expected_head_branch": proposal["expected_head_branch"],
        "pr_node_id": identity["node_id"],
    }
    if live.get("merged") is True or live.get("merged_at") is not None:
        return Result("NO_ACTION", ("PULL_REQUEST_ALREADY_MERGED",), **common)
    state = live.get("state")
    draft = live.get("draft")
    if state == "closed":
        return Result("NO_ACTION", ("PULL_REQUEST_ALREADY_CLOSED",), **common)
    if state != "open" or not isinstance(draft, bool):
        return Result("ERROR", ("LIVE_PR_STATE_INVALID",), **common)
    if draft:
        return Result("NO_ACTION", ("PULL_REQUEST_ALREADY_DRAFT",), **common)

    ready_at = _parse_time(proposal["ready_event_at"], "ready_event_at")
    if ready_at > now + MAX_FUTURE_SKEW:
        return Result("DENY", ("READY_EVENT_FROM_FUTURE",), **common)
    if now - ready_at > MAX_EVENT_AGE:
        return Result("DENY", ("READY_EVENT_STALE",), **common)

    try:
        events = _flatten_events(events_value)
    except InputError:
        return Result("ERROR", ("EVENT_INPUT_INVALID",), **common)
    matched: list[dict[str, Any]] = []
    later_transition = False
    for event in events:
        event_name = event.get("event")
        if event_name not in TRANSITION_EVENTS:
            continue
        try:
            created_at = _parse_time(event.get("created_at"), "event.created_at")
        except InputError:
            return Result("ERROR", ("TRANSITION_EVENT_TIME_INVALID",), **common)
        if created_at > ready_at:
            later_transition = True
        if event_name != "ready_for_review" or created_at != ready_at:
            continue
        actor = event.get("actor")
        issue = event.get("issue")
        if not isinstance(actor, dict):
            return Result("ERROR", ("READY_EVENT_SHAPE_INVALID",), **common)
        if issue is not None and (
            not isinstance(issue, dict) or issue.get("number") != proposal["pr_number"]
        ):
            continue
        try:
            app_slug = _app_slug(event)
        except InputError:
            return Result("ERROR", ("READY_EVENT_APP_INVALID",), **common)
        if (
            actor.get("login") == proposal["ready_actor"]
            and app_slug == proposal["ready_performed_via_app"]
        ):
            matched.append(event)
    if len(matched) != 1:
        return Result(
            "DENY",
            ("READY_EVENT_NOT_FOUND",) if not matched else ("READY_EVENT_DUPLICATE",),
            **common,
        )
    if later_transition:
        return Result("DENY", ("LATER_TRANSITION_PRESENT",), **common)
    return Result(
        "PASS",
        ("EXACT_UNAUTHORIZED_READY_EVENT_BOUND",),
        fetch_eligible=True,
        write_eligible=True,
        **common,
    )


def verify_post_state(proposal_value: Any, live: Any, expected: str) -> Result:
    preflight = validate_proposal(proposal_value)
    if preflight.outcome != "PASS":
        return preflight
    assert isinstance(proposal_value, dict)
    identity_result, identity = _live_identity(proposal_value, live)
    if identity_result is not None:
        return identity_result
    assert identity is not None and isinstance(live, dict)
    common = {
        "pr_number": proposal_value["pr_number"],
        "expected_base_sha": proposal_value["expected_base_sha"],
        "expected_head_sha": proposal_value["expected_head_sha"],
        "expected_head_branch": proposal_value["expected_head_branch"],
        "pr_node_id": identity["node_id"],
    }
    merged = live.get("merged") is True or live.get("merged_at") is not None
    if expected == "draft":
        passed = live.get("state") == "open" and live.get("draft") is True and not merged
        reason = "RESTORED_DRAFT_VERIFIED"
    else:
        passed = live.get("state") == "closed" and live.get("draft") is False and not merged
        reason = "CLOSED_UNMERGED_VERIFIED"
    return Result("PASS" if passed else "DENY", (reason if passed else "POST_ACTION_STATE_MISMATCH",), **common)


def _now(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    return _parse_time(value, "now")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("proposal", type=Path)
    parser.add_argument("--live-pr", type=Path)
    parser.add_argument("--events", type=Path)
    parser.add_argument("--verify-state", choices=("draft", "closed"))
    parser.add_argument("--now")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        proposal = load_json(args.proposal)
        if args.verify_state is not None:
            if args.live_pr is None or args.events is not None:
                raise InputError("post-state verification requires --live-pr and forbids --events")
            result = verify_post_state(proposal, load_json(args.live_pr), args.verify_state)
        elif args.live_pr is None and args.events is None:
            result = validate_proposal(proposal)
        elif args.live_pr is not None and args.events is not None:
            result = validate_live(
                proposal,
                load_json(args.live_pr),
                load_json(args.events),
                now=_now(args.now),
            )
        else:
            raise InputError("--live-pr and --events must be supplied together")
    except InputError:
        result = Result("ERROR", ("INPUT_INVALID",))
    print(json.dumps(result.as_dict(), sort_keys=True, separators=(",", ":")))
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
