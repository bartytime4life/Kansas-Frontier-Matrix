#!/usr/bin/env python3
"""Validate synthetic Agriculture public-safe map feature candidates."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import date
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
SCHEMA = ROOT / "schemas/contracts/v1/domains/agriculture/public_safe_map_feature.schema.json"
FIXTURES = ROOT / "fixtures/domains/agriculture/public_safe_map_feature/cases.json"
PROFILE = "kfm.domains.agriculture.public-safe-map-feature.v1"
PREFIX = "ag-map-feature:"
MAX_FINDINGS = 100

FAMILY_ROLES = {
    "CropObservation": {"OBSERVED_AGGREGATE"},
    "CropRotation": {"DERIVED_CONTEXT"},
    "YieldObservation": {"OBSERVED_AGGREGATE"},
    "IrrigationLink": {"IRRIGATION_CONTEXT"},
    "ConservationPractice": {"PRACTICE_CONTEXT"},
    "SoilCropSuitability": {"MODELED_SUITABILITY"},
    "AgriculturalEconomyObservation": {"ECONOMIC_AGGREGATE"},
    "SupplyChainNode": {"INFRASTRUCTURE_CONTEXT"},
    "DroughtStressIndicator": {"DERIVED_INDICATOR"},
    "PestStressIndicator": {"DERIVED_INDICATOR"},
}
FAMILY_INDICATOR_KEYS = {
    "CropObservation": {"cropland_class"},
    "CropRotation": {"crop_rotation_class"},
    "YieldObservation": {"yield_rate"},
    "IrrigationLink": {"irrigation_context_class"},
    "ConservationPractice": {"conservation_practice_context_class"},
    "SoilCropSuitability": {"soil_crop_suitability_index"},
    "AgriculturalEconomyObservation": {"agricultural_receipts"},
    "SupplyChainNode": {"supply_chain_context_class"},
    "DroughtStressIndicator": {"drought_stress_index"},
    "PestStressIndicator": {"pest_stress_index"},
}
SUPPORT_KEY_PATTERNS = {
    "COUNTY": re.compile(r"^US-KS-20[0-9]{3}$"),
    "REGION": re.compile(r"^KS-AG-[A-Z0-9]+(?:-[A-Z0-9]+)*-REGION-[0-9]{2}$"),
    "GENERALIZED_GRID": re.compile(r"^KS-GRID-[1-9][0-9]*KM-[0-9]{3}-[0-9]{3}$"),
}
SUPPORT_PRECISION = {
    "COUNTY": "AGGREGATE_PUBLIC_SAFE",
    "REGION": "GENERALIZED_PUBLIC_SAFE",
    "GENERALIZED_GRID": "GENERALIZED_PUBLIC_SAFE",
}
ROLE_SUPPORT = {
    "OBSERVED_AGGREGATE": {"COUNTY", "REGION"},
    "ECONOMIC_AGGREGATE": {"COUNTY", "REGION"},
    "DERIVED_CONTEXT": {"COUNTY", "REGION", "GENERALIZED_GRID"},
    "MODELED_SUITABILITY": {"COUNTY", "REGION", "GENERALIZED_GRID"},
    "DERIVED_INDICATOR": {"COUNTY", "REGION", "GENERALIZED_GRID"},
    "IRRIGATION_CONTEXT": {"COUNTY", "REGION"},
    "PRACTICE_CONTEXT": {"COUNTY", "REGION"},
    "INFRASTRUCTURE_CONTEXT": {"COUNTY", "REGION"},
}
ROLE_VALUE = {
    "OBSERVED_AGGREGATE": "OBSERVED",
    "ECONOMIC_AGGREGATE": "OBSERVED",
    "DERIVED_CONTEXT": "MODELED_OR_DERIVED",
    "MODELED_SUITABILITY": "MODELED_OR_DERIVED",
    "DERIVED_INDICATOR": "MODELED_OR_DERIVED",
    "IRRIGATION_CONTEXT": "CONTEXT_ONLY",
    "PRACTICE_CONTEXT": "CONTEXT_ONLY",
    "INFRASTRUCTURE_CONTEXT": "CONTEXT_ONLY",
}
FORBIDDEN_KEYS = {
    "geometry", "coordinates", "field_boundary", "field_geometry", "field_id",
    "farm_id", "operator_id", "operator_name", "owner", "owner_name",
    "parcel_id", "parcel_owner", "address", "street_address", "well_id",
    "permit_id", "water_right_id", "longitude", "latitude", "lon", "lat",
    "transform", "proprietary_yield", "input_rate", "application_rate",
}
FALSE_SENSITIVITY = {
    "exact_field_geometry": False,
    "operator_identity": False,
    "parcel_owner_join": False,
    "private_address": False,
    "sensitive_infrastructure": False,
    "proprietary_value": False,
    "transform_parameters": False,
}
FALSE_AUTHORITY = {
    "hydrology_observation": False,
    "water_right": False,
    "habitat_occurrence": False,
    "geology_truth": False,
    "atmosphere_forecast": False,
    "hazard_alert": False,
}
FALSE_RELEASE = {
    "state": "UNRELEASED_CANDIDATE",
    "policy_evaluated": False,
    "review_approved": False,
    "release_authorized": False,
    "public_use_allowed": False,
    "published": False,
}

PROTECTED_IDENTIFIER_PATTERN = re.compile(
    r"(?i)\b(?:parcel|field|farm|operator|owner|well|permit|water[-_ ]?right)"
    r"(?:[-_ ]?id)?\s*[:=#]\s*[a-z0-9][a-z0-9._/-]{2,}\b"
)
LABELED_COORDINATE_PATTERN = re.compile(
    r"(?i)\b(?:lat(?:itude)?|lon(?:gitude)?)\s*[:=]\s*[+-]?\d{1,3}\.\d+\b"
)
COORDINATE_PAIR_PATTERN = re.compile(
    r"(?<![\w.])([+-]?\d{1,3}\.\d{3,})\s*,\s*"
    r"([+-]?\d{1,3}\.\d{3,})(?![\w.])"
)
WKT_POINT_PATTERN = re.compile(
    r"(?i)\bpoint\s*\(\s*[+-]?\d{1,3}\.\d+\s+"
    r"[+-]?\d{1,3}\.\d+\s*\)"
)
EVIDENCE_REF_PATTERN = re.compile(
    r"^evidence:synthetic:agriculture:[a-z0-9]+(?:-[a-z0-9]+)*:v[1-9][0-9]*$"
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class StrictJSONError(ValueError):
    """Fail-closed JSON decoding error with a stable public finding."""

    def __init__(self, code: str, path: str = "/") -> None:
        super().__init__(code)
        self.finding = Finding(code, path)


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema() -> Mapping[str, Any]:
    return _strict_json_loads(SCHEMA.read_text(encoding="utf-8"))


def _reject_duplicate_members(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise StrictJSONError("AG_MAP_DUPLICATE_JSON_MEMBER", f"/{key}")
        value[key] = item
    return value


def _reject_nonfinite_constant(_: str) -> None:
    raise StrictJSONError("AG_MAP_NONFINITE_NUMBER_DENIED")


def _strict_json_loads(text: str) -> Any:
    return json.loads(
        text,
        object_pairs_hook=_reject_duplicate_members,
        parse_constant=_reject_nonfinite_constant,
    )


def _contains_coordinate_literal(value: str) -> bool:
    if LABELED_COORDINATE_PATTERN.search(value) or WKT_POINT_PATTERN.search(value):
        return True
    for match in COORDINATE_PAIR_PATTERN.finditer(value):
        first, second = (float(part) for part in match.groups())
        if ((abs(first) <= 90 and abs(second) <= 180)
                or (abs(first) <= 180 and abs(second) <= 90)):
            return True
    return False


def _unsafe_scalar_findings(value: Any, path: tuple[Any, ...] = ()) -> set[Finding]:
    findings: set[Finding] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            findings.update(_unsafe_scalar_findings(item, (*path, key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.update(_unsafe_scalar_findings(item, (*path, index)))
    elif isinstance(value, float) and not math.isfinite(value):
        findings.add(Finding("AG_MAP_NONFINITE_NUMBER_DENIED", _pointer(path)))
    elif isinstance(value, str):
        if (_contains_coordinate_literal(value)
                or PROTECTED_IDENTIFIER_PATTERN.search(value)):
            findings.add(Finding("AG_MAP_HARMFUL_PRECISION_DENIED", _pointer(path)))
    return findings


def _forbidden_key_findings(value: Any, path: tuple[Any, ...] = ()) -> set[Finding]:
    findings: set[Finding] = set()
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in FORBIDDEN_KEYS:
                findings.add(Finding("AG_MAP_HARMFUL_PRECISION_DENIED", _pointer((*path, key))))
            findings.update(_forbidden_key_findings(item, (*path, key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.update(_forbidden_key_findings(item, (*path, index)))
    return findings


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    validator = Draft202012Validator(_schema(), format_checker=FormatChecker())
    findings = {
        Finding("AG_MAP_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in islice(validator.iter_errors(value), MAX_FINDINGS)
    }
    return tuple(sorted(findings))


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("id", None)
    payload.pop("spec_hash", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    digest = canonical_hash(value)
    return f"sha256:{digest}", f"{PREFIX}{digest[:24]}"


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    family = value["object_family"]
    role = value["semantic_role"]
    support = value["support"]
    temporal = value["temporal"]
    freshness = value["freshness"]
    indicator = value["indicator"]

    if role not in FAMILY_ROLES[family]:
        findings.add(Finding("AG_MAP_FAMILY_ROLE_COLLAPSE", "/semantic_role"))
    if support["kind"] not in ROLE_SUPPORT[role]:
        findings.add(Finding("AG_MAP_SUPPORT_ROLE_COLLAPSE", "/support/kind"))
    if not SUPPORT_KEY_PATTERNS[support["kind"]].fullmatch(support["key"]):
        findings.add(Finding("AG_MAP_SUPPORT_KEY_KIND_MISMATCH", "/support/key"))
    if support["precision_class"] != SUPPORT_PRECISION[support["kind"]]:
        findings.add(Finding(
            "AG_MAP_SUPPORT_PRECISION_MISMATCH",
            "/support/precision_class",
        ))
    if role in FAMILY_ROLES[family] and indicator["key"] not in FAMILY_INDICATOR_KEYS[family]:
        findings.add(Finding("AG_MAP_INDICATOR_KEY_FAMILY_MISMATCH", "/indicator/key"))
    if indicator["value_role"] != ROLE_VALUE[role]:
        findings.add(Finding("AG_MAP_VALUE_ROLE_COLLAPSE", "/indicator/value_role"))

    start = date.fromisoformat(temporal["start"])
    end = date.fromisoformat(temporal["end"])
    vintage = date.fromisoformat(temporal["source_vintage"])
    year = temporal["year"]
    if start > end:
        findings.add(Finding("AG_MAP_TEMPORAL_INTERVAL_INVALID", "/temporal"))
    if temporal["kind"] == "CALENDAR_YEAR":
        if start != date(year, 1, 1):
            findings.add(Finding("AG_MAP_YEAR_START_MISMATCH", "/temporal/start"))
        if end != date(year, 12, 31):
            findings.add(Finding("AG_MAP_YEAR_END_MISMATCH", "/temporal/end"))
    elif not (start.year <= year <= end.year):
        findings.add(Finding("AG_MAP_YEAR_OUTSIDE_INTERVAL", "/temporal/year"))
    if vintage < end:
        findings.add(Finding("AG_MAP_SOURCE_VINTAGE_PRECEDES_PERIOD", "/temporal/source_vintage"))

    evaluated_at = date.fromisoformat(freshness["evaluated_at"])
    if evaluated_at < vintage:
        findings.add(Finding(
            "AG_MAP_FRESHNESS_EVALUATION_PRECEDES_VINTAGE",
            "/freshness/evaluated_at",
        ))
    else:
        age_days = (evaluated_at - vintage).days
        expected_state = "CURRENT" if age_days <= freshness["max_age_days"] else "STALE"
        if freshness["state"] != expected_state:
            findings.add(Finding("AG_MAP_FRESHNESS_STATE_MISMATCH", "/freshness/state"))

    evidence_refs = value["evidence_refs"]
    if evidence_refs != sorted(set(evidence_refs)):
        findings.add(Finding("AG_MAP_EVIDENCE_REFS_NONCANONICAL", "/evidence_refs"))
    for index, evidence_ref in enumerate(evidence_refs):
        if not EVIDENCE_REF_PATTERN.fullmatch(evidence_ref):
            findings.add(Finding(
                "AG_MAP_EVIDENCE_REF_NAMESPACE_MISMATCH",
                f"/evidence_refs/{index}",
            ))
    limitations = value["limitations"]
    if limitations != sorted(set(limitations)):
        findings.add(Finding("AG_MAP_LIMITATIONS_NONCANONICAL", "/limitations"))

    if value["sensitivity"] != FALSE_SENSITIVITY:
        findings.add(Finding("AG_MAP_SENSITIVITY_OVERCLAIM", "/sensitivity"))
    if value["authority"] != FALSE_AUTHORITY:
        findings.add(Finding("AG_MAP_AUTHORITY_OVERCLAIM", "/authority"))
    if value["release"] != FALSE_RELEASE:
        findings.add(Finding("AG_MAP_RELEASE_OVERCLAIM", "/release"))

    digest, identifier = canonical_identity(value)
    if value["spec_hash"] != digest:
        findings.add(Finding("AG_MAP_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value["id"] != identifier:
        findings.add(Finding("AG_MAP_ID_MISMATCH", "/id"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    precision = tuple(sorted(
        _forbidden_key_findings(value) | _unsafe_scalar_findings(value)
    ))
    if precision:
        return Result("DENY", precision)
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    return Result("PASS", ())


def _set(document: Any, pointer: str, replacement: Any) -> None:
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
    return _strict_json_loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set(document, mutation["path"], mutation.get("value"))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["id"] = case.get("id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append({
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual,
            })
    print(json.dumps(
        {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
        sort_keys=True, separators=(",", ":")
    ))
    return 0 if not failures else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixtures()
    if not args.path:
        parser.error("path or --fixtures required")
    try:
        value = _strict_json_loads(Path(args.path).read_text(encoding="utf-8"))
    except StrictJSONError as error:
        result = Result("DENY", (error.finding,))
    else:
        result = validate_payload(value)
    print(json.dumps({
        "outcome": result.outcome,
        "findings": [{"code": f.code, "path": f.path} for f in result.findings],
        "authority": "NONE",
        "execution_mode": "SYNTHETIC_NO_NETWORK",
    }, sort_keys=True, separators=(",", ":")))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
