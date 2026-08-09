"""Validate the fixture-only ReleaseBoundRunReceipt proof profile.

A passing result proves bounded schema, deterministic identity, and cross-reference
coherence only. It does not resolve evidence, execute policy, authenticate review,
verify signatures, promote, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/release_bound_run_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/release_bound_run_receipt/cases.json"
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
if HASHING_SRC.is_dir():
    sys.path.insert(0, str(HASHING_SRC))

try:
    from hashing import compute_spec_hash as _shared_compute_spec_hash
except Exception:  # pragma: no cover - local fallback for isolated fixture replay
    _shared_compute_spec_hash = None


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _fallback_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = dict(candidate)
    subject.pop("profile_spec_hash", None)
    if _shared_compute_spec_hash is not None:
        return _shared_compute_spec_hash(subject)
    return _fallback_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (list(error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    expected = candidate.get("profile_spec_hash")
    if isinstance(expected, str) and compute_profile_hash(candidate) != expected:
        findings.append(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))

    started = _parse_time(candidate.get("started_at"))
    finished = _parse_time(candidate.get("finished_at"))
    observed = _parse_time(candidate.get("observed_at"))
    if started and finished and finished < started:
        findings.append(Finding("TIMESTAMP_ORDER_INVALID", "/finished_at"))
    if finished and observed and observed < finished:
        findings.append(Finding("OBSERVATION_PRECEDES_FINISH", "/observed_at"))

    binding = candidate.get("runtime_receipt_binding")
    input_artifacts = candidate.get("input_artifacts")
    output_artifacts = candidate.get("output_artifacts")
    if isinstance(binding, dict) and isinstance(input_artifacts, list):
        declared = binding.get("inputs")
        materialized = [item.get("uri") for item in input_artifacts if isinstance(item, dict)]
        if declared != sorted(materialized) or materialized != sorted(set(materialized)):
            findings.append(Finding("INPUT_BINDING_MISMATCH", "/runtime_receipt_binding/inputs"))
    if isinstance(binding, dict) and isinstance(output_artifacts, list):
        declared = binding.get("outputs")
        materialized = [item.get("uri") for item in output_artifacts if isinstance(item, dict)]
        if declared != sorted(materialized) or materialized != sorted(set(materialized)):
            findings.append(Finding("OUTPUT_BINDING_MISMATCH", "/runtime_receipt_binding/outputs"))
        if binding.get("outcome") != "SUCCESS":
            findings.append(Finding("RUNTIME_RECEIPT_NOT_SUCCESS", "/runtime_receipt_binding/outcome"))

    attestations = candidate.get("attestations")
    attestation_states = [item.get("verification_status") for item in attestations if isinstance(item, dict)] if isinstance(attestations, list) else []
    if "ERROR" in attestation_states:
        findings.append(Finding("ATTESTATION_ERROR", "/attestations"))
    if "FAILED" in attestation_states:
        findings.append(Finding("ATTESTATION_FAILED", "/attestations"))
    if "UNVERIFIED" in attestation_states:
        findings.append(Finding("ATTESTATION_UNVERIFIED", "/attestations"))

    release = candidate.get("release_binding")
    if isinstance(release, dict):
        status_codes = {
            ("evidence_status", "UNRESOLVED"): "EVIDENCE_UNRESOLVED",
            ("evidence_status", "DENIED"): "EVIDENCE_DENIED",
            ("evidence_status", "ERROR"): "EVIDENCE_ERROR",
            ("policy_status", "HOLD"): "POLICY_HOLD",
            ("policy_status", "DENY"): "POLICY_DENIED",
            ("policy_status", "ERROR"): "POLICY_ERROR",
            ("review_status", "PENDING"): "REVIEW_PENDING",
            ("review_status", "CHANGES_REQUESTED"): "REVIEW_CHANGES_REQUESTED",
            ("review_status", "REJECTED"): "REVIEW_REJECTED",
            ("review_status", "ERROR"): "REVIEW_ERROR",
            ("signature_status", "PENDING"): "SIGNATURE_PENDING",
            ("signature_status", "FAILED"): "SIGNATURE_FAILED",
            ("signature_status", "ERROR"): "SIGNATURE_ERROR",
            ("correction_status", "MISSING"): "CORRECTION_PATH_MISSING",
            ("correction_status", "ERROR"): "CORRECTION_ERROR",
            ("rollback_status", "MISSING"): "ROLLBACK_MISSING",
            ("rollback_status", "ERROR"): "ROLLBACK_ERROR",
        }
        for (field, state), code in status_codes.items():
            if release.get(field) == state:
                findings.append(Finding(code, f"/release_binding/{field}"))
        signature_status = release.get("signature_status")
        if signature_status == "VERIFIED" and any(state != "VERIFIED" for state in attestation_states):
            findings.append(Finding("ATTESTATION_STATUS_INCONSISTENT", "/release_binding/signature_status"))

    authority = candidate.get("authority_claims")
    if isinstance(authority, dict) and any(value is not False for value in authority.values()):
        findings.append(Finding("AUTHORITY_OVERCLAIM_DENIED", "/authority_claims"))
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(schema_findings)))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    error_codes = {code for code in codes if code.endswith("_ERROR") or code in {"ATTESTATION_ERROR", "REVIEW_ERROR", "SIGNATURE_ERROR", "POLICY_ERROR", "EVIDENCE_ERROR", "CORRECTION_ERROR", "ROLLBACK_ERROR"}}
    deny_codes = {code for code in codes if code.endswith("_DENIED") or code.endswith("_FAILED") or code.endswith("_MISSING") or code.endswith("_MISMATCH") or code in {"TIMESTAMP_ORDER_INVALID", "OBSERVATION_PRECEDES_FINISH", "RUNTIME_RECEIPT_NOT_SUCCESS", "ATTESTATION_STATUS_INCONSISTENT", "AUTHORITY_OVERCLAIM_DENIED"}}
    abstain_codes = {code for code in codes if code.endswith("_PENDING") or code.endswith("_UNRESOLVED") or code in {"ATTESTATION_UNVERIFIED", "POLICY_HOLD", "REVIEW_CHANGES_REQUESTED"}}
    if error_codes:
        outcome = "ERROR"
    elif deny_codes:
        outcome = "DENY"
    elif abstain_codes:
        outcome = "ABSTAIN"
    else:
        outcome = "PASS"
    return ValidationResult(outcome, tuple(sorted(findings)))




def _merge_patch(base: object, patch: object) -> object:
    """Apply a bounded RFC 7396-style merge patch to synthetic fixture data."""
    if not isinstance(patch, dict):
        return patch
    target = dict(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> object:
    return _merge_patch(manifest["base_candidate"], entry.get("patch", {}))

def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate = json.loads(args.input.read_text(encoding="utf-8"))
    result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
