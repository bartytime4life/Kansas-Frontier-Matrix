#!/usr/bin/env python3
"""Render a deterministic reviewer summary from ``stable_diff.py`` output.

This helper is presentation-only. It does not compare source artifacts itself,
interpret evidence or policy, approve promotion, create proof, release, publish,
or write any KFM lifecycle state.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

MAX_REPORT_BYTES = 1_048_576
TOOL_NAME = "stable-diff"
SUMMARY_TITLE = "Stable Diff Review Summary"


class DuplicateKeyError(ValueError):
    """Raised when an input JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when input JSON contains NaN or infinity."""


class SummaryRenderError(ValueError):
    """Safe deterministic failure for malformed or contradictory input."""

    def __init__(self, code: str, field: str) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


@dataclass(frozen=True)
class RenderResult:
    """Rendered Markdown plus the finite process disposition."""

    markdown: str
    status: str
    blocking: bool
    exit_code: int


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_report(path: Path) -> dict[str, Any]:
    try:
        if path.is_symlink():
            raise SummaryRenderError("INPUT_SYMLINK_DENIED", "/")
        if not path.is_file():
            raise SummaryRenderError("INPUT_NOT_FILE", "/")
        if path.stat().st_size > MAX_REPORT_BYTES:
            raise SummaryRenderError("INPUT_TOO_LARGE", "/")
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except SummaryRenderError:
        raise
    except UnicodeDecodeError as exc:
        raise SummaryRenderError("JSON_NOT_UTF8", "/") from exc
    except DuplicateKeyError as exc:
        raise SummaryRenderError("JSON_DUPLICATE_KEY", f"/{exc.args[0]}") from exc
    except NonFiniteNumberError as exc:
        raise SummaryRenderError("JSON_NONFINITE_NUMBER", "/") from exc
    except json.JSONDecodeError as exc:
        raise SummaryRenderError("JSON_INVALID", "/") from exc
    except OSError as exc:
        raise SummaryRenderError("INPUT_READ_ERROR", "/") from exc
    if not isinstance(value, dict):
        raise SummaryRenderError("ROOT_NOT_OBJECT", "/")
    return value


def _exact_keys(
    value: Mapping[str, Any],
    *,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
    field: str,
) -> None:
    keys = frozenset(value)
    if not required <= keys or not keys <= required | optional:
        raise SummaryRenderError("REPORT_SHAPE_INVALID", field)


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise SummaryRenderError("FIELD_INVALID", field)
    if any(ord(char) < 32 for char in value):
        raise SummaryRenderError("FIELD_INVALID", field)
    return value


def _canonical_string_array(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise SummaryRenderError("SUMMARY_ARRAY_INVALID", field)
    if any(any(ord(char) < 32 for char in item) for item in value):
        raise SummaryRenderError("SUMMARY_ARRAY_INVALID", field)
    if value != sorted(set(value)):
        raise SummaryRenderError("SUMMARY_ARRAY_NOT_CANONICAL", field)
    return value


def _display_name(value: str) -> str:
    normalized = value.replace("\\", "/")
    name = PurePosixPath(normalized).name or normalized
    return _markdown_code(name[:160])


def _markdown_code(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|")
    return f"`{escaped}`"


def _keys_cell(values: Sequence[str]) -> str:
    if not values:
        return "—"
    return "<br>".join(_markdown_code(json.dumps(item, ensure_ascii=False)) for item in values)


def _validate_report(report: Mapping[str, Any]) -> tuple[str, bool, str, str, dict[str, list[str]], str | None]:
    _exact_keys(
        report,
        required=frozenset({"tool", "status", "blocking", "left", "right", "summary"}),
        optional=frozenset({"error"}),
        field="/",
    )
    if report.get("tool") != TOOL_NAME:
        raise SummaryRenderError("TOOL_INVALID", "/tool")
    status = _text(report.get("status"), "/status")
    if status not in {"same", "changed", "error"}:
        raise SummaryRenderError("STATUS_INVALID", "/status")
    blocking = report.get("blocking")
    if not isinstance(blocking, bool):
        raise SummaryRenderError("BLOCKING_INVALID", "/blocking")
    left = _text(report.get("left"), "/left")
    right = _text(report.get("right"), "/right")
    summary = report.get("summary")
    if not isinstance(summary, dict):
        raise SummaryRenderError("SUMMARY_INVALID", "/summary")
    _exact_keys(
        summary,
        required=frozenset({"added", "removed", "changed"}),
        field="/summary",
    )
    normalized = {
        name: _canonical_string_array(summary.get(name), f"/summary/{name}")
        for name in ("added", "removed", "changed")
    }
    all_keys = normalized["added"] + normalized["removed"] + normalized["changed"]
    if len(all_keys) != len(set(all_keys)):
        raise SummaryRenderError("SUMMARY_CLASS_OVERLAP", "/summary")
    changed = bool(all_keys)

    error_code: str | None = None
    error = report.get("error")
    if status == "same":
        if changed or blocking or error is not None:
            raise SummaryRenderError("STATUS_CONTRADICTION", "/status")
    elif status == "changed":
        if not changed or error is not None:
            raise SummaryRenderError("STATUS_CONTRADICTION", "/status")
    else:
        if changed or not blocking or not isinstance(error, dict):
            raise SummaryRenderError("STATUS_CONTRADICTION", "/status")
        _exact_keys(
            error,
            required=frozenset({"code", "message"}),
            field="/error",
        )
        error_code = _text(error.get("code"), "/error/code")
        _text(error.get("message"), "/error/message")
    return status, blocking, left, right, normalized, error_code


def render_stable_diff_summary(report_path: Path, output_path: Path | None = None) -> RenderResult:
    """Validate one stable-diff report and render a bounded Markdown summary."""

    report = _read_report(report_path)
    status, blocking, left, right, summary, error_code = _validate_report(report)
    total = sum(len(values) for values in summary.values())
    lines = [
        f"# {SUMMARY_TITLE}",
        "",
        f"- **Status:** `{status}`",
        f"- **Blocking:** `{'true' if blocking else 'false'}`",
        f"- **Left artifact:** {_display_name(left)}",
        f"- **Right artifact:** {_display_name(right)}",
        f"- **Changed top-level keys:** `{total}`",
    ]
    if error_code is not None:
        lines.append(f"- **Error code:** {_markdown_code(error_code)}")
    lines.extend(
        [
            "",
            "| Class | Count | Keys |",
            "|---|---:|---|",
            f"| Added | `{len(summary['added'])}` | {_keys_cell(summary['added'])} |",
            f"| Removed | `{len(summary['removed'])}` | {_keys_cell(summary['removed'])} |",
            f"| Changed | `{len(summary['changed'])}` | {_keys_cell(summary['changed'])} |",
            "",
            "## Boundary",
            "",
            "This deterministic Markdown is a reviewer-facing projection of one "
            "`stable-diff` report. It does not compare source bytes, establish evidence "
            "sufficiency, decide policy, approve review, promote, create proof, release, "
            "publish, or authorize public use.",
            "",
        ]
    )
    markdown = "\n".join(lines)
    exit_code = 2 if status == "error" else 1 if blocking else 0
    if output_path is not None:
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding="utf-8", newline="\n")
        except OSError as exc:
            raise SummaryRenderError("OUTPUT_WRITE_ERROR", "/output") from exc
    return RenderResult(markdown=markdown, status=status, blocking=blocking, exit_code=exit_code)


def _error_payload(error: SummaryRenderError) -> str:
    return json.dumps(
        {
            "object_type": "StableDiffSummaryRenderError",
            "outcome": "ERROR",
            "code": error.code,
            "field": error.field,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a deterministic reviewer summary from stable-diff JSON."
    )
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = render_stable_diff_summary(args.report, args.output)
    except SummaryRenderError as error:
        print(_error_payload(error))
        return 2
    if args.output is None:
        print(result.markdown, end="")
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
