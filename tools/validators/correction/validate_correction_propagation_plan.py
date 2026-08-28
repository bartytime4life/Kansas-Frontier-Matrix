#!/usr/bin/env python3
"""Validate fixture-only CorrectionPropagationPlan records."""
from __future__ import annotations
import argparse,copy,json,math,sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any,Iterable,Mapping,Sequence
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parents[3]; HS=ROOT/"packages/hashing/src"; sys.path.insert(0,str(HS)) if str(HS) not in sys.path else None
from hashing import CanonicalizationFailure,compute_spec_hash
SCHEMA=ROOT/"schemas/contracts/v1/correction/correction_propagation_plan.schema.json"; FIXTURES=ROOT/"fixtures/contracts/v1/correction/correction_propagation_plan/cases.json"; PREFIX="kfm:correction-propagation:"; MAX=4*1024*1024
@dataclass(frozen=True,order=True)
class Finding: code:str; path:str
@dataclass(frozen=True)
class Result: outcome:str; findings:tuple[Finding,...]
class DK(ValueError):pass
class NF(ValueError):pass
def _uniq(p):
 d={}
 for k,v in p:
  if k in d:raise DK
  d[k]=v
 return d
def _rej(_):raise NF
def _flt(v):
 x=float(v)
 if not math.isfinite(x):raise NF
 return x
def _ptr(p):
 x=[str(i).replace("~","~0").replace("/","~1") for i in p];return "/"+"/".join(x) if x else "/"
def _time(v):
 if not isinstance(v,str):return None
 try:return datetime.fromisoformat(v[:-1]+"+00:00" if v.endswith("Z") else v)
 except ValueError:return None
def _read(p):
 try:
  if p.is_symlink():return None,(Finding("CORRECTION_INPUT_SYMLINK_DENIED","/"),)
  if not p.is_file():return None,(Finding("CORRECTION_INPUT_NOT_FILE","/"),)
  if p.stat().st_size>MAX:return None,(Finding("CORRECTION_INPUT_TOO_LARGE","/"),)
  v=json.loads(p.read_text(),object_pairs_hook=_uniq,parse_constant=_rej,parse_float=_flt)
 except DK:return None,(Finding("CORRECTION_JSON_DUPLICATE_KEY","/"),)
 except NF:return None,(Finding("CORRECTION_JSON_NONFINITE_NUMBER","/"),)
 except Exception:return None,(Finding("CORRECTION_JSON_INVALID","/"),)
 return (v,()) if isinstance(v,dict) else (None,(Finding("CORRECTION_ROOT_NOT_OBJECT","/"),))
def canonical_identity(v):
 s={k:x for k,x in v.items() if k not in {"plan_id","spec_hash"}};h=compute_spec_hash(s);return h,PREFIX+h.split(":",1)[1][:24]
ACT={"INVALIDATE":"INVALIDATE_DERIVATIVE","MARK_STALE":"MARK_STALE","REBUILD":"REBUILD_DERIVATIVE","REPOINT_ALIAS":"REPOINT_ALIAS","REPUBLISH":"REPUBLISH_DERIVATIVE","WITHDRAW":"WITHDRAW_DERIVATIVE","REVIEW_ONLY":"REVIEW_REQUIRED"}; STAT={"PENDING":"PENDING_ACTION","BLOCKED":"BLOCKED_DEPENDENCY","COMPLETED":"COMPLETION_RECORDED","ERROR":"PROPAGATION_ERROR"}
def reasons(e):return sorted([ACT[e["action"]],STAT[e["status"]]])
def recompute_summary(entries):
 c={"pending_count":0,"blocked_count":0,"completed_count":0,"error_count":0}
 for e in entries:c[e["status"].lower()+"_count"]+=1
 overall="ERROR" if c["error_count"] else "HOLD" if c["blocked_count"] else "COMPLETE" if c["completed_count"]==len(entries) else "READY"
 return {"entry_count":len(entries),**c,"public_impact":any(e["visibility"] in {"PUBLIC","SEMI_PUBLIC"} for e in entries),"overall_outcome":overall}
def _schema(v):
 try:s=json.loads(SCHEMA.read_text());Draft202012Validator.check_schema(s);errs=list(islice(Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(v),101))
 except Exception:return (Finding("CORRECTION_SCHEMA_UNAVAILABLE","/"),)
 errs.sort(key=lambda e:(_ptr(e.absolute_path),str(e.validator)));return tuple(sorted({Finding("CORRECTION_SCHEMA_INVALID",_ptr(e.absolute_path)) for e in errs[:100]}))
def _semantic(v):
 out=set();entries=v["entries"]
 try:eh,eid=canonical_identity(v)
 except CanonicalizationFailure:out.add(Finding("CORRECTION_CANONICALIZATION_ERROR","/"))
 else:
  if v["spec_hash"]!=eh:out.add(Finding("CORRECTION_SPEC_HASH_MISMATCH","/spec_hash"))
  if v["plan_id"]!=eid:out.add(Finding("CORRECTION_ID_MISMATCH","/plan_id"))
 keys=[(e["surface_kind"],e["artifact_ref"]) for e in entries]
 if keys!=sorted(keys):out.add(Finding("CORRECTION_ENTRY_ORDER_INVALID","/entries"))
 if len(keys)!=len(set(k[1] for k in keys)):out.add(Finding("CORRECTION_ARTIFACT_DUPLICATE","/entries"))
 kinds=sorted(set(e["surface_kind"] for e in entries))
 if v["declared_surface_kinds"]!=kinds:out.add(Finding("CORRECTION_SURFACE_CLOSURE_MISMATCH","/declared_surface_kinds"))
 obs=_time(v["observed_at"])
 for i,e in enumerate(entries):
  p=f"/entries/{i}";u=_time(e["updated_at"])
  if obs is None or u is None or u>obs:out.add(Finding("CORRECTION_TIME_INVALID",p+"/updated_at"))
  if e["reason_codes"]!=reasons(e):out.add(Finding("CORRECTION_REASON_CODES_MISMATCH",p+"/reason_codes"))
  if e["status"]=="COMPLETED" and e["completion_receipt_ref"] is None:out.add(Finding("CORRECTION_COMPLETION_RECEIPT_REQUIRED",p+"/completion_receipt_ref"))
  if e["status"]!="COMPLETED" and e["completion_receipt_ref"] is not None:out.add(Finding("CORRECTION_COMPLETION_RECEIPT_FORBIDDEN",p+"/completion_receipt_ref"))
  if e["action"] in {"REPOINT_ALIAS","REPUBLISH"}:
   if v["replacement_release_ref"] is None or e["target_release_ref"]!=v["replacement_release_ref"]:out.add(Finding("CORRECTION_TARGET_RELEASE_REQUIRED",p+"/target_release_ref"))
  elif e["target_release_ref"] is not None:out.add(Finding("CORRECTION_TARGET_RELEASE_FORBIDDEN",p+"/target_release_ref"))
  if e["visibility"] in {"PUBLIC","SEMI_PUBLIC"} and e["action"]=="REVIEW_ONLY":out.add(Finding("CORRECTION_PUBLIC_REVIEW_ONLY_FORBIDDEN",p+"/action"))
 if v["summary"]!=recompute_summary(entries):out.add(Finding("CORRECTION_SUMMARY_MISMATCH","/summary"))
 return tuple(sorted(out))
def validate_payload(v):
 s=_schema(v)
 if s:return Result("DENY",s)
 m=_semantic(v)
 if m:return Result("DENY",m)
 o=v["summary"]["overall_outcome"]
 return {"READY":Result("PASS",()),"COMPLETE":Result("PASS",()),"HOLD":Result("ABSTAIN",(Finding("CORRECTION_PROPAGATION_BLOCKED","/summary/overall_outcome"),)),"ERROR":Result("ERROR",(Finding("CORRECTION_PROPAGATION_ERROR","/summary/overall_outcome"),))}[o]
def _replace(d,p,v):
 parts=[x.replace("~1","/").replace("~0","~") for x in p[1:].split("/")];t=d
 for x in parts[:-1]:t=t[int(x)] if isinstance(t,list) else t[x]
 k=parts[-1];t[int(k) if isinstance(t,list) else k]=copy.deepcopy(v)
def load_fixtures():return json.loads(FIXTURES.read_text())
def materialize_case(m,c):
 d=copy.deepcopy(m["bases"][c["base"]])
 for x in c.get("mutations",[]):_replace(d,x["path"],x.get("value"))
 for e in d["entries"]:e["reason_codes"]=reasons(e)
 d["summary"]=recompute_summary(d["entries"]);d["summary"].update(c.get("summary_override",{}))
 h,i=canonical_identity(d);d["spec_hash"]=c.get("spec_hash_override",h);d["plan_id"]=c.get("plan_id_override",i);return d
def run_fixtures():
 m=load_fixtures();ok=True
 for c in m["cases"]:
  r=validate_payload(materialize_case(m,c));a=[{"code":x.code,"path":x.path} for x in r.findings];match=r.outcome==c["expected_outcome"] and a==c["expected_findings"];print(json.dumps({"case_id":c["case_id"],"outcome":r.outcome,"findings":a,"suite_match":match},sort_keys=True,separators=(",",":")));ok=ok and match
 return 0 if ok else 1
def serialize(p,r):return json.dumps({"authority":"NONE","execution_mode":"FIXTURE_ONLY","file":p.as_posix() if p else None,"findings":[{"code":x.code,"path":x.path} for x in r.findings],"outcome":r.outcome,"non_effects":["no_cache_invalidation","no_alias_repoint","no_release","no_publication","no_history_deletion"]},sort_keys=True,separators=(",",":"))
def main(argv:Sequence[str]|None=None):
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",nargs="?",type=Path);p.add_argument("--fixtures",action="store_true");a=p.parse_args(argv)
 if a.fixtures:return run_fixtures()
 if a.input is None:p.error("input required")
 v,f=_read(a.input);r=Result("ERROR",f) if v is None else validate_payload(v);print(serialize(a.input,r));return {"PASS":0,"DENY":1,"ERROR":2,"ABSTAIN":3}[r.outcome]
if __name__=="__main__":raise SystemExit(main())
