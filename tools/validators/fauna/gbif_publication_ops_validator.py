#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from copy import deepcopy
from pathlib import Path

FORBIDDEN_FIELDS={"decimalLatitude","decimalLongitude","occurrenceLatitude","occurrenceLongitude","exact_coordinate","exactCoordinates","raw_occurrence_point","rawGbifCoordinate","site_level_location","precise_location"}
FORBIDDEN_PHRASES=["confirmed present","verified present","known population","exact location","site-level record","precise coordinates","occurrence point","raw gbif location"]


def canonicalize(value):
    if isinstance(value, dict):
        return {k: canonicalize(value[k]) for k in sorted(value)}
    if isinstance(value, list):
        c=[canonicalize(v) for v in value]
        if all(isinstance(v,(str,int,float,bool,type(None))) for v in c):
            return sorted(c, key=lambda x: json.dumps(x, sort_keys=True))
        return c
    return value


def stable_hash(doc, exclude=()):
    c=deepcopy(doc)
    for k in exclude:
        c.pop(k,None)
    b=json.dumps(canonicalize(c), sort_keys=True, separators=(",",":"))
    return "sha256:"+hashlib.sha256(b.encode()).hexdigest()


def scan(obj,path="$",errors=None):
    errors=errors or []
    if isinstance(obj, dict):
        for k,v in obj.items():
            if k in FORBIDDEN_FIELDS:
                errors.append(f"forbidden field at {path}.{k}")
            scan(v,f"{path}.{k}",errors)
    elif isinstance(obj,list):
        for i,v in enumerate(obj):
            scan(v,f"{path}[{i}]",errors)
    elif isinstance(obj,str):
        low=obj.lower()
        for p in FORBIDDEN_PHRASES:
            if p in low:
                errors.append(f"forbidden language '{p}' at {path}")
    return errors


def validate_publication_package(doc, replay=None):
    e=[]
    e.extend(scan(doc))
    if not doc.get("kfm:spec_hash"): e.append("missing kfm:spec_hash")
    for req in ["source_evidence_bundle_ids","download_keys","query_predicate_hashes","geoprivacy_receipt_refs","answer_receipt_refs"]:
        if not doc.get(req): e.append(f"missing {req}")
    if doc.get("release_posture")=="published":
        if doc.get("rights_posture")!="public_allowed": e.append("published package requires rights_posture public_allowed")
        if doc.get("sensitivity_posture")=="restricted": e.append("published package cannot be restricted sensitivity")
        if doc.get("presence_posture")!="reported_occurrence_not_confirmed_presence": e.append("published package invalid presence posture")
        if replay and replay.get("verification_posture")!="verified": e.append("published state requires verified replay")
    return e


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--kind", choices=["publication_package","publication_status","audit_ledger","replay_verification","correction_receipt","withdrawal_receipt"], required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--replay-verification")
    a=ap.parse_args()
    doc=json.loads(Path(a.input).read_text())
    errs=[]
    if a.kind=="publication_package":
        replay=json.loads(Path(a.replay_verification).read_text()) if a.replay_verification else None
        errs=validate_publication_package(doc,replay)
    if a.kind=="publication_status":
        if doc.get("current_state")=="withdrawn" and not doc.get("withdrawal_receipt_refs"): errs.append("withdrawn state requires withdrawal receipt")
        if doc.get("current_state")=="corrected" and not doc.get("correction_receipt_refs"): errs.append("corrected state requires correction receipt")
        if doc.get("current_state")=="corrected" and not doc.get("superseded_by"): errs.append("corrected package without supersession linkage")
    if a.kind=="audit_ledger":
        if not doc.get("policy_version"): errs.append("audit ledger entry missing policy_version")
        if not doc.get("decision"): errs.append("audit ledger entry missing decision")
        if not doc.get("input_artifact_hashes") or not doc.get("output_artifact_hashes"): errs.append("audit ledger entry missing artifact hashes")
    if a.kind=="replay_verification":
        if doc.get("verification_posture")=="verified" and any(not c.get("passed") for c in doc.get("checks",[])): errs.append("verified replay has failed checks")
    if a.kind=="correction_receipt":
        if not doc.get("changed_fields"): errs.append("correction receipt missing changed_fields")
        if doc.get("reviewer_required") and not doc.get("reviewer",{}).get("actor_id"): errs.append("correction reviewer required")
    if a.kind=="withdrawal_receipt":
        if doc.get("public_use_allowed") is not False: errs.append("withdrawal receipt must set public_use_allowed false")
    if errs:
        print("\n".join(errs)); raise SystemExit(1)
    print("ok")

if __name__=="__main__":
    main()
