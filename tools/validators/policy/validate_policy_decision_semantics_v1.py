#!/usr/bin/env python3
"""Validate PolicyDecision semantics against the inactive v1 vocabulary."""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_decision.schema.json"
VOCABULARY = ROOT / "policy/decision/vocabulary.v1.json"
SCOPE = "policy-decision-semantics-v1-fixture-only"
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED", "JSON_INVALID", "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
    "VOCABULARY_UNAVAILABLE",
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


def _vocabulary() -> tuple[dict[str, Mapping[str, Any]], dict[str, Mapping[str, Any]]] | None:
    candidate, findings = _read(VOCABULARY)
    if candidate is None or findings:
        return None
    reasons = candidate.get("reason_codes")
    obligations = candidate.get("obligation_codes")
    if not isinstance(reasons, list) or not isinstance(obligations, list):
        return None
    reason_map = {
        item["code"]: item
        for item in reasons
        if isinstance(item, Mapping) and isinstance(item.get("code"), str)
    }
    obligation_map = {
        item["code"]: item
        for item in obligations
        if isinstance(item, Mapping) and isinstance(item.get("code"), str)
    }
    return reason_map, obligation_map


def _canonical_codes(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    vocab = _vocabulary()
    if vocab is None:
        return [Finding("VOCABULARY_UNAVAILABLE", "/")]
    reason_map, obligation_map = vocab
    findings: list[Finding] = []

    reasons = candidate.get("reasons")
    obligations = candidate.get("obligations")
    if not _canonical_codes(reasons):
        findings.append(Finding("REASONS_NOT_CANONICAL", "/reasons"))
    if not _canonical_codes(obligations):
        findings.append(Finding("OBLIGATIONS_NOT_CANONICAL", "/obligations"))

    reason_codes = reasons if isinstance(reasons, list) else []
    obligation_codes = obligations if isinstance(obligations, list) else []
    outcome = candidate.get("outcome")
    family = candidate.get("policy_family")

    for index, code in enumerate(reason_codes):
        entry = reason_map.get(code)
        if entry is None:
            findings.append(Finding("REASON_CODE_UNKNOWN", f"/reasons/{index}"))
            continue
        if entry.get("outcome") != outcome:
            findings.append(Finding("REASON_OUTCOME_MISMATCH", f"/reasons/{index}"))
        families = entry.get("policy_families")
        if isinstance(families, list) and family not in families:
            findings.append(Finding("REASON_FAMILY_MISMATCH", f"/reasons/{index}"))

    for index, code in enumerate(obligation_codes):
        entry = obligation_map.get(code)
        if entry is None:
            findings.append(Finding("OBLIGATION_CODE_UNKNOWN", f"/obligations/{index}"))
            continue
        outcomes = entry.get("applicable_outcomes")
        if isinstance(outcomes, list) and outcome not in outcomes:
            findings.append(Finding("OBLIGATION_OUTCOME_MISMATCH", f"/obligations/{index}"))
        families = entry.get("policy_families")
        if isinstance(families, list) and family not in families:
            findings.append(Finding("OBLIGATION_FAMILY_MISMATCH", f"/obligations/{index}"))

    if outcome in {"ABSTAIN", "DENY", "ERROR"}:
        if not reason_codes:
            findings.append(Finding("NEGATIVE_REASON_REQUIRED", "/reasons"))
        if obligation_codes:
            findings.append(Finding("NEGATIVE_OBLIGATIONS_DENIED", "/obligations"))
    if outcome == "ANSWER":
        if not reason_codes:
            findings.append(Finding("ANSWER_REASON_REQUIRED", "/reasons"))
        if (
            "OPERATION_ALLOWED_WITH_OBLIGATIONS" in reason_codes
            and not obligation_codes
        ):
            findings.append(Finding("ANSWER_OBLIGATION_REQUIRED", "/obligations"))
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
                "decision_authenticated": False,
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
    parser.add_argument("records", nargs="+", type=Path)
    args = parser.parse_args(argv)
    ok = True
    for path in args.records:
        result = validate_record(path)
        print(serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
