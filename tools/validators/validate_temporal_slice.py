#!/usr/bin/env python3
"""Validate proposed KFM TemporalSlice records without network access.

A green result proves bounded shape, deterministic identity, temporal ordering,
canonical references, and local change-lineage consistency only. It does not
resolve evidence or receipts, evaluate policy, create an index, or authorize
promotion, release, publication, or public use.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
from tools.validators._common.local_resolver import build_registry

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/temporal_slice.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/temporal_slice"
MAX_FILE_BYTES = 1_048_576
MAX_DEPTH = 64
MAX_SCHEMA_FINDINGS = 100
SCOPE = "temporal-slice-shape-identity-time-and-change-lineage-only"
ERROR_CODES = frozenset({
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "INPUT_NOT_REGULAR_FILE", "JSON_COMPLEXITY_LIMIT", "JSON_DUPLICATE_KEY",
    "JSON_INVALID", "JSON_NONFINITE_NUMBER", "JSON_NOT_UTF8", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "SCHEMA_EVALUATION_LIMIT",
})

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    @property
    def ok(self) -> bool: return not self.findings
    @property
    def error(self) -> bool: return any(f.code in ERROR_CODES for f in self.findings)

def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result: raise DuplicateKeyError
        result[key] = value
    return result

def _reject_nonfinite(_: str) -> None: raise NonFiniteNumberError

def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _too_deep(text: str) -> bool:
    depth = 0; in_string = False; escaped = False
    for char in text:
        if in_string:
            if escaped: escaped = False
            elif char == "\\": escaped = True
            elif char == '"': in_string = False
            continue
        if char == '"': in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_DEPTH: return True
        elif char in "]}": depth -= 1
    return False

def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.exists(): return None, [Finding("FILE_NOT_FOUND", "/")]
        if not path.is_file(): return None, [Finding("INPUT_NOT_REGULAR_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES: return None, [Finding("FILE_TOO_LARGE", "/")]
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if _too_deep(text): return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    try:
        value = json.loads(text, object_pairs_hook=_unique_object,
                           parse_constant=_reject_nonfinite, parse_float=_finite_float)
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except (RecursionError, ValueError): return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []

def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, registry=build_registry(REPO_ROOT),
                                 format_checker=FormatChecker())

def _schema_findings(validator: Draft202012Validator,
                     candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_EVALUATION_LIMIT", "/")]
    findings = [Finding("SCHEMA_INVALID", _pointer(tuple(e.absolute_path)))
                for e in sorted(errors[:MAX_SCHEMA_FINDINGS],
                                key=lambda e: (_pointer(tuple(e.absolute_path)), str(e.validator)))]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings

def _mapping(value: Any) -> Mapping[str, Any]: return value if isinstance(value, Mapping) else {}
def _array(value: Any) -> list[Any]: return value if isinstance(value, list) else []
def _canonical_strings(value: Any) -> bool:
    values = _array(value)
    return all(isinstance(x, str) for x in values) and values == sorted(set(values))

def canonical_slice_id(candidate: Mapping[str, Any]) -> str:
    temporal = _mapping(candidate.get("temporal_window")); spatial = _mapping(candidate.get("spatial")); provenance = _mapping(candidate.get("provenance"))
    projection = {
        "dataset_version_ref": candidate.get("dataset_version_ref"),
        "temporal_window": temporal,
        "footprint_hash": spatial.get("footprint_hash"),
        "grid_system": spatial.get("grid_system"),
        "grid_key": spatial.get("grid_key"),
        "spec_hash": provenance.get("spec_hash"),
    }
    encoded = json.dumps(projection, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "kfm:temporal-slice:sha256:" + hashlib.sha256(encoded).hexdigest()

def _aware_datetime(value: Any) -> tuple[datetime | None, bool]:
    if not isinstance(value, str): return None, False
    try: parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError: return None, False
    return parsed, parsed.tzinfo is None or parsed.utcoffset() is None

def _placeholder_digest(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("sha256:") and set(value[7:]) == {"0"}

def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    temporal = _mapping(candidate.get("temporal_window")); spatial = _mapping(candidate.get("spatial")); provenance = _mapping(candidate.get("provenance")); verification = _mapping(candidate.get("verification")); change = _mapping(candidate.get("change")); materialization = _mapping(candidate.get("materialization")); governance = _mapping(candidate.get("governance"))

    supplied = candidate.get("slice_id")
    if isinstance(supplied, str):
        try: expected = canonical_slice_id(candidate)
        except (TypeError, ValueError, RecursionError): expected = None
        if expected is not None and supplied != expected: findings.append(Finding("SLICE_ID_MISMATCH", "/slice_id"))

    start, start_naive = _aware_datetime(temporal.get("start")); end, end_naive = _aware_datetime(temporal.get("end"))
    if start_naive: findings.append(Finding("TEMPORAL_TIMEZONE_REQUIRED", "/temporal_window/start"))
    if end_naive: findings.append(Finding("TEMPORAL_TIMEZONE_REQUIRED", "/temporal_window/end"))
    if start is not None and end is not None and start > end: findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal_window/end"))

    arrays = {
        "/provenance/evidence_bundle_refs": provenance.get("evidence_bundle_refs"),
        "/provenance/input_refs": provenance.get("input_refs"),
        "/verification/check_refs": verification.get("check_refs"),
        "/verification/policy_decision_refs": verification.get("policy_decision_refs"),
        "/verification/policy_labels": verification.get("policy_labels"),
        "/verification/obligations": verification.get("obligations"),
        "/change/change_flags": change.get("change_flags"),
        "/materialization/surfaces": materialization.get("surfaces"),
    }
    for field, value in arrays.items():
        if not _canonical_strings(value): findings.append(Finding("REFS_NOT_CANONICAL", field))

    refs: list[str] = []
    for index, raw in enumerate(_array(materialization.get("artifacts"))):
        artifact = _mapping(raw); ref = artifact.get("artifact_ref")
        if isinstance(ref, str): refs.append(ref)
        if _placeholder_digest(artifact.get("digest")): findings.append(Finding("DIGEST_PLACEHOLDER_DENIED", f"/materialization/artifacts/{index}/digest"))
    if refs != sorted(refs) or len(refs) != len(set(refs)): findings.append(Finding("ARTIFACT_REFS_NOT_CANONICAL", "/materialization/artifacts"))
    for field, value in (("/spatial/footprint_hash", spatial.get("footprint_hash")), ("/provenance/spec_hash", provenance.get("spec_hash"))):
        if _placeholder_digest(value): findings.append(Finding("DIGEST_PLACEHOLDER_DENIED", field))

    state = change.get("state"); previous = change.get("previous_slice_ref"); assessment = change.get("material_change_assessment_ref"); delta = change.get("delta_proof_ref"); magnitude = change.get("delta_magnitude"); flags = _array(change.get("change_flags")); support = assessment is not None or delta is not None or magnitude is not None or bool(flags)
    if isinstance(supplied, str) and previous == supplied: findings.append(Finding("PREVIOUS_SLICE_SELF_REFERENCE", "/change/previous_slice_ref"))
    if previous is None:
        if state != "BASELINE": findings.append(Finding("PREVIOUS_SLICE_REQUIRED", "/change/previous_slice_ref"))
        if support: findings.append(Finding("CHANGE_WITHOUT_PREVIOUS_SLICE", "/change"))
    elif state == "BASELINE": findings.append(Finding("BASELINE_WITH_PREVIOUS_SLICE", "/change/state"))
    if state == "BASELINE" and support: findings.append(Finding("BASELINE_WITH_CHANGE_SUPPORT", "/change"))
    elif state == "CHANGED":
        if assessment is None and delta is None: findings.append(Finding("CHANGE_SUPPORT_MISSING", "/change"))
        if magnitude is None and not flags: findings.append(Finding("CHANGE_SIGNAL_MISSING", "/change"))
    elif state == "UNCHANGED":
        if assessment is None: findings.append(Finding("UNCHANGED_ASSESSMENT_REQUIRED", "/change/material_change_assessment_ref"))
        if delta is not None or magnitude is not None or flags: findings.append(Finding("UNCHANGED_WITH_DELTA", "/change"))

    if candidate.get("lifecycle_stage") == "CATALOG" and verification.get("promotion_gate_ref") is None:
        findings.append(Finding("CATALOG_GATE_REFERENCE_REQUIRED", "/verification/promotion_gate_ref"))
    flags_false = ("authority_created", "evidence_closure_claimed", "policy_evaluated", "promotion_authorized", "release_authorized", "publication_authorized", "public_use_allowed")
    if any(governance.get(name) is not False for name in flags_false) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings

def validate_slice(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None: return ValidationResult(tuple(sorted(set(findings))))
    try: schema = _schema_validator()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError): return ValidationResult((Finding("SCHEMA_UNAVAILABLE", "/"),))
    findings.extend(_schema_findings(schema, candidate)); findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))

def _display(path: Path) -> str:
    try: return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError): return path.name

def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps({"file": _display(path), "findings": [{"code": f.code, "field": f.field} for f in result.findings], "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"), "scope": SCOPE}, sort_keys=True, separators=(",", ":"))

def _fixtures(directory: Path) -> list[Path]:
    return sorted((p for p in directory.glob("*.json") if p.name != "expected_findings_manifest.json"), key=lambda p: p.name)

def _expected() -> dict[str, list[str]]:
    value = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    if not isinstance(value, dict): raise ValueError
    return {k: sorted(x for x in v if isinstance(x, str)) for k, v in value.items() if isinstance(k, str) and isinstance(v, list)}

def validate_fixtures() -> int:
    valid = _fixtures(FIXTURE_ROOT / "valid"); invalid = _fixtures(FIXTURE_ROOT / "invalid")
    if not valid or not invalid: print("ERROR: valid and invalid fixture lanes must both be non-empty"); return 1
    try: expected = _expected()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError): print("ERROR: expected findings manifest could not be loaded"); return 1
    ok = sorted(expected) == [p.name for p in invalid]
    for path in valid:
        result = validate_slice(path); print(_serialize(path, result)); ok = result.ok and ok
    for path in invalid:
        result = validate_slice(path); print(_serialize(path, result)); actual = sorted({f.code for f in result.findings}); wanted = expected.get(path.name, [])
        if result.ok or actual != wanted:
            ok = False; print(json.dumps({"actual": actual, "expected": wanted, "file": path.name, "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    if ok:
        print(f"CONFIRMED: {len(valid)} valid and {len(invalid)} invalid TemporalSlice fixtures passed exact polarity."); return 0
    return 1

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM TemporalSlice records.")
    parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files: parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda p: p.as_posix()):
        result = validate_slice(path); print(_serialize(path, result)); failed = failed or not result.ok
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
