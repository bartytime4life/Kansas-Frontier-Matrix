#!/usr/bin/env python3
"""Deterministically compare the top-level keys of two local JSON objects.

This tool is intentionally non-authoritative. It reports structural value
changes and does not interpret policy, evidence sufficiency, promotion,
release, publication, or rollback state.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

TOOL_NAME = "stable-diff"
EXIT_OK = 0
EXIT_CHANGED = 1
EXIT_ERROR = 2


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or Infinity."""


class InputError(ValueError):
    """A deterministic, user-safe input failure."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _load_object(path: Path, label: str) -> dict[str, Any]:
    code_prefix = label.upper()

    if not path.exists():
        raise InputError(f"{code_prefix}_NOT_FOUND", f"{label} input does not exist.")
    if not path.is_file():
        raise InputError(
            f"{code_prefix}_NOT_FILE", f"{label} input is not a regular file."
        )

    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
            )
    except UnicodeDecodeError as exc:
        raise InputError(
            f"{code_prefix}_NOT_UTF8", f"{label} input is not valid UTF-8."
        ) from exc
    except DuplicateKeyError as exc:
        raise InputError(
            f"{code_prefix}_JSON_DUPLICATE_KEY",
            f"{label} input contains duplicate JSON key {exc.args[0]!r}.",
        ) from exc
    except NonFiniteNumberError as exc:
        raise InputError(
            f"{code_prefix}_JSON_NONFINITE_NUMBER",
            f"{label} input contains non-finite JSON number {exc.args[0]!r}.",
        ) from exc
    except json.JSONDecodeError as exc:
        raise InputError(
            f"{code_prefix}_JSON_INVALID",
            (
                f"{label} input is malformed JSON at "
                f"line {exc.lineno}, column {exc.colno}."
            ),
        ) from exc
    except OSError as exc:
        raise InputError(
            f"{code_prefix}_READ_ERROR", f"{label} input could not be read."
        ) from exc

    if not isinstance(value, dict):
        raise InputError(
            f"{code_prefix}_ROOT_NOT_OBJECT",
            f"{label} input must have a JSON object at its root.",
        )

    return value


def _canonical_value(value: Any) -> str:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def _summary(
    left: dict[str, Any], right: dict[str, Any]
) -> dict[str, list[str]]:
    left_keys = set(left)
    right_keys = set(right)
    shared_keys = left_keys & right_keys

    return {
        "added": sorted(right_keys - left_keys),
        "removed": sorted(left_keys - right_keys),
        "changed": sorted(
            key
            for key in shared_keys
            if _canonical_value(left[key]) != _canonical_value(right[key])
        ),
    }


def _base_report(left: Path, right: Path) -> dict[str, Any]:
    return {
        "tool": TOOL_NAME,
        "status": "error",
        "blocking": True,
        "left": str(left),
        "right": str(right),
        "summary": {"added": [], "removed": [], "changed": []},
    }


def compare_paths(
    left: Path, right: Path, *, fail_on_change: bool = False
) -> tuple[dict[str, Any], int]:
    """Compare two JSON object files and return a report plus process exit code."""

    report = _base_report(left, right)

    try:
        left_value = _load_object(left, "left")
        right_value = _load_object(right, "right")
    except InputError as exc:
        report["error"] = {"code": exc.code, "message": exc.message}
        return report, EXIT_ERROR

    report["summary"] = _summary(left_value, right_value)
    has_changes = any(report["summary"].values())
    report["status"] = "changed" if has_changes else "same"
    report["blocking"] = bool(has_changes and fail_on_change)

    if has_changes and fail_on_change:
        return report, EXIT_CHANGED
    return report, EXIT_OK


def _serialized(report: dict[str, Any]) -> str:
    return json.dumps(
        report,
        allow_nan=False,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def _write_report(output: Path, report: dict[str, Any]) -> None:
    with output.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(_serialized(report))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two local JSON objects by top-level key and emit a "
            "deterministic, non-authoritative JSON report."
        )
    )
    parser.add_argument("--left", required=True, type=Path)
    parser.add_argument("--right", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--fail-on-change",
        action="store_true",
        help="Return exit code 1 when valid inputs differ.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report, exit_code = compare_paths(
        args.left,
        args.right,
        fail_on_change=args.fail_on_change,
    )

    if args.output is None:
        print(_serialized(report), end="")
        return exit_code

    try:
        _write_report(args.output, report)
    except OSError:
        output_error = _base_report(args.left, args.right)
        output_error["error"] = {
            "code": "OUTPUT_WRITE_ERROR",
            "message": "Output report could not be written.",
        }
        print(_serialized(output_error), end="")
        return EXIT_ERROR

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
