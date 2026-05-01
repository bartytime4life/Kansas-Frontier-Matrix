#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.accountability.soil._accountability_common import *
def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--accountability-root',required=True); a.add_argument('--assurance-root',required=True); a.add_argument('--response',required=True); a.add_argument('--assurance-id');x=a.parse_args(argv)
 aid=x.assurance_id or load_current_assurance(x.assurance_root)['active_assurance_id']; p=load_json(x.response)
 if p.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'accepted':False,'reasons':['missing steward approval']})); return 1
 rid='rs-'+stable_payload_hash(p)[:16]; out=Path(x.accountability_root)/f'accountability/soil/responses/{aid}'
 n={'schema_version':'kfm.v1','object_type':'SoilAccountabilityResponseNotice','domain':'soil','response_id':rid,**{k:p.get(k) for k in ['target_type','target_id','response_type','public_message','evidence_refs','recommended_action']},'created':utc_now_iso()}
 write_json_atomic(out/f'{rid}.response_notice.json',n); write_json_atomic(out/f'{rid}.response_receipt.json',{'schema_version':'kfm.v1','receipt_type':'AccountabilityResponseReceipt','response_id':rid,'response_notice_hash':'sha256:'+stable_payload_hash(n),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}); print(json.dumps({'accepted':True,'response_id':rid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
