from __future__ import annotations
import argparse, copy, json, sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages" / "hashing" / "src"
for p in (REPO_ROOT, PACKAGE_SRC):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
from hashing import JsonInputError, compute_spec_hash, load_json_file

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

def dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def pointer(parts) -> str:
    if not parts: return "/"
    return "/" + "/".join(str(p).replace("~","~0").replace("/","~1") for p in parts)

def set_pointer(doc, path, value, remove=False):
    parts=[p.replace("~1","/").replace("~0","~") for p in path.strip("/").split("/") if p]
    cur=doc
    for p in parts[:-1]: cur=cur[int(p)] if isinstance(cur,list) else cur[p]
    last=parts[-1]
    if remove:
        (cur.pop(int(last)) if isinstance(cur,list) else cur.pop(last,None))
    elif isinstance(cur,list): cur[int(last)]=value
    else: cur[last]=value
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/evidence/wimas_wwc5_aggregate_first_profile.schema.json"
FIXTURE_PATH=REPO_ROOT/"fixtures/contracts/v1/evidence/wimas_wwc5_aggregate_first_profile/cases.json"

def schema_findings(d):
 s=json.loads(SCHEMA_PATH.read_text());Draft202012Validator.check_schema(s);v=Draft202012Validator(s,format_checker=FormatChecker());return {Finding("WATER_SCHEMA_INVALID",pointer(e.absolute_path)) for e in v.iter_errors(d)}
def semantic(d):
 a=set();n=set();e=set();p=d["wimas_wwc5_profile"];b=d["bundle"];ev=set(b["evidence_refs"]);src=set(b["source_records"]);roles=p["source_roles"]
 required={"WIMAS_WATER_USE_AGGREGATE","WIMAS_WATER_RIGHT_CONTEXT","WWC5_WELL_RECORD_REFERENCE"}
 if {x["role"] for x in roles}!=required:n.add(Finding("WATER_REQUIRED_ROLE_MISSING","/wimas_wwc5_profile/source_roles"))
 if len({x["source_descriptor_ref"] for x in roles})!=3:n.add(Finding("WATER_SOURCE_ROLE_COLLAPSED","/wimas_wwc5_profile/source_roles"))
 for i,x in enumerate(roles):
  if x["source_descriptor_ref"] not in src:a.add(Finding("WATER_SOURCE_RECORD_UNRESOLVED",f"/wimas_wwc5_profile/source_roles/{i}/source_descriptor_ref"))
  for j,r in enumerate(x["support_ref_ids"]):
   if r not in ev:a.add(Finding("WATER_SUPPORT_UNRESOLVED",f"/wimas_wwc5_profile/source_roles/{i}/support_ref_ids/{j}"))
  if dt(x["source_time"])>dt(x["retrieved_at"]):e.add(Finding("WATER_SOURCE_TIME_INVALID",f"/wimas_wwc5_profile/source_roles/{i}/source_time"))
 if not p["policy_profile_ref"]:a.add(Finding("WATER_POLICY_UNRESOLVED","/wimas_wwc5_profile/policy_profile_ref"))
 for k,v in p["review_refs"].items():
  if not v:a.add(Finding("WATER_REVIEW_UNRESOLVED",f"/wimas_wwc5_profile/review_refs/{k}"))
 if not (dt(p["temporal_lineage"]["period_start"])<=dt(p["temporal_lineage"]["period_end"])<=dt(p["temporal_lineage"]["computed_at"])):e.add(Finding("WATER_TIME_INVALID","/wimas_wwc5_profile/temporal_lineage"))
 ids=[]; role_map={x["role"]:x for x in roles}
 for i,x in enumerate(p["aggregates"]):
  if x["aggregate_id"] in ids:e.add(Finding("WATER_DUPLICATE_AGGREGATE_ID",f"/wimas_wwc5_profile/aggregates/{i}/aggregate_id"))
  ids.append(x["aggregate_id"])
  if x["group_count"]<p["privacy_controls"]["minimum_group_size"]:n.add(Finding("WATER_GROUP_BELOW_MINIMUM",f"/wimas_wwc5_profile/aggregates/{i}/group_count"))
  if x["source_role"] not in role_map or x["position_quality"]!=role_map[x["source_role"]]["position_quality"]:n.add(Finding("WATER_ROLE_AGGREGATE_MISMATCH",f"/wimas_wwc5_profile/aggregates/{i}/source_role"))
  if x["source_role"]!="WIMAS_WATER_USE_AGGREGATE" and x["quantity_scaled"]!=0:e.add(Finding("WATER_ROLE_ARITHMETIC_CONTRADICTION",f"/wimas_wwc5_profile/aggregates/{i}/quantity_scaled"))
  for j,r in enumerate(x["support_ref_ids"]):
   if r not in ev:a.add(Finding("WATER_SUPPORT_UNRESOLVED",f"/wimas_wwc5_profile/aggregates/{i}/support_ref_ids/{j}"))
 subject=copy.deepcopy(p);subject.pop("spec_hash",None);actual=compute_spec_hash(subject)
 if p["spec_hash"]!=actual:e.add(Finding("WATER_PROFILE_HASH_MISMATCH","/wimas_wwc5_profile/spec_hash"))
 if d["assessment_id"]!="kfm:wimas-wwc5-assessment:"+actual:e.add(Finding("WATER_ASSESSMENT_ID_MISMATCH","/assessment_id"))
 if b["claim_scope"]!=d["assessment_id"] or b["checksums"]["wimas_wwc5_aggregate_first_profile"]!=actual:e.add(Finding("WATER_BUNDLE_BINDING_MISMATCH","/bundle/checksums/wimas_wwc5_aggregate_first_profile"))
 bs=copy.deepcopy(b);bs.pop("spec_hash",None)
 if b["spec_hash"]!=compute_spec_hash(bs):e.add(Finding("WATER_BUNDLE_HASH_MISMATCH","/bundle/spec_hash"))
 return a,n,e
def validate_document(d):
 if not isinstance(d,Mapping):return "DENY",(Finding("WATER_ROOT_TYPE","/"),)
 s=schema_findings(d)
 if s:return "DENY",tuple(sorted(s))
 a,n,e=semantic(d)
 if e:return "ERROR",tuple(sorted(e))
 if n:return "DENY",tuple(sorted(n))
 if a:return "ABSTAIN",tuple(sorted(a))
 return "PASS",()
def build_case(s,c):
 d=copy.deepcopy(s["base_document"])
 for m in c.get("pre_hash_mutations",[]):set_pointer(d,m["path"],m.get("value"),m["op"]=="remove")
 p=copy.deepcopy(d["wimas_wwc5_profile"]);p.pop("spec_hash",None);h=compute_spec_hash(p);d["wimas_wwc5_profile"]["spec_hash"]=h;d["assessment_id"]="kfm:wimas-wwc5-assessment:"+h;d["bundle"]["claim_scope"]=d["assessment_id"];d["bundle"]["checksums"]["wimas_wwc5_aggregate_first_profile"]=h;b=copy.deepcopy(d["bundle"]);b.pop("spec_hash",None);d["bundle"]["spec_hash"]=compute_spec_hash(b)
 for m in c.get("post_hash_mutations",[]):set_pointer(d,m["path"],m.get("value"),m["op"]=="remove")
 return d
def run_fixture_suite():
 s=load_json_file(FIXTURE_PATH);counts={x:0 for x in ("PASS","ABSTAIN","DENY","ERROR")};mis=[]
 for c in s["cases"]:
  out,f=validate_document(build_case(s,c));counts[out]+=1;actual=[{"code":x.code,"path":x.path} for x in f]
  if out!=c["expected_outcome"] or actual!=c["expected_findings"]:mis.append({"case_id":c["case_id"],"expected":c["expected_outcome"],"actual":out,"findings":actual})
 return not mis,{"scope":"evidence.wimas_wwc5_aggregate_first","authority":"NONE","cases":len(s["cases"]),"counts":counts,"mismatches":mis,"outcome":"PASS" if not mis else "ERROR"}
def main(argv:Sequence[str]|None=None):
 ap=argparse.ArgumentParser();ap.add_argument("files",nargs="*",type=Path);ap.add_argument("--fixtures",action="store_true");a=ap.parse_args(argv)
 if a.fixtures:
  ok,p=run_fixture_suite();print(json.dumps(p,sort_keys=True,separators=(",",":")));return 0 if ok else 2
 if not a.files:ap.error("provide files or --fixtures")
 rc=0
 for path in a.files:
  try:out,f=validate_document(load_json_file(path))
  except JsonInputError:out,f="ERROR",(Finding("WATER_INPUT_READ_ERROR","/"),)
  print(json.dumps({"file":path.as_posix(),"outcome":out,"findings":[{"code":x.code,"path":x.path} for x in f],"authority":"NONE"},sort_keys=True,separators=(",",":")));rc=max(rc,{"PASS":0,"DENY":1,"ERROR":2,"ABSTAIN":3}[out])
 return rc
if __name__=="__main__":raise SystemExit(main())
