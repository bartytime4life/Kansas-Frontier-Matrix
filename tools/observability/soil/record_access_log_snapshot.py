#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT)) if str(ROOT) not in sys.path else None
from tools.observability.soil._delivery_observability_common import *
ALLOWED={'schema_version','object_type','created','method','route_template','status','release_id','routing_id','delivery_id','response_bytes','error_category'}
def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--delivery-root',required=True);a.add_argument('--delivery-id');a.add_argument('--snapshot-id');a.add_argument('--access-log',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 did=x.delivery_id or load_current_public_delivery(x.delivery_root)['active_delivery_id']; sid=sanitize_id(x.snapshot_id or f'{did}-snapshot')
 bad=[]; rows=[]
 for ln in Path(x.access_log).read_text(encoding='utf-8').splitlines():
  if not ln.strip(): continue
  e=json.loads(ln)
  if set(e)-ALLOWED: bad.append('unexpected fields'); continue
  if scan_access_log_for_private_fields(e) or scan_payload_for_forbidden_terms(e) or scan_payload_for_contact_or_secret_terms(e): bad.append('unsafe entry'); continue
  if has_private_path(e.get('route_template','')): bad.append('private path'); continue
  rows.append(e)
 if bad:
  print(json.dumps({'public_safe':False,'delivery_id':did,'reasons':sorted(set(bad))})); return 1
 ag={}
 for r in rows:
  k=(r.get('route_template'),int(r.get('status',0)),r.get('error_category') or 'none'); ag[k]=ag.get(k,0)+1
 aggregated=[{'route_template':k[0],'status':k[1],'error_category':k[2],'count':v} for k,v in sorted(ag.items())]
 outd=Path(x.out_root)/f'observability/soil/access_snapshots/{did}'; outd.mkdir(parents=True,exist_ok=True)
 snap={'schema_version':'kfm.v1','object_type':'SoilPublicSafeAccessLogSnapshot','domain':'soil','snapshot_id':sid,'delivery_id':did,'entry_count':len(rows),'aggregated_routes':aggregated,'public_safe':True,'unsafe_entry_count':0,'created':utc_now_iso()}
 receipt={'schema_version':'kfm.v1','receipt_type':'SoilAccessLogSnapshotReceipt','domain':'soil','snapshot_id':sid,'delivery_id':did,'decision':'pass','snapshot_sha256':stable_payload_hash(snap),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(outd/f'{sid}.access_log_snapshot.json',snap); write_json_atomic(outd/f'{sid}.access_log_snapshot_receipt.json',receipt)
 print(json.dumps({'public_safe':True,'delivery_id':did,'snapshot_id':sid})); return 0
if __name__=='__main__': raise SystemExit(main())
