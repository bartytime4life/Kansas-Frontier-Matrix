#!/usr/bin/env python3
"""Validate synthetic historical place/route proximity assessments.

The helper is deterministic, no-network, and no-write. It validates declared
time, uncertainty, source-role, interpretation, and non-authority coherence. It
does not resolve sources or evidence, calculate real geometry, establish a
historical relationship, evaluate policy, release, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/joins/"
    "historical_network_proximity_assessment.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/joins/"
    "historical_network_proximity_assessment/cases.json"
)
MAX_JSON_BYTES = 2 * 1024 * 1024
EXPECTED_LIMITATIONS = [
    "DISTANCE_IS_NOT_RELATIONSHIP",
    "NO_CAUSAL_OR_SERVICE_INFERENCE",
    "NO_GEOMETRY_EXECUTION",
    "NO_RELEASE_OR_PUBLICATION_AUTHORITY",
    "NO_SOURCE_OR_EVIDENCE_RESOLUTION",
]


class DuplicateKeyError(ValueError):
    """Raised when parsed JSON repeats an object member."""


class NonFiniteNumberError(ValueError):
    """Raised when parsed JSON contains a non-standard number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, Any]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, Any]:
    value = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("schema root must be an object")
    return value


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", _pointer(list(error.absolute_path)))
        for error in errors[:100]
    ]


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _interval(assertion: Mapping[str, Any]) -> tuple[datetime, datetime] | None:
    valid_time = assertion.get("valid_time")
    if not isinstance(valid_time, Mapping):
        return None
    start = _parse_utc(valid_time.get("start"))
    end = _parse_utc(valid_time.get("end"))
    if start is None or end is None or start >= end:
        return None
    return start, end


def calculated_temporal_overlap(candidate: Mapping[str, Any]) -> bool | None:
    place = candidate.get("place_assertion")
    route = candidate.get("route_assertion")
    if not isinstance(place, Mapping) or not isinstance(route, Mapping):
        return None
    place_interval = _interval(place)
    route_interval = _interval(route)
    if place_interval is None or route_interval is None:
        return None
    place_start, place_end = place_interval
    route_start, route_end = route_interval
    return place_start < route_end and route_start < place_end


def derive_interpretation(
    candidate: Mapping[str, Any],
) -> tuple[str, str, list[str]]:
    place = candidate.get("place_assertion")
    route = candidate.get("route_assertion")
    if not isinstance(place, Mapping) or not isinstance(route, Mapping):
        return "UNSUPPORTED", "ABSTAIN", ["ASSERTION_UNRESOLVED"]

    resolutions = {place.get("resolution"), route.get("resolution")}
    if "UNRESOLVED" in resolutions:
        return "UNSUPPORTED", "ABSTAIN", ["ASSERTION_UNRESOLVED"]
    if "AMBIGUOUS" in resolutions:
        return "AMBIGUOUS", "ABSTAIN", ["ASSERTION_AMBIGUOUS"]

    modern_reasons = []
    if place.get("source_role") == "MODERN_REFERENCE":
        modern_reasons.append("MODERN_PLACE_CONTEXT_ONLY")
    if route.get("source_role") == "MODERN_DESIGNATED_ALIGNMENT":
        modern_reasons.append("MODERN_ALIGNMENT_CONTEXT_ONLY")
    if modern_reasons:
        return "UNSUPPORTED", "ABSTAIN", sorted(modern_reasons)

    overlap = calculated_temporal_overlap(candidate)
    if overlap is False:
        return "NO_TEMPORAL_OVERLAP", "ABSTAIN", ["NO_TEMPORAL_OVERLAP"]
    if overlap is None:
        return "UNSUPPORTED", "ABSTAIN", ["ASSERTION_UNRESOLVED"]
    return "PROXIMITY_CANDIDATE", "CANDIDATE", ["QUALIFIED_PROXIMITY_ONLY"]


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()

    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))

    limitations = candidate.get("limitations")
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    evaluated_at = _parse_utc(candidate.get("evaluated_at"))
    if evaluated_at is None:
        findings.add(Finding("TIMESTAMP_NOT_UTC", "/evaluated_at"))

    place = candidate.get("place_assertion")
    route = candidate.get("route_assertion")
    proximity = candidate.get("proximity")
    interpretation = candidate.get("interpretation")
    conclusion = candidate.get("conclusion")
    if not all(
        isinstance(item, Mapping)
        for item in (place, route, proximity, interpretation, conclusion)
    ):
        return sorted(findings)
    assert isinstance(place, Mapping)
    assert isinstance(route, Mapping)
    assert isinstance(proximity, Mapping)
    assert isinstance(interpretation, Mapping)
    assert isinstance(conclusion, Mapping)

    for name, assertion in (("place", place), ("route", route)):
        valid_time = assertion.get("valid_time")
        if isinstance(valid_time, Mapping):
            start = _parse_utc(valid_time.get("start"))
            end = _parse_utc(valid_time.get("end"))
            if start is None:
                findings.add(
                    Finding("TIMESTAMP_NOT_UTC", f"/{name}_assertion/valid_time/start")
                )
            if end is None:
                findings.add(
                    Finding("TIMESTAMP_NOT_UTC", f"/{name}_assertion/valid_time/end")
                )
            if start is not None and end is not None and start >= end:
                findings.add(
                    Finding("VALID_TIME_ORDER_INVALID", f"/{name}_assertion/valid_time")
                )
        refs = assertion.get("evidence_refs")
        if not _canonical_strings(refs):
            findings.add(
                Finding("EVIDENCE_REFS_NOT_CANONICAL", f"/{name}_assertion/evidence_refs")
            )

    overlap = calculated_temporal_overlap(candidate)
    if overlap is not None and proximity.get("temporal_overlap") is not overlap:
        findings.add(Finding("TEMPORAL_OVERLAP_MISMATCH", "/proximity/temporal_overlap"))

    distance_min = proximity.get("distance_min_m")
    distance_max = proximity.get("distance_max_m")
    if isinstance(distance_min, int) and isinstance(distance_max, int):
        if distance_min > distance_max:
            findings.add(Finding("DISTANCE_BAND_INVALID", "/proximity"))

    place_uncertainty = place.get("uncertainty_m")
    route_uncertainty = route.get("uncertainty_m")
    combined = proximity.get("combined_uncertainty_m")
    if all(isinstance(value, int) for value in (place_uncertainty, route_uncertainty, combined)):
        if combined != place_uncertainty + route_uncertainty:
            findings.add(
                Finding("COMBINED_UNCERTAINTY_MISMATCH", "/proximity/combined_uncertainty_m")
            )

    if (
        place.get("coordinate_method")
        in {"APPROXIMATE_CENTROID", "UNCERTAINTY_ENVELOPE"}
        and place_uncertainty == 0
    ):
        findings.add(Finding("PLACE_UNCERTAINTY_REQUIRED", "/place_assertion/uncertainty_m"))

    if route.get("alignment_method") == "HISTORICAL_RECONSTRUCTION" and route_uncertainty == 0:
        findings.add(Finding("ROUTE_UNCERTAINTY_REQUIRED", "/route_assertion/uncertainty_m"))

    modern_role = route.get("source_role") == "MODERN_DESIGNATED_ALIGNMENT"
    modern_alignment = route.get("alignment_method") == "MODERN_DESIGNATED_ALIGNMENT"
    if modern_role != modern_alignment:
        findings.add(Finding("MODERN_ALIGNMENT_ROLE_MISMATCH", "/route_assertion"))

    expected_kind, expected_outcome, expected_reasons = derive_interpretation(candidate)
    if interpretation.get("relation_kind") != expected_kind:
        findings.add(
            Finding("INTERPRETATION_KIND_MISMATCH", "/interpretation/relation_kind")
        )
    if conclusion.get("declared_outcome") != expected_outcome:
        findings.add(
            Finding("DECLARED_OUTCOME_MISMATCH", "/conclusion/declared_outcome")
        )
    reason_codes = conclusion.get("reason_codes")
    if not _canonical_strings(reason_codes):
        findings.add(
            Finding("REASON_CODES_NOT_CANONICAL", "/conclusion/reason_codes")
        )
    elif reason_codes != expected_reasons:
        findings.add(Finding("REASON_CODES_MISMATCH", "/conclusion/reason_codes"))

    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    return ValidationResult("PASS" if not findings else "DENY", tuple(findings))


def _decode_pointer(pointer: str) -> list[str]:
    if not pointer.startswith("/") or pointer == "/":
        raise ValueError("fixture pointer is invalid")
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]


def _set_pointer(document: object, pointer: str, value: object) -> None:
    parts = _decode_pointer(pointer)
    target = document
    for part in parts[:-1]:
        if isinstance(target, list):
            target = target[int(part)]
        elif isinstance(target, dict):
            target = target[part]
        else:
            raise ValueError("fixture pointer cannot be traversed")
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    elif isinstance(target, dict):
        target[final] = copy.deepcopy(value)
    else:
        raise ValueError("fixture pointer target is invalid")


def materialize_fixture_case(
    manifest: Mapping[str, Any], entry: Mapping[str, Any]
) -> dict[str, Any]:
    base = manifest.get("base_candidate")
    if not isinstance(base, Mapping):
        raise ValueError("fixture base candidate is missing")
    candidate = copy.deepcopy(dict(base))
    changes = entry.get("set", {})
    if not isinstance(changes, Mapping):
        raise ValueError("fixture set map is invalid")
    for pointer in sorted(changes):
        if not isinstance(pointer, str):
            raise ValueError("fixture pointer is invalid")
        _set_pointer(candidate, pointer, changes[pointer])
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper_profile_hash") is True:
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({finding.code for finding in load_findings}),
                },
            }
        ]
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {"outcome": "ERROR", "codes": ["FIXTURE_CASES_INVALID"]},
            }
        ]

    results: list[dict[str, object]] = []
    for entry in cases:
        if not isinstance(entry, Mapping):
            results.append(
                {
                    "name": "invalid-entry",
                    "ok": False,
                    "observed": {"outcome": "ERROR", "codes": ["FIXTURE_CASE_INVALID"]},
                }
            )
            continue
        try:
            candidate = materialize_fixture_case(manifest, entry)
            result = validate_candidate(candidate)
            observed = {"outcome": result.outcome, "codes": result.codes}
        except (KeyError, IndexError, TypeError, ValueError, RecursionError):
            observed = {"outcome": "ERROR", "codes": ["FIXTURE_CASE_INVALID"]}
        expected = entry.get("expected")
        results.append(
            {
                "name": entry.get("name", "invalid-entry"),
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic historical network proximity assessments."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)

    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(result["ok"] for result in results) else 1

    candidate, load_findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(load_findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
