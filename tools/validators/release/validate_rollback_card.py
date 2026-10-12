#!/usr/bin/env python3
"""Validate proposed KFM RollbackCard candidates without network access.

A passing result proves bounded candidate shape and local consistency only.
It does not execute rollback, authorize release mutation, erase history, or publish.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/rollback_card.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/release/rollback_card"
MAX_FILE_BYTES = 1_048_576
SCOPE = "rollback-card-candidate-shape-and-local-consistency-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
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
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: dict[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in validator.iter_errors(candidate)
    ]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + ("0" * 64)


def _sorted_unique_strings(values: list[Any]) -> bool:
    return (
        all(isinstance(item, str) for item in values)
        and values == sorted(set(values))
    )


def _semantic_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    card_id = candidate.get("id")
    disposition = candidate.get("disposition")
    spec_hash = candidate.get("spec_hash")
    target = _mapping(candidate.get("target"))
    restoration = _mapping(candidate.get("restoration"))
    timing = _mapping(candidate.get("timing"))
    lineage = _mapping(candidate.get("lineage"))
    governance = _mapping(candidate.get("governance"))

    if _is_zero_digest(spec_hash):
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))

    for field in (
        "evidence_bundle_refs",
        "policy_decision_refs",
        "review_record_refs",
        "invalidations",
    ):
        values = _array(candidate.get(field))
        if values and not _sorted_unique_strings(values):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/{field}"))

    affected_release = candidate.get("affected_release_ref")
    target_mode = target.get("mode")
    target_release = target.get("release_ref")
    correction_notice = candidate.get("correction_notice_ref")

    if disposition == "ROLLBACK_CANDIDATE":
        if target_mode != "PRIOR_RELEASE" or not isinstance(target_release, str):
            findings.append(Finding("TARGET_RELEASE_REQUIRED", "/target/release_ref"))
        if not _array(candidate.get("evidence_bundle_refs")):
            findings.append(Finding("EVIDENCE_REQUIRED", "/evidence_bundle_refs"))
        if not _array(candidate.get("policy_decision_refs")):
            findings.append(Finding("POLICY_DECISION_REQUIRED", "/policy_decision_refs"))
    elif disposition == "WITHDRAWAL_CANDIDATE":
        if target_mode != "WITHDRAWAL" or target_release is not None:
            findings.append(Finding("WITHDRAWAL_TARGET_MISMATCH", "/target"))
    elif disposition == "HOLD":
        if target_mode != "HOLD" or target_release is not None:
            findings.append(Finding("HOLD_TARGET_MISMATCH", "/target"))
    elif disposition == "ERROR":
        if target_mode != "HOLD":
            findings.append(Finding("ERROR_TARGET_MISMATCH", "/target/mode"))

    if (
        isinstance(target_release, str)
        and isinstance(affected_release, str)
        and target_release == affected_release
    ):
        findings.append(Finding("ROLLBACK_TARGET_NOT_PRIOR", "/target/release_ref"))

    if (
        target_mode == "PRIOR_RELEASE"
        and isinstance(target_release, str)
        and restoration.get("restore_release_ref") != target_release
    ):
        findings.append(
            Finding("RESTORATION_TARGET_MISMATCH", "/restoration/restore_release_ref")
        )

    if restoration.get("public_notice_required") is True and not isinstance(
        correction_notice, str
    ):
        findings.append(
            Finding("CORRECTION_NOTICE_REQUIRED", "/correction_notice_ref")
        )

    decided_at = _parse_time(timing.get("decided_at"))
    effective_at = _parse_time(timing.get("effective_at"))
    detected_at = _parse_time(_mapping(candidate.get("trigger")).get("detected_at"))
    if detected_at and decided_at and detected_at > decided_at:
        findings.append(Finding("DECISION_BEFORE_DETECTION", "/timing/decided_at"))
    if decided_at and effective_at and effective_at < decided_at:
        findings.append(Finding("EFFECTIVE_BEFORE_DECISION", "/timing/effective_at"))

    if card_id and lineage.get("supersedes") == card_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/supersedes"))
    if card_id and lineage.get("superseded_by") == card_id:
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/superseded_by"))

    flag_fields = (
        "authority_created",
        "policy_evaluated",
        "review_completed",
        "rollback_executed",
        "public_state_mutated",
    )
    if (
        any(governance.get(field) is not False for field in flag_fields)
        or governance.get("release_ref") is not None
    ):
        findings.append(
            Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance")
        )

    return findings


def validate_rollback_card(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(
        directory.glob(f"{prefix}*.json"),
        key=lambda path: path.as_posix(),
    )


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads(
            (directory / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 1

    passed = True
    for path in valid_files:
        result = validate_rollback_card(path)
        print(_serialize(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_rollback_card(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected,
                        "file": path.as_posix(),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM RollbackCard candidates."
    )
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
        result = validate_rollback_card(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
