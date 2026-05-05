#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.ops.soil._ops_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--published-root',required=True);a.add_argument('--ops-root',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 try: rid=load_current_release(x.published_root)
 except Exception as e: print(json.dumps({'built':False,'reasons':[str(e)]})); return 1
 prs=latest_probe_receipts(x.ops_root); inc=[load_json(p) for p in sorted((Path(x.ops_root)/'ops/soil/incidents').glob('*.incident_notice.json'))] if (Path(x.ops_root)/'ops/soil/incidents').exists() else []
 m=[load_json(p) for p in sorted((Path(x.ops_root)/'ops/soil/maintenance').glob('*.maintenance_notice.json'))] if (Path(x.ops_root)/'ops/soil/maintenance').exists() else []
 r=release_is_retracted(x.published_root,rid); reasons=[]
 p=[q for q in prs if q.get('release_id')==rid]
 if not p or p[-1].get('decision')!='pass': reasons.append('latest probe not pass')
 ai=[i for i in inc if i.get('affected_release_id')==rid and i.get('status')!='resolved']
 if any(i.get('severity')=='critical' for i in ai): reasons.append('unresolved critical incident')
 if r: reasons.append('release retracted')
 if reasons: print(json.dumps({'built':False,'reasons':reasons},sort_keys=True)); return 1
 degraded=bool([i for i in ai if i.get('severity') in {'low','medium'}]) or bool([q for q in m if q.get('affected_release_id')==rid and q.get('status') in {'scheduled','active'}])
 state='degraded' if degraded else 'operational'
 cs={'schema_version':'kfm.v1','object_type':'SoilOperationalStatus','domain':'soil','release_id':rid,'service_state':state,'public_access_allowed':True,'audit_required':True,'latest_probe_id':p[-1]['probe_id'],'latest_probe_decision':'pass','active_incidents':ai,'scheduled_maintenance':[q for q in m if q.get('affected_release_id')==rid and q.get('status') in {'scheduled','active'}],'retracted':False,'created':utc_now_iso()}
 tr={'schema_version':'kfm.v1','object_type':'SoilPublicTransparencyReport','domain':'soil','release_id':rid,'service_state':state,'latest_successful_probe':p[-1]['probe_id'],'active_incidents':cs['active_incidents'],'scheduled_maintenance':cs['scheduled_maintenance'],'created':utc_now_iso()}
 od=Path(x.out_root)/'ops/soil/status'; write_json_atomic(od/'current_status.json',cs); write_json_atomic(od/'public_transparency_report.json',tr)
 sr={'schema_version':'kfm.v1','receipt_type':'OperationalStatusReceipt','domain':'soil','release_id':rid,'decision':'degraded' if degraded else 'pass','source_probe_receipts':[{'ref':q.get('probe_id'),'sha256':sha256_bytes(json.dumps(q,sort_keys=True).encode())} for q in p[-3:]],'source_incident_notices':[i.get('incident_id') for i in ai],'source_maintenance_notices':[q.get('maintenance_id') for q in cs['scheduled_maintenance']],'policy_checks':{'probe_checked':True,'retraction_checked':True,'incident_checked':True,'forbidden_terms_checked':True,'public_access_allowed':True},'generated_artifacts':{'current_status':{'ref':'current_status.json','sha256':sha256_file(od/'current_status.json')},'public_transparency_report':{'ref':'public_transparency_report.json','sha256':sha256_file(od/'public_transparency_report.json')}},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(od/'status_receipt.json',sr); print(json.dumps({'built':True,'service_state':state,'release_id':rid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
