#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
CASES=ROOT/"fixtures/domains/soil/soil_component/cases.json"
FALSE_EFFECTS={"component_persisted":False,"evidence_resolved":False,"policy_evaluated":False,"review_approved":False,"released":False,"published":False}
def expected_identity(c):
    x=dict(c); x.pop("id",None); x.pop("spec_hash",None)
    h=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
    return "sha256:"+h,"soil-component:"+h[:24]
def evaluate(c):
    findings=[]
    if c.get("profile")!="kfm.domains.soil.soil-component.v1" or c.get("status")!="PROPOSED_INACTIVE": findings.append("PROFILE_INVALID")
    if c.get("effects")!=FALSE_EFFECTS: findings.append("EFFECT_OVERCLAIM")
    if c.get("public_use_allowed") is not False: findings.append("PUBLIC_USE_OVERCLAIM")
    if c.get("release_state")!="UNRELEASED" or c.get("release_ref") is not None: findings.append("RELEASE_OVERCLAIM")
    if c.get("support_type") not in {"authoritative_static_soil","gridded_derivative_soil"}: findings.append("SUPPORT_TYPE_INVALID")
    p=c.get("component_percent")
    if not isinstance(p,(int,float)) or isinstance(p,bool) or not 0<=p<=100: findings.append("COMPONENT_PERCENT_INVALID")
    if not c.get("map_unit_ref") or not c.get("map_unit_native_id"): findings.append("MAP_UNIT_REF_MISSING")
    if c.get("source_native_key_family")!="COKEY": findings.append("SOURCE_KEY_FAMILY_MISMATCH")
    if not c.get("evidence_refs") or not c.get("rollback_ref") or not c.get("percent_method_ref"): findings.append("BOUNDARY_REF_MISSING")
    h,i=expected_identity(c)
    if c.get("spec_hash")!=h: findings.append("SPEC_HASH_MISMATCH")
    elif c.get("id")!=i: findings.append("ID_MISMATCH")
    findings=sorted(set(findings))
    if any(x in findings for x in ("PROFILE_INVALID","SPEC_HASH_MISMATCH","ID_MISMATCH")): return "ERROR",findings
    if findings: return "DENY",findings
    return "PASS",[]
def main():
    p=argparse.ArgumentParser(); p.add_argument("path",nargs="?"); p.add_argument("--fixtures",action="store_true"); a=p.parse_args()
    if a.fixtures:
        bad=0
        for row in json.loads(CASES.read_text())["cases"]:
            got=evaluate(row["candidate"]); print(row["name"],got[0],",".join(got[1])); bad += got!=(row["expected_outcome"],row["expected_findings"])
        raise SystemExit(1 if bad else 0)
    if not a.path: p.error("path or --fixtures required")
    out,find=evaluate(json.loads(Path(a.path).read_text())); print(json.dumps({"outcome":out,"findings":find},sort_keys=True))
if __name__=="__main__": main()
