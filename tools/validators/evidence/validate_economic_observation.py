#!/usr/bin/env python3
"""Validate fixture-only EconomicObservation records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import date, datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/evidence/economic_observation.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/economic_observation/cases.json"
PREFIX = "kfm:economic-observation:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
REQUIRED_LIMITS = {
    "AGGREGATE_ONLY",
    "NO_BUSINESS_OR_INDIVIDUAL_INFERENCE",
    "NO_CAUSAL_CLAIM",
    "NO_PUBLICATION_AUTHORITY",
    "PRICE_BASIS_DECLARED",
    "SOURCE_ROLE_PRESERVED",
    "SUPPRESSION_PRESERVED",
    "VERSION_BOUND",
}
MISSING_REASONS = {"SOURCE_MISSING", "NOT_COLLECTED", "NOT_AVAILABLE"}
MONETARY_UNITS = {
    "TOTAL_WAGES": "USD",
    "AVERAGE_ANNUAL_WAGE": "USD_PER_JOB",
    "PERSONAL_INCOME": "USD",
    "PER_CAPITA_INCOME": "USD_PER_PERSON",
    "GDP": "USD",
    "INDUSTRY_OUTPUT": "USD",
}


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


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("ECONOMIC_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ECONOMIC_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ECONOMIC_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ECONOMIC_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ECONOMIC_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ECONOMIC_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ECONOMIC_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("ECONOMIC_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def _instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = dict(value)
    subject.pop("observation_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    temporal = value["temporal"]
    measure = value["measure"]
    suppression = value["suppression"]
    source = value["source"]
    lineage = value["lineage"]
    disclosure = value["disclosure"]

    reference_year = temporal["reference_year"]
    period_start = date.fromisoformat(temporal["reference_period_start"])
    period_end = date.fromisoformat(temporal["reference_period_end"])
    if period_end < period_start:
        findings.add(
            Finding("ECONOMIC_REFERENCE_PERIOD_INVERTED", "/temporal/reference_period_end")
        )
    if period_start != date(reference_year, 1, 1) or period_end != date(reference_year, 12, 31):
        findings.add(
            Finding("ECONOMIC_REFERENCE_PERIOD_NOT_CALENDAR_YEAR", "/temporal")
        )

    released_at = _instant(temporal["source_released_at"])
    retrieved_at = _instant(temporal["retrieved_at"])
    if released_at.date() < period_end:
        findings.add(
            Finding("ECONOMIC_RELEASE_PRECEDES_PERIOD_END", "/temporal/source_released_at")
        )
    if retrieved_at < released_at:
        findings.add(
            Finding("ECONOMIC_RETRIEVAL_PRECEDES_RELEASE", "/temporal/retrieved_at")
        )
    corrected_at = temporal["corrected_at"]
    corrected_instant = _instant(corrected_at) if corrected_at is not None else None
    if corrected_instant is not None and corrected_instant < released_at:
        findings.add(
            Finding("ECONOMIC_CORRECTION_PRECEDES_RELEASE", "/temporal/corrected_at")
        )

    result_state = measure["result_state"]
    value_present = measure["value"] is not None
    missing_reason = measure["missing_reason"]
    suppression_status = suppression["status"]
    suppression_reason = suppression["reason"]
    suppression_method = suppression["method_ref"]

    if result_state == "OBSERVED":
        if not value_present:
            findings.add(Finding("ECONOMIC_OBSERVED_VALUE_REQUIRED", "/measure/value"))
        if missing_reason != "NOT_APPLICABLE":
            findings.add(
                Finding("ECONOMIC_OBSERVED_MISSING_REASON_INVALID", "/measure/missing_reason")
            )
        if (
            suppression_status != "NOT_SUPPRESSED"
            or suppression_reason != "NOT_APPLICABLE"
            or suppression_method is not None
        ):
            findings.add(Finding("ECONOMIC_OBSERVED_SUPPRESSION_INVALID", "/suppression"))
    elif result_state == "SUPPRESSED":
        if value_present:
            findings.add(Finding("ECONOMIC_SUPPRESSED_VALUE_DENIED", "/measure/value"))
        if missing_reason != "SOURCE_SUPPRESSED":
            findings.add(
                Finding("ECONOMIC_SUPPRESSION_MISSING_REASON_INVALID", "/measure/missing_reason")
            )
        if (
            suppression_status != "SUPPRESSED"
            or suppression_reason not in {"CONFIDENTIALITY", "RELIABILITY"}
            or suppression_method is None
        ):
            findings.add(Finding("ECONOMIC_SUPPRESSION_CLOSURE_INCOMPLETE", "/suppression"))
    elif result_state == "MISSING":
        if value_present:
            findings.add(Finding("ECONOMIC_MISSING_VALUE_DENIED", "/measure/value"))
        if missing_reason not in MISSING_REASONS:
            findings.add(Finding("ECONOMIC_MISSING_REASON_INVALID", "/measure/missing_reason"))
        if (
            suppression_status != "MISSING"
            or suppression_reason != missing_reason
            or suppression_method is not None
        ):
            findings.add(Finding("ECONOMIC_MISSING_SUPPRESSION_STATE_INVALID", "/suppression"))

    family = measure["measure_family"]
    if family == "EMPLOYMENT":
        if measure["unit"] != "PERSONS":
            findings.add(Finding("ECONOMIC_EMPLOYMENT_UNIT_INVALID", "/measure/unit"))
        if measure["price_basis"] != "NOT_APPLICABLE" or measure["price_year"] is not None:
            findings.add(
                Finding("ECONOMIC_EMPLOYMENT_PRICE_BASIS_INVALID", "/measure/price_basis")
            )
        if measure["seasonal_adjustment"] == "NOT_APPLICABLE":
            findings.add(
                Finding(
                    "ECONOMIC_EMPLOYMENT_SEASONAL_POSTURE_REQUIRED",
                    "/measure/seasonal_adjustment",
                )
            )
    else:
        if measure["unit"] != MONETARY_UNITS[family]:
            findings.add(Finding("ECONOMIC_MONETARY_UNIT_INVALID", "/measure/unit"))
        if measure["price_basis"] == "NOT_APPLICABLE":
            findings.add(
                Finding("ECONOMIC_MONETARY_PRICE_BASIS_REQUIRED", "/measure/price_basis")
            )
        if measure["seasonal_adjustment"] != "NOT_APPLICABLE":
            findings.add(
                Finding("ECONOMIC_MONETARY_SEASONAL_POSTURE_INVALID", "/measure/seasonal_adjustment")
            )

    if measure["price_basis"] == "CONSTANT_DOLLARS":
        if measure["price_year"] is None:
            findings.add(Finding("ECONOMIC_CONSTANT_PRICE_YEAR_REQUIRED", "/measure/price_year"))
    elif measure["price_year"] is not None:
        findings.add(Finding("ECONOMIC_PRICE_YEAR_DENIED", "/measure/price_year"))

    classification_ref = measure["industry_classification_ref"]
    industry_code = measure["industry_code"]
    if measure["industry_scope"] == "SPECIFIC_INDUSTRY":
        if classification_ref is None or industry_code is None:
            findings.add(Finding("ECONOMIC_INDUSTRY_BINDING_INCOMPLETE", "/measure"))
    elif classification_ref is not None or industry_code is not None:
        findings.add(Finding("ECONOMIC_ALL_INDUSTRIES_BINDING_DENIED", "/measure"))

    evidence_refs = source["evidence_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("ECONOMIC_EVIDENCE_ORDER_INVALID", "/source/evidence_refs"))

    correction_state = lineage["correction_state"]
    lineage_refs = (lineage["predecessor_ref"], lineage["correction_record_ref"])
    if correction_state == "ORIGINAL":
        if corrected_at is not None or any(item is not None for item in lineage_refs):
            findings.add(Finding("ECONOMIC_ORIGINAL_LINEAGE_INVALID", "/lineage"))
    else:
        if corrected_at is None or any(item is None for item in lineage_refs):
            findings.add(Finding("ECONOMIC_CORRECTED_LINEAGE_INCOMPLETE", "/lineage"))

    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(
            Finding("ECONOMIC_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits")
        )
    if set(limits) != REQUIRED_LIMITS:
        findings.add(
            Finding("ECONOMIC_REQUIRED_LIMIT_MISMATCH", "/disclosure/interpretation_limits")
        )

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("ECONOMIC_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("ECONOMIC_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["observation_id"] != identifier:
            findings.add(Finding("ECONOMIC_OBSERVATION_ID_MISMATCH", "/observation_id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    return Result("PASS", ())


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
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["observation_id"] = case.get("observation_id_override", identifier)
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
                "no_source_data_access",
                "no_geography_resolution",
                "no_industry_classification_resolution",
                "no_evidence_resolution",
                "no_business_or_individual_inference",
                "no_frontier_classification",
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
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
