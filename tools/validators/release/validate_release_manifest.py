#!/usr/bin/env python3
"""Validate the inactive, fixture-only ReleaseManifest candidate profile.

The legacy permissive id-only profile remains accepted. Strict candidates get
closed-schema and deterministic semantic checks only; PASS creates no evidence,
policy, review, promotion, release, publication, signature, lifecycle-write, or
public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_IMPORT_ERROR: Exception | None = exc
else:
    HASH_IMPORT_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/release/release_manifest.schema.json"
FIXTURES = ROOT / "fixtures/release/release_manifest"
CASES = FIXTURES / "cases.json"
SCOPE = "release-manifest-fixture-only-v1"
MAX_BYTES = 2_097_152
MAX_SCHEMA_FINDINGS = 100
FLOATING_LATEST = re.compile(r"(^|[:/@._-])latest($|[:/@._-])", re.I)
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "HASHING_UNAVAILABLE",
}
REFERENCE_ARRAYS = (
    "source_descriptor_refs", "evidence_bundle_refs", "policy_decision_refs",
    "promotion_decision_refs", "review_record_refs", "catalog_refs", "proof_refs",
    "receipt_refs", "attestation_refs",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("id", None)
    subject.pop("spec_hash", None)
    return subject


def compute_manifest_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_IMPORT_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing package unavailable") from HASH_IMPORT_ERROR
    return compute_spec_hash(identity_subject(candidate))


def compute_manifest_id(candidate: Mapping[str, Any]) -> str:
    digest = compute_manifest_spec_hash(candidate).removeprefix("sha256:")
    return "release-manifest:" + digest[:24]


def _canonical_ref_array(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _dt(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None


def _iter_role_refs(candidate: Mapping[str, Any]) -> Iterable[tuple[str, object]]:
    yield "/release_id", candidate.get("release_id")
    for name in REFERENCE_ARRAYS:
        value = candidate.get(name)
        if isinstance(value, list):
            for index, item in enumerate(value):
                yield f"/{name}/{index}", item
    scope = candidate.get("release_scope")
    if isinstance(scope, Mapping):
        refs = scope.get("transform_receipt_refs")
        if isinstance(refs, list):
            for index, item in enumerate(refs):
                yield f"/release_scope/transform_receipt_refs/{index}", item
    lineage = candidate.get("lineage")
    if isinstance(lineage, Mapping):
        yield (
            "/lineage/previous_release_manifest_ref",
            lineage.get("previous_release_manifest_ref"),
        )
        yield "/lineage/withdrawal_ref", lineage.get("withdrawal_ref")
        yield "/lineage/rollback_ref", lineage.get("rollback_ref")
        refs = lineage.get("correction_refs")
        if isinstance(refs, list):
            for index, item in enumerate(refs):
                yield f"/lineage/correction_refs/{index}", item
    provenance = candidate.get("provenance")
    if isinstance(provenance, Mapping):
        yield "/provenance/run_receipt_ref", provenance.get("run_receipt_ref")


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    if candidate.get("object_type") != "ReleaseManifest":
        return []
    findings: set[Finding] = set()
    try:
        if candidate.get("spec_hash") != compute_manifest_spec_hash(candidate):
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("id") != compute_manifest_id(candidate):
            findings.add(Finding("MANIFEST_ID_MISMATCH", "/id"))
    except (TypeError, ValueError, RuntimeError, RecursionError):
        findings.add(Finding("HASHING_UNAVAILABLE", "/spec_hash"))

    for name in REFERENCE_ARRAYS:
        if not _canonical_ref_array(candidate.get(name)):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/{name}"))
    scope = candidate.get("release_scope")
    if isinstance(scope, Mapping) and not _canonical_ref_array(
        scope.get("transform_receipt_refs")
    ):
        findings.add(
            Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/release_scope/transform_receipt_refs")
        )
    lineage = candidate.get("lineage")
    if isinstance(lineage, Mapping) and not _canonical_ref_array(
        lineage.get("correction_refs")
    ):
        findings.add(
            Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/lineage/correction_refs")
        )

    artifacts = candidate.get("artifacts")
    if isinstance(artifacts, list):
        refs = [
            item.get("artifact_ref")
            for item in artifacts
            if isinstance(item, Mapping)
        ]
        if refs != sorted(refs) or len(refs) != len(set(refs)):
            findings.add(Finding("ARTIFACT_ARRAY_NOT_CANONICAL", "/artifacts"))
        if candidate.get("artifact_count") != len(artifacts):
            findings.add(Finding("ARTIFACT_COUNT_MISMATCH", "/artifact_count"))
        evidence_artifacts = {
            item.get("artifact_ref")
            for item in artifacts
            if isinstance(item, Mapping) and item.get("role") == "EVIDENCE_BUNDLE"
        }
        evidence_refs = candidate.get("evidence_bundle_refs")
        if isinstance(evidence_refs, list) and not set(evidence_refs).issubset(
            evidence_artifacts
        ):
            findings.add(
                Finding("EVIDENCE_ARTIFACT_BINDING_MISSING", "/evidence_bundle_refs")
            )

    role_values: list[str] = []
    for path, value in _iter_role_refs(candidate):
        if isinstance(value, str):
            role_values.append(value)
            if FLOATING_LATEST.search(value):
                findings.add(Finding("FLOATING_REFERENCE_DENIED", path))
    # Repeated RunReceipt is allowed between receipt_refs and provenance because it is
    # one declared process-memory object, not a role collapse. Remove that exact pair.
    provenance = candidate.get("provenance")
    allowed_repeat = (
        provenance.get("run_receipt_ref")
        if isinstance(provenance, Mapping)
        else None
    )
    adjusted = list(role_values)
    if isinstance(allowed_repeat, str) and adjusted.count(allowed_repeat) == 2:
        adjusted.remove(allowed_repeat)
    if len(adjusted) != len(set(adjusted)):
        findings.add(Finding("REFERENCE_ROLE_COLLAPSE", "/"))

    temporal = candidate.get("temporal")
    if isinstance(temporal, Mapping):
        start = _dt(temporal.get("effective_from"))
        end = _dt(temporal.get("effective_to"))
        if start is not None and end is not None and start > end:
            findings.add(Finding("TEMPORAL_WINDOW_INCOHERENT", "/temporal"))

    if isinstance(lineage, Mapping):
        corrections = lineage.get("correction_refs")
        if (
            isinstance(corrections, list)
            and corrections
            and lineage.get("previous_release_manifest_ref") is None
        ):
            findings.add(
                Finding("CORRECTION_PREDECESSOR_REQUIRED", "/lineage")
            )

    if isinstance(scope, Mapping) and scope.get("audience") == "PUBLIC":
        if scope.get("rights_status") != "APPROVED":
            findings.add(
                Finding("PUBLIC_RIGHTS_NOT_APPROVED", "/release_scope/rights_status")
            )
        if scope.get("sensitivity_status") not in {
            "PUBLIC_SAFE",
            "TRANSFORM_REQUIRED",
        }:
            findings.add(
                Finding(
                    "PUBLIC_SENSITIVITY_NOT_APPROVED",
                    "/release_scope/sensitivity_status",
                )
            )
        if not candidate.get("evidence_bundle_refs"):
            findings.add(Finding("PUBLIC_EVIDENCE_REQUIRED", "/evidence_bundle_refs"))
        if not candidate.get("policy_decision_refs"):
            findings.add(Finding("PUBLIC_POLICY_REQUIRED", "/policy_decision_refs"))
        if not candidate.get("promotion_decision_refs"):
            findings.add(
                Finding("PUBLIC_PROMOTION_REQUIRED", "/promotion_decision_refs")
            )
        if not candidate.get("review_record_refs"):
            findings.add(Finding("PUBLIC_REVIEW_REQUIRED", "/review_record_refs"))
    if (
        isinstance(scope, Mapping)
        and scope.get("sensitivity_status") == "TRANSFORM_REQUIRED"
        and (
            scope.get("generalized") is not True
            or not scope.get("transform_receipt_refs")
        )
    ):
        findings.add(Finding("TRANSFORM_EVIDENCE_REQUIRED", "/release_scope"))

    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(
        value is not False for value in governance.values()
    ):
        findings.add(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return sorted(findings)


def _outcome(findings: Sequence[Finding]) -> str:
    return (
        "ERROR"
        if any(item.code in ERROR_CODES for item in findings)
        else ("FAIL" if findings else "PASS")
    )


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is not None:
        schema_findings = _schema_findings(candidate)
        findings.extend(schema_findings)
        if not schema_findings:
            findings.extend(_semantic(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": _display(path),
            "findings": [
                {"code": item.code, "path": item.path}
                for item in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _segments(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/") or pointer == "/":
        raise ValueError("fixture pointer must be a non-root JSON pointer")
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]


def _parent(candidate: dict[str, Any], pointer: str) -> tuple[dict[str, Any], str]:
    parts = _segments(pointer)
    current: Any = candidate
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise ValueError("fixture pointer does not resolve")
        current = current[part]
    if not isinstance(current, dict):
        raise ValueError("fixture pointer parent is not an object")
    return current, parts[-1]


def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parent, key = _parent(candidate, pointer)
    parent[key] = copy.deepcopy(value)


def _remove_pointer(candidate: dict[str, Any], pointer: str) -> None:
    parent, key = _parent(candidate, pointer)
    if key not in parent:
        raise ValueError("fixture remove pointer does not resolve")
    del parent[key]


def _reverse_pointer(candidate: dict[str, Any], pointer: str) -> None:
    parent, key = _parent(candidate, pointer)
    value = parent.get(key)
    if not isinstance(value, list):
        raise ValueError("fixture reverse pointer is not an array")
    parent[key] = list(reversed(value))


def materialize_case(
    matrix: Mapping[str, Any], record: Mapping[str, Any]
) -> dict[str, Any]:
    bases = matrix.get("bases")
    base_id = record.get("base")
    if not isinstance(bases, Mapping) or not isinstance(base_id, str):
        raise ValueError("fixture case lacks a valid base")
    base = bases.get(base_id)
    if not isinstance(base, Mapping):
        raise ValueError("fixture case references an unknown base")
    candidate = copy.deepcopy(dict(base))
    removals = record.get("remove", [])
    settings = record.get("set", {})
    reversals = record.get("reverse", [])
    overrides = record.get("override", {})
    if not isinstance(removals, list) or not all(
        isinstance(item, str) for item in removals
    ):
        raise ValueError("fixture remove must be an array of pointers")
    if not isinstance(settings, Mapping) or not isinstance(overrides, Mapping):
        raise ValueError("fixture set/override must be pointer mappings")
    if not isinstance(reversals, list) or not all(
        isinstance(item, str) for item in reversals
    ):
        raise ValueError("fixture reverse must be an array of pointers")
    for pointer in removals:
        _remove_pointer(candidate, pointer)
    for pointer, value in sorted(settings.items()):
        if not isinstance(pointer, str):
            raise ValueError("fixture set pointer must be a string")
        _set_pointer(candidate, pointer, value)
    for pointer in reversals:
        _reverse_pointer(candidate, pointer)
    if (
        record.get("recompute_identity") is True
        and candidate.get("object_type") == "ReleaseManifest"
    ):
        candidate["spec_hash"] = compute_manifest_spec_hash(candidate)
        candidate["id"] = compute_manifest_id(candidate)
    for pointer, value in sorted(overrides.items()):
        if not isinstance(pointer, str):
            raise ValueError("fixture override pointer must be a string")
        _set_pointer(candidate, pointer, value)
    return candidate


def validate_candidate(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def serialize_label(label: str, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": label,
            "findings": [
                {"code": item.code, "path": item.path}
                for item in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    matrix, findings = _read(CASES)
    if matrix is None or findings:
        return 1
    passed = True
    seen = 0
    for group in ("valid", "invalid"):
        group_cases = matrix.get(group)
        if not isinstance(group_cases, Mapping):
            return 1
        for case_id, record in sorted(group_cases.items()):
            if not isinstance(case_id, str) or not isinstance(record, Mapping):
                passed = False
                continue
            expected = record.get("expected")
            if not isinstance(expected, Mapping):
                passed = False
                continue
            try:
                candidate = materialize_case(matrix, record)
            except (TypeError, ValueError, RuntimeError, RecursionError):
                passed = False
                continue
            result = validate_candidate(candidate)
            print(serialize_label(f"fixture:{group}:{case_id}", result))
            actual = sorted({item.code for item in result.findings})
            if (
                result.outcome != expected.get("outcome")
                or actual != expected.get("findings")
            ):
                passed = False
            seen += 1
    return 0 if passed and seen == 21 else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or --fixtures")
    results = [validate_record(path) for path in args.files]
    for path, result in zip(args.files, results):
        print(serialize(path, result))
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
