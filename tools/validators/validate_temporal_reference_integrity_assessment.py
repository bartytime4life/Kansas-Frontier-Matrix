"""Validate fixture-only temporal reference-integrity assessments.

The validator checks local record-presence declarations and finite interval
relations. It does not resolve a reference, inspect or mutate a database,
execute a constraint or quarantine, decide policy or review, release, publish,
or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/temporal_reference_integrity_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/temporal_reference_integrity_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "SUBJECT_RECORD_UNRESOLVED",
    "TARGET_RECORD_UNRESOLVED",
    "SUBJECT_WINDOW_UNRESOLVED",
    "TARGET_WINDOW_UNRESOLVED",
}
AXES_BY_MODE = {
    "VALID_TIME": ["VALID_TIME"],
    "TRANSACTION_TIME": ["TRANSACTION_TIME"],
    "BITEMPORAL": ["VALID_TIME", "TRANSACTION_TIME"],
}
TARGET_KIND_BY_ROLE = {
    "SOURCE_VERSION": "SOURCE_VERSION",
    "GEOGRAPHY_VERSION": "GEOGRAPHY_VERSION",
    "IDENTITY_VERSION": "IDENTITY_VERSION",
    "OTHER": "OTHER",
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
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
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


def _contains(window: Mapping[str, object], instant: datetime) -> bool:
    start, end = _interval(window)
    if instant == start:
        return bool(window["start_inclusive"])
    if instant == end:
        return bool(window["end_inclusive"])
    return start < instant < end


def _subject_within_target(
    subject: Mapping[str, object], target: Mapping[str, object]
) -> bool:
    subject_start, subject_end = _interval(subject)
    target_start, target_end = _interval(target)
    lower_ok = subject_start > target_start or (
        subject_start == target_start
        and (not bool(subject["start_inclusive"]) or bool(target["start_inclusive"]))
    )
    upper_ok = subject_end < target_end or (
        subject_end == target_end
        and (not bool(subject["end_inclusive"]) or bool(target["end_inclusive"]))
    )
    return lower_ok and upper_ok


def _overlaps(
    subject: Mapping[str, object], target: Mapping[str, object]
) -> bool:
    subject_start, subject_end = _interval(subject)
    target_start, target_end = _interval(target)
    lower = max(subject_start, target_start)
    upper = min(subject_end, target_end)
    if lower < upper:
        return True
    if lower > upper:
        return False
    return _contains(subject, lower) and _contains(target, lower)


def evaluate_constraint(
    constraint: str,
    subject: Mapping[str, object],
    target: Mapping[str, object],
) -> bool:
    if constraint == "SUBJECT_WITHIN_TARGET":
        return _subject_within_target(subject, target)
    if constraint == "SUBJECT_OVERLAPS_TARGET":
        return _overlaps(subject, target)
    if constraint == "SUBJECT_START_WITHIN_TARGET":
        return _contains(target, _interval(subject)[0])
    if constraint == "SUBJECT_END_WITHIN_TARGET":
        return _contains(target, _interval(subject)[1])
    raise ValueError(f"unsupported constraint: {constraint}")


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("assessed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/assessed_at"))

    subject = candidate["subject"]
    target = candidate["target"]
    assert isinstance(subject, Mapping) and isinstance(target, Mapping)
    if subject["ref"] == target["ref"]:
        findings.add(Finding("SELF_REFERENCE_INVALID", "/target/ref"))
    if target["record_kind"] != TARGET_KIND_BY_ROLE[candidate["target_role"]]:
        findings.add(Finding("TARGET_ROLE_KIND_MISMATCH", "/target/record_kind"))

    subject_presence = subject["presence"]
    target_presence = target["presence"]
    if subject_presence == "MISSING":
        findings.add(Finding("SUBJECT_RECORD_MISSING", "/subject/presence"))
    elif subject_presence == "UNRESOLVED":
        findings.add(Finding("SUBJECT_RECORD_UNRESOLVED", "/subject/presence"))
    if target_presence == "MISSING":
        findings.add(Finding("TARGET_RECORD_MISSING", "/target/presence"))
    elif target_presence == "UNRESOLVED":
        findings.add(Finding("TARGET_RECORD_UNRESOLVED", "/target/presence"))

    checks = candidate["checks"]
    assert isinstance(checks, list)
    observed_axes = [check["axis"] for check in checks]
    expected_axes = AXES_BY_MODE[candidate["temporal_mode"]]
    if observed_axes != expected_axes:
        findings.add(Finding("TEMPORAL_AXIS_SET_MISMATCH", "/checks"))

    window_unresolved = False
    interval_invalid = False
    relation_violated = False
    for index, check in enumerate(checks):
        subject_window = check["subject_window"]
        target_window = check["target_window"]
        assert isinstance(subject_window, Mapping) and isinstance(target_window, Mapping)
        local_unresolved = False
        local_valid = True
        for side, window in (("subject", subject_window), ("target", target_window)):
            if window["resolution"] == "UNRESOLVED":
                window_unresolved = True
                local_unresolved = True
                code = "SUBJECT_WINDOW_UNRESOLVED" if side == "subject" else "TARGET_WINDOW_UNRESOLVED"
                findings.add(Finding(code, f"/checks/{index}/{side}_window/resolution"))
            for endpoint in ("start", "end"):
                if not _is_utc(window[endpoint]):
                    local_valid = False
                    interval_invalid = True
                    findings.add(Finding("UTC_TIMESTAMP_REQUIRED", f"/checks/{index}/{side}_window/{endpoint}"))
            start, end = _interval(window)
            if start >= end:
                local_valid = False
                interval_invalid = True
                findings.add(Finding("INTERVAL_ORDER_INVALID", f"/checks/{index}/{side}_window"))

        expected_state: str | None = None
        if local_unresolved:
            expected_state = "UNRESOLVED"
        elif local_valid:
            satisfied = evaluate_constraint(check["constraint"], subject_window, target_window)
            expected_state = "SATISFIED" if satisfied else "VIOLATED"
            if not satisfied:
                relation_violated = True
                findings.add(Finding("TEMPORAL_REFERENCE_INVALID", f"/checks/{index}"))
        if expected_state is not None and check["declared_state"] != expected_state:
            findings.add(Finding("CHECK_STATE_MISMATCH", f"/checks/{index}/declared_state"))

    record_missing = subject_presence == "MISSING" or target_presence == "MISSING"
    record_unresolved = subject_presence == "UNRESOLVED" or target_presence == "UNRESOLVED"
    if record_missing or interval_invalid or relation_violated:
        expected_overall = "VIOLATED"
    elif record_unresolved or window_unresolved:
        expected_overall = "UNRESOLVED"
    else:
        expected_overall = "SATISFIED"
    if candidate["declared_overall_state"] != expected_overall:
        findings.add(Finding("OVERALL_STATE_MISMATCH", "/declared_overall_state"))

    handling = candidate["failure_handling"]
    assert isinstance(handling, Mapping)
    review_refs = handling["review_record_refs"]
    if not _canonical_strings(review_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/failure_handling/review_record_refs"))
    action = handling["recommended_action"]
    if expected_overall == "VIOLATED":
        if action not in {"DENY_CANDIDATE", "QUARANTINE_CANDIDATE"}:
            findings.add(Finding("FAILURE_ACTION_REQUIRED", "/failure_handling/recommended_action"))
        if not review_refs:
            findings.add(Finding("FAILURE_REVIEW_REFERENCE_REQUIRED", "/failure_handling/review_record_refs"))
    elif action != "NONE":
        findings.add(Finding("FAILURE_ACTION_MISMATCH", "/failure_handling/recommended_action"))

    if not _canonical_strings(candidate["evidence_refs"]):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/evidence_refs"))
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
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only temporal reference-integrity assessments."
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
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
