#!/usr/bin/env python3
"""Validate inactive, synthetic purpose-specific hash-binding assessments.

PASS proves closed shape, exact reference closure to the existing readiness
matrix, a valid assessment spec_hash, non-recursive subject selection, and
bounded comparison/canonicalization controls only. It does not implement or
activate a candidate profile, compute production digests, migrate hashes,
authorize signing, decide policy, release, or publish.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/common/hash_binding_assessment.schema.json"
MATRIX = ROOT / "control_plane/hash_profile_readiness_matrix.json"
FIXTURES = ROOT / "fixtures/contracts/v1/common/hash_binding_assessment"
BASELINE = FIXTURES / "valid_assessment.json"
CASES = FIXTURES / "cases.json"
MAX_JSON_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "synthetic-hash-binding-conformance-only"

EXPECTED_PURPOSE = {
    "content_hash": ("ARTIFACT_BYTE_INTEGRITY", "RAW_BYTES"),
    "descriptor_hash": ("SEMANTIC_DESCRIPTOR_IDENTITY", "JSON_FIELD_SELECTION"),
    "range_hash": ("RANGE_PROOF_IDENTITY", "BYTE_RANGE"),
    "root_hash": ("ORDERED_FILESET_IDENTITY", "ORDERED_FILESET"),
    "signature_digest": ("SIGNED_SUBJECT_IDENTITY", "DSSE_PAYLOAD_BYTES"),
    "spec_hash": ("SPECIFICATION_IDENTITY", "JSON_FIELD_SELECTION"),
}
EXPECTED_PREFIX = {"SHA-256": "sha256:", "BLAKE3": "blake3:"}
REQUIRED_GAP_CONTROLS = {
    "NORMALIZED_GEOMETRY_IDENTITY": {
        "CRS_PROFILE",
        "FINITE_COORDINATES",
        "GEOMETRY_NORMALIZATION",
    },
    "RECEIPT_PAYLOAD_IDENTITY": {
        "PAYLOAD_SUBJECT_SELECTION",
        "SIGNATURE_EXCLUSION",
        "VOLATILE_FIELD_EXCLUSION",
    },
}


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
    def outcome(self) -> str:
        return "PASS" if self.ok else "ERROR"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except FileNotFoundError:
        return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical(values: Any) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _semantic(value: Mapping[str, Any], matrix: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    declared_hash = value.get("spec_hash")
    if isinstance(declared_hash, str):
        subject = {key: item for key, item in value.items() if key != "spec_hash"}
        if declared_hash != compute_spec_hash(subject):
            findings.append(Finding("ASSESSMENT_SPEC_HASH_MISMATCH", "/spec_hash"))

    matrix_hash = matrix.get("spec_hash")
    if value.get("readiness_matrix_spec_hash") != matrix_hash:
        findings.append(Finding("READINESS_MATRIX_REFERENCE_MISMATCH", "/readiness_matrix_spec_hash"))

    matrix_profiles = matrix.get("profiles") if isinstance(matrix.get("profiles"), list) else []
    matrix_by_id = {
        profile.get("profile_id"): profile
        for profile in matrix_profiles
        if isinstance(profile, dict) and isinstance(profile.get("profile_id"), str)
    }
    bindings = value.get("bindings") if isinstance(value.get("bindings"), list) else []
    profile_ids = [binding.get("profile_id") for binding in bindings if isinstance(binding, dict)]
    if profile_ids != sorted(profile_ids):
        findings.append(Finding("BINDINGS_NOT_CANONICAL", "/bindings"))
    if len(profile_ids) != len(set(profile_ids)):
        findings.append(Finding("BINDING_PROFILE_DUPLICATE", "/bindings"))
    if set(profile_ids) != set(matrix_by_id):
        findings.append(Finding("READINESS_PROFILE_SET_MISMATCH", "/bindings"))

    matrix_fields = (
        "hash_role",
        "algorithm",
        "digest_prefix",
        "canonicalization_profile",
        "implementation_state",
        "activation_state",
    )
    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            continue
        base = f"/bindings/{index}"
        profile_id = binding.get("profile_id")
        matrix_profile = matrix_by_id.get(profile_id)
        role = binding.get("hash_role")
        if isinstance(matrix_profile, dict):
            if any(binding.get(field) != matrix_profile.get(field) for field in matrix_fields):
                findings.append(Finding("READINESS_PROFILE_MISMATCH", base))
            if matrix_profile.get("activation_state") == "INACTIVE" and binding.get("activation_state") != "INACTIVE":
                findings.append(Finding("NEW_ACTIVATION_FORBIDDEN", f"{base}/activation_state"))
        expected_purpose = EXPECTED_PURPOSE.get(role)
        if expected_purpose and (binding.get("purpose"), binding.get("subject_kind")) != expected_purpose:
            findings.append(Finding("ROLE_PURPOSE_MISMATCH", f"{base}/purpose"))
        if binding.get("digest_prefix") != EXPECTED_PREFIX.get(binding.get("algorithm")):
            findings.append(Finding("ALGORITHM_PREFIX_MISMATCH", f"{base}/digest_prefix"))

        field_names = (
            "included_fields",
            "excluded_fields",
            "volatile_fields",
            "digest_fields",
            "signature_fields",
        )
        for field_name in field_names:
            if not _canonical(binding.get(field_name)):
                findings.append(Finding("FIELD_SET_NOT_CANONICAL", f"{base}/{field_name}"))
        included = set(binding.get("included_fields", []))
        excluded = set(binding.get("excluded_fields", []))
        volatile = set(binding.get("volatile_fields", []))
        digests = set(binding.get("digest_fields", []))
        signatures = set(binding.get("signature_fields", []))
        if included & excluded:
            findings.append(Finding("FIELD_SELECTION_OVERLAP", base))
        if not digests <= excluded or included & digests:
            findings.append(Finding("SELF_HASH_FIELD_INCLUDED", f"{base}/digest_fields"))
        if not signatures <= excluded or included & signatures:
            findings.append(Finding("SIGNATURE_FIELD_INCLUDED", f"{base}/signature_fields"))
        if not volatile <= excluded or included & volatile:
            findings.append(Finding("VOLATILE_FIELD_INCLUDED", f"{base}/volatile_fields"))

        collections = binding.get("unordered_collections")
        if isinstance(collections, list):
            collection_fields = [item.get("field") for item in collections if isinstance(item, dict)]
            if collection_fields != sorted(collection_fields) or len(collection_fields) != len(set(collection_fields)):
                findings.append(Finding("COLLECTION_RULES_NOT_CANONICAL", f"{base}/unordered_collections"))
            for collection_index, item in enumerate(collections):
                if not isinstance(item, dict):
                    continue
                collection_base = f"{base}/unordered_collections/{collection_index}"
                if item.get("field") not in included:
                    findings.append(Finding("UNORDERED_COLLECTION_NOT_INCLUDED", f"{collection_base}/field"))
                if item.get("ordering_rule") == "UNDECLARED":
                    findings.append(Finding("UNORDERED_COLLECTION_RULE_MISSING", f"{collection_base}/ordering_rule"))

        if binding.get("canonicalization_profile") == "RFC8785-JCS" and binding.get("finite_numbers_required") is not True:
            findings.append(Finding("JCS_NONFINITE_NOT_REJECTED", f"{base}/finite_numbers_required"))
        if binding.get("comparison_profile_id") != profile_id or binding.get("equality_scope") != "SAME_PROFILE_ONLY":
            findings.append(Finding("CROSS_PROFILE_COMPARISON", f"{base}/comparison_profile_id"))

    gaps = value.get("purpose_gaps") if isinstance(value.get("purpose_gaps"), list) else []
    gap_purposes = [gap.get("purpose") for gap in gaps if isinstance(gap, dict)]
    if gap_purposes != sorted(gap_purposes) or set(gap_purposes) != set(REQUIRED_GAP_CONTROLS):
        findings.append(Finding("PURPOSE_GAPS_NOT_CANONICAL", "/purpose_gaps"))
    for index, gap in enumerate(gaps):
        if not isinstance(gap, dict):
            continue
        base = f"/purpose_gaps/{index}"
        purpose = gap.get("purpose")
        controls = gap.get("required_controls")
        control_set = set(controls) if isinstance(controls, list) else set()
        if not _canonical(controls):
            findings.append(Finding("GAP_CONTROLS_NOT_CANONICAL", f"{base}/required_controls"))
        if gap.get("status") != "HOLD_NO_PROFILE" or gap.get("profile_id") is not None:
            findings.append(Finding("PURPOSE_GAP_BOUND_WITHOUT_DECISION", base))
        if not REQUIRED_GAP_CONTROLS.get(purpose, set()) <= control_set:
            code = "AMBIGUOUS_CRS_NOT_HELD" if purpose == "NORMALIZED_GEOMETRY_IDENTITY" else "RECEIPT_SUBJECT_CONTROLS_MISSING"
            findings.append(Finding(code, f"{base}/required_controls"))

    effects = value.get("authority_effects")
    if isinstance(effects, dict):
        for key, enabled in effects.items():
            if enabled is not False:
                findings.append(Finding("AUTHORITY_EFFECT_ENABLED", f"/authority_effects/{key}"))
    return findings


def _load_matrix() -> tuple[dict[str, Any] | None, list[Finding]]:
    matrix, findings = _read(MATRIX)
    if matrix is None:
        return None, [Finding("READINESS_MATRIX_UNAVAILABLE", finding.field) for finding in findings]
    declared = matrix.get("spec_hash")
    subject = {key: item for key, item in matrix.items() if key != "spec_hash"}
    if not isinstance(declared, str) or declared != compute_spec_hash(subject):
        return None, [Finding("READINESS_MATRIX_INVALID", "/spec_hash")]
    return matrix, []


def validate_value(value: Mapping[str, Any], matrix: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(value)
    if not findings:
        findings.extend(_semantic(value, matrix))
    return ValidationResult(tuple(sorted(set(findings))))


def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None:
        return ValidationResult(tuple(sorted(set(findings))))
    matrix, matrix_findings = _load_matrix()
    if matrix is None:
        return ValidationResult(tuple(sorted(set(matrix_findings))))
    return validate_value(value, matrix)


def _replace(candidate: Any, pointer: str, value: Any) -> None:
    if not pointer.startswith("/") or pointer == "/":
        raise ValueError("invalid patch pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    current = candidate
    for raw in parts[:-1]:
        current = current[int(raw)] if isinstance(current, list) else current[raw]
    key = parts[-1]
    if isinstance(current, list):
        current[int(key)] = value
    else:
        current[key] = value


def run_fixtures() -> int:
    try:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        suite = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    matrix, findings = _load_matrix()
    if matrix is None:
        return 1
    passed = True
    for case in suite["cases"]:
        candidate = copy.deepcopy(baseline)
        for mutation in case["mutations"]:
            if mutation.get("op") != "replace":
                return 1
            _replace(candidate, mutation["path"], mutation["value"])
        if case.get("recompute_spec_hash"):
            candidate["spec_hash"] = compute_spec_hash({key: item for key, item in candidate.items() if key != "spec_hash"})
        result = validate_value(candidate, matrix)
        codes = sorted({finding.code for finding in result.findings})
        match = result.outcome == case["expected_outcome"] and codes == case["expected_findings"]
        print(
            json.dumps(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": codes,
                    "suite_match": match,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and match
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    files = args.files or [BASELINE]
    failed = False
    for path in sorted(files, key=lambda item: item.as_posix()):
        result = validate(path)
        print(
            json.dumps(
                {
                    "file": path.as_posix(),
                    "outcome": result.outcome,
                    "findings": [
                        {"code": finding.code, "field": finding.field}
                        for finding in result.findings
                    ],
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
