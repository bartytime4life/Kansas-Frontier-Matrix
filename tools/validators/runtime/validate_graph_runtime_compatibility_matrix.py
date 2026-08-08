#!/usr/bin/env python3
"""Validate the inactive graph runtime compatibility matrix without network."""
from __future__ import annotations
import argparse, json, math, sys
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
except ImportError:
    import hashlib
    def compute_spec_hash(value: Any) -> str:
        encoded=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
        return "sha256:"+hashlib.sha256(encoded).hexdigest()

MATRIX = ROOT / "control_plane/graph_runtime_compatibility_matrix.json"
SCHEMA = ROOT / "schemas/contracts/v1/runtime/graph_runtime_compatibility_matrix.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/runtime/graph_runtime_compatibility_matrix"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "graph-runtime-readiness-evidence-only"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]
    @property
    def ok(self) -> bool: return not self.findings
    @property
    def outcome(self) -> str: return "PASS" if self.ok else "ERROR"

def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out={}
    for key,value in pairs:
        if key in out: raise DuplicateKeyError(key)
        out[key]=value
    return out

def _reject(_value: str) -> None: raise NonFiniteNumberError

def _finite(value: str) -> float:
    parsed=float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str,Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file(): return None,[Finding("INPUT_NOT_FILE","/")]
        if path.stat().st_size > MAX_BYTES: return None,[Finding("INPUT_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_finite)
    except UnicodeDecodeError: return None,[Finding("JSON_INVALID","/")]
    except DuplicateKeyError: return None,[Finding("JSON_DUPLICATE_KEY","/")]
    except NonFiniteNumberError: return None,[Finding("JSON_NONFINITE_NUMBER","/")]
    except json.JSONDecodeError: return None,[Finding("JSON_INVALID","/")]
    except OSError: return None,[Finding("INPUT_READ_ERROR","/")]
    if not isinstance(value,dict): return None,[Finding("ROOT_NOT_OBJECT","/")]
    return value,[]

def _ptr(parts: Iterable[Any]) -> str:
    encoded=[str(p).replace("~","~0").replace("/","~1") for p in parts]
    return "/"+"/".join(encoded) if encoded else "/"

def _schema(value: Mapping[str,Any]) -> list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors=list(islice(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value),MAX_SCHEMA_FINDINGS+1))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE","/")]
    findings=[Finding("SCHEMA_INVALID",_ptr(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors)>MAX_SCHEMA_FINDINGS: findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED","/"))
    return findings

def _semantic(value: Mapping[str,Any]) -> list[Finding]:
    findings=[]
    declared=value.get("spec_hash")
    if isinstance(declared,str):
        subject={k:v for k,v in value.items() if k!="spec_hash"}
        if declared != compute_spec_hash(subject):
            findings.append(Finding("MATRIX_SPEC_HASH_MISMATCH","/spec_hash"))
    rows=value.get("rows") if isinstance(value.get("rows"),list) else []
    ids=[row.get("row_id") for row in rows if isinstance(row,dict)]
    if ids != sorted(ids): findings.append(Finding("ROWS_NOT_CANONICAL","/rows"))
    if len(ids)!=len(set(ids)): findings.append(Finding("ROW_ID_DUPLICATE","/rows"))
    tuples=[]
    for index,row in enumerate(rows):
        if not isinstance(row,dict): continue
        base=f"/rows/{index}"
        key=(row.get("runtime_name"),row.get("runtime_version"),row.get("jvm_major"),row.get("gds_version"),row.get("driver_version"),row.get("deployment_mode"))
        tuples.append(key)
        for field in ("evidence_refs","reason_codes"):
            items=row.get(field)
            if isinstance(items,list) and items != sorted(set(items)):
                findings.append(Finding("ARRAY_NOT_CANONICAL",f"{base}/{field}"))
        mode=row.get("deployment_mode")
        rehearsal=row.get("discovery_rehearsal_state")
        rehearsal_ref=row.get("discovery_rehearsal_ref")
        support=row.get("support_state")
        if mode=="SINGLE" and (rehearsal!="NOT_APPLICABLE" or rehearsal_ref is not None):
            findings.append(Finding("SINGLE_REHEARSAL_INVALID",f"{base}/discovery_rehearsal_state"))
        if mode=="CLUSTERED" and support!="UNSUPPORTED" and rehearsal=="NOT_APPLICABLE":
            findings.append(Finding("CLUSTER_REHEARSAL_REQUIRED",f"{base}/discovery_rehearsal_state"))
        if rehearsal=="PASSED" and not isinstance(rehearsal_ref,str):
            findings.append(Finding("REHEARSAL_REF_REQUIRED",f"{base}/discovery_rehearsal_ref"))
        if support=="SUPPORTED":
            unresolved = row.get("runtime_version")=="UNRESOLVED" or row.get("jvm_major") is None
            if unresolved or not row.get("evidence_refs"):
                findings.append(Finding("SUPPORTED_EVIDENCE_INCOMPLETE",base))
            if mode=="CLUSTERED" and (rehearsal!="PASSED" or not isinstance(rehearsal_ref,str)):
                findings.append(Finding("SUPPORTED_CLUSTER_REHEARSAL_INCOMPLETE",base))
        governance=row.get("governance")
        if isinstance(governance,dict) and any(governance.get(name) is not False for name in ("readiness_authorized","migration_authorized","release_authorized","publication_authorized")):
            findings.append(Finding("ROW_AUTHORITY_OVERREACH",f"{base}/governance"))
    if len(tuples)!=len(set(tuples)): findings.append(Finding("COMPATIBILITY_TUPLE_DUPLICATE","/rows"))
    return findings

def validate(path: Path) -> Result:
    value,findings=_read(path)
    if value is None: return Result(tuple(sorted(set(findings))))
    findings.extend(_schema(value))
    if not findings: findings.extend(_semantic(value))
    return Result(tuple(sorted(set(findings))))

def run_fixtures() -> int:
    try: cases=json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]
    except (OSError,UnicodeError,json.JSONDecodeError,KeyError): return 1
    passed=True
    for case in cases:
        result=validate(FIXTURES/case["input"])
        codes=sorted({finding.code for finding in result.findings})
        match=result.outcome==case["expected_outcome"] and codes==case["expected_findings"]
        print(json.dumps({"case_id":case["case_id"],"outcome":result.outcome,"findings":codes,"suite_match":match},sort_keys=True,separators=(",",":")))
        passed=passed and match
    return 0 if passed else 1

def main(argv: Sequence[str] | None=None) -> int:
    parser=argparse.ArgumentParser(description="Validate graph runtime compatibility matrices.")
    parser.add_argument("files",nargs="*",type=Path)
    parser.add_argument("--fixtures",action="store_true")
    args=parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    failed=False
    for path in args.files or [MATRIX]:
        result=validate(path)
        print(json.dumps({"file":path.as_posix(),"outcome":result.outcome,"findings":[{"code":f.code,"field":f.field} for f in result.findings],"scope":SCOPE},sort_keys=True,separators=(",",":")))
        failed=failed or not result.ok
    return 1 if failed else 0

if __name__=="__main__": raise SystemExit(main())
