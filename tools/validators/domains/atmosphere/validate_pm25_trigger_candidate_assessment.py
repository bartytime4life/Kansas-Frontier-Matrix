#!/usr/bin/env python3
"""Validate fixture-only PM2.5 trigger candidate assessments."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/pm25_trigger_candidate_assessment.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:pm25-trigger-candidate:"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("PM25_TRIGGER_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("PM25_TRIGGER_FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("PM25_TRIGGER_FILE_TOO_LARGE", "/"),)
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique, parse_constant=_reject_constant, parse_float=_finite)
    except DuplicateKeyError:
        return None, (Finding("PM25_TRIGGER_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("PM25_TRIGGER_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("PM25_TRIGGER_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("PM25_TRIGGER_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("PM25_TRIGGER_SCHEMA_UNAVAILABLE", "/"),)
    return tuple(sorted(Finding("PM25_TRIGGER_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors))


def _identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(_identity_subject(value))
    return spec_hash, IDENTITY_PREFIX + spec_hash.removeprefix("sha256:")[:24]


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def expected_assessment(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = value["subject"]
    integrity = value["integrity"]
    if integrity["input_state"] == "ERROR":
        return {"outcome": "ERROR", "reason_codes": ["UPSTREAM_ERROR"]}
    unknown = (
        subject["threshold_relation"] == "UNKNOWN"
        or subject["trailing_median_relation"] == "UNKNOWN"
        or integrity["freshness"] != "FRESH"
        or integrity["quality"] != "ACCEPTABLE"
        or integrity["source_state"] != "MONITORED"
    )
    if unknown:
        reason = "CONTEXT_INSUFFICIENT" if "UNKNOWN" in {subject["threshold_relation"], subject["trailing_median_relation"], integrity["freshness"], integrity["quality"], integrity["source_state"]} else "SOURCE_INTEGRITY_HOLD"
        return {"outcome": "HOLD", "reason_codes": [reason]}
    if subject["threshold_relation"] == "ABOVE_MONITORED_THRESHOLD" and subject["trailing_median_relation"] == "ABOVE_TRAILING_MEDIAN":
        return {"outcome": "PROPOSED_TRIGGER_CANDIDATE", "reason_codes": ["ABOVE_MONITORED_THRESHOLD", "ABOVE_TRAILING_MEDIAN"]}
    return {"outcome": "NO_TRIGGER_CANDIDATE", "reason_codes": ["AT_OR_BELOW_REFERENCE"]}


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    subject = value["subject"]
    if subject["observation_ref"] == subject["trailing_median_ref"]:
        out.add(Finding("PM25_TRIGGER_REFERENCE_ROLE_COLLAPSE", "/subject/trailing_median_ref"))
    observed = _time(subject["observed_at"])
    retrieved = _time(subject["retrieved_at"])
    if observed and retrieved and observed > retrieved:
        out.add(Finding("PM25_TRIGGER_TIME_ORDER_INVALID", "/subject/retrieved_at"))
    if value["assessment"]["outcome"] == "PROPOSED_TRIGGER_CANDIDATE" and len(subject["evidence_refs"]) < 2:
        out.add(Finding("PM25_TRIGGER_EVIDENCE_INSUFFICIENT", "/subject/evidence_refs"))
    if value["assessment"] != expected_assessment(value):
        out.add(Finding("PM25_TRIGGER_ASSESSMENT_MISMATCH", "/assessment"))
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("PM25_TRIGGER_CANONICALIZATION_FAILED", "/spec_hash"))
    else:
        if value["spec_hash"] != expected_hash:
            out.add(Finding("PM25_TRIGGER_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            out.add(Finding("PM25_TRIGGER_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return tuple(sorted(out))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    outcome = value["assessment"]["outcome"]
    if outcome == "HOLD":
        return Result("ABSTAIN", (Finding("PM25_TRIGGER_CONTEXT_HELD", "/assessment/outcome"),))
    if outcome == "ERROR":
        return Result("ERROR", (Finding("PM25_TRIGGER_UPSTREAM_ERROR", "/assessment/outcome"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(json.dumps({"authority": "NONE", "execution_mode": "FIXTURE_ONLY", "file": args.input.as_posix(), "findings": [{"code": item.code, "path": item.path} for item in result.findings], "non_effects": ["no_network", "no_numeric_threshold", "no_event_or_health_advice", "no_policy_review_release_or_publication"], "outcome": result.outcome}, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
