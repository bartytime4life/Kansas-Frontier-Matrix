#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
FORBIDDEN=["confirmed present","verified present","known population","exact location","site-level record"]

def c(v: Any)->str:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def h(v: Any)->str:return f"sha256:{hashlib.sha256(c(v).encode()).hexdigest()}"
def spec(d:dict[str,Any])->str:
    s={k:v for k,v in d.items() if k not in {"created_at","answer_id"}}
    return h(s)

def abstain(query,reason):
    ans={"answer_id":"abstain","query":query,"answer_posture":"abstain","summary":"Abstained.","claims":[],"limitations":[],"abstain_reason":reason,"created_at":datetime.now(timezone.utc).isoformat()}
    ans["kfm:spec_hash"]=spec(ans);return ans

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--claims',required=True);ap.add_argument('--taxon-key');ap.add_argument('--scientific-name');ap.add_argument('--geography-id');ap.add_argument('--aggregation-unit',default='county');ap.add_argument('--query-text',default='');ap.add_argument('--output',required=True);args=ap.parse_args()
    query={"taxon_key":args.taxon_key,"scientific_name":args.scientific_name,"geography_id":args.geography_id,"aggregation_unit":args.aggregation_unit}
    qt=args.query_text.lower()
    if 'exact coordinate' in qt or 'decimallatitude' in qt: ans=abstain(query,'exact_coordinate_request')
    elif 'confirmed present' in qt or 'verified present' in qt: ans=abstain(query,'confirmed_presence_request')
    else:
      claims=json.loads(Path(args.claims).read_text()); matches=[]
      for cl in claims:
        if args.taxon_key and cl['subject'].get('taxon_key')!=args.taxon_key: continue
        if args.scientific_name and cl['subject'].get('scientific_name')!=args.scientific_name: continue
        if args.geography_id and cl['object'].get('geography_id')!=args.geography_id: continue
        if cl['object'].get('aggregation_unit')!=args.aggregation_unit: continue
        ev=cl.get('evidence',{})
        qf=cl.get('qualifiers',{})
        if qf.get('rights_posture')!='public_allowed' or qf.get('sensitivity_posture')=='restricted': continue
        if not all([ev.get('source_evidence_bundle_id'),ev.get('download_key'),ev.get('geoprivacy_receipt_ref'),cl.get('kfm:spec_hash')]): continue
        matches.append({"claim_id":cl['claim_id'],"claim_text":cl.get('claim_text','GBIF-reported public occurrence aggregate'),"presence_posture":qf.get('presence_posture'),'citations':[{"source_system":"GBIF","source_evidence_bundle_id":ev['source_evidence_bundle_id'],"download_key":ev['download_key'],"source_aggregate_id":ev.get('source_aggregate_id'),"geoprivacy_receipt_ref":ev['geoprivacy_receipt_ref'],"kfm:spec_hash":ev.get('kfm:spec_hash')}]})
      if not matches: ans=abstain(query,'no_matching_cited_claim')
      else:
        ans={"answer_id":"gbif-answer-1","query":query,"answer_posture":"cited_answer","summary":"Cited GBIF-reported public occurrence aggregate results.","claims":matches,"limitations":[],"abstain_reason":None,"created_at":datetime.now(timezone.utc).isoformat()}
        ans['kfm:spec_hash']=spec(ans)
    Path(args.output).write_text(json.dumps(ans,indent=2))

if __name__=='__main__':main()
