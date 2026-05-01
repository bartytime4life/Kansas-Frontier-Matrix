#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path
from tools.validators.hydrology.validate_huc12_comid_catalog_record import validate

LIFECYCLE_RE = re.compile(r"/(raw|work|quarantine)/", re.IGNORECASE)

def parse_args():
    p=argparse.ArgumentParser()
    p.add_argument("--catalog-jsonl", required=True)
    p.add_argument("--huc12", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--snapshot-id")
    p.add_argument("--include-revoked", action="store_true")
    p.add_argument("--require-published", action="store_true", default=True)
    return p.parse_args()

def parse_day(v:str)->datetime:
    try: return datetime.strptime(v, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError as e: raise ValueError(f"invalid date format, expected YYYY-MM-DD: {e}")
def parse_ts(v:str)->datetime: return datetime.fromisoformat(v.replace("Z","+00:00"))

def resolve(catalog_jsonl:Path,huc12:str,date:str,snapshot_id:str|None=None,include_revoked:bool=False,require_published:bool=True)->dict:
    errors=[]; day=parse_day(date)
    schema=Path("schemas/hydrology/huc12_comid_catalog_record.schema.json")
    recs=[]
    for line in catalog_jsonl.read_text().splitlines():
        if not line.strip(): continue
        rec=json.loads(line)
        if schema.exists() and not validate_record_ok(rec, schema):
            continue
        recs.append(rec)
    matches=[]
    for r in recs:
        if r.get("huc12")!=huc12: continue
        if snapshot_id and r.get("snapshot_id")!=snapshot_id: continue
        if require_published and r.get("release_state")!="published": continue
        if not include_revoked and r.get("release_state")=="revoked": continue
        if any(LIFECYCLE_RE.search(r.get(k,"")) for k in ["published_manifest_uri","published_crosswalk_uri","evidence_bundle_uri"]):
            errors.append("lifecycle leakage in published uri fields"); continue
        if parse_ts(r["valid_from"])<=day<=parse_ts(r["valid_to"]): matches.append(r)
    uniq={json.dumps(m,sort_keys=True,separators=(",",":")):m for m in matches}
    matches=[uniq[k] for k in sorted(uniq.keys())]
    if len(matches)==0: return {"ok":False,"errors":errors+["no matching timeslice"],"selected":None,"evidence_drawer":None}
    if len(matches)>1: return {"ok":False,"errors":errors+["multiple conflicting matches"],"selected":None,"evidence_drawer":None}
    s=matches[0]
    selected={k:s[k] for k in ["manifest_id","timeslice_id","huc12","snapshot_id","nhd_snapshot_id","valid_from","valid_to","published_manifest_uri","published_crosswalk_uri","crosswalk_digest"]}
    return {"ok":True,"errors":[],"selected":selected,"evidence_drawer":s["evidence_drawer"]}

def validate_record_ok(rec,schema_path:Path)->bool:
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        rp=Path(d)/"r.json"; rp.write_text(json.dumps(rec))
        res=validate(rp,schema_path)
        return res["ok"]

def main():
    a=parse_args(); r=resolve(Path(a.catalog_jsonl),a.huc12,a.date,a.snapshot_id,a.include_revoked,a.require_published)
    print(json.dumps(r,sort_keys=True,separators=(",",":")))
    return 0 if r["ok"] else 1
if __name__=="__main__": raise SystemExit(main())
