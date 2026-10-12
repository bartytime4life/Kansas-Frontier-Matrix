#!/usr/bin/env python3
"""Validate fixture-only ReviewShareLink records."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/review/review_share_link.schema.json"
MAX_JSON_BYTES = 256 * 1024
MAX_SCHEMA_FINDINGS = 100
SAFE_REF_PREFIXES = ("/api/", "/release/", "/reports/", "kfm://")
DENIED_PATH_PARTS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "/processed/",
    "/proofs/",
    "/canonical/",
    "/internal/",
)


class DuplicateKeyError(ValueError):
    """Raised when an object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised for NaN or Infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_payload(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    ordered = sorted(errors, key=lambda error: (_pointer(error.absolute_path), str(error.validator)))[:MAX_SCHEMA_FINDINGS]
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in ordered]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(payload: Mapping[str, Any]) -> str:
    """Return deterministic SHA-256 over the object without top-level spec_hash."""
    body = {key: value for key, value in payload.items() if key != "spec_hash"}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _is_safe_ref(value: str) -> bool:
    lowered = value.lower()
    parsed = urlsplit(value)
    if parsed.scheme in {"http", "https"} or value.startswith("//"):
        return False
    if not value.startswith(SAFE_REF_PREFIXES):
        return False
    return not any(part in lowered for part in DENIED_PATH_PARTS)


def expected_state(payload: Mapping[str, Any]) -> str:
    evaluated = _parse_time(str(payload["evaluated_at"]))
    revoked = payload.get("revoked_at")
    if isinstance(revoked, str) and _parse_time(revoked) <= evaluated:
        return "REVOKED"
    expires = payload.get("expires_at")
    if isinstance(expires, str) and evaluated >= _parse_time(expires):
        return "EXPIRED"
    return "ACTIVE"


def expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    reasons: set[str] = set()
    state = expected_state(payload)
    if state == "REVOKED":
        reasons.add("LINK_REVOKED")
    elif state == "EXPIRED":
        reasons.add("LINK_EXPIRED")
    context = payload["context"]
    for key in ("decision_envelope_ref", "manifest_ref", "receipts_summary_ref"):
        value = context.get(key)
        if isinstance(value, str) and not _is_safe_ref(value):
            reasons.add("UNSAFE_CONTEXT_REF")
    return sorted(reasons)


def expected_outcome(reasons: Sequence[str]) -> str:
    return "DENY" if reasons else "ALLOW"


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        created = _parse_time(str(payload["created_at"]))
        evaluated = _parse_time(str(payload["evaluated_at"]))
        expires = _parse_time(str(payload["expires_at"])) if payload.get("expires_at") else None
        revoked = _parse_time(str(payload["revoked_at"])) if payload.get("revoked_at") else None
    except (TypeError, ValueError):
        return [Finding("TIME_PARSE_ERROR", "/")]

    if evaluated < created:
        findings.append(Finding("EVALUATED_BEFORE_CREATED", "/evaluated_at"))
    if expires is not None and expires <= created:
        findings.append(Finding("EXPIRY_NOT_AFTER_CREATED", "/expires_at"))
    if revoked is not None and revoked < created:
        findings.append(Finding("REVOCATION_BEFORE_CREATED", "/revoked_at"))

    state = expected_state(payload)
    if payload["state"] != state:
        findings.append(Finding("STATE_MISMATCH", "/state"))
    reasons = expected_reasons(payload)
    decision = payload["decision"]
    if decision["reasons"] != reasons:
        findings.append(Finding("DECISION_REASONS_MISMATCH", "/decision/reasons"))
    if decision["outcome"] != expected_outcome(reasons):
        findings.append(Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome"))
    if payload["spec_hash"] != canonical_spec_hash(payload):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(payload)
    if not findings:
        findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    payload, findings = _load_payload(path)
    if payload is None:
        return ValidationResult(tuple(sorted(findings)))
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a fixture-only ReviewShareLink record.")
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_file(args.path)
    output = {
        "ok": result.ok,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": "fixture-only-review-share-link",
        "authority": {
            "access_grant": False,
            "secret_persistence": False,
            "lifecycle_write": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
