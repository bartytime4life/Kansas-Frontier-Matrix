#!/usr/bin/env python3
"""Validate fixture-only map manifest integrity assessments."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/map_manifest_integrity_assessment.schema.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
ERROR_REASONS = frozenset({"ASSET_VERIFY_ERROR", "SIGNATURE_VERIFY_ERROR"})
DENY_REASONS = frozenset({
    "ASSET_HASH_MISMATCH", "ASSET_SIZE_MISMATCH", "EVIDENCE_BUNDLE_DENIED",
    "EXPECTED_SPEC_HASH_MISMATCH", "MANIFEST_SPEC_HASH_MISMATCH", "PROOF_DENIED",
    "SELECTED_ASSET_MISSING", "SIGNATURE_FAILED", "SIGNER_IDENTITY_MISMATCH",
})

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
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file(): return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES: return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=_reject_nonfinite)
    except UnicodeError: return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except OSError: return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
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
    if truncated: findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical_hash(value: Mapping[str, Any], omitted_key: str) -> str:
    body = {key: item for key, item in value.items() if key != omitted_key}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def canonical_manifest_spec_hash(manifest: Mapping[str, Any]) -> str:
    return _canonical_hash(manifest, "spec_hash")


def canonical_spec_hash(payload: Mapping[str, Any]) -> str:
    return _canonical_hash(payload, "spec_hash")


def _asset_by_id(payload: Mapping[str, Any]) -> Mapping[str, Any] | None:
    selected = payload.get("selected_asset_id")
    if not isinstance(selected, str): return None
    for asset in payload["manifest"]["assets"]:
        if asset["asset_id"] == selected: return asset
    return None


def expected_reasons(payload: Mapping[str, Any]) -> list[str]:
    reasons: set[str] = set()
    manifest = payload["manifest"]
    if manifest["spec_hash"] != canonical_manifest_spec_hash(manifest):
        reasons.add("MANIFEST_SPEC_HASH_MISMATCH")
    if payload["expected_manifest_spec_hash"] != manifest["spec_hash"]:
        reasons.add("EXPECTED_SPEC_HASH_MISMATCH")

    signature = payload["signature_verdict"]
    state = signature["state"]
    if state == "FAILED": reasons.add("SIGNATURE_FAILED")
    elif state in {"UNVERIFIED", "NOT_CONFIGURED"}: reasons.add("SIGNATURE_UNVERIFIED")
    elif state == "ERROR": reasons.add("SIGNATURE_VERIFY_ERROR")
    elif state == "VERIFIED" and signature.get("signer_identity") != manifest["publisher"]["identity"]:
        reasons.add("SIGNER_IDENTITY_MISMATCH")

    evidence = payload["evidence_resolution"]
    bundle_state = evidence["bundle_state"]
    proof_state = evidence["proof_state"]
    if not manifest.get("bundle_ref"): reasons.add("EVIDENCE_BUNDLE_MISSING")
    if bundle_state == "MISSING": reasons.add("EVIDENCE_BUNDLE_MISSING")
    elif bundle_state == "UNRESOLVED": reasons.add("EVIDENCE_BUNDLE_UNRESOLVED")
    elif bundle_state == "DENIED": reasons.add("EVIDENCE_BUNDLE_DENIED")
    if not manifest.get("proof_ref"): reasons.add("PROOF_REF_MISSING")
    if proof_state == "MISSING": reasons.add("PROOF_REF_MISSING")
    elif proof_state == "UNRESOLVED": reasons.add("PROOF_UNRESOLVED")
    elif proof_state == "DENIED": reasons.add("PROOF_DENIED")

    selected = _asset_by_id(payload)
    verification = payload["asset_verification"]
    if payload["deep_verify_required"] and selected is None:
        reasons.add("SELECTED_ASSET_MISSING")
    if verification["state"] == "ERROR":
        reasons.add("ASSET_VERIFY_ERROR")
    elif verification["state"] == "SKIPPED" and payload["deep_verify_required"]:
        reasons.add("ASSET_DEEP_VERIFY_SKIPPED")
    elif verification["state"] in {"VERIFIED", "FAILED"}:
        if selected is None:
            reasons.add("SELECTED_ASSET_MISSING")
        else:
            if verification.get("observed_sha256") != selected["sha256"]:
                reasons.add("ASSET_HASH_MISMATCH")
            if verification.get("observed_bytes") != selected["bytes"]:
                reasons.add("ASSET_SIZE_MISMATCH")
    return sorted(reasons)


def expected_outcome(reasons: Sequence[str]) -> str:
    if any(reason in ERROR_REASONS for reason in reasons): return "ERROR"
    if any(reason in DENY_REASONS for reason in reasons): return "DENY"
    if reasons: return "ABSTAIN"
    return "ANSWER"


def _semantic_findings(payload: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    assets = payload["manifest"]["assets"]
    asset_ids = [item["asset_id"] for item in assets]
    if asset_ids != sorted(asset_ids): findings.append(Finding("ASSETS_NOT_CANONICAL", "/manifest/assets"))
    if len(asset_ids) != len(set(asset_ids)): findings.append(Finding("ASSET_ID_DUPLICATE", "/manifest/assets"))

    signature = payload["signature_verdict"]
    if signature["state"] == "VERIFIED":
        if not signature.get("signer_identity"): findings.append(Finding("SIGNER_IDENTITY_REQUIRED", "/signature_verdict/signer_identity"))
        if not signature.get("verdict_ref"): findings.append(Finding("SIGNATURE_VERDICT_REF_REQUIRED", "/signature_verdict/verdict_ref"))
    elif signature.get("signer_identity") or signature.get("verdict_ref"):
        findings.append(Finding("SIGNATURE_DETAILS_UNEXPECTED", "/signature_verdict"))

    verification = payload["asset_verification"]
    if verification["state"] in {"VERIFIED", "FAILED"}:
        if not verification.get("observed_sha256"): findings.append(Finding("OBSERVED_HASH_REQUIRED", "/asset_verification/observed_sha256"))
        if "observed_bytes" not in verification: findings.append(Finding("OBSERVED_BYTES_REQUIRED", "/asset_verification/observed_bytes"))
    elif verification.get("observed_sha256") or "observed_bytes" in verification:
        findings.append(Finding("OBSERVED_ASSET_DETAILS_UNEXPECTED", "/asset_verification"))

    reasons = expected_reasons(payload)
    decision = payload["decision"]
    if decision["reasons"] != reasons: findings.append(Finding("DECISION_REASONS_MISMATCH", "/decision/reasons"))
    if decision["outcome"] != expected_outcome(reasons): findings.append(Finding("DECISION_OUTCOME_MISMATCH", "/decision/outcome"))
    if payload["spec_hash"] != canonical_spec_hash(payload): findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    return findings


def validate_payload(payload: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(payload)
    if not findings: findings.extend(_semantic_findings(payload))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_file(path: Path) -> ValidationResult:
    payload, findings = _load_payload(path)
    if payload is None: return ValidationResult(tuple(sorted(findings)))
    return validate_payload(payload)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a fixture-only map manifest integrity assessment.")
    parser.add_argument("path", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv); result = validate_file(args.path)
    output={"ok":result.ok,"findings":[{"code":f.code,"path":f.path} for f in result.findings],"scope":"fixture-only-map-manifest-integrity-assessment","authority":{"network_fetch":False,"crypto_verification":False,"promotion":False,"release":False,"publication":False}}
    print(json.dumps(output,sort_keys=True,separators=(",",":")))
    return 0 if result.ok else 1

if __name__ == "__main__": sys.exit(main())
