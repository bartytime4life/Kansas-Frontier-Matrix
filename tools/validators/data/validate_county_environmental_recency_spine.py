#!/usr/bin/env python3
"""Validate deterministic fixture-only county environmental recency spines."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/data/county_environmental_recency_spine.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/data/county_environmental_recency_spine/cases.json"
LANES = ("AIR", "BIODIVERSITY", "HYDROLOGY", "IMAGERY", "SOILS", "VEGETATION")
HEALTH_REASON = {
    "HEALTHY": "HEALTHY_WITHIN_WEEK",
    "DEGRADED": "SOURCE_DEGRADED",
    "STALE": "SOURCE_STALE",
    "UNAVAILABLE": "SOURCE_UNAVAILABLE",
}
MAX_JSON_BYTES = 1024 * 1024


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
    outcome: str
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


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("spine_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_spine_id(spec_hash: str) -> str:
    return f"kfm:county-environmental-recency:{spec_hash.removeprefix('sha256:')[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def expected_summary(document: Mapping[str, Any]) -> dict[str, Any]:
    entries = document["entries"]
    recorded = sum(item["check_result"] == "RECORDED" for item in entries)
    errors = sum(item["check_result"] == "ERROR" for item in entries)
    holds = sum(
        item["check_result"] == "MISSED"
        or (item["check_result"] == "RECORDED" and item["health_outcome"] != "HEALTHY")
        for item in entries
    )
    outcome = "ERROR" if errors else ("HOLD" if holds else "COMPLETE")
    return {
        "lane_count": 6,
        "recorded_count": recorded,
        "hold_count": holds,
        "error_count": errors,
        "overall_outcome": outcome,
        "separate_interpretation_gate_required": True,
    }


def _entry_finding(
    entry: Mapping[str, Any], index: int, start: datetime, end: datetime
) -> Finding | None:
    result = entry["check_result"]
    health = entry["health_outcome"]
    checked_raw = entry["checked_at"]
    reasons = entry["reason_codes"]
    path = f"/entries/{index}"

    checked = _parse_time(checked_raw) if checked_raw is not None else None
    if checked is not None and not (start <= checked <= end):
        return Finding("COUNTY_RECENCY_CHECK_TIME_OUTSIDE_WEEK", path + "/checked_at")

    if result == "RECORDED":
        if checked is None or health == "UNKNOWN":
            return Finding("COUNTY_RECENCY_ENTRY_STATE_INCONSISTENT", path)
        expected_reason = HEALTH_REASON[health]
    elif result == "MISSED":
        if checked is not None or health != "UNKNOWN":
            return Finding("COUNTY_RECENCY_ENTRY_STATE_INCONSISTENT", path)
        expected_reason = "CHECK_MISSING"
    else:
        if checked is None or health != "UNKNOWN":
            return Finding("COUNTY_RECENCY_ENTRY_STATE_INCONSISTENT", path)
        expected_reason = "CHECK_ERROR"

    if reasons != [expected_reason]:
        return Finding("COUNTY_RECENCY_ENTRY_REASON_MISMATCH", path + "/reason_codes")
    return None


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return ValidationResult(
            "DENY",
            (Finding("COUNTY_RECENCY_SCHEMA_INVALID", _json_pointer(errors[0].absolute_path)),),
        )

    week = document["week"]
    start = _parse_time(week["period_start"])
    end = _parse_time(week["period_end"])
    assessed = _parse_time(week["assessed_at"])
    if any(value.utcoffset() != timedelta(0) for value in (start, end, assessed)):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_WEEK_TIMEZONE_INVALID", "/week"),)
        )
    if end - start != timedelta(hours=168):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_WEEK_DURATION_INVALID", "/week"),)
        )
    if assessed < end:
        return ValidationResult(
            "DENY",
            (Finding("COUNTY_RECENCY_ASSESSMENT_BEFORE_END", "/week/assessed_at"),),
        )

    entries = document["entries"]
    if tuple(item["lane"] for item in entries) != LANES:
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_LANE_SET_INVALID", "/entries"),)
        )
    if len({item["source_descriptor_ref"] for item in entries}) != len(entries):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_SOURCE_REF_REUSED", "/entries"),)
        )
    if len({item["source_health_assessment_ref"] for item in entries}) != len(entries):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_HEALTH_REF_REUSED", "/entries"),)
        )

    for index, entry in enumerate(entries):
        finding = _entry_finding(entry, index, start, end)
        if finding is not None:
            return ValidationResult("DENY", (finding,))

    if document["summary"] != expected_summary(document):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_SUMMARY_MISMATCH", "/summary"),)
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_SPEC_HASH_MISMATCH", "/spec_hash"),)
        )
    actual_id = expected_spine_id(actual_hash)
    if not hmac.compare_digest(document["spine_id"], actual_id):
        return ValidationResult(
            "DENY", (Finding("COUNTY_RECENCY_ID_MISMATCH", "/spine_id"),)
        )

    outcome = document["summary"]["overall_outcome"]
    if outcome == "COMPLETE":
        return ValidationResult("PASS", ())
    if outcome == "HOLD":
        return ValidationResult(
            "ABSTAIN", (Finding("COUNTY_RECENCY_HOLD", "/summary/overall_outcome"),)
        )
    return ValidationResult(
        "ERROR", (Finding("COUNTY_RECENCY_CHECK_ERROR", "/summary/overall_outcome"),)
    )


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
    document["spine_id"] = expected_spine_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "spine_id_override" in case:
        document["spine_id"] = case["spine_id_override"]
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
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
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
        document = _load_document(args.path)
        result = validate_payload(document)
    except DuplicateKeyError:
        result = ValidationResult("ERROR", (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult(
            "ERROR", (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),)
        )
    except InputTooLargeError:
        result = ValidationResult("ERROR", (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"outcome": result.outcome, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
