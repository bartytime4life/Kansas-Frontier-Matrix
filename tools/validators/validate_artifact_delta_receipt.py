#!/usr/bin/env python3
"""Validate proposed KFM ArtifactDeltaReceiptCandidate records without network access.

A passing result proves bounded shape and local consistency only. It does not verify
cryptography or OCI state, evaluate policy, complete review, authorize promotion or
release, execute rollback, or publish.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/receipts/artifact_delta_receipt.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/receipts/artifact_delta_receipt"
MAX_FILE_BYTES = 1_048_576
SCOPE = "artifact-delta-receipt-shape-and-local-consistency-only"
ZERO_DIGEST = "sha256:" + ("0" * 64)


class DuplicateKeyError(ValueError):
    pass


class UnsupportedFloatError(ValueError):
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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise NonFiniteNumberError(value)


def _reject_float(value: str) -> None:
    raise UnsupportedFloatError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if path.is_symlink() or not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_constant,
                parse_float=_reject_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except UnsupportedFloatError:
        return None, [Finding("JSON_FLOAT_UNSUPPORTED", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: dict[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in validator.iter_errors(candidate)
    ]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def canonical_payload_bytes(candidate: dict[str, Any]) -> bytes:
    payload = copy.deepcopy(candidate)
    canonicalization = payload.get("canonicalization")
    if isinstance(canonicalization, dict):
        canonicalization.pop("payload_digest", None)
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def expected_payload_digest(candidate: dict[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(canonical_payload_bytes(candidate)).hexdigest()


def _semantic_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    before = _mapping(candidate.get("before"))
    after = _mapping(candidate.get("after"))
    decision = _mapping(candidate.get("decision"))
    review = _mapping(candidate.get("review"))
    attestation = _mapping(candidate.get("attestation"))
    canonicalization = _mapping(candidate.get("canonicalization"))
    governance = _mapping(candidate.get("governance"))

    for prefix, snapshot in (("before", before), ("after", after)):
        for field in ("spec_hash", "artifact_digest"):
            if snapshot.get(field) == ZERO_DIGEST:
                findings.append(Finding("DIGEST_PLACEHOLDER", f"/{prefix}/{field}"))

    before_identity = (
        before.get("artifact_ref"),
        before.get("spec_hash"),
        before.get("artifact_digest"),
    )
    after_identity = (
        after.get("artifact_ref"),
        after.get("spec_hash"),
        after.get("artifact_digest"),
    )
    if all(item is not None for item in before_identity + after_identity):
        if before_identity == after_identity:
            findings.append(Finding("DELTA_NO_EFFECT", "/after"))

    if before.get("run_receipt_ref") and before.get("run_receipt_ref") == after.get("run_receipt_ref"):
        findings.append(Finding("RUN_RECEIPT_REUSED", "/after/run_receipt_ref"))

    outcome = decision.get("outcome")
    if outcome == "APPROVE":
        if (
            review.get("state") != "APPROVED"
            or not isinstance(review.get("review_record_ref"), str)
            or not isinstance(review.get("actor_ref"), str)
            or not isinstance(review.get("steward_kid"), str)
        ):
            findings.append(Finding("APPROVAL_REQUIRES_APPROVED_REVIEW", "/review"))
        if (
            attestation.get("verification_state") != "VERIFIED"
            or attestation.get("format") == "NONE"
            or not isinstance(attestation.get("attestation_ref"), str)
            or not isinstance(attestation.get("signer_kid"), str)
            or not isinstance(attestation.get("oci_referrer_uri"), str)
        ):
            findings.append(
                Finding("APPROVAL_REQUIRES_VERIFIED_ATTESTATION", "/attestation")
            )
        if not isinstance(candidate.get("rollback_target_ref"), str):
            findings.append(
                Finding("APPROVAL_REQUIRES_ROLLBACK_TARGET", "/rollback_target_ref")
            )

    change_kind = candidate.get("change_kind")
    if change_kind == "ROLLBACK" and not isinstance(candidate.get("rollback_target_ref"), str):
        findings.append(Finding("ROLLBACK_TARGET_REQUIRED", "/rollback_target_ref"))
    if change_kind == "CORRECTION" and not isinstance(candidate.get("correction_notice_ref"), str):
        findings.append(Finding("CORRECTION_NOTICE_REQUIRED", "/correction_notice_ref"))

    declared = canonicalization.get("payload_digest")
    if isinstance(declared, str) and declared != expected_payload_digest(candidate):
        findings.append(Finding("PAYLOAD_DIGEST_MISMATCH", "/canonicalization/payload_digest"))

    expected_governance = {
        "candidate_only": True,
        "cryptographic_verification_performed": False,
        "policy_authority_created": False,
        "review_authority_created": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "publication_authorized": False,
        "public_use_allowed": False,
    }
    if governance and governance != expected_governance:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_candidate(candidate: dict[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_receipt(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    result = validate_candidate(candidate)
    return ValidationResult(tuple(sorted(set(findings + list(result.findings)))))


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_files(directory: Path, prefix: str) -> list[Path]:
    return sorted(directory.glob(f"{prefix}*.json"), key=lambda path: path.as_posix())


def _expected_manifest(directory: Path) -> dict[str, list[str]]:
    try:
        value = json.loads(
            (directory / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = _fixture_files(FIXTURE_ROOT / "valid", "valid_")
    invalid_files = _fixture_files(FIXTURE_ROOT / "invalid", "invalid_")
    manifest = _expected_manifest(FIXTURE_ROOT / "invalid")
    if not valid_files or not invalid_files:
        return 2

    passed = True
    for path in valid_files:
        result = validate_receipt(path)
        print(_serialize(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_receipt(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual": actual,
                        "expected": expected,
                        "file": path.as_posix(),
                        "outcome": "FIXTURE_POLARITY_ERROR",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM ArtifactDeltaReceiptCandidate records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_receipt(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
