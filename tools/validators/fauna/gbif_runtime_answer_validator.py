#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from jsonschema import Draft202012Validator

REPO=Path(__file__).resolve().parents[3]
BANNED={"decimalLatitude","decimalLongitude","occurrenceLatitude","occurrenceLongitude","exact_coordinate","exactCoordinates","raw_occurrence_point"}
FORBIDDEN=["confirmed present","verified present","known population","exact location","site-level record","precise coordinates","occurrence point","raw gbif location"]

def walk(v):
    if isinstance(v,dict):
        for k,val in v.items():
            yield k,val
            yield from walk(val)
    elif isinstance(v,list):
        for i in v: yield from walk(i)

def validate_file(schema_path,payload):
    schema=json.loads((REPO/schema_path).read_text()); errs=list(Draft202012Validator(schema).iter_errors(payload))
    return [e.message for e in errs]

def validate(payload):
    errs=[]
    for k,_ in walk(payload):
        if k in BANNED: errs.append(f"banned field: {k}")
    s=json.dumps(payload).lower()
    if any(t in s for t in FORBIDDEN): errs.append("forbidden language present")
    if payload.get("answer_posture")=="cited_answer":
        if not payload.get("claims"): errs.append("cited_answer with no claims")
        if not payload.get("answer_receipt_ref"): errs.append("cited_answer without answer_receipt_ref")
        if not payload.get("limitations"): errs.append("cited_answer without limitations")
        if sum(len(c.get("citations",[])) for c in payload.get("claims",[]))==0: errs.append("cited_answer with zero citations")
    return errs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--kind",required=True,choices=["query","answer","card","layer","receipt"]); ap.add_argument("--input",required=True); a=ap.parse_args()
    payload=json.loads(Path(a.input).read_text())
    schema_map={"query":"schemas/runtime/fauna/gbif_occurrence_query.schema.json","answer":"schemas/runtime/fauna/gbif_occurrence_answer_envelope.schema.json","card":"schemas/ui/fauna/gbif_occurrence_card.schema.json","receipt":"schemas/receipts/fauna/gbif_answer_receipt.schema.json"}
    errs=[]
    if a.kind in schema_map: errs.extend(validate_file(schema_map[a.kind],payload))
    errs.extend(validate(payload))
    if a.kind=="card":
        if not payload.get("citations"): errs.append("UI card with no citations")
        if not payload.get("claim_refs"): errs.append("UI card with no claim_refs")
    if a.kind=="layer":
        if payload.get("geometry_role")!="generalized_public_area": errs.append("map layer without geometry_role == generalized_public_area")
        if not payload.get("geoprivacy_receipt_ref"): errs.append("map layer without geoprivacy_receipt_ref")
    if a.kind=="receipt":
        if not payload.get("policy_version"): errs.append("receipt without policy_version")
        if not payload.get("rights_posture_checked") or not payload.get("sensitivity_posture_checked") or not payload.get("geoprivacy_checked"): errs.append("receipt without checks")
    if "kfm:spec_hash" not in payload: errs.append("missing kfm:spec_hash")
    if errs:
        print("DENY:"+";".join(errs)); sys.exit(1)
    print("ALLOW")
if __name__=='__main__': main()
