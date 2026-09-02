#!/usr/bin/env python3
"""Validate fixture-only sampling-effort and non-detection assessments.

The validator is deterministic and local. A coherent candidate returns HOLD,
never ALLOW; it creates no evidence, absence claim, source, policy, review,
release, publication, or public-use authority.
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

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/non_detection_support_assessment.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/non_detection_support_assessment/cases.json"
IDENTITY_PREFIX = "kfm:non-detection-support:"
SCOPE = "non-detection-support-fixture-only-v1"


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
    "OBSERVED_DETECTION": ("ANSWER", "DETECTION_RECORDED", "VERIFY_OCCURRENCE_SCOPE"),
    "SUPPORTED_NON_DETECTION": ("ANSWER", "NON_DETECTION_SUPPORTED_BY_EFFORT", "DO_NOT_INFER_ABSENCE"),
    "NOT_SAMPLED": ("ABSTAIN", "SAMPLING_NOT_DOCUMENTED", "DOCUMENT_SAMPLING_EFFORT"),
    "INCOMPLETE_EFFORT": ("ABSTAIN", "SAMPLING_EFFORT_INCOMPLETE", "COMPLETE_SAMPLING_EFFORT"),
    "UNKNOWN_EFFORT": ("ABSTAIN", "DETECTION_OPPORTUNITY_UNKNOWN", "RESOLVE_DETECTION_OPPORTUNITY"),
    "SUPPRESSED_RESULT": ("DENY", "PRIVACY_SUPPRESSION_REQUIRED", "WITHHOLD_RESTRICTED_RESULT"),
    "STALE_COVERAGE": ("ABSTAIN", "SAMPLING_COVERAGE_STALE", "REFRESH_SAMPLING_COVERAGE"),
}


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in candidate.items() if key not in {"assessment_id", "spec_hash"}}


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


def _derive_state(candidate: Mapping[str, Any]) -> str:
    event = _mapping(candidate.get("sampling_event"))
    opportunity = _mapping(candidate.get("detection_opportunity"))
    assertion = _mapping(candidate.get("assertion"))
    count = assertion.get("observed_count")

    if event.get("privacy_class") == "RESTRICTED" or opportunity.get("opportunity_state") == "SUPPRESSED":
        return "SUPPRESSED_RESULT"
    if event.get("coverage_current") is False:
        return "STALE_COVERAGE"
    if isinstance(count, int) and not isinstance(count, bool) and count > 0:
        return "OBSERVED_DETECTION"
    if event.get("effort_duration_minutes") == 0 or event.get("observer_or_instrument_count") == 0:
        return "NOT_SAMPLED"
    if (
        event.get("complete_checklist") is False
        or opportunity.get("target_in_protocol_scope") is False
        or opportunity.get("method_suitable") == "NO"
        or opportunity.get("season_supported") == "NO"
        or opportunity.get("opportunity_state") == "INADEQUATE"
    ):
        return "INCOMPLETE_EFFORT"
    if (
        count is None
        or opportunity.get("method_suitable") == "UNKNOWN"
        or opportunity.get("season_supported") == "UNKNOWN"
        or opportunity.get("opportunity_state") == "UNKNOWN"
    ):
        return "UNKNOWN_EFFORT"
    if (
        count == 0
        and event.get("complete_checklist") is True
        and opportunity.get("target_in_protocol_scope") is True
        and opportunity.get("method_suitable") == "YES"
        and opportunity.get("season_supported") == "YES"
        and opportunity.get("opportunity_state") == "ADEQUATE"
    ):
        return "SUPPORTED_NON_DETECTION"
    return "UNKNOWN_EFFORT"


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

    event = _mapping(candidate.get("sampling_event"))
    assertion = _mapping(candidate.get("assertion"))
    started = _time(event.get("started_at"))
    ended = _time(event.get("ended_at"))
    evaluated = _time(candidate.get("evaluated_at"))
    if started is None or ended is None or evaluated is None:
        findings.add(Finding("EVENT_TIME_INVALID", "/sampling_event"))
    else:
        if started >= ended:
            findings.add(Finding("EVENT_INTERVAL_INVALID", "/sampling_event"))
        if ended > evaluated:
            findings.add(Finding("EVENT_AFTER_EVALUATION", "/evaluated_at"))

    privacy = event.get("privacy_class")
    transform = event.get("privacy_transform_ref")
    if privacy in {"GENERALIZED", "RESTRICTED"} and transform is None:
        findings.add(Finding("PRIVACY_TRANSFORM_REQUIRED", "/sampling_event/privacy_transform_ref"))
    if privacy == "PUBLIC_SAFE" and transform is not None:
        findings.add(Finding("PRIVACY_TRANSFORM_UNEXPECTED", "/sampling_event/privacy_transform_ref"))

    state = _derive_state(candidate)
    decision, reason, obligation = DERIVED[state]
    if assertion.get("state") != state:
        findings.add(Finding("ASSERTION_STATE_MISMATCH", "/assertion/state"))
    if assertion.get("decision") != decision:
        findings.add(Finding("ASSERTION_DECISION_MISMATCH", "/assertion/decision"))
    reasons = assertion.get("reason_codes")
    obligations = assertion.get("obligations")
    if not isinstance(reasons, list) or reason not in reasons:
        findings.add(Finding("ASSERTION_REASON_REQUIRED", "/assertion/reason_codes"))
    if not isinstance(obligations, list) or obligation not in obligations:
        findings.add(Finding("ASSERTION_OBLIGATION_REQUIRED", "/assertion/obligations"))

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
