"""Bounded local I/O and schema helpers for SourceArtifact validation."""

from __future__ import annotations

import json
import math
import os
import stat
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

MAX_METADATA_BYTES = 1_000_000
MAX_PAYLOAD_BYTES = 50 * 1024 * 1024
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def strings(value: object) -> list[str]:
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _too_deep(text: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in text:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                return True
        elif character in "]}":
            depth -= 1
    return False


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def read_regular_bytes(path: Path, limit: int) -> tuple[bytes | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
    descriptor: int | None = None
    try:
        metadata = os.lstat(path)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
        if metadata.st_size > limit:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
        descriptor = os.open(path, flags)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
        data = os.read(descriptor, limit + 1)
        if len(data) > limit:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]
        return data, []
    except OSError:
        return None, [Finding("READ_ERROR", "/", "input could not be read safely")]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def read_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    data, findings = read_regular_bytes(path, MAX_METADATA_BYTES)
    if data is None:
        return None, findings
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        return None, [Finding("READ_ERROR", "/", "input is not UTF-8")]
    if _too_deep(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/", "input exceeds parser complexity limits")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=object_no_duplicates,
            parse_constant=reject_nonfinite,
            parse_float=finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/", "input contains a duplicate member")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/", "JSON numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/", "input is not valid JSON")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/", "input exceeds parser complexity limits")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/", "input root must be an object")]
    return value, []


def _pointer(parts: Sequence[object]) -> str:
    return "/" if not parts else "/" + "/".join(str(part).replace("~", "~0").replace("/", "~1") for part in parts)


def schema_findings(schema_path: Path, candidate: Mapping[str, object]) -> list[Finding]:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be loaded or evaluated")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator or "schema")))
    findings = [Finding("SCHEMA", _pointer(tuple(error.absolute_path)), f"schema constraint failed: {error.validator or 'schema'}") for error in errors]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings were truncated"))
    return findings
