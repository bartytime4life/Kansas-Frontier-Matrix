#!/usr/bin/env python3
"""Validate fixture-only baseline cohort assessments.

The validator is deterministic and local. A coherent candidate returns HOLD,
never ALLOW; it creates no baseline truth, threshold, anomaly, source, policy,
review, release, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/baseline_cohort_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json"
IDENTITY_PREFIX = "kfm:baseline-cohort:"
SCOPE = "baseline-cohort-fixture-only-v1"


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.outcome == "HOLD" and not self.findings


DERIVED: dict[str, tuple[str, str, str]] = {
    "REPLAYABLE": ("REVIEW_CANDIDATE", "BASELINE_REPLAYABLE", "HUMAN_REVIEW_REQUIRED"),
    "QUALIFIED": (
        "REVIEW_CANDIDATE",
        "BASELINE_QUALIFIED",
        "REVIEW_EXCLUSIONS_AND_DISCONTINUITIES",
    ),
    "INSUFFICIENT": ("HOLD", "INSUFFICIENT_ELIGIBLE_COHORT", "REBUILD_COHORT_BEFORE_USE"),
    "DISCONTINUITY_UNRESOLVED": (
        "HOLD",
        "BASELINE_DISCONTINUITY_UNRESOLVED",
        "RESOLVE_DISCONTINUITY_BEFORE_USE",
    ),
}


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: copy.deepcopy(value)
        for key, value in candidate.items()
        if key not in {"assessment_id", "spec_hash"}
    }


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return a copy with deterministic RFC 8785 identity fields."""
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["assessment_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical_unique_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _derive_state(candidate: Mapping[str, Any]) -> str:
    cohort = _mapping(candidate.get("cohort_eligibility_report"))
    discontinuities = candidate.get("discontinuity_records")
    if isinstance(discontinuities, list) and any(
        isinstance(record, Mapping) and record.get("resolution") == "UNRESOLVED"
        for record in discontinuities
    ):
        return "DISCONTINUITY_UNRESOLVED"
    candidate_count = cohort.get("candidate_count")
    eligible_count = cohort.get("eligible_count")
    if candidate_count == 0 or eligible_count == 0:
        return "INSUFFICIENT"
    if (
        isinstance(discontinuities, list)
        and discontinuities
        or isinstance(cohort.get("excluded_count"), int)
        and cohort.get("excluded_count", 0) > 0
        or isinstance(cohort.get("missing_count"), int)
        and cohort.get("missing_count", 0) > 0
    ):
        return "QUALIFIED"
    return "REPLAYABLE"


def validate_document(candidate: object) -> Result:
    findings: set[Finding] = set()
    try:
        schema = load_json_file(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (JsonInputError, ValueError, TypeError, RecursionError):
        return Result("DENY", (Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings.update(Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path))) for error in errors[:100])
    if errors or not isinstance(candidate, Mapping):
        return Result("DENY", tuple(sorted(findings)))

    try:
        expected_hash = compute_spec_hash(_identity_projection(candidate))
    except (CanonicalizationFailure, TypeError, ValueError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
        return Result("DENY", tuple(sorted(findings)))
    expected_id = IDENTITY_PREFIX + expected_hash.removeprefix("sha256:")
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    manifest = _mapping(candidate.get("baseline_manifest"))
    cohort = _mapping(candidate.get("cohort_eligibility_report"))
    validation = _mapping(candidate.get("baseline_validation_report"))
    rebuild = _mapping(candidate.get("baseline_rebuild_receipt"))
    discontinuities = candidate.get("discontinuity_records")

    for field in ("input_artifact_refs", "source_refs"):
        if not _canonical_unique_strings(manifest.get(field)):
            findings.add(Finding("MANIFEST_REFS_NOT_CANONICAL", f"/baseline_manifest/{field}"))
    if not _canonical_unique_strings(cohort.get("known_blind_spots")):
        findings.add(Finding("BLIND_SPOTS_NOT_CANONICAL", "/cohort_eligibility_report/known_blind_spots"))

    candidate_count = cohort.get("candidate_count")
    eligible_count = cohort.get("eligible_count")
    excluded_count = cohort.get("excluded_count")
    missing_count = cohort.get("missing_count")
    if all(isinstance(value, int) and not isinstance(value, bool) for value in (candidate_count, eligible_count, excluded_count, missing_count)):
        if candidate_count != eligible_count + excluded_count + missing_count:
            findings.add(Finding("COHORT_COUNTS_DO_NOT_CLOSE", "/cohort_eligibility_report"))
        expected_missingness = (
            "INSUFFICIENT"
            if candidate_count == 0 or eligible_count == 0
            else "PARTIAL"
            if missing_count > 0
            else "COMPLETE"
        )
        if cohort.get("missingness_state") != expected_missingness:
            findings.add(Finding("MISSINGNESS_STATE_MISMATCH", "/cohort_eligibility_report/missingness_state"))
    reasons = cohort.get("exclusion_reason_counts")
    if isinstance(reasons, Mapping) and isinstance(excluded_count, int):
        if sum(value for value in reasons.values() if isinstance(value, int) and not isinstance(value, bool)) != excluded_count:
            findings.add(Finding("EXCLUSION_COUNTS_DO_NOT_CLOSE", "/cohort_eligibility_report/exclusion_reason_counts"))

    lookback_start = _time(manifest.get("lookback_started_at"))
    lookback_end = _time(manifest.get("lookback_ended_at"))
    generated_at = _time(rebuild.get("generated_at"))
    evaluated_at = _time(validation.get("evaluated_at"))
    if None in {lookback_start, lookback_end, generated_at, evaluated_at}:
        findings.add(Finding("BASELINE_TIME_INVALID", "/"))
    else:
        assert lookback_start is not None and lookback_end is not None
        assert generated_at is not None and evaluated_at is not None
        if lookback_start >= lookback_end:
            findings.add(Finding("LOOKBACK_INTERVAL_INVALID", "/baseline_manifest"))
        if lookback_end > generated_at:
            findings.add(Finding("REBUILD_BEFORE_LOOKBACK_END", "/baseline_rebuild_receipt/generated_at"))
        if generated_at > evaluated_at:
            findings.add(Finding("VALIDATION_BEFORE_REBUILD", "/baseline_validation_report/evaluated_at"))

    if isinstance(discontinuities, list):
        discontinuity_refs: list[str] = []
        order_keys: list[tuple[datetime, str]] = []
        for index, raw_record in enumerate(discontinuities):
            record = _mapping(raw_record)
            reference = record.get("discontinuity_ref")
            if isinstance(reference, str):
                discontinuity_refs.append(reference)
            effective_at = _time(record.get("effective_at"))
            if effective_at is not None and isinstance(reference, str):
                order_keys.append((effective_at, reference))
                if lookback_start is not None and effective_at < lookback_start:
                    findings.add(Finding("DISCONTINUITY_OUTSIDE_LOOKBACK", f"/discontinuity_records/{index}/effective_at"))
                if lookback_end is not None and effective_at > lookback_end:
                    findings.add(Finding("DISCONTINUITY_OUTSIDE_LOOKBACK", f"/discontinuity_records/{index}/effective_at"))
            if record.get("resolution") == "SEGMENT_BASELINE" and (
                record.get("predecessor_segment_ref") is None
                or record.get("successor_segment_ref") is None
            ):
                findings.add(Finding("SEGMENT_REFS_REQUIRED", f"/discontinuity_records/{index}"))
        if discontinuity_refs != sorted(set(discontinuity_refs)):
            findings.add(Finding("DISCONTINUITY_REFS_NOT_CANONICAL", "/discontinuity_records"))
        if len(order_keys) == len(discontinuities) and order_keys != sorted(order_keys):
            findings.add(Finding("DISCONTINUITIES_NOT_CHRONOLOGICAL", "/discontinuity_records"))

    previous = manifest.get("previous_baseline_ref")
    supersedes = rebuild.get("supersedes_baseline_ref")
    if previous != supersedes:
        findings.add(Finding("BASELINE_SUPERSESSION_MISMATCH", "/baseline_rebuild_receipt/supersedes_baseline_ref"))
    if previous is not None and previous == manifest.get("baseline_ref"):
        findings.add(Finding("BASELINE_SELF_SUPERSESSION", "/baseline_manifest/previous_baseline_ref"))
    if rebuild.get("correction_ref") is not None and previous is None:
        findings.add(Finding("CORRECTION_PREDECESSOR_REQUIRED", "/baseline_rebuild_receipt/correction_ref"))

    derived_state = _derive_state(candidate)
    decision, reason, obligation = DERIVED[derived_state]
    if validation.get("baseline_state") != derived_state:
        findings.add(Finding("BASELINE_STATE_MISMATCH", "/baseline_validation_report/baseline_state"))
    if validation.get("decision") != decision:
        findings.add(Finding("BASELINE_DECISION_MISMATCH", "/baseline_validation_report/decision"))
    reason_codes = validation.get("reason_codes")
    obligations = validation.get("obligations")
    if not isinstance(reason_codes, list) or reason not in reason_codes:
        findings.add(Finding("BASELINE_REASON_REQUIRED", "/baseline_validation_report/reason_codes"))
    if not isinstance(obligations, list) or obligation not in obligations:
        findings.add(Finding("BASELINE_OBLIGATION_REQUIRED", "/baseline_validation_report/obligations"))

    return Result("DENY" if findings else "HOLD", tuple(sorted(findings)))


def validate_file(path: Path | str) -> Result:
    try:
        return validate_document(load_json_file(path))
    except JsonInputError:
        return Result("DENY", (Finding("INPUT_JSON_INVALID", "/"),))
    except (KeyError, TypeError, ValueError, CanonicalizationFailure):
        return Result("DENY", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/")]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent: Any = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list):
        parent[int(parts[-1])] = copy.deepcopy(value)
    else:
        parent[parts[-1]] = copy.deepcopy(value)


def fixture_cases(path: Path = CASES_PATH) -> list[tuple[Mapping[str, Any], Result, str, tuple[str, ...]]]:
    matrix = load_json_file(path)
    if not isinstance(matrix, Mapping) or not isinstance(matrix.get("base"), Mapping) or not isinstance(matrix.get("cases"), list):
        raise ValueError("fixture matrix is invalid")
    base = seal(matrix["base"])
    materialized: list[tuple[Mapping[str, Any], Result, str, tuple[str, ...]]] = []
    for raw_case in matrix["cases"]:
        if not isinstance(raw_case, Mapping) or not isinstance(raw_case.get("name"), str):
            raise ValueError("fixture case is invalid")
        candidate = copy.deepcopy(base)
        mutations = raw_case.get("mutations", [])
        if not isinstance(mutations, list):
            raise ValueError("case mutations are invalid")
        for mutation in mutations:
            if not isinstance(mutation, Mapping) or not isinstance(mutation.get("path"), str) or "value" not in mutation:
                raise ValueError("case mutation is invalid")
            _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw_case.get("reseal", True) is True:
            candidate = seal(candidate)
        expected_outcome = raw_case.get("expected_outcome")
        expected_findings = raw_case.get("expected_findings", [])
        if not isinstance(expected_outcome, str) or not isinstance(expected_findings, list) or not all(isinstance(code, str) for code in expected_findings):
            raise ValueError("case expectations are invalid")
        materialized.append((candidate, validate_document(candidate), expected_outcome, tuple(expected_findings)))
    return materialized


def fixture_profile(path: Path = CASES_PATH) -> int:
    try:
        cases = fixture_cases(path)
    except (JsonInputError, ValueError, TypeError, KeyError, CanonicalizationFailure):
        print(json.dumps({"scope": SCOPE, "status": "FAIL", "reason": "FIXTURE_MATRIX_INVALID"}, sort_keys=True, separators=(",", ":")))
        return 1
    failures = []
    for index, (_candidate, result, expected_outcome, expected_findings) in enumerate(cases):
        codes = {finding.code for finding in result.findings}
        if result.outcome != expected_outcome or not set(expected_findings).issubset(codes):
            failures.append(index)
    payload = {"cases": len(cases), "failed_case_indexes": failures, "scope": SCOPE, "status": "FAIL" if failures else "PASS"}
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 1 if failures else 0


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide assessment files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate_file(path)
        payload = {
            "file": _display(path),
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
