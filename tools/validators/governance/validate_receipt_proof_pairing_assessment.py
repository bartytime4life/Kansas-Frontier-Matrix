"""Validate fixture-only receipt/proof pairing assessment candidates.

A PASS proves only local one-to-one pairing coherence for synthetic references.
It does not resolve evidence, authenticate proof, decide review or policy, change
lifecycle state, promote, release, publish, or authorize public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/receipt_proof_pairing_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/receipt_proof_pairing_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:receipt-proof-pairing:"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

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
        if key in value: raise DuplicateKeyError
        value[key] = item
    return value

def _nonfinite(_value: str) -> object: raise NonFiniteNumberError

def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file(): return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES: return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError): return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []

def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

def compute_identity_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)

def compute_assessment_id(candidate: Mapping[str, object]) -> str:
    return IDENTITY_PREFIX + compute_identity_hash(candidate).split(":", 1)[1][:24]

def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)

def bind_candidate(candidate: dict[str, object]) -> dict[str, object]:
    candidate = copy.deepcopy(candidate)
    candidate["assessment_id"] = compute_assessment_id(candidate)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    return candidate

def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (tuple(str(p) for p in error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(p) for p in error.absolute_path)) for error in errors[:100]]

def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"): return False
    try: datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError: return False
    return True

def _canonical_records(records: object, ref_field: str) -> bool:
    if not isinstance(records, list): return False
    keys = [(item.get("logical_key"), item.get(ref_field)) for item in records if isinstance(item, Mapping)]
    return len(keys) == len(records) and keys == sorted(keys)

def _parse_time(value: object) -> datetime | None:
    if not _is_utc(value): return None
    assert isinstance(value, str)
    return datetime.fromisoformat(value[:-1] + "+00:00")

def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("assessment_id") != compute_assessment_id(candidate): findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate): findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")): findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))
    receipts = candidate["receipts"]; proofs = candidate["proofs"]
    assert isinstance(receipts, list) and isinstance(proofs, list)
    if not _canonical_records(receipts, "receipt_ref"): findings.add(Finding("RECEIPTS_NOT_CANONICAL", "/receipts"))
    if not _canonical_records(proofs, "proof_ref"): findings.add(Finding("PROOFS_NOT_CANONICAL", "/proofs"))
    receipt_refs = [r["receipt_ref"] for r in receipts]; proof_refs = [p["proof_ref"] for p in proofs]
    if len(receipt_refs) != len(set(receipt_refs)): findings.add(Finding("RECEIPT_REFERENCE_DUPLICATE", "/receipts"))
    if len(proof_refs) != len(set(proof_refs)): findings.add(Finding("PROOF_REFERENCE_DUPLICATE", "/proofs"))
    subject_ref = candidate["subject_ref"]
    for idx, record in enumerate(receipts):
        if record["subject_ref"] != subject_ref: findings.add(Finding("SUBJECT_REFERENCE_MISMATCH", f"/receipts/{idx}/subject_ref"))
    for idx, record in enumerate(proofs):
        if record["subject_ref"] != subject_ref: findings.add(Finding("SUBJECT_REFERENCE_MISMATCH", f"/proofs/{idx}/subject_ref"))
    rkeys = [(r["logical_key"], r["subject_ref"]) for r in receipts]
    pkeys = [(p["logical_key"], p["subject_ref"]) for p in proofs]
    if len(rkeys) != len(set(rkeys)): findings.add(Finding("RECEIPT_LOGICAL_KEY_DUPLICATE", "/receipts"))
    if len(pkeys) != len(set(pkeys)): findings.add(Finding("PROOF_LOGICAL_KEY_DUPLICATE", "/proofs"))
    if set(rkeys) - set(pkeys): findings.add(Finding("ORPHAN_RECEIPT", "/receipts"))
    if set(pkeys) - set(rkeys): findings.add(Finding("ORPHAN_PROOF", "/proofs"))
    pairs = set(rkeys) & set(pkeys)
    if candidate["declared_pair_count"] != len(pairs): findings.add(Finding("PAIR_COUNT_MISMATCH", "/declared_pair_count"))
    by_r = {(r["logical_key"], r["subject_ref"]): r for r in receipts}
    by_p = {(p["logical_key"], p["subject_ref"]): p for p in proofs}
    for key in sorted(pairs):
        rt = _parse_time(by_r[key]["produced_at"]); pt = _parse_time(by_p[key]["produced_at"])
        if rt is None or pt is None: findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/receipts_or_proofs/produced_at"))
        elif pt < rt: findings.add(Finding("PROOF_PRECEDES_RECEIPT", f"/proofs/{key[0]}"))
    review = candidate["review"]; assert isinstance(review, Mapping)
    refs = review["review_record_refs"]; assert isinstance(refs, list)
    if refs != sorted(set(refs)): findings.add(Finding("REVIEW_REFERENCES_NOT_CANONICAL", "/review/review_record_refs"))
    if review["state"] == "COMPLETE_FOR_DECLARED_SCOPE" and not refs: findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/review_record_refs"))
    return sorted(findings)

def validate_candidate(candidate: object) -> ValidationResult:
    schema = _schema_findings(candidate)
    if schema: return ValidationResult("ERROR", tuple(schema))
    assert isinstance(candidate, dict)
    semantic = _semantic_findings(candidate)
    if semantic: return ValidationResult("DENY", tuple(semantic))
    records = list(candidate["receipts"]) + list(candidate["proofs"])
    unresolved = any(record["resolution_state"] == "UNRESOLVED" for record in records)
    if unresolved: return ValidationResult("ABSTAIN", (Finding("REFERENCE_UNRESOLVED", "/receipts_or_proofs"),))
    return ValidationResult("PASS", ())


def _resolve_parent(value: object, path: Sequence[object]) -> tuple[object, object]:
    if not path:
        raise ValueError("operation path must not be empty")
    current = value
    for part in path[:-1]:
        if isinstance(current, list) and isinstance(part, int):
            current = current[part]
        elif isinstance(current, dict) and isinstance(part, str):
            current = current[part]
        else:
            raise ValueError("operation path is invalid")
    return current, path[-1]


def _apply_operations(base: Mapping[str, object], operations: object) -> dict[str, object]:
    candidate = copy.deepcopy(dict(base))
    if not isinstance(operations, list):
        raise ValueError("operations must be a list")
    for operation in operations:
        if not isinstance(operation, Mapping):
            raise ValueError("operation must be an object")
        op = operation.get("op")
        path = operation.get("path")
        if not isinstance(path, list):
            raise ValueError("operation path must be a list")
        parent, key = _resolve_parent(candidate, path)
        if op == "set":
            value = copy.deepcopy(operation.get("value"))
            if isinstance(parent, list) and isinstance(key, int):
                parent[key] = value
            elif isinstance(parent, dict) and isinstance(key, str):
                parent[key] = value
            else:
                raise ValueError("set operation path is invalid")
        elif op == "delete":
            if isinstance(parent, list) and isinstance(key, int):
                del parent[key]
            elif isinstance(parent, dict) and isinstance(key, str):
                del parent[key]
            else:
                raise ValueError("delete operation path is invalid")
        else:
            raise ValueError("unsupported fixture operation")
    return candidate


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    base = manifest.get("base_candidate")
    if not isinstance(base, Mapping):
        raise ValueError("base_candidate must be an object")
    candidate = _apply_operations(base, entry.get("operations", []))
    candidate = bind_candidate(candidate)
    tamper = entry.get("tamper")
    if tamper == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif tamper == "assessment_id":
        candidate["assessment_id"] = IDENTITY_PREFIX + "f" * 24
    elif tamper is not None:
        raise ValueError("unsupported tamper mode")
    return candidate

def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, errors = load_json_object(path)
    if manifest is None: return [{"name":"fixture_manifest","ok":False,"observed":{"outcome":"ERROR","codes":[e.code for e in errors]}}]
    results=[]
    for entry in manifest.get("cases", []):
        try:
            candidate = materialize_fixture_case(manifest, entry)
            result = validate_candidate(candidate)
        except (KeyError, TypeError, ValueError):
            result = ValidationResult("ERROR", (Finding("FIXTURE_MATERIALIZATION_ERROR", "/cases"),))
        expected_outcome=entry.get("expected_outcome"); expected_codes=sorted(entry.get("expected_codes", []))
        results.append({"name":entry.get("name"),"ok":result.outcome==expected_outcome and result.codes==expected_codes,"expected":{"outcome":expected_outcome,"codes":expected_codes},"observed":{"outcome":result.outcome,"codes":result.codes}})
    return results

def main(argv: Sequence[str] | None = None) -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("path", nargs="?", type=Path); parser.add_argument("--fixtures", action="store_true")
    args=parser.parse_args(argv)
    if args.fixtures:
        results=validate_fixture_manifest(); print(json.dumps(results, sort_keys=True)); return 0 if all(r["ok"] for r in results) else 1
    if args.path is None: parser.error("path is required unless --fixtures is used")
    candidate, errors=load_json_object(args.path)
    result=ValidationResult("ERROR", tuple(errors)) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome":result.outcome,"findings":[{"code":f.code,"field":f.field} for f in result.findings]}, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1

if __name__ == "__main__": raise SystemExit(main())
