from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from stale_scan_core import Finding, StaleScanError


OPEN_MARKER = "<!-- [KFM_META_BLOCK_V2]"
CLOSE_MARKER = "[/KFM_META_BLOCK_V2] -->"
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
KEY_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", re.ASCII)
PLACEHOLDER_PATTERN = re.compile(
    r"(?:\bTODO\b|\bTBD\b|\bUNKNOWN\b|\bUNASSIGNED\b|\bPLACEHOLDER\b|<[^>]+>)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ParsedMetadata:
    has_block: bool
    metadata: Mapping[str, Any]
    findings: tuple[Finding, ...]


def _repo_relative(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def collect_markdown_paths(repo_root: Path, inputs: Sequence[str]) -> tuple[Path, ...]:
    root = repo_root.resolve()
    if not root.exists() or not root.is_dir():
        raise StaleScanError("repository root is not a readable directory")
    collected: dict[str, Path] = {}
    for raw in inputs:
        candidate = root / raw
        try:
            lexical = candidate.resolve(strict=False)
            lexical.relative_to(root)
        except (OSError, ValueError) as exc:
            raise StaleScanError(f"input escapes repository root: {raw}") from exc
        if candidate.is_symlink():
            raise StaleScanError(f"symbolic-link input denied: {raw}")
        if not candidate.exists():
            raise StaleScanError(f"input does not exist: {raw}")
        if candidate.is_file():
            if candidate.suffix.lower() in {".md", ".markdown"}:
                collected[_repo_relative(root, candidate)] = candidate
            continue
        if not candidate.is_dir():
            raise StaleScanError(f"input is not a regular file or directory: {raw}")
        for path in sorted(candidate.rglob("*")):
            if path.is_symlink():
                continue
            if path.is_file() and path.suffix.lower() in {".md", ".markdown"}:
                try:
                    path.resolve().relative_to(root)
                except (OSError, ValueError):
                    continue
                collected[_repo_relative(root, path)] = path
    return tuple(collected[key] for key in sorted(collected))


def read_utf8(path: Path) -> str:
    if path.is_symlink():
        raise StaleScanError("symbolic-link Markdown input denied")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise StaleScanError(f"could not read UTF-8 Markdown: {path}") from exc


def _split_inline_list(value: str) -> list[str]:
    stripped = value.strip()
    if not stripped.startswith("[") or not stripped.endswith("]"):
        return [stripped] if stripped else []
    try:
        parsed = ast.literal_eval(stripped)
    except (SyntaxError, ValueError):
        inner = stripped[1:-1]
        return [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
    if isinstance(parsed, (list, tuple)):
        return [str(item).strip() for item in parsed if str(item).strip()]
    return [str(parsed).strip()] if str(parsed).strip() else []


def _parse_scalar(value: str) -> Any:
    stripped = value.strip()
    if not stripped:
        return ""
    if stripped.startswith("[") and stripped.endswith("]"):
        return _split_inline_list(stripped)
    if (
        (stripped.startswith('"') and stripped.endswith('"'))
        or (stripped.startswith("'") and stripped.endswith("'"))
    ):
        return stripped[1:-1]
    return stripped


def parse_meta_block(text: str, path: str) -> ParsedMetadata:
    openings = [match.start() for match in re.finditer(re.escape(OPEN_MARKER), text)]
    closings = [match.start() for match in re.finditer(re.escape(CLOSE_MARKER), text)]
    if not openings and not closings:
        return ParsedMetadata(False, {}, ())
    findings: list[Finding] = []
    if len(openings) != 1 or len(closings) != 1:
        findings.append(
            Finding(
                "DELEGATE_TO_META_BLOCK",
                "warn",
                path,
                "Metadata delimiters are missing or duplicated; full structure belongs to the meta-block validator.",
            )
        )
        return ParsedMetadata(False, {}, tuple(findings))
    start = openings[0] + len(OPEN_MARKER)
    end = closings[0]
    if end <= start:
        findings.append(
            Finding(
                "DELEGATE_TO_META_BLOCK",
                "warn",
                path,
                "Metadata closing delimiter precedes the opening delimiter.",
            )
        )
        return ParsedMetadata(False, {}, tuple(findings))

    metadata: dict[str, Any] = {}
    active_list_key: str | None = None
    for raw_line in text[start:end].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            stripped = raw_line.strip()
            if active_list_key and stripped.startswith("-"):
                metadata.setdefault(active_list_key, [])
                assert isinstance(metadata[active_list_key], list)
                value = stripped[1:].strip().strip("'\"")
                if value:
                    metadata[active_list_key].append(value)
                continue
            findings.append(
                Finding(
                    "DELEGATE_TO_META_BLOCK",
                    "warn",
                    path,
                    "Nested or unsupported metadata content requires the meta-block validator.",
                )
            )
            active_list_key = None
            continue
        match = KEY_PATTERN.match(raw_line.strip())
        if not match:
            findings.append(
                Finding(
                    "DELEGATE_TO_META_BLOCK",
                    "warn",
                    path,
                    "Unparseable top-level metadata content requires the meta-block validator.",
                )
            )
            active_list_key = None
            continue
        key = match.group(1).lower().replace("-", "_")
        value = match.group(2) or ""
        if key in metadata:
            findings.append(
                Finding(
                    "DELEGATE_TO_META_BLOCK",
                    "warn",
                    path,
                    f"Duplicate metadata key '{key}' requires the meta-block validator.",
                )
            )
            active_list_key = None
            continue
        parsed = _parse_scalar(value)
        if parsed == "":
            metadata[key] = []
            active_list_key = key
        else:
            metadata[key] = parsed
            active_list_key = None
    return ParsedMetadata(True, metadata, tuple(findings))


def scalar(metadata: Mapping[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = metadata.get(key)
        if value is None:
            continue
        if isinstance(value, list):
            if not value:
                continue
            return "; ".join(str(item).strip() for item in value if str(item).strip()) or None
        text = str(value).strip()
        if text:
            return text
    return None


def list_values(metadata: Mapping[str, Any], *keys: str) -> tuple[str, ...]:
    for key in keys:
        value = metadata.get(key)
        if value is None:
            continue
        if isinstance(value, list):
            return tuple(str(item).strip() for item in value if str(item).strip())
        text = str(value).strip()
        if not text:
            return ()
        return tuple(item.strip() for item in text.split(";") if item.strip())
    return ()


def owner_text(metadata: Mapping[str, Any]) -> str | None:
    return scalar(metadata, "owner", "owners")


def owner_is_placeholder(value: str | None) -> bool:
    return bool(value and PLACEHOLDER_PATTERN.search(value))


def root_segment(path: str) -> str:
    parts = PurePosixPath(path).parts
    return parts[0] if len(parts) > 1 else "."


def temporal_marker_values(metadata: Mapping[str, Any]) -> tuple[tuple[str, str], ...]:
    markers: list[tuple[str, str]] = []
    for key in ("review_due", "expires", "expiry", "temporary_until", "sunset_date"):
        value = scalar(metadata, key)
        if value:
            markers.append((key, value))
    return tuple(markers)
