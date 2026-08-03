"""Validate KFM TemporalWindow records without network access.

The validator enforces the proposed JSON Schema and the semantic interval rule
that ``start`` must not occur after ``end`` after timezone normalization. A
passing result proves only bounded shape, timestamp syntax, timezone presence,
and interval ordering. It does not establish source truth, freshness, policy,
review, correction closure, release, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import islice
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/temporal_window.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/common/temporal_window"

MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard or overflowing number."""


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic finding that does not echo candidate values."""

    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    """Bounded result for one TemporalWindow candidate."""

    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite_number(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
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
        return None, [
            Finding("UNSAFE_FILE", "/", "candidate must be a regular file")
        ]

    descriptor: int | None = None
    flags = (
        os.O_RDONLY
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    try:
        descriptor = os.open(path, flags)
        file_stat = os.fstat(descriptor)
        if not stat.S_ISREG(file_stat.st_mode):
            return None, [
                Finding("UNSAFE_FILE", "/", "candidate must be a regular file")
            ]
        if file_stat.st_size > MAX_FILE_BYTES:
            return None, [
                Finding("FILE_TOO_LARGE", "/", "candidate exceeds the parser budget")
            ]

        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            block = os.read(descriptor, min(64 * 1024, remaining))
            if not block:
                break
            chunks.append(block)
            remaining -= len(block)
        encoded = b"".join(chunks)
        if len(encoded) > MAX_FILE_BYTES:
            return None, [
                Finding("FILE_TOO_LARGE", "/", "candidate exceeds the parser budget")
            ]
        return encoded.decode("utf-8"), []
    except (OSError, UnicodeError):
        return None, [
            Finding("READ_ERROR", "/", "candidate could not be read safely")
        ]
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    text, findings = _read_bounded_regular_file(path)
    if text is None:
        return None, findings
    if _json_depth_exceeded(text):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/",
                "candidate exceeds JSON parser complexity limits",
            )
        ]

    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, [
            Finding("DUPLICATE_KEY", "/", "candidate contains a duplicate member")
        ]
    except NonFiniteNumberError:
        return None, [
            Finding("NONFINITE_NUMBER", "/", "candidate numbers must be finite")
        ]
    except json.JSONDecodeError:
        return None, [
            Finding("INVALID_JSON", "/", "candidate is not valid UTF-8 JSON")
        ]
    except (RecursionError, ValueError):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/",
                "candidate exceeds JSON parser complexity limits",
            )
        ]

    if not isinstance(value, dict):
        return None, [
            Finding("ROOT_TYPE", "/", "candidate root must be an object")
        ]
    return value, []


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _json_pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded)


def _schema_findings(
    validator: Draft202012Validator,
    candidate: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(
            islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1)
        )
    except (RecursionError, ValueError):
        return [
            Finding(
                "SCHEMA_EVALUATION_LIMIT",
                "/",
                "schema evaluation exceeded bounded complexity limits",
            )
        ]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors[:MAX_SCHEMA_FINDINGS],
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
    )
    findings: list[Finding] = []
    for error in errors:
        keyword = str(error.validator or "schema")
        detail = f"JSON Schema keyword {keyword} failed"
        if keyword == "format":
            detail += " for date-time"
        elif keyword == "additionalProperties":
            detail += " because additional properties are closed"
        findings.append(
            Finding(
                "SCHEMA_INVALID",
                _json_pointer(tuple(error.absolute_path)),
                detail,
            )
        )
    if truncated:
        findings.append(
            Finding(
                "SCHEMA_FINDINGS_TRUNCATED",
                "/",
                "schema findings were truncated at the output limit",
            )
        )
    return findings


def _parse_aware_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    start = _parse_aware_datetime(candidate.get("start"))
    end = _parse_aware_datetime(candidate.get("end"))
    if start is None or end is None:
        return []
    if start > end:
        return [
            Finding(
                "TEMPORAL_ORDER_INVALID",
                "/end",
                "end must not precede start after timezone normalization",
            )
        ]
    return []


def validate_candidate(candidate: Mapping[str, object]) -> ValidationResult:
    """Validate one parsed TemporalWindow object."""

    try:
        validator = _load_schema_validator()
    except (OSError, UnicodeError, ValueError):
        return ValidationResult(
            (
                Finding(
                    "SCHEMA_UNAVAILABLE",
                    "/",
                    "TemporalWindow schema could not be loaded safely",
                ),
            )
        )

    findings = _schema_findings(validator, candidate)
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    """Validate one bounded local JSON file."""

    candidate, findings = _load_json_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(findings)))
    return validate_candidate(candidate)


def _finding_text(findings: Sequence[Finding]) -> str:
    return "\n".join(
        f"{finding.code} {finding.field} {finding.detail}".lower()
        for finding in findings
    )


def _expected_rejection_matches(
    expected_path: Path,
    findings: Sequence[Finding],
) -> bool:
    try:
        expected = expected_path.read_text(encoding="utf-8").strip().lower()
    except (OSError, UnicodeError):
        return False
    if not expected:
        return False

    combined = _finding_text(findings)
    normalized = combined.replace("additionalproperties", "additional properties")
    for line in (line.strip() for line in expected.splitlines()):
        if not line:
            continue
        if "|" in line:
            try:
                if re.search(line, normalized) is None:
                    return False
            except re.error:
                return False
        elif line not in normalized:
            return False
    return True


def _serialize(
    path: Path,
    findings: Sequence[Finding],
    *,
    expected_rejection: bool = False,
) -> str:
    if findings and expected_rejection:
        outcome = "EXPECTED_REJECTION"
    else:
        outcome = "PASS" if not findings else "FAIL"
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {
                    "code": finding.code,
                    "field": finding.field,
                    "detail": finding.detail,
                }
                for finding in findings
            ],
            "outcome": outcome,
            "scope": "temporal-window-shape-and-order-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.json"), key=lambda path: path.as_posix())


def _validate_fixture_lane(
    directory: Path,
    *,
    expect_valid: bool,
) -> bool:
    files = _fixture_files(directory)
    if not files:
        print(
            _serialize(
                directory,
                (
                    Finding(
                        "FIXTURE_LANE_EMPTY",
                        "/",
                        "fixture lane contains no JSON candidates",
                    ),
                ),
            )
        )
        return False

    ok = True
    for path in files:
        result = validate_file(path)
        if expect_valid:
            print(_serialize(path, result.findings))
            ok = result.ok and ok
            continue

        expected_path = path.with_suffix(".expected_error.txt")
        expected_matches = expected_path.is_file() and _expected_rejection_matches(
            expected_path,
            result.findings,
        )
        if result.ok:
            findings = (
                Finding(
                    "FIXTURE_POLARITY_ERROR",
                    "/",
                    "expected rejection candidate passed validation",
                ),
            )
            print(_serialize(path, findings))
            ok = False
        elif not expected_matches:
            findings = tuple(result.findings) + (
                Finding(
                    "EXPECTED_REJECTION_MISMATCH",
                    "/",
                    "findings did not match reviewed expected-error evidence",
                ),
            )
            print(_serialize(path, findings))
            ok = False
        else:
            print(
                _serialize(
                    path,
                    result.findings,
                    expected_rejection=True,
                )
            )
    return ok


def run_fixture_profile() -> int:
    """Run non-vacuous valid, schema-invalid, and semantic-invalid lanes."""

    valid_ok = _validate_fixture_lane(FIXTURE_ROOT / "valid", expect_valid=True)
    invalid_ok = _validate_fixture_lane(FIXTURE_ROOT / "invalid", expect_valid=False)
    semantic_ok = _validate_fixture_lane(
        FIXTURE_ROOT / "semantic_invalid",
        expect_valid=False,
    )
    return 0 if valid_ok and invalid_ok and semantic_ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate KFM TemporalWindow records without network access."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_file(path)
        print(_serialize(path, result.findings))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
