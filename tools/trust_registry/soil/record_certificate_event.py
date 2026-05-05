#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.trust_registry.soil._trust_registry_common import *
from tools.validators.soil.trust_registry_check import main as rcheck
ALLOWED={'suspend':'suspended','reinstate':'active','revoke':'revoked','tombstone':'tombstoned'}

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--registry-root',required=True); a.add_argument('--published-root',required=True); a.add_argument('--ops-root',required=True); a.add_argument('--event',required=True); a.add_argument('--registry-id'); a.add_argument('--out-root',required=True); x=a.parse_args(argv)
 if rcheck(['--registry-root',x.registry_root]+(['--registry-id',x.registry_id] if x.registry_id else []))!=0: print(json.dumps({'event_recorded':False,'reasons':['registry invalid']})); return 1
 e=load_json(x.event); et=e.get('event_type'); fail=[]
 if et not in ALLOWED: fail.append('unknown event_type')
 if e.get('steward_review',{}).get('decision')!='approved': fail.append('missing steward approval')
 if not e.get('public_message'): fail.append('missing public message')
 if scan_payload_for_forbidden_terms(e): fail.append('forbidden terms')
 root=Path(x.registry_root)/'trust_registry/soil'; rid=x.registry_id or load_json(root/'current_registry.json')['active_registry_id']; m=load_json(root/f'registrations/{rid}/registry_manifest.json')
 if et=='reinstate' and release_is_retracted(x.published_root,m.get('release_id')): fail.append('retracted')
 if fail: print(json.dumps({'event_recorded':False,'registry_id':rid,'reasons':fail},sort_keys=True)); return 1
 eid=f"{utc_now_iso().replace(':','').replace('-','')}_{sanitize_id(et)}"
 status={'schema_version':'kfm.v1','object_type':'SoilTrustCertificateStatus','domain':'soil','registry_id':rid,'certification_id':m.get('certification_id'),'release_id':m.get('release_id'),'certificate_status':ALLOWED[et],'public_advertising_allowed':ALLOWED[et]=='active','status_reason':e.get('reason_type'),'status_events':[{'event_type':et,'decision':'pass','ref':f'events/{rid}/{eid}.certificate_event_notice.json','sha256':'pending','created':utc_now_iso()}],'retracted':False,'suspended':ALLOWED[et]=='suspended','revoked':ALLOWED[et]=='revoked','tombstoned':ALLOWED[et]=='tombstoned','created':utc_now_iso()}
 evdir=Path(x.out_root)/f'trust_registry/soil/events/{rid}'; sdir=Path(x.out_root)/'trust_registry/soil/status';
 notice={'schema_version':'kfm.v1','object_type':'SoilTrustCertificateEventNotice','domain':'soil','registry_id':rid,'event_id':eid,'request':e,'result_status':ALLOWED[et],'created':utc_now_iso()}
 receipt={'schema_version':'kfm.v1','receipt_type':'SoilTrustCertificateEventReceipt','domain':'soil','registry_id':rid,'event_id':eid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(evdir/f'{eid}.certificate_event_notice.json',notice); write_json_atomic(evdir/f'{eid}.certificate_event_receipt.json',receipt); write_json_atomic(sdir/f'{rid}.latest_certificate_status.json',status)
 print(json.dumps({'event_recorded':True,'registry_id':rid,'event_id':eid,'certificate_status':ALLOWED[et]},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
