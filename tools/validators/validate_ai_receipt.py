#!/usr/bin/env python3
"""Validate proposed KFM AIReceipt records without network access.

A passing result proves bounded schema shape and local receipt consistency only.
It does not resolve evidence, authenticate policy or citation decisions, approve a
model, authorize a public answer, promote lifecycle state, release, or publish.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/runtime/ai_receipt.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/ai_receipt"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "ai-receipt-shape-and-local-consistency-only"
EMPTY_FIELDS = (
    "run_id",
    "adapter",
    "model_ref",
    "policy_decision_ref",
    "citation_validation_ref",
)
ERROR_CODES = frozenset(
    {
        "FILE_NOT_FOUND",
        "FILE_READ_ERROR",
        "FILE_TOO_LARGE",
        "INPUT_SYMLINK_DENIED",
        "JSON_DUPLICATE_KEY",
        "JSON_INVALID",
        "JSON_NONFINITE_NUMBER",
        "JSON_NOT_UTF8",
        "ROOT_NOT_OBJECT",
        "SCHEMA_UNAVAILABLE",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic, payload-safe validation finding."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite result for one AIReceipt candidate."""

    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    """Raised when a parsed JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON uses a non-standard non-finite number token."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    errors.sort(
        key=lambda error: (
            _json_pointer(error.absolute_path),
            str(error.validator),
        )
    )
    findings = [
        Finding("SCHEMA_INVALID", _json_pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()

    for field in EMPTY_FIELDS:
        value = candidate.get(field)
        if isinstance(value, str) and not value.strip():
            findings.add(Finding("FIELD_EMPTY", f"/{field}"))

    for field in ("inputs_digest", "outputs_digest"):
        value = candidate.get(field)
        if isinstance(value, str) and value == "sha256:" + ("0" * 64):
            findings.add(Finding("DIGEST_PLACEHOLDER", f"/{field}"))

    return sorted(findings)


def _outcome(findings: Sequence[Finding]) -> str:
    if not findings:
        return "PASS"
    if any(finding.code in ERROR_CODES for finding in findings):
        return "ERROR"
    return "FAIL"


def validate_ai_receipt(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is not None:
        schema_findings = _schema_findings(candidate)
        findings.extend(schema_findings)
        if not schema_findings:
            findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize_result(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": _display_path(path),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(group: str, prefix: str) -> list[Path]:
    return sorted(
        (FIXTURE_ROOT / group).glob(f"{prefix}*.json"),
        key=lambda path: path.as_posix(),
    )


def run_fixture_profile() -> int:
    valid_files = _fixture_files("valid", "valid_")
    invalid_files = _fixture_files("invalid", "invalid_")
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = validate_ai_receipt(path)
        print(serialize_result(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_ai_receipt(path)
        print(serialize_result(path, result))
        passed = passed and not result.ok

    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_ai_receipt(path)
        print(serialize_result(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
