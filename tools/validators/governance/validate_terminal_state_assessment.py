#!/usr/bin/env python3
"""Validate fixture-only TerminalStateAssessment records."""
from __future__ import annotations
import argparse, copy, json, math, sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[3]
HASH_SRC=ROOT/"packages/hashing/src"
if str(HASH_SRC) not in sys.path: sys.path.insert(0,str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash
SCHEMA=ROOT/"schemas/contracts/v1/governance/terminal_state_assessment.schema.json"
FIXTURES=ROOT/"fixtures/contracts/v1/governance/terminal_state_assessment/cases.json"
MAX_BYTES=4*1024*1024; MAX_FINDINGS=100
PREFIX="kfm:terminal-state-assessment:"
NON_EFFECTS=("no_pull_request_mutation","no_ready_transition","no_merge","no_settings_change","no_history_rewrite")
@dataclass(frozen=True,order=True)
class Finding: code:str; path:str
@dataclass(frozen=True)
class Result: outcome:str; findings:tuple[Finding,...]
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
def _unique(pairs):
 d={}
 for k,v in pairs:
  if k in d: raise DuplicateKeyError
  d[k]=v
 return d
def _reject(_): raise NonFiniteNumberError
def _float(v):
 x=float(v)
 if not math.isfinite(x): raise NonFiniteNumberError
 return x
def _ptr(parts:Iterable[Any])->str:
 p=[str(x).replace("~","~0").replace("/","~1") for x in parts]
 return "/"+"/".join(p) if p else "/"
def _time(v:object):
 if not isinstance(v,str): return None
 try: return datetime.fromisoformat(v[:-1]+"+00:00" if v.endswith("Z") else v)
 except ValueError: return None
def _read(path:Path):
 try:
  if path.is_symlink(): return None,(Finding("TERMINAL_INPUT_SYMLINK_DENIED","/"),)
  if not path.is_file(): return None,(Finding("TERMINAL_INPUT_NOT_FILE","/"),)
  if path.stat().st_size>MAX_BYTES: return None,(Finding("TERMINAL_INPUT_TOO_LARGE","/"),)
  v=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_float)
 except DuplicateKeyError: return None,(Finding("TERMINAL_JSON_DUPLICATE_KEY","/"),)
 except NonFiniteNumberError: return None,(Finding("TERMINAL_JSON_NONFINITE_NUMBER","/"),)
 except (OSError,UnicodeError,json.JSONDecodeError): return None,(Finding("TERMINAL_JSON_INVALID","/"),)
 if not isinstance(v,dict): return None,(Finding("TERMINAL_ROOT_NOT_OBJECT","/"),)
 return v,()
def canonical_identity(v:Mapping[str,Any]):
 s={k:x for k,x in v.items() if k not in {"assessment_id","spec_hash"}}
 h=compute_spec_hash(s); return h,PREFIX+h.split(":",1)[1][:24]
def recompute_result(v:Mapping[str,Any]):
 a=v["authorization"]; o=v["observed"]; state=a["authorization_state"]
 if state=="MISSING": return {"outcome":"HOLD","reason_codes":["AUTHORIZATION_MISSING"]}
 if state=="EXPIRED": return {"outcome":"HOLD","reason_codes":["AUTHORIZATION_EXPIRED"]}
 if o["state"]=="UNKNOWN": return {"outcome":"HOLD","reason_codes":["HOST_STATE_UNKNOWN"]}
 allowed={"DRAFT_PR":{"OPEN_DRAFT"},"READY_PR":{"OPEN_DRAFT","OPEN_READY","CLOSED_UNMERGED"}}[a["terminal_ceiling"]]
 if o["state"] not in allowed: return {"outcome":"DIVERGENCE","reason_codes":["TERMINAL_STATE_DIVERGENCE"]}
 return {"outcome":"WITHIN_CEILING","reason_codes":["TERMINAL_STATE_WITHIN_CEILING"]}
def _schema(v):
 try:
  s=json.loads(SCHEMA.read_text()); Draft202012Validator.check_schema(s)
  errors=list(islice(Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(v),MAX_FINDINGS+1))
 except Exception: return (Finding("TERMINAL_SCHEMA_UNAVAILABLE","/"),)
 errors.sort(key=lambda e:(_ptr(e.absolute_path),str(e.validator)))
 out=[Finding("TERMINAL_SCHEMA_INVALID",_ptr(e.absolute_path)) for e in errors[:MAX_FINDINGS]]
 if len(errors)>MAX_FINDINGS: out.append(Finding("TERMINAL_SCHEMA_FINDINGS_TRUNCATED","/"))
 return tuple(sorted(set(out)))
def _semantic(v):
 out=set(); a=v["authorization"]; o=v["observed"]
 try: eh,eid=canonical_identity(v)
 except CanonicalizationFailure: out.add(Finding("TERMINAL_CANONICALIZATION_ERROR","/"))
 else:
  if v["spec_hash"]!=eh: out.add(Finding("TERMINAL_SPEC_HASH_MISMATCH","/spec_hash"))
  if v["assessment_id"]!=eid: out.add(Finding("TERMINAL_ID_MISMATCH","/assessment_id"))
 if a["authorization_state"]!="MISSING" and a["head_sha"]!=o["head_sha"]: out.add(Finding("TERMINAL_HEAD_SHA_MISMATCH","/observed/head_sha"))
 ev=o["events"]; times=[_time(x.get("at")) for x in ev]
 if any(x is None for x in times) or times!=sorted(times) or any(x>_time(v["evaluated_at"]) for x in times if x): out.add(Finding("TERMINAL_EVENT_ORDER_INVALID","/observed/events"))
 types=[x["type"] for x in ev]
 state=o["state"]
 ok=(state=="OPEN_DRAFT" and "OPENED_DRAFT" in types and not any(x in types for x in ["READY_FOR_REVIEW","CLOSED","MERGED"])) or (state=="OPEN_READY" and "READY_FOR_REVIEW" in types and "MERGED" not in types and "CLOSED" not in types) or (state=="CLOSED_UNMERGED" and "CLOSED" in types and "MERGED" not in types) or (state=="MERGED" and "MERGED" in types) or state=="UNKNOWN"
 if not ok: out.add(Finding("TERMINAL_EVENT_STATE_MISMATCH","/observed/events"))
 if state=="MERGED" and o["merge_commit_sha"] is None: out.add(Finding("TERMINAL_MERGE_COMMIT_REQUIRED","/observed/merge_commit_sha"))
 if state!="MERGED" and o["merge_commit_sha"] is not None: out.add(Finding("TERMINAL_MERGE_COMMIT_FORBIDDEN","/observed/merge_commit_sha"))
 exp=_time(a["expires_at"]); evaluated=_time(v["evaluated_at"])
 if a["authorization_state"]=="PRESENT" and (exp is None or evaluated is None or evaluated>exp): out.add(Finding("TERMINAL_AUTHORIZATION_STATE_MISMATCH","/authorization/authorization_state"))
 if a["authorization_state"]=="EXPIRED" and (exp is None or evaluated is None or evaluated<=exp): out.add(Finding("TERMINAL_AUTHORIZATION_STATE_MISMATCH","/authorization/authorization_state"))
 if a["authorization_state"]=="MISSING" and a["expires_at"] is not None: out.add(Finding("TERMINAL_AUTHORIZATION_STATE_MISMATCH","/authorization/expires_at"))
 if v["result"]!=recompute_result(v): out.add(Finding("TERMINAL_RESULT_MISMATCH","/result"))
 return tuple(sorted(out))
def validate_payload(v):
 s=_schema(v)
 if s: return Result("DENY",s)
 m=_semantic(v)
 if m: return Result("DENY",m)
 return {"WITHIN_CEILING":Result("PASS",()),"DIVERGENCE":Result("DENY",(Finding("TERMINAL_STATE_DIVERGENCE","/result/outcome"),)),"HOLD":Result("ABSTAIN",(Finding(v["result"]["reason_codes"][0],"/result/outcome"),)),"ERROR":Result("ERROR",(Finding("TERMINAL_ASSESSMENT_ERROR","/result/outcome"),))}[v["result"]["outcome"]]
def _replace(doc,pointer,value):
 parts=[x.replace("~1","/").replace("~0","~") for x in pointer[1:].split("/")]; t=doc
 for p in parts[:-1]: t=t[int(p)] if isinstance(t,list) else t[p]
 k=parts[-1]; t[int(k) if isinstance(t,list) else k]=copy.deepcopy(value)
def load_fixtures(): return json.loads(FIXTURES.read_text())
def materialize_case(manifest,case):
 d=copy.deepcopy(manifest["bases"][case["base"]])
 for m in case.get("mutations",[]): _replace(d,m["path"],m.get("value"))
 d["result"]=recompute_result(d); d["result"].update(case.get("result_override",{}))
 h,i=canonical_identity(d); d["spec_hash"]=case.get("spec_hash_override",h); d["assessment_id"]=case.get("assessment_id_override",i)
 return d
def run_fixtures():
 try: m=load_fixtures()
 except Exception: return 2
 ok=True
 for c in m["cases"]:
  r=validate_payload(materialize_case(m,c)); actual=[{"code":x.code,"path":x.path} for x in r.findings]
  match=r.outcome==c["expected_outcome"] and actual==c["expected_findings"]
  print(json.dumps({"case_id":c["case_id"],"outcome":r.outcome,"findings":actual,"suite_match":match},sort_keys=True,separators=(",",":")))
  ok=ok and match
 return 0 if ok else 1
def serialize(path,result): return json.dumps({"authority":"NONE","execution_mode":"FIXTURE_ONLY","file":path.as_posix() if path else None,"findings":[{"code":x.code,"path":x.path} for x in result.findings],"non_effects":NON_EFFECTS,"outcome":result.outcome},sort_keys=True,separators=(",",":"))
def main(argv:Sequence[str]|None=None):
 p=argparse.ArgumentParser(description=__doc__); p.add_argument("input",nargs="?",type=Path); p.add_argument("--fixtures",action="store_true"); a=p.parse_args(argv)
 if a.fixtures:
  if a.input: p.error("--fixtures cannot be combined with input")
  return run_fixtures()
 if a.input is None: p.error("input is required unless --fixtures is used")
 v,f=_read(a.input); r=Result("ERROR",f) if v is None else validate_payload(v); print(serialize(a.input,r)); return {"PASS":0,"DENY":1,"ERROR":2,"ABSTAIN":3}[r.outcome]
if __name__=="__main__": raise SystemExit(main())
