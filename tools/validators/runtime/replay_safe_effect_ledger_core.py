"""Shared parsing, schema, identity, and value helpers for the ledger validator."""
from __future__ import annotations

import json
import math
import os
import stat
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for item in (REPO_ROOT, HASH_SRC):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/runtime/replay_safe_effect_ledger.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/replay_safe_effect_ledger"
MANIFEST_PATH = FIXTURE_ROOT / "expected_findings_manifest.json"
SCOPE = "runtime.replay_safe_effect_ledger_candidate"
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
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    ledger_id: str | None = None


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _constant(_value: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_depth_exceeded(value: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in value:
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


def _read_bounded_regular_file(path: Path) -> tuple[str | None, list[Finding]]:
    if _has_symlink_component(path):
        return None, [Finding("UNSAFE_FILE", "/")]
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
        )
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, [Finding("UNSAFE_FILE", "/")]
        if metadata.st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        encoded = os.read(descriptor, MAX_FILE_BYTES + 1)
        if len(encoded) > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [Finding("READ_ERROR", "/")]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def load_candidate(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    text, findings = _read_bounded_regular_file(path)
    if text is None:
        return None, findings
    if _json_depth_exceeded(text):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    try:
        value = json.loads(
            text,
            object_pairs_hook=_pairs,
            parse_constant=_constant,
            parse_float=_float,
        )
    except DuplicateKeyError:
        return None, [Finding("DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("INVALID_JSON", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_TYPE", "/")]
    return value, []


def _pointer(parts: Sequence[object]) -> str:
    return "/" if not parts else "/" + "/".join(
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    )


def schema_findings(candidate: Mapping[str, object]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    try:
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path)))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (
                _pointer(tuple(error.absolute_path)),
                str(error.validator),
            ),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def records(value: object) -> list[Mapping[str, object]]:
    return [item for item in value if isinstance(item, Mapping)] if isinstance(value, list) else []


def strings(value: object) -> list[str]:
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def event_projection(event: Mapping[str, object]) -> dict[str, object]:
    return {
        key: event[key]
        for key in ("event_type", "subject_ref", "occurred_at", "payload_digest")
    }


def effect_projection(
    event: Mapping[str, object], effect: Mapping[str, object]
) -> dict[str, object]:
    return {
        "event_id": event["event_id"],
        "subject_ref": event["subject_ref"],
        "effect_type": effect["effect_type"],
        "idempotency_scope": effect["idempotency_scope"],
    }
