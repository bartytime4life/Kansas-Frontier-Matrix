#!/usr/bin/env python3
"""Validate deterministic temporal and freshness semantics for KDHE HAB snapshots.

PASS is bounded to repository-local schema and semantic checks. It does not
establish current conditions, activate a source, issue an alert, release,
deploy, or publish any advisory.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/kdhe_hab_advisory_snapshot.schema.json"
FIXTURES = ROOT / "fixtures/domains/hazards/kdhe_hab_advisory_snapshot"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
ACTIVE_STATES = {"WATCH", "WARNING", "HAZARD"}
ERROR_CODES = {
    "KDHE_HAB_FILE_NOT_FOUND",
    "KDHE_HAB_FILE_READ_ERROR",
    "KDHE_HAB_FILE_TOO_LARGE",
    "KDHE_HAB_INPUT_SYMLINK_DENIED",
    "KDHE_HAB_JSON_INVALID",
    "KDHE_HAB_JSON_DUPLICATE_KEY",
    "KDHE_HAB_JSON_NONFINITE_NUMBER",
    "KDHE_HAB_ROOT_NOT_OBJECT",
    "KDHE_HAB_SCHEMA_UNAVAILABLE",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


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


def _nonfinite(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("KDHE_HAB_INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("KDHE_HAB_FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("KDHE_HAB_FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except DuplicateKeyError:
        return None, [Finding("KDHE_HAB_JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("KDHE_HAB_JSON_NONFINITE_NUMBER", "/")]
    except (UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("KDHE_HAB_JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("KDHE_HAB_FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("KDHE_HAB_ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("KDHE_HAB_SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("KDHE_HAB_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("KDHE_HAB_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    first = _time(candidate.get("first_observed_at"))
    last = _time(candidate.get("last_observed_at"))
    retrieved = _time(candidate.get("retrieved_at"))
    source_updated_raw = candidate.get("source_updated_at")
    source_updated = _time(source_updated_raw) if source_updated_raw is not None else None

    if first is not None and last is not None and retrieved is not None:
        if first > last or last > retrieved:
            findings.append(Finding("KDHE_HAB_OBSERVATION_TIME_ORDER_INVALID", "/last_observed_at"))
    if source_updated is not None and retrieved is not None and source_updated > retrieved:
        findings.append(Finding("KDHE_HAB_SOURCE_TIME_AFTER_RETRIEVAL", "/source_updated_at"))

    freshness = candidate.get("freshness_status")
    state = candidate.get("normalized_state")
    budget = candidate.get("freshness_budget_hours")
    if state in ACTIVE_STATES and freshness != "current":
        findings.append(Finding("KDHE_HAB_ACTIVE_STATE_NOT_CURRENT", "/freshness_status"))
    if freshness == "current" and source_updated is None:
        findings.append(Finding("KDHE_HAB_CURRENT_SOURCE_TIME_MISSING", "/source_updated_at"))
    if (
        freshness == "current"
        and source_updated is not None
        and retrieved is not None
        and isinstance(budget, int)
        and not isinstance(budget, bool)
        and retrieved - source_updated > timedelta(hours=budget)
    ):
        findings.append(Finding("KDHE_HAB_FRESHNESS_BUDGET_EXCEEDED", "/freshness_status"))
    return findings


def validate_document(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    outcome = "ERROR" if any(item.code in ERROR_CODES for item in ordered) else "DENY"
    return ValidationResult(outcome, ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult("ERROR", ordered)
    return validate_document(candidate)


def _payload(result: ValidationResult, target: str) -> dict[str, Any]:
    return {
        "profile": "kfm.kdhe-hab-temporal.v1",
        "target": target,
        "outcome": result.outcome,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "authority": "NONE",
        "non_effects": [
            "no_live_source_access",
            "no_alert_release_deployment_or_publication",
        ],
    }


def run_fixture_suite() -> tuple[bool, dict[str, Any]]:
    valid = sorted((FIXTURES / "valid").glob("*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("*.json"))
    failures: list[dict[str, str]] = []
    for path in valid:
        result = validate_file(path)
        if result.outcome != "PASS":
            failures.append({"fixture": path.name, "actual": result.outcome, "expected": "PASS"})
    for path in invalid:
        result = validate_file(path)
        if result.outcome == "PASS":
            failures.append({"fixture": path.name, "actual": result.outcome, "expected": "DENY_OR_ERROR"})
    if not valid or not invalid:
        failures.append({"fixture": "fixture_inventory", "actual": "MISSING", "expected": "VALID_AND_INVALID"})
    payload = {
        "profile": "kfm.kdhe-hab-temporal.fixtures.v1",
        "outcome": "PASS" if not failures else "ERROR",
        "valid_fixtures": len(valid),
        "invalid_fixtures": len(invalid),
        "failures": failures,
        "authority": "NONE",
    }
    return not failures, payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate KDHE HAB snapshot temporal semantics.")
    parser.add_argument("files", nargs="*", help="Repository-local JSON snapshots to validate.")
    parser.add_argument("--fixtures", action="store_true", help="Replay committed valid and invalid fixtures.")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not args.files:
        parser.error("provide --fixtures or at least one JSON file")
    exit_code = 0
    for raw_path in args.files:
        result = validate_file(Path(raw_path))
        print(json.dumps(_payload(result, raw_path), sort_keys=True, separators=(",", ":")))
        if result.outcome == "DENY":
            exit_code = max(exit_code, 1)
        elif result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
