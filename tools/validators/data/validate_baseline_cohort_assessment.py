#!/usr/bin/env python3
"""Validate fixture-only baseline cohort assessments."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/data/baseline_cohort_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/data/baseline_cohort_assessment/cases.json"
MAX_JSON_BYTES = 1024 * 1024
DISCONTINUITY_REASON = {
    "RELOCATION": "RELOCATION_DISCONTINUITY",
    "METHOD_CHANGE": "METHOD_DISCONTINUITY",
    "INSTRUMENT_CHANGE": "INSTRUMENT_DISCONTINUITY",
    "GAP": "GAP_DISCONTINUITY",
    "CORRECTION": "CORRECTION_DISCONTINUITY",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    outcome: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    digest = spec_hash.removeprefix("sha256:")
    return f"kfm:baseline-cohort:{digest[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    candidates = document["candidates"]
    included = sum(item["eligibility"] == "INCLUDE" for item in candidates)
    excluded = sum(item["eligibility"] == "EXCLUDE" for item in candidates)
    holds = sum(item["eligibility"] == "HOLD" for item in candidates)
    if holds:
        outcome = "HOLD"
    elif not included:
        outcome = "ABSTAIN"
    else:
        outcome = "COMPLETE"
    discontinuities = document["discontinuities"]
    rebuild = any(
        item["class"] in {"RELOCATION", "METHOD_CHANGE", "INSTRUMENT_CHANGE"}
        or item["disposition"] == "SEGMENT"
        for item in discontinuities
    )
    return {
        "candidate_count": len(candidates),
        "included_count": included,
        "excluded_count": excluded,
        "hold_count": holds,
        "discontinuity_count": len(discontinuities),
        "cohort_outcome": outcome,
        "rebuild_required": rebuild,
        "baseline_use_authorized": False,
        "baseline_publishable": False,
        "separate_materiality_policy_required": True,
    }


def _baseline_time_valid(baseline: Mapping[str, Any]) -> bool:
    start = _dt(baseline["valid_start"])
    end = _dt(baseline["valid_end"])
    return start < end <= _dt(baseline["recorded_at"])


def _candidate_time_valid(candidate: Mapping[str, Any]) -> bool:
    return _dt(candidate["observed_at"]) <= _dt(candidate["recorded_at"])


def _candidate_state_valid(candidate: Mapping[str, Any], baseline: Mapping[str, Any]) -> bool:
    observed = _dt(candidate["observed_at"])
    inside = _dt(baseline["valid_start"]) <= observed < _dt(baseline["valid_end"])
    method_matches = candidate["method_profile_ref"] == baseline["method_profile_ref"]
    complete = candidate["missingness"] == "COMPLETE"
    eligibility = candidate["eligibility"]
    reasons = set(candidate["reason_codes"])
    discontinuity_ref = candidate["discontinuity_ref"]
    evidence = candidate["evidence_refs"]
    if eligibility == "INCLUDE":
        return (
            inside and method_matches and complete and bool(evidence)
            and reasons == {"ELIGIBLE"} and discontinuity_ref is None
        )
    if eligibility == "HOLD":
        return bool(reasons & {"QUALITY_HOLD", "DISCONTINUITY_REVIEW_PENDING"})

    supported = False
    if not inside and "OUTSIDE_WINDOW" in reasons:
        supported = True
    if not method_matches and "METHOD_MISMATCH" in reasons:
        supported = True
    if not complete and "MISSING_SUPPORT" in reasons:
        supported = True
    if discontinuity_ref is not None and reasons & set(DISCONTINUITY_REASON.values()):
        supported = True
    return supported and "ELIGIBLE" not in reasons


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY", None,
            (Finding("BASELINE_COHORT_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    baseline = document["baseline"]
    if not _baseline_time_valid(baseline):
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_WINDOW_INVALID", "/baseline"),)
        )

    candidates = document["candidates"]
    member_ids = [item["member_id"] for item in candidates]
    if member_ids != sorted(set(member_ids)):
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_CANDIDATE_ORDER_INVALID", "/candidates"),)
        )
    for index, candidate in enumerate(candidates):
        if not _candidate_time_valid(candidate):
            return ValidationResult(
                "DENY", None, (Finding("BASELINE_COHORT_TIME_INVALID", f"/candidates/{index}"),)
            )

    discontinuities = document["discontinuities"]
    discontinuity_ids = [item["discontinuity_id"] for item in discontinuities]
    if discontinuity_ids != sorted(set(discontinuity_ids)):
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_DISCONTINUITY_ORDER_INVALID", "/discontinuities"),)
        )
    by_member = {item["member_id"]: item for item in candidates}
    for index, discontinuity in enumerate(discontinuities):
        member_id = discontinuity["member_id"]
        expected_ref = f"kfm:discontinuity:{discontinuity['discontinuity_id']}"
        if member_id not in by_member or by_member[member_id]["discontinuity_ref"] != expected_ref:
            return ValidationResult(
                "DENY", None,
                (Finding("BASELINE_COHORT_DISCONTINUITY_BINDING_INVALID", f"/discontinuities/{index}"),),
            )
        if _dt(discontinuity["effective_at"]) > _dt(discontinuity["recorded_at"]):
            return ValidationResult(
                "DENY", None, (Finding("BASELINE_COHORT_TIME_INVALID", f"/discontinuities/{index}"),)
            )
        candidate = by_member[member_id]
        disposition = discontinuity["disposition"]
        required_eligibility = "HOLD" if disposition == "HOLD" else "EXCLUDE"
        reason_compatible = (
            "DISCONTINUITY_REVIEW_PENDING" in candidate["reason_codes"]
            if disposition == "HOLD"
            else DISCONTINUITY_REASON[discontinuity["class"]] in candidate["reason_codes"]
        )
        if candidate["eligibility"] != required_eligibility or not reason_compatible:
            return ValidationResult(
                "DENY", None,
                (Finding("BASELINE_COHORT_DISCONTINUITY_STATE_INVALID", f"/discontinuities/{index}"),),
            )

    for index, candidate in enumerate(candidates):
        if not _candidate_state_valid(candidate, baseline):
            return ValidationResult(
                "DENY", None, (Finding("BASELINE_COHORT_CANDIDATE_STATE_INVALID", f"/candidates/{index}"),)
            )

    summary = expected_summary(document)
    if document["summary"] != summary:
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_SUMMARY_MISMATCH", "/summary"),)
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_SPEC_HASH_MISMATCH", "/spec_hash"),)
        )
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult(
            "DENY", None, (Finding("BASELINE_COHORT_ID_MISMATCH", "/assessment_id"),)
        )
    status = "PASS" if summary["cohort_outcome"] == "COMPLETE" else "ABSTAIN"
    return ValidationResult(status, summary["cohort_outcome"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_summary"):
        document["summary"] = expected_summary(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(
            stream,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.status != case["expected_status"]
            or result.outcome != case["expected_outcome"]
            or findings != case["expected_findings"]
        ):
            failures.append({
                "case_id": case["case_id"],
                "expected_status": case["expected_status"],
                "actual_status": result.status,
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": findings,
            })
    print(json.dumps(
        {"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures},
        sort_keys=True,
        separators=(",", ":"),
    ))
    return 0 if not failures else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult("ERROR", None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),))
    except InputTooLargeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_UNREADABLE", "/"),))
    except json.JSONDecodeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INVALID", "/"),))
    except (ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_ROOT_INVALID", "/"),))
    print(json.dumps({
        "status": result.status,
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
    }, sort_keys=True, separators=(",", ":")))
    return 0 if result.status in {"PASS", "ABSTAIN"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
