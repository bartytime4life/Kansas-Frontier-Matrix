#!/usr/bin/env python3
"""Validate bounded structural invariants for critical KFM Markdown.

This standard-library checker is deterministic, local-only, and read-only. It
does not interpret document claims or grant governance, review, or release
authority.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Sequence


PROFILE = "kfm.docs.critical-structure.v1"
DEFAULT_DOCUMENTS = ("CONTRIBUTING.md",)
EXPECTED_H1 = {"CONTRIBUTING.md": "Contributing to Kansas Frontier Matrix"}
MAX_DOCUMENTS = 16
MAX_MARKDOWN_BYTES = 2_000_000

FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
FENCE_CLOSE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
ATX_HEADING_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+\s*)?$")
INTERRUPTED_HEADING_RE = re.compile(r"]\s*#{1,6}\s+\S")
CONFLICT_MARKER_RE = re.compile(r"^ {0,3}(?:<{7}|>{7}|\|{7})(?:\s|$)")


class StructureCheckError(RuntimeError):
    """A bounded input could not be inspected safely."""


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    code: str
    detail: str


@dataclass(frozen=True)
class CheckResult:
    documents: tuple[str, ...]
    findings: tuple[Finding, ...]

    @property
    def outcome(self) -> str:
        return (
            "DOC_CRITICAL_STRUCTURE_FAIL"
            if self.findings
            else "DOC_CRITICAL_STRUCTURE_PASS"
        )

    @property
    def exit_code(self) -> int:
        return 1 if self.findings else 0

    def to_payload(self) -> dict[str, object]:
        return {
            "profile": PROFILE,
            "outcome": self.outcome,
            "documents": list(self.documents),
            "counts": {
                "documents": len(self.documents),
                "findings": len(self.findings),
            },
            "findings": [asdict(finding) for finding in self.findings],
            "non_effects": {
                "network": False,
                "writes": False,
                "governance_authority": False,
                "review_authority": False,
                "release_authority": False,
            },
        }

    def to_json(self) -> str:
        return json.dumps(
            self.to_payload(), sort_keys=True, separators=(",", ":")
        )


def _strip_html_comments(
    line: str, in_comment: bool
) -> tuple[str, bool, bool]:
    """Return visible text, next comment state, and a new unclosed marker."""

    visible: list[str] = []
    cursor = 0
    opened_here = False
    inline_closures = _inline_code_closures(line)
    while cursor < len(line):
        if in_comment:
            end = line.find("-->", cursor)
            if end == -1:
                visible.append(" " * (len(line) - cursor))
                return "".join(visible), True, opened_here
            visible.append(" " * (end + 3 - cursor))
            in_comment = False
            opened_here = False
            cursor = end + 3
            continue

        if line.startswith("<!--", cursor):
            visible.append(" " * 4)
            in_comment = True
            opened_here = True
            cursor += 4
            continue

        if line[cursor] == "`" and not _is_backtick_run_escaped(line, cursor):
            closing = inline_closures.get(cursor)
            if closing is not None:
                _, close_end = closing
                visible.append(line[cursor:close_end])
                cursor = close_end
                continue

        visible.append(line[cursor])
        cursor += 1
    return "".join(visible), in_comment, opened_here


def _visible_lines(
    text: str,
) -> tuple[tuple[tuple[int, str], ...], int | None, int | None]:
    """Return lines outside comments/fences plus unclosed marker locations."""

    visible: list[tuple[int, str]] = []
    in_comment = False
    comment_start: int | None = None
    fence: tuple[str, int, int] | None = None

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if fence is not None:
            match = FENCE_CLOSE_RE.match(raw_line)
            if (
                match
                and match.group(1)[0] == fence[0]
                and len(match.group(1)) >= fence[1]
            ):
                fence = None
            continue

        if not in_comment:
            match = FENCE_OPEN_RE.match(raw_line)
            if match:
                marker = match.group(1)
                remainder = match.group(2)
                if not (marker.startswith("`") and "`" in remainder):
                    fence = (marker[0], len(marker), line_number)
                    continue

        line, next_comment, opened_here = _strip_html_comments(
            raw_line, in_comment
        )
        if opened_here and next_comment:
            comment_start = line_number
        if in_comment and not next_comment:
            comment_start = None
        in_comment = next_comment

        visible.append((line_number, line))

    fence_start = fence[2] if fence is not None else None
    return tuple(visible), fence_start, comment_start if in_comment else None


def _heading_text(raw: str) -> str:
    return " ".join(raw.strip().split())


def _backtick_runs(line: str) -> tuple[tuple[int, int], ...]:
    """Return maximal backtick runs in one bounded line in linear time."""

    runs: list[tuple[int, int]] = []
    cursor = 0
    while cursor < len(line):
        start = line.find("`", cursor)
        if start == -1:
            break
        end = start
        while end < len(line) and line[end] == "`":
            end += 1
        runs.append((start, end))
        cursor = end
    return tuple(runs)


def _inline_code_closures(line: str) -> dict[int, tuple[int, int]]:
    """Map each backtick run to the next maximal run of equal length."""

    closures: dict[int, tuple[int, int]] = {}
    next_by_length: dict[int, tuple[int, int]] = {}
    for start, end in reversed(_backtick_runs(line)):
        run_length = end - start
        closing = next_by_length.get(run_length)
        if closing is not None:
            closures[start] = closing
        next_by_length[run_length] = (start, end)
    return closures


def _is_backtick_run_escaped(line: str, start: int) -> bool:
    backslashes = 0
    cursor = start - 1
    while cursor >= 0 and line[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def _mask_inline_code(line: str) -> str:
    """Mask paired inline-code spans while preserving line length."""

    characters = list(line)
    inline_closures = _inline_code_closures(line)
    cursor = 0
    while cursor < len(line):
        if line[cursor] != "`" or _is_backtick_run_escaped(line, cursor):
            cursor += 1
            continue
        closing = inline_closures.get(cursor)
        if closing is None:
            cursor += 1
            continue
        _, close_end = closing
        for index in range(cursor, close_end):
            characters[index] = " "
        cursor = close_end
    return "".join(characters)


def inspect_text(path: str, text: str) -> tuple[Finding, ...]:
    """Inspect one already-bounded Markdown value."""

    findings: list[Finding] = []
    if not text.endswith("\n"):
        findings.append(
            Finding(
                path,
                max(1, len(text.splitlines())),
                "FINAL_NEWLINE_MISSING",
                "Document must end with a newline.",
            )
        )

    visible, fence_start, comment_start = _visible_lines(text)
    if fence_start is not None:
        findings.append(
            Finding(path, fence_start, "UNCLOSED_FENCE", "Fenced code block is not closed.")
        )
    if comment_start is not None:
        findings.append(
            Finding(path, comment_start, "UNCLOSED_HTML_COMMENT", "HTML comment is not closed.")
        )

    h1s: list[tuple[int, str]] = []
    h2s: dict[str, list[tuple[int, str]]] = {}
    masked_visible = tuple(
        (line_number, _mask_inline_code(line))
        for line_number, line in visible
    )
    conflict_open = False
    for index, (line_number, line) in enumerate(visible):
        masked_line = masked_visible[index][1]
        if CONFLICT_MARKER_RE.match(masked_line):
            findings.append(
                Finding(
                    path,
                    line_number,
                    "MERGE_CONFLICT_MARKER",
                    "An unresolved merge-conflict marker is visible.",
                )
            )
            marker = masked_line.lstrip()
            if marker.startswith("<<<<<<<"):
                conflict_open = True
            elif marker.startswith(">>>>>>>"):
                conflict_open = False
            continue
        if conflict_open:
            continue
        if INTERRUPTED_HEADING_RE.search(masked_line):
            findings.append(
                Finding(
                    path,
                    line_number,
                    "INTERRUPTED_LINK_OR_HEADING",
                    "A closing link bracket is followed by heading syntax on the same line.",
                )
            )
        match = ATX_HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = _heading_text(match.group(2))
        if level == 1:
            h1s.append((line_number, title))
        elif level == 2:
            h2s.setdefault(title.casefold(), []).append((line_number, title))

    if len(h1s) != 1:
        line = h1s[0][0] if h1s else 1
        findings.append(
            Finding(
                path,
                line,
                "H1_COUNT",
                f"Expected exactly one visible ATX H1; found {len(h1s)}.",
            )
        )
    elif path in EXPECTED_H1 and h1s[0][1] != EXPECTED_H1[path]:
        findings.append(
            Finding(
                path,
                h1s[0][0],
                "H1_TITLE_MISMATCH",
                f"Expected H1 {EXPECTED_H1[path]!r}.",
            )
        )

    expected_title = EXPECTED_H1.get(path)
    if (
        expected_title is not None
        and len(h1s) == 1
        and h1s[0][1] == expected_title
    ):
        title_token = f"# {expected_title}"
        occurrence_count = sum(
            line.count(title_token) for _, line in masked_visible
        )
        if occurrence_count != 1:
            findings.append(
                Finding(
                    path,
                    h1s[0][0] if h1s else 1,
                    "TITLE_OCCURRENCE_COUNT",
                    f"Expected one visible title token; found {occurrence_count}.",
                )
            )

    for occurrences in h2s.values():
        if len(occurrences) < 2:
            continue
        title = occurrences[0][1]
        lines = ",".join(str(item[0]) for item in occurrences)
        findings.append(
            Finding(
                path,
                occurrences[1][0],
                "DUPLICATE_H2",
                f"Visible H2 {title!r} repeats at lines {lines}.",
            )
        )

    return tuple(sorted(findings))


def _bounded_path(repo_root: Path, raw_path: str) -> Path:
    if (
        not raw_path
        or "\x00" in raw_path
        or "\\" in raw_path
        or any(
            ord(character) < 32 or ord(character) == 127
            for character in raw_path
        )
    ):
        raise StructureCheckError("Document path is empty or malformed.")
    parsed = PurePosixPath(raw_path)
    if (
        parsed.is_absolute()
        or "." in parsed.parts
        or ".." in parsed.parts
        or parsed.as_posix() != raw_path
    ):
        raise StructureCheckError(
            f"Document path must be normalized and repository-relative: {raw_path}"
        )
    unresolved = repo_root / raw_path
    if unresolved.is_symlink():
        raise StructureCheckError(f"Symbolic-link input is denied: {raw_path}")
    resolved = unresolved.resolve(strict=False)
    try:
        resolved.relative_to(repo_root)
    except ValueError as error:
        raise StructureCheckError(
            f"Document path escapes repository root: {raw_path}"
        ) from error
    if not resolved.is_file():
        raise StructureCheckError(f"Document is missing or not a file: {raw_path}")
    if resolved.suffix.casefold() not in {".md", ".markdown"}:
        raise StructureCheckError(f"Document is not Markdown: {raw_path}")
    if resolved.stat().st_size > MAX_MARKDOWN_BYTES:
        raise StructureCheckError(
            f"Document exceeds {MAX_MARKDOWN_BYTES} bytes: {raw_path}"
        )
    return resolved


def _read_bounded_markdown(path: Path, raw_path: str) -> str:
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_MARKDOWN_BYTES + 1)
    except OSError as error:
        raise StructureCheckError(
            f"Document is not readable: {raw_path}"
        ) from error
    if len(raw) > MAX_MARKDOWN_BYTES:
        raise StructureCheckError(
            f"Document exceeds {MAX_MARKDOWN_BYTES} bytes: {raw_path}"
        )
    try:
        return raw.decode("utf-8")
    except UnicodeError as error:
        raise StructureCheckError(
            f"Document is not readable UTF-8: {raw_path}"
        ) from error


def check_paths(repo_root: Path, paths: Sequence[str]) -> CheckResult:
    root = repo_root.resolve(strict=True)
    normalized = tuple(dict.fromkeys(paths))
    if not normalized or len(normalized) > MAX_DOCUMENTS:
        raise StructureCheckError(
            f"Expected between 1 and {MAX_DOCUMENTS} explicit document paths."
        )

    documents: list[str] = []
    findings: list[Finding] = []
    for raw_path in normalized:
        path = _bounded_path(root, raw_path)
        text = _read_bounded_markdown(path, raw_path)
        display = path.relative_to(root).as_posix()
        documents.append(display)
        findings.extend(inspect_text(display, text))

    return CheckResult(tuple(documents), tuple(sorted(findings)))


def _render_text(payload: dict[str, object]) -> str:
    lines = [
        f"outcome={payload['outcome']}",
        f"profile={payload['profile']}",
        f"documents={payload['counts']['documents']}",  # type: ignore[index]
        f"findings={payload['counts']['findings']}",  # type: ignore[index]
    ]
    for finding in payload["findings"]:  # type: ignore[assignment]
        lines.append(
            "{path}:{line}:{code}:{detail}".format(**finding)  # type: ignore[arg-type]
        )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate structural invariants for critical KFM Markdown."
    )
    parser.add_argument("paths", nargs="*", default=list(DEFAULT_DOCUMENTS))
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args(argv)

    try:
        result = check_paths(args.repo_root, args.paths)
        payload = result.to_payload()
        exit_code = result.exit_code
    except (OSError, StructureCheckError) as error:
        payload = {
            "profile": PROFILE,
            "outcome": "ERROR",
            "documents": [],
            "counts": {"documents": 0, "findings": 1},
            "findings": [
                {"path": ".", "line": 0, "code": "ERROR", "detail": str(error)}
            ],
            "non_effects": {
                "network": False,
                "writes": False,
                "governance_authority": False,
                "review_authority": False,
                "release_authority": False,
            },
        }
        exit_code = 2

    output = (
        json.dumps(payload, sort_keys=True, separators=(",", ":"))
        if args.format == "json"
        else _render_text(payload)
    )
    print(output)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
