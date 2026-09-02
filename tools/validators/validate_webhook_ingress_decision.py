#!/usr/bin/env python3
"""Validate proposed WebhookIngressDecision records without network access.

A pass proves bounded schema and fixture semantics only. It does not verify a
provider secret or signature, activate a source, write RAW, operate a queue or
DLQ, evaluate policy, attest materialization, promote, release, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/webhook_ingress_decision.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/webhook_ingress_decision"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "webhook-ingress-decision-shape-replay-routing-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(item.code.startswith(("FILE_", "JSON_", "INPUT_", "ROOT_", "SCHEMA_UNAVAILABLE")) for item in self.findings)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise NonFiniteNumberError
    return result


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(projected, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    supplied = candidate.get("spec_hash")
    if isinstance(supplied, str) and supplied != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    source = _mapping(candidate.get("source"))
    event = _mapping(candidate.get("event"))
    verification = _mapping(candidate.get("verification"))
    idem = _mapping(candidate.get("idempotency"))
    fallback = _mapping(candidate.get("fallback"))
    decision = _mapping(candidate.get("decision"))
    governance = _mapping(candidate.get("governance"))
    dlq = _mapping(decision.get("dlq"))

    outcome = decision.get("outcome")
    next_action = decision.get("next_action")
    signature_ok = verification.get("signature_status") == "VALID"
    timestamp_ok = (
        verification.get("timestamp_status") == "FRESH"
        and isinstance(verification.get("event_age_seconds"), int)
        and isinstance(verification.get("max_skew_seconds"), int)
        and verification["event_age_seconds"] <= verification["max_skew_seconds"]
    )
    nonce_ok = verification.get("nonce_status") == "UNSEEN"

    if any(verification.get(name) is not False for name in ("raw_signature_persisted", "raw_secret_persisted", "raw_nonce_persisted")):
        findings.append(Finding("SECRET_PERSISTENCE_DENIED", "/verification"))

    if outcome == "ACCEPT":
        if not (signature_ok and timestamp_ok and nonce_ok and idem.get("status") == "NEW" and source.get("activation_state") == "ACTIVE"):
            findings.append(Finding("ACCEPT_VERIFICATION_INCOMPLETE", "/decision/outcome"))
        if verification.get("timestamp_status") == "STALE" or (
            isinstance(verification.get("event_age_seconds"), int)
            and isinstance(verification.get("max_skew_seconds"), int)
            and verification["event_age_seconds"] > verification["max_skew_seconds"]
        ):
            findings.append(Finding("STALE_EVENT_NOT_REJECTED", "/verification/timestamp_status"))
        if verification.get("nonce_status") == "REPLAYED":
            findings.append(Finding("NONCE_REPLAY_NOT_REJECTED", "/verification/nonce_status"))
        if next_action != "ADMIT_TO_RAW" or not isinstance(decision.get("materialization_request_key"), str):
            findings.append(Finding("ACCEPT_ROUTE_INVALID", "/decision"))

    if idem.get("status") == "DUPLICATE_MATCH":
        digest_mismatch = idem.get("prior_body_digest") != event.get("body_digest")
        if digest_mismatch:
            findings.append(Finding("IDEMPOTENCY_DIGEST_MISMATCH", "/idempotency/prior_body_digest"))
        if digest_mismatch or outcome != "DUPLICATE_NOOP" or next_action != "NOOP" or decision.get("materialization_request_key") is not None or idem.get("side_effects_applied") is not False or fallback.get("mode") != "NONE" or dlq.get("required") is not False:
            findings.append(Finding("DUPLICATE_NOOP_INVALID", "/decision"))

    if fallback.get("mode") == "CONDITIONAL_POLL":
        trigger_ok = fallback.get("trigger") in {"SEQUENCE_GAP", "PROVIDER_MAINTENANCE", "WEBHOOK_UNAVAILABLE", "VERIFIER_ERROR"}
        validator_ok = isinstance(fallback.get("etag"), str) or isinstance(fallback.get("last_modified"), str)
        if not trigger_ok or fallback.get("conditional_request_required") is not True or not validator_ok or not isinstance(fallback.get("poll_request_key"), str):
            findings.append(Finding("POLLING_FALLBACK_INVALID", "/fallback"))
        if fallback.get("trigger") == "SEQUENCE_GAP" and _mapping(event.get("sequence")).get("gap_detected") is not True:
            findings.append(Finding("SEQUENCE_GAP_TRIGGER_UNSUPPORTED", "/event/sequence/gap_detected"))

    if decision.get("materialization_attestation_required_before_publish") is not True:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/decision/materialization_attestation_required_before_publish"))
    governed_flags = (
        "raw_body_public",
        "canonical_source_mutated",
        "evidence_closure_claimed",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
        "public_route_created",
    )
    if any(governance.get(name) is not False for name in governed_flags):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    if governance.get("rollback_attestation_ref") is not None:
        findings.append(Finding("ROLLBACK_ATTESTATION_PREMATURE", "/governance/rollback_attestation_ref"))

    return findings


def validate_decision(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_manifest() -> dict[str, list[str]]:
    path = FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected findings manifest must be an object")
    return {str(name): sorted(str(code) for code in codes) for name, codes in value.items() if isinstance(name, str) and isinstance(codes, list)}


def validate_fixtures() -> int:
    valid_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted(path for path in (FIXTURE_ROOT / "invalid").glob("*.json") if path.name != "expected_findings_manifest.json")
    try:
        expected = _expected_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        print("ERROR: expected findings manifest is unavailable or invalid.")
        return 1
    if not valid_paths or not invalid_paths or sorted(expected) != [path.name for path in invalid_paths]:
        print("ERROR: webhook ingress fixture inventory is incomplete or drifted.")
        return 1
    failed = False
    for path in valid_paths:
        result = validate_decision(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    for path in invalid_paths:
        result = validate_decision(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        failed = failed or result.ok or actual != expected[path.name]
    if failed:
        print("ERROR: webhook ingress fixture polarity failed.")
        return 1
    print(f"CONFIRMED: {len(valid_paths)} valid and {len(invalid_paths)} invalid webhook ingress fixtures passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM WebhookIngressDecision records.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_decision(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
