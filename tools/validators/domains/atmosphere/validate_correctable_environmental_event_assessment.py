#!/usr/bin/env python3
"""Validate fixture-only correctable environmental-event lifecycle packets."""
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

SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:correctable-event:"


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
            return None, (Finding("EVENT_LIFECYCLE_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("EVENT_LIFECYCLE_FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("EVENT_LIFECYCLE_FILE_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("EVENT_LIFECYCLE_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("EVENT_LIFECYCLE_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("EVENT_LIFECYCLE_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("EVENT_LIFECYCLE_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("EVENT_LIFECYCLE_SCHEMA_UNAVAILABLE", "/"),)
    return tuple(sorted(Finding("EVENT_LIFECYCLE_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors))


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


def expected_assessment(value: Mapping[str, Any]) -> dict[str, str]:
    if value["assessment_state"] == "ERROR" or value["integrity"]["source_state"] == "ERROR":
        return {"outcome": "ERROR", "reason_code": "UPSTREAM_ERROR"}
    if value["integrity"]["freshness"] != "FRESH":
        return {"outcome": "HOLD", "reason_code": "SOURCE_INTEGRITY_HOLD"}
    if value["lifecycle_scope"] == "CANDIDATE_ONLY":
        return {"outcome": "HOLD", "reason_code": "CANDIDATE_REMAINS_PROVISIONAL"}
    if value["lifecycle_scope"] == "EVENT_CORRECTED":
        return {"outcome": "CORRECTION_CHAIN_CONFIRMED", "reason_code": "CORRECTION_LINEAGE_CONFIRMED"}
    return {"outcome": "EVENT_CHAIN_CONFIRMED", "reason_code": "EVENT_TRANSITION_CONFIRMED"}


def _scope_matches(value: Mapping[str, Any]) -> bool:
    subject = value["subject"]
    scope = value["lifecycle_scope"]
    event_fields = ["review_disposition_ref", "event_ref", "event_basis_candidate_ref", "reviewed_at", "event_at"]
    correction_fields = ["correction_ref", "correction_of_event_ref", "replacement_event_ref", "corrected_at"]
    if scope == "CANDIDATE_ONLY":
        return all(subject[field] is None for field in event_fields + correction_fields)
    if scope == "EVENT_DECLARED":
        return all(subject[field] is not None for field in event_fields) and all(subject[field] is None for field in correction_fields)
    return all(subject[field] is not None for field in event_fields + correction_fields)


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    subject = value["subject"]
    roles = subject["source_roles"]
    role_names = [entry["role"] for entry in roles]
    source_refs = [entry["source_ref"] for entry in roles]
    if role_names != sorted(role_names) or len(role_names) != len(set(role_names)):
        out.add(Finding("EVENT_LIFECYCLE_SOURCE_ROLE_ORDER_INVALID", "/subject/source_roles"))
    if len(source_refs) != len(set(source_refs)):
        out.add(Finding("EVENT_LIFECYCLE_SOURCE_ROLE_COLLAPSE", "/subject/source_roles"))
    required_roles = {"BASELINE_SOURCE", "OBSERVATION_SOURCE"}
    if value["lifecycle_scope"] != "CANDIDATE_ONLY":
        required_roles.add("CORROBORATION_SOURCE")
    if not required_roles.issubset(set(role_names)):
        out.add(Finding("EVENT_LIFECYCLE_SOURCE_ROLE_INCOMPLETE", "/subject/source_roles"))

    if subject["observation_ref"] not in subject["candidate_basis_observation_refs"]:
        out.add(Finding("EVENT_LIFECYCLE_OBSERVATION_BASIS_MISSING", "/subject/candidate_basis_observation_refs"))
    if value["lifecycle_scope"] != "CANDIDATE_ONLY" and subject["event_basis_candidate_ref"] != subject["candidate_ref"]:
        out.add(Finding("EVENT_LIFECYCLE_CANDIDATE_BASIS_MISMATCH", "/subject/event_basis_candidate_ref"))
    if value["lifecycle_scope"] == "EVENT_CORRECTED" and subject["correction_of_event_ref"] != subject["event_ref"]:
        out.add(Finding("EVENT_LIFECYCLE_CORRECTION_TARGET_MISMATCH", "/subject/correction_of_event_ref"))

    role_refs = [
        subject["observation_ref"],
        subject["candidate_ref"],
        subject["baseline_snapshot_ref"],
        subject["review_disposition_ref"],
        subject["event_ref"],
        subject["correction_ref"],
        subject["replacement_event_ref"],
    ]
    present_refs = [item for item in role_refs if item is not None]
    if len(present_refs) != len(set(present_refs)):
        out.add(Finding("EVENT_LIFECYCLE_REFERENCE_ROLE_COLLAPSE", "/subject"))
    if not _scope_matches(value):
        out.add(Finding("EVENT_LIFECYCLE_SCOPE_MISMATCH", "/subject"))

    ordered_times = [
        _time(subject["observed_at"]),
        _time(subject["candidate_at"]),
        _time(subject["reviewed_at"]),
        _time(subject["event_at"]),
        _time(subject["corrected_at"]),
    ]
    present_times = [item for item in ordered_times if item is not None]
    if any(left > right for left, right in zip(present_times, present_times[1:])):
        out.add(Finding("EVENT_LIFECYCLE_TIME_ORDER_INVALID", "/subject"))

    if value["assessment"] != expected_assessment(value):
        out.add(Finding("EVENT_LIFECYCLE_ASSESSMENT_MISMATCH", "/assessment"))
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("EVENT_LIFECYCLE_CANONICALIZATION_FAILED", "/spec_hash"))
    else:
        if value["spec_hash"] != expected_hash:
            out.add(Finding("EVENT_LIFECYCLE_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            out.add(Finding("EVENT_LIFECYCLE_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
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
        return Result("ABSTAIN", (Finding("EVENT_LIFECYCLE_HELD", "/assessment/outcome"),))
    if outcome == "ERROR":
        return Result("ERROR", (Finding("EVENT_LIFECYCLE_UPSTREAM_ERROR", "/assessment/outcome"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(json.dumps({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "file": args.input.as_posix(),
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "non_effects": ["no_network_or_live_feed", "no_threshold_or_candidate_promotion", "no_real_event_correction_or_alert", "no_policy_review_release_or_publication"],
        "outcome": result.outcome,
    }, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
