"""Validate fixture-only temporal uniqueness assessments.

The validator compares declared finite intervals for opaque same-key records.
It does not inspect a table, resolve a reference, execute a constraint or
quarantine, decide policy or review, release, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/temporal_uniqueness_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/temporal_uniqueness_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "KEY_PROFILE_UNRESOLVED",
    "OVERLAP_POLICY_UNRESOLVED",
    "SUBJECT_RECORD_UNRESOLVED",
    "PEER_RECORD_UNRESOLVED",
    "SUBJECT_WINDOW_UNRESOLVED",
    "PEER_WINDOW_UNRESOLVED",
}
AXES_BY_MODE = {
    "VALID_TIME": ["VALID_TIME"],
    "TRANSACTION_TIME": ["TRANSACTION_TIME"],
    "BITEMPORAL": ["VALID_TIME", "TRANSACTION_TIME"],
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


def intervals_overlap(
    subject: Mapping[str, object], peer: Mapping[str, object]
) -> bool:
    subject_start, subject_end = _interval(subject)
    peer_start, peer_end = _interval(peer)
    lower = max(subject_start, peer_start)
    upper = min(subject_end, peer_end)
    if lower < upper:
        return True
    if lower > upper:
        return False
    return _contains(subject, lower) and _contains(peer, lower)


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

    key_profile = candidate["key_profile"]
    policy = candidate["overlap_policy"]
    subject = candidate["subject"]
    assert isinstance(key_profile, Mapping)
    assert isinstance(policy, Mapping)
    assert isinstance(subject, Mapping)
    if key_profile["resolution"] == "UNRESOLVED":
        findings.add(Finding("KEY_PROFILE_UNRESOLVED", "/key_profile/resolution"))
    if policy["resolution"] == "UNRESOLVED":
        findings.add(Finding("OVERLAP_POLICY_UNRESOLVED", "/overlap_policy/resolution"))
    if subject["presence"] == "UNRESOLVED":
        findings.add(Finding("SUBJECT_RECORD_UNRESOLVED", "/subject/presence"))
    if not _canonical_strings(key_profile["identity_field_refs"]):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/key_profile/identity_field_refs"))

    exception_refs = policy["exception_review_refs"]
    if not _canonical_strings(exception_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/overlap_policy/exception_review_refs"))
    if policy["mode"] != "ALLOW_REVIEWED_PARALLEL" and exception_refs:
        findings.add(Finding("EXCEPTION_REVIEW_REFERENCE_UNEXPECTED", "/overlap_policy/exception_review_refs"))

    comparisons = candidate["comparisons"]
    assert isinstance(comparisons, list)
    peer_refs = [comparison["peer"]["ref"] for comparison in comparisons]
    if len(peer_refs) != len(set(peer_refs)):
        findings.add(Finding("PEER_REFERENCE_DUPLICATE", "/comparisons"))

    expected_axes = AXES_BY_MODE[key_profile["temporal_mode"]]
    comparison_unresolved = False
    classification_blocked = False
    pair_states: list[tuple[bool, bool]] = []
    for comparison_index, comparison in enumerate(comparisons):
        peer = comparison["peer"]
        axes = comparison["axes"]
        assert isinstance(peer, Mapping) and isinstance(axes, list)
        if peer["ref"] == subject["ref"]:
            findings.add(Finding("SELF_COMPARISON_INVALID", f"/comparisons/{comparison_index}/peer/ref"))
        if peer["key_digest"] != subject["key_digest"]:
            findings.add(Finding("TEMPORAL_KEY_DIGEST_MISMATCH", f"/comparisons/{comparison_index}/peer/key_digest"))
        if peer["presence"] == "UNRESOLVED":
            comparison_unresolved = True
            findings.add(Finding("PEER_RECORD_UNRESOLVED", f"/comparisons/{comparison_index}/peer/presence"))

        lineage_relation = comparison["lineage_relation"]
        lineage_ref = comparison["lineage_ref"]
        if lineage_relation == "NONE" and lineage_ref is not None:
            findings.add(Finding("LINEAGE_REFERENCE_UNEXPECTED", f"/comparisons/{comparison_index}/lineage_ref"))
        elif lineage_relation != "NONE" and lineage_ref is None:
            findings.add(Finding("LINEAGE_REFERENCE_REQUIRED", f"/comparisons/{comparison_index}/lineage_ref"))

        observed_axes = [axis["axis"] for axis in axes]
        if observed_axes != expected_axes:
            classification_blocked = True
            findings.add(Finding("TEMPORAL_AXIS_SET_MISMATCH", f"/comparisons/{comparison_index}/axes"))

        axis_overlaps: list[bool] = []
        local_unresolved = peer["presence"] == "UNRESOLVED"
        local_invalid = False
        for axis_index, axis in enumerate(axes):
            subject_window = axis["subject_window"]
            peer_window = axis["peer_window"]
            assert isinstance(subject_window, Mapping) and isinstance(peer_window, Mapping)
            axis_unresolved = False
            axis_valid = True
            for side, window in (("subject", subject_window), ("peer", peer_window)):
                if window["resolution"] == "UNRESOLVED":
                    axis_unresolved = True
                    local_unresolved = True
                    comparison_unresolved = True
                    code = "SUBJECT_WINDOW_UNRESOLVED" if side == "subject" else "PEER_WINDOW_UNRESOLVED"
                    findings.add(Finding(code, f"/comparisons/{comparison_index}/axes/{axis_index}/{side}_window/resolution"))
                for endpoint in ("start", "end"):
                    if not _is_utc(window[endpoint]):
                        axis_valid = False
                        local_invalid = True
                        classification_blocked = True
                        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", f"/comparisons/{comparison_index}/axes/{axis_index}/{side}_window/{endpoint}"))
                start, end = _interval(window)
                if start >= end:
                    axis_valid = False
                    local_invalid = True
                    classification_blocked = True
                    findings.add(Finding("INTERVAL_ORDER_INVALID", f"/comparisons/{comparison_index}/axes/{axis_index}/{side}_window"))

            expected_overlap: str | None = None
            if axis_unresolved:
                expected_overlap = "UNRESOLVED"
            elif axis_valid:
                overlap = intervals_overlap(subject_window, peer_window)
                axis_overlaps.append(overlap)
                expected_overlap = "OVERLAPS" if overlap else "DISJOINT"
            if expected_overlap is not None and axis["declared_overlap"] != expected_overlap:
                findings.add(Finding("AXIS_OVERLAP_MISMATCH", f"/comparisons/{comparison_index}/axes/{axis_index}/declared_overlap"))

        pair_conflict = False
        pair_resolved = not local_unresolved and not local_invalid and len(axis_overlaps) == len(expected_axes)
        if pair_resolved:
            pair_conflict = (
                any(axis_overlaps)
                if key_profile["pair_conflict_rule"] == "ANY_DECLARED_AXIS_OVERLAP"
                else all(axis_overlaps)
            )
        pair_states.append((pair_resolved, pair_conflict))

    known_conflict_indexes = [
        index for index, (resolved, conflict) in enumerate(pair_states) if resolved and conflict
    ]
    disallowed_conflict = False
    if policy["mode"] == "DENY_OVERLAP":
        disallowed_conflict = bool(known_conflict_indexes)
    elif policy["mode"] == "ALLOW_WITH_SUPERSESSION":
        for index in known_conflict_indexes:
            comparison = comparisons[index]
            if comparison["lineage_relation"] == "NONE" or comparison["lineage_ref"] is None:
                disallowed_conflict = True
                findings.add(Finding("SUPERSESSION_LINEAGE_REQUIRED", f"/comparisons/{index}"))
    elif policy["mode"] == "ALLOW_REVIEWED_PARALLEL" and known_conflict_indexes and not exception_refs:
        disallowed_conflict = True
        findings.add(Finding("OVERLAP_REVIEW_REFERENCE_REQUIRED", "/overlap_policy/exception_review_refs"))

    core_unresolved = (
        key_profile["resolution"] == "UNRESOLVED"
        or policy["resolution"] == "UNRESOLVED"
        or subject["presence"] == "UNRESOLVED"
    )
    expected_state: str | None = None
    if not classification_blocked:
        if core_unresolved:
            expected_state = "UNRESOLVED"
        elif disallowed_conflict:
            expected_state = "CONFLICT"
        elif comparison_unresolved:
            expected_state = "UNRESOLVED"
        elif known_conflict_indexes:
            expected_state = "ALLOWED_OVERLAP"
        else:
            expected_state = "UNIQUE"

    if expected_state == "CONFLICT":
        findings.add(Finding("TEMPORAL_UNIQUENESS_CONFLICT", "/declared_state"))
    if expected_state is not None and candidate["declared_state"] != expected_state:
        findings.add(Finding("DECLARED_STATE_MISMATCH", "/declared_state"))

    handling = candidate["failure_handling"]
    assert isinstance(handling, Mapping)
    review_refs = handling["review_record_refs"]
    if not _canonical_strings(review_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/failure_handling/review_record_refs"))
    action = handling["recommended_action"]
    if expected_state == "CONFLICT":
        if action not in {"DENY_CANDIDATE", "QUARANTINE_CANDIDATE"}:
            findings.add(Finding("FAILURE_ACTION_REQUIRED", "/failure_handling/recommended_action"))
        if not review_refs:
            findings.add(Finding("FAILURE_REVIEW_REFERENCE_REQUIRED", "/failure_handling/review_record_refs"))
    elif expected_state == "ALLOWED_OVERLAP":
        if action != "REVIEW_OVERLAP":
            findings.add(Finding("OVERLAP_REVIEW_ACTION_REQUIRED", "/failure_handling/recommended_action"))
        if not review_refs:
            findings.add(Finding("OVERLAP_REVIEW_REFERENCE_REQUIRED", "/failure_handling/review_record_refs"))
    elif expected_state in {"UNIQUE", "UNRESOLVED"} and action != "NONE":
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
        description="Validate fixture-only temporal uniqueness assessments."
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
