#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, datetime as dt
from pathlib import Path
from tools.ops.soil._ops_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--ops-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--maintenance',required=True);x=a.parse_args(argv)
 d=load_json(x.maintenance); reasons=[]
 if d.get('maintenance_type') not in {'scheduled','emergency'} or d.get('status') not in {'scheduled','active','completed','cancelled'}: reasons.append('invalid enum')
 if (d.get('steward_review') or {}).get('decision')!='approved': reasons.append('missing steward approval')
 if not d.get('public_message'): reasons.append('missing public_message')
 if scan_text_for_forbidden_terms(d.get('public_message','')): reasons.append('forbidden terms')
 rid=d.get('affected_release_id')
 if not (Path(x.published_root)/'published/soil/releases'/str(rid)).exists(): reasons.append('affected release missing')
 try:
  if d.get('starts_at') and d.get('ends_at') and dt.datetime.fromisoformat(d['starts_at'].replace('Z','+00:00'))>dt.datetime.fromisoformat(d['ends_at'].replace('Z','+00:00')): reasons.append('invalid time range')
 except Exception: reasons.append('invalid time range')
 if reasons: print(json.dumps({'recorded':False,'reasons':reasons},sort_keys=True)); return 1
 mid=sanitize_id(d.get('maintenance_id') or ('maint-'+deterministic_probe_id(d)[6:]))
 n={'schema_version':'kfm.v1','object_type':'SoilMaintenanceNotice','domain':'soil','maintenance_id':mid,**{k:d.get(k) for k in ['maintenance_type','status','affected_release_id','starts_at','ends_at','public_message','public_access_allowed']},'created':utc_now_iso()}
 r={'schema_version':'kfm.v1','receipt_type':'MaintenanceReceipt','domain':'soil','maintenance_id':mid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 root=Path(x.ops_root)/'ops/soil/maintenance'; write_json_atomic(root/f'{mid}.maintenance_notice.json',n); write_json_atomic(root/f'{mid}.maintenance_receipt.json',r); print(json.dumps({'recorded':True,'maintenance_id':mid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
