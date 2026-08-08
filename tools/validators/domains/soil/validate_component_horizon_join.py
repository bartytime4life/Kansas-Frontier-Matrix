#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
CASES=ROOT/"fixtures/domains/soil/component_horizon_join/cases.json"
FALSE_EFFECTS={"join_persisted":False,"evidence_resolved":False,"policy_evaluated":False,"review_approved":False,"released":False,"published":False}

def expected_identity(c):
    x=dict(c); x.pop("id",None); x.pop("spec_hash",None)
    raw=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    h=hashlib.sha256(raw).hexdigest()
    return "sha256:"+h,"soil-component-horizon-join:"+h[:24]

def evaluate(c):
    findings=[]
    if c.get("profile")!="kfm.domains.soil.component-horizon-join.v1" or c.get("status")!="PROPOSED_INACTIVE": findings.append("PROFILE_INVALID")
    if c.get("effects")!=FALSE_EFFECTS: findings.append("EFFECT_OVERCLAIM")
    if c.get("public_use_allowed") is not False: findings.append("PUBLIC_USE_OVERCLAIM")
    if c.get("release_state")!="UNRELEASED" or c.get("release_ref") is not None: findings.append("RELEASE_OVERCLAIM")
    if c.get("support_type") not in {"authoritative_static_soil","gridded_derivative_soil"}: findings.append("SUPPORT_TYPE_INVALID")
    keys=c.get("source_native_keys")
    if not isinstance(keys,dict) or any(not isinstance(keys.get(k),str) or not keys.get(k) for k in ("MUKEY","COKEY","CHKEY")): findings.append("SOURCE_NATIVE_KEYS_INCOMPLETE")
    if any(not c.get(k) for k in ("map_unit_ref","component_ref","horizon_ref","source_ref","source_role","rollback_ref")) or not c.get("evidence_refs"): findings.append("LINEAGE_REF_MISSING")
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
            got=evaluate(row["candidate"])
            print(row["name"],got[0],",".join(got[1]))
            bad += got!=(row["expected_outcome"],row["expected_findings"])
        raise SystemExit(1 if bad else 0)
    if not a.path: p.error("path or --fixtures required")
    out,find=evaluate(json.loads(Path(a.path).read_text())); print(json.dumps({"outcome":out,"findings":find},sort_keys=True))
if __name__=="__main__": main()
