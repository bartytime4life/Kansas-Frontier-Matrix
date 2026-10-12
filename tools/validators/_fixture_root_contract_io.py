"""Bounded parsing helpers for the fixture-root contract validator."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any

MAX_TEXT_BYTES = 2 * 1024 * 1024
MAX_JSON_BYTES = 4 * 1024 * 1024

REQUIRED_META = {
    "doc_id": "kfm://doc/fixtures-readme",
    "current_path": "fixtures/README.md",
    "owning_root": "fixtures/",
    "root_id": "root.fixtures",
    "readme_profile": "ROOT_FULL",
}

REQUIRED_H2 = (
    "Purpose",
    "Root class and authority owner",
    "Adoption and conformance status",
    "What belongs here and what is prohibited",
    "Inputs, outputs, and permitted writers",
    "Public exposure and sensitivity posture",
    "Mutability, retention, generation, and physical storage",
    "Validation and negative checks",
    "Owner, reviewers, and escalation path",
    "Governing ADRs, migrations, aliases, and canonical target",
    "Direct-child directory map",
    "Last evidence review and review trigger",
)

_META_BLOCK = re.compile(
    r"<!-- \[KFM_META_BLOCK_V2\]\n(?P<body>.*?)\n\[/KFM_META_BLOCK_V2\] -->",
    re.DOTALL,
)
_DIRECT_CHILD_SNAPSHOT = re.compile(
    r"\|\s*Direct-child snapshot\s*\|\s*`README\.md`\s+plus\s+"
    r"(?P<count>\d+)\s+directories(?:\s+at\s+[^|]+)?\s*\|",
)
_TREE_ENTRY = re.compile(
    r"^[\s│]*[├└]──\s+(?P<name>[A-Za-z0-9_.-]+)(?:/)?(?:\s|$)"
)
_TARGET = re.compile(r"(?m)^fixtures:\n(?P<body>(?:\t[^\n]*\n?)+)")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_text(path: Path, *, limit: int, field: str) -> tuple[str | None, str | None]:
    try:
        if path.is_symlink():
            return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file():
            return None, "INPUT_NOT_FILE"
        if path.stat().st_size > limit:
            return None, "INPUT_TOO_LARGE"
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError:
        return None, "INPUT_NOT_UTF8"
    except OSError:
        return None, "INPUT_READ_ERROR"


def read_json(path: Path, *, field: str) -> tuple[dict[str, Any] | None, str | None]:
    text, error = read_text(path, limit=MAX_JSON_BYTES, field=field)
    if text is None:
        return None, error
    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except json.JSONDecodeError:
        return None, "JSON_INVALID"
    except DuplicateKeyError:
        return None, "JSON_DUPLICATE_KEY"
    except NonFiniteNumberError:
        return None, "JSON_NONFINITE_NUMBER"
    except (RecursionError, ValueError):
        return None, "JSON_COMPLEXITY_LIMIT"
    if not isinstance(value, dict):
        return None, "JSON_ROOT_NOT_OBJECT"
    return value, None


def metadata(text: str) -> tuple[dict[str, str], str | None]:
    matches = list(_META_BLOCK.finditer(text))
    if len(matches) != 1:
        return {}, "META_BLOCK_COUNT_INVALID"
    result: dict[str, str] = {}
    for line in matches[0].group("body").splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        clean = value.strip().strip('"').strip("'")
        if clean:
            result[key.strip()] = clean
    return result, None


def headings(text: str) -> tuple[list[str], list[str]]:
    h1: list[str] = []
    h2: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        marker = re.match(r"(`{3,}|~{3,})", raw.lstrip())
        if marker:
            char = marker.group(1)[0]
            fence = char if fence is None else (None if fence == char else fence)
            continue
        if fence is not None:
            continue
        if raw.startswith("# ") and not raw.startswith("## "):
            h1.append(raw[2:].strip())
        elif raw.startswith("## ") and not raw.startswith("### "):
            h2.append(raw[3:].strip())
    return h1, h2


def direct_child_snapshot(text: str) -> int | None:
    match = _DIRECT_CHILD_SNAPSHOT.search(text)
    return None if match is None else int(match.group("count"))


def tree_entries(text: str) -> tuple[set[str] | None, str | None]:
    marker = "## Direct-child directory map"
    start = text.find(marker)
    if start < 0:
        return None, "DIRECT_CHILD_SECTION_MISSING"
    tail = text[start + len(marker) :]
    fence = re.search(r"```text\n(?P<body>.*?)\n```", tail, re.DOTALL)
    if fence is None:
        return None, "DIRECT_CHILD_TREE_MISSING"
    names = {
        match.group("name")
        for line in fence.group("body").splitlines()
        if (match := _TREE_ENTRY.match(line))
    }
    return names, None


def fixtures_target_lines(text: str) -> list[str]:
    target = _TARGET.search(text)
    return [] if target is None else target.group("body").splitlines()
