#!/usr/bin/env python3
"""Validate one no-network GovernedRunChain linkage object.

The validator proves bounded JSON safety, schema conformance, and cross-object
linkage only. It never fetches a source, mutates lifecycle state, evaluates live
policy, signs evidence, promotes, releases, or publishes.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/governed_run_chain.schema.json"
)
MAX_JSON_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for JSON NaN or infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    operational_error: bool = False

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


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_payload(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        payload = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "/")]

    if not isinstance(payload, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return payload, []


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(
        schema,
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )


def _schema_findings(payload: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(
            islice(
                _schema_validator().iter_errors(payload),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered = sorted(
        errors,
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in ordered
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    chain_hash = payload["spec_hash"]
    run_receipt = payload["run_receipt"]
    policy_decision = payload["policy_decision"]
    quarantine = payload["quarantine_record"]
    promotion = payload["promotion_decision"]
    outcome = payload["outcome"]

    if run_receipt["spec_hash"] != chain_hash:
        findings.append(Finding("RUN_SPEC_HASH_MISMATCH", "/run_receipt/spec_hash"))
    if policy_decision["policy_family"] != "promotion":
        findings.append(
            Finding("POLICY_FAMILY_NOT_PROMOTION", "/policy_decision/policy_family")
        )

    if quarantine is not None:
        if quarantine["subject_ref"] != payload["subject_ref"]:
            findings.append(
                Finding("QUARANTINE_SUBJECT_MISMATCH", "/quarantine_record/subject_ref")
            )
        if quarantine["spec_hash"] != chain_hash:
            findings.append(
                Finding("QUARANTINE_SPEC_HASH_MISMATCH", "/quarantine_record/spec_hash")
            )
        if quarantine["run_receipt_ref"] != run_receipt["run_id"]:
            findings.append(
                Finding(
                    "QUARANTINE_RUN_REF_MISMATCH",
                    "/quarantine_record/run_receipt_ref",
                )
            )
        if quarantine["policy_decision_ref"] != policy_decision["decision_id"]:
            findings.append(
                Finding(
                    "QUARANTINE_POLICY_REF_MISMATCH",
                    "/quarantine_record/policy_decision_ref",
                )
            )

    if promotion is not None and promotion["run_id"] != run_receipt["run_id"]:
        findings.append(
            Finding("PROMOTION_RUN_REF_MISMATCH", "/promotion_decision/run_id")
        )

    expected: dict[str, Any] = {
        "PROMOTABLE": {
            "run": "SUCCESS",
            "policy": "ANSWER",
            "quarantine": None,
            "promotion": "APPROVE",
        },
        "QUARANTINED": {
            "policy": "DENY",
            "quarantine": "QUARANTINED",
            "promotion": None,
        },
        "HELD": {
            "policy": "ABSTAIN",
            "quarantine": "HELD",
            "promotion": None,
        },
        "ERROR": {
            "run": "FAIL",
            "policy": "ERROR",
            "quarantine": None,
            "promotion": None,
        },
    }[outcome]

    expected_run = expected.get("run")
    if expected_run is not None and run_receipt["outcome"] != expected_run:
        findings.append(Finding("OUTCOME_RUN_MISMATCH", "/run_receipt/outcome"))

    if policy_decision["outcome"] != expected["policy"]:
        findings.append(
            Finding("OUTCOME_POLICY_MISMATCH", "/policy_decision/outcome")
        )

    expected_quarantine = expected["quarantine"]
    if expected_quarantine is None:
        if quarantine is not None:
            findings.append(
                Finding("OUTCOME_QUARANTINE_FORBIDDEN", "/quarantine_record")
            )
    elif quarantine is None:
        findings.append(Finding("OUTCOME_QUARANTINE_REQUIRED", "/quarantine_record"))
    elif quarantine["state"] != expected_quarantine:
        findings.append(
            Finding("OUTCOME_QUARANTINE_STATE_MISMATCH", "/quarantine_record/state")
        )

    expected_promotion = expected["promotion"]
    if expected_promotion is None:
        if promotion is not None:
            findings.append(
                Finding("OUTCOME_PROMOTION_FORBIDDEN", "/promotion_decision")
            )
    elif promotion is None:
        findings.append(Finding("OUTCOME_PROMOTION_REQUIRED", "/promotion_decision"))
    elif promotion["decision"] != expected_promotion:
        findings.append(
            Finding("OUTCOME_PROMOTION_DECISION_MISMATCH", "/promotion_decision/decision")
        )

    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    operational = any(
        finding.code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE"))
        for finding in findings
    )
    return ValidationResult(tuple(sorted(set(findings))), operational)


def validate_file(path: Path) -> ValidationResult:
    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(findings)), operational_error=True)
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-only governed run chain."
    )
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    outcome = "ANSWER" if result.ok else ("ERROR" if result.operational_error else "DENY")
    output = {
        "ok": result.ok,
        "outcome": outcome,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "scope": "fixture-only-governed-run-chain",
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "lifecycle_write": False,
            "policy_evaluation": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
