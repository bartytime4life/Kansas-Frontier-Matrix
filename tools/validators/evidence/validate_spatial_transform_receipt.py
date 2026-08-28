#!/usr/bin/env python3
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
FIXTURES=ROOT/"fixtures/contracts/v1/evidence/spatial_transform_receipt/cases.json"
REQ={"receipt_id","input_ref","output_ref","source_crs","target_crs","operations","input_digest","output_digest","changed","evidence_refs","network_access","outcome","reason_codes"}

def validate(r):
    if not isinstance(r,dict) or not REQ.issubset(r): return "ERROR"
    if r["network_access"] is not False: return "DENY"
    if r["input_ref"] == r["output_ref"] or not r["operations"] or not r["evidence_refs"]: return "DENY"
    if r["changed"] is not True: return "DENY"
    if r["input_digest"] == r["output_digest"]: return "DENY"
    if not r["source_crs"] or not r["target_crs"]: return "DENY"
    return "PASS" if r["outcome"] == "PASS" else ("ERROR" if r["outcome"] == "ERROR" else "DENY")

def replay(path=FIXTURES):
    data=json.loads(Path(path).read_text()); bad=[]
    for c in data["cases"]:
        got=validate(c["record"])
        if got != c["expected"]: bad.append((c["name"],c["expected"],got))
    return bad

def main():
    p=argparse.ArgumentParser(); p.add_argument("path",nargs="?"); p.add_argument("--fixtures",action="store_true"); a=p.parse_args()
    if a.fixtures:
        bad=replay()
        if bad:
            for x in bad: print("FAIL",*x)
            raise SystemExit(1)
        print("PASS spatial transform receipt fixtures"); return
    if not a.path: p.error("path required unless --fixtures")
    print(validate(json.loads(Path(a.path).read_text())))

if __name__=="__main__": main()
