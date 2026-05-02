#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *
def main(argv=None):
 p=argparse.ArgumentParser(); [p.add_argument(a,required=True) for a in ['--resilience-root','--observability-root','--delivery-root','--recommissioning-root','--monitor']]; ns=p.parse_args(argv)
 req=load_json(ns.monitor)
 if scan_payload_for_contact_or_secret_terms(req) or req.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'ok':False})); return 1
 if req.get('monitor_status')=='pass' and not req.get('monitor_receipt_ref'): print(json.dumps({'ok':False,'reasons':['missing receipt']})); return 1
 rid=load_current_public_resilience(ns.resilience_root)['active_resilience_id']; mid=sanitize_id('mon-'+req.get('monitor_type','x'))
 rec={'schema_version':'kfm.v1','object_type':'SoilRevalidationMonitor','domain':'soil','monitor_id':mid,'resilience_id':rid,'monitor_type':req.get('monitor_type'),'monitor_status':req.get('monitor_status'),'monitor_receipt_ref':req.get('monitor_receipt_ref'),'monitor_receipt_sha256':req.get('monitor_receipt_sha256'),'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'created':utc_now_iso()}
 out=Path(ns.recommissioning_root)/f'recommissioning/soil/revalidation_monitors/{rid}/{mid}.revalidation_monitor.json'; write_json_atomic(out,rec); write_json_atomic(str(out).replace('.json','_receipt.json'),{'schema_version':'kfm.v1','receipt_type':'SoilRevalidationMonitorReceipt','monitor_id':mid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}})
 print(json.dumps({'ok':True,'monitor_id':mid})); return 0
if __name__=='__main__': raise SystemExit(main())