"""Bounded parsing and repository input helpers for documentation graph QA."""

from __future__ import annotations

import ast
import html
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Sequence
from urllib.parse import unquote, urlsplit

from document_graph_core import (
    MAX_BYTES,
    MAX_DOCS,
    MARKDOWN_SUFFIXES,
    DocumentGraphError,
    Metadata,
    RegistryEntry,
    _inside,
    _relative,
)

GIT_DIFF_RE = re.compile(r"^[0-9a-fA-F]{7,40}\.\.\.(?:HEAD|[0-9a-fA-F]{7,40})$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)(?:\s+#+\s*)?$")
META_RE = re.compile(
    r"<!--\s*\[KFM_META_BLOCK_V2\](.*?)\[/KFM_META_BLOCK_V2\]\s*-->",
    re.DOTALL | re.IGNORECASE,
)
CONTROL_RE = re.compile(
    r"<!--\s*KFM_DOCUMENT_CONTROL\s*(.*?)-->", re.DOTALL | re.IGNORECASE
)
INLINE_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))")
REF_DEF_RE = re.compile(
    r"^\s{0,3}\[([^\]\n]+)\]:\s*(?:<([^>\n]+)>|([^\s]+))\s*"
    r"(?:[\"'(].*)?$"
)
REF_USE_RE = re.compile(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]")
ROOT_PREFIXES = frozenset(
    {
        ".github", "apps", "artifacts", "catalog", "configs", "connectors",
        "contracts", "control_plane", "data", "docs", "examples", "fixtures",
        "infra", "jsonschema", "migrations", "packages", "pipeline_specs",
        "pipelines", "policies", "policy", "release", "runtime", "schemas",
        "scripts", "src", "styles", "tests", "tools", "ui",
        "viewer_templates", "web",
    }
)


def _read(path: Path) -> str:
    try:
        if path.is_symlink() or not path.is_file():
            raise DocumentGraphError("Markdown input is not a regular file")
        if path.stat().st_size > MAX_BYTES:
            raise DocumentGraphError("Markdown input exceeds 5 MB")
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise DocumentGraphError("Markdown input could not be read safely") from error


def _collect(root: Path, inputs: Sequence[str]) -> tuple[Path, ...]:
    found: set[Path] = set()
    for raw in inputs:
        candidate = (root / raw).resolve(strict=False)
        if not _inside(candidate, root):
            raise DocumentGraphError("document input escapes repository root")
        if candidate.is_symlink():
            raise DocumentGraphError("symbolic-link document input denied")
        if candidate.is_file():
            if candidate.suffix.casefold() not in MARKDOWN_SUFFIXES:
                raise DocumentGraphError("explicit document input is not Markdown")
            found.add(candidate)
            continue
        if not candidate.is_dir():
            raise DocumentGraphError("document input does not exist")
        for path in candidate.rglob("*"):
            if path.is_symlink():
                raise DocumentGraphError("symbolic-link entry in document scope denied")
            if path.is_file() and path.suffix.casefold() in MARKDOWN_SUFFIXES:
                found.add(path.resolve())
                if len(found) > MAX_DOCS:
                    raise DocumentGraphError("document scope exceeds bounded limit")
    if not found:
        raise DocumentGraphError("document scope contains no Markdown")
    return tuple(sorted(found, key=lambda path: _relative(path, root)))


def _visible_lines(text: str) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    fence: str | None = None
    in_comment = False
    for number, raw in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(raw)
        if match:
            marker = match.group(1)[0]
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence:
            continue
        line, cursor, visible = raw, 0, []
        while cursor < len(line):
            if in_comment:
                end = line.find("-->", cursor)
                if end < 0:
                    cursor = len(line)
                    break
                in_comment, cursor = False, end + 3
                continue
            start = line.find("<!--", cursor)
            if start < 0:
                visible.append(line[cursor:])
                break
            visible.append(line[cursor:start])
            in_comment, cursor = True, start + 4
        value = "".join(visible)
        value = re.sub(r"`+[^`]*`+", "", value)
        result.append((number, value))
    return result


def extract_links(text: str) -> tuple[tuple[int, str], ...]:
    lines = _visible_lines(text)
    definitions: dict[str, str] = {}
    definition_lines: set[int] = set()
    for number, line in lines:
        match = REF_DEF_RE.match(line)
        if match:
            label = " ".join(match.group(1).casefold().split())
            definitions.setdefault(label, match.group(2) or match.group(3) or "")
            definition_lines.add(number)
    links: list[tuple[int, str]] = []
    for number, line in lines:
        links.extend(
            (number, match.group(1) or match.group(2) or "")
            for match in INLINE_LINK_RE.finditer(line)
        )
        if number in definition_lines:
            continue
        for match in REF_USE_RE.finditer(line):
            label = match.group(2) or match.group(1)
            target = definitions.get(" ".join(label.casefold().split()))
            if target:
                links.append((number, target))
    return tuple(links)


def _scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        try:
            return str(ast.literal_eval(value))
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def _sequence(value: str) -> tuple[str, ...] | None:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError):
        parsed = None
    if isinstance(parsed, (list, tuple)):
        return tuple(str(item).strip() for item in parsed if str(item).strip())
    inner = value[1:-1].strip()
    return tuple(_scalar(item) for item in inner.split(",") if item.strip())


def _metadata_values(body: str) -> tuple[dict[str, object], tuple[str, ...]]:
    values: dict[str, object] = {}
    warnings: set[str] = set()
    active: str | None = None
    for raw in body.splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("-") and active:
            item = _scalar(stripped[1:].strip())
            if item and isinstance(values.get(active), list):
                values[active].append(item)  # type: ignore[union-attr]
            continue
        if ":" not in stripped:
            warnings.add("META_BLOCK_UNSUPPORTED_NESTING")
            continue
        key, raw_value = stripped.split(":", 1)
        key, raw_value = key.strip(), raw_value.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", key):
            warnings.add("META_BLOCK_INVALID_KEY")
            active = None
            continue
        if key in values:
            warnings.add("META_BLOCK_DUPLICATE_KEY")
        if not raw_value:
            values[key], active = [], key
            continue
        sequence = _sequence(raw_value)
        values[key] = list(sequence) if sequence is not None else _scalar(raw_value)
        active = None
    return values, tuple(sorted(warnings))


def _as_sequence(value: object) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return (value.strip(),) if isinstance(value, str) and value.strip() else ()


def parse_metadata(text: str) -> Metadata:
    match, source = META_RE.search(text), "KFM_META_BLOCK_V2"
    if not match:
        match, source = CONTROL_RE.search(text), "KFM_DOCUMENT_CONTROL"
    if not match:
        return Metadata(None, None, None, None, None, None, None, (), (), (), ())
    values, warnings = _metadata_values(match.group(1))
    doc_id = values.get("doc_id") or values.get("document_id")
    owners = _as_sequence(values.get("owner") or values.get("owners"))

    def string(key: str) -> str | None:
        value = values.get(key)
        return value.strip() if isinstance(value, str) and value.strip() else None

    return Metadata(
        source,
        doc_id.strip() if isinstance(doc_id, str) and doc_id.strip() else None,
        string("title"), string("type"), string("status"),
        "; ".join(owners) if owners else None, string("policy_label"),
        _as_sequence(values.get("related")),
        _as_sequence(values.get("supersedes")),
        _as_sequence(values.get("superseded_by")), warnings,
    )


def _first_heading(text: str) -> str | None:
    for _, line in _visible_lines(text):
        match = HEADING_RE.match(line)
        if match:
            return html.unescape(re.sub(r"[`*_~]", "", match.group(1))).strip()
    return None


def _target(root: Path, source: Path, raw: str) -> tuple[Path | None, str]:
    value = html.unescape(raw.strip())
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith("//"):
        return None, "external"
    decoded = unquote(parsed.path).replace("\\", "/")
    if not decoded:
        return source, "self"
    if "\x00" in decoded:
        return None, "invalid"
    if decoded.startswith("/"):
        candidate = root / decoded.lstrip("/")
    else:
        parts = PurePosixPath(decoded).parts
        repo_candidate, source_candidate = root / decoded, source.parent / decoded
        candidate = (
            repo_candidate
            if (parts and parts[0] in ROOT_PREFIXES) or repo_candidate.exists()
            else source_candidate
        )
    resolved = candidate.resolve(strict=False)
    if not _inside(resolved, root):
        return resolved, "escape"
    if resolved.is_dir() and (resolved / "README.md").is_file():
        resolved = (resolved / "README.md").resolve()
    return resolved, "local"


def _registry(path: Path) -> tuple[tuple[RegistryEntry, ...], tuple[str, ...]]:
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 2_000_000:
            raise DocumentGraphError("document registry is not a bounded regular file")
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise DocumentGraphError("document registry could not be read") from error
    in_entries, current = False, None
    raw_entries: list[dict[str, str]] = []
    warnings: set[str] = set()

    def flush() -> None:
        nonlocal current
        if current is not None:
            raw_entries.append(current)
        current = None

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not in_entries:
            in_entries = stripped == "entries:"
            continue
        if not raw.startswith(" "):
            flush()
            break
        if raw.startswith("  - "):
            flush()
            current = {}
            fragment = raw[4:].strip()
        elif raw.startswith("    ") and current is not None:
            fragment = stripped
        else:
            warnings.add("REGISTRY_UNSUPPORTED_NESTING")
            continue
        if fragment:
            if ":" not in fragment:
                warnings.add("REGISTRY_UNSUPPORTED_ENTRY")
                continue
            key, value = fragment.split(":", 1)
            if key.strip() in current:
                warnings.add("REGISTRY_DUPLICATE_KEY")
            current[key.strip()] = _scalar(value)
    flush()
    entries: list[RegistryEntry] = []
    for item in raw_entries:
        doc_id, target = item.get("doc_id", "").strip(), item.get("path", "").strip()
        if not doc_id or not target:
            warnings.add("REGISTRY_ENTRY_INCOMPLETE")
            continue
        entries.append(RegistryEntry(doc_id, target))
    return tuple(entries), tuple(sorted(warnings))


def _changed(root: Path, selector: str | None) -> frozenset[str]:
    if selector is None:
        return frozenset()
    if not GIT_DIFF_RE.fullmatch(selector):
        raise DocumentGraphError("invalid git-diff selector")
    try:
        run = subprocess.run(
            ["git", "-C", str(root), "diff", "--name-only", "--diff-filter=ACMR", "-z", selector, "--"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        raise DocumentGraphError("changed-file discovery failed") from error
    return frozenset(item.decode("utf-8") for item in run.stdout.split(b"\0") if item)
