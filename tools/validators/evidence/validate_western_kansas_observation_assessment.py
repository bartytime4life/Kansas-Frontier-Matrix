#!/usr/bin/env python3
"""Validate the inactive western Kansas hydrology observation assessment profile."""
from __future__ import annotations

import argparse
import copy
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/western_kansas_observation_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/domains/hydrology/western_kansas_observation_assessment/cases.json"
PROFILE = "kfm.western-kansas-observation-assessment.v1"
SCOPE = "synthetic-no-network-observation-join-claim-assessment"

DIRECT_SUPPORT = {
    "DROUGHT_CLASSIFICATION": {"USDM"},
    "STREAMFLOW_CONDITION": {"USGS_STREAMFLOW"},
    "GROUNDWATER_CONDITION": {"KGS_GROUNDWATER"},
    "EVAPORATIVE_DEMAND": {"PRECIP_EDDI"},
    "PRECIPITATION_CONDITION": {"PRECIP_EDDI"},
    "SOIL_MOISTURE_CONDITION": {"SOIL_MOISTURE"},
    "AGRICULTURE_CONTEXT": {"AGRICULTURE_CONTEXT"},
    "MANAGEMENT_BOUNDARY_CONTEXT": {"WATER_MANAGEMENT_BOUNDARY"},
}
ERROR_CODES = frozenset(
    {
        "SCHEMA_INVALID",
        "PROFILE_INVALID",
        "TEMPORAL_ORDER_INVALID",
        "CORRECTION_LINK_REQUIRED",
        "SUPERSESSION_LINK_REQUIRED",
        "SOURCE_SUPPORT_ERASURE_DENIED",
        "MATERIAL_CHANGE_DECLARATION_MISMATCH",
        "GOVERNANCE_BOUNDARY_VIOLATION",
        "TUPLE_EVIDENCE_INCOMPLETE",
        "DERIVATION_REFERENCE_REQUIRED",
        "DECLARED_OUTCOME_MISMATCH",
    }
)
ABSTAIN_CODES = frozenset(
    {
        "MISSING_OBSERVATION",
        "SOURCE_SUPERSEDED",
        "USDM_CANNOT_PROVE_GROUNDWATER",
        "STREAMFLOW_CANNOT_PROVE_GROUNDWATER",
        "CONTEXT_CANNOT_PROVE_AGRICULTURAL_LOSS",
        "BOUNDARY_CANNOT_PROVE_CONDITION",
        "COUNTY_INTERSECTION_NOT_UNIFORM",
        "SOURCE_FAMILY_CANNOT_DIRECTLY_SUPPORT_CLAIM",
    }
)


@dataclass(frozen=True)
class Assessment:
    outcome: str
    reason_codes: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "outcome": self.outcome,
            "reason_codes": list(self.reason_codes),
            "scope": SCOPE,
        }


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_validator() -> Draft202012Validator:
    schema = _load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _schema_valid(candidate: Any) -> bool:
    try:
        return not list(_schema_validator().iter_errors(candidate))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return False


def _instant(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timezone required")
    return parsed.astimezone(timezone.utc)


def _try_instant(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return _instant(value)
    except (TypeError, ValueError, OverflowError):
        return None


def _deep_update(target: dict[str, Any], overrides: Mapping[str, Any]) -> None:
    for key, value in overrides.items():
        current = target.get(key)
        if isinstance(current, dict) and isinstance(value, Mapping):
            _deep_update(current, value)
        else:
            target[key] = copy.deepcopy(value)


def candidate_from_case(base_candidate: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(base_candidate))
    overrides = case.get("overrides", {})
    if isinstance(overrides, Mapping):
        _deep_update(candidate, overrides)
    return candidate


def _source_semantic_reasons(candidate: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    analysis_time = _try_instant(candidate["analysis_time"])
    if analysis_time is None:
        return ["TEMPORAL_ORDER_INVALID"]

    max_age_days = int(candidate["max_age_days"])
    claim = candidate["claim"]
    evidence_refs = set(claim["tuple_evidence_refs"])
    source_refs: set[str] = set()

    for source in candidate["sources"]:
        source_refs.add(source["evidence_ref"])
        observed_start = _try_instant(source["observation_start"])
        observed_end = _try_instant(source["observation_end"])
        publication = _try_instant(source["publication_time"])
        retrieval = _try_instant(source["retrieval_time"])
        if (
            observed_start is None
            or observed_end is None
            or publication is None
            or retrieval is None
        ):
            reasons.append("TEMPORAL_ORDER_INVALID")
            continue
        if not (observed_start <= observed_end <= publication <= retrieval <= analysis_time):
            reasons.append("TEMPORAL_ORDER_INVALID")

        valid_start = source.get("valid_start")
        valid_end = source.get("valid_end")
        if (valid_start is None) != (valid_end is None):
            reasons.append("TEMPORAL_ORDER_INVALID")
        elif valid_start is not None:
            parsed_valid_start = _try_instant(valid_start)
            parsed_valid_end = _try_instant(valid_end)
            if (
                parsed_valid_start is None
                or parsed_valid_end is None
                or parsed_valid_start > parsed_valid_end
            ):
                reasons.append("TEMPORAL_ORDER_INVALID")

        revision = source["revision_status"]
        if revision == "CORRECTED" and (
            source.get("correction_ref") is None or source.get("supersedes_ref") is None
        ):
            reasons.append("CORRECTION_LINK_REQUIRED")
        if revision == "SUPERSEDED" and source.get("supersedes_ref") is None:
            reasons.append("SUPERSESSION_LINK_REQUIRED")

        if source["observation_status"] == "MISSING":
            reasons.append("MISSING_OBSERVATION")
        if revision == "SUPERSEDED":
            reasons.append("SOURCE_SUPERSEDED")
        if source["observation_status"] == "PRESENT":
            age_days = (analysis_time - observed_end).total_seconds() / 86400
            if age_days > max_age_days:
                reasons.append("OBSERVATION_STALE")

    if not source_refs.issubset(evidence_refs):
        reasons.append("TUPLE_EVIDENCE_INCOMPLETE")
    return reasonsdef _claim_reasons(candidate: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    claim = candidate["claim"]
    kind = claim["kind"]
    families = {source["source_family"] for source in candidate["sources"]}

    if claim["resampled"] and not claim["source_support_preserved"]:
        reasons.append("SOURCE_SUPPORT_ERASURE_DENIED")
    if claim["county_intersection_only"] and claim["support_kind"] == "COUNTY":
        reasons.append("COUNTY_INTERSECTION_NOT_UNIFORM")
    if kind == "GROUNDWATER_CONDITION" and "USDM" in families:
        reasons.append("USDM_CANNOT_PROVE_GROUNDWATER")
    if kind == "GROUNDWATER_CONDITION" and "USGS_STREAMFLOW" in families:
        reasons.append("STREAMFLOW_CANNOT_PROVE_GROUNDWATER")
    if kind == "AGRICULTURAL_LOSS":
        reasons.append("CONTEXT_CANNOT_PROVE_AGRICULTURAL_LOSS")
    if (
        "WATER_MANAGEMENT_BOUNDARY" in families
        and kind != "MANAGEMENT_BOUNDARY_CONTEXT"
    ):
        reasons.append("BOUNDARY_CANNOT_PROVE_CONDITION")

    if kind == "CROSS_SOURCE_STRESS":
        if claim.get("transformation_ref") is None:
            reasons.append("DERIVATION_REFERENCE_REQUIRED")
    else:
        supported = DIRECT_SUPPORT.get(kind, set())
        if not families or not families.issubset(supported):
            if not any(code in reasons for code in ABSTAIN_CODES):
                reasons.append("SOURCE_FAMILY_CANNOT_DIRECTLY_SUPPORT_CLAIM")
    return reasons


def _material_change_reasons(candidate: Mapping[str, Any]) -> list[str]:
    material = candidate["material_change"]
    prior = material["prior_claim_digest"]
    current = material["current_claim_digest"]
    actual = prior is not None and prior != current
    if bool(material["declared_material"]) != actual:
        return ["MATERIAL_CHANGE_DECLARATION_MISMATCH"]
    return []


def assess(candidate: Any) -> Assessment:
    if not isinstance(candidate, Mapping) or not _schema_valid(candidate):
        return Assessment("ERROR", ("SCHEMA_INVALID",))

    reasons: list[str] = []
    if candidate["profile"] != PROFILE:
        reasons.append("PROFILE_INVALID")
    reasons.extend(_source_semantic_reasons(candidate))
    reasons.extend(_claim_reasons(candidate))
    reasons.extend(_material_change_reasons(candidate))

    if any(value is not False for value in candidate["governance"].values()):
        reasons.append("GOVERNANCE_BOUNDARY_VIOLATION")

    reasons = sorted(set(reasons))
    if any(code in ERROR_CODES for code in reasons):
        outcome = "ERROR"
    elif any(code in ABSTAIN_CODES for code in reasons):
        outcome = "ABSTAIN"
    elif "OBSERVATION_STALE" in reasons:
        outcome = "STALE"
    elif candidate["claim"]["source_conflict"]:
        reasons = sorted(set([*reasons, "SOURCE_CONFLICT"]))
        outcome = "CONFLICT"
    elif candidate["claim"]["kind"] == "CROSS_SOURCE_STRESS":
        outcome = "DERIVED"
    else:
        outcome = "OBSERVED"

    if candidate["outcome"] != outcome:
        reasons = sorted(set([*reasons, "DECLARED_OUTCOME_MISMATCH"]))
        outcome = "ERROR"
    return Assessment(outcome, tuple(reasons))


def validate_cases() -> int:
    try:
        value = _load_json(CASES_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(json.dumps({"outcome": "ERROR", "reason_codes": ["CASES_UNAVAILABLE"]}, sort_keys=True))
        return 1

    base_candidate = value.get("base_candidate") if isinstance(value, Mapping) else None
    cases = value.get("cases") if isinstance(value, Mapping) else None
    if not isinstance(base_candidate, Mapping) or not isinstance(cases, list) or not cases:
        print(json.dumps({"outcome": "ERROR", "reason_codes": ["CASES_INVALID"]}, sort_keys=True))
        return 1

    failed = False
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, Mapping) or not isinstance(case.get("case_id"), str):
            failed = True
            continue
        case_id = case["case_id"]
        if case_id in seen:
            failed = True
        seen.add(case_id)
        actual = assess(candidate_from_case(base_candidate, case))
        comparable = {"outcome": actual.outcome, "reason_codes": list(actual.reason_codes)}
        expected = case.get("expected")
        if comparable != expected:
            failed = True
            print(json.dumps({"case_id": case_id, "actual": comparable, "expected": expected}, sort_keys=True))
        else:
            print(json.dumps({"case_id": case_id, **comparable}, sort_keys=True))
    if failed:
        return 1
    print(f"CONFIRMED: {len(seen)} western Kansas observation cases passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.files:
            parser.error("--cases cannot be combined with files")
        return validate_cases()
    if not args.files:
        parser.error("provide one or more files or use --cases")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        try:
            result = assess(_load_json(path))
        except (OSError, UnicodeError, json.JSONDecodeError):
            result = Assessment("ERROR", ("INPUT_UNAVAILABLE",))
        print(json.dumps({"file": path.name, **result.as_dict()}, sort_keys=True))
        failed = failed or result.outcome == "ERROR"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
