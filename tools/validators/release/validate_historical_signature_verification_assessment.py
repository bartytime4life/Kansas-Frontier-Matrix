#!/usr/bin/env python3
"""Validate fixture-only HistoricalSignatureVerificationAssessment records."""
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
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/release/historical_signature_verification_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/release/historical_signature_verification_assessment/cases.json"
PREFIX = "kfm:historical-signature:"
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
            return None, (Finding("HISTORICAL_SIGNATURE_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("HISTORICAL_SIGNATURE_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("HISTORICAL_SIGNATURE_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("HISTORICAL_SIGNATURE_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("HISTORICAL_SIGNATURE_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("HISTORICAL_SIGNATURE_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("HISTORICAL_SIGNATURE_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"assessment_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def derive_status(events: Sequence[Mapping[str, Any]], when: datetime | None) -> str:
    if when is None:
        return "UNKNOWN"
    status = "UNKNOWN"
    for event in events:
        effective = _time(event["effective_at"])
        if effective is not None and effective <= when:
            status = event["status"]
        elif effective is not None and effective > when:
            break
    return status


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        state, reason = "ERROR", "ASSESSMENT_ERROR"
    else:
        verification = value["verification"]
        signing_status = value["status_at_signing"]
        current_status = value["status_at_verification"]
        if verification["cryptographic_result"] == "FAILED":
            state, reason = "INVALID_SIGNATURE", "DECLARED_SIGNATURE_VERIFICATION_FAILED"
        elif signing_status != "ACTIVE" or value["signer_authorized_at_signing"] is not True:
            state, reason = "UNAUTHORIZED_AT_SIGNING", "SIGNER_OR_KEY_UNAUTHORIZED_AT_SIGNING"
        elif (
            verification["cryptographic_result"] == "NOT_RUN"
            or verification["evidence_complete"] is not True
            or current_status == "UNKNOWN"
        ):
            state, reason = "UNKNOWN_TRUST", "VERIFICATION_EVIDENCE_INCOMPLETE"
        elif value["signing_trust_profile_version"] != value["verification_trust_profile_version"]:
            state, reason = "PROFILE_REEVALUATION_REQUIRED", "TRUST_PROFILE_VERSION_CHANGED"
        elif current_status == "COMPROMISED":
            state, reason = "REVIEW_COMPROMISE", "KEY_COMPROMISE_REVIEW_REQUIRED"
        elif current_status == "REVOKED":
            state, reason = "REVIEW_REVOKED_AFTER_SIGNING", "KEY_REVOKED_AFTER_SIGNING"
        elif current_status == "ACTIVE":
            state, reason = "VERIFIED_CURRENT", "CURRENT_TRUST_COHERENT"
        elif current_status in {"VERIFY_ONLY", "EXPIRED", "SUPERSEDED"}:
            state, reason = "VERIFIED_HISTORICAL", "HISTORICAL_TRUST_COHERENT"
        else:
            state, reason = "UNKNOWN_TRUST", "VERIFICATION_EVIDENCE_INCOMPLETE"
    return {
        "state": state,
        "reason_codes": [reason],
        "review_required": True,
        "release_authorized": False,
        "historical_evidence_rewritten": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("HISTORICAL_SIGNATURE_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("HISTORICAL_SIGNATURE_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("HISTORICAL_SIGNATURE_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _event_shape_is_coherent(event: Mapping[str, Any], signer_key_id: str) -> bool:
    status = event["status"]
    reason = event["reason"]
    superseded_by = event["superseded_by_key_id"]
    expected_reason = {
        "ACTIVE": "PROVISIONED",
        "VERIFY_ONLY": "ROTATION",
        "EXPIRED": "EXPIRY",
        "REVOKED": "ADMINISTRATIVE_REVOCATION",
        "COMPROMISED": "KEY_COMPROMISE",
        "SUPERSEDED": "SUPERSESSION",
        "UNKNOWN": "TRUST_UNKNOWN",
    }[status]
    if reason != expected_reason:
        return False
    if status == "SUPERSEDED":
        return superseded_by is not None and superseded_by != signer_key_id
    return superseded_by is None


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("HISTORICAL_SIGNATURE_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("HISTORICAL_SIGNATURE_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("HISTORICAL_SIGNATURE_ID_MISMATCH", "/assessment_id"))

    signed = _time(value["signed_at"])
    verified = _time(value["verified_at"])
    if signed is not None and verified is not None and signed > verified:
        findings.add(Finding("HISTORICAL_SIGNATURE_TIME_ORDER_INVALID", "/verified_at"))

    events = value["key_status_events"]
    expected_sequence = 1
    previous_time: datetime | None = None
    for index, event in enumerate(events):
        if event["sequence"] != expected_sequence:
            findings.add(Finding("HISTORICAL_SIGNATURE_EVENT_SEQUENCE_INVALID", f"/key_status_events/{index}/sequence"))
            break
        current_time = _time(event["effective_at"])
        if previous_time is not None and current_time is not None and current_time <= previous_time:
            findings.add(Finding("HISTORICAL_SIGNATURE_EVENT_TIME_INVALID", f"/key_status_events/{index}/effective_at"))
            break
        if not _event_shape_is_coherent(event, value["signer_key_id"]):
            findings.add(Finding("HISTORICAL_SIGNATURE_EVENT_STATE_INVALID", f"/key_status_events/{index}"))
            break
        previous_time = current_time
        expected_sequence += 1
    if previous_time is not None and verified is not None and previous_time > verified:
        findings.add(Finding("HISTORICAL_SIGNATURE_EVENT_AFTER_VERIFICATION", "/key_status_events"))

    expected_signing_status = derive_status(events, signed)
    expected_verification_status = derive_status(events, verified)
    if value["status_at_signing"] != expected_signing_status:
        findings.add(Finding("HISTORICAL_SIGNATURE_SIGNING_STATUS_MISMATCH", "/status_at_signing"))
    if value["status_at_verification"] != expected_verification_status:
        findings.add(Finding("HISTORICAL_SIGNATURE_VERIFICATION_STATUS_MISMATCH", "/status_at_verification"))

    verification = value["verification"]
    if verification["mode"] == "OFFLINE":
        if verification["offline_material_ref"] is None:
            findings.add(Finding("HISTORICAL_SIGNATURE_OFFLINE_MATERIAL_REQUIRED", "/verification/offline_material_ref"))
    elif verification["offline_material_ref"] is not None:
        findings.add(Finding("HISTORICAL_SIGNATURE_OFFLINE_MATERIAL_FORBIDDEN", "/verification/offline_material_ref"))

    if value["decision"] != recompute_decision(value):
        findings.add(Finding("HISTORICAL_SIGNATURE_DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    state = value["decision"]["state"]
    if state in {"VERIFIED_CURRENT", "VERIFIED_HISTORICAL"}:
        return Result("PASS", ())
    if state in {"REVIEW_REVOKED_AFTER_SIGNING", "REVIEW_COMPROMISE", "PROFILE_REEVALUATION_REQUIRED", "UNKNOWN_TRUST"}:
        return Result("ABSTAIN", (Finding(value["decision"]["reason_codes"][0], "/decision/state"),))
    if state in {"INVALID_SIGNATURE", "UNAUTHORIZED_AT_SIGNING"}:
        return Result("DENY", (Finding(value["decision"]["reason_codes"][0], "/decision/state"),))
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
    document["decision"] = copy.deepcopy(case.get("decision_override", recompute_decision(document)))
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
            failures.append({"case_id": case["case_id"], "expected_outcome": case["expected_outcome"], "actual_outcome": result.outcome, "expected_findings": case["expected_findings"], "actual_findings": actual})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": ["no_keys", "no_cryptography", "no_network", "no_trust_mutation", "no_signing", "no_release", "no_correction", "no_withdrawal", "no_publication"],
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
