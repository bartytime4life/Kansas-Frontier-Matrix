#!/usr/bin/env python3
"""Validate fixture-only Cosign attestation-verification plans.

A passing result proves only that a proposed invocation is internally consistent,
uses a security-baselined Cosign version, binds explicit subject/predicate/bundle
inputs, and preserves KFM non-authority flags. It does not execute Cosign, verify
cryptography, resolve evidence, evaluate policy, authenticate review, promote,
release, deploy, publish, or permit public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/release/cosign_attestation_verification_plan.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/release/cosign_attestation_verification_plan"
)
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "cosign-attestation-verification-plan-preflight-only"
EXPECTED_ADVISORIES = ["CVE-2026-39395", "GHSA-w6c6-c85g-mmv6"]
EXPECTED_OUTCOMES = ["DENIED", "ERROR", "VERIFIED"]
ZERO_DIGEST = "sha256:" + ("0" * 64)
SEMVER = re.compile(r"^(?P<major>[0-9]+)\.(?P<minor>[0-9]+)\.(?P<patch>[0-9]+)$")


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
            raise DuplicateKeyError
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


def _canonical_hash(candidate: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(candidate))
    payload.pop("spec_hash", None)
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _version_tuple(value: Any) -> tuple[int, int, int] | None:
    if not isinstance(value, str):
        return None
    match = SEMVER.fullmatch(value)
    if match is None:
        return None
    return tuple(int(match.group(name)) for name in ("major", "minor", "patch"))


def _canonical_array(values: Any) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    baseline = _mapping(candidate.get("security_baseline"))
    tool = _mapping(candidate.get("tool"))
    subject = _mapping(candidate.get("subject"))
    predicate = _mapping(candidate.get("predicate"))
    bundle = _mapping(candidate.get("bundle"))
    trust = _mapping(candidate.get("trust"))
    invocation = _mapping(candidate.get("invocation"))
    expected_runtime = _mapping(candidate.get("expected_runtime"))
    governance = _mapping(candidate.get("governance"))

    advisory_ids = baseline.get("advisory_ids")
    if advisory_ids != EXPECTED_ADVISORIES or not _canonical_array(advisory_ids):
        findings.append(Finding("SECURITY_BASELINE_MISMATCH", "/security_baseline/advisory_ids"))
    if baseline.get("minimum_v2") != "2.6.3" or baseline.get("minimum_v3") != "3.0.6":
        findings.append(Finding("SECURITY_BASELINE_MISMATCH", "/security_baseline"))
    if baseline.get("strict_claim_validation_required") is not True:
        findings.append(Finding("CLAIM_VALIDATION_DISABLED", "/security_baseline/strict_claim_validation_required"))

    version = _version_tuple(tool.get("version"))
    if version is None:
        findings.append(Finding("COSIGN_VERSION_INVALID", "/tool/version"))
    elif version[0] == 2:
        if version < (2, 6, 3):
            findings.append(Finding("COSIGN_VERSION_VULNERABLE", "/tool/version"))
    elif version[0] == 3:
        if version < (3, 0, 6):
            findings.append(Finding("COSIGN_VERSION_VULNERABLE", "/tool/version"))
    else:
        findings.append(Finding("COSIGN_VERSION_TRACK_UNSUPPORTED", "/tool/version"))

    for field, value in (
        ("/tool/binary_digest", tool.get("binary_digest")),
        ("/subject/digest", subject.get("digest")),
        ("/bundle/digest", bundle.get("digest")),
    ):
        if value == ZERO_DIGEST:
            findings.append(Finding("DIGEST_PLACEHOLDER_DENIED", field))

    subject_digest = subject.get("digest")
    artifact_ref = subject.get("artifact_ref")
    plan_id = candidate.get("plan_id")
    if isinstance(subject_digest, str) and isinstance(artifact_ref, str):
        if not artifact_ref.endswith("@" + subject_digest):
            findings.append(Finding("SUBJECT_BINDING_MISMATCH", "/subject/artifact_ref"))
        expected_plan_id = "cosign-attestation-plan:" + subject_digest.removeprefix("sha256:")[:24]
        if plan_id != expected_plan_id:
            findings.append(Finding("PLAN_ID_MISMATCH", "/plan_id"))

    if invocation.get("command") != "verify-blob-attestation":
        findings.append(Finding("COMMAND_UNSUPPORTED", "/invocation/command"))
    if predicate.get("check_claims") is not True:
        findings.append(Finding("CLAIM_VALIDATION_DISABLED", "/predicate/check_claims"))

    if bundle.get("subject_digest") != subject_digest:
        findings.append(Finding("SUBJECT_BINDING_MISMATCH", "/bundle/subject_digest"))
    if invocation.get("subject_digest_argument") != subject_digest:
        findings.append(Finding("SUBJECT_BINDING_MISMATCH", "/invocation/subject_digest_argument"))
    if invocation.get("bundle_ref_argument") != bundle.get("ref"):
        findings.append(Finding("BUNDLE_BINDING_MISMATCH", "/invocation/bundle_ref_argument"))
    if invocation.get("predicate_type_argument") != predicate.get("predicate_type"):
        findings.append(Finding("PREDICATE_BINDING_MISMATCH", "/invocation/predicate_type_argument"))

    if bundle.get("rekor_inclusion_required") is not True or bundle.get("signed_entry_timestamp_required") is not True:
        findings.append(Finding("TRANSPARENCY_REQUIREMENT_MISSING", "/bundle"))
    if bundle.get("offline_verification_material_embedded") is not True:
        findings.append(Finding("OFFLINE_MATERIAL_MISSING", "/bundle/offline_verification_material_embedded"))

    mode = trust.get("mode")
    if mode == "KEYLESS":
        if (
            not isinstance(trust.get("certificate_identity"), str)
            or not isinstance(trust.get("certificate_oidc_issuer"), str)
            or trust.get("public_key_ref") is not None
        ):
            findings.append(Finding("KEYLESS_TRUST_INCOMPLETE", "/trust"))
    elif mode == "KEYED":
        if (
            not isinstance(trust.get("public_key_ref"), str)
            or trust.get("certificate_identity") is not None
            or trust.get("certificate_oidc_issuer") is not None
        ):
            findings.append(Finding("KEYED_TRUST_INCOMPLETE", "/trust"))

    if invocation.get("explicit_inputs_only") is not True or invocation.get("implicit_discovery") is not False:
        findings.append(Finding("IMPLICIT_DISCOVERY_ALLOWED", "/invocation"))
    if invocation.get("network_access") != "DENIED":
        findings.append(Finding("NETWORK_POSTURE_UNSAFE", "/invocation/network_access"))
    if invocation.get("allow_http_registry") is not False:
        findings.append(Finding("INSECURE_REGISTRY_ALLOWED", "/invocation/allow_http_registry"))
    if invocation.get("allow_insecure_registry") is not False:
        findings.append(Finding("INSECURE_REGISTRY_ALLOWED", "/invocation/allow_insecure_registry"))

    outcomes = expected_runtime.get("finite_outcomes")
    if outcomes != EXPECTED_OUTCOMES or not _canonical_array(outcomes):
        findings.append(Finding("OUTCOME_VOCABULARY_MISMATCH", "/expected_runtime/finite_outcomes"))
    for field in (
        "verified_requires_exit_code_zero",
        "stdout_is_not_authority",
        "stderr_is_not_authority",
    ):
        if expected_runtime.get(field) is not True:
            findings.append(Finding("RUNTIME_SUCCESS_RULE_UNSAFE", f"/expected_runtime/{field}"))

    forbidden_governance_true = (
        "cryptographic_verification_performed",
        "authority_created",
        "evidence_closure_claimed",
        "policy_evaluated",
        "review_authenticated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
    )
    if (
        any(governance.get(field) is not False for field in forbidden_governance_true)
        or governance.get("runtime_result_ref") is not None
    ):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    try:
        expected_hash = _canonical_hash(candidate)
    except (TypeError, ValueError, RecursionError):
        findings.append(Finding("SPEC_HASH_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    return findings


def validate_plan(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult(tuple(sorted(set(schema_findings))))
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


def _expected_manifest() -> dict[str, list[str]]:
    path = FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def run_fixture_profile() -> int:
    valid_files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid_files = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    semantic_files = sorted((FIXTURE_ROOT / "invalid").glob("semantic_invalid_*.json"))
    manifest = _expected_manifest()
    all_invalid = invalid_files + semantic_files
    if not valid_files or not all_invalid or not manifest:
        return 1

    passed = True
    for path in valid_files:
        result = validate_plan(path)
        print(_serialize(path, result))
        passed = result.ok and passed

    for path in all_invalid:
        result = validate_plan(path)
        print(_serialize(path, result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(manifest.get(path.name, []))
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": _display_path(path),
                        "actual_codes": actual,
                        "expected_codes": expected,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                        "scope": SCOPE,
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )

    if set(manifest) != {path.name for path in all_invalid}:
        passed = False
    return 0 if passed else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        return run_fixture_profile()
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2

    passed = True
    for raw in sorted(args.files):
        path = Path(raw)
        result = validate_plan(path)
        print(_serialize(path, result))
        passed = result.ok and passed
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(run())
