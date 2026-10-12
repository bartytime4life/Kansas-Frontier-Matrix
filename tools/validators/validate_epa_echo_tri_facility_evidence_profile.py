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
SCHEMA_PATH=REPO_ROOT/"schemas/contracts/v1/evidence/epa_echo_tri_facility_evidence_profile.schema.json"
FIXTURE_PATH=REPO_ROOT/"fixtures/contracts/v1/evidence/epa_echo_tri_facility_evidence_profile/cases.json"
PREFIX="EPA"
SEVERITY={"PASS":0,"ABSTAIN":1,"DENY":2,"ERROR":3}

def schema_findings(doc):
    schema=json.loads(SCHEMA_PATH.read_text())
    Draft202012Validator.check_schema(schema)
    v=Draft202012Validator(schema, format_checker=FormatChecker())
    return {Finding("EPA_SCHEMA_INVALID",pointer(e.absolute_path)) for e in v.iter_errors(doc)}

def semantic(doc):
    abstain=set(); deny=set(); error=set(); p=doc["epa_echo_tri_profile"]; b=doc["bundle"]
    evidence=set(b["evidence_refs"]); sources=set(b["source_records"])
    roles=p["source_roles"]
    role_names=[r["role"] for r in roles]
    if not {"ECHO_COMPLIANCE","TRI_ANNUAL_RELEASE"}.issubset(role_names): deny.add(Finding("EPA_REQUIRED_ROLE_MISSING","/epa_echo_tri_profile/source_roles"))
    if len({r["source_descriptor_ref"] for r in roles}) != len(roles): deny.add(Finding("EPA_SOURCE_ROLE_COLLAPSED","/epa_echo_tri_profile/source_roles"))
    for i,r in enumerate(roles):
        if r["source_descriptor_ref"] not in sources: abstain.add(Finding("EPA_SOURCE_RECORD_UNRESOLVED",f"/epa_echo_tri_profile/source_roles/{i}/source_descriptor_ref"))
        for j,x in enumerate(r["support_ref_ids"]):
            if x not in evidence: abstain.add(Finding("EPA_SUPPORT_UNRESOLVED",f"/epa_echo_tri_profile/source_roles/{i}/support_ref_ids/{j}"))
        if dt(r["source_time"])>dt(r["retrieved_at"]): error.add(Finding("EPA_SOURCE_TIME_INVALID",f"/epa_echo_tri_profile/source_roles/{i}/source_time"))
    if not p["policy_profile_ref"]: abstain.add(Finding("EPA_POLICY_UNRESOLVED","/epa_echo_tri_profile/policy_profile_ref"))
    for k,v in p["review_refs"].items():
        if not v: abstain.add(Finding("EPA_REVIEW_UNRESOLVED",f"/epa_echo_tri_profile/review_refs/{k}"))
    if not (dt(p["temporal_lineage"]["period_start"])<=dt(p["temporal_lineage"]["period_end"])<=dt(p["temporal_lineage"]["computed_at"])): error.add(Finding("EPA_TIME_INVALID","/epa_echo_tri_profile/temporal_lineage"))
    ids=[]
    for i,r in enumerate(p["records"]):
        if r["record_id"] in ids: error.add(Finding("EPA_DUPLICATE_RECORD_ID",f"/epa_echo_tri_profile/records/{i}/record_id"))
        ids.append(r["record_id"])
        expected={"ECHO_COMPLIANCE":"COMPLIANCE_EVENT","TRI_ANNUAL_RELEASE":"ANNUAL_CHEMICAL_RELEASE","DERIVED_PUBLIC_SAFE_SUMMARY":"PUBLIC_SAFE_SUMMARY"}[r["source_role"]]
        if r["record_kind"]!=expected: deny.add(Finding("EPA_ROLE_KIND_MISMATCH",f"/epa_echo_tri_profile/records/{i}/record_kind"))
        if r["source_role"]=="ECHO_COMPLIANCE" and r["quantity_scaled"]!=0: error.add(Finding("EPA_ROLE_ARITHMETIC_CONTRADICTION",f"/epa_echo_tri_profile/records/{i}/quantity_scaled"))
        for j,x in enumerate(r["support_ref_ids"]):
            if x not in evidence: abstain.add(Finding("EPA_SUPPORT_UNRESOLVED",f"/epa_echo_tri_profile/records/{i}/support_ref_ids/{j}"))
    subject=copy.deepcopy(p); subject.pop("spec_hash",None); actual=compute_spec_hash(subject)
    if p["spec_hash"]!=actual: error.add(Finding("EPA_PROFILE_HASH_MISMATCH","/epa_echo_tri_profile/spec_hash"))
    expected_id="kfm:epa-facility-assessment:"+actual
    if doc["assessment_id"]!=expected_id: error.add(Finding("EPA_ASSESSMENT_ID_MISMATCH","/assessment_id"))
    if b["claim_scope"]!=doc["assessment_id"] or b["checksums"]["epa_echo_tri_facility_evidence_profile"]!=actual: error.add(Finding("EPA_BUNDLE_BINDING_MISMATCH","/bundle/checksums/epa_echo_tri_facility_evidence_profile"))
    bs=copy.deepcopy(b); bs.pop("spec_hash",None)
    if b["spec_hash"]!=compute_spec_hash(bs): error.add(Finding("EPA_BUNDLE_HASH_MISMATCH","/bundle/spec_hash"))
    return abstain,deny,error

def validate_document(doc):
    if not isinstance(doc,Mapping): return "DENY",(Finding("EPA_ROOT_TYPE","/"),)
    sf=schema_findings(doc)
    if sf: return "DENY",tuple(sorted(sf))
    a,d,e=semantic(doc)
    if e:return "ERROR",tuple(sorted(e))
    if d:return "DENY",tuple(sorted(d))
    if a:return "ABSTAIN",tuple(sorted(a))
    return "PASS",()

def build_case(suite,c):
    d=copy.deepcopy(suite["base_document"])
    for m in c.get("pre_hash_mutations",[]): set_pointer(d,m["path"],m.get("value"),m["op"]=="remove")
    if c.get("recompute_identity",True):
        p=copy.deepcopy(d["epa_echo_tri_profile"]);p.pop("spec_hash",None);h=compute_spec_hash(p);d["epa_echo_tri_profile"]["spec_hash"]=h;d["assessment_id"]="kfm:epa-facility-assessment:"+h;d["bundle"]["claim_scope"]=d["assessment_id"];d["bundle"]["checksums"]["epa_echo_tri_facility_evidence_profile"]=h;b=copy.deepcopy(d["bundle"]);b.pop("spec_hash",None);d["bundle"]["spec_hash"]=compute_spec_hash(b)
    for m in c.get("post_hash_mutations",[]): set_pointer(d,m["path"],m.get("value"),m["op"]=="remove")
    return d

def run_fixture_suite():
    suite=load_json_file(FIXTURE_PATH); mismatches=[];counts={x:0 for x in SEVERITY}
    for c in suite["cases"]:
        out,find=validate_document(build_case(suite,c));counts[out]+=1;actual=[{"code":f.code,"path":f.path} for f in find]
        if out!=c["expected_outcome"] or actual!=c["expected_findings"]:mismatches.append({"case_id":c["case_id"],"expected":c["expected_outcome"],"actual":out,"findings":actual})
    return not mismatches,{"scope":"evidence.epa_echo_tri_facility","authority":"NONE","cases":len(suite["cases"]),"counts":counts,"mismatches":mismatches,"outcome":"PASS" if not mismatches else "ERROR"}

def main(argv:Sequence[str]|None=None):
    ap=argparse.ArgumentParser();ap.add_argument("files",nargs="*",type=Path);ap.add_argument("--fixtures",action="store_true");a=ap.parse_args(argv)
    if a.fixtures:
        ok,p=run_fixture_suite();print(json.dumps(p,sort_keys=True,separators=(",",":")));return 0 if ok else 2
    if not a.files:ap.error("provide files or --fixtures")
    rc=0
    for path in a.files:
        try:doc=load_json_file(path);out,find=validate_document(doc)
        except JsonInputError:out,find="ERROR",(Finding("EPA_INPUT_READ_ERROR","/"),)
        print(json.dumps({"file":path.as_posix(),"outcome":out,"findings":[{"code":f.code,"path":f.path} for f in find],"authority":"NONE"},sort_keys=True,separators=(",",":")))
        rc=max(rc,{"PASS":0,"DENY":1,"ERROR":2,"ABSTAIN":3}[out])
    return rc
if __name__=="__main__":raise SystemExit(main())
