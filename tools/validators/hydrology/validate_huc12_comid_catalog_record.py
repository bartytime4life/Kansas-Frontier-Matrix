#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from datetime import datetime
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator

LIFECYCLE_RE = re.compile(r"/(raw|work|quarantine)/", re.IGNORECASE)

def parse_args():
    p=argparse.ArgumentParser()
    p.add_argument("--record", required=True)
    p.add_argument("--schema", required=True)
    p.add_argument("--evidence-bundle")
    p.add_argument("--evidence-schema")
    return p.parse_args()

def load(path:Path)->dict[str,Any]: return json.loads(path.read_text())
def parse_iso(v:str)->datetime: return datetime.fromisoformat(v.replace("Z","+00:00"))

def validate(record_path:Path,schema_path:Path,evidence_bundle_path:Path|None=None,evidence_schema_path:Path|None=None)->dict[str,Any]:
    errors=[]
    rec=load(record_path); schema=load(schema_path)
    for e in sorted(Draft202012Validator(schema).iter_errors(rec), key=lambda x:list(x.path)):
        errors.append(f"schema:{'.'.join(str(p) for p in e.path) or '<root>'}:{e.message}")
    if "valid_from" in rec and "valid_to" in rec:
        if parse_iso(rec["valid_from"])>parse_iso(rec["valid_to"]): errors.append("validity:valid_from must be <= valid_to")
    expected_manifest_id=f"{rec.get('huc12','')}@{rec.get('snapshot_id','')}::{rec.get('spec_hash','')}"
    s=parse_iso(rec.get("valid_from","1970-01-01T00:00:00Z")).strftime("%Y%m%d")
    t=parse_iso(rec.get("valid_to","1970-01-01T00:00:00Z")).strftime("%Y%m%d")
    expected_timeslice=f"huc12::{rec.get('snapshot_id','')}::{s}-{t}"
    if rec.get("manifest_id")!=expected_manifest_id: errors.append("ids:invalid manifest_id")
    if rec.get("timeslice_id")!=expected_timeslice: errors.append("ids:invalid timeslice_id")
    ed=rec.get("evidence_drawer",{})
    for k in ["snapshot_id","nhd_snapshot_id","spec_hash","manifest_id","timeslice_id","manifest_digest","crosswalk_digest","run_receipt_url","evidence_bundle_uri","release_state"]:
        if ed.get(k)!=rec.get(k): errors.append(f"evidence_drawer:mismatch {k}")
    for k in ["published_manifest_uri","published_crosswalk_uri","evidence_bundle_uri"]:
        if LIFECYCLE_RE.search(rec.get(k, "")): errors.append(f"lifecycle:forbidden segment in {k}")
    if evidence_bundle_path and evidence_schema_path:
        eb=load(evidence_bundle_path); es=load(evidence_schema_path)
        for e in sorted(Draft202012Validator(es).iter_errors(eb), key=lambda x:list(x.path)):
            errors.append(f"evidence_schema:{'.'.join(str(p) for p in e.path) or '<root>'}:{e.message}")
        for k in ["manifest_id","timeslice_id","manifest_digest","crosswalk_digest","snapshot_id","nhd_snapshot_id","spec_hash"]:
            if eb.get(k)!=rec.get(k): errors.append(f"evidence_bundle:mismatch {k}")
    return {"ok":not errors,"errors":errors,"manifest_id":rec.get("manifest_id",""),"timeslice_id":rec.get("timeslice_id",""),"release_state":rec.get("release_state","")}

def main()->int:
    a=parse_args(); r=validate(Path(a.record),Path(a.schema),Path(a.evidence_bundle) if a.evidence_bundle else None,Path(a.evidence_schema) if a.evidence_schema else None)
    print(json.dumps(r,sort_keys=True,separators=(",",":")))
    return 0 if r["ok"] else 1
if __name__=="__main__": raise SystemExit(main())
