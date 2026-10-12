"""Bounded JSON, schema, identity, and hash support for VerificationBacklogItem."""
from __future__ import annotations

import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = REPO_ROOT / "schemas/contracts/v1/governance/verification_backlog_item.schema.json"
MAX_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Evaluation:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def _constant(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json(path: Path) -> dict[str, object]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("input exceeds 4 MiB")
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_pairs,
        parse_constant=_constant,
        parse_float=_float,
    )
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _pointer(parts: Iterable[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_validator().iter_errors(document), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _sorted_unique(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(value)
        and len(value) == len(set(value))
    )


def _nested(document: Mapping[str, object], parent: str | None, key: str) -> object:
    if parent is None:
        return document.get(key)
    value = document.get(parent)
    return value.get(key) if isinstance(value, dict) else None


def _evidence_key(item: Mapping[str, object]) -> tuple[str, str, str]:
    return (str(item.get("mode", "")), str(item.get("locator", "")), str(item.get("title", "")))


def identity_projection(document: Mapping[str, object]) -> dict[str, object]:
    return {
        "profile": document.get("profile"),
        "priority": document.get("priority"),
        "question": document.get("question"),
        "scope": copy.deepcopy(document.get("scope")),
        "research_modes": copy.deepcopy(document.get("research_modes")),
        "basis_refs": copy.deepcopy(document.get("basis_refs")),
    }


def expected_item_id(document: Mapping[str, object]) -> str:
    digest = compute_spec_hash(identity_projection(document)).split(":", 1)[1]
    return f"kfm:verification-backlog:{digest}"


def state_projection(document: Mapping[str, object]) -> dict[str, object]:
    projection = copy.deepcopy(dict(document))
    projection.pop("spec_hash", None)
    return projection


def expected_spec_hash(document: Mapping[str, object]) -> str:
    return compute_spec_hash(state_projection(document))


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
