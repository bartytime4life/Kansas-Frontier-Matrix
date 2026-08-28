#!/usr/bin/env python3
"""Validate inactive per-input AI output artifacts and their batch indexes."""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import sys
from dataclasses import dataclass
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
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

ARTIFACT_SCHEMA = ROOT / "schemas/contracts/v1/runtime/ai_output_artifact.schema.json"
BATCH_SCHEMA = ROOT / "schemas/contracts/v1/runtime/ai_output_batch_manifest.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/runtime/ai_output_artifact"
CASE_FILES = tuple(sorted((FIXTURES / "cases").glob("*.json")))
SCOPE = "ai-output-artifact-fixture-only-v1"
MAX_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
FLOATING = re.compile(r"(^|[:/@._-])latest($|[:/@._-])", re.I)
REASON = {
    "ANSWER": "AI_OUTPUT_SUPPORTED",
    "ABSTAIN": "AI_OUTPUT_ABSTAINED",
    "DENY": "AI_OUTPUT_DENIED",
    "ERROR": "AI_OUTPUT_ERROR",
}
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "HASHING_UNAVAILABLE", "OBJECT_TYPE_UNKNOWN",
}


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
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


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
            path.read_text(encoding="utf-8"), object_pairs_hook=_pairs,
            parse_constant=_nonfinite, parse_float=_float,
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
    path = {
        "AIOutputArtifact": ARTIFACT_SCHEMA,
        "AIOutputBatchManifest": BATCH_SCHEMA,
    }.get(candidate.get("object_type"))
    if path is None:
        return [Finding("OBJECT_TYPE_UNKNOWN", "/object_type")]
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            MAX_SCHEMA_FINDINGS + 1,
        ))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda e: (_pointer(e.absolute_path), str(e.validator)))
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _hash(value: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(value)


def _identity(candidate: Mapping[str, Any], *excluded: str) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    for key in excluded:
        subject.pop(key, None)
    return subject


def compute_artifact_spec_hash(candidate: Mapping[str, Any]) -> str:
    return _hash(_identity(candidate, "artifact_id", "spec_hash"))


def compute_artifact_id(candidate: Mapping[str, Any]) -> str:
    return "ai-output-artifact:" + compute_artifact_spec_hash(candidate).removeprefix("sha256:")[:24]


def compute_batch_spec_hash(candidate: Mapping[str, Any]) -> str:
    return _hash(_identity(candidate, "manifest_id", "spec_hash"))


def compute_batch_id(candidate: Mapping[str, Any]) -> str:
    return "ai-output-batch-manifest:" + compute_batch_spec_hash(candidate).removeprefix("sha256:")[:24]


def _canonical(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _refs(value: object, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_path = f"{path}/{key}"
            if key.endswith("_ref") and isinstance(child, str):
                yield child_path, child
            elif key.endswith("_refs") and isinstance(child, list):
                yield from ((f"{child_path}/{i}", item) for i, item in enumerate(child) if isinstance(item, str))
            yield from _refs(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _refs(child, f"{path}/{index}")


def _governance(candidate: Mapping[str, Any], findings: set[Finding]) -> None:
    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.add(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))


def _hash_identity(candidate: Mapping[str, Any], *, batch: bool, findings: set[Finding]) -> None:
    try:
        expected_hash = compute_batch_spec_hash(candidate) if batch else compute_artifact_spec_hash(candidate)
        expected_id = compute_batch_id(candidate) if batch else compute_artifact_id(candidate)
        id_field = "manifest_id" if batch else "artifact_id"
        id_code = "BATCH_MANIFEST_ID_MISMATCH" if batch else "ARTIFACT_ID_MISMATCH"
        if candidate.get("spec_hash") != expected_hash:
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get(id_field) != expected_id:
            findings.add(Finding(id_code, f"/{id_field}"))
    except (TypeError, ValueError, RuntimeError, RecursionError):
        findings.add(Finding("HASHING_UNAVAILABLE", "/spec_hash"))


def _artifact_semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    _hash_identity(candidate, batch=False, findings=findings)
    support = candidate.get("support")
    lineage = candidate.get("lineage")
    output = candidate.get("output")
    reason_codes = candidate.get("reason_codes")
    for path, value in _refs(candidate):
        if FLOATING.search(value):
            findings.add(Finding("FLOATING_REFERENCE_DENIED", path))
    if not _canonical(reason_codes):
        findings.add(Finding("REASON_CODES_NOT_CANONICAL", "/reason_codes"))
    if isinstance(support, Mapping):
        for name in ("evidence_bundle_refs", "citation_refs", "review_record_refs", "attestation_refs"):
            if not _canonical(support.get(name)):
                findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/support/{name}"))
    if isinstance(lineage, Mapping):
        for name in ("correction_refs", "revocation_reason_codes"):
            if not _canonical(lineage.get(name)):
                findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/lineage/{name}"))
    authoritative = [ref for path, ref in _refs(candidate) if path.startswith(("/model", "/generation", "/support", "/lineage"))]
    if len(authoritative) != len(set(authoritative)):
        findings.add(Finding("REFERENCE_ROLE_COLLAPSE", "/"))

    outcome = candidate.get("outcome")
    if isinstance(outcome, str) and isinstance(reason_codes, list) and REASON.get(outcome) not in reason_codes:
        findings.add(Finding("OUTCOME_REASON_REQUIRED", "/reason_codes"))
    if isinstance(output, Mapping):
        has_result = isinstance(output.get("result_ref"), str) and isinstance(output.get("media_type"), str)
        if outcome == "ANSWER":
            if not has_result:
                findings.add(Finding("ANSWER_OUTPUT_REQUIRED", "/output"))
            if not isinstance(support, Mapping) or not support.get("evidence_bundle_refs") or not support.get("citation_refs"):
                findings.add(Finding("ANSWER_EVIDENCE_REQUIRED", "/support"))
        elif has_result or output.get("result_ref") is not None or output.get("media_type") is not None:
            findings.add(Finding("NEGATIVE_OUTPUT_FORBIDDEN", "/output"))

    if isinstance(lineage, Mapping):
        status = lineage.get("status")
        corrections = lineage.get("correction_refs")
        successor = lineage.get("successor_artifact_ref")
        revoked_at = lineage.get("revoked_at")
        reasons = lineage.get("revocation_reason_codes")
        if status == "ACTIVE" and (corrections or successor is not None or revoked_at is not None or reasons):
            findings.add(Finding("ACTIVE_LINEAGE_NOT_CLEAN", "/lineage"))
        elif status == "REVOKED" and (not corrections or revoked_at is None or not reasons or successor is not None):
            findings.add(Finding("REVOCATION_CLOSURE_REQUIRED", "/lineage"))
        elif status == "SUPERSEDED" and (not corrections or not isinstance(successor, str) or revoked_at is not None or reasons):
            findings.add(Finding("SUPERSESSION_CLOSURE_REQUIRED", "/lineage"))
    _governance(candidate, findings)
    return sorted(findings)


def _batch_counts(items: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    return {
        "total": len(items),
        "active": sum(item.get("lineage_status") == "ACTIVE" for item in items),
        "revoked": sum(item.get("lineage_status") == "REVOKED" for item in items),
        "superseded": sum(item.get("lineage_status") == "SUPERSEDED" for item in items),
        "answer": sum(item.get("outcome") == "ANSWER" for item in items),
        "abstain": sum(item.get("outcome") == "ABSTAIN" for item in items),
        "deny": sum(item.get("outcome") == "DENY" for item in items),
        "error": sum(item.get("outcome") == "ERROR" for item in items),
    }


def _batch_status(items: Sequence[Mapping[str, Any]]) -> str:
    statuses = [item.get("lineage_status") for item in items]
    if statuses and all(status == "REVOKED" for status in statuses):
        return "WITHDRAWN"
    if statuses and all(status == "SUPERSEDED" for status in statuses):
        return "SUPERSEDED"
    if any(status == "REVOKED" for status in statuses):
        return "PARTIALLY_REVOKED"
    return "ACTIVE"


def _batch_semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    _hash_identity(candidate, batch=True, findings=findings)
    for path, value in _refs(candidate):
        if FLOATING.search(value):
            findings.add(Finding("FLOATING_REFERENCE_DENIED", path))
    if not _canonical(candidate.get("run_receipt_refs")):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/run_receipt_refs"))
    lineage = candidate.get("lineage")
    if isinstance(lineage, Mapping) and not _canonical(lineage.get("correction_refs")):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/lineage/correction_refs"))
    raw_items = candidate.get("artifacts")
    items = [item for item in raw_items if isinstance(item, Mapping)] if isinstance(raw_items, list) else []
    input_refs = [str(item.get("input_ref", "")) for item in items]
    artifact_ids = [str(item.get("artifact_id", "")) for item in items]
    artifact_hashes = [str(item.get("artifact_spec_hash", "")) for item in items]
    if input_refs != sorted(input_refs):
        findings.add(Finding("BATCH_ITEMS_NOT_CANONICAL", "/artifacts"))
    for values, code in (
        (input_refs, "DUPLICATE_BATCH_INPUT"),
        (artifact_ids, "DUPLICATE_BATCH_ARTIFACT"),
        (artifact_hashes, "DUPLICATE_BATCH_ARTIFACT_HASH"),
    ):
        if len(values) != len(set(values)):
            findings.add(Finding(code, "/artifacts"))
    if candidate.get("counts") != _batch_counts(items):
        findings.add(Finding("BATCH_COUNTS_MISMATCH", "/counts"))
    if candidate.get("batch_status") != _batch_status(items):
        findings.add(Finding("BATCH_STATUS_MISMATCH", "/batch_status"))
    _governance(candidate, findings)
    return sorted(findings)


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    if candidate.get("object_type") == "AIOutputArtifact":
        return _artifact_semantic(candidate)
    if candidate.get("object_type") == "AIOutputBatchManifest":
        return _batch_semantic(candidate)
    return [Finding("OBJECT_TYPE_UNKNOWN", "/object_type")]


def _outcome(findings: Sequence[Finding]) -> str:
    return "ERROR" if any(item.code in ERROR_CODES for item in findings) else ("FAIL" if findings else "PASS")


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is not None:
        findings.extend(validate_payload(candidate).findings)
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps({
        "authority_created": False,
        "file": _display(path),
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome,
        "scope": SCOPE,
    }, sort_keys=True, separators=(",", ":"))


def validate_fixture_suite() -> tuple[bool, list[str]]:
    ok, lines, seen = True, [], set()
    for case_file in CASE_FILES:
        suite, errors = _read(case_file)
        if suite is None:
            lines.append(serialize(case_file, ValidationResult(_outcome(errors), tuple(errors))))
            ok = False
            continue
        cases = suite.get("cases")
        if suite.get("schema_version") != "kfm.ai-output-artifact-fixtures.v1" or not isinstance(cases, list):
            lines.append(serialize(case_file, ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/cases"),))))
            ok = False
            continue
        for case in cases:
            if not isinstance(case, Mapping):
                ok = False
                continue
            case_id, payload = case.get("case_id"), case.get("payload")
            expected, codes = case.get("expected_outcome"), case.get("expected_findings")
            if not isinstance(case_id, str) or case_id in seen or not isinstance(payload, Mapping) or expected not in {"PASS", "FAIL", "ERROR"} or not isinstance(codes, list):
                ok = False
                continue
            seen.add(case_id)
            result = validate_payload(payload)
            actual = sorted({finding.code for finding in result.findings})
            match = result.outcome == expected and actual == sorted(set(str(code) for code in codes))
            ok = ok and match
            lines.append(json.dumps({
                "case_id": case_id,
                "fixture": f"{_display(case_file)}#{case_id}",
                "finding_codes": actual,
                "outcome": result.outcome,
                "scope": SCOPE,
                "suite_match": match,
            }, sort_keys=True, separators=(",", ":")))
    return ok and len(seen) == 26, lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        ok, lines = validate_fixture_suite()
        print(*lines, sep="\n")
        return 0 if ok else 1
    if not args.files:
        parser.error("provide one or more files or --fixtures")
    results = [validate_record(path) for path in args.files]
    for path, result in zip(args.files, results):
        print(serialize(path, result))
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
