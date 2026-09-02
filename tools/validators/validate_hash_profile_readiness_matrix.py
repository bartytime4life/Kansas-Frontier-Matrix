#!/usr/bin/env python3
"""Validate the inactive KFM hash-profile readiness matrix without network access.

PASS proves closed schema shape, exact matrix spec_hash, canonical ordering, and
bounded role/algorithm/prefix/canonicalization readiness invariants only. It
does not adopt a hash policy, activate an algorithm, authorize signing, migrate
stored digests, release, or publish.
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

MATRIX = ROOT / "control_plane/hash_profile_readiness_matrix.json"
SCHEMA = ROOT / "schemas/contracts/v1/common/hash_profile_readiness_matrix.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/common/hash_profile_readiness_matrix"
CASES = FIXTURES / "cases.json"
MAX_JSON_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "hash-profile-readiness-evidence-only"

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
    def outcome(self) -> str: return "PASS" if self.ok else "ERROR"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise DuplicateKeyError(key)
        out[key] = value
    return out

def _reject(_value: str) -> None: raise NonFiniteNumberError

def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(fd).st_mode): return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(fd, "rb") as stream:
                fd = -1; raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if fd >= 0: os.close(fd)
        if len(raw) > MAX_JSON_BYTES: return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique, parse_constant=_reject, parse_float=_finite)
    except FileNotFoundError: return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except OSError: return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []

def _ptr(parts: Iterable[Any]) -> str:
    encoded = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [Finding("SCHEMA_INVALID", _ptr(e.absolute_path)) for e in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS: findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings

def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    declared = value.get("spec_hash")
    if isinstance(declared, str):
        subject = {k: v for k, v in value.items() if k != "spec_hash"}
        if declared != compute_spec_hash(subject):
            findings.append(Finding("MATRIX_SPEC_HASH_MISMATCH", "/spec_hash"))

    profiles = value.get("profiles") if isinstance(value.get("profiles"), list) else []
    profile_ids = [p.get("profile_id") for p in profiles if isinstance(p, dict)]
    roles = [p.get("hash_role") for p in profiles if isinstance(p, dict)]
    if profile_ids != sorted(profile_ids):
        findings.append(Finding("PROFILES_NOT_CANONICAL", "/profiles"))
    if len(profile_ids) != len(set(profile_ids)):
        findings.append(Finding("PROFILE_ID_DUPLICATE", "/profiles"))
    if len(roles) != len(set(roles)):
        findings.append(Finding("HASH_ROLE_DUPLICATE", "/profiles"))

    expected_prefix = {"SHA-256": "sha256:", "BLAKE3": "blake3:"}
    expected_canonicalization = {
        "spec_hash": "RFC8785-JCS",
        "descriptor_hash": "RFC8785-JCS",
        "content_hash": "RAW-BYTES",
        "root_hash": "ORDERED-FILESET-V1",
        "range_hash": "BAO-TREE-V1",
        "signature_digest": "DSSE-PAYLOAD-BYTES",
    }
    baseline_count = 0
    for index, profile in enumerate(profiles):
        if not isinstance(profile, dict): continue
        base = f"/profiles/{index}"
        families = profile.get("object_families")
        if isinstance(families, list) and families != sorted(set(families)):
            findings.append(Finding("OBJECT_FAMILIES_NOT_CANONICAL", f"{base}/object_families"))
        algorithm = profile.get("algorithm")
        if profile.get("digest_prefix") != expected_prefix.get(algorithm):
            findings.append(Finding("ALGORITHM_PREFIX_MISMATCH", f"{base}/digest_prefix"))
        role = profile.get("hash_role")
        if profile.get("canonicalization_profile") != expected_canonicalization.get(role):
            findings.append(Finding("ROLE_CANONICALIZATION_MISMATCH", f"{base}/canonicalization_profile"))
        if role == "signature_digest" and profile.get("signature_required") is not True:
            findings.append(Finding("SIGNATURE_ROLE_REQUIREMENT_INVALID", f"{base}/signature_required"))
        if role != "signature_digest" and profile.get("signature_required") is not False:
            findings.append(Finding("SIGNATURE_REQUIREMENT_OVERREACH", f"{base}/signature_required"))
        if profile.get("activation_state") == "BASELINE":
            baseline_count += 1
            if role != "spec_hash":
                findings.append(Finding("BASELINE_ROLE_NOT_AUTHORIZED", f"{base}/hash_role"))
            if profile.get("implementation_state") != "EXECUTABLE":
                findings.append(Finding("UNAVAILABLE_PROFILE_ACTIVE", f"{base}/implementation_state"))
            if not (
                algorithm == "SHA-256"
                and profile.get("digest_prefix") == "sha256:"
                and profile.get("canonicalization_profile") == "RFC8785-JCS"
                and profile.get("proof_kind") == "SEMANTIC_IDENTITY"
            ):
                findings.append(Finding("BASELINE_SPEC_PROFILE_INVALID", base))
        if profile.get("implementation_state") == "UNAVAILABLE" and profile.get("activation_state") != "INACTIVE":
            code = Finding("UNAVAILABLE_PROFILE_ACTIVE", f"{base}/implementation_state")
            if code not in findings: findings.append(code)
        if role == "range_hash" and not (
            algorithm == "BLAKE3"
            and profile.get("canonicalization_profile") == "BAO-TREE-V1"
            and profile.get("activation_state") == "INACTIVE"
        ):
            findings.append(Finding("RANGE_PROFILE_NOT_INACTIVE_BAO", base))
    if baseline_count != 1:
        findings.append(Finding("BASELINE_PROFILE_COUNT_INVALID", "/profiles"))
    return findings

def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None: return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(value))
    if not findings: findings.extend(_semantic(value))
    return ValidationResult(tuple(sorted(set(findings))))

def _replace(candidate: Any, pointer: str, value: Any) -> None:
    if not pointer.startswith("/") or pointer == "/": raise ValueError("invalid patch pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    current = candidate
    for raw in parts[:-1]:
        current = current[int(raw)] if isinstance(current, list) else current[raw]
    key = parts[-1]
    if isinstance(current, list): current[int(key)] = value
    else: current[key] = value

def run_fixtures() -> int:
    try:
        base = json.loads(MATRIX.read_text(encoding="utf-8"))
        suite = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError): return 1
    passed = True
    for case in suite["cases"]:
        candidate = copy.deepcopy(base)
        for mutation in case["mutations"]:
            if mutation.get("op") != "replace": return 1
            _replace(candidate, mutation["path"], mutation["value"])
        if case.get("recompute_spec_hash"):
            candidate["spec_hash"] = compute_spec_hash({k: v for k, v in candidate.items() if k != "spec_hash"})
        temp = FIXTURES / ".fixture-candidate.json"
        temp.write_text(json.dumps(candidate, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        try: result = validate(temp)
        finally: temp.unlink(missing_ok=True)
        codes = sorted({f.code for f in result.findings})
        match = result.outcome == case["expected_outcome"] and codes == case["expected_findings"]
        print(json.dumps({"case_id":case["case_id"],"outcome":result.outcome,"findings":codes,"suite_match":match}, sort_keys=True, separators=(",", ":")))
        passed = passed and match
    return 0 if passed else 1

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    files = args.files or [MATRIX]
    failed = False
    for path in sorted(files, key=lambda p: p.as_posix()):
        result = validate(path)
        print(json.dumps({"file":path.as_posix(),"outcome":result.outcome,"findings":[{"code":f.code,"field":f.field} for f in result.findings],"scope":SCOPE}, sort_keys=True, separators=(",", ":")))
        failed = failed or not result.ok
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
