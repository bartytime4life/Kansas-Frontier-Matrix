#!/usr/bin/env python3
"""Validate fixture-only proof-session handoff candidates.

PASS means only that a bounded experiment handoff is locally coherent and
explicit about its proof boundary. It does not resolve evidence, decide policy
or review, establish proof, or grant promotion, release, deployment,
publication, or public-use authority.
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

REPO_ROOT=Path(__file__).resolve().parents[3]
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/governance/proof_session_handoff.schema.json"
FIXTURE_PATH=REPO_ROOT/"fixtures/contracts/v1/governance/proof_session_handoff/cases.json"
MAX_FILE_BYTES=1_048_576
ABSTAIN_CODES={"PROOF_SESSION_SUPPORT_UNRESOLVED","PROOF_SESSION_SUPPORT_INCOMPLETE","PROOF_SESSION_VALIDATION_NOT_RUN"}
REF_ARRAY_PATHS=(
 "/support/source_descriptor_refs","/support/evidence_refs","/support/evidence_bundle_refs","/support/policy_question_refs",
 "/work_products/contract_refs","/work_products/schema_refs","/work_products/fixture_refs","/work_products/validator_refs","/work_products/test_refs",
 "/results/validation_report_refs","/results/demonstrated_surfaces","/results/unresolved_items",
)

class DuplicateKeyError(ValueError):pass
class NonFiniteNumberError(ValueError):pass

@dataclass(frozen=True,order=True)
class Finding:
    code:str
    field:str

@dataclass(frozen=True)
class ValidationResult:
    outcome:str
    findings:tuple[Finding,...]
    assessment_state:str|None=None
    @property
    def codes(self)->list[str]:return sorted({x.code for x in self.findings})

def _pairs(items:list[tuple[str,object]])->dict[str,object]:
    out={}
    for k,v in items:
        if k in out:raise DuplicateKeyError
        out[k]=v
    return out

def _nonfinite(_value:str)->object:raise NonFiniteNumberError

def _finite_float(value:str)->float:
    parsed=float(value)
    if not math.isfinite(parsed):raise NonFiniteNumberError
    return parsed

def load_json_object(path:Path)->tuple[dict[str,object]|None,list[Finding]]:
    try:
        if path.is_symlink():return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file():return None,[Finding("FILE_NOT_FOUND","/")]
        if path.stat().st_size>MAX_FILE_BYTES:return None,[Finding("FILE_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_pairs,parse_constant=_nonfinite,parse_float=_finite_float)
    except DuplicateKeyError:return None,[Finding("JSON_DUPLICATE_KEY","/")]
    except NonFiniteNumberError:return None,[Finding("JSON_NONFINITE_NUMBER","/")]
    except (OSError,UnicodeError,json.JSONDecodeError,RecursionError,ValueError):return None,[Finding("JSON_INVALID","/")]
    if not isinstance(value,dict):return None,[Finding("ROOT_NOT_OBJECT","/")]
    return value,[]

def canonical_hash(value:object)->str:
    payload=json.dumps(value,ensure_ascii=False,allow_nan=False,sort_keys=True,separators=(",",":")).encode("utf-8")
    return "sha256:"+hashlib.sha256(payload).hexdigest()

def canonical_identity(candidate:Mapping[str,object])->tuple[str,str]:
    subject=copy.deepcopy(dict(candidate));subject.pop("profile_spec_hash",None);subject.pop("session_id",None)
    digest=canonical_hash(subject)
    return digest,"kfm:proof-session:"+digest.removeprefix("sha256:")[:24]

def _schema_findings(candidate:object)->list[Finding]:
    try:
        schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"));Draft202012Validator.check_schema(schema)
        errors=sorted(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(candidate),key=lambda e:(list(e.absolute_path),str(e.validator)))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):return [Finding("SCHEMA_UNAVAILABLE","/")]
    return [Finding("SCHEMA_INVALID","/"+"/".join(str(x) for x in e.absolute_path)) for e in errors[:100]]

def _utc(value:object)->datetime|None:
    if not isinstance(value,str) or not value.endswith("Z"):return None
    try:return datetime.fromisoformat(value[:-1]+"+00:00")
    except ValueError:return None

def _canonical_strings(value:object)->bool:
    return isinstance(value,list) and all(isinstance(x,str) for x in value) and value==sorted(set(value))

def _get_pointer(candidate:Mapping[str,object],pointer:str)->object:
    current:object=candidate
    for part in pointer.strip("/").split("/"):
        assert isinstance(current,Mapping);current=current[part]
    return current

def _semantic_findings(candidate:Mapping[str,object])->list[Finding]:
    findings:set[Finding]=set()
    expected_hash,expected_id=canonical_identity(candidate)
    if candidate.get("profile_spec_hash")!=expected_hash:findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH","/profile_spec_hash"))
    if candidate.get("session_id")!=expected_id:findings.add(Finding("PROOF_SESSION_ID_MISMATCH","/session_id"))

    session=candidate["session"];scope=candidate["scope"];support=candidate["support"];results=candidate["results"];handoff=candidate["handoff"];claims=candidate["session_claims"]
    assert all(isinstance(x,Mapping) for x in (session,scope,support,results,handoff,claims))
    started=_utc(session["started_at"]);completed=_utc(session["completed_at"])
    if started is None or completed is None or completed<started:findings.add(Finding("PROOF_SESSION_TIME_ORDER_INVALID","/session"))

    for pointer in REF_ARRAY_PATHS:
        if not _canonical_strings(_get_pointer(candidate,pointer)):
            findings.add(Finding("PROOF_SESSION_ARRAY_NOT_CANONICAL",pointer))

    posture=support["support_posture"]
    if posture=="UNRESOLVED":findings.add(Finding("PROOF_SESSION_SUPPORT_UNRESOLVED","/support/support_posture"))
    elif not support["source_descriptor_refs"] or not support["evidence_refs"] or not support["evidence_bundle_refs"]:
        findings.add(Finding("PROOF_SESSION_SUPPORT_INCOMPLETE","/support"))
    place_kind=scope["place_scope"]["kind"]
    if posture=="SYNTHETIC_ONLY" and place_kind!="SYNTHETIC":
        findings.add(Finding("SYNTHETIC_SUPPORT_FOR_REAL_SCOPE_DENIED","/scope/place_scope/kind"))

    time_scope=scope["time_scope"];kind=time_scope["kind"];start=time_scope["start"];end=time_scope["end"]
    if kind=="FIXTURE_ONLY":
        if start is not None or end is not None:findings.add(Finding("PROOF_SESSION_TIME_SCOPE_INVALID","/scope/time_scope"))
    elif kind in {"VALID_INTERVAL","OBSERVATION_TIME"}:
        start_dt=_utc(start);end_dt=_utc(end)
        if start_dt is None or end_dt is None or end_dt<start_dt:findings.add(Finding("PROOF_SESSION_TIME_SCOPE_INVALID","/scope/time_scope"))

    validation_outcome=results["validation_outcome"]
    if validation_outcome=="NOT_RUN":findings.add(Finding("PROOF_SESSION_VALIDATION_NOT_RUN","/results/validation_outcome"))
    surfaces=results["demonstrated_surfaces"]
    if "NONE" in surfaces and len(surfaces)>1:findings.add(Finding("PROOF_SESSION_SURFACES_INCOHERENT","/results/demonstrated_surfaces"))
    disposition=handoff["disposition"]
    if validation_outcome in {"DENY","ERROR"} and disposition not in {"HOLD","STOP"}:
        findings.add(Finding("PROOF_SESSION_DISPOSITION_INCOHERENT","/handoff/disposition"))
    if validation_outcome in {"NOT_RUN","ABSTAIN"} and disposition=="CONTINUE_REVIEW":
        findings.add(Finding("PROOF_SESSION_DISPOSITION_INCOHERENT","/handoff/disposition"))

    if claims["proof_established"]:findings.add(Finding("PROOF_SESSION_PROOF_CLAIM_DENIED","/session_claims/proof_established"))
    if claims["release_ready"]:findings.add(Finding("PROOF_SESSION_RELEASE_READY_CLAIM_DENIED","/session_claims/release_ready"))
    if claims["public_use_ready"]:findings.add(Finding("PROOF_SESSION_PUBLIC_USE_CLAIM_DENIED","/session_claims/public_use_ready"))
    return sorted(findings)

def validate_candidate(candidate:object)->ValidationResult:
    schema_findings=_schema_findings(candidate)
    if schema_findings:return ValidationResult("ERROR",tuple(schema_findings),None)
    assert isinstance(candidate,dict)
    findings=_semantic_findings(candidate);codes={x.code for x in findings}
    if not codes:outcome="PASS"
    elif codes<=ABSTAIN_CODES:outcome="ABSTAIN"
    else:outcome="DENY"
    return ValidationResult(outcome,tuple(findings),"REVIEW_REQUIRED" if outcome=="PASS" else None)

def _merge_patch(base:object,patch:object)->object:
    if not isinstance(patch,dict):return copy.deepcopy(patch)
    target=copy.deepcopy(base) if isinstance(base,dict) else {}
    for k,v in patch.items():target[k]=_merge_patch(target.get(k),v)
    return target

def materialize_fixture_case(manifest:Mapping[str,object],entry:Mapping[str,object])->dict[str,object]:
    candidate=_merge_patch(manifest["base_candidate"],entry.get("patch",{}));assert isinstance(candidate,dict)
    candidate["profile_spec_hash"],candidate["session_id"]=canonical_identity(candidate)
    if entry.get("tamper")=="profile_hash":candidate["profile_spec_hash"]="sha256:"+"f"*64
    if entry.get("tamper")=="session_id":candidate["session_id"]="kfm:proof-session:"+"f"*24
    return candidate

def load_fixtures()->dict[str,object]:
    value,findings=load_json_object(FIXTURE_PATH)
    if value is None:raise ValueError(findings)
    return value

def validate_fixture_manifest()->list[dict[str,object]]:
    manifest=load_fixtures();out=[]
    for entry in manifest["cases"]:
        result=validate_candidate(materialize_fixture_case(manifest,entry));observed={"outcome":result.outcome,"codes":result.codes};expected=entry["expected"]
        out.append({"name":entry["name"],"ok":observed==expected,"expected":expected,"observed":observed})
    return out

def _serialize(result:ValidationResult)->str:
    return json.dumps({"assessment_state":result.assessment_state,"authority":{"establishes_proof":False,"authorizes_release":False,"publishes":False},"codes":result.codes,"outcome":result.outcome},sort_keys=True,separators=(",",":"))

def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group(required=True);group.add_argument("--fixtures",action="store_true");group.add_argument("--input",type=Path);args=parser.parse_args(argv)
    if args.fixtures:
        results=validate_fixture_manifest();print(json.dumps(results,indent=2,sort_keys=True));return 0 if all(x["ok"] for x in results) else 1
    candidate,findings=load_json_object(args.input);result=ValidationResult("ERROR",tuple(findings),None) if candidate is None else validate_candidate(candidate);print(_serialize(result));return 0 if result.outcome=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
