"""Deterministic RFC 8785 JCS + SHA-256 helpers for KFM ``spec_hash``.

This module computes and compares content identity only. It creates no source,
evidence, policy, review, promotion, release, publication, or public-use authority.
Pre-canonicalization transforms such as rounding, projection, or field selection
remain the responsibility of the calling object-family contract.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import math
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import rfc8785

SPEC_HASH_PREFIX = "sha256:"
SPEC_HASH_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
CANONICALIZATION_PROFILE = "RFC8785-JCS"
HASH_ALGORITHM = "SHA-256"
MAX_JSON_BYTES = 1_000_000
MAX_JSON_INTEGER_DIGITS = 512
MAX_DOCUMENT_DEPTH = 64
MAX_DOCUMENT_NODES = 4_096


class SpecHashError(ValueError):
    """Base error for bounded spec-hash operations."""


class JsonInputError(SpecHashError):
    """Raised when a JSON input cannot be read or parsed safely."""


class CanonicalizationFailure(SpecHashError):
    """Raised when a value is outside the admitted RFC 8785 JSON domain."""


class SpecHashFormatError(SpecHashError):
    """Raised when a stored hash does not match the current executable grammar."""


@dataclass(frozen=True)
class VerificationResult:
    """Deterministic comparison result for one subject and stored hash."""

    expected: str
    actual: str

    @property
    def matches(self) -> bool:
        return hmac.compare_digest(self.expected, self.actual)


def _parse_bounded_int(raw_value: str) -> int:
    if len(raw_value.lstrip("-")) > MAX_JSON_INTEGER_DIGITS:
        raise ValueError("JSON integer exceeds the configured digit limit")
    return int(raw_value)


def _parse_finite_float(raw_value: str) -> float:
    value = float(raw_value)
    if not math.isfinite(value):
        raise ValueError("JSON number is not finite")
    return value


def _reject_json_constant(_raw_value: str) -> None:
    raise ValueError("non-standard JSON numeric constant")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    candidate: dict[str, Any] = {}
    for key, value in pairs:
        if key in candidate:
            raise ValueError("duplicate JSON object key")
        candidate[key] = value
    return candidate


def _json_structure_is_bounded(candidate: object) -> bool:
    pending = [(candidate, 0)]
    visited = 0
    while pending:
        value, depth = pending.pop()
        visited += 1
        if visited > MAX_DOCUMENT_NODES or depth > MAX_DOCUMENT_DEPTH:
            return False
        if isinstance(value, dict):
            if len(value) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((child, depth + 1) for child in value.values())
        elif isinstance(value, list):
            if len(value) > MAX_DOCUMENT_NODES - visited:
                return False
            pending.extend((child, depth + 1) for child in value)
    return True


def _read_bounded_regular_file(path: Path) -> bytes:
    flags = os.O_RDONLY
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NONBLOCK", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)

    descriptor = os.open(path, flags)
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise OSError("input must be a regular file")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            return stream.read(MAX_JSON_BYTES + 1)
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def load_json_file(path: Path | str) -> Any:
    """Load bounded, duplicate-free UTF-8 JSON from a regular non-symlink file."""

    input_path = Path(path)
    try:
        raw_bytes = _read_bounded_regular_file(input_path)
        if len(raw_bytes) > MAX_JSON_BYTES:
            raise JsonInputError("JSON input exceeds the configured byte limit")
        candidate = json.loads(
            raw_bytes.decode("utf-8"),
            parse_int=_parse_bounded_int,
            parse_float=_parse_finite_float,
            parse_constant=_reject_json_constant,
            object_pairs_hook=_reject_duplicate_keys,
        )
        if not _json_structure_is_bounded(candidate):
            raise JsonInputError("JSON input exceeds structural limits")
        return candidate
    except JsonInputError:
        raise
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        raise JsonInputError("JSON input could not be read safely") from exc


def canonicalize_json(value: Any) -> bytes:
    """Return RFC 8785 JCS bytes without applying implicit normalization."""

    try:
        return rfc8785.dumps(value)
    except (
        rfc8785.CanonicalizationError,
        TypeError,
        ValueError,
        OverflowError,
        RecursionError,
    ) as exc:
        raise CanonicalizationFailure(
            "value is outside the admitted RFC 8785 canonicalization domain"
        ) from exc


def compute_spec_hash(value: Any) -> str:
    """Compute the current KFM executable ``sha256:<hex>`` spec-hash value."""

    digest = hashlib.sha256(canonicalize_json(value)).hexdigest()
    return f"{SPEC_HASH_PREFIX}{digest}"


def is_valid_spec_hash(value: object) -> bool:
    """Return whether ``value`` matches the current executable hash grammar."""

    return isinstance(value, str) and SPEC_HASH_PATTERN.fullmatch(value) is not None


def verify_spec_hash(value: Any, expected: str) -> VerificationResult:
    """Recompute a subject hash and compare it to a stored value."""

    if not is_valid_spec_hash(expected):
        raise SpecHashFormatError("stored spec_hash does not match the current grammar")
    return VerificationResult(expected=expected, actual=compute_spec_hash(value))
