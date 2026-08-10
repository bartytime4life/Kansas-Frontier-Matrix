#!/usr/bin/env python3
"""Validate fixture-only DeliveryAvailabilityAssessment records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/delivery_availability_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/delivery_availability_assessment/cases.json"
PREFIX = "kfm:delivery-availability:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("DELIVERY_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("DELIVERY_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("DELIVERY_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("DELIVERY_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("DELIVERY_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("DELIVERY_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("DELIVERY_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def recompute_learned_observation(value: Mapping[str, Any]) -> dict[str, Any]:
    observation = value["observation"]
    generated = _time(observation["generated_at"])
    available = _time(observation["actually_available_at"])
    latency: int | None = None
    if generated is not None and available is not None:
        seconds = (available - generated).total_seconds()
        if seconds >= 0 and seconds.is_integer():
            latency = int(seconds)
    return {
        "observed_delivery_latency_seconds": latency,
        "use_for_expectation_update": "REVIEW_REQUIRED",
        "expectation_mutated": False,
    }


def _freshness_state(value: Mapping[str, Any]) -> str:
    observation = value["observation"]
    if observation["actually_available_at"] is None:
        return "UNAVAILABLE"
    observed = _time(observation["observed_at"])
    assessed = _time(value["assessed_at"])
    if observed is None or assessed is None:
        return "ERROR"
    freshness = observed + timedelta(seconds=value["expectation"]["freshness_window_seconds"])
    stale = observed + timedelta(seconds=value["expectation"]["stale_threshold_seconds"])
    if assessed <= freshness:
        return "WITHIN_WINDOW"
    if assessed <= stale:
        return "PAST_FRESHNESS"
    return "STALE"


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return {
            "state": "ERROR",
            "freshness_state": "ERROR",
            "reason_codes": ["ASSESSMENT_ERROR"],
            "review_required": True,
            "policy_change_candidate": False,
        }

    observation = value["observation"]
    assessed = _time(value["assessed_at"])
    observed = _time(observation["observed_at"])
    available = _time(observation["actually_available_at"])
    expected_until = _time(observation["expected_available_until"])
    freshness_state = _freshness_state(value)

    if assessed is None or observed is None or expected_until is None:
        state, reason = "ERROR", "ASSESSMENT_ERROR"
        freshness_state = "ERROR"
    elif observation["superseded_by_revision"] is not None:
        state, reason = "SUPERSEDED", "SOURCE_REVISION_SUPERSEDED"
    elif observation["retrieval_result"] == "SOURCE_ERROR":
        state, reason = "SOURCE_OUTAGE", "SOURCE_OUTAGE_EVIDENCED"
    elif available is None:
        if assessed <= expected_until:
            state, reason = "EXPECTED_LAG", "WITHIN_EXPECTED_DELIVERY_WINDOW"
        else:
            state, reason = "MISSING", "DELIVERY_MISSING_AFTER_EXPECTED_WINDOW"
    else:
        stale = observed + timedelta(seconds=value["expectation"]["stale_threshold_seconds"])
        if assessed > stale:
            state, reason = "STALE", "STALE_THRESHOLD_ELAPSED"
        elif available <= expected_until:
            state, reason = "ON_TIME", "DELIVERED_WITHIN_EXPECTED_WINDOW"
        else:
            state, reason = "LATE", "DELIVERY_AFTER_EXPECTED_WINDOW"

    return {
        "state": state,
        "freshness_state": freshness_state,
        "reason_codes": [reason],
        "review_required": True,
        "policy_change_candidate": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("DELIVERY_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("DELIVERY_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("DELIVERY_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("DELIVERY_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("DELIVERY_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("DELIVERY_ID_MISMATCH", "/assessment_id"))

    if value["source_descriptor_ref"] != f"kfm://source/{value['source_id']}":
        findings.add(Finding("DELIVERY_SOURCE_REF_MISMATCH", "/source_descriptor_ref"))

    expectation = value["expectation"]
    window = expectation["delivery_window_seconds"]
    if window["minimum_seconds"] > window["maximum_seconds"]:
        findings.add(
            Finding("DELIVERY_EXPECTATION_WINDOW_INVALID", "/expectation/delivery_window_seconds")
        )
    if expectation["freshness_window_seconds"] >= expectation["stale_threshold_seconds"]:
        findings.add(
            Finding("DELIVERY_FRESHNESS_THRESHOLD_INVALID", "/expectation/stale_threshold_seconds")
        )

    observation = value["observation"]
    observed = _time(observation["observed_at"])
    generated = _time(observation["generated_at"])
    expected_from = _time(observation["expected_available_from"])
    expected_until = _time(observation["expected_available_until"])
    available = _time(observation["actually_available_at"])
    retrieved = _time(observation["retrieved_at"])
    validated = _time(observation["validated_at"])
    released = _time(observation["released_at"])
    assessed = _time(value["assessed_at"])

    if generated is not None:
        derived_from = generated + timedelta(seconds=window["minimum_seconds"])
        derived_until = generated + timedelta(seconds=window["maximum_seconds"])
        if expected_from != derived_from or expected_until != derived_until:
            findings.add(Finding("DELIVERY_EXPECTED_WINDOW_MISMATCH", "/observation"))
    if observed is not None and generated is not None and generated < observed:
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/observation/generated_at"))
    if generated is not None and available is not None and available < generated:
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/observation/actually_available_at"))
    if retrieved is not None and (available is None or retrieved < available):
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/observation/retrieved_at"))
    if validated is not None and (retrieved is None or validated < retrieved):
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/observation/validated_at"))
    if released is not None and (validated is None or released < validated):
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/observation/released_at"))
    if assessed is not None and observed is not None and assessed < observed:
        findings.add(Finding("DELIVERY_TIME_ORDER_INVALID", "/assessed_at"))

    retrieval_result = observation["retrieval_result"]
    if retrieval_result == "SUCCESS":
        if available is None or retrieved is None or validated is None:
            findings.add(
                Finding("DELIVERY_RETRIEVAL_STATE_MISMATCH", "/observation/retrieval_result")
            )
    elif retrieval_result in {"NOT_YET_AVAILABLE", "NOT_FOUND", "SOURCE_ERROR"}:
        if available is not None or retrieved is not None or validated is not None:
            findings.add(
                Finding("DELIVERY_RETRIEVAL_STATE_MISMATCH", "/observation/retrieval_result")
            )
    elif retrieval_result == "NOT_RETRIEVED" and (retrieved is not None or validated is not None):
        findings.add(
            Finding("DELIVERY_RETRIEVAL_STATE_MISMATCH", "/observation/retrieval_result")
        )

    outage_ref = observation["source_outage_evidence_ref"]
    if retrieval_result == "SOURCE_ERROR":
        if outage_ref is None or not expectation["outage_exception_allowed"]:
            findings.add(
                Finding("DELIVERY_OUTAGE_EVIDENCE_REQUIRED", "/observation/source_outage_evidence_ref")
            )
    elif outage_ref is not None:
        findings.add(
            Finding("DELIVERY_OUTAGE_EVIDENCE_FORBIDDEN", "/observation/source_outage_evidence_ref")
        )

    superseded_by = observation["superseded_by_revision"]
    if superseded_by is not None and superseded_by == observation["source_revision"]:
        findings.add(
            Finding("DELIVERY_SUPERSESSION_SELF_REFERENCE", "/observation/superseded_by_revision")
        )

    if value["learned_observation"] != recompute_learned_observation(value):
        findings.add(Finding("DELIVERY_LEARNED_OBSERVATION_MISMATCH", "/learned_observation"))
    if value["decision"] != recompute_decision(value):
        findings.add(Finding("DELIVERY_DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    state = value["decision"]["state"]
    if state in {"ON_TIME", "EXPECTED_LAG", "LATE"}:
        return Result("PASS", ())
    if state in {"STALE", "MISSING", "SUPERSEDED", "SOURCE_OUTAGE"}:
        return Result(
            "ABSTAIN",
            (Finding(value["decision"]["reason_codes"][0], "/decision/state"),),
        )
    return Result("ERROR", (Finding("ASSESSMENT_ERROR", "/decision/state"),))


def _replace(document: Any, pointer: str, replacement: Any) -> None:
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
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["learned_observation"] = copy.deepcopy(
        case.get("learned_override", recompute_learned_observation(document))
    )
    document["decision"] = copy.deepcopy(
        case.get("decision_override", recompute_decision(document))
    )
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "no_network",
                "no_source_activation",
                "no_expectation_update",
                "no_policy_evaluation",
                "no_raw_write",
                "no_promotion",
                "no_release",
                "no_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
