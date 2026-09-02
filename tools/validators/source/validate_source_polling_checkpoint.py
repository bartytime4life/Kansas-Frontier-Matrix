#!/usr/bin/env python3
"""Validate fixture-only SourcePollingCheckpoint records."""
from __future__ import annotations
import argparse,copy,json,math,sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any,Iterable,Mapping,Sequence
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parents[3];HS=ROOT/"packages/hashing/src";sys.path.insert(0,str(HS)) if str(HS) not in sys.path else None
from hashing import CanonicalizationFailure,compute_spec_hash
SCHEMA=ROOT/"schemas/contracts/v1/source/source_polling_checkpoint.schema.json";FIXTURES=ROOT/"fixtures/contracts/v1/source/source_polling_checkpoint/cases.json";PREFIX="kfm:source-polling-checkpoint:";MAX=4*1024*1024
@dataclass(frozen=True,order=True)
class Finding:code:str;path:str
@dataclass(frozen=True)
class Result:outcome:str;findings:tuple[Finding,...]
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
def _read(p):
 try:
  if p.is_symlink():return None,(Finding("POLL_INPUT_SYMLINK_DENIED","/"),)
  if not p.is_file():return None,(Finding("POLL_INPUT_NOT_FILE","/"),)
  if p.stat().st_size>MAX:return None,(Finding("POLL_INPUT_TOO_LARGE","/"),)
  v=json.loads(p.read_text(),object_pairs_hook=_uniq,parse_constant=_rej,parse_float=_flt)
 except DK:return None,(Finding("POLL_JSON_DUPLICATE_KEY","/"),)
 except NF:return None,(Finding("POLL_JSON_NONFINITE_NUMBER","/"),)
 except Exception:return None,(Finding("POLL_JSON_INVALID","/"),)
 return (v,()) if isinstance(v,dict) else (None,(Finding("POLL_ROOT_NOT_OBJECT","/"),))
def canonical_identity(v):
 s={k:x for k,x in v.items() if k not in {"checkpoint_id","spec_hash"}};h=compute_spec_hash(s);return h,PREFIX+h.split(":",1)[1][:24]
def has_validator(s):return any(s.get(k) is not None for k in ["etag","last_modified","representation_digest"])
def recompute(v):
 o=v["retrieval_outcome"]
 if o=="NOT_MODIFIED":return ("NO_ACTION",["VALIDATORS_UNCHANGED"])
 if o=="MODIFIED":return ("FETCH_CANDIDATE",["FETCH_REVIEW_REQUIRED","VALIDATORS_CHANGED"])
 if o=="UNAVAILABLE":return ("HOLD",["SOURCE_UNAVAILABLE"])
 if o=="UNKNOWN":return ("HOLD",["SOURCE_STATE_UNKNOWN"])
 return ("ERROR",["POLLING_ERROR"])
def _schema(v):
 try:s=json.loads(SCHEMA.read_text());Draft202012Validator.check_schema(s);e=list(islice(Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(v),101))
 except Exception:return (Finding("POLL_SCHEMA_UNAVAILABLE","/"),)
 e.sort(key=lambda x:(_ptr(x.absolute_path),str(x.validator)));return tuple(sorted({Finding("POLL_SCHEMA_INVALID",_ptr(x.absolute_path)) for x in e[:100]}))
def _semantic(v):
 out=set();p=v["prior_state"];c=v["current_state"];o=v["retrieval_outcome"]
 try:eh,eid=canonical_identity(v)
 except CanonicalizationFailure:out.add(Finding("POLL_CANONICALIZATION_ERROR","/"))
 else:
  if v["spec_hash"]!=eh:out.add(Finding("POLL_SPEC_HASH_MISMATCH","/spec_hash"))
  if v["checkpoint_id"]!=eid:out.add(Finding("POLL_ID_MISMATCH","/checkpoint_id"))
 if v["source_descriptor_ref"]!=f"kfm://source/{v['source_id']}":out.add(Finding("POLL_SOURCE_REF_MISMATCH","/source_descriptor_ref"))
 changed=p!=c
 if o=="NOT_MODIFIED" and (not has_validator(c) or changed):out.add(Finding("POLL_NOT_MODIFIED_UNPROVEN","/current_state"))
 if o=="MODIFIED" and (not has_validator(c) or not changed):out.add(Finding("POLL_MODIFIED_UNPROVEN","/current_state"))
 decision,reasons=recompute(v)
 if v["decision"]!=decision:out.add(Finding("POLL_DECISION_MISMATCH","/decision"))
 if v["reason_codes"]!=reasons:out.add(Finding("POLL_REASON_CODES_MISMATCH","/reason_codes"))
 if v["decision"]=="FETCH_CANDIDATE" and v["candidate_fetch_ref"] is None:out.add(Finding("POLL_FETCH_CANDIDATE_REQUIRED","/candidate_fetch_ref"))
 if v["decision"]!="FETCH_CANDIDATE" and v["candidate_fetch_ref"] is not None:out.add(Finding("POLL_FETCH_CANDIDATE_FORBIDDEN","/candidate_fetch_ref"))
 return tuple(sorted(out))
def validate_payload(v):
 s=_schema(v)
 if s:return Result("DENY",s)
 m=_semantic(v)
 if m:return Result("DENY",m)
 return {"NO_ACTION":Result("PASS",()),"FETCH_CANDIDATE":Result("PASS",()),"HOLD":Result("ABSTAIN",(Finding(v["reason_codes"][0],"/decision"),)),"ERROR":Result("ERROR",(Finding("POLLING_ERROR","/decision"),))}[v["decision"]]
def _replace(d,p,v):
 parts=[x.replace("~1","/").replace("~0","~") for x in p[1:].split("/")];t=d
 for x in parts[:-1]:t=t[int(x)] if isinstance(t,list) else t[x]
 k=parts[-1];t[int(k) if isinstance(t,list) else k]=copy.deepcopy(v)
def load_fixtures():return json.loads(FIXTURES.read_text())
def materialize_case(m,c):
 d=copy.deepcopy(m["bases"][c["base"]])
 for x in c.get("mutations",[]):_replace(d,x["path"],x.get("value"))
 dec,rs=recompute(d);d["decision"]=c.get("decision_override",dec);d["reason_codes"]=c.get("reason_codes_override",rs)
 h,i=canonical_identity(d);d["spec_hash"]=c.get("spec_hash_override",h);d["checkpoint_id"]=c.get("checkpoint_id_override",i);return d
def run_fixtures():
 m=load_fixtures();ok=True
 for c in m["cases"]:
  r=validate_payload(materialize_case(m,c));a=[{"code":x.code,"path":x.path} for x in r.findings];match=r.outcome==c["expected_outcome"] and a==c["expected_findings"];print(json.dumps({"case_id":c["case_id"],"outcome":r.outcome,"findings":a,"suite_match":match},sort_keys=True,separators=(",",":")));ok=ok and match
 return 0 if ok else 1
def serialize(p,r):return json.dumps({"authority":"NONE","execution_mode":"FIXTURE_ONLY","file":p.as_posix() if p else None,"findings":[{"code":x.code,"path":x.path} for x in r.findings],"outcome":r.outcome,"non_effects":["no_network","no_source_activation","no_fetch","no_raw_write","no_release","no_publication"]},sort_keys=True,separators=(",",":"))
def main(argv:Sequence[str]|None=None):
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",nargs="?",type=Path);p.add_argument("--fixtures",action="store_true");a=p.parse_args(argv)
 if a.fixtures:return run_fixtures()
 if a.input is None:p.error("input required")
 v,f=_read(a.input);r=Result("ERROR",f) if v is None else validate_payload(v);print(serialize(a.input,r));return {"PASS":0,"DENY":1,"ERROR":2,"ABSTAIN":3}[r.outcome]
if __name__=="__main__":raise SystemExit(main())
