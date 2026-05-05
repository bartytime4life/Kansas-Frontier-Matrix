#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

def c(v: Any)->str: return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def h(v: Any)->str: return f"sha256:{hashlib.sha256(c(v).encode()).hexdigest()}"
def spec(d: dict[str,Any])->str:
    s={k:v for k,v in d.items() if k!="created_at"}
    if "limitations" in s: s["limitations"]=sorted(s["limitations"])
    return h(s)

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--catalog',required=True); ap.add_argument('--aggregates',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    catalog=json.loads(Path(a.catalog).read_text()); aggs=json.loads(Path(a.aggregates).read_text())
    claims=[]
    for agg in aggs:
        claim={
            "claim_id":f"gbif-claim-{agg['aggregate_id']}",
            "subject":{"type":"taxon","taxon_key":agg["taxon_key"],"scientific_name":agg["scientific_name"]},
            "predicate":"has_public_gbif_occurrence_aggregate",
            "object":{"type":"geography","aggregation_unit":agg["aggregation_unit"],"geography_id":agg["geography_id"],"display_name":agg["display_name"]},
            "qualifiers":{"observation_count":agg["observation_count"],"record_count":agg["record_count"],"date_range":agg["date_range"],"basis":"GBIF occurrence aggregate","presence_posture":"reported_occurrence_not_confirmed_presence","geometry_role":"generalized_public_area","rights_posture":agg["rights_posture"],"sensitivity_posture":agg["sensitivity_posture"]},
            "claim_text":f"GBIF-reported public occurrence aggregate for {agg['scientific_name']} in {agg['display_name']} ({agg['aggregation_unit']}).",
            "evidence":{"source_system":"GBIF","source_evidence_bundle_id":agg["source_evidence_bundle_id"],"download_key":agg["download_key"],"query_predicate_hash":agg["query_predicate_hash"],"source_aggregate_id":agg["aggregate_id"],"geoprivacy_receipt_ref":agg["geoprivacy_receipt_ref"],"kfm:spec_hash":agg.get("kfm:spec_hash") or h({k:v for k,v in agg.items() if k!="created_at"})},
            "limitations":["Occurrence records may include observer/reporting bias.","Aggregate is not a verified conservation-status determination.","Aggregate is not exact-location evidence."],
            "kfm:spec_hash":"",
            "created_at":datetime.now(timezone.utc).isoformat()
        }
        claim["kfm:spec_hash"]=spec(claim); claims.append(claim)
    Path(a.output).write_text(json.dumps(claims,indent=2))

if __name__=='__main__': main()
