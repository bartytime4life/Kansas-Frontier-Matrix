"""Validate fixture-only public-map-service SLO assessment candidates.

The validator checks declared window, availability, latency, error-budget,
support-reference, report, and deterministic-identity coherence only. It never
queries a service, authenticates telemetry, sets policy, changes promotion or
rollback state, releases, deploys, or publishes.
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
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/validation/public_map_service_slo_assessment.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/validation/public_map_service_slo_assessment/cases.json"
)
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ASSESSMENT_INCOMPLETE",
    "LATENCY_OBSERVATION_UNRESOLVED",
    "LATENCY_SAMPLE_REQUIRED",
    "MEASUREMENT_WINDOW_INCOMPLETE",
    "REVIEW_REFERENCE_REQUIRED",
    "ROLLBACK_REFERENCE_REQUIRED",
    "SLO_POLICY_UNRESOLVED",
    "TELEMETRY_REFERENCE_REQUIRED",
}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_LIVE_MONITORING",
    "NO_PROMOTION_AUTHORITY",
    "NO_RELEASE_AUTHORITY",
    "TELEMETRY_NOT_TRUTH",
]


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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


def compute_spec_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return canonical_hash(subject)


def expected_assessment_id(spec_hash: str) -> str:
    return "kfm:public-map-service-slo-assessment:" + spec_hash.removeprefix(
        "sha256:"
    )[:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
        for error in errors[:100]
    ]


def _utc_datetime(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _allowed_bad_events(availability: Mapping[str, object]) -> int:
    eligible = int(availability["eligible_events"])
    target = int(availability["target_basis_points"])
    return eligible * (10000 - target) // 10000


def _observed_bad_events(availability: Mapping[str, object]) -> int:
    return int(availability["eligible_events"]) - int(availability["good_events"])


def _expected_latency_state(latency: Mapping[str, object]) -> str:
    observed = latency["observed_milliseconds"]
    if observed is None or int(latency["sample_count"]) == 0:
        return "UNASSESSED"
    return (
        "WITHIN_TARGET"
        if int(observed) <= int(latency["target_milliseconds"])
        else "BREACHED"
    )


def expected_report(candidate: Mapping[str, object]) -> dict[str, object]:
    codes: set[str] = set()
    state = candidate["assessment_state"]
    window = candidate["measurement_window"]
    policy = candidate["policy"]
    availability = candidate["availability"]
    latency = candidate["latency"]
    support = candidate["support"]
    assert isinstance(window, Mapping)
    assert isinstance(policy, Mapping)
    assert isinstance(availability, Mapping)
    assert isinstance(latency, Mapping)
    assert isinstance(support, Mapping)

    if state == "ERROR":
        codes.add("ASSESSMENT_ERROR")
    elif state == "INCOMPLETE":
        codes.add("ASSESSMENT_INCOMPLETE")
    if window.get("status") == "INCOMPLETE":
        codes.add("MEASUREMENT_WINDOW_INCOMPLETE")
    if policy.get("objective_status") == "UNRESOLVED" or policy.get(
        "slo_policy_ref"
    ) is None:
        codes.add("SLO_POLICY_UNRESOLVED")
    if not support.get("telemetry_receipt_refs"):
        codes.add("TELEMETRY_REFERENCE_REQUIRED")
    if not support.get("review_record_refs"):
        codes.add("REVIEW_REFERENCE_REQUIRED")
    if support.get("rollback_ref") is None:
        codes.add("ROLLBACK_REFERENCE_REQUIRED")
    if latency.get("observed_milliseconds") is None:
        codes.add("LATENCY_OBSERVATION_UNRESOLVED")
    if int(latency.get("sample_count", 0)) == 0:
        codes.add("LATENCY_SAMPLE_REQUIRED")

    allowed = _allowed_bad_events(availability)
    observed_bad = _observed_bad_events(availability)
    if observed_bad > allowed:
        codes.add("BUDGET_EXHAUSTED")
    if _expected_latency_state(latency) == "BREACHED":
        codes.add("LATENCY_BREACH")

    if "ASSESSMENT_ERROR" in codes:
        outcome = "ERROR"
    elif codes & {"BUDGET_EXHAUSTED", "LATENCY_BREACH"}:
        outcome = "DENY"
    elif codes:
        outcome = "ABSTAIN"
    else:
        outcome = "PASS"
    return {
        "assessment_outcome": outcome,
        "finding_codes": sorted(codes),
        "promotion_effect": "NO_AUTOMATIC_EFFECT",
        "rollback_effect": "REVIEW_ONLY",
    }


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash = compute_spec_hash(candidate)
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_assessment_id(expected_hash):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    assessed_at = _utc_datetime(candidate.get("assessed_at"))
    if assessed_at is None:
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/assessed_at"))

    window = candidate["measurement_window"]
    policy = candidate["policy"]
    availability = candidate["availability"]
    latency = candidate["latency"]
    budget = candidate["error_budget"]
    support = candidate["support"]
    report = candidate["report"]
    assert isinstance(window, Mapping)
    assert isinstance(policy, Mapping)
    assert isinstance(availability, Mapping)
    assert isinstance(latency, Mapping)
    assert isinstance(budget, Mapping)
    assert isinstance(support, Mapping)
    assert isinstance(report, Mapping)

    started = _utc_datetime(window.get("started_at"))
    ended = _utc_datetime(window.get("ended_at"))
    if started is None:
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/measurement_window/started_at"))
    if ended is None:
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/measurement_window/ended_at"))
    if started is not None and ended is not None and started >= ended:
        findings.add(Finding("MEASUREMENT_WINDOW_ORDER_INVALID", "/measurement_window"))

    if policy.get("objective_status") == "RESOLVED":
        if policy.get("slo_policy_ref") is None:
            findings.add(Finding("SLO_POLICY_REFERENCE_REQUIRED", "/policy/slo_policy_ref"))
    elif policy.get("slo_policy_ref") is not None:
        findings.add(Finding("UNRESOLVED_POLICY_REFERENCE_PRESENT", "/policy/slo_policy_ref"))

    if int(availability["good_events"]) > int(availability["eligible_events"]):
        findings.add(Finding("GOOD_EVENTS_EXCEED_ELIGIBLE", "/availability/good_events"))
    allowed = _allowed_bad_events(availability)
    observed_bad = _observed_bad_events(availability)
    remaining = allowed - observed_bad
    budget_state = "WITHIN_BUDGET" if observed_bad <= allowed else "EXHAUSTED"
    if budget.get("allowed_bad_events") != allowed:
        findings.add(Finding("ALLOWED_BAD_EVENTS_MISMATCH", "/error_budget/allowed_bad_events"))
    if budget.get("observed_bad_events") != observed_bad:
        findings.add(Finding("OBSERVED_BAD_EVENTS_MISMATCH", "/error_budget/observed_bad_events"))
    if budget.get("remaining_bad_events") != remaining:
        findings.add(Finding("REMAINING_BAD_EVENTS_MISMATCH", "/error_budget/remaining_bad_events"))
    if budget.get("state") != budget_state:
        findings.add(Finding("BUDGET_STATE_MISMATCH", "/error_budget/state"))

    latency_state = _expected_latency_state(latency)
    if latency.get("state") != latency_state:
        findings.add(Finding("LATENCY_STATE_MISMATCH", "/latency/state"))

    for field in ("telemetry_receipt_refs", "review_record_refs"):
        if not _canonical_strings(support.get(field)):
            findings.add(Finding("SUPPORT_REFS_NOT_CANONICAL", f"/support/{field}"))
    limitations = candidate["limitations"]
    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    if not _canonical_strings(report.get("finding_codes")):
        findings.add(Finding("REPORT_FINDINGS_NOT_CANONICAL", "/report/finding_codes"))

    projected = expected_report(candidate)
    if report.get("assessment_outcome") != projected["assessment_outcome"]:
        findings.add(Finding("REPORT_OUTCOME_MISMATCH", "/report/assessment_outcome"))
    if report.get("finding_codes") != projected["finding_codes"]:
        findings.add(Finding("REPORT_FINDINGS_MISMATCH", "/report/finding_codes"))

    for code in projected["finding_codes"]:
        findings.add(Finding(str(code), "/report/finding_codes"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "ASSESSMENT_ERROR" in codes:
        outcome = "ERROR"
    elif not codes:
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


def _reproduce_derived_fields(candidate: dict[str, object]) -> None:
    availability = candidate["availability"]
    latency = candidate["latency"]
    assert isinstance(availability, Mapping)
    assert isinstance(latency, Mapping)
    allowed = _allowed_bad_events(availability)
    observed_bad = _observed_bad_events(availability)
    candidate["error_budget"] = {
        "allowed_bad_events": allowed,
        "observed_bad_events": observed_bad,
        "remaining_bad_events": allowed - observed_bad,
        "state": "WITHIN_BUDGET" if observed_bad <= allowed else "EXHAUSTED",
    }
    mutable_latency = dict(latency)
    mutable_latency["state"] = _expected_latency_state(mutable_latency)
    candidate["latency"] = mutable_latency
    candidate["report"] = expected_report(candidate)


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    _reproduce_derived_fields(candidate)
    tamper = entry.get("tamper")
    budget = candidate["error_budget"]
    latency = candidate["latency"]
    support = candidate["support"]
    report = candidate["report"]
    assert isinstance(budget, dict)
    assert isinstance(latency, dict)
    assert isinstance(support, dict)
    assert isinstance(report, dict)
    if tamper == "allowed_bad_events":
        budget["allowed_bad_events"] = int(budget["allowed_bad_events"]) + 1
    elif tamper == "observed_bad_events":
        budget["observed_bad_events"] = int(budget["observed_bad_events"]) + 1
    elif tamper == "remaining_bad_events":
        budget["remaining_bad_events"] = int(budget["remaining_bad_events"]) + 1
    elif tamper == "budget_state":
        budget["state"] = "EXHAUSTED"
    elif tamper == "latency_state":
        latency["state"] = "BREACHED"
    elif tamper == "report_outcome":
        report["assessment_outcome"] = "DENY"
    elif tamper == "report_findings":
        report["finding_codes"] = ["LATENCY_BREACH"]
    elif tamper == "support_ref_order":
        support["telemetry_receipt_refs"] = list(
            reversed(support["telemetry_receipt_refs"])
        )
    elif tamper == "limitations":
        candidate["limitations"] = EXPECTED_LIMITATIONS[:-1]
    elif tamper == "unknown_field":
        candidate["unexpected"] = True
    elif tamper == "authority":
        authority = candidate["authority_claims"]
        assert isinstance(authority, dict)
        authority["promotion_authority"] = True

    spec_hash = compute_spec_hash(candidate)
    candidate["spec_hash"] = spec_hash
    candidate["assessment_id"] = expected_assessment_id(spec_hash)
    if tamper == "spec_hash":
        candidate["spec_hash"] = "sha256:" + "f" * 64
    elif tamper == "assessment_id":
        candidate["assessment_id"] = (
            "kfm:public-map-service-slo-assessment:" + "f" * 24
        )
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
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
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
        description="Validate fixture-only public-map-service SLO assessments."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, load_findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(load_findings))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "findings": [
                    {"code": finding.code, "field": finding.field}
                    for finding in result.findings
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
