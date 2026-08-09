#!/usr/bin/env python3
"""Validate evidence-backed Pass 11 policy-enforcement maturity claims."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash  # noqa: E402
from jsonschema import Draft202012Validator

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/policy/policy_enforcement_maturity.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/policy/policy_enforcement_maturity/cases.json"
MAX_JSON_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
STAGES = ["DESIGNED", "FIXTURE_TESTED", "MERGE_BLOCKING", "PROMOTION_BLOCKING", "RUNTIME_ENFORCED"]
EXPECTED_KIND = {
    "DESIGNED": "CONTRACT_OR_POLICY",
    "FIXTURE_TESTED": "FIXTURE_OR_TEST",
    "MERGE_BLOCKING": "REQUIRED_CHECK",
    "PROMOTION_BLOCKING": "PROMOTION_GATE",
    "RUNTIME_ENFORCED": "RUNTIME_OBSERVATION",
}


class DuplicateKeyError(ValueError):
    """Raised when a parsed JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON includes a non-standard finite-number violation."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS" and not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_UNREADABLE", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("JSON_ROOT_INVALID", "/")])


def _schema_findings(record: Mapping[str, Any]) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = list(islice(Draft202012Validator(schema).iter_errors(record), MAX_SCHEMA_FINDINGS + 1))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _spec_subject(record: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in record.items() if key != "spec_hash"}


def compute_record_spec_hash(record: Mapping[str, Any]) -> str:
    return compute_spec_hash(_spec_subject(record))


def validate_record(record: Any) -> ValidationResult:
    if not isinstance(record, dict):
        return ValidationResult("ERROR", (Finding("JSON_ROOT_INVALID", "/"),))

    findings = _schema_findings(record)
    if findings:
        return ValidationResult("ERROR", tuple(sorted(findings)))

    try:
        expected_hash = compute_record_spec_hash(record)
    except CanonicalizationFailure:
        return ValidationResult("ERROR", (Finding("SPEC_HASH_CANONICALIZATION_ERROR", "/spec_hash"),))
    if record["spec_hash"] != expected_hash:
        return ValidationResult("ERROR", (Finding("SPEC_HASH_MISMATCH", "/spec_hash"),))

    denied: list[Finding] = []
    if record["deterministic"] is not True:
        denied.append(Finding("DETERMINISM_REQUIRED", "/deterministic"))
    if record["network_access"] is not False:
        denied.append(Finding("NETWORK_ACCESS_FORBIDDEN", "/network_access"))

    claimed_index = STAGES.index(record["claimed_stage"])
    required_stages = STAGES[: claimed_index + 1]
    evidence = record["evidence"]
    supplied_stages = [item["stage"] for item in evidence]
    if supplied_stages != required_stages:
        denied.append(Finding("MATURITY_STAGE_CHAIN_INVALID", "/evidence"))

    for index, item in enumerate(evidence):
        stage = item["stage"]
        if item["evidence_kind"] != EXPECTED_KIND[stage]:
            denied.append(Finding("EVIDENCE_KIND_MISMATCH", f"/evidence/{index}/evidence_kind"))
        if item["refs"] != sorted(item["refs"]):
            denied.append(Finding("EVIDENCE_REFS_NOT_CANONICAL", f"/evidence/{index}/refs"))

    if record["assessment_outcome"] != "PASS" or record["reason_codes"] != []:
        denied.append(Finding("ASSESSMENT_OVERCLAIM", "/assessment_outcome"))

    return ValidationResult("DENY" if denied else "PASS", tuple(sorted(set(denied))))


def evaluate(record: Any) -> str:
    return validate_record(record).outcome


def replay(path: Path = FIXTURES) -> list[tuple[str, str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[tuple[str, str, str]] = []
    for case in data["cases"]:
        actual = evaluate(case["record"])
        if actual != case["expected"]:
            failures.append((case["name"], case["expected"], actual))
    return failures


def _report(result: ValidationResult) -> dict[str, Any]:
    return {
        "authority": "NONE",
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome,
        "policy_enforced": False,
        "publication_authorized": False,
        "scope": "pass11-policy-enforcement-maturity",
        "status": "PASS" if result.outcome == "PASS" else "FAIL",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        failures = replay()
        if failures:
            for name, expected, actual in failures:
                print(json.dumps({"actual": actual, "expected": expected, "name": name}, sort_keys=True))
            return 1
        print(json.dumps({"cases": 9, "scope": "pass11-policy-enforcement-maturity", "status": "PASS"}, sort_keys=True))
        return 0

    if args.path is None:
        parser.error("path required unless --fixtures is used")
    record, findings = _load_object(args.path)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if record is None
        else validate_record(record)
    )
    print(json.dumps(_report(result), sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
