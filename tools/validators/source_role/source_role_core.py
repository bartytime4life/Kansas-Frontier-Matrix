"""Bounded I/O, schema, vocabulary, and identity helpers for source-role validation."""
from __future__ import annotations

import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import compute_spec_hash  # noqa: E402

REQUEST_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_role_use_request.schema.json"
DESCRIPTOR_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_role_use_request"
BASE_PATH = FIXTURE_ROOT / "base.json"
CASES_PATH = FIXTURE_ROOT / "cases.json"
PROFILE = "kfm.source-role-use-request.v1"
VALIDATOR = {"name": "validate_source_role", "version": "1.0.0"}
MAX_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_JSON_NODES = 20_000
MAX_JSON_DEPTH = 64
EXIT_CODES = {"PASS": 0, "ERROR": 2, "HOLD": 3, "RESTRICT": 4, "ABSTAIN": 5, "DENY": 6}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    severity: str


@dataclass(frozen=True)
class Evaluation:
    outcome: str
    findings: tuple[Finding, ...]
    report: Mapping[str, Any]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _bounded(value: Any) -> bool:
    pending: list[tuple[Any, int]] = [(value, 0)]
    count = 0
    while pending:
        current, depth = pending.pop()
        count += 1
        if count > MAX_JSON_NODES or depth > MAX_JSON_DEPTH:
            return False
        if isinstance(current, dict):
            pending.extend((item, depth + 1) for item in current.values())
        elif isinstance(current, list):
            pending.extend((item, depth + 1) for item in current)
    return True


def load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("input exceeds 4 MiB")
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_object,
        parse_constant=_reject_nonfinite,
        parse_float=_parse_float,
    )
    if not isinstance(value, dict) or not _bounded(value):
        raise ValueError("input must be a bounded JSON object")
    return value


def _load_schema(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(value)
    return value


def request_validator() -> Draft202012Validator:
    return Draft202012Validator(_load_schema(REQUEST_SCHEMA_PATH), format_checker=FormatChecker())


def descriptor_validator() -> Draft202012Validator:
    return Draft202012Validator(_load_schema(DESCRIPTOR_SCHEMA_PATH), format_checker=FormatChecker())


def descriptor_vocabularies() -> dict[str, frozenset[str]]:
    schema = _load_schema(DESCRIPTOR_SCHEMA_PATH)
    defs = schema.get("$defs", {})
    return {
        "source_role": frozenset(defs.get("source_role", {}).get("enum", [])),
        "authority_rank": frozenset(defs.get("authority_rank", {}).get("enum", [])),
        "claim_role": frozenset(defs.get("claim_role", {}).get("enum", [])),
    }


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def schema_findings(validator: Draft202012Validator, value: Mapping[str, Any], code: str, prefix: str) -> list[Finding]:
    errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding(code, prefix + _pointer(error.absolute_path), "error")
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", prefix or "/", "error"))
    return findings


def sorted_unique_strings(value: Any, *, allow_empty: bool = True) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) and bool(item) for item in value)
        and value == sorted(value)
        and len(value) == len(set(value))
    )


def identity_projection(packet: Mapping[str, Any]) -> dict[str, Any]:
    use = copy.deepcopy(packet.get("use", {}))
    if isinstance(use, dict):
        use.pop("request_id", None)
    return {
        "profile": packet.get("profile"),
        "descriptor": copy.deepcopy(packet.get("descriptor")),
        "use": use,
    }


def expected_request_id(packet: Mapping[str, Any]) -> str:
    digest = compute_spec_hash(identity_projection(packet)).split(":", 1)[1]
    return f"kfm:source-role-use:{digest}"


def report_for(packet: Mapping[str, Any] | None, outcome: str, findings: Iterable[Finding]) -> dict[str, Any]:
    request_id = None
    if isinstance(packet, dict) and isinstance(packet.get("use"), dict):
        request_id = packet["use"].get("request_id")
    return {
        "profile": "kfm.source-role-use-assessment.v1",
        "validator": VALIDATOR,
        "request_id": request_id,
        "outcome": outcome,
        "findings": [finding.__dict__ for finding in sorted(set(findings))],
        "authority_created": False,
        "descriptor_mutated": False,
        "source_activated": False,
        "evidence_created": False,
        "policy_decided": False,
        "review_approved": False,
        "release_created": False,
        "publication_created": False,
    }
