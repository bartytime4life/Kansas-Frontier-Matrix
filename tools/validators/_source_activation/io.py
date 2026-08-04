"""Bounded local JSON and schema helpers for SourceActivationDecision."""

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

MAX_FILE_BYTES = 1_000_000
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
    route: str | None
    activation_state: str | None

    @property
    def ok(self) -> bool:
        return not self.findings


def mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def strings(value: object) -> set[str]:
    return {item for item in value if isinstance(item, str)} if isinstance(value, list) else set()


def _object_no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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


def read_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
    descriptor: int | None = None
    try:
        metadata = os.lstat(path)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
        if metadata.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
        descriptor = os.open(path, flags)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/", "input must be a regular file")]
        data = os.read(descriptor, MAX_FILE_BYTES + 1)
        if len(data) > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds parser budget")]
        text = data.decode("utf-8")
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/", "input could not be read safely")]
    finally:
        if descriptor is not None:
            os.close(descriptor)

    if _too_deep(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/", "input exceeds parser complexity limits")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/", "input contains a duplicate member")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/", "JSON numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/", "input is not valid UTF-8 JSON")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/", "input exceeds parser complexity limits")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/", "input root must be an object")]
    return value, []


def load_schema_validator(schema_path: Path) -> Draft202012Validator:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    return "/" + "/".join(str(part).replace("~", "~0").replace("/", "~1") for part in parts)


def schema_findings(
    validator: Draft202012Validator,
    candidate: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/", "schema evaluation exceeded limits")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator or "schema")),
    )
    findings = [
        Finding(
            "SCHEMA",
            _pointer(tuple(error.absolute_path)),
            f"schema constraint failed: {error.validator or 'schema'}",
        )
        for error in errors
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings were truncated"))
    return findings
