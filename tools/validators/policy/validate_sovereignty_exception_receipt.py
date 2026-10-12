#!/usr/bin/env python3
"""Validate fixture-only sovereignty exception receipt candidates.

PASS proves local record coherence only. It does not authenticate reviewers,
evaluate policy, grant an exception, allow access, release, or publish.
"""
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

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/policy/sovereignty_exception_receipt.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm://policy/sovereignty-exception-receipt/"


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
            return None, (Finding("SOVEREIGNTY_EXCEPTION_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("SOVEREIGNTY_EXCEPTION_FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("SOVEREIGNTY_EXCEPTION_FILE_TOO_LARGE", "/"),)
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique, parse_constant=_reject_constant, parse_float=_finite)
    except DuplicateKeyError:
        return None, (Finding("SOVEREIGNTY_EXCEPTION_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("SOVEREIGNTY_EXCEPTION_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("SOVEREIGNTY_EXCEPTION_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("SOVEREIGNTY_EXCEPTION_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("SOVEREIGNTY_EXCEPTION_SCHEMA_UNAVAILABLE", "/"),)
    return tuple(sorted(Finding("SOVEREIGNTY_EXCEPTION_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors))


def _identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("receipt_id", None)
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


def _canonical(values: object) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    decision = value["decision"]
    provenance = value["provenance"]
    disposition = decision["disposition"]

    for path, values in (
        ("/reason_codes", value["reason_codes"]),
        ("/decision/review_record_refs", decision["review_record_refs"]),
        ("/decision/obligations", decision["obligations"]),
        ("/provenance/evidence_refs", provenance["evidence_refs"]),
    ):
        if not _canonical(values):
            out.add(Finding("SOVEREIGNTY_EXCEPTION_REFERENCE_ORDER_INVALID", path))

    requested = _time(value["requested_at"])
    recorded = _time(value["recorded_at"])
    decided = _time(decision["decided_at"])
    expires = _time(decision["expires_at"])
    if requested and recorded and requested > recorded:
        out.add(Finding("SOVEREIGNTY_EXCEPTION_TIME_ORDER_INVALID", "/recorded_at"))
    if decided and requested and decided < requested:
        out.add(Finding("SOVEREIGNTY_EXCEPTION_TIME_ORDER_INVALID", "/decision/decided_at"))
    if decided and recorded and decided > recorded:
        out.add(Finding("SOVEREIGNTY_EXCEPTION_TIME_ORDER_INVALID", "/decision/decided_at"))

    external_complete = all((decision["policy_decision_ref"], decision["review_record_refs"], decision["approver_roster_ref"], decision["decided_at"], provenance["activity_ref"]))
    if disposition == "PENDING_REVIEW":
        if any((decision["policy_decision_ref"], decision["review_record_refs"], decision["approver_roster_ref"], decision["decided_at"], decision["expires_at"], decision["obligations"], provenance["activity_ref"])):
            out.add(Finding("SOVEREIGNTY_EXCEPTION_PENDING_STATE_CONFLICT", "/decision"))
    else:
        if not external_complete:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_EXTERNAL_AUTHORITY_INCOMPLETE", "/decision"))
        external_refs = [decision["policy_decision_ref"], decision["approver_roster_ref"], provenance["activity_ref"], *decision["review_record_refs"]]
        if value["receipt_id"] in external_refs:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_SELF_AUTHORITY_DENIED", "/decision"))

    if disposition == "RECORDED_APPROVED":
        required = {"AUDIT_REQUIRED", "EXPIRY_ENFORCED"}
        if value["requested_operation"] == "EXPORT":
            required.add("NO_RAW_EGRESS")
        if value["requested_operation"] == "RELEASE_CANDIDATE":
            required.add("GENERALIZED_OUTPUT_ONLY")
        if not required.issubset(set(decision["obligations"])):
            out.add(Finding("SOVEREIGNTY_EXCEPTION_OBLIGATIONS_INCOMPLETE", "/decision/obligations"))
        if expires is None or (recorded and expires <= recorded) or (decided and expires <= decided):
            out.add(Finding("SOVEREIGNTY_EXCEPTION_TIME_ORDER_INVALID", "/decision/expires_at"))
    elif disposition == "RECORDED_DENIED":
        if decision["expires_at"] is not None or decision["obligations"]:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_DENIAL_STATE_CONFLICT", "/decision"))
    elif disposition == "EXPIRED":
        if expires is None or recorded is None or expires > recorded:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_EXPIRY_STATE_INVALID", "/decision/expires_at"))

    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("SOVEREIGNTY_EXCEPTION_CANONICALIZATION_FAILED", "/spec_hash"))
    else:
        if value["spec_hash"] != expected_hash:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["receipt_id"] != expected_id:
            out.add(Finding("SOVEREIGNTY_EXCEPTION_RECEIPT_ID_MISMATCH", "/receipt_id"))
    return tuple(sorted(out))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    if value["decision"]["disposition"] == "PENDING_REVIEW":
        return Result("ABSTAIN", (Finding("SOVEREIGNTY_EXCEPTION_PENDING_REVIEW", "/decision/disposition"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(json.dumps({"authority": "NONE", "execution_mode": "FIXTURE_ONLY", "file": args.input.as_posix(), "findings": [{"code": item.code, "path": item.path} for item in result.findings], "non_effects": ["no_network", "no_exception_authority", "no_policy_override", "no_access", "no_lifecycle_write", "no_release_or_publication"], "outcome": result.outcome}, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
