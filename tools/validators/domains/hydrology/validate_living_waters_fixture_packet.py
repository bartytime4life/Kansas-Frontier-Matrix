#!/usr/bin/env python3
"""Validate one bounded, synthetic Living Waters proof packet."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json"
MAX_BYTES = 1_048_576
MAX_FINDINGS = 100
EXPECTED_SCENARIOS = {
    "current": ("AVAILABLE", "EXACT", "FIXTURE_EVIDENCE_RESOLVED"),
    "stale": ("STALE", "EXACT", "FRESHNESS_THRESHOLD_EXCEEDED"),
    "no-results": ("NO_RESULTS", "NOT_ATTEMPTED", "BOUNDED_QUERY_EMPTY"),
    "unavailable": ("UNAVAILABLE", "NOT_ATTEMPTED", "ARTIFACT_UNAVAILABLE"),
    "ambiguous-reach": ("ABSTAIN", "AMBIGUOUS", "MULTIPLE_REACH_CANDIDATES"),
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite number")
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _utc_instant_key(timestamp: str) -> tuple[str, str]:
    """Order a schema-validated UTC-Z timestamp without losing precision.

    The schema/format check must run first. Separate the fixed-width whole
    second from its fractional digits: a raw trailing Z sorts after a decimal
    point even though the whole second precedes its fractions. Remove only
    insignificant trailing zeros so alternate spellings of one instant compare
    equal. Fractional digits compare exactly without float rounding, integer
    conversion, or datetime's microsecond truncation. Preserve the input bytes;
    this key is not a general offset/leap-second parser or a timestamp rewrite.
    """
    whole_second, _, fraction = timestamp[:-1].partition(".")
    return whole_second.upper(), fraction.rstrip("0")


def validate_payload(payload: Mapping[str, Any]) -> tuple[Finding, ...]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(payload), MAX_FINDINGS + 1))
    findings = {
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    if findings:
        return tuple(sorted(findings))

    scenarios = payload["scenarios"]
    by_id = {item["id"]: item for item in scenarios}
    if set(by_id) != set(EXPECTED_SCENARIOS) or len(by_id) != len(scenarios):
        findings.add(Finding("SCENARIO_SET_INVALID", "/scenarios"))
    for scenario_id, (state, join, reason) in EXPECTED_SCENARIOS.items():
        item = by_id.get(scenario_id)
        if item is None:
            continue
        if (item["state"], item["join_outcome"]) != (state, join):
            findings.add(Finding("SCENARIO_OUTCOME_INVALID", f"/scenarios/{scenario_id}"))
        if reason not in item["reason_codes"]:
            findings.add(Finding("SCENARIO_REASON_MISSING", f"/scenarios/{scenario_id}/reason_codes"))

    points = payload["series"]["points"]
    timestamps = [_utc_instant_key(item["observed_at"]) for item in points]
    if timestamps != sorted(set(timestamps)):
        findings.add(Finding("HYDROGRAPH_TIME_ORDER_INVALID", "/series/points"))
    if payload["snapshot"]["reach_ids"] != sorted(payload["snapshot"]["reach_ids"]):
        findings.add(Finding("REACH_IDS_NOT_CANONICAL", "/snapshot/reach_ids"))
    return tuple(sorted(findings))


def validate_file(path: Path) -> tuple[Finding, ...]:
    try:
        if path.is_symlink():
            return (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return (Finding("FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return (Finding("FILE_TOO_LARGE", "/"),)
        payload = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite")), parse_float=_finite)
        if not isinstance(payload, dict):
            return (Finding("ROOT_NOT_OBJECT", "/"),)
        return validate_payload(payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("INPUT_INVALID", "/"),)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    findings = validate_file(args.path)
    print(json.dumps({
        "outcome": "PASS" if not findings else "FAIL",
        "findings": [{"code": item.code, "field": item.field} for item in findings],
        "authority": {"network_fetch": False, "source_admission": False, "source_activation": False, "policy_evaluation": False, "release": False, "deployment": False, "publication": False},
    }, sort_keys=True, separators=(",", ":")))
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
