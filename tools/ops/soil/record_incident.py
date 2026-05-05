#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.ops.soil._ops_common import *
T={'availability','quality','rights','provenance','security','maintenance'};S={'low','medium','high','critical'};ST={'investigating','mitigated','resolved'}
def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--ops-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--incident',required=True);x=a.parse_args(argv)
 d=load_json(x.incident); rid=d.get('affected_release_id'); reasons=[]
 if d.get('incident_type') not in T or d.get('severity') not in S or d.get('status') not in ST: reasons.append('invalid enum')
 if (d.get('steward_review') or {}).get('decision')!='approved': reasons.append('missing steward approval')
 if not d.get('public_message'): reasons.append('missing public_message')
 if scan_text_for_forbidden_terms((d.get('summary') or '')+' '+(d.get('public_message') or '')): reasons.append('forbidden terms')
 if not (Path(x.published_root)/'published/soil/releases'/str(rid)).exists(): reasons.append('affected release missing')
 pa=not ((d.get('severity')=='critical' and d.get('status') in {'investigating','mitigated'}) or (d.get('severity')=='high' and d.get('incident_type') in {'security','rights'} and d.get('status')!='resolved'))
 iid=sanitize_id(d.get('incident_id') or deterministic_probe_id(d).replace('probe-','incident-'))
 if reasons: print(json.dumps({'recorded':False,'reasons':reasons},sort_keys=True)); return 1
 n={'schema_version':'kfm.v1','object_type':'SoilIncidentNotice','domain':'soil','incident_id':iid,'incident_type':d['incident_type'],'severity':d['severity'],'status':d['status'],'affected_release_id':rid,'public_access_allowed':pa,'summary':d['summary'],'public_message':d['public_message'],'evidence_refs':d.get('evidence_refs',[]),'created':utc_now_iso()}
 r={'schema_version':'kfm.v1','receipt_type':'IncidentReceipt','domain':'soil','incident_id':iid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 root=Path(x.ops_root)/'ops/soil/incidents'; write_json_atomic(root/f'{iid}.incident_notice.json',n); write_json_atomic(root/f'{iid}.incident_receipt.json',r); print(json.dumps({'recorded':True,'incident_id':iid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
