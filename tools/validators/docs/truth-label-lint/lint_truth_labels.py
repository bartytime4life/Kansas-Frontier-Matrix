#!/usr/bin/env python3
"""Opt-in structural lint for separate KFM authority and capability-maturity axes.

This checker is documentation QA only. It does not decide truth, evidence
sufficiency, capability acceptance, review state, release state, or publication.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence

MARKER_RE = re.compile(
    r"<!--\s*kfm-assessment-axes\s*:\s*required\s*-->", re.IGNORECASE
)
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
DECORATION_RE = re.compile(r"[*_`]+")
SPACE_RE = re.compile(r"\s+")

PASS = "DOC_TRUTH_LABEL_LINT_PASS"
NOT_APPLICABLE = "DOC_TRUTH_LABEL_LINT_NOT_APPLICABLE"
FAIL = "DOC_TRUTH_LABEL_LINT_FAIL"
ERROR = "ERROR"

MARKER_MISSING = "ASSESSMENT_AXES_MARKER_MISSING"
TABLE_MISSING = "ASSESSMENT_TABLE_MISSING"
AUTHORITY_MISSING = "AUTHORITY_AXIS_MISSING"
MATURITY_MISSING = "CAPABILITY_MATURITY_AXIS_MISSING"
VALUE_MISSING = "ASSESSMENT_AXIS_VALUE_MISSING"
COLLAPSED = "ASSESSMENT_AXES_COLLAPSED"
DUPLICATE = "ASSESSMENT_AXIS_DUPLICATE"
SPLIT_TABLE = "ASSESSMENT_AXES_SPLIT_TABLE"


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    line: int | None = None


@dataclass(frozen=True)
class LintResult:
    path: str
    outcome: str
    marker_present: bool
    authority_posture: str | None
    capability_maturity: str | None
    findings: tuple[Finding, ...]

    def as_dict(self) -> dict[str, object]:
        payload = asdict(self)
        payload["findings"] = [asdict(item) for item in self.findings]
        return payload


@dataclass(frozen=True)
class MarkdownTable:
    header: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    row_lines: tuple[int, ...]


def _visible_lines(text: str) -> list[tuple[int, str]]:
    """Return lines outside fenced code blocks while preserving line numbers."""
    visible: list[tuple[int, str]] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is None:
            visible.append((number, line))
    return visible


def _split_row(line: str) -> tuple[str, ...] | None:
    value = line.strip()
    if "|" not in value:
        return None
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|") and not value.endswith(r"\|"):
        value = value[:-1]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in value:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return tuple(cells)


def _is_separator(row: tuple[str, ...] | None) -> bool:
    return bool(row) and all(SEPARATOR_RE.fullmatch(cell.strip()) for cell in row)


def _parse_tables(lines: Sequence[tuple[int, str]]) -> tuple[MarkdownTable, ...]:
    tables: list[MarkdownTable] = []
    index = 0
    while index + 1 < len(lines):
        header = _split_row(lines[index][1])
        separator = _split_row(lines[index + 1][1])
        if not header or not _is_separator(separator) or len(header) != len(separator):
            index += 1
            continue

        rows: list[tuple[str, ...]] = []
        row_lines: list[int] = []
        cursor = index + 2
        while cursor < len(lines):
            candidate = _split_row(lines[cursor][1])
            if candidate is None or len(candidate) != len(header):
                break
            rows.append(candidate)
            row_lines.append(lines[cursor][0])
            cursor += 1
        tables.append(MarkdownTable(header, tuple(rows), tuple(row_lines)))
        index = max(cursor, index + 2)
    return tuple(tables)


def _normalize(value: str) -> str:
    value = DECORATION_RE.sub("", value).replace("&nbsp;", " ")
    return SPACE_RE.sub(" ", value.strip().lower())


def _header_indexes(header: Sequence[str]) -> tuple[int, int] | None:
    normalized = [_normalize(cell) for cell in header]
    if "axis" not in normalized:
        return None
    for name in ("result", "assessment", "value", "current result"):
        if name in normalized:
            return normalized.index("axis"), normalized.index(name)
    return None


def _axis_kind(label: str) -> str | None:
    value = _normalize(label)
    authority = "authority" in value or "epistemic" in value
    maturity = "maturity" in value and (
        "capability" in value or "implementation" in value
    )
    if authority and maturity:
        return "collapsed"
    if authority and (
        "epistemic" in value
        or "posture" in value
        or "evidence" in value
        or value == "authority"
    ):
        return "authority"
    if maturity:
        return "maturity"
    return None


def lint_text(
    text: str,
    *,
    path: str = "<memory>",
    require_marker: bool = False,
) -> LintResult:
    lines = _visible_lines(text)
    marker_present = MARKER_RE.search("\n".join(line for _, line in lines)) is not None
    if not marker_present:
        if not require_marker:
            return LintResult(path, NOT_APPLICABLE, False, None, None, ())
        return LintResult(
            path,
            FAIL,
            False,
            None,
            None,
            (Finding(MARKER_MISSING, "required opt-in marker is absent"),),
        )

    candidates: list[tuple[int, list[tuple[str, str, int]]]] = []
    findings: list[Finding] = []
    for table_index, table in enumerate(_parse_tables(lines)):
        indexes = _header_indexes(table.header)
        if indexes is None:
            continue
        axis_index, value_index = indexes
        recognized: list[tuple[str, str, int]] = []
        for row, line_number in zip(table.rows, table.row_lines, strict=True):
            kind = _axis_kind(row[axis_index])
            if kind == "collapsed":
                findings.append(
                    Finding(
                        COLLAPSED,
                        "authority/epistemic posture and capability maturity share one row",
                        line_number,
                    )
                )
            elif kind:
                recognized.append((kind, row[value_index].strip(), line_number))
        candidates.append((table_index, recognized))

    if not candidates:
        return LintResult(
            path,
            FAIL,
            True,
            None,
            None,
            (Finding(TABLE_MISSING, "no assessment table with Axis and result headers was found"),),
        )

    authority_entries: list[tuple[str, int, int]] = []
    maturity_entries: list[tuple[str, int, int]] = []
    for table_index, entries in candidates:
        for kind, value, line_number in entries:
            target = authority_entries if kind == "authority" else maturity_entries
            target.append((value, line_number, table_index))

    if not authority_entries:
        findings.append(Finding(AUTHORITY_MISSING, "Authority / epistemic posture row is missing"))
    if not maturity_entries:
        findings.append(Finding(MATURITY_MISSING, "Capability maturity row is missing"))

    for label, entries in (
        ("Authority / epistemic posture", authority_entries),
        ("Capability maturity", maturity_entries),
    ):
        if len(entries) > 1:
            findings.append(
                Finding(DUPLICATE, f"{label} appears more than once", entries[1][1])
            )
        if entries and not entries[0][0]:
            findings.append(
                Finding(
                    VALUE_MISSING,
                    f"{label} result is empty; record an explicit bounded result",
                    entries[0][1],
                )
            )

    if authority_entries and maturity_entries:
        if authority_entries[0][2] != maturity_entries[0][2]:
            findings.append(
                Finding(
                    SPLIT_TABLE,
                    "the two assessment axes must appear in the same table",
                    maturity_entries[0][1],
                )
            )

    findings.sort(key=lambda item: (item.line is None, item.line or 0, item.code))
    authority_value = authority_entries[0][0] if authority_entries else None
    maturity_value = maturity_entries[0][0] if maturity_entries else None
    return LintResult(
        path,
        FAIL if findings else PASS,
        True,
        authority_value,
        maturity_value,
        tuple(findings),
    )


def lint_path(path: Path, *, require_marker: bool = False) -> LintResult:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return LintResult(
            path.as_posix(),
            ERROR,
            False,
            None,
            None,
            (Finding(ERROR, f"could not read UTF-8 Markdown: {exc}"),),
        )
    return lint_text(text, path=path.as_posix(), require_marker=require_marker)


def discover_markdown(paths: Iterable[Path]) -> tuple[tuple[Path, ...], tuple[Finding, ...]]:
    discovered: set[Path] = set()
    errors: list[Finding] = []
    for supplied in paths:
        if not supplied.exists():
            errors.append(Finding(ERROR, f"input path does not exist: {supplied}"))
            continue
        if supplied.is_symlink():
            errors.append(Finding(ERROR, f"symlink input is not followed: {supplied}"))
            continue
        if supplied.is_file():
            if supplied.suffix.lower() == ".md":
                discovered.add(supplied)
            else:
                errors.append(Finding(ERROR, f"input is not Markdown: {supplied}"))
            continue

        for root, directories, files in os.walk(supplied, followlinks=False):
            directories[:] = sorted(
                name for name in directories if not (Path(root) / name).is_symlink()
            )
            for filename in sorted(files):
                candidate = Path(root) / filename
                if candidate.suffix.lower() == ".md" and not candidate.is_symlink():
                    discovered.add(candidate)
    return tuple(sorted(discovered, key=lambda item: item.as_posix())), tuple(errors)


def _aggregate_outcome(
    results: Sequence[LintResult], discovery_errors: Sequence[Finding]
) -> str:
    if discovery_errors or any(result.outcome == ERROR for result in results):
        return ERROR
    if any(result.outcome == FAIL for result in results):
        return FAIL
    return PASS


def _json_report(
    results: Sequence[LintResult], discovery_errors: Sequence[Finding]
) -> str:
    payload = {
        "outcome": _aggregate_outcome(results, discovery_errors),
        "results": [result.as_dict() for result in results],
        "discovery_errors": [asdict(item) for item in discovery_errors],
        "summary": {
            "files": len(results),
            "pass": sum(result.outcome == PASS for result in results),
            "fail": sum(result.outcome == FAIL for result in results),
            "not_applicable": sum(result.outcome == NOT_APPLICABLE for result in results),
            "error": sum(result.outcome == ERROR for result in results) + len(discovery_errors),
        },
        "authority_boundary": (
            "Documentation structure only; no truth, evidence, policy, review, release, "
            "deployment, promotion, or publication authority."
        ),
    }
    return json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n"


def _text_report(
    results: Sequence[LintResult], discovery_errors: Sequence[Finding]
) -> str:
    output: list[str] = []
    for finding in discovery_errors:
        output.append(f"ERROR -: {finding.code}: {finding.message}")
    for result in results:
        if result.outcome == PASS:
            output.append(f"PASS {result.path}: separate authority and capability-maturity axes")
        elif result.outcome == NOT_APPLICABLE:
            output.append(f"SKIP {result.path}: opt-in marker absent")
        else:
            for finding in result.findings:
                location = f":{finding.line}" if finding.line is not None else ""
                output.append(
                    f"{result.outcome} {result.path}{location}: {finding.code}: {finding.message}"
                )
    output.append(
        "SUMMARY "
        f"files={len(results)} "
        f"pass={sum(result.outcome == PASS for result in results)} "
        f"fail={sum(result.outcome == FAIL for result in results)} "
        f"not_applicable={sum(result.outcome == NOT_APPLICABLE for result in results)} "
        f"error={sum(result.outcome == ERROR for result in results) + len(discovery_errors)}"
    )
    output.append("BOUNDARY structural documentation QA only; no truth or publication authority")
    return "\n".join(output) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Check opted-in Markdown assessments for separate authority/epistemic "
            "posture and capability-maturity rows."
        )
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files or directories")
    parser.add_argument(
        "--require-marker",
        action="store_true",
        help="fail when an explicitly supplied Markdown file does not opt in",
    )
    parser.add_argument(
        "--format", choices=("text", "json"), default="text", help="deterministic output format"
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths, discovery_errors = discover_markdown(args.paths)
    results = tuple(
        lint_path(path, require_marker=args.require_marker) for path in paths
    )
    report = (
        _json_report(results, discovery_errors)
        if args.format == "json"
        else _text_report(results, discovery_errors)
    )
    sys.stdout.write(report)
    outcome = _aggregate_outcome(results, discovery_errors)
    return 2 if outcome == ERROR else 1 if outcome == FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
