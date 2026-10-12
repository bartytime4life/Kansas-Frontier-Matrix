#!/usr/bin/env python3
"""Validate the inactive PolicyDecision reason/obligation vocabulary."""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_decision_vocabulary.schema.json"
REGISTRY = ROOT / "policy/decision/vocabulary.v1.json"
SCOPE = "policy-decision-vocabulary-fixture-only"
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED", "JSON_INVALID", "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
}


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

    @property
    def error(self) -> bool:
        return any(item.code in ERROR_CODES for item in self.findings)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _nonfinite(_value: str) -> object:
    raise NonFiniteError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        raw = path.read_bytes()
        if len(raw) > 1_048_576:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
            for error in sorted(
                validator.iter_errors(candidate),
                key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
            )
        ]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def _canonical_entries(value: object) -> bool:
    if not isinstance(value, list) or not all(isinstance(item, Mapping) for item in value):
        return False
    codes = [item.get("code") for item in value]
    return all(isinstance(code, str) for code in codes) and codes == sorted(set(codes))


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    reasons = candidate.get("reason_codes")
    obligations = candidate.get("obligation_codes")

    if not _canonical_entries(reasons):
        findings.append(Finding("REASON_CODES_NOT_CANONICAL", "/reason_codes"))
    if not _canonical_entries(obligations):
        findings.append(Finding("OBLIGATION_CODES_NOT_CANONICAL", "/obligation_codes"))

    reason_items = reasons if isinstance(reasons, list) else []
    obligation_items = obligations if isinstance(obligations, list) else []

    for index, item in enumerate(reason_items):
        if isinstance(item, Mapping) and not _canonical_strings(item.get("policy_families")):
            findings.append(Finding(
                "POLICY_FAMILIES_NOT_CANONICAL",
                f"/reason_codes/{index}/policy_families",
            ))

    for index, item in enumerate(obligation_items):
        if not isinstance(item, Mapping):
            continue
        if not _canonical_strings(item.get("policy_families")):
            findings.append(Finding(
                "POLICY_FAMILIES_NOT_CANONICAL",
                f"/obligation_codes/{index}/policy_families",
            ))
        if item.get("applicable_outcomes") != ["ANSWER"]:
            findings.append(Finding(
                "OBLIGATION_OUTCOME_UNSUPPORTED",
                f"/obligation_codes/{index}/applicable_outcomes",
            ))

    reason_codes = {
        item.get("code") for item in reason_items
        if isinstance(item, Mapping) and isinstance(item.get("code"), str)
    }
    obligation_codes = {
        item.get("code") for item in obligation_items
        if isinstance(item, Mapping) and isinstance(item.get("code"), str)
    }
    if reason_codes.intersection(obligation_codes):
        findings.append(Finding("CODE_NAMESPACE_COLLISION", "/"))

    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_payload(candidate).findings)
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": outcome,
            "scope": SCOPE,
            "authority": {
                "policy_evaluation": False,
                "decision_emitted": False,
                "promotion": False,
                "release": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="*", type=Path)
    parser.add_argument("--registry", action="store_true")
    args = parser.parse_args(argv)

    records = list(args.records)
    if args.registry:
        records.append(REGISTRY)
    if not records:
        parser.error("provide records or --registry")

    ok = True
    for path in records:
        result = validate_record(path)
        print(serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
