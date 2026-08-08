"""Strict no-network I/O helpers for the path-alias validator."""

from __future__ import annotations

import hashlib
import json
import math
from datetime import date
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

from .path_alias_model import (
    DuplicateKeyError,
    Finding,
    MAX_FILE_BYTES,
    MAX_SCHEMA_FINDINGS,
    NonFiniteNumberError,
    SCHEMA_PATH,
)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_nonfinite,
            parse_float=parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_COMPATIBLE_YAML_REQUIRED", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()  # nosec B324 - Git object identity, not security


def load_root_registry(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    value, findings = read_object(path)
    if value is None:
        return None, [Finding("ROOT_REGISTRY_UNAVAILABLE", "/root_registry")]
    entry_defaults = value.get("entry_defaults")
    class_defaults = value.get("class_defaults")
    resolved_roots: list[Any] = []
    for raw in array(value.get("roots")):
        if not isinstance(raw, Mapping):
            resolved_roots.append(raw)
            continue
        merged: dict[str, Any] = {}
        if isinstance(entry_defaults, Mapping):
            merged.update(entry_defaults)
        if isinstance(class_defaults, Mapping):
            class_profile = class_defaults.get(raw.get("class"), {})
            if isinstance(class_profile, Mapping):
                merged.update(class_profile)
        merged.update(raw)
        resolved_roots.append(merged)
    resolved = dict(value)
    resolved["roots"] = resolved_roots
    return resolved, findings


def root_for_path(path: str, by_path: Mapping[str, Mapping[str, Any]]) -> Mapping[str, Any] | None:
    matches = [entry for root, entry in by_path.items() if path.startswith(root)]
    return max(matches, key=lambda entry: len(str(entry.get("path", "")))) if matches else None


def parse_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None
