#!/usr/bin/env python3
"""Validate fixture-only AnalyticOutputDisclosureAssessment records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/evidence/analytic_output_disclosure_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/analytic_output_disclosure_assessment/cases.json"
PREFIX = "kfm:analytic-output-disclosure:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100

ROLE_BY_KIND = {
    "STATISTIC": "DERIVED",
    "INDICATOR": "DERIVED",
    "ML_MODEL": "MODELED",
    "MODEL_INTERPRETATION": "INTERPRETIVE",
    "PLANNING_SCENARIO": "INTERPRETIVE",
}

COMMON_LIMITS = {"NOT_ROOT_TRUTH", "NOT_OBSERVATION", "SCOPE_BOUND", "NO_PUBLICATION_AUTHORITY"}
CAUSAL_LIMIT_KINDS = {"STATISTIC", "INDICATOR", "PLANNING_SCENARIO"}
MODEL_LIMIT_KINDS = {"ML_MODEL", "MODEL_INTERPRETATION"}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


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


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("ANALYTIC_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ANALYTIC_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ANALYTIC_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ANALYTIC_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ANALYTIC_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ANALYTIC_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ANALYTIC_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("ANALYTIC_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def required_limits(kind: str) -> set[str]:
    limits = set(COMMON_LIMITS)
    if kind in CAUSAL_LIMIT_KINDS:
        limits.add("NO_CAUSAL_CLAIM")
    if kind in MODEL_LIMIT_KINDS:
        limits.add("MODEL_LIMITS_APPLY")
    if kind == "PLANNING_SCENARIO":
        limits.add("NO_AUTOMATED_RECOMMENDATION")
    return limits


def _fully_closed(value: Mapping[str, Any]) -> bool:
    return bool(
        all(item["evidence_bundle_ref"] is not None for item in value["inputs"])
        and value["validation"]["status"] == "PASS"
        and value["validation"]["validation_report_ref"] is not None
        and value["uncertainty"]["uncertainty_ref"] is not None
        and value["uncertainty"]["uncertainty_class"] != "UNKNOWN"
        and value["disclosure"]["confidence_class"] != "UNRESOLVED"
        and value["disclosure"]["citation_refs"]
    )


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    state = value["output"]["support_state"]
    if value["assessment_state"] == "ERROR" or state == "ERROR":
        return {"outcome": "ERROR", "reason_codes": ["ASSESSMENT_ERROR"]}
    if state == "SUPPORTED":
        return {"outcome": "PASS", "reason_codes": ["DISCLOSURE_COMPLETE"]}
    if state == "PARTIAL":
        return {"outcome": "ABSTAIN", "reason_codes": ["DISCLOSURE_PARTIAL"]}
    return {"outcome": "ABSTAIN", "reason_codes": ["SUPPORT_UNRESOLVED"]}


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _method_findings(value: Mapping[str, Any]) -> set[Finding]:
    kind = value["output"]["analysis_kind"]
    method = value["method"]
    required: set[str] = set()
    if kind == "INDICATOR":
        required.add("indicator_definition_ref")
    elif kind == "ML_MODEL":
        required.update(
            {"feature_set_manifest_ref", "model_card_ref", "model_run_receipt_ref", "training_lineage_ref"}
        )
    elif kind == "MODEL_INTERPRETATION":
        required.update({"model_card_ref", "model_run_receipt_ref"})
    optional_fields = {
        "indicator_definition_ref",
        "feature_set_manifest_ref",
        "model_card_ref",
        "model_run_receipt_ref",
        "training_lineage_ref",
    }
    findings: set[Finding] = set()
    for field in sorted(required):
        if method[field] is None:
            findings.add(Finding("ANALYTIC_METHOD_BINDING_REQUIRED", f"/method/{field}"))
    for field in sorted(optional_fields - required):
        if method[field] is not None:
            findings.add(Finding("ANALYTIC_METHOD_BINDING_UNEXPECTED", f"/method/{field}"))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    output = value["output"]
    kind = output["analysis_kind"]
    if output["source_role"] != ROLE_BY_KIND[kind]:
        findings.add(Finding("ANALYTIC_SOURCE_ROLE_MISMATCH", "/output/source_role"))

    valid_from = _time(output["valid_from"])
    valid_to = _time(output["valid_to"])
    computed_at = _time(output["computed_at"])
    if (valid_to is not None and valid_from is not None and valid_to < valid_from) or (
        computed_at is not None and valid_from is not None and computed_at < valid_from
    ):
        findings.add(Finding("ANALYTIC_TIME_ORDER_INVALID", "/output"))

    inputs = value["inputs"]
    input_refs = [item["input_ref"] for item in inputs]
    if len(input_refs) != len(set(input_refs)):
        findings.add(Finding("ANALYTIC_INPUT_DUPLICATE", "/inputs"))
    if input_refs != sorted(input_refs):
        findings.add(Finding("ANALYTIC_INPUT_ORDER_INVALID", "/inputs"))

    for field, path in (
        (value["assumption_refs"], "/assumption_refs"),
        (value["disclosure"]["citation_refs"], "/disclosure/citation_refs"),
        (value["disclosure"]["interpretation_limits"], "/disclosure/interpretation_limits"),
    ):
        if field != sorted(field):
            findings.add(Finding("ANALYTIC_ARRAY_ORDER_INVALID", path))

    findings.update(_method_findings(value))
    limits = set(value["disclosure"]["interpretation_limits"])
    if not required_limits(kind).issubset(limits):
        findings.add(Finding("ANALYTIC_REQUIRED_LIMIT_MISSING", "/disclosure/interpretation_limits"))

    state = output["support_state"]
    error_pair = value["assessment_state"] == "ERROR" and state == "ERROR"
    if (value["assessment_state"] == "ERROR" or state == "ERROR") and not error_pair:
        findings.add(Finding("ANALYTIC_ERROR_STATE_MISMATCH", "/assessment_state"))
    if error_pair and value["validation"]["status"] != "ERROR":
        findings.add(Finding("ANALYTIC_ERROR_VALIDATION_MISMATCH", "/validation/status"))

    fully_closed = _fully_closed(value)
    if state == "SUPPORTED":
        if not all(item["evidence_bundle_ref"] is not None for item in inputs):
            findings.add(Finding("ANALYTIC_EVIDENCE_CLOSURE_REQUIRED", "/inputs"))
        if value["validation"]["status"] != "PASS" or value["validation"]["validation_report_ref"] is None:
            findings.add(Finding("ANALYTIC_VALIDATION_PASS_REQUIRED", "/validation"))
        if value["uncertainty"]["uncertainty_ref"] is None or value["uncertainty"]["uncertainty_class"] == "UNKNOWN":
            findings.add(Finding("ANALYTIC_UNCERTAINTY_REQUIRED", "/uncertainty"))
        if value["disclosure"]["confidence_class"] == "UNRESOLVED":
            findings.add(Finding("ANALYTIC_CONFIDENCE_REQUIRED", "/disclosure/confidence_class"))
        if not value["disclosure"]["citation_refs"]:
            findings.add(Finding("ANALYTIC_CITATION_REQUIRED", "/disclosure/citation_refs"))
    elif state in {"PARTIAL", "UNSUPPORTED"} and fully_closed:
        findings.add(Finding("ANALYTIC_ABSTAIN_STATE_UNJUSTIFIED", "/output/support_state"))

    if value["decision"] != recompute_decision(value):
        findings.add(Finding("ANALYTIC_DECISION_MISMATCH", "/decision"))
    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("ANALYTIC_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("ANALYTIC_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != identifier:
            findings.add(Finding("ANALYTIC_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    outcome = value["decision"]["outcome"]
    if outcome == "PASS":
        return Result("PASS", ())
    return Result(
        outcome,
        tuple(Finding(code, "/decision/outcome") for code in value["decision"]["reason_codes"]),
    )


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in manifest["variants"][case["base"]]:
        _replace(document, mutation["path"], mutation.get("value"))
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["decision"] = copy.deepcopy(case.get("decision_override", recompute_decision(document)))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_network",
                "no_reference_resolution",
                "no_analysis_execution",
                "no_evidence_creation",
                "no_policy_evaluation",
                "no_review_approval",
                "no_promotion",
                "no_release",
                "no_public_use",
                "no_publication",
            ],
            "outcome": result.outcome,
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
