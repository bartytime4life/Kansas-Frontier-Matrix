#!/usr/bin/env python3
"""Bounded JSON mechanics for synthetic public-safe domain fixture profiles.

This module owns parser, file, output, and CLI mechanics only. Domain modules
remain responsible for every semantic field and finding.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence


MAX_FIXTURE_BYTES = 1_000_000
MAX_JSON_INTEGER_DIGITS = 512
MAX_DOCUMENT_DEPTH = 64
MAX_DOCUMENT_NODES = 4_096


@dataclass(frozen=True, order=True)
class Finding:
    """A stable machine-readable finding without candidate values."""

    code: str
    path: str


Validator = Callable[[object], list[Finding]]


def is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_finite_number(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def add_finding(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def find_undeclared_fields(
    findings: set[Finding],
    candidate: dict[object, object],
    allowed_fields: frozenset[str],
    code: str,
    parent_path: str,
) -> None:
    for key in sorted(candidate, key=lambda value: (type(value).__name__, repr(value))):
        if key not in allowed_fields:
            add_finding(findings, code, f"{parent_path}.{key}")


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


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    candidate: dict[str, object] = {}
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
            raise OSError("fixture input must be a regular file")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            return stream.read(MAX_FIXTURE_BYTES + 1)
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def validate_fixture_file(path: Path | str, validator: Validator) -> list[Finding]:
    """Decode bounded, duplicate-free UTF-8 JSON and apply one domain profile."""

    fixture_path = Path(path)
    try:
        raw_bytes = _read_bounded_regular_file(fixture_path)
        if len(raw_bytes) > MAX_FIXTURE_BYTES:
            return [Finding("FIXTURE_TOO_LARGE", "$")]
        candidate = json.loads(
            raw_bytes.decode("utf-8"),
            parse_int=_parse_bounded_int,
            parse_float=_parse_finite_float,
            parse_constant=_reject_json_constant,
            object_pairs_hook=_reject_duplicate_keys,
        )
        if not _json_structure_is_bounded(candidate):
            return [Finding("FIXTURE_JSON_INVALID", "$")]
    except (OSError, UnicodeError, ValueError, RecursionError):
        return [Finding("FIXTURE_JSON_INVALID", "$")]
    return validator(candidate)


def serialize_result(scope: str, path: Path, findings: list[Finding]) -> str:
    payload = {
        "file": str(path),
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in sorted(findings)
        ],
        "scope": scope,
        "status": "FAIL" if findings else "PASS",
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def run_cli(
    *,
    argv: Sequence[str] | None,
    description: str,
    scope: str,
    validator: Callable[[Path | str], list[Finding]],
) -> int:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("files", nargs="*", type=Path, help="fixture JSON file")
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one fixture file is required", file=sys.stderr)
        return 2

    any_findings = False
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = validator(path)
        any_findings = any_findings or bool(findings)
        print(serialize_result(scope, path, findings))
    return 1 if any_findings else 0
