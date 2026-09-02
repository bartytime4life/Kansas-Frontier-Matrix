#!/usr/bin/env python3
"""Validate proposed GeneratedRuntimeProofArtifact records without network access.

A passing result proves bounded schema shape and local lifecycle consistency only.
It does not authenticate reviewers, create evidence or policy authority, authorize
KFM lifecycle promotion, release, deployment, or publication.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/generated_runtime_proof_artifact.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/runtime/generated_runtime_proof_artifact"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "generated-runtime-proof-artifact-shape-and-local-lifecycle-only"
ZERO_DIGEST = "sha256:" + ("0" * 64)

ALLOWED_PREVIOUS_STATES: dict[str, set[str | None]] = {
    "EPHEMERAL": {None},
    "RETAINED": {"EPHEMERAL"},
    "REVIEWED": {"RETAINED", "STALE"},
    "PROMOTED_GOLDEN": {"REVIEWED"},
    "STALE": {"RETAINED", "REVIEWED", "PROMOTED_GOLDEN"},
    "INVALIDATED": {"RETAINED", "REVIEWED", "PROMOTED_GOLDEN", "STALE"},
    "DELETED": {"EPHEMERAL", "RETAINED", "REVIEWED", "STALE", "INVALIDATED"},
}


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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


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
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
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

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _non_null(value: Any) -> bool:
    return value is not None


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    profile = _mapping(candidate.get("profile"))
    content = _mapping(candidate.get("content"))
    lifecycle = _mapping(candidate.get("lifecycle"))
    provenance = _mapping(candidate.get("provenance"))
    review = _mapping(candidate.get("review"))
    promotion = _mapping(candidate.get("golden_promotion"))
    invalidation = _mapping(candidate.get("invalidation"))
    safety = _mapping(candidate.get("safety"))
    governance = _mapping(candidate.get("governance"))

    for field, value in (
        ("/profile/spec_hash", profile.get("spec_hash")),
        ("/content/digest", content.get("digest")),
    ):
        if value == ZERO_DIGEST:
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    digest = content.get("digest")
    artifact_ref = candidate.get("artifact_ref")
    if isinstance(digest, str) and isinstance(artifact_ref, str):
        if not artifact_ref.endswith("@" + digest):
            findings.append(
                Finding("ARTIFACT_REF_DIGEST_MISMATCH", "/artifact_ref")
            )

    canonical_arrays = (
        ("/lifecycle/reason_codes", _array(lifecycle.get("reason_codes"))),
        ("/provenance/input_refs", _array(provenance.get("input_refs"))),
        ("/review/review_record_refs", _array(review.get("review_record_refs"))),
        (
            "/golden_promotion/review_record_refs",
            _array(promotion.get("review_record_refs")),
        ),
        (
            "/invalidation/reason_codes",
            _array(invalidation.get("reason_codes")),
        ),
    )
    for field, values in canonical_arrays:
        if not _sorted_unique_strings(values):
            findings.append(Finding("REFS_OR_REASONS_NOT_CANONICAL", field))

    generated_at = _parse_time(provenance.get("generated_at"))
    transitioned_at = _parse_time(lifecycle.get("transitioned_at"))
    lifecycle_expires_at = _parse_time(lifecycle.get("expires_at"))
    promotion_decided_at = _parse_time(promotion.get("decided_at"))
    promotion_expires_at = _parse_time(promotion.get("expires_at"))

    if generated_at and transitioned_at and generated_at > transitioned_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/provenance/generated_at"))
    if transitioned_at and lifecycle_expires_at and transitioned_at > lifecycle_expires_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/lifecycle/expires_at"))
    if generated_at and promotion_decided_at and generated_at > promotion_decided_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/golden_promotion/decided_at"))
    if promotion_decided_at and promotion_expires_at and promotion_decided_at > promotion_expires_at:
        findings.append(Finding("TIMING_ORDER_INVALID", "/golden_promotion/expires_at"))

    state = lifecycle.get("state")
    previous_state = lifecycle.get("previous_state")
    if isinstance(state, str) and state in ALLOWED_PREVIOUS_STATES:
        if previous_state not in ALLOWED_PREVIOUS_STATES[state]:
            findings.append(
                Finding("LIFECYCLE_TRANSITION_INVALID", "/lifecycle/previous_state")
            )

    prior_record_ref = lifecycle.get("prior_record_ref")
    if state == "EPHEMERAL":
        if previous_state is not None or prior_record_ref is not None or lifecycle.get("expires_at") is None:
            findings.append(
                Finding("LIFECYCLE_STATE_REQUIREMENT_MISMATCH", "/lifecycle")
            )
    elif isinstance(state, str) and state in ALLOWED_PREVIOUS_STATES:
        if prior_record_ref is None:
            findings.append(
                Finding("LIFECYCLE_STATE_REQUIREMENT_MISMATCH", "/lifecycle/prior_record_ref")
            )

    review_state = review.get("state")
    review_refs = _array(review.get("review_record_refs"))
    if review_state in {"APPROVED", "CHANGES_REQUESTED", "REJECTED"} and not review_refs:
        findings.append(Finding("REVIEW_SUPPORT_MISSING", "/review/review_record_refs"))
    if state == "REVIEWED" and review_state not in {
        "APPROVED",
        "CHANGES_REQUESTED",
        "REJECTED",
    }:
        findings.append(Finding("REVIEW_SUPPORT_MISSING", "/review/state"))

    promotion_decision = promotion.get("decision")
    if state == "PROMOTED_GOLDEN":
        required_promotion_fields = (
            promotion.get("decision_id"),
            promotion.get("decided_at"),
            promotion.get("artifact_digest"),
            promotion.get("expires_at"),
        )
        promotion_review_refs = _array(promotion.get("review_record_refs"))
        if (
            review_state != "APPROVED"
            or not review_refs
            or not promotion_review_refs
            or promotion_decision != "PROMOTE_GOLDEN"
            or not all(_non_null(value) for value in required_promotion_fields)
        ):
            findings.append(
                Finding("GOLDEN_PROMOTION_REVIEW_MISSING", "/golden_promotion")
            )
        if promotion.get("artifact_digest") != digest:
            findings.append(
                Finding(
                    "GOLDEN_PROMOTION_BINDING_MISMATCH",
                    "/golden_promotion/artifact_digest",
                )
            )
        if promotion.get("expires_at") != lifecycle.get("expires_at"):
            findings.append(
                Finding(
                    "GOLDEN_PROMOTION_BINDING_MISMATCH",
                    "/golden_promotion/expires_at",
                )
            )
        unsafe = (
            safety.get("data_class") != "SYNTHETIC_PUBLIC_SAFE"
            or safety.get("contains_secrets") is not False
            or safety.get("contains_personal_data") is not False
            or safety.get("contains_precise_sensitive_geometry") is not False
            or safety.get("public_use_allowed") is not False
        )
        if unsafe:
            findings.append(
                Finding("GOLDEN_PROMOTION_SAFETY_DENIED", "/safety")
            )
    elif promotion_decision == "PROMOTE_GOLDEN":
        findings.append(
            Finding("GOLDEN_PROMOTION_STATE_MISMATCH", "/golden_promotion/decision")
        )

    invalidation_reasons = _array(invalidation.get("reason_codes"))
    if state in {"STALE", "INVALIDATED"} and not invalidation_reasons:
        findings.append(
            Finding("INVALIDATION_SUPPORT_MISSING", "/invalidation/reason_codes")
        )
    if state == "INVALIDATED" and not (
        invalidation.get("correction_ref") or invalidation.get("superseded_by_ref")
    ):
        findings.append(
            Finding("INVALIDATION_SUPPORT_MISSING", "/invalidation")
        )
    if state == "DELETED" and not invalidation.get("deletion_receipt_ref"):
        findings.append(
            Finding("DELETION_RECEIPT_MISSING", "/invalidation/deletion_receipt_ref")
        )

    governance_flags = (
        "authority_created",
        "evidence_closure_claimed",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
    )
    if any(governance.get(field) is not False for field in governance_flags) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_artifact(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
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
        return 1

    passed = True
    for path in valid_files:
        result = validate_artifact(path)
        print(_serialize(path, result))
        passed = passed and result.ok

    for path in invalid_files:
        result = validate_artifact(path)
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
        description="Validate proposed GeneratedRuntimeProofArtifact records."
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
        result = validate_artifact(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
