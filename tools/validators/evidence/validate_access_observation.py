#!/usr/bin/env python3
"""Validate fixture-only AccessObservation records."""
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

SCHEMA = ROOT / "schemas/contracts/v1/evidence/access_observation.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/access_observation/cases.json"
PREFIX = "kfm:access-observation:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
REQUIRED_LIMITS = {
    "AGGREGATE_ONLY",
    "METHOD_BOUND",
    "NO_CAUSAL_CLAIM",
    "NO_PROVIDER_ELIGIBILITY_GUARANTEE",
    "NO_PUBLICATION_AUTHORITY",
    "NO_ROUTING_OR_EMERGENCY_GUIDANCE",
    "SOURCE_ROLE_PRESERVED",
    "VERSION_BOUND",
}
MISSING_REASONS = {"SOURCE_MISSING", "NOT_COLLECTED", "NOT_AVAILABLE"}
FAMILY_UNITS = {
    "TRAVEL_TIME": "MINUTES",
    "DISTANCE": "KILOMETRES",
    "PROVIDER_COUNT": "COUNT",
    "SERVICE_COVERAGE": "PERCENT",
}
FAMILY_METHODS = {
    "TRAVEL_TIME": "NETWORK_TRAVEL_TIME",
    "DISTANCE": "STRAIGHT_LINE_DISTANCE",
    "PROVIDER_COUNT": "PROVIDER_INVENTORY",
    "SERVICE_COVERAGE": "COVERAGE_ESTIMATE",
}
FAMILY_AGGREGATIONS = {
    "TRAVEL_TIME": {"MEAN", "MEDIAN", "MINIMUM", "MAXIMUM"},
    "DISTANCE": {"MEAN", "MEDIAN", "MINIMUM", "MAXIMUM"},
    "PROVIDER_COUNT": {"COUNT"},
    "SERVICE_COVERAGE": {"PERCENT"},
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
            return None, (Finding("ACCESS_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ACCESS_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ACCESS_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ACCESS_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ACCESS_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ACCESS_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ACCESS_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema() -> Mapping[str, Any]:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("ACCESS_SCHEMA_INVALID", _pointer(error.absolute_path))
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
    method = value["method"]
    suppression = value["suppression"]
    source = value["source"]
    lineage = value["lineage"]
    disclosure = value["disclosure"]

    year = temporal["reference_year"]
    start = date.fromisoformat(temporal["reference_period_start"])
    end = date.fromisoformat(temporal["reference_period_end"])
    if start != date(year, 1, 1):
        findings.add(Finding("ACCESS_PERIOD_START_INVALID", "/temporal/reference_period_start"))
    if end != date(year, 12, 31):
        findings.add(Finding("ACCESS_PERIOD_END_INVALID", "/temporal/reference_period_end"))
    released_at = _instant(temporal["source_released_at"])
    retrieved_at = _instant(temporal["retrieved_at"])
    if released_at.date() < end:
        findings.add(Finding("ACCESS_RELEASE_PRECEDES_PERIOD", "/temporal/source_released_at"))
    if retrieved_at < released_at:
        findings.add(Finding("ACCESS_RETRIEVAL_PRECEDES_RELEASE", "/temporal/retrieved_at"))
    corrected_at = temporal["corrected_at"]
    corrected_instant = _instant(corrected_at) if corrected_at is not None else None
    if corrected_instant is not None and corrected_instant < released_at:
        findings.add(Finding("ACCESS_CORRECTION_PRECEDES_RELEASE", "/temporal/corrected_at"))

    state = measure["result_state"]
    value_present = measure["value"] is not None
    missing_reason = measure["missing_reason"]
    if state == "OBSERVED":
        if not value_present:
            findings.add(Finding("ACCESS_OBSERVED_VALUE_REQUIRED", "/measure/value"))
        if missing_reason != "NOT_APPLICABLE":
            findings.add(
                Finding("ACCESS_OBSERVED_MISSING_REASON_INVALID", "/measure/missing_reason")
            )
    elif state == "SUPPRESSED":
        if value_present:
            findings.add(Finding("ACCESS_SUPPRESSED_VALUE_DENIED", "/measure/value"))
        if missing_reason != "SOURCE_SUPPRESSED":
            findings.add(Finding("ACCESS_SUPPRESSION_REASON_REQUIRED", "/measure/missing_reason"))
    elif state == "MISSING":
        if value_present:
            findings.add(Finding("ACCESS_MISSING_VALUE_DENIED", "/measure/value"))
        if missing_reason not in MISSING_REASONS:
            findings.add(Finding("ACCESS_MISSING_REASON_INVALID", "/measure/missing_reason"))

    suppression_fields = (suppression["reason"], suppression["method_ref"])
    if state == "SUPPRESSED":
        if suppression["status"] != "SOURCE_SUPPRESSED" or any(
            item is None for item in suppression_fields
        ):
            findings.add(Finding("ACCESS_SUPPRESSION_BLOCK_REQUIRED", "/suppression"))
    elif suppression["status"] != "NOT_APPLICABLE" or any(
        item is not None for item in suppression_fields
    ):
        findings.add(Finding("ACCESS_SUPPRESSION_BLOCK_DENIED", "/suppression"))

    family = measure["measure_family"]
    if measure["unit"] != FAMILY_UNITS[family]:
        findings.add(Finding("ACCESS_UNIT_MISMATCH", "/measure/unit"))
    if method["method_family"] != FAMILY_METHODS[family]:
        findings.add(Finding("ACCESS_METHOD_FAMILY_MISMATCH", "/method/method_family"))
    if method["aggregation_method"] not in FAMILY_AGGREGATIONS[family]:
        findings.add(
            Finding("ACCESS_AGGREGATION_MISMATCH", "/method/aggregation_method")
        )

    network_ref = method["network_or_model_ref"]
    if family in {"TRAVEL_TIME", "SERVICE_COVERAGE"}:
        if network_ref is None:
            findings.add(
                Finding("ACCESS_NETWORK_OR_MODEL_REQUIRED", "/method/network_or_model_ref")
            )
    elif network_ref is not None:
        findings.add(
            Finding("ACCESS_NETWORK_OR_MODEL_DENIED", "/method/network_or_model_ref")
        )

    threshold_ref = method["threshold_ref"]
    if family == "SERVICE_COVERAGE":
        if threshold_ref is None:
            findings.add(Finding("ACCESS_THRESHOLD_REQUIRED", "/method/threshold_ref"))
        if measure["value"] is not None and measure["value"] > 100:
            findings.add(Finding("ACCESS_PERCENT_RANGE_INVALID", "/measure/value"))
    elif threshold_ref is not None:
        findings.add(Finding("ACCESS_THRESHOLD_DENIED", "/method/threshold_ref"))

    service_ref = measure["source_service_ref"]
    if measure["service_domain"] == "SOURCE_DEFINED":
        if service_ref is None:
            findings.add(Finding("ACCESS_SOURCE_SERVICE_REQUIRED", "/measure/source_service_ref"))
    elif service_ref is not None:
        findings.add(Finding("ACCESS_SOURCE_SERVICE_DENIED", "/measure/source_service_ref"))

    evidence_refs = source["evidence_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("ACCESS_EVIDENCE_ORDER_INVALID", "/source/evidence_refs"))

    correction_state = lineage["correction_state"]
    lineage_refs = (lineage["predecessor_ref"], lineage["correction_record_ref"])
    if correction_state == "ORIGINAL":
        if corrected_at is not None or any(item is not None for item in lineage_refs):
            findings.add(Finding("ACCESS_ORIGINAL_LINEAGE_INVALID", "/lineage"))
    elif corrected_at is None or any(item is None for item in lineage_refs):
        findings.add(Finding("ACCESS_CORRECTED_LINEAGE_INCOMPLETE", "/lineage"))

    limits = disclosure["interpretation_limits"]
    if limits != sorted(limits):
        findings.add(Finding("ACCESS_LIMIT_ORDER_INVALID", "/disclosure/interpretation_limits"))
    if set(limits) != REQUIRED_LIMITS:
        findings.add(
            Finding("ACCESS_REQUIRED_LIMIT_MISMATCH", "/disclosure/interpretation_limits")
        )

    try:
        digest, identifier = canonical_identity(value)
    except (CanonicalizationFailure, TypeError, ValueError, RecursionError):
        findings.add(Finding("ACCESS_IDENTITY_ERROR", "/spec_hash"))
    else:
        if value["spec_hash"] != digest:
            findings.add(Finding("ACCESS_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["observation_id"] != identifier:
            findings.add(Finding("ACCESS_OBSERVATION_ID_MISMATCH", "/observation_id"))
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
                "no_evidence_resolution",
                "no_method_execution",
                "no_provider_identity_resolution",
                "no_route_computation",
                "no_eligibility_or_emergency_guidance",
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
