"""Validate fixture-only period-boundary predicate disclosures.

The validator proves closed shape, deterministic identity, UTC interval order,
declared boundary convention, endpoint relation, intersection shape, and local
reference ordering. It does not resolve claims, windows, or evidence; determine
temporal truth; decide policy or review; promote; release; deploy; publish; or
authorize public use.
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
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/period_boundary_predicate_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/period_boundary_predicate_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"CLAIM_SCOPE_UNRESOLVED", "WINDOW_REFERENCE_UNRESOLVED"}
PREDICATES = {
    "BEFORE",
    "MEETS",
    "OVERLAPS",
    "STARTS",
    "DURING",
    "FINISHES",
    "EQUALS",
    "FINISHED_BY",
    "CONTAINS",
    "STARTED_BY",
    "OVERLAPPED_BY",
    "MET_BY",
    "AFTER",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


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


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
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
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _instant(value: object) -> datetime:
    assert isinstance(value, str)
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _interval(window: Mapping[str, object]) -> tuple[datetime, datetime]:
    return _instant(window["start"]), _instant(window["end"])


def compute_predicate(
    left: Mapping[str, object], right: Mapping[str, object]
) -> str:
    """Return the finite endpoint-order relation for two proper intervals."""

    left_start, left_end = _interval(left)
    right_start, right_end = _interval(right)
    if left_end < right_start:
        return "BEFORE"
    if left_end == right_start:
        return "MEETS"
    if left_start > right_end:
        return "AFTER"
    if left_start == right_end:
        return "MET_BY"
    if left_start == right_start and left_end == right_end:
        return "EQUALS"
    if left_start == right_start:
        return "STARTS" if left_end < right_end else "STARTED_BY"
    if left_end == right_end:
        return "FINISHES" if left_start > right_start else "FINISHED_BY"
    if right_start < left_start and left_end < right_end:
        return "DURING"
    if left_start < right_start and right_end < left_end:
        return "CONTAINS"
    if left_start < right_start < left_end < right_end:
        return "OVERLAPS"
    if right_start < left_start < right_end < left_end:
        return "OVERLAPPED_BY"
    raise ValueError("proper finite intervals must have one supported relation")


def _contains(window: Mapping[str, object], instant: datetime) -> bool:
    start, end = _interval(window)
    if instant == start:
        return bool(window["start_inclusive"])
    if instant == end:
        return bool(window["end_inclusive"])
    return start < instant < end


def compute_intersection_shape(
    left: Mapping[str, object], right: Mapping[str, object]
) -> str:
    left_start, left_end = _interval(left)
    right_start, right_end = _interval(right)
    lower = max(left_start, right_start)
    upper = min(left_end, right_end)
    if lower < upper:
        return "INTERVAL"
    if lower > upper:
        return "EMPTY"
    return "POINT" if _contains(left, lower) and _contains(right, lower) else "EMPTY"


def _convention_matches(candidate: Mapping[str, object]) -> bool:
    left = candidate["left_window"]
    right = candidate["right_window"]
    assert isinstance(left, Mapping) and isinstance(right, Mapping)
    left_pattern = (left["start_inclusive"], left["end_inclusive"])
    right_pattern = (right["start_inclusive"], right["end_inclusive"])
    convention = candidate["interval_convention"]
    patterns = {
        "CLOSED": (True, True),
        "OPEN": (False, False),
        "LEFT_CLOSED_RIGHT_OPEN": (True, False),
        "LEFT_OPEN_RIGHT_CLOSED": (False, True),
    }
    if convention == "MIXED_EXPLICIT":
        return left_pattern != right_pattern
    expected = patterns[convention]
    return left_pattern == expected and right_pattern == expected


def _canonical_refs(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    claim_scope = candidate["claim_scope"]
    assert isinstance(claim_scope, Mapping)
    if claim_scope["resolution"] == "UNRESOLVED":
        findings.add(Finding("CLAIM_SCOPE_UNRESOLVED", "/claim_scope/resolution"))

    left = candidate["left_window"]
    right = candidate["right_window"]
    assert isinstance(left, Mapping) and isinstance(right, Mapping)
    intervals_valid = True
    for name, window in (("left_window", left), ("right_window", right)):
        if window["resolution"] == "UNRESOLVED":
            findings.add(Finding("WINDOW_REFERENCE_UNRESOLVED", f"/{name}/resolution"))
        for endpoint in ("start", "end"):
            if not _is_utc(window[endpoint]):
                findings.add(Finding("UTC_TIMESTAMP_REQUIRED", f"/{name}/{endpoint}"))
        start, end = _interval(window)
        if start >= end:
            intervals_valid = False
            findings.add(Finding("INTERVAL_ORDER_INVALID", f"/{name}"))

    if not _convention_matches(candidate):
        findings.add(Finding("INTERVAL_CONVENTION_MISMATCH", "/interval_convention"))
    if not _canonical_refs(candidate["evidence_refs"]):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs"))

    if intervals_valid:
        if candidate["declared_predicate"] != compute_predicate(left, right):
            findings.add(Finding("PREDICATE_MISMATCH", "/declared_predicate"))
        if candidate["declared_intersection_shape"] != compute_intersection_shape(left, right):
            findings.add(Finding("INTERSECTION_SHAPE_MISMATCH", "/declared_intersection_shape"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
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
                    "codes": sorted({item.code for item in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only period-boundary predicate disclosures."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
