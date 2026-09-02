#!/usr/bin/env python3
"""Validate the fixture-first KFM watcher registry without network access.

A PASS proves closed schema conformance, canonical ordering, unique identities,
registry spec_hash integrity, and exact declarative-spec byte binding only. It
creates no source, activation, execution, RAW, promotion, release, publication,
or notification authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

REGISTRY = ROOT / "control_plane/watcher_registry.json"
SCHEMA = ROOT / "schemas/contracts/v1/source/watcher_registry.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/watcher_registry"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SPEC_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "watcher-registry-control-plane-index-only"

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
    def outcome(self) -> str: return "PASS" if self.ok else "ERROR"

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

def _canonical_path(raw: Any) -> PurePosixPath | None:
    if not isinstance(raw, str) or not raw or raw.startswith("/") or "\\" in raw: return None
    path = PurePosixPath(raw)
    if str(path) != raw or any(p in {".", ".."} for p in path.parts): return None
    return path

def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""): digest.update(block)
    return "sha256:" + digest.hexdigest()

def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    declared = value.get("spec_hash")
    if isinstance(declared, str):
        subject = {k:v for k,v in value.items() if k != "spec_hash"}
        if declared != compute_spec_hash(subject): findings.append(Finding("REGISTRY_SPEC_HASH_MISMATCH", "/spec_hash"))
    watchers = value.get("watchers") if isinstance(value.get("watchers"), list) else []
    ids = [w.get("watcher_id") for w in watchers if isinstance(w, dict)]
    canonical_ids = [w.get("canonical_id") for w in watchers if isinstance(w, dict)]
    spec_paths = [w.get("spec_path") for w in watchers if isinstance(w, dict)]
    if ids != sorted(ids): findings.append(Finding("WATCHERS_NOT_CANONICAL", "/watchers"))
    if len(ids) != len(set(ids)): findings.append(Finding("WATCHER_ID_DUPLICATE", "/watchers"))
    if len(canonical_ids) != len(set(canonical_ids)): findings.append(Finding("CANONICAL_ID_DUPLICATE", "/watchers"))
    if len(spec_paths) != len(set(spec_paths)): findings.append(Finding("SPEC_PATH_DUPLICATE", "/watchers"))
    for index, watcher in enumerate(watchers):
        if not isinstance(watcher, dict): continue
        base = f"/watchers/{index}"
        caps = watcher.get("capabilities")
        if isinstance(caps, list) and caps != sorted(set(caps)): findings.append(Finding("CAPABILITIES_NOT_CANONICAL", f"{base}/capabilities"))
        outputs = watcher.get("outputs")
        if isinstance(outputs, list):
            expected = sorted(outputs, key=lambda item: (item.get("output_type",""), item.get("target_zone",""), item.get("contract_ref",""), item.get("schema_ref","")) if isinstance(item, dict) else ("", "", "", ""))
            if outputs != expected: findings.append(Finding("OUTPUTS_NOT_CANONICAL", f"{base}/outputs"))
        relative = _canonical_path(watcher.get("spec_path"))
        if relative is None or not relative.parts or relative.parts[0] != "pipeline_specs":
            findings.append(Finding("SPEC_PATH_INVALID", f"{base}/spec_path")); continue
        candidate = ROOT.joinpath(*relative.parts)
        try:
            if candidate.is_symlink() or not candidate.is_file(): findings.append(Finding("SPEC_FILE_MISSING", f"{base}/spec_path")); continue
            if candidate.stat().st_size > MAX_SPEC_BYTES: findings.append(Finding("SPEC_FILE_TOO_LARGE", f"{base}/spec_path")); continue
            actual = _hash_file(candidate)
        except OSError:
            findings.append(Finding("SPEC_FILE_UNREADABLE", f"{base}/spec_path")); continue
        if watcher.get("spec_sha256") != actual: findings.append(Finding("SPEC_FILE_HASH_MISMATCH", f"{base}/spec_sha256"))
        governance = watcher.get("governance")
        if isinstance(governance, dict) and any(governance.get(name) is not False for name in ("raw_admission_authorized","promotion_authorized","release_authorized","publication_authorized")):
            findings.append(Finding("WATCHER_AUTHORITY_OVERREACH", f"{base}/governance"))
    return findings

def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None: return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(value))
    if not findings: findings.extend(_semantic(value))
    return ValidationResult(tuple(sorted(set(findings))))

def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps({'file':path.as_posix(),'outcome':result.outcome,'findings':[{'code':f.code,'field':f.field} for f in result.findings],'scope':SCOPE}, sort_keys=True, separators=(',',':'))

def run_fixtures() -> int:
    try: manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError): return 1
    passed = True
    for case in manifest['cases']:
        path = FIXTURES / case['input']; result = validate(path)
        codes = sorted({f.code for f in result.findings})
        match = result.outcome == case['expected_outcome'] and codes == case['expected_findings']
        print(json.dumps({'case_id':case['case_id'],'outcome':result.outcome,'findings':codes,'suite_match':match}, sort_keys=True, separators=(',',':')))
        passed = passed and match
    return 0 if passed else 1

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Validate KFM watcher registry projections.')
    parser.add_argument('files', nargs='*', type=Path); parser.add_argument('--fixtures', action='store_true')
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error('--fixtures cannot be combined with files')
        return run_fixtures()
    files = args.files or [REGISTRY]
    failed = False
    for path in sorted(files, key=lambda p:p.as_posix()):
        result = validate(path); print(_serialize(path, result)); failed = failed or not result.ok
    return 1 if failed else 0

if __name__ == '__main__': raise SystemExit(main())
