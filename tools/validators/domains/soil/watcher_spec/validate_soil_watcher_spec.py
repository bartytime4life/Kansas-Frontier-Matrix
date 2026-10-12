#!/usr/bin/env python3
"""Validate the inactive fixture-only SSURGO/gNATSGO watcher specification."""
from __future__ import annotations
import argparse, json, math, sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[5]
HASH_SRC=ROOT/"packages/hashing/src"
if str(HASH_SRC) not in sys.path: sys.path.insert(0,str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError:
    import hashlib
    def compute_spec_hash(value:Any)->str:
        raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
        return "sha256:"+hashlib.sha256(raw).hexdigest()

SPEC=ROOT/"pipeline_specs/watchers/soil_ssurgo_gnatsgo.json"
SCHEMA=ROOT/"schemas/contracts/v1/domains/soil/soil_watcher_spec.schema.json"
FIXTURES=ROOT/"fixtures/domains/soil/watcher_spec"
MANIFEST=FIXTURES/"expected_findings_manifest.json"
MAX_BYTES=2*1024*1024
MAX_SCHEMA_FINDINGS=100
SCOPE="soil-watcher-spec-inactive-fixture-only"
PHASES=["SNAPSHOT","NORMALIZE","HARD_QA","MATERIALITY","PACKAGE","RECEIPT"]
QA_REQUIRED={"SOIL_GEOMETRY_VALIDITY","SOIL_REFERENTIAL_INTEGRITY","SOIL_REQUIRED_KEYS","SOIL_SCHEMA_CONFORMANCE"}
SOURCE_ROLES={"GNATSGO":"GRIDDED_DERIVATIVE_SOIL","SSURGO":"AUTHORITATIVE_STATIC_SOIL_SURVEY"}
MATERIALITY={"GNATSGO":("NRCS_GNATSGO_GRID_V1","DIGEST_OR_GRID_SCHEMA_CHANGE"),"SSURGO":("NRCS_SSURGO_TABULAR_V1","DIGEST_OR_KEYED_ROW_CHANGE")}

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding:
    code:str
    field:str
@dataclass(frozen=True)
class Result:
    findings:tuple[Finding,...]
    @property
    def ok(self)->bool:return not self.findings
    @property
    def outcome(self)->str:return "PASS" if self.ok else "ERROR"

def _unique(pairs:list[tuple[str,Any]])->dict[str,Any]:
    out={}
    for key,value in pairs:
        if key in out:raise DuplicateKeyError(key)
        out[key]=value
    return out
def _reject(_value:str)->None:raise NonFiniteNumberError
def _finite(value:str)->float:
    parsed=float(value)
    if not math.isfinite(parsed):raise NonFiniteNumberError
    return parsed
def _read(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
    try:
        if path.is_symlink():return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file():return None,[Finding("INPUT_NOT_FILE","/")]
        if path.stat().st_size>MAX_BYTES:return None,[Finding("INPUT_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_finite)
    except UnicodeDecodeError:return None,[Finding("JSON_INVALID","/")]
    except DuplicateKeyError:return None,[Finding("JSON_DUPLICATE_KEY","/")]
    except NonFiniteNumberError:return None,[Finding("JSON_NONFINITE_NUMBER","/")]
    except json.JSONDecodeError:return None,[Finding("JSON_INVALID","/")]
    except OSError:return None,[Finding("INPUT_READ_ERROR","/")]
    if not isinstance(value,dict):return None,[Finding("ROOT_NOT_OBJECT","/")]
    return value,[]
def _ptr(parts:Iterable[Any])->str:
    encoded=[str(p).replace("~","~0").replace("/","~1") for p in parts]
    return "/"+"/".join(encoded) if encoded else "/"
def _schema(value:Mapping[str,Any])->list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding="utf-8"));Draft202012Validator.check_schema(schema)
        errors=list(islice(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value),MAX_SCHEMA_FINDINGS+1))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):return [Finding("SCHEMA_UNAVAILABLE","/")]
    findings=[Finding("SCHEMA_INVALID",_ptr(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors)>MAX_SCHEMA_FINDINGS:findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED","/"))
    return findings
def _semantic(value:Mapping[str,Any])->list[Finding]:
    findings=[]
    declared=value.get("spec_hash")
    if isinstance(declared,str) and declared!=compute_spec_hash({k:v for k,v in value.items() if k!="spec_hash"}):
        findings.append(Finding("SOIL_SPEC_HASH_MISMATCH","/spec_hash"))
    sources=value.get("source_scope") if isinstance(value.get("source_scope"),list) else []
    source_ids=[item.get("source_id") for item in sources if isinstance(item,dict)]
    if source_ids!=sorted(source_ids):findings.append(Finding("SOIL_SOURCE_SCOPE_NOT_CANONICAL","/source_scope"))
    if len(source_ids)!=len(set(source_ids)):findings.append(Finding("SOIL_SOURCE_ID_DUPLICATE","/source_scope"))
    families=[]
    for index,item in enumerate(sources):
        if not isinstance(item,dict):continue
        family=item.get("source_family");families.append(family)
        if item.get("support_type")!=SOURCE_ROLES.get(family):findings.append(Finding("SOIL_SOURCE_ROLE_INVALID",f"/source_scope/{index}/support_type"))
        modes=item.get("acquisition_modes")
        if isinstance(modes,list) and modes!=sorted(set(modes)):findings.append(Finding("SOIL_ACQUISITION_MODES_NOT_CANONICAL",f"/source_scope/{index}/acquisition_modes"))
        ref=item.get("source_registry_ref")
        if not isinstance(ref,str) or not ref.startswith("data/registry/sources/soil/"):findings.append(Finding("SOIL_SOURCE_REGISTRY_REF_INVALID",f"/source_scope/{index}/source_registry_ref"))
    if set(families)!=set(SOURCE_ROLES):findings.append(Finding("SOIL_SOURCE_FAMILY_SET_INVALID","/source_scope"))
    phases=value.get("pipeline_phases") if isinstance(value.get("pipeline_phases"),list) else []
    if [item.get("phase") for item in phases if isinstance(item,dict)]!=PHASES:findings.append(Finding("SOIL_PHASE_ORDER_INVALID","/pipeline_phases"))
    qa=value.get("qa_rules") if isinstance(value.get("qa_rules"),list) else []
    qa_ids=[item.get("rule_id") for item in qa if isinstance(item,dict)]
    if qa_ids!=sorted(qa_ids):findings.append(Finding("SOIL_QA_RULES_NOT_CANONICAL","/qa_rules"))
    if set(qa_ids)!=QA_REQUIRED:findings.append(Finding("SOIL_QA_RULES_INCOMPLETE","/qa_rules"))
    materiality=value.get("materiality_rules") if isinstance(value.get("materiality_rules"),list) else []
    profile_ids=[item.get("profile_id") for item in materiality if isinstance(item,dict)]
    if profile_ids!=sorted(profile_ids):findings.append(Finding("SOIL_MATERIALITY_NOT_CANONICAL","/materiality_rules"))
    seen={}
    for index,item in enumerate(materiality):
        if not isinstance(item,dict):continue
        family=item.get("source_family")
        if family in seen:findings.append(Finding("SOIL_MATERIALITY_FAMILY_DUPLICATE","/materiality_rules"))
        seen[family]=item
        if (item.get("profile_id"),item.get("rule_kind"))!=MATERIALITY.get(family):findings.append(Finding("SOIL_MATERIALITY_PROFILE_INVALID",f"/materiality_rules/{index}"))
    if set(seen)!=set(MATERIALITY):findings.append(Finding("SOIL_MATERIALITY_PROFILE_MISSING","/materiality_rules"))
    outputs=value.get("outputs") if isinstance(value.get("outputs"),list) else []
    expected=sorted(outputs,key=lambda item:(item.get("output_type",""),item.get("target_zone","")) if isinstance(item,dict) else ("",""))
    if outputs!=expected:findings.append(Finding("SOIL_OUTPUTS_NOT_CANONICAL","/outputs"))
    if any(isinstance(item,dict) and item.get("target_zone") not in {"WORK","QUARANTINE"} for item in outputs):findings.append(Finding("SOIL_OUTPUT_AUTHORITY_OVERREACH","/outputs"))
    receipts=value.get("receipt_expectations")
    if isinstance(receipts,list) and receipts!=sorted(set(receipts)):findings.append(Finding("SOIL_RECEIPTS_NOT_CANONICAL","/receipt_expectations"))
    governance=value.get("governance")
    if isinstance(governance,dict) and any(governance.get(name) is not False for name in ("source_activation_authorized","network_authorized","execution_authorized","raw_admission_authorized","promotion_authorized","release_authorized","publication_authorized")):
        findings.append(Finding("SOIL_WATCHER_AUTHORITY_OVERREACH","/governance"))
    return findings
def validate(path:Path)->Result:
    value,findings=_read(path)
    if value is None:return Result(tuple(sorted(set(findings))))
    findings.extend(_schema(value))
    if not findings:findings.extend(_semantic(value))
    return Result(tuple(sorted(set(findings))))
def run_fixtures()->int:
    try:cases=json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]
    except (OSError,UnicodeError,json.JSONDecodeError,KeyError):return 1
    passed=True
    for case in cases:
        result=validate(FIXTURES/case["input"]);codes=sorted({item.code for item in result.findings})
        match=result.outcome==case["expected_outcome"] and codes==case["expected_findings"]
        print(json.dumps({"case_id":case["case_id"],"outcome":result.outcome,"findings":codes,"suite_match":match},sort_keys=True,separators=(",",":")))
        passed=passed and match
    return 0 if passed else 1
def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description="Validate inactive soil watcher specifications.")
    parser.add_argument("files",nargs="*",type=Path);parser.add_argument("--fixtures",action="store_true");args=parser.parse_args(argv)
    if args.fixtures:
        if args.files:parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    failed=False
    for path in args.files or [SPEC]:
        result=validate(path);print(json.dumps({"file":path.as_posix(),"outcome":result.outcome,"findings":[{"code":f.code,"field":f.field} for f in result.findings],"scope":SCOPE},sort_keys=True,separators=(",",":")));failed=failed or not result.ok
    return 1 if failed else 0
if __name__=="__main__":raise SystemExit(main())
