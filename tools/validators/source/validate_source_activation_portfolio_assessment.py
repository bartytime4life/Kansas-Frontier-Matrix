#!/usr/bin/env python3
"""Validate fixture-only SourceActivationPortfolioAssessment records."""
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

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/source_activation_portfolio_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_activation_portfolio_assessment/cases.json"
PREFIX = "kfm:source-portfolio:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
READINESS_FIELDS = (
    "source_role",
    "rights_currentness",
    "sensitivity",
    "reviewer",
    "dependencies",
    "acceptance_tests",
    "correction_rollback",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]
    portfolio_outcome: str | None = None


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("SOURCE_PORTFOLIO_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("SOURCE_PORTFOLIO_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("SOURCE_PORTFOLIO_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("SOURCE_PORTFOLIO_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("SOURCE_PORTFOLIO_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("SOURCE_PORTFOLIO_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("SOURCE_PORTFOLIO_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"portfolio_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def derive_candidate(candidate: Mapping[str, Any], assessment_state: str) -> tuple[str, list[str]]:
    if assessment_state == "ERROR":
        return "ERROR", ["ASSESSMENT_ERROR"]

    risk_class = candidate["risk_class"]
    readiness = candidate["readiness"]
    if risk_class == "DENIED_CLASS":
        return "HOLD", ["DENIED_CLASS_RETAINED"]

    hold_order = (
        ("rights_currentness", {"HOLD", "DENIED"}, "RIGHTS_OR_CURRENTNESS_HELD"),
        ("sensitivity", {"HOLD", "DENIED"}, "SENSITIVITY_HELD"),
        ("source_role", {"HOLD"}, "SOURCE_ROLE_HELD"),
        ("reviewer", {"HOLD"}, "REVIEWER_HELD"),
        ("dependencies", {"HOLD"}, "DEPENDENCY_HELD"),
        ("acceptance_tests", {"HOLD"}, "ACCEPTANCE_TEST_HELD"),
        ("correction_rollback", {"HOLD"}, "CORRECTION_ROLLBACK_HELD"),
    )
    for field, states, reason in hold_order:
        if readiness[field] in states:
            return "HOLD", [reason]

    if risk_class == "HIGH_RISK":
        return "CONDITIONAL", ["HIGH_RISK_SEPARATE_AUTHORITY_REQUIRED"]
    if any(readiness[field] == "REVIEW_REQUIRED" for field in READINESS_FIELDS):
        return "CONDITIONAL", ["UPSTREAM_REVIEW_REQUIRED"]
    if risk_class == "CONDITIONAL_AGENCY":
        return "CONDITIONAL", ["CONDITIONAL_SOURCE_REVIEW_REQUIRED"]
    return "READY_FOR_REVIEW", ["READY_FOR_REVIEW_ONLY"]


def derive_portfolio(value: Mapping[str, Any]) -> dict[str, Any]:
    candidates = value["candidates"]
    source_ids = [candidate["source_id"] for candidate in candidates]
    if value["assessment_state"] == "ERROR":
        return {
            "outcome": "ERROR",
            "ordered_source_ids": source_ids,
            "ready_source_ids": [],
            "conditional_source_ids": [],
            "held_source_ids": [],
            "reason_codes": ["ASSESSMENT_ERROR"],
        }

    ready = sorted(candidate["source_id"] for candidate in candidates if candidate["declared_outcome"] == "READY_FOR_REVIEW")
    conditional = sorted(candidate["source_id"] for candidate in candidates if candidate["declared_outcome"] == "CONDITIONAL")
    held = sorted(candidate["source_id"] for candidate in candidates if candidate["declared_outcome"] == "HOLD")
    if held:
        outcome, reasons = "HOLD", ["PORTFOLIO_CONTAINS_HOLD"]
    elif conditional:
        outcome, reasons = "CONDITIONAL", ["PORTFOLIO_CONTAINS_CONDITIONAL"]
    else:
        outcome, reasons = "READY_FOR_REVIEW", ["PORTFOLIO_READY_FOR_REVIEW_ONLY"]
    return {
        "outcome": outcome,
        "ordered_source_ids": source_ids,
        "ready_source_ids": ready,
        "conditional_source_ids": conditional,
        "held_source_ids": held,
        "reason_codes": reasons,
    }


def _schema_finding(value: Mapping[str, Any]) -> Finding | None:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return Finding("SOURCE_PORTFOLIO_SCHEMA_UNAVAILABLE", "/")
    if not errors:
        return None
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    return Finding("SOURCE_PORTFOLIO_SCHEMA_INVALID", _pointer(errors[0].absolute_path))


def _semantic_finding(value: Mapping[str, Any]) -> Finding | None:
    candidates = value["candidates"]
    source_ids = [candidate["source_id"] for candidate in candidates]
    if len(source_ids) != len(set(source_ids)):
        return Finding("SOURCE_PORTFOLIO_SOURCE_ID_DUPLICATE", "/candidates")
    if source_ids != sorted(source_ids):
        return Finding("SOURCE_PORTFOLIO_CANDIDATES_NOT_CANONICAL", "/candidates")

    for index, candidate in enumerate(candidates):
        for field in ("reviewer_role_refs", "dependency_refs", "acceptance_test_refs"):
            values = candidate[field]
            if values != sorted(values):
                return Finding("SOURCE_PORTFOLIO_REFERENCES_NOT_CANONICAL", f"/candidates/{index}/{field}")
        expected_outcome, expected_reasons = derive_candidate(candidate, value["assessment_state"])
        if candidate["declared_outcome"] != expected_outcome:
            return Finding("SOURCE_PORTFOLIO_CANDIDATE_OUTCOME_MISMATCH", f"/candidates/{index}/declared_outcome")
        if candidate["reason_codes"] != expected_reasons:
            return Finding("SOURCE_PORTFOLIO_CANDIDATE_REASON_MISMATCH", f"/candidates/{index}/reason_codes")

    if value["portfolio_decision"] != derive_portfolio(value):
        return Finding("SOURCE_PORTFOLIO_DECISION_MISMATCH", "/portfolio_decision")

    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        return Finding("SOURCE_PORTFOLIO_CANONICALIZATION_ERROR", "/")
    if value["spec_hash"] != expected_hash:
        return Finding("SOURCE_PORTFOLIO_SPEC_HASH_MISMATCH", "/spec_hash")
    if value["portfolio_id"] != expected_id:
        return Finding("SOURCE_PORTFOLIO_ID_MISMATCH", "/portfolio_id")
    return None


def validate_payload(value: Mapping[str, Any]) -> Result:
    finding = _schema_finding(value)
    if finding is not None:
        return Result("DENY", (finding,))
    finding = _semantic_finding(value)
    if finding is not None:
        return Result("DENY", (finding,))
    portfolio_outcome = value["portfolio_decision"]["outcome"]
    if portfolio_outcome == "READY_FOR_REVIEW":
        return Result("PASS", (), portfolio_outcome)
    if portfolio_outcome in {"CONDITIONAL", "HOLD"}:
        return Result("ABSTAIN", (), portfolio_outcome)
    return Result("ERROR", (), portfolio_outcome)


def _parts(pointer: str) -> list[str]:
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]


def _target(document: Any, pointer: str) -> tuple[Any, str]:
    parts = _parts(pointer)
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    return target, parts[-1]


def _apply(document: dict[str, Any], operation: Mapping[str, Any]) -> None:
    target, key = _target(document, operation["path"])
    if operation["op"] == "set":
        if isinstance(target, list):
            target[int(key)] = copy.deepcopy(operation["value"])
        else:
            target[key] = copy.deepcopy(operation["value"])
    elif operation["op"] == "delete":
        if isinstance(target, list):
            del target[int(key)]
        else:
            del target[key]
    elif operation["op"] == "swap":
        container = target[int(key)] if isinstance(target, list) else target[key]
        first, second = operation["indexes"]
        container[first], container[second] = container[second], container[first]
    else:
        raise ValueError(f"unsupported fixture operation: {operation['op']}")


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for operation in case.get("operations", []):
        _apply(document, operation)
    if case.get("recompute_derived", True):
        for candidate in document["candidates"]:
            outcome, reasons = derive_candidate(candidate, document["assessment_state"])
            candidate["declared_outcome"] = outcome
            candidate["reason_codes"] = reasons
        document["portfolio_decision"] = derive_portfolio(document)
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["portfolio_id"] = case.get("portfolio_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_status"]
            or result.portfolio_outcome != case["expected_portfolio_outcome"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_status": case["expected_status"],
                    "actual_status": result.outcome,
                    "expected_portfolio_outcome": case["expected_portfolio_outcome"],
                    "actual_portfolio_outcome": result.portfolio_outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_source_contact",
                "no_admission",
                "no_activation",
                "no_review_scheduling",
                "no_mutation",
                "no_promotion",
                "no_release",
                "no_publication",
                "no_public_use",
            ],
            "outcome": result.outcome,
            "portfolio_outcome": result.portfolio_outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
