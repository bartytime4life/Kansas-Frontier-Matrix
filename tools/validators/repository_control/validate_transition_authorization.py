#!/usr/bin/env python3
"""Validate a short-lived, head-bound repository transition authorization.

The GitHub workflow supplies two untrusted JSON inputs:

* the ``pull_request_target`` event payload; and
* the paginated comments returned for the repository-control issue.

This validator never reads GitHub or executes pull-request code. It accepts only
an unedited comment by the repository owner whose bounded JSON record matches
the repository, control issue, pull request, base SHA, head SHA, owner login,
decision, and expiry. A pass is an explicit Model B transition record, not
independent review and not proof of the browser, app, token, or client that
created the owner-account comment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Sequence

MARKER = "<!-- KFM_REPOSITORY_TRANSITION_AUTHORIZATION_V1"
COMMENT_CLOSE = "-->"
MAX_COMMENT_BYTES = 65_536
MAX_PAYLOAD_BYTES = 8_192
MAX_COMMENTS = 10_000
MAX_AUTHORIZATION_AGE = timedelta(hours=4)
AUTHORITY_BOUNDARY = (
    "A pass records an exact owner-account transition decision only. "
    "It is not independent review, initiating-client attribution, "
    "ruleset evidence, release authority, or publication authority."
)
RFC3339_PATTERN = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}[Tt][0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]+)?(?:[Zz]|[+-][0-9]{2}:[0-9]{2})$"
)
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
GITHUB_LOGIN_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")

RECORD_KEYS = {
    "schema_version",
    "authorization_id",
    "repository",
    "control_issue",
    "pr_number",
    "base_sha",
    "head_sha",
    "authorizing_actor",
    "decision",
    "expires_at",
    "reason",
    "evidence_refs",
}
RESULT_KEYS = {
    "outcome_class",
    "reason_code",
    "summary",
    "pr_number",
    "head_sha",
    "authorization_id",
    "comment_id",
    "expires_at",
    "authority_boundary",
}


class InputError(ValueError):
    """Raised when an input cannot be interpreted safely."""


@dataclass(frozen=True)
class Result:
    outcome_class: str
    reason_code: str
    summary: str
    pr_number: int | None = None
    head_sha: str | None = None
    authorization_id: str | None = None
    comment_id: int | None = None
    expires_at: str | None = None

    @property
    def exit_code(self) -> int:
        return {
            "PASS": 0,
            "NOT_APPLICABLE": 0,
            "EXPECTED_READINESS_HOLD": 3,
            "REGRESSION": 1,
        }[self.outcome_class]

    def as_dict(self) -> dict[str, Any]:
        return {
            "outcome_class": self.outcome_class,
            "reason_code": self.reason_code,
            "summary": self.summary,
            "pr_number": self.pr_number,
            "head_sha": self.head_sha,
            "authorization_id": self.authorization_id,
            "comment_id": self.comment_id,
            "expires_at": self.expires_at,
            "authority_boundary": AUTHORITY_BOUNDARY,
        }


def append_github_step_summary(path: Path, result: Result) -> None:
    """Append a bounded classification without copying untrusted comment text."""

    posture = "BLOCKING" if result.exit_code else "NON_BLOCKING"
    lines = [
        "### Repository transition classification",
        "",
        f"- Outcome class: `{result.outcome_class}`.",
        f"- Reason code: `{result.reason_code}`.",
        f"- Exit code: `{result.exit_code}`.",
        f"- Transition posture: `{posture}`.",
    ]
    if result.pr_number is not None:
        lines.append(f"- Pull request: `#{result.pr_number}`.")
    if result.head_sha is not None:
        lines.append(f"- Head SHA: `{result.head_sha}`.")
    if result.authorization_id is not None:
        lines.append(f"- Authorization ID: `{result.authorization_id}`.")
    if result.comment_id is not None:
        lines.append(f"- Authorization comment ID: `{result.comment_id}`.")
    if result.expires_at is not None:
        lines.append(f"- Authorization expiry: `{result.expires_at}`.")
    lines.extend(
        [
            "- Classification source: bounded validator fields only; untrusted "
            "issue-comment bodies and free-form reasons are not copied.",
            f"- Authority boundary: {AUTHORITY_BOUNDARY}",
            "",
        ]
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def _object_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object_no_duplicates,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, InputError) as exc:
        raise InputError(f"cannot parse {path}: {exc}") from exc


def _time(value: Any, field: str) -> datetime:
    if (
        not isinstance(value, str)
        or not value
        or RFC3339_PATTERN.fullmatch(value) is None
    ):
        raise InputError(f"{field} must be an RFC 3339 timestamp")
    text = value[:-1] + "+00:00" if value[-1] in {"Z", "z"} else value
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
        and all(character in "0123456789abcdef" for character in value)
    )


def _nonempty_string(value: Any, *, maximum: int) -> bool:
    return isinstance(value, str) and 0 < len(value) <= maximum


def _authorization_id(value: Any) -> bool:
    return (
        _nonempty_string(value, maximum=192)
        and len(value) >= 3
        and value[0].isalnum()
        and all(
            character in "abcdefghijklmnopqrstuvwxyz0123456789._:-"
            for character in value
        )
    )


def _flatten_comments(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise InputError("comments input must be an array or an array of pages")
    flattened: list[Any] = []
    for item in value:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    if len(flattened) > MAX_COMMENTS:
        raise InputError(f"comments input exceeds {MAX_COMMENTS} records")
    if any(not isinstance(comment, dict) for comment in flattened):
        raise InputError("every comment must be an object")
    return flattened


def _extract_payload(body: Any) -> dict[str, Any] | None:
    if not isinstance(body, str):
        return None
    encoded = body.encode("utf-8")
    if len(encoded) > MAX_COMMENT_BYTES:
        if MARKER in body:
            raise InputError("authorization comment exceeds the size limit")
        return None
    if MARKER not in body:
        return None
    if body.count(MARKER) != 1:
        raise InputError("authorization comment must contain exactly one marker")
    start = body.index(MARKER) + len(MARKER)
    end = body.find(COMMENT_CLOSE, start)
    if end < 0:
        raise InputError("authorization marker is not closed")
    payload_text = body[start:end].strip()
    if not payload_text or len(payload_text.encode("utf-8")) > MAX_PAYLOAD_BYTES:
        raise InputError("authorization payload is empty or exceeds the size limit")
    try:
        payload = json.loads(payload_text, object_pairs_hook=_object_no_duplicates)
    except (json.JSONDecodeError, InputError) as exc:
        raise InputError(f"authorization payload is not strict JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise InputError("authorization payload root must be an object")
    return payload


def _event_fields(
    event: Any, *, default_branch: str
) -> tuple[str, int, str, str, bool, str]:
    if not isinstance(event, dict):
        raise InputError("event root must be an object")
    repository = event.get("repository")
    pull_request = event.get("pull_request")
    if not isinstance(repository, dict) or not isinstance(pull_request, dict):
        raise InputError("event must include repository and pull_request objects")
    repository_name = repository.get("full_name")
    number = pull_request.get("number")
    base = pull_request.get("base")
    head = pull_request.get("head")
    draft = pull_request.get("draft")
    state = pull_request.get("state")
    if (
        not isinstance(repository_name, str)
        or REPOSITORY_PATTERN.fullmatch(repository_name) is None
    ):
        raise InputError("repository.full_name must match the repository schema")
    if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
        raise InputError("pull_request.number must be a positive integer")
    if not isinstance(base, dict) or not isinstance(head, dict):
        raise InputError("pull_request base and head must be objects")
    if base.get("ref") != default_branch:
        return repository_name, number, "", "", bool(draft), str(state)
    base_sha = base.get("sha")
    head_sha = head.get("sha")
    if not _sha(base_sha) or not _sha(head_sha):
        raise InputError("pull_request base.sha and head.sha must be lowercase SHAs")
    if not isinstance(draft, bool):
        raise InputError("pull_request.draft must be a boolean")
    if state not in {"open", "closed"}:
        raise InputError("pull_request.state must be open or closed")
    return repository_name, number, base_sha, head_sha, draft, state


def _record_errors(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = sorted(RECORD_KEYS - set(record))
    extra = sorted(set(record) - RECORD_KEYS)
    if missing:
        errors.append(f"missing keys: {', '.join(missing)}")
    if extra:
        errors.append(f"unsupported keys: {', '.join(extra)}")
    if errors:
        return errors
    if record["schema_version"] != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if not _authorization_id(record["authorization_id"]):
        errors.append(
            "authorization_id must contain 3 to 192 supported characters"
        )
    if (
        not isinstance(record["repository"], str)
        or REPOSITORY_PATTERN.fullmatch(record["repository"]) is None
    ):
        errors.append("repository must match the repository schema")
    if (
        not isinstance(record["control_issue"], int)
        or isinstance(record["control_issue"], bool)
        or record["control_issue"] <= 0
    ):
        errors.append("control_issue must be a positive integer")
    if (
        not isinstance(record["pr_number"], int)
        or isinstance(record["pr_number"], bool)
        or record["pr_number"] <= 0
    ):
        errors.append("pr_number must be a positive integer")
    if not _sha(record["base_sha"]) or not _sha(record["head_sha"]):
        errors.append("base_sha and head_sha must be lowercase 40-character SHAs")
    if (
        not isinstance(record["authorizing_actor"], str)
        or GITHUB_LOGIN_PATTERN.fullmatch(record["authorizing_actor"]) is None
    ):
        errors.append("authorizing_actor must match the GitHub login schema")
    if record["decision"] != "ALLOW_READY_AND_MERGE":
        errors.append("decision must be ALLOW_READY_AND_MERGE")
    try:
        _time(record["expires_at"], "expires_at")
    except InputError as exc:
        errors.append(str(exc))
    if not _nonempty_string(record["reason"], maximum=512):
        errors.append("reason must be a bounded non-empty string")
    refs = record["evidence_refs"]
    if (
        not isinstance(refs, list)
        or not refs
        or any(not _nonempty_string(ref, maximum=2048) for ref in refs)
        or len(refs) != len(set(refs))
    ):
        errors.append("evidence_refs must be unique bounded non-empty strings")
    return errors


def validate_transition_record(record: Any) -> dict[str, Any]:
    """Return one complete authorization record or reject it fail closed."""

    if not isinstance(record, dict):
        raise InputError("authorization record must be a JSON object")
    errors = _record_errors(record)
    if errors:
        # The detailed field values originate in an untrusted comment and are
        # intentionally not copied into the public classification output.
        raise InputError("authorization record does not match the required schema")
    return record


def _result_errors(value: Any) -> list[str]:
    """Validate the bounded classification before any bytes reach stdout."""

    if not isinstance(value, dict):
        return ["result root must be an object"]
    errors: list[str] = []
    missing = sorted(RESULT_KEYS - set(value))
    extra = sorted(set(value) - RESULT_KEYS)
    if missing:
        errors.append("result has missing keys")
    if extra:
        errors.append("result has unsupported keys")
    if errors:
        return errors

    outcome_class = value["outcome_class"]
    if outcome_class not in {
        "PASS",
        "NOT_APPLICABLE",
        "EXPECTED_READINESS_HOLD",
        "REGRESSION",
    }:
        errors.append("result outcome_class is unsupported")
    if not _nonempty_string(value["reason_code"], maximum=128):
        errors.append("result reason_code is invalid")
    if not _nonempty_string(value["summary"], maximum=1_024):
        errors.append("result summary is invalid")
    if value["authority_boundary"] != AUTHORITY_BOUNDARY:
        errors.append("result authority boundary is invalid")

    pr_number = value["pr_number"]
    if pr_number is not None and (
        not isinstance(pr_number, int) or isinstance(pr_number, bool) or pr_number <= 0
    ):
        errors.append("result pr_number is invalid")
    head_sha = value["head_sha"]
    if head_sha is not None and not _sha(head_sha):
        errors.append("result head_sha is invalid")

    authorization_id = value["authorization_id"]
    comment_id = value["comment_id"]
    expires_at = value["expires_at"]
    authorization_fields_present = any(
        item is not None for item in (authorization_id, comment_id, expires_at)
    )
    authorization_fields_complete = (
        _authorization_id(authorization_id)
        and isinstance(comment_id, int)
        and not isinstance(comment_id, bool)
        and comment_id > 0
    )
    if authorization_fields_complete:
        try:
            _time(expires_at, "result.expires_at")
        except InputError:
            authorization_fields_complete = False

    if outcome_class == "PASS":
        if value["reason_code"] != "TRANSITION_AUTHORIZED":
            errors.append("PASS result reason is invalid")
        if pr_number is None or head_sha is None or not authorization_fields_complete:
            errors.append("PASS result is missing exact authorization fields")
    elif authorization_fields_present:
        errors.append("non-PASS result contains partial authorization fields")
    return errors


def render_result(result: Result) -> tuple[Result, str]:
    """Build a complete JSON object and replace unsafe output with a regression."""

    try:
        value = result.as_dict()
        errors = _result_errors(value)
        if errors:
            raise InputError("validator result failed its output contract")
        rendered = json.dumps(
            value,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    except (InputError, TypeError, ValueError, RecursionError):
        result = Result(
            "REGRESSION",
            "RESULT_SERIALIZATION_INVALID",
            "The validator could not emit a complete result; the transition remains blocked.",
        )
        rendered = json.dumps(
            result.as_dict(),
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    return result, rendered


def evaluate(
    event: Any,
    comments_value: Any,
    *,
    control_issue: int,
    authorized_login: str,
    default_branch: str,
    now: datetime,
) -> Result:
    try:
        repository, pr_number, base_sha, head_sha, draft, state = _event_fields(
            event, default_branch=default_branch
        )
        comments = _flatten_comments(comments_value)
    except InputError as exc:
        return Result("REGRESSION", "INPUT_INVALID", str(exc))

    if not base_sha:
        return Result(
            "NOT_APPLICABLE",
            "NON_DEFAULT_BRANCH_TARGET",
            "The pull request does not target the configured default branch.",
            pr_number=pr_number,
        )
    if state != "open":
        return Result(
            "NOT_APPLICABLE",
            "PULL_REQUEST_NOT_OPEN",
            "The pull request is not open.",
            pr_number=pr_number,
            head_sha=head_sha,
        )
    if draft:
        return Result(
            "EXPECTED_READINESS_HOLD",
            "PULL_REQUEST_IS_DRAFT",
            "The pull request remains draft; ready and merge transitions are held.",
            pr_number=pr_number,
            head_sha=head_sha,
        )

    matching_seen = False
    mismatch_reason: str | None = None
    invalid_record_seen = False
    valid: list[tuple[datetime, dict[str, Any], dict[str, Any]]] = []

    for comment in comments:
        body = comment.get("body")
        if not isinstance(body, str) or MARKER not in body:
            continue
        user = comment.get("user")
        login = user.get("login") if isinstance(user, dict) else None
        if login != authorized_login or comment.get("author_association") != "OWNER":
            continue
        try:
            record = _extract_payload(body)
        except InputError:
            matching_seen = True
            invalid_record_seen = True
            continue
        if record is None:
            continue
        try:
            record = validate_transition_record(record)
        except InputError:
            matching_seen = True
            invalid_record_seen = True
            continue
        if (
            record.get("repository") != repository
            or record.get("control_issue") != control_issue
            or record.get("pr_number") != pr_number
        ):
            continue
        matching_seen = True
        if record["authorizing_actor"] != login:
            invalid_record_seen = True
            continue
        if record["base_sha"] != base_sha:
            mismatch_reason = "AUTHORIZATION_BASE_MISMATCH"
            continue
        if record["head_sha"] != head_sha:
            mismatch_reason = "AUTHORIZATION_HEAD_MISMATCH"
            continue
        comment_id = comment.get("id")
        if not isinstance(comment_id, int) or isinstance(comment_id, bool):
            invalid_record_seen = True
            continue
        try:
            created_at = _time(comment.get("created_at"), "comment.created_at")
            updated_at = _time(comment.get("updated_at"), "comment.updated_at")
            expires_at = _time(record["expires_at"], "expires_at")
        except InputError:
            invalid_record_seen = True
            continue
        if created_at != updated_at:
            invalid_record_seen = True
            continue
        if created_at > now + timedelta(minutes=5):
            invalid_record_seen = True
            continue
        if expires_at <= created_at:
            invalid_record_seen = True
            continue
        if expires_at - created_at > MAX_AUTHORIZATION_AGE:
            invalid_record_seen = True
            continue
        if expires_at <= now:
            mismatch_reason = "AUTHORIZATION_EXPIRED"
            continue
        valid.append((created_at, record, comment))

    if valid:
        _, record, comment = max(valid, key=lambda item: item[0])
        return Result(
            "PASS",
            "TRANSITION_AUTHORIZED",
            "An unedited owner comment authorizes ready and merge for this exact base and head.",
            pr_number=pr_number,
            head_sha=head_sha,
            authorization_id=record["authorization_id"],
            comment_id=comment["id"],
            expires_at=record["expires_at"],
        )
    if invalid_record_seen and matching_seen:
        return Result(
            "REGRESSION",
            "MATCHING_AUTHORIZATION_INVALID",
            "A matching owner transition record is malformed, edited, "
            "future-dated, or outside its permitted validity window.",
            pr_number=pr_number,
            head_sha=head_sha,
        )
    if mismatch_reason is not None:
        return Result(
            "EXPECTED_READINESS_HOLD",
            mismatch_reason,
            "A transition record exists for this pull request but not for the current base, head, or time.",
            pr_number=pr_number,
            head_sha=head_sha,
        )
    return Result(
        "EXPECTED_READINESS_HOLD",
        "TRANSITION_AUTHORIZATION_MISSING",
        "No current unedited owner transition record matches this pull request and head.",
        pr_number=pr_number,
        head_sha=head_sha,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--control-issue", type=int, required=True)
    parser.add_argument("--authorized-login", required=True)
    parser.add_argument("--default-branch", default="main")
    parser.add_argument("--now")
    parser.add_argument("--github-step-summary", type=Path)
    args = parser.parse_args(argv)

    try:
        event = load_json(args.event)
        comments = load_json(args.comments)
        now = _time(args.now, "now") if args.now else datetime.now(timezone.utc)
    except InputError as exc:
        result = Result("REGRESSION", "INPUT_INVALID", str(exc))
    else:
        result = evaluate(
            event,
            comments,
            control_issue=args.control_issue,
            authorized_login=args.authorized_login,
            default_branch=args.default_branch,
            now=now,
        )
    result, rendered = render_result(result)
    sys.stdout.write(rendered + "\n")
    if args.github_step_summary is not None:
        try:
            append_github_step_summary(args.github_step_summary, result)
        except OSError as exc:
            print(f"REGRESSION: STEP_SUMMARY_WRITE_FAILED: {exc}", file=sys.stderr)
            return 1
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
