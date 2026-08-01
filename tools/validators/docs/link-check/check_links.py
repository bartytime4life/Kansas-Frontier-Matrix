#!/usr/bin/env python3
"""Validate local inline Markdown links without making network requests.

The checker is documentation QA only. It verifies repository-local file,
directory, image, and fragment targets. External targets are recorded as
unverified information and are never requested.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence
from urllib.parse import unquote, urlsplit


MAX_MARKDOWN_BYTES = 5_000_000
MARKDOWN_SUFFIXES = {".md", ".markdown"}
FAILURE_OUTCOMES = {
    "ANCHOR_MISSING",
    "ERROR",
    "LOCAL_TARGET_MISSING",
    "PATH_ESCAPE",
}
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
ATX_HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)(?:\s+#+\s*)?$")
SETEXT_RE = re.compile(r"^\s{0,3}(=+|-+)\s*$")
HTML_ANCHOR_RE = re.compile(
    r"<[^>]+\s(?:id|name)\s*=\s*([\"'])(.*?)\1",
    re.IGNORECASE,
)
REFERENCE_DEFINITION_RE = re.compile(
    r"^\s{0,3}\[([^\]\n]{1,999})\]:[ \t]*"
    r"(?:<([^>\n]+)>|([^\s]+))"
    r"(?:[ \t]+(?:\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'|"
    r"\((?:[^()\\]|\\.)*\)))?[ \t]*$"
)
GIT_DIFF_RE = re.compile(
    r"^[0-9a-fA-F]{7,40}\.\.\.(?:HEAD|[0-9a-fA-F]{7,40})$"
)


class LinkCheckError(RuntimeError):
    """A bounded input or repository operation could not be completed safely."""


@dataclass(frozen=True, order=True)
class Finding:
    source: str
    line: int
    outcome: str
    target: str
    detail: str
    image: bool = False


@dataclass(frozen=True)
class CheckResult:
    outcome: str
    checked_documents: int
    checked_local_targets: int
    external_targets_unverified: int
    findings: tuple[Finding, ...]
    scope: str

    @property
    def exit_code(self) -> int:
        return 1 if any(item.outcome in FAILURE_OUTCOMES for item in self.findings) else 0

    def to_json(self) -> str:
        payload = {
            "outcome": self.outcome,
            "scope": self.scope,
            "checked_documents": self.checked_documents,
            "checked_local_targets": self.checked_local_targets,
            "external_targets_unverified": self.external_targets_unverified,
            "findings": [asdict(item) for item in self.findings],
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"))


@dataclass(frozen=True)
class LinkReference:
    line: int
    target: str
    image: bool


@dataclass(frozen=True)
class ReferenceDefinition:
    line: int
    target: str


def _visible_markdown_lines(text: str) -> Iterator[tuple[int, str]]:
    """Yield lines outside fenced code and HTML comments with markup intact."""

    fence: str | None = None
    in_comment = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        fence_match = FENCE_RE.match(raw_line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is not None:
            continue

        line = raw_line
        visible: list[str] = []
        cursor = 0
        while cursor < len(line):
            if in_comment:
                end = line.find("-->", cursor)
                if end == -1:
                    cursor = len(line)
                    break
                in_comment = False
                cursor = end + 3
                continue
            start = line.find("<!--", cursor)
            if start == -1:
                visible.append(line[cursor:])
                break
            visible.append(line[cursor:start])
            cursor = start + 4
            in_comment = True

        yield line_number, "".join(visible)


def _masked_markdown_lines(text: str) -> Iterator[tuple[int, str]]:
    """Yield link-visible Markdown lines with inline code spans masked."""

    for line_number, line in _visible_markdown_lines(text):
        yield line_number, _mask_code_spans(line)


def _mask_code_spans(line: str) -> str:
    chars = list(line)
    cursor = 0
    while cursor < len(line):
        if line[cursor] != "`" or (cursor and line[cursor - 1] == "\\"):
            cursor += 1
            continue
        end_run = cursor
        while end_run < len(line) and line[end_run] == "`":
            end_run += 1
        marker = line[cursor:end_run]
        closing = line.find(marker, end_run)
        if closing == -1:
            cursor = end_run
            continue
        for index in range(cursor, closing + len(marker)):
            chars[index] = " "
        cursor = closing + len(marker)
    return "".join(chars)


def _inline_links(line: str, line_number: int) -> Iterator[LinkReference]:
    cursor = 0
    while cursor < len(line):
        bracket = line.find("[", cursor)
        if bracket == -1:
            return
        image = bracket > 0 and line[bracket - 1] == "!"
        if bracket > 0 and line[bracket - 1] == "\\":
            cursor = bracket + 1
            continue
        label_end = line.find("]", bracket + 1)
        if label_end == -1 or label_end + 1 >= len(line) or line[label_end + 1] != "(":
            cursor = bracket + 1
            continue

        target_start = label_end + 2
        while target_start < len(line) and line[target_start].isspace():
            target_start += 1
        if target_start >= len(line):
            return

        if line[target_start] == "<":
            target_end = line.find(">", target_start + 1)
            if target_end == -1:
                cursor = label_end + 1
                continue
            target = line[target_start + 1 : target_end]
            closing = line.find(")", target_end + 1)
            cursor = closing + 1 if closing != -1 else target_end + 1
        else:
            depth = 1
            index = target_start
            target_end = target_start
            while index < len(line):
                character = line[index]
                if character == "\\":
                    index += 2
                    target_end = index
                    continue
                if character == "(":
                    depth += 1
                elif character == ")":
                    depth -= 1
                    if depth == 0:
                        break
                elif character.isspace() and depth == 1:
                    break
                target_end = index + 1
                index += 1
            target = line[target_start:target_end]
            cursor = max(index + 1, label_end + 2)

        if target:
            yield LinkReference(line=line_number, target=target, image=image)


def _normalize_reference_label(value: str) -> str:
    """Normalize a bounded GFM reference label for deterministic matching."""

    return " ".join(html.unescape(value).casefold().split())


def _reference_definitions(
    text: str,
) -> tuple[dict[str, ReferenceDefinition], frozenset[int]]:
    """Collect first-wins, single-line reference definitions outside code/comments."""

    definitions: dict[str, ReferenceDefinition] = {}
    definition_lines: set[int] = set()
    for line_number, line in _visible_markdown_lines(text):
        match = REFERENCE_DEFINITION_RE.fullmatch(line)
        if not match or match.group(1).lstrip().startswith("^"):
            continue
        label = _normalize_reference_label(match.group(1))
        if not label:
            continue
        target = match.group(2) or match.group(3)
        definitions.setdefault(
            label,
            ReferenceDefinition(line=line_number, target=target),
        )
        definition_lines.add(line_number)
    return definitions, frozenset(definition_lines)


def _closing_bracket(line: str, start: int, *, allow_nested: bool) -> int | None:
    depth = 1
    cursor = start
    while cursor < len(line):
        character = line[cursor]
        if character == "\\":
            cursor += 2
            continue
        if allow_nested and character == "[":
            depth += 1
        elif character == "]":
            depth -= 1
            if depth == 0:
                return cursor
        cursor += 1
    return None


def _reference_links(
    line: str,
    line_number: int,
    definitions: dict[str, ReferenceDefinition],
) -> Iterator[LinkReference]:
    """Yield bounded full, collapsed, and defined shortcut reference links."""

    cursor = 0
    while cursor < len(line):
        bracket = line.find("[", cursor)
        if bracket == -1:
            return
        if bracket > 0 and line[bracket - 1] == "\\":
            cursor = bracket + 1
            continue

        label_end = _closing_bracket(line, bracket + 1, allow_nested=True)
        if label_end is None:
            return
        link_text = line[bracket + 1 : label_end]
        image = bracket > 0 and line[bracket - 1] == "!"
        following = label_end + 1

        if following < len(line) and line[following] == "(":
            cursor = following + 1
            continue

        if following < len(line) and line[following] == "[":
            reference_end = _closing_bracket(
                line,
                following + 1,
                allow_nested=False,
            )
            if reference_end is None:
                cursor = following + 1
                continue
            reference_text = line[following + 1 : reference_end] or link_text
            label = _normalize_reference_label(reference_text)
            definition = definitions.get(label)
            if definition is not None:
                yield LinkReference(
                    line=line_number,
                    target=definition.target,
                    image=image,
                )
            cursor = reference_end + 1
            continue

        label = _normalize_reference_label(link_text)
        definition = definitions.get(label)
        if definition is not None:
            yield LinkReference(
                line=line_number,
                target=definition.target,
                image=image,
            )
        cursor = label_end + 1


def extract_links(path: Path) -> tuple[LinkReference, ...]:
    try:
        if path.stat().st_size > MAX_MARKDOWN_BYTES:
            raise LinkCheckError(
                f"Markdown input exceeds {MAX_MARKDOWN_BYTES} bytes: {path}"
            )
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise LinkCheckError(f"Cannot read Markdown input {path}: {error}") from error

    definitions, definition_lines = _reference_definitions(text)
    links: list[LinkReference] = []
    for line_number, line in _masked_markdown_lines(text):
        links.extend(_inline_links(line, line_number))
        if line_number not in definition_lines:
            links.extend(_reference_links(line, line_number, definitions))
    return tuple(links)


def _plain_heading_markup(value: str) -> str:
    """Remove supported inline markup while retaining its visible contents."""

    value = re.sub(r"!\[([^]]*)]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value)


def _heading_text(value: str) -> str:
    """Return visible heading text without treating code contents as markup."""

    parts: list[str] = []
    plain_start = 0
    cursor = 0
    while cursor < len(value):
        if value[cursor] != "`" or (cursor and value[cursor - 1] == "\\"):
            cursor += 1
            continue
        end_run = cursor
        while end_run < len(value) and value[end_run] == "`":
            end_run += 1
        marker = value[cursor:end_run]
        closing = value.find(marker, end_run)
        if closing == -1:
            cursor = end_run
            continue
        parts.append(_plain_heading_markup(value[plain_start:cursor]))
        parts.append(value[end_run:closing])
        cursor = closing + len(marker)
        plain_start = cursor

    parts.append(_plain_heading_markup(value[plain_start:]))
    return "".join(parts).strip()


def _github_slug(value: str) -> str:
    value = _heading_text(value).lower()
    return "".join(
        "-" if character == " " else character
        for character in value
        if character == " "
        or (
            not character.isspace()
            and (character.isalnum() or character in {"-", "_"})
        )
    )


def collect_anchors(path: Path) -> frozenset[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise LinkCheckError(f"Cannot read anchor target {path}: {error}") from error

    anchors: set[str] = set()
    slug_counts: dict[str, int] = {}
    previous: tuple[int, str] | None = None
    for line_number, line in _visible_markdown_lines(text):
        anchors.update(
            match.group(2)
            for match in HTML_ANCHOR_RE.finditer(_mask_code_spans(line))
        )
        heading = ATX_HEADING_RE.match(line)
        heading_text: str | None = heading.group(2) if heading else None
        if heading_text is None and previous and SETEXT_RE.match(line):
            heading_text = previous[1]
        if heading_text is not None:
            base = _github_slug(heading_text)
            if base:
                occurrence = slug_counts.get(base, 0)
                anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
                slug_counts[base] = occurrence + 1
        previous = (line_number, line) if line.strip() else None
    return frozenset(anchors)


def _is_external(target: str) -> bool:
    parsed = urlsplit(target)
    return bool(parsed.scheme or parsed.netloc or target.startswith("//"))


def _external_display(target: str) -> str:
    """Return a bounded external identifier without path, query, or credentials."""

    parsed = urlsplit(target)
    if parsed.netloc:
        host = parsed.hostname or "<invalid-host>"
        prefix = f"{parsed.scheme}:" if parsed.scheme else ""
        return f"{prefix}//{host}"
    return f"{parsed.scheme}:" if parsed.scheme else "//<external-host>"


def _relative_display(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _has_exact_case(repo_root: Path, relative: Path) -> bool:
    current = repo_root
    for part in relative.parts:
        try:
            names = {entry.name for entry in os.scandir(current)}
        except OSError:
            return False
        if part not in names:
            return False
        current = current / part
    return True


def _resolve_local_target(
    repo_root: Path,
    source: Path,
    target: str,
) -> tuple[Path | None, str, str | None]:
    parsed = urlsplit(target)
    raw_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    base = repo_root if raw_path.startswith("/") else source.parent
    candidate = base / raw_path.lstrip("/") if raw_path else source
    resolved = candidate.resolve(strict=False)
    try:
        relative = resolved.relative_to(repo_root)
    except ValueError:
        return None, fragment, "PATH_ESCAPE"
    if not resolved.exists() or not _has_exact_case(repo_root, relative):
        return resolved, fragment, "LOCAL_TARGET_MISSING"
    return resolved, fragment, None


def _normalize_inputs(repo_root: Path, paths: Iterable[str]) -> tuple[Path, ...]:
    inputs: set[Path] = set()
    for raw_path in paths:
        unresolved = repo_root / raw_path
        if unresolved.is_symlink():
            raise LinkCheckError(f"Symbolic-link Markdown input is denied: {raw_path}")
        candidate = unresolved.resolve(strict=False)
        try:
            relative = candidate.relative_to(repo_root)
        except ValueError as error:
            raise LinkCheckError(f"Input path escapes repository root: {raw_path}") from error
        if not candidate.exists() or not _has_exact_case(repo_root, relative):
            raise LinkCheckError(f"Input path is missing or case-mismatched: {raw_path}")
        if candidate.is_dir():
            for path in candidate.rglob("*"):
                if path.is_symlink():
                    raise LinkCheckError(
                        "Symbolic links are denied inside Markdown input directories: "
                        f"{_relative_display(path, repo_root)}"
                    )
                if path.is_file() and path.suffix.lower() in MARKDOWN_SUFFIXES:
                    inputs.add(path.resolve())
        elif candidate.is_file() and candidate.suffix.lower() in MARKDOWN_SUFFIXES:
            inputs.add(candidate)
        else:
            raise LinkCheckError(f"Input is not Markdown: {raw_path}")
    return tuple(sorted(inputs, key=lambda path: _relative_display(path, repo_root)))


def discover_git_diff(repo_root: Path, diff_spec: str) -> tuple[str, ...]:
    if not GIT_DIFF_RE.fullmatch(diff_spec):
        raise LinkCheckError(
            "Git diff spec must be <7-40 hex>...HEAD or <7-40 hex>...<7-40 hex>."
        )
    command = [
        "git",
        "diff",
        "--name-only",
        "--diff-filter=ACMR",
        "-z",
        diff_spec,
        "--",
        "*.md",
        "*.markdown",
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=repo_root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", b"")
        message = detail.decode("utf-8", errors="replace").strip()
        raise LinkCheckError(f"Cannot enumerate changed Markdown: {message or error}") from error
    return tuple(
        item.decode("utf-8", errors="strict")
        for item in completed.stdout.split(b"\0")
        if item
    )


def check_paths(repo_root: Path, paths: Sequence[str], *, scope: str) -> CheckResult:
    root = repo_root.resolve(strict=True)
    documents = _normalize_inputs(root, paths) if paths else ()
    findings: list[Finding] = []
    checked_local = 0
    external_count = 0
    anchor_cache: dict[Path, frozenset[str]] = {}

    for source in documents:
        source_display = _relative_display(source, root)
        for reference in extract_links(source):
            if _is_external(reference.target):
                external_count += 1
                findings.append(
                    Finding(
                        source=source_display,
                        line=reference.line,
                        outcome="EXTERNAL_TARGET_UNVERIFIED",
                        target=_external_display(reference.target),
                        detail=(
                            "External target was classified but not requested; "
                            "path, query, fragment, and credentials are omitted."
                        ),
                        image=reference.image,
                    )
                )
                continue

            checked_local += 1
            target_path, fragment, error_outcome = _resolve_local_target(
                root, source, reference.target
            )
            if error_outcome:
                findings.append(
                    Finding(
                        source=source_display,
                        line=reference.line,
                        outcome=error_outcome,
                        target=reference.target,
                        detail=(
                            "Target resolves outside the repository root."
                            if error_outcome == "PATH_ESCAPE"
                            else "Target is missing or its path casing does not match."
                        ),
                        image=reference.image,
                    )
                )
                continue

            assert target_path is not None
            anchor_path = target_path / "README.md" if target_path.is_dir() else target_path
            if fragment:
                if (
                    not anchor_path.is_file()
                    or anchor_path.suffix.lower() not in MARKDOWN_SUFFIXES
                ):
                    anchors = frozenset()
                else:
                    anchors = anchor_cache.setdefault(
                        anchor_path, collect_anchors(anchor_path)
                    )
                if fragment not in anchors:
                    findings.append(
                        Finding(
                            source=source_display,
                            line=reference.line,
                            outcome="ANCHOR_MISSING",
                            target=reference.target,
                            detail="Fragment does not match a Markdown heading or explicit HTML anchor.",
                            image=reference.image,
                        )
                    )

    ordered = tuple(sorted(findings))
    failed = any(item.outcome in FAILURE_OUTCOMES for item in ordered)
    return CheckResult(
        outcome="DOC_LINK_CHECK_FAIL" if failed else "DOC_LINK_CHECK_PASS",
        checked_documents=len(documents),
        checked_local_targets=checked_local,
        external_targets_unverified=external_count,
        findings=ordered,
        scope=scope,
    )


def render_text(result: CheckResult) -> str:
    lines = [
        (
            f"{result.outcome} scope={result.scope} "
            f"documents={result.checked_documents} "
            f"local_targets={result.checked_local_targets} "
            f"external_unverified={result.external_targets_unverified}"
        )
    ]
    for finding in result.findings:
        level = "INFO" if finding.outcome == "EXTERNAL_TARGET_UNVERIFIED" else "FAIL"
        lines.append(
            f"{level} {finding.outcome} {finding.source}:{finding.line} "
            f"target={json.dumps(finding.target)} detail={finding.detail}"
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Markdown files or directories to check")
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument(
        "--git-diff",
        help="Check added/copied/modified/renamed Markdown in <base>...HEAD",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.git_diff and args.paths:
        parser.error("paths and --git-diff are mutually exclusive")
    try:
        repo_root = Path(args.repo_root).resolve(strict=True)
        if args.git_diff:
            paths = discover_git_diff(repo_root, args.git_diff)
            scope = "changed_markdown" if paths else "changed_markdown_empty"
        else:
            paths = tuple(args.paths) if args.paths else (".",)
            scope = "explicit_or_repository_markdown"
        result = check_paths(repo_root, paths, scope=scope)
    except (LinkCheckError, OSError, UnicodeError) as error:
        payload = {
            "outcome": "ERROR",
            "detail": str(error),
        }
        if args.format == "json":
            print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        else:
            print(f"ERROR {error}", file=sys.stderr)
        return 2

    print(result.to_json() if args.format == "json" else render_text(result))
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
