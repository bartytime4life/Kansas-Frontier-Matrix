#!/usr/bin/env python3
"""Normalize and validate bounded repository-control source evidence.

The workflow streams one base64-encoded issue-comment JSON object per line into
this helper. The helper performs no network access, bounds every encoded record,
the aggregate decoded input, and the record count before it writes one canonical
comments array. A separate mode validates the strict local source-status record.
No mode emits untrusted response bodies or executes their content.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, BinaryIO, Sequence

STATUS_KEYS = {"schema_version", "repository", "control_issue", "status"}
STATUS_VALUES = {"AVAILABLE", "UNAVAILABLE", "INVALID", "OVER_LIMIT"}
MAX_CONTROL_SOURCE_COMMENTS = 10_000
MAX_CONTROL_SOURCE_BYTES = 16 * 1024 * 1024
MAX_ENCODED_COMMENT_RECORD_BYTES = 512 * 1024
AUTHORITY_BOUNDARY = (
    "This result proves only whether the workflow obtained and bounded the "
    "designated control issue comments for this run. It is not transition "
    "authorization, independent review, settings evidence, release authority, "
    "or publication authority."
)


class InputError(ValueError):
    """Raised when bounded source input is unsafe or malformed."""


class LimitError(InputError):
    """Raised when bounded source input exceeds a declared limit."""


@dataclass(frozen=True)
class Result:
    outcome_class: str
    reason_code: str
    summary: str
    repository: str | None = None
    control_issue: int | None = None

    @property
    def exit_code(self) -> int:
        return 0 if self.outcome_class == "PASS" else 1

    def as_dict(self) -> dict[str, Any]:
        return {
            "outcome_class": self.outcome_class,
            "reason_code": self.reason_code,
            "summary": self.summary,
            "repository": self.repository,
            "control_issue": self.control_issue,
            "authority_boundary": AUTHORITY_BOUNDARY,
        }


def _object_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _positive_int(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be an integer") from exc
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def normalize_comment_stream(
    stream: BinaryIO,
    output_path: Path,
    *,
    max_comments: int = MAX_CONTROL_SOURCE_COMMENTS,
    max_bytes: int = MAX_CONTROL_SOURCE_BYTES,
    max_encoded_record_bytes: int = MAX_ENCODED_COMMENT_RECORD_BYTES,
) -> tuple[int, int]:
    """Normalize a bounded base64-per-line comment stream to one JSON array."""

    if max_comments <= 0 or max_bytes <= 0 or max_encoded_record_bytes <= 0:
        raise InputError("normalization limits must be positive integers")

    comments: list[dict[str, Any]] = []
    decoded_bytes = 2  # opening and closing brackets in the normalized array

    while True:
        encoded_line = stream.readline(max_encoded_record_bytes + 1)
        if not encoded_line:
            break
        if len(encoded_line) > max_encoded_record_bytes:
            raise LimitError("encoded comment record exceeds the byte limit")

        encoded = encoded_line.strip()
        if not encoded:
            continue
        try:
            raw = base64.b64decode(encoded, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise InputError("comment stream contains invalid base64") from exc

        projected_bytes = decoded_bytes + len(raw) + (1 if comments else 0)
        if projected_bytes > max_bytes:
            raise LimitError("comment stream exceeds the aggregate byte limit")

        try:
            value = json.loads(
                raw.decode("utf-8"),
                object_pairs_hook=_object_no_duplicates,
            )
        except (UnicodeError, json.JSONDecodeError, InputError) as exc:
            raise InputError("comment stream contains invalid JSON") from exc
        if not isinstance(value, dict):
            raise InputError("comment stream records must be JSON objects")

        comments.append(value)
        decoded_bytes = projected_bytes
        if len(comments) > max_comments:
            raise LimitError("comment stream exceeds the record-count limit")

    normalized = (
        json.dumps(
            comments,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")
    if len(normalized) > max_bytes:
        raise LimitError("normalized comments exceed the aggregate byte limit")

    try:
        output_path.write_bytes(normalized)
    except OSError as exc:
        raise InputError("cannot write normalized comments") from exc
    return len(comments), len(normalized)


def load_json(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object_no_duplicates,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, InputError) as exc:
        raise InputError(f"cannot parse source status: {exc}") from exc


def evaluate(
    value: Any,
    *,
    expected_repository: str,
    expected_control_issue: int,
) -> Result:
    if not isinstance(value, dict):
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            "The control-source status root must be an object.",
        )

    missing = sorted(STATUS_KEYS - set(value))
    extra = sorted(set(value) - STATUS_KEYS)
    if missing or extra:
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            "The control-source status has missing or unsupported fields.",
        )

    repository = value.get("repository")
    control_issue = value.get("control_issue")
    status = value.get("status")
    if value.get("schema_version") != "1.0.0":
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            "The control-source status schema version is unsupported.",
        )
    if (
        not isinstance(repository, str)
        or not repository
        or len(repository) > 255
        or repository != expected_repository
    ):
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_BINDING_MISMATCH",
            "The control-source repository binding does not match this run.",
        )
    if (
        not isinstance(control_issue, int)
        or isinstance(control_issue, bool)
        or control_issue <= 0
        or control_issue != expected_control_issue
    ):
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_BINDING_MISMATCH",
            "The control-source issue binding does not match this run.",
            repository=repository,
        )
    if status not in STATUS_VALUES:
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            "The control-source availability state is unsupported.",
            repository=repository,
            control_issue=control_issue,
        )
    if status == "UNAVAILABLE":
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_UNAVAILABLE",
            "The designated repository-control issue comments were unavailable.",
            repository=repository,
            control_issue=control_issue,
        )
    if status == "INVALID":
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_RESPONSE_INVALID",
            "The designated repository-control response was not a valid bounded comment stream.",
            repository=repository,
            control_issue=control_issue,
        )
    if status == "OVER_LIMIT":
        return Result(
            "REGRESSION",
            "CONTROL_SOURCE_LIMIT_EXCEEDED",
            "The designated repository-control response exceeded a configured input limit.",
            repository=repository,
            control_issue=control_issue,
        )
    return Result(
        "PASS",
        "CONTROL_SOURCE_AVAILABLE",
        "The designated repository-control issue comments were obtained and bounded for this run.",
        repository=repository,
        control_issue=control_issue,
    )


def append_github_step_summary(path: Path, result: Result) -> None:
    posture = "NON_BLOCKING" if result.exit_code == 0 else "BLOCKING"
    lines = [
        "### Repository-control source classification",
        "",
        f"- Outcome class: `{result.outcome_class}`.",
        f"- Reason code: `{result.reason_code}`.",
        f"- Exit code: `{result.exit_code}`.",
        f"- Transition posture: `{posture}`.",
    ]
    if result.repository is not None:
        lines.append(f"- Repository: `{result.repository}`.")
    if result.control_issue is not None:
        lines.append(f"- Control issue: `#{result.control_issue}`.")
    lines.extend(
        [
            "- Response bodies and transport errors are not copied into this summary.",
            f"- Authority boundary: {AUTHORITY_BOUNDARY}",
            "",
        ]
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--normalize-comments-stream", action="store_true")
    parser.add_argument("--comments-output", type=Path)
    parser.add_argument(
        "--max-comments",
        type=_positive_int,
        default=MAX_CONTROL_SOURCE_COMMENTS,
    )
    parser.add_argument(
        "--max-bytes",
        type=_positive_int,
        default=MAX_CONTROL_SOURCE_BYTES,
    )
    parser.add_argument(
        "--max-encoded-record-bytes",
        type=_positive_int,
        default=MAX_ENCODED_COMMENT_RECORD_BYTES,
    )
    parser.add_argument("--status-file", type=Path)
    parser.add_argument("--expected-repository")
    parser.add_argument("--expected-control-issue", type=int)
    parser.add_argument("--github-step-summary", type=Path)
    args = parser.parse_args(argv)

    if args.normalize_comments_stream:
        if args.comments_output is None:
            parser.error("--comments-output is required with --normalize-comments-stream")
        if any(
            value is not None
            for value in (
                args.status_file,
                args.expected_repository,
                args.expected_control_issue,
                args.github_step_summary,
            )
        ):
            parser.error("status-validation options cannot be mixed with normalization mode")
        try:
            record_count, normalized_bytes = normalize_comment_stream(
                sys.stdin.buffer,
                args.comments_output,
                max_comments=args.max_comments,
                max_bytes=args.max_bytes,
                max_encoded_record_bytes=args.max_encoded_record_bytes,
            )
        except LimitError:
            print(
                json.dumps(
                    {
                        "outcome_class": "REGRESSION",
                        "reason_code": "CONTROL_SOURCE_LIMIT_EXCEEDED",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            return 2
        except InputError:
            print(
                json.dumps(
                    {
                        "outcome_class": "REGRESSION",
                        "reason_code": "CONTROL_SOURCE_RESPONSE_INVALID",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            return 1
        print(
            json.dumps(
                {
                    "outcome_class": "PASS",
                    "reason_code": "CONTROL_SOURCE_STREAM_NORMALIZED",
                    "record_count": record_count,
                    "normalized_bytes": normalized_bytes,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 0

    if args.status_file is None:
        parser.error("--status-file is required for status validation")
    if args.expected_repository is None:
        parser.error("--expected-repository is required for status validation")
    if args.expected_control_issue is None:
        parser.error("--expected-control-issue is required for status validation")

    try:
        value = load_json(args.status_file)
    except InputError as exc:
        result = Result(
            "REGRESSION",
            "CONTROL_SOURCE_STATUS_INVALID",
            str(exc),
        )
    else:
        result = evaluate(
            value,
            expected_repository=args.expected_repository,
            expected_control_issue=args.expected_control_issue,
        )

    print(json.dumps(result.as_dict(), sort_keys=True, separators=(",", ":")))
    if args.github_step_summary is not None:
        try:
            append_github_step_summary(args.github_step_summary, result)
        except OSError as exc:
            print(f"REGRESSION: STEP_SUMMARY_WRITE_FAILED: {exc}", file=sys.stderr)
            return 1
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
