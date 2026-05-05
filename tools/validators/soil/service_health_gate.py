#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from tools.ops.soil._ops_common import load_json

def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('--status',required=True);p.add_argument('--status-receipt',required=True);a=p.parse_args(argv)
 s=load_json(a.status); r=load_json(a.status_receipt); reasons=[]
 if s.get('object_type')!='SoilOperationalStatus' or s.get('service_state') not in {'operational','degraded'} or s.get('public_access_allowed') is not True or s.get('latest_probe_decision')!='pass' or s.get('retracted') is True: reasons.append('status blocked')
 if r.get('receipt_type')!='OperationalStatusReceipt' or (r.get('policy_checks') or {}).get('public_access_allowed') is not True or not r.get('signatures'): reasons.append('receipt blocked')
 if any(i.get('severity')=='critical' and i.get('status')!='resolved' for i in s.get('active_incidents',[])): reasons.append('critical incident active')
 out={'service_advertising_allowed':not reasons,'release_id':s.get('release_id'),'decision':'pass' if not reasons else 'fail'}
 if reasons: out['reasons']=reasons
 print(json.dumps(out,sort_keys=True)); return 0 if not reasons else 1
if __name__=='__main__': raise SystemExit(main())
