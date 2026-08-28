"""Shared no-network helpers for the release-support ProofPack tools."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path, PurePosixPath
from typing import Mapping

MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_COMPONENT_BYTES = 16 * 1024 * 1024
MAX_TOTAL_COMPONENT_BYTES = 128 * 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> Mapping[str, object]:
    if path.is_symlink():
        raise ValueError("symbolic-link JSON inputs are denied")
    if not path.is_file():
        raise ValueError("JSON input is not a regular file")
    if path.stat().st_size > MAX_JSON_BYTES:
        raise ValueError("JSON input exceeds the 2 MiB limit")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except (DuplicateKeyError, NonFiniteNumberError, json.JSONDecodeError) as exc:
        raise ValueError("JSON input is not safe canonical JSON") from exc
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def canonical_relative_path(raw: object) -> PurePosixPath | None:
    if not isinstance(raw, str) or not raw or raw.startswith("/") or "\\" in raw:
        return None
    path = PurePosixPath(raw)
    if str(path) != raw or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def has_symlink_component(root: Path, relative: PurePosixPath) -> bool:
    candidate = root
    for part in relative.parts:
        candidate = candidate / part
        if candidate.is_symlink():
            return True
    return False


def resolve_regular_file(root: Path, raw: object) -> Path:
    relative = canonical_relative_path(raw)
    if relative is None:
        raise ValueError("component path must be canonical and repository-relative")
    resolved_root = root.resolve(strict=True)
    if root.is_symlink() or has_symlink_component(resolved_root, relative):
        raise ValueError("symbolic-link component paths are denied")
    candidate = resolved_root.joinpath(*relative.parts)
    resolved = candidate.resolve(strict=True)
    resolved.relative_to(resolved_root)
    if not resolved.is_file():
        raise ValueError("component path is not a regular file")
    if resolved.stat().st_size > MAX_COMPONENT_BYTES:
        raise ValueError("component exceeds the 16 MiB limit")
    return resolved


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"
