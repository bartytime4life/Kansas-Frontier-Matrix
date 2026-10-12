#!/usr/bin/env python3
"""Validate bounded availability evidence for the repository-control issue.

The workflow converts its GitHub issue-comment read into one strict local status
record. This validator performs no network access, emits no untrusted response
body, and fails closed when the designated source is unavailable or malformed.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

STATUS_KEYS = {"schema_version", "repository", "control_issue", "status"}
STATUS_VALUES = {"AVAILABLE", "UNAVAILABLE"}
AUTHORITY_BOUNDARY = (
    "This result proves only whether the workflow obtained the designated "
    "control issue comments for this run. It is not transition authorization, "
    "independent review, settings evidence, release authority, or publication authority."
)


class InputError(ValueError):
    """Raised when the bounded source-status input is unsafe or malformed."""


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
    return Result(
        "PASS",
        "CONTROL_SOURCE_AVAILABLE",
        "The designated repository-control issue comments were obtained for this run.",
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
    parser.add_argument("--status-file", type=Path, required=True)
    parser.add_argument("--expected-repository", required=True)
    parser.add_argument("--expected-control-issue", type=int, required=True)
    parser.add_argument("--github-step-summary", type=Path)
    args = parser.parse_args(argv)

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
