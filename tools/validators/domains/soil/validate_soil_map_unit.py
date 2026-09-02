#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CASES = ROOT / "fixtures/domains/soil/soil_map_unit/cases.json"
FALSE_EFFECTS={"source_activated":False,"evidence_resolved":False,"policy_evaluated":False,"review_approved":False,"released":False,"published":False}

def expected_identity(c):
    x=dict(c); x.pop("id",None); x.pop("spec_hash",None)
    raw=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    h=hashlib.sha256(raw).hexdigest()
    return "sha256:"+h,"soil-map-unit:"+h[:24]

def evaluate(c):
    findings=[]
    if c.get("profile")!="kfm.domains.soil.soil-map-unit.v1" or c.get("status")!="PROPOSED_INACTIVE": findings.append("PROFILE_INVALID")
    if c.get("effects")!=FALSE_EFFECTS: findings.append("EFFECT_OVERCLAIM")
    if c.get("public_use_allowed") is not False: findings.append("PUBLIC_USE_OVERCLAIM")
    if c.get("release_state")!="UNRELEASED" or c.get("release_ref") is not None: findings.append("RELEASE_OVERCLAIM")
    if c.get("geometry_posture") not in {"SOURCE_POLYGON","DERIVED_POLYGON","HIDDEN","DENIED"}: findings.append("PARCEL_BOUNDARY_OVERCLAIM")
    ts=c.get("temporal_scope") or {}
    if ts.get("kind") not in {"SOURCE_VINTAGE","VALID_INTERVAL","DERIVATIVE_VINTAGE"}: findings.append("CURRENT_CONDITION_OVERCLAIM")
    support=c.get("support_type")
    if support not in {"authoritative_static_soil","gridded_derivative_soil"}: findings.append("SUPPORT_TYPE_INVALID")
    if support=="authoritative_static_soil" and c.get("source_native_key_family")!="MUKEY": findings.append("SOURCE_KEY_FAMILY_MISMATCH")
    if not c.get("evidence_refs") or not c.get("rollback_ref"): findings.append("BOUNDARY_REF_MISSING")
    h,i=expected_identity(c)
    if c.get("spec_hash")!=h: findings.append("SPEC_HASH_MISMATCH")
    elif c.get("id")!=i: findings.append("ID_MISMATCH")
    if any(x in findings for x in ("SPEC_HASH_MISMATCH","ID_MISMATCH","PROFILE_INVALID")): return "ERROR",sorted(set(findings))
    if findings: return "DENY",sorted(set(findings))
    return "PASS",[]

def main():
    p=argparse.ArgumentParser(); p.add_argument("path",nargs="?"); p.add_argument("--fixtures",action="store_true"); a=p.parse_args()
    if a.fixtures:
        bad=0
        for row in json.loads(CASES.read_text())["cases"]:
            out,find=evaluate(row["candidate"])
            print(row["name"],out,",".join(find))
            bad += out!=row["expected_outcome"] or find!=row["expected_findings"]
        raise SystemExit(1 if bad else 0)
    if not a.path: p.error("path or --fixtures required")
    out,find=evaluate(json.loads(Path(a.path).read_text())); print(json.dumps({"outcome":out,"findings":find},sort_keys=True))
if __name__=="__main__": main()
