"""Validate fixture-only after-image reconstruction record candidates.

The validator checks closed shape, deterministic content identity, temporal
ordering, reference-only after-image modes, reconstruction support, retention,
minimization, sensitivity, and review declarations. It never stores a payload,
writes a tracking log, reconstructs state, applies a correction, decides
policy or review, or grants release or publication authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/after_image_reconstruction_record.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/after_image_reconstruction_record/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "AFTER_IMAGE_DIGEST_ONLY",
    "AFTER_IMAGE_WITHHELD",
    "MINIMIZATION_UNRESOLVED",
    "RETENTION_POLICY_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SENSITIVITY_UNRESOLVED",
    "TRACKING_LOG_UNRESOLVED",
}
REFERENCE_ARRAY_FIELDS = (
    "run_receipt_refs",
    "correction_notice_refs",
    "release_manifest_refs",
    "rollback_refs",
)
USE_CASE_SUPPORT = {
    "AUDIT": "run_receipt_refs",
    "CORRECTION": "correction_notice_refs",
    "DISPUTED_RELEASE": "release_manifest_refs",
    "ROLLBACK_ANALYSIS": "rollback_refs",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


def _utc_datetime(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _tracking_findings(binding: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = binding.get("state")
    ref = binding.get("ref")
    digest = binding.get("digest")
    if state == "RESOLVED":
        if ref is None or digest is None:
            findings.add(Finding("TRACKING_LOG_BINDING_REQUIRED", "/tracking_log_binding"))
    else:
        if ref is not None or digest is not None:
            findings.add(Finding("TRACKING_LOG_BINDING_PROHIBITED", "/tracking_log_binding"))
        findings.add(Finding("TRACKING_LOG_UNRESOLVED", "/tracking_log_binding/state"))
    return findings


def _after_image_findings(after_image: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    mode = after_image.get("mode")
    ref = after_image.get("ref")
    digest = after_image.get("digest")
    schema_ref = after_image.get("schema_ref")
    schema_digest = after_image.get("schema_digest")
    reason_ref = after_image.get("withholding_reason_ref")
    if mode in {"EXTERNAL_REFERENCE", "MINIMIZED_REFERENCE"}:
        coherent = all(value is not None for value in (ref, digest, schema_ref, schema_digest)) and reason_ref is None
    elif mode == "DIGEST_ONLY":
        coherent = ref is None and digest is not None and schema_ref is None and schema_digest is None and reason_ref is None
        findings.add(Finding("AFTER_IMAGE_DIGEST_ONLY", "/after_image/mode"))
    else:
        coherent = all(value is None for value in (ref, digest, schema_ref, schema_digest)) and reason_ref is not None
        findings.add(Finding("AFTER_IMAGE_WITHHELD", "/after_image/mode"))
        if reason_ref is None:
            findings.add(Finding("WITHHOLDING_REASON_REQUIRED", "/after_image/withholding_reason_ref"))
    if not coherent:
        findings.add(Finding("AFTER_IMAGE_BINDING_INCOHERENT", "/after_image"))
    return findings


def _reconstruction_findings(scope: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    use_cases = scope.get("use_cases")
    if not _canonical_strings(use_cases):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/reconstruction_scope/use_cases"))
    assert isinstance(use_cases, list)
    for field in REFERENCE_ARRAY_FIELDS:
        refs = scope.get(field)
        if not _canonical_strings(refs):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/reconstruction_scope/{field}"))
        assert isinstance(refs, list)
    for use_case in use_cases:
        field = USE_CASE_SUPPORT[use_case]
        if not scope[field]:
            findings.add(Finding("RECONSTRUCTION_SUPPORT_REQUIRED", f"/reconstruction_scope/{field}"))
    if "DISPUTED_RELEASE" in use_cases and scope.get("as_of_snapshot_ref") is None:
        findings.add(Finding("AS_OF_SNAPSHOT_REQUIRED", "/reconstruction_scope/as_of_snapshot_ref"))
    return findings


def _retention_findings(
    retention: Mapping[str, object], after_mode: object, recorded_at: datetime | None
) -> set[Finding]:
    findings: set[Finding] = set()
    binding = retention["policy_binding"]
    assert isinstance(binding, Mapping)
    if binding.get("state") == "RESOLVED":
        if binding.get("ref") is None or binding.get("digest") is None:
            findings.add(Finding("RETENTION_POLICY_BINDING_REQUIRED", "/retention/policy_binding"))
    else:
        if binding.get("ref") is not None or binding.get("digest") is not None:
            findings.add(Finding("RETENTION_POLICY_BINDING_PROHIBITED", "/retention/policy_binding"))
        findings.add(Finding("RETENTION_POLICY_UNRESOLVED", "/retention/policy_binding/state"))

    minimization = retention.get("minimization_state")
    sensitivity = retention.get("sensitivity_state")
    if minimization == "UNRESOLVED":
        findings.add(Finding("MINIMIZATION_UNRESOLVED", "/retention/minimization_state"))
    if sensitivity == "UNRESOLVED":
        findings.add(Finding("SENSITIVITY_UNRESOLVED", "/retention/sensitivity_state"))
    if after_mode == "MINIMIZED_REFERENCE" and minimization != "APPLIED":
        findings.add(Finding("MINIMIZATION_REQUIRED", "/retention/minimization_state"))

    retention_class = retention.get("class")
    expires_at = retention.get("expires_at")
    expiry = _utc_datetime(expires_at) if expires_at is not None else None
    if expires_at is not None and expiry is None:
        findings.add(Finding("RETENTION_EXPIRY_NOT_UTC", "/retention/expires_at"))
    if retention_class in {"TRANSIENT", "BOUNDED"}:
        if expires_at is None:
            findings.add(Finding("RETENTION_EXPIRY_REQUIRED", "/retention/expires_at"))
        elif expiry is not None and recorded_at is not None and expiry <= recorded_at:
            findings.add(Finding("RETENTION_EXPIRY_NOT_FUTURE", "/retention/expires_at"))
    elif expires_at is not None:
        findings.add(Finding("RETENTION_EXPIRY_PROHIBITED", "/retention/expires_at"))

    if (after_mode == "WITHHELD") != (retention_class == "WITHHELD"):
        findings.add(Finding("RETENTION_CLASS_INCOHERENT", "/retention/class"))
    return findings


def _review_findings(review: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    refs = review.get("record_refs")
    if not _canonical_strings(refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/review/record_refs"))
    assert isinstance(refs, list)
    state = review.get("state")
    if state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif state == "COMPLETE_FOR_DECLARED_SCOPE":
        if not refs:
            findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))
        if review.get("rationale_summary") is None:
            findings.add(Finding("RATIONALE_SUMMARY_REQUIRED", "/review/rationale_summary"))
    return findings


def _time_findings(candidate: Mapping[str, object]) -> tuple[set[Finding], datetime | None]:
    findings: set[Finding] = set()
    transition = candidate["transition"]
    assert isinstance(transition, Mapping)
    recorded = _utc_datetime(candidate.get("recorded_at"))
    transaction = _utc_datetime(transition.get("transaction_time"))
    valid_start = _utc_datetime(transition.get("valid_time_start"))
    valid_end_raw = transition.get("valid_time_end")
    valid_end = _utc_datetime(valid_end_raw) if valid_end_raw is not None else None
    if recorded is None:
        findings.add(Finding("RECORDED_AT_NOT_UTC", "/recorded_at"))
    if transaction is None:
        findings.add(Finding("TRANSACTION_TIME_NOT_UTC", "/transition/transaction_time"))
    if valid_start is None or (valid_end_raw is not None and valid_end is None):
        findings.add(Finding("VALID_TIME_NOT_UTC", "/transition"))
    if recorded is not None and transaction is not None and transaction > recorded:
        findings.add(Finding("TRANSACTION_TIME_AFTER_RECORDED_AT", "/transition/transaction_time"))
    if valid_start is not None and valid_end is not None and valid_start >= valid_end:
        findings.add(Finding("VALID_TIME_ORDER_INVALID", "/transition/valid_time_end"))
    return findings, recorded


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings, recorded = _time_findings(candidate)
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    tracking = candidate["tracking_log_binding"]
    after_image = candidate["after_image"]
    scope = candidate["reconstruction_scope"]
    retention = candidate["retention"]
    review = candidate["review"]
    assert all(isinstance(value, Mapping) for value in (tracking, after_image, scope, retention, review))
    findings.update(_tracking_findings(tracking))
    findings.update(_after_image_findings(after_image))
    findings.update(_reconstruction_findings(scope))
    findings.update(_retention_findings(retention, after_image.get("mode"), recorded))
    findings.update(_review_findings(review))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})},
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only after-image reconstruction records."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
