"""Bounded input collection and KFM metadata-block parsing."""

from __future__ import annotations

import ast
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Sequence

from meta_block_core import (
    GIT_DIFF_RE, KEY_RE, MARKDOWN_SUFFIXES, MAX_DOCUMENTS, MAX_MARKDOWN_BYTES,
    Finding, MetaBlockError, SEVERITY_FAIL, SEVERITY_WARN, _inside, _relative,
)

def _collect_documents(root: Path, inputs: Sequence[str]) -> tuple[Path, ...]:
    found: set[Path] = set()
    for raw in inputs:
        candidate = (root / raw).resolve(strict=False)
        if not _inside(candidate, root):
            raise MetaBlockError("document input escapes repository root")
        if candidate.is_symlink():
            raise MetaBlockError("symbolic-link document input denied")
        if candidate.is_file():
            if candidate.suffix.casefold() not in MARKDOWN_SUFFIXES:
                raise MetaBlockError("explicit document input is not Markdown")
            found.add(candidate)
            continue
        if not candidate.is_dir():
            raise MetaBlockError("document input does not exist")
        for path in candidate.rglob("*"):
            if path.is_symlink():
                raise MetaBlockError("symbolic-link entry in document scope denied")
            if path.is_file() and path.suffix.casefold() in MARKDOWN_SUFFIXES:
                found.add(path.resolve())
                if len(found) > MAX_DOCUMENTS:
                    raise MetaBlockError("document scope exceeds bounded limit")
    if not found:
        raise MetaBlockError("document scope contains no Markdown")
    return tuple(sorted(found, key=lambda path: _relative(path, root)))


def _read_text(path: Path) -> str:
    try:
        if path.is_symlink() or not path.is_file():
            raise MetaBlockError("Markdown input is not a regular file")
        if path.stat().st_size > MAX_MARKDOWN_BYTES:
            raise MetaBlockError("Markdown input exceeds 5 MB")
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise MetaBlockError("Markdown input could not be read safely") from error


def _changed_documents(root: Path, selector: str | None) -> frozenset[str]:
    if selector is None:
        return frozenset()
    if not GIT_DIFF_RE.fullmatch(selector):
        raise MetaBlockError("invalid git-diff selector")
    try:
        run = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "diff",
                "--name-only",
                "--diff-filter=ACMR",
                "-z",
                selector,
                "--",
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        raise MetaBlockError("changed-file discovery failed") from error
    values: set[str] = set()
    for item in run.stdout.split(b"\0"):
        if not item:
            continue
        try:
            path = item.decode("utf-8")
        except UnicodeDecodeError as error:
            raise MetaBlockError("changed-file path is not UTF-8") from error
        if PurePosixPath(path).suffix.casefold() in MARKDOWN_SUFFIXES:
            values.add(path)
    return frozenset(values)


def _scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        return str(parsed)
    return value


def _inline_sequence(raw: str) -> tuple[str, ...] | None:
    value = raw.strip()
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


def _parse_meta_body(body: str, path: str) -> tuple[dict[str, object], list[Finding]]:
    metadata: dict[str, object] = {}
    findings: list[Finding] = []
    active_list: str | None = None
    for raw_line in body.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if stripped.startswith("-"):
            if active_list is None or not isinstance(metadata.get(active_list), list):
                findings.append(
                    Finding(
                        SEVERITY_FAIL,
                        "META_BLOCK_MALFORMED",
                        path,
                        "/",
                        "sequence item has no owning top-level field",
                    )
                )
                continue
            item = _scalar(stripped[1:].strip())
            if not item:
                findings.append(
                    Finding(
                        SEVERITY_FAIL,
                        "FIELD_VALUE_INVALID",
                        path,
                        f"/{active_list}",
                        "sequence values must be non-empty strings",
                    )
                )
            else:
                metadata[active_list].append(item)  # type: ignore[union-attr]
            continue
        if raw_line[:1].isspace():
            findings.append(
                Finding(
                    SEVERITY_WARN,
                    "META_BLOCK_UNSUPPORTED_NESTING",
                    path,
                    "/",
                    "nested mappings are outside the bounded metadata profile",
                )
            )
            active_list = None
            continue
        if ":" not in stripped:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "META_BLOCK_MALFORMED",
                    path,
                    "/",
                    "top-level metadata line is missing a key separator",
                )
            )
            active_list = None
            continue
        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        if not KEY_RE.fullmatch(key):
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "FIELD_NAME_INVALID",
                    path,
                    "/",
                    "metadata field name is outside the bounded key grammar",
                )
            )
            active_list = None
            continue
        if key in metadata:
            findings.append(
                Finding(
                    SEVERITY_FAIL,
                    "META_BLOCK_DUPLICATE_KEY",
                    path,
                    f"/{key}",
                    "metadata fields must not repeat",
                )
            )
        value = raw_value.strip()
        if not value:
            metadata[key] = []
            active_list = key
            continue
        sequence = _inline_sequence(value)
        metadata[key] = list(sequence) if sequence is not None else _scalar(value)
        active_list = None
    return metadata, findings
