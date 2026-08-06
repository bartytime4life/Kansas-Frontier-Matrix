#!/usr/bin/env python3
"""Validate synthetic U.S. Drought Monitor material-change assessments.

The profile compares immutable weekly snapshots without fetching USDM data. It
keeps weekly expert classification separate from precipitation, groundwater,
reservoir, impact, forecast, and legal drought-declaration records. A green
result proves only deterministic comparison semantics for committed fixtures.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hazards/usdm_materiality"
CASES_PATH = FIXTURE_ROOT / "cases.json"
PROFILE = "kfm-usdm-materiality-v1"
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
STATES = frozenset({"UNCHANGED", "SEMANTIC_NON_MATERIAL", "MATERIAL", "UNDETERMINED"})
OUTCOMES = {
    "UNCHANGED": "NON_EVENT",
    "SEMANTIC_NON_MATERIAL": "NON_EVENT",
    "MATERIAL": "PROMOTION_CANDIDATE",
    "UNDETERMINED": "HOLD",
}
AREA_FIELDS = ("d1_d4", "d2_d4", "d3_d4", "d4")


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Assessment:
    state: str
    outcome: str
    triggered_criteria: tuple[str, ...]


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    computed: Assessment | None

    @property
    def ok(self) -> bool:
        return not self.findings


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _percent(value: Any) -> float | None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) and 0 <= parsed <= 100 else None


def _integer(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def _date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _valid_digest(value: Any) -> bool:
    return isinstance(value, str) and SHA256.fullmatch(value) is not None and set(value[7:]) != {"0"}


def _snapshot_findings(snapshot: Mapping[str, Any], field: str) -> list[Finding]:
    findings: list[Finding] = []
    allowed = {"valid_date", "geometry_digest", "area_percent", "population_in_drought"}
    for name in sorted(set(snapshot) - allowed):
        findings.append(Finding("UNEXPECTED_SNAPSHOT_FIELD", f"{field}/{name}"))
    if _date(snapshot.get("valid_date")) is None:
        findings.append(Finding("VALID_DATE_INVALID", field + "/valid_date"))
    if not _valid_digest(snapshot.get("geometry_digest")):
        findings.append(Finding("GEOMETRY_DIGEST_INVALID", field + "/geometry_digest"))
    areas = _mapping(snapshot.get("area_percent"))
    values: dict[str, float] = {}
    for name in AREA_FIELDS:
        parsed = _percent(areas.get(name))
        if parsed is None:
            findings.append(Finding("AREA_PERCENT_INVALID", f"{field}/area_percent/{name}"))
        else:
            values[name] = parsed
    if len(values) == len(AREA_FIELDS) and not (values["d4"] <= values["d3_d4"] <= values["d2_d4"] <= values["d1_d4"]):
        findings.append(Finding("SEVERITY_AREA_HIERARCHY_INVALID", field + "/area_percent"))
    if _integer(snapshot.get("population_in_drought")) is None:
        findings.append(Finding("POPULATION_INVALID", field + "/population_in_drought"))
    return findings


def compute_assessment(candidate: Mapping[str, Any]) -> Assessment:
    previous = _mapping(candidate.get("previous"))
    current = _mapping(candidate.get("current"))
    thresholds = _mapping(candidate.get("thresholds"))
    previous_areas = _mapping(previous.get("area_percent"))
    current_areas = _mapping(current.get("area_percent"))
    statewide = float(thresholds.get("statewide_area_percentage_points"))
    severe = float(thresholds.get("severe_area_percentage_points"))
    population_fraction = float(thresholds.get("population_change_fraction"))

    criteria: list[str] = []
    changes = {name: abs(float(current_areas[name]) - float(previous_areas[name])) for name in AREA_FIELDS}
    if changes["d1_d4"] >= statewide:
        criteria.append("D1_D4_AREA_THRESHOLD")
    if changes["d2_d4"] >= severe:
        criteria.append("D2_D4_AREA_THRESHOLD")
    if changes["d3_d4"] >= severe:
        criteria.append("D3_D4_AREA_THRESHOLD")
    if changes["d4"] >= severe:
        criteria.append("D4_AREA_THRESHOLD")
    if float(previous_areas["d3_d4"]) == 0 and float(current_areas["d3_d4"]) > 0:
        criteria.append("D3_APPEARED")
    if float(previous_areas["d4"]) == 0 and float(current_areas["d4"]) > 0:
        criteria.append("D4_APPEARED")

    previous_population = int(previous["population_in_drought"])
    current_population = int(current["population_in_drought"])
    denominator = max(previous_population, 1)
    if abs(current_population - previous_population) / denominator >= population_fraction:
        criteria.append("POPULATION_THRESHOLD")

    geometry_changed = previous.get("geometry_digest") != current.get("geometry_digest")
    metrics_changed = any(value > 0 for value in changes.values()) or previous_population != current_population
    if geometry_changed and metrics_changed:
        criteria.append("GEOMETRY_CHANGED_WITH_METRICS")
    elif geometry_changed and not metrics_changed:
        return Assessment("UNDETERMINED", "HOLD", ("GEOMETRY_CHANGED_WITHOUT_METRICS",))

    if not geometry_changed and not metrics_changed:
        return Assessment("UNCHANGED", "NON_EVENT", ())
    if criteria:
        return Assessment("MATERIAL", "PROMOTION_CANDIDATE", tuple(sorted(set(criteria))))
    return Assessment("SEMANTIC_NON_MATERIAL", "NON_EVENT", ())


def validate_candidate(candidate: Mapping[str, Any]) -> ValidationResult:
    findings: list[Finding] = []
    if candidate.get("profile") != PROFILE:
        findings.append(Finding("PROFILE_INVALID", "/profile"))
    if candidate.get("fixture_only") is not True:
        findings.append(Finding("FIXTURE_ONLY_REQUIRED", "/fixture_only"))
    if candidate.get("network_access") != "forbidden":
        findings.append(Finding("NETWORK_ACCESS_NOT_FORBIDDEN", "/network_access"))
    previous = _mapping(candidate.get("previous"))
    current = _mapping(candidate.get("current"))
    findings.extend(_snapshot_findings(previous, "/previous"))
    findings.extend(_snapshot_findings(current, "/current"))
    previous_date = _date(previous.get("valid_date"))
    current_date = _date(current.get("valid_date"))
    if previous_date is not None and current_date is not None and current_date <= previous_date:
        findings.append(Finding("SNAPSHOT_TIME_ORDER_INVALID", "/current/valid_date"))

    thresholds = _mapping(candidate.get("thresholds"))
    for name in ("statewide_area_percentage_points", "severe_area_percentage_points"):
        value = thresholds.get(name)
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)) or float(value) <= 0:
            findings.append(Finding("THRESHOLD_INVALID", f"/thresholds/{name}"))
    fraction = thresholds.get("population_change_fraction")
    if not isinstance(fraction, (int, float)) or isinstance(fraction, bool) or not math.isfinite(float(fraction)) or not 0 < float(fraction) <= 1:
        findings.append(Finding("THRESHOLD_INVALID", "/thresholds/population_change_fraction"))

    governance = _mapping(candidate.get("governance"))
    if any(governance.get(name) is not False for name in ("authority_created", "source_activated", "promotion_authorized", "release_authorized", "publication_authorized")):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    computed: Assessment | None = None
    if not findings:
        computed = compute_assessment(candidate)
        declared = _mapping(candidate.get("assessment"))
        declared_criteria = declared.get("triggered_criteria")
        if declared.get("state") not in STATES or declared.get("outcome") not in set(OUTCOMES.values()) or not isinstance(declared_criteria, list):
            findings.append(Finding("ASSESSMENT_SHAPE_INVALID", "/assessment"))
        else:
            if declared.get("outcome") != OUTCOMES.get(str(declared.get("state"))):
                findings.append(Finding("STATE_OUTCOME_MISMATCH", "/assessment/outcome"))
            if (
                declared.get("state") != computed.state
                or declared.get("outcome") != computed.outcome
                or tuple(declared_criteria) != computed.triggered_criteria
            ):
                findings.append(Finding("DECLARED_ASSESSMENT_MISMATCH", "/assessment"))
    return ValidationResult(tuple(sorted(set(findings))), computed)


def validate_file(path: Path) -> ValidationResult:
    try:
        if path.is_symlink():
            return ValidationResult((Finding("INPUT_SYMLINK_DENIED", "/"),), None)
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return ValidationResult((Finding("FILE_NOT_FOUND", "/"),), None)
    except (OSError, UnicodeError):
        return ValidationResult((Finding("FILE_READ_ERROR", "/"),), None)
    except json.JSONDecodeError:
        return ValidationResult((Finding("JSON_INVALID", "/"),), None)
    if not isinstance(value, dict):
        return ValidationResult((Finding("ROOT_NOT_OBJECT", "/"),), None)
    return validate_candidate(value)


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "assessment": None if result.computed is None else {"outcome": result.computed.outcome, "state": result.computed.state, "triggered_criteria": list(result.computed.triggered_criteria)},
            "file": path.as_posix(),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else "FAIL",
            "profile": PROFILE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _apply_case_patch(base: Mapping[str, Any], changes: Mapping[str, Any]) -> dict[str, Any]:
    import copy

    candidate = copy.deepcopy(dict(base))
    for pointer, value in sorted(changes.items()):
        if not isinstance(pointer, str) or not pointer.startswith("/"):
            raise ValueError
        parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
        target: Any = candidate
        for part in parts[:-1]:
            target = target[int(part)] if isinstance(target, list) else target[part]
        final = parts[-1]
        if isinstance(value, Mapping) and value.get("$delete") is True:
            if isinstance(target, list):
                del target[int(final)]
            else:
                del target[final]
        elif isinstance(target, list):
            target[int(final)] = value
        else:
            target[final] = value
    return candidate


def fixture_cases() -> tuple[dict[str, Mapping[str, Any]], list[tuple[str, Mapping[str, Any], list[str]]]]:
    value = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("valid"), list) or not isinstance(value.get("invalid"), list):
        raise ValueError
    valid = {str(entry["name"]): entry["candidate"] for entry in value["valid"] if isinstance(entry, Mapping) and isinstance(entry.get("candidate"), Mapping)}
    if len(valid) != len(value["valid"]):
        raise ValueError
    invalid: list[tuple[str, Mapping[str, Any], list[str]]] = []
    for entry in value["invalid"]:
        if not isinstance(entry, Mapping) or str(entry.get("base")) not in valid or not isinstance(entry.get("set"), Mapping) or not isinstance(entry.get("expected"), list):
            raise ValueError
        invalid.append((str(entry.get("name", "invalid")), _apply_case_patch(valid[str(entry["base"])], entry["set"]), [str(code) for code in entry["expected"]]))
    return valid, invalid


def validate_fixtures() -> int:
    try:
        valid_cases, invalid_cases = fixture_cases()
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError):
        print("ERROR: USDM case manifest unavailable or invalid")
        return 1
    if not valid_cases or not invalid_cases:
        print("ERROR: USDM case lanes must be non-empty")
        return 1
    failed = False
    for name, candidate in sorted(valid_cases.items()):
        result = validate_candidate(candidate)
        print(_serialize(Path(name + ".json"), result))
        failed = failed or not result.ok
    for name, candidate, expected in invalid_cases:
        result = validate_candidate(candidate)
        print(_serialize(Path(name + ".json"), result))
        actual = sorted({item.code for item in result.findings})
        failed = failed or result.ok or actual != sorted(expected)
    return 1 if failed else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_file(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
