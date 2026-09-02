#!/usr/bin/env python3
"""Validate a fixture-only sensitive-overlay reveal-expiry transition.

The validator consumes hashes and synthetic verification summaries only. It
derives state, countdown, target view, and required actions, but performs no
token parsing, key handling, cleanup, UI mutation, receipt write, policy
evaluation, release, or publication.
"""

from __future__ import annotations

import argparse
import copy
import hmac
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for import_root in (REPO_ROOT, HASHING_SRC):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from hashing import compute_spec_hash  # noqa: E402
from tools.validators._common.public_safe_fixture import (  # noqa: E402
    validate_fixture_file,
)


SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/"
    "sensitive_overlay_reveal_expiry.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/"
    "sensitive_overlay_reveal_expiry/cases.json"
)
PROFILE = "kfm.sensitive-overlay-reveal-expiry.fixture.v1"
SCOPE = "sensitive-overlay-reveal-expiry-summary-only"
MAX_TTL = timedelta(hours=24)
EXPIRING_WINDOW = timedelta(minutes=5)
CLEANUP_ACTIONS = (
    "DISCARD_CLIENT_KEY",
    "EMIT_REVEAL_AUDIT_RECEIPT",
    "REMOVE_DECRYPTED_OVERLAY",
    "RESTORE_BLURRED_VIEW",
)
ACTIVE_ACTIONS = (
    "KEEP_COUNTDOWN_VISIBLE",
    "SCHEDULE_EXPIRY_INVALIDATION",
)
EXPIRING_ACTIONS = (
    "KEEP_COUNTDOWN_VISIBLE",
    "SCHEDULE_EXPIRY_INVALIDATION",
    "WARN_REVEAL_EXPIRING",
)
LIMITATIONS = (
    "actions_are_declarative_only",
    "fixture_only",
    "no_cleanup_side_effects",
    "no_key_or_raw_token_material",
    "no_live_policy_or_attestation_verification",
    "no_release_or_publication",
    "no_ui_runtime_mutation",
)
NON_EFFECTS = (
    "no_raw_token_identity_key_or_genomic_material",
    "no_network_revocation_or_attestation_request",
    "no_decryption_or_cryptographic_erasure",
    "no_browser_cache_worker_map_or_hud_mutation",
    "no_audit_receipt_or_lifecycle_write",
    "no_policy_release_deployment_or_publication_authority",
)
FORBIDDEN_SECRET_FIELDS = frozenset(
    {
        "access_token",
        "bearer_token",
        "credential",
        "decryption_key",
        "genomic_payload",
        "identity_token",
        "jwt",
        "key",
        "key_material",
        "private_key",
        "raw_token",
        "secret",
        "token",
    }
)
ABSTAIN_REASONS = frozenset(
    {
        "ATTESTATION_UNKNOWN",
        "REVOCATION_STATUS_UNKNOWN",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    """One stable finding that contains no candidate value."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite transition result."""

    outcome: str
    lease_state: str
    required_actions: tuple[str, ...]
    findings: tuple[Finding, ...]


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


@lru_cache(maxsize=1)
def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    return (
        "kfm:sensitive-overlay-reveal-expiry:"
        + spec_hash.removeprefix("sha256:")[:24]
    )


def _parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc)


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code, path))


def _schema_findings(document: object) -> set[Finding]:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    return {
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:100]
    }


def _find_secret_fields(
    value: object,
    findings: set[Finding],
    path: str = "",
) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_path = f"{path}/{str(key).replace('~', '~0').replace('/', '~1')}"
            if key in FORBIDDEN_SECRET_FIELDS:
                _add(findings, "SECRET_FIELD_DENIED", child_path)
            _find_secret_fields(child, findings, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _find_secret_fields(child, findings, f"{path}/{index}")


def _remaining_seconds(evaluated_at: datetime, expires_at: datetime) -> int:
    remaining = max(0, int((expires_at - evaluated_at).total_seconds()))
    return min(86400, remaining)


def derive_assessment(document: Mapping[str, Any]) -> dict[str, Any]:
    """Derive the pure transition result from a schema-shaped summary."""

    lease = _mapping(document.get("lease"))
    evaluated_at = _parse_datetime(document.get("evaluated_at"))
    issued_at = _parse_datetime(lease.get("issued_at"))
    expires_at = _parse_datetime(lease.get("expires_at"))
    checked_at = _parse_datetime(lease.get("revocation_checked_at"))
    if evaluated_at is None or issued_at is None or expires_at is None:
        raise ValueError("schema-shaped timestamps are required")

    seconds_remaining = _remaining_seconds(evaluated_at, expires_at)
    revoked = lease.get("revoked") is True or lease.get("revocation_status") == "REVOKED"
    if revoked:
        return {
            "lease_state": "REVOKED",
            "outcome": "DENY",
            "seconds_remaining": seconds_remaining,
            "reason_codes": ["REVEAL_REVOKED"],
            "required_actions": list(CLEANUP_ACTIONS),
            "target_view_state": "BLURRED",
            "authority": "NONE",
        }

    deny_reasons: list[str] = []
    interval_valid = expires_at > issued_at
    if not interval_valid:
        deny_reasons.append("LEASE_INTERVAL_INVALID")
    elif expires_at - issued_at > MAX_TTL:
        deny_reasons.append("LEASE_TTL_EXCEEDED")
    if evaluated_at < issued_at:
        deny_reasons.append("TOKEN_NOT_YET_VALID")
    if lease.get("single_use") is not True:
        deny_reasons.append("TOKEN_NOT_SINGLE_USE")
    if lease.get("consumed") is True:
        deny_reasons.append("TOKEN_ALREADY_CONSUMED")
    if checked_at != evaluated_at:
        deny_reasons.append("REVOCATION_CHECK_STALE")
    if lease.get("revocation_status") == "UNKNOWN":
        deny_reasons.append("REVOCATION_STATUS_UNKNOWN")
    if lease.get("attestation_status") == "FAILED":
        deny_reasons.append("ATTESTATION_FAILED")
    elif lease.get("attestation_status") != "VERIFIED":
        deny_reasons.append("ATTESTATION_UNKNOWN")
    policy_hash = lease.get("policy_hash")
    current_policy_hash = lease.get("current_policy_hash")
    if not (
        isinstance(policy_hash, str)
        and isinstance(current_policy_hash, str)
        and hmac.compare_digest(policy_hash, current_policy_hash)
    ):
        deny_reasons.append("POLICY_HASH_STALE")

    if deny_reasons:
        outcome = (
            "ABSTAIN"
            if set(deny_reasons).issubset(ABSTAIN_REASONS)
            else "DENY"
        )
        return {
            "lease_state": "ABSTAINED" if outcome == "ABSTAIN" else "DENIED",
            "outcome": outcome,
            "seconds_remaining": seconds_remaining,
            "reason_codes": deny_reasons,
            "required_actions": list(CLEANUP_ACTIONS),
            "target_view_state": "BLURRED",
            "authority": "NONE",
        }
    if evaluated_at >= expires_at:
        return {
            "lease_state": "EXPIRED",
            "outcome": "DENY",
            "seconds_remaining": 0,
            "reason_codes": ["REVEAL_EXPIRED"],
            "required_actions": list(CLEANUP_ACTIONS),
            "target_view_state": "BLURRED",
            "authority": "NONE",
        }
    if expires_at - evaluated_at <= EXPIRING_WINDOW:
        return {
            "lease_state": "EXPIRING",
            "outcome": "HOLD",
            "seconds_remaining": seconds_remaining,
            "reason_codes": ["REVEAL_EXPIRING"],
            "required_actions": list(EXPIRING_ACTIONS),
            "target_view_state": "REVEALED",
            "authority": "NONE",
        }
    return {
        "lease_state": "ACTIVE",
        "outcome": "HOLD",
        "seconds_remaining": seconds_remaining,
        "reason_codes": ["REVEAL_ACTIVE"],
        "required_actions": list(ACTIVE_ACTIONS),
        "target_view_state": "REVEALED",
        "authority": "NONE",
    }


def validate_payload(document: object) -> ValidationResult:
    """Validate one materialized summary and its declared transition."""

    schema_findings = _schema_findings(document)
    if schema_findings:
        return ValidationResult(
            "DENY",
            "DENIED",
            CLEANUP_ACTIONS,
            tuple(sorted(schema_findings)),
        )
    assert isinstance(document, Mapping)

    findings: set[Finding] = set()
    _find_secret_fields(document, findings)

    expected_hash = expected_spec_hash(document)
    spec_hash = document.get("spec_hash")
    if not (
        isinstance(spec_hash, str)
        and hmac.compare_digest(spec_hash, expected_hash)
    ):
        _add(findings, "SPEC_HASH_MISMATCH", "/spec_hash")
    expected_id = expected_assessment_id(expected_hash)
    assessment_id = document.get("assessment_id")
    if not (
        isinstance(assessment_id, str)
        and hmac.compare_digest(assessment_id, expected_id)
    ):
        _add(findings, "ASSESSMENT_ID_MISMATCH", "/assessment_id")

    if document.get("limitations") != list(LIMITATIONS):
        _add(findings, "LIMITATIONS_MISMATCH", "/limitations")

    lease = _mapping(document.get("lease"))
    revoked_flag = lease.get("revoked") is True
    revoked_status = lease.get("revocation_status") == "REVOKED"
    if revoked_flag != revoked_status:
        _add(
            findings,
            "REVOCATION_SUMMARY_INCONSISTENT",
            "/lease/revocation_status",
        )

    governance = _mapping(document.get("governance"))
    denied_governance = {
        "raw_token_material_present": "RAW_TOKEN_MATERIAL_DENIED",
        "key_material_present": "KEY_MATERIAL_DENIED",
        "cleanup_performed": "CLEANUP_SIDE_EFFECT_CLAIM_DENIED",
        "audit_receipt_emitted": "AUDIT_RECEIPT_CLAIM_DENIED",
        "policy_evaluated": "POLICY_EVALUATION_CLAIM_DENIED",
        "release_issued": "RELEASE_AUTHORITY_DENIED",
        "publication_authorized": "PUBLICATION_AUTHORITY_DENIED",
    }
    for field, code in denied_governance.items():
        if governance.get(field) is not False:
            _add(findings, code, f"/governance/{field}")

    expected = derive_assessment(document)
    assessment = _mapping(document.get("assessment"))
    comparisons = (
        ("lease_state", "ASSESSMENT_LEASE_STATE_MISMATCH"),
        ("outcome", "ASSESSMENT_OUTCOME_MISMATCH"),
        ("seconds_remaining", "ASSESSMENT_COUNTDOWN_MISMATCH"),
        ("reason_codes", "ASSESSMENT_REASON_CODES_MISMATCH"),
        ("required_actions", "ASSESSMENT_ACTIONS_MISMATCH"),
        ("target_view_state", "ASSESSMENT_TARGET_VIEW_MISMATCH"),
        ("authority", "ASSESSMENT_AUTHORITY_MISMATCH"),
    )
    for field, code in comparisons:
        if assessment.get(field) != expected[field]:
            _add(findings, code, f"/assessment/{field}")

    return ValidationResult(
        "DENY" if findings else expected["outcome"],
        str(expected["lease_state"]),
        tuple(expected["required_actions"]),
        tuple(sorted(findings)),
    )


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest must be an object")
    return value


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be a JSON pointer")
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    """Apply input mutations, derive transition, then apply assertion mutations."""

    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    document["assessment"] = derive_assessment(document)
    for mutation in case.get("assessment_mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    return document


def validate_file(path: Path | str) -> ValidationResult:
    captured: list[object] = []

    def capture(candidate: object) -> list[Any]:
        captured.append(candidate)
        return []

    parser_findings = validate_fixture_file(path, capture)
    if parser_findings:
        return ValidationResult(
            "ERROR",
            "ERROR",
            CLEANUP_ACTIONS,
            tuple(Finding(item.code, item.path) for item in parser_findings),
        )
    if len(captured) != 1:
        return ValidationResult(
            "ERROR",
            "ERROR",
            CLEANUP_ACTIONS,
            (Finding("FIXTURE_JSON_INVALID", "/"),),
        )
    return validate_payload(captured[0])


def render_result(result: ValidationResult) -> str:
    payload = {
        "authority": "NONE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "lease_state": result.lease_state,
        "non_effects": list(NON_EFFECTS),
        "outcome": result.outcome,
        "required_actions": list(result.required_actions),
        "scope": SCOPE,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _run_fixture_suite() -> int:
    manifest = load_fixtures()
    rows = []
    suite_match = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        case_match = (
            result.outcome == case["expected_outcome"]
            and result.lease_state == case["expected_state"]
            and actual_findings == case["expected_findings"]
        )
        suite_match = suite_match and case_match
        rows.append(
            {
                "case_id": case["case_id"],
                "lease_state": result.lease_state,
                "match": case_match,
                "outcome": result.outcome,
            }
        )
    payload = {
        "authority": "NONE",
        "case_count": len(rows),
        "cases": rows,
        "non_effects": list(NON_EFFECTS),
        "profile": PROFILE,
        "suite_match": suite_match,
    }
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0 if suite_match else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="validate the frozen synthetic transition matrix",
    )
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("path cannot be combined with --fixtures")
        return _run_fixture_suite()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(render_result(result))
    if result.outcome == "ERROR":
        return 2
    return 0 if result.outcome == "HOLD" else 1


if __name__ == "__main__":
    raise SystemExit(main())
