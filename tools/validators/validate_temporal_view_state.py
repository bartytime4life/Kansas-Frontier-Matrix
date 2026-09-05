"""Validate the proposed KFM TemporalViewState profile without network access."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import math
import os
from pathlib import Path
import stat
import sys
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/temporal_view_state.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/common/temporal_view_state"
TEMPORAL_SRC = REPO_ROOT / "packages/temporal/src"

if str(TEMPORAL_SRC) not in sys.path:
    sys.path.insert(0, str(TEMPORAL_SRC))

from temporal.core import (  # noqa: E402
    normalize_temporal_query,
    validate_temporal_view_state,
)

MAX_FILE_BYTES = 1_000_000
MAX_JSON_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationReport:
    outcome: str
    findings: tuple[Finding, ...]
    normalization: str | None = None

    @property
    def ok(self) -> bool:
        return self.outcome in {"PASS", "UNSUPPORTED"} and not self.findings


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


def _depth_exceeded(value: str) -> bool:
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


def _read_regular_file(path: Path) -> tuple[str | None, tuple[Finding, ...]]:
    if path.is_symlink():
        return None, (Finding("UNSAFE_FILE", "/", "regular file required"),)
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0),
        )
    except OSError:
        return None, (Finding("READ_ERROR", "/", "candidate could not be read"),)

    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, (Finding("UNSAFE_FILE", "/", "regular file required"),)
        if metadata.st_size > MAX_FILE_BYTES:
            return None, (Finding("FILE_TOO_LARGE", "/", "parser budget exceeded"),)
        chunks: list[bytes] = []
        remaining = MAX_FILE_BYTES + 1
        while remaining:
            block = os.read(descriptor, min(64 * 1024, remaining))
            if not block:
                break
            chunks.append(block)
            remaining -= len(block)
        data = b"".join(chunks)
        if len(data) > MAX_FILE_BYTES:
            return None, (Finding("FILE_TOO_LARGE", "/", "parser budget exceeded"),)
        try:
            return data.decode("utf-8"), ()
        except UnicodeDecodeError:
            return None, (Finding("INVALID_UTF8", "/", "candidate must be UTF-8"),)
    finally:
        os.close(descriptor)


def _load_json(path: Path) -> tuple[Mapping[str, Any] | None, tuple[Finding, ...]]:
    text, findings = _read_regular_file(path)
    if text is None:
        return None, findings
    if _depth_exceeded(text):
        return None, (Finding("JSON_COMPLEXITY_LIMIT", "/", "parser budget exceeded"),)
    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("DUPLICATE_KEY", "/", "duplicate member rejected"),)
    except NonFiniteNumberError:
        return None, (Finding("NONFINITE_NUMBER", "/", "number must be finite"),)
    except (json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("INVALID_JSON", "/", "candidate is not JSON"),)
    if not isinstance(value, Mapping):
        return None, (Finding("ROOT_TYPE", "/", "object root required"),)
    return value, ()


def _pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    return "/" + "/".join(
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    )


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(validator.iter_errors(candidate))
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be evaluated")]

    errors = sorted(
        errors[: MAX_SCHEMA_FINDINGS + 1],
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
    )
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _pointer(tuple(error.absolute_path)),
            str(error.validator or "schema"),
        )
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if truncated:
        findings.append(
            Finding(
                "SCHEMA_FINDINGS_TRUNCATED",
                "/",
                "schema findings exceeded the output budget",
            )
        )
    return findings


def validate_candidate(candidate: Mapping[str, Any]) -> ValidationReport:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationReport("FAIL", tuple(schema_findings))

    status, semantic_codes = validate_temporal_view_state(candidate)
    unsupported_codes = {"UNSUPPORTED_PROFILE", "UNKNOWN_TIMEZONE", "UNCERTAIN_ORDERING"}
    if status == "UNSUPPORTED" and set(semantic_codes).issubset(unsupported_codes):
        return ValidationReport(
            "UNSUPPORTED",
            (),
            semantic_codes[-1] if semantic_codes else "UNSUPPORTED",
        )
    findings = tuple(
        Finding(code, "/", "bounded temporal semantic check failed")
        for code in semantic_codes
    )
    if findings:
        return ValidationReport("FAIL", findings, status)
    return ValidationReport("PASS", (), "SUPPORTED")


def validate_file(path: Path) -> ValidationReport:
    candidate, parse_findings = _load_json(path)
    if candidate is None:
        return ValidationReport("FAIL", parse_findings)
    return validate_candidate(candidate)


def _render(path: Path, report: ValidationReport) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "field": item.field, "detail": item.detail}
                for item in report.findings
            ],
            "normalization": report.normalization,
            "outcome": report.outcome,
            "scope": "closed-state-shape-and-local-temporal-semantics-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_matches(path: Path, findings: Sequence[Finding]) -> bool:
    try:
        expected = path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return False
    if not expected:
        return False
    if expected.startswith("{"):
        # Match the shared schema-sidecar identity, not renderer-dependent prose.
        # Unsupported keys (including message predicates) fail closed because
        # bounded temporal findings deliberately do not expose raw messages.
        try:
            structured = json.loads(
                expected, object_pairs_hook=_reject_duplicate_keys
            )
        except (ValueError, RecursionError):
            return False
        if not isinstance(structured, dict) or set(structured) != {
            "kind", "field", "keyword"
        }:
            return False
        field = structured["field"]
        keyword = structured["keyword"]
        if (
            structured["kind"] != "schema"
            or not isinstance(field, str)
            or not field.startswith("/")
            or not isinstance(keyword, str)
            or not keyword
        ):
            return False
        return any(
            item.code == "SCHEMA_INVALID"
            and item.field == field
            and item.detail == keyword
            for item in findings
        )
    expected = expected.lower()
    searchable = "\n".join(
        f"{item.code} {item.field} {item.detail}".lower() for item in findings
    )
    for line in (line.strip() for line in expected.splitlines()):
        if line and line not in searchable:
            return False
    return True


def _lane_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.json"), key=lambda item: item.as_posix())


def _check_lane(
    directory: Path,
    expected_outcome: str,
    *,
    expected_error_files: bool = False,
) -> bool:
    paths = _lane_files(directory)
    if not paths:
        print(
            _render(
                directory,
                ValidationReport(
                    "FAIL",
                    (Finding("FIXTURE_LANE_EMPTY", "/", "lane has no JSON fixtures"),),
                ),
            )
        )
        return False

    success = True
    for path in paths:
        report = validate_file(path)
        expected_path = path.with_suffix(".expected_error.txt")
        if expected_outcome == "PASS":
            success = success and report.outcome == "PASS" and report.ok
        elif expected_outcome == "UNSUPPORTED":
            success = success and report.outcome == "UNSUPPORTED" and report.ok
        else:
            matches = (
                expected_path.is_file()
                and _expected_matches(expected_path, report.findings)
                if expected_error_files
                else report.outcome == "FAIL"
            )
            success = success and report.outcome == "FAIL" and matches
        print(_render(path, report))
    return success


def run_fixture_profile() -> int:
    valid = _check_lane(FIXTURE_ROOT / "valid", "PASS")
    invalid = _check_lane(
        FIXTURE_ROOT / "invalid",
        "FAIL",
        expected_error_files=True,
    )
    unsupported = _check_lane(FIXTURE_ROOT / "unsupported", "UNSUPPORTED")
    return 0 if valid and invalid and unsupported else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate KFM TemporalViewState without network access."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixture_profile()
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        report = validate_file(path)
        print(_render(path, report))
        failed = failed or not report.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
