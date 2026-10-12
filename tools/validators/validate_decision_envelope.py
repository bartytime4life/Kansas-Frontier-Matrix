#!/usr/bin/env python3
"""Validate DecisionEnvelope records with bounded no-network semantics.

A green result proves schema and local semantic conformance only. It does not
resolve EvidenceRefs, evaluate policy, authenticate review, establish release
state, authorize an action, publish, or permit public use.
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
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/runtime/decision_envelope.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/runtime/decision_envelope"
MANIFEST_PATH = FIXTURES_ROOT / "expected_findings_manifest.json"
MAX_JSON_BYTES = 256 * 1024
MAX_SCHEMA_FINDINGS = 50
SHA256_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?$")
REASON_CODE_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]{0,63}$")
SAFE_REF_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._~:/#?=&%+@-]{0,319}$")
DENIED_REF_PREFIXES = (
    "raw:",
    "work:",
    "quarantine:",
    "internal:",
    "canonical:",
    "proof:",
    "model:",
)
SENSITIVE_TEXT_MARKERS = (
    "authorization:",
    "bearer ",
    "password=",
    "secret=",
    "token=",
    "private_key",
    "begin private key",
)
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
    "MANIFEST_INVALID",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(item.code in ERROR_CODES for item in self.findings)

    @property
    def outcome(self) -> str:
        if self.ok:
            return "PASS"
        return "ERROR" if self.error else "FAIL"


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise DuplicateKeyError
        output[key] = value
    return output


def _reject_constant(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    descriptor: int | None = None
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "symbolic links are denied")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        mode = os.fstat(descriptor).st_mode
        if not stat.S_ISREG(mode):
            return None, [Finding("FILE_NOT_FOUND", "/", "input is not a regular file")]
        size = os.fstat(descriptor).st_size
        if size > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds 256 KiB")]
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            raw = stream.read(MAX_JSON_BYTES + 1)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds 256 KiB")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except FileNotFoundError:
        return None, [Finding("FILE_NOT_FOUND", "/", "input file was not found")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate object members are denied")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "input is not valid JSON")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("FILE_READ_ERROR", "/", "input could not be read safely")]
    finally:
        if descriptor is not None:
            os.close(descriptor)

    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/", "JSON root must be an object")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator() -> Draft202012Validator:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError("schema unavailable") from exc
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(value: Mapping[str, object]) -> list[Finding]:
    try:
        errors = list(islice(_schema_validator().iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except RuntimeError:
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be loaded safely")]
    errors = sorted(errors, key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _pointer(error.absolute_path),
            f"schema constraint failed: {error.validator}",
        )
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(
            Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings were truncated")
        )
    return findings


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _string_array_findings(
    value: object,
    *,
    field: str,
    code: str,
    allow_empty: bool,
) -> list[Finding]:
    if not isinstance(value, list):
        return []
    findings: list[Finding] = []
    strings = [item for item in value if isinstance(item, str)]
    if len(strings) != len(value):
        return findings
    if not allow_empty and not strings:
        findings.append(Finding(code, field, "at least one entry is required"))
    if len(strings) != len(set(strings)):
        findings.append(Finding(code, field, "entries must be unique"))
    for item in strings:
        if (
            not item
            or item != item.strip()
            or len(item) > 240
            or any(ord(char) < 32 or ord(char) == 127 for char in item)
        ):
            findings.append(Finding(code, field, "entries must be bounded clean text"))
            break
    return findings


def _contains_sensitive_marker(value: object) -> bool:
    if not isinstance(value, list):
        return False
    for item in value:
        if not isinstance(item, str):
            continue
        lowered = item.casefold()
        if any(marker in lowered for marker in SENSITIVE_TEXT_MARKERS):
            return True
    return False


def _semantic_findings(value: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []

    outcome = value.get("outcome")
    alias = value.get("decision")
    refs = value.get("evidence_refs")
    refs_list = [item for item in refs if isinstance(item, str)] if isinstance(refs, list) else []

    if alias is not None and alias != outcome:
        findings.append(
            Finding(
                "OUTCOME_ALIAS_MISMATCH",
                "/decision",
                "decision alias must match outcome",
            )
        )

    findings.extend(
        _string_array_findings(
            value.get("reasons"),
            field="/reasons",
            code="REASONS_NOT_CANONICAL",
            allow_empty=False,
        )
    )
    findings.extend(
        _string_array_findings(
            value.get("obligations"),
            field="/obligations",
            code="OBLIGATIONS_NOT_CANONICAL",
            allow_empty=True,
        )
    )

    if _contains_sensitive_marker(value.get("reasons")) or _contains_sensitive_marker(
        value.get("obligations")
    ):
        findings.append(
            Finding(
                "SENSITIVE_TEXT_DENIED",
                "/",
                "reason and obligation text must not contain credential-like material",
            )
        )

    if refs_list:
        if refs_list != sorted(set(refs_list)):
            findings.append(
                Finding(
                    "EVIDENCE_REFS_NOT_CANONICAL",
                    "/evidence_refs",
                    "evidence references must be sorted and unique",
                )
            )
        if any(not SAFE_REF_PATTERN.fullmatch(item) for item in refs_list):
            findings.append(
                Finding(
                    "EVIDENCE_REF_INVALID",
                    "/evidence_refs",
                    "evidence references must use the bounded reference grammar",
                )
            )
        if any(item.casefold().startswith(DENIED_REF_PREFIXES) for item in refs_list):
            findings.append(
                Finding(
                    "INTERNAL_REFERENCE_DENIED",
                    "/evidence_refs",
                    "internal or lifecycle-private references are denied",
                )
            )

    if outcome == "DENY" and refs_list:
        findings.append(
            Finding(
                "DENY_SUPPORT_LEAK",
                "/evidence_refs",
                "DENY envelopes cannot expose evidence references",
            )
        )
    if outcome == "ERROR" and refs_list:
        findings.append(
            Finding(
                "ERROR_SUPPORT_LEAK",
                "/evidence_refs",
                "ERROR envelopes cannot expose evidence references",
            )
        )

    evaluated_at = _parse_time(value.get("evaluated_at"))
    issued_at = _parse_time(value.get("issued_at"))
    if evaluated_at is not None and issued_at is not None and issued_at < evaluated_at:
        findings.append(
            Finding(
                "TIME_ORDER_INVALID",
                "/issued_at",
                "issued_at cannot precede evaluated_at",
            )
        )

    spec_hash = value.get("spec_hash")
    if spec_hash is not None and (
        not isinstance(spec_hash, str) or not SHA256_PATTERN.fullmatch(spec_hash)
    ):
        findings.append(
            Finding(
                "SPEC_HASH_INVALID",
                "/spec_hash",
                "spec_hash must be a lowercase SHA-256 digest",
            )
        )

    version = value.get("version")
    if version is not None and (
        not isinstance(version, str) or not SEMVER_PATTERN.fullmatch(version)
    ):
        findings.append(
            Finding(
                "VERSION_INVALID",
                "/version",
                "version must use semantic-version syntax",
            )
        )

    reason_code = value.get("reason_code")
    if reason_code is not None and (
        not isinstance(reason_code, str) or not REASON_CODE_PATTERN.fullmatch(reason_code)
    ):
        findings.append(
            Finding(
                "REASON_CODE_INVALID",
                "/reason_code",
                "reason_code must use upper snake case",
            )
        )

    generic_id = value.get("id")
    if generic_id is not None and (
        not isinstance(generic_id, str)
        or not generic_id
        or len(generic_id) > 160
        or any(ord(char) < 32 or ord(char) == 127 for char in generic_id)
    ):
        findings.append(
            Finding(
                "COMPATIBILITY_ID_INVALID",
                "/id",
                "compatibility id must be bounded clean text",
            )
        )

    return findings


def validate_value(value: Mapping[str, object]) -> ValidationResult:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return ValidationResult(tuple(sorted(set(schema_findings))))
    return ValidationResult(tuple(sorted(set(_semantic_findings(value)))))


def validate(path: Path) -> ValidationResult:
    value, findings = _read_object(path)
    if value is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_value(value)


def _load_manifest() -> dict[str, object]:
    value, findings = _read_object(MANIFEST_PATH)
    if value is None or findings:
        raise ValueError("manifest invalid")
    cases = value.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("manifest invalid")
    return value


def run_fixtures() -> int:
    try:
        manifest = _load_manifest()
    except ValueError:
        print("DECISION_ENVELOPE_FIXTURES_ERROR code=MANIFEST_INVALID")
        return 2

    failures: list[str] = []
    cases = manifest["cases"]
    assert isinstance(cases, list)
    for raw_case in cases:
        if not isinstance(raw_case, dict):
            failures.append("non-object-case")
            continue
        case_id = raw_case.get("case_id")
        relative = raw_case.get("path")
        expected_outcome = raw_case.get("expected_outcome")
        expected_findings = raw_case.get("expected_findings")
        if (
            not isinstance(case_id, str)
            or not isinstance(relative, str)
            or not isinstance(expected_outcome, str)
            or not isinstance(expected_findings, list)
            or any(not isinstance(item, str) for item in expected_findings)
        ):
            failures.append(str(case_id))
            continue
        candidate = FIXTURES_ROOT / relative
        result = validate(candidate)
        actual_findings = sorted({item.code for item in result.findings})
        if result.outcome != expected_outcome or actual_findings != sorted(expected_findings):
            failures.append(case_id)
        print(
            "DECISION_ENVELOPE_FIXTURE "
            f"case={case_id} outcome={result.outcome} "
            f"findings={','.join(actual_findings) if actual_findings else '-'}"
        )

    if failures:
        for case_id in failures:
            print(f"DECISION_ENVELOPE_FIXTURE_MISMATCH case={case_id}")
        return 1
    print(
        "DECISION_ENVELOPE_FIXTURES_VALID "
        f"cases={len(cases)} no_network=true authority=validation-only"
    )
    return 0


def _emit_result(path: Path, result: ValidationResult) -> int:
    if result.ok:
        print(f"DECISION_ENVELOPE_VALID file={path.name}")
        return 0
    for finding in result.findings:
        print(
            "DECISION_ENVELOPE_INVALID "
            f"code={finding.code} field={finding.field} detail={finding.detail}"
        )
    return 2 if result.error else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            raise SystemExit("--fixtures cannot be combined with files")
        return run_fixtures()
    if not args.files:
        print("No files provided", file=sys.stderr)
        return 2
    exit_code = 0
    for path in args.files:
        exit_code = max(exit_code, _emit_result(path, validate(path)))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
