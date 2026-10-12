"""Bounded input, schema, and deterministic identity helpers."""
from __future__ import annotations

import copy
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "packages/hashing/src"))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/governance/published_language_review.schema.json"
CASES = ROOT / "fixtures/contracts/v1/governance/published_language_review/cases.json"
SCOPE = "published-language-review-fixture-only-v1"
MAX_BYTES = 1_048_576
FALSE_EFFECTS = {
    key: False
    for key in (
        "schema_changed",
        "api_changed",
        "context_map_changed",
        "adopted",
        "released",
        "published",
    )
}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
    "PUBLISHED_LANGUAGE_REVIEW_ID_MISMATCH",
    "FIXTURE_MANIFEST_INVALID",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _bad_number(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_bad_number,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError):
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(
                schema, format_checker=FormatChecker()
            ).iter_errors(candidate),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("review_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_review_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return f"published-language-review:{digest[:24]}"


def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate))
    result["spec_hash"] = canonical_spec_hash(result)
    result["review_id"] = expected_review_id(result)
    return result
