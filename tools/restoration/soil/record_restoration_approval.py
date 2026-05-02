#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--restoration-root',required=True); p.add_argument('--recommissioning-id'); p.add_argument('--approval',required=True); ns=p.parse_args(argv)
 rid=ns.recommissioning_id or load_current_delivery_recommissioning(ns.recommissioning_root)['active_recommissioning_id']
 m=load_delivery_recommissioning_manifest(ns.recommissioning_root,rid); a=load_json(ns.approval)
 errs=[]
 if not validate_restoration_approval(a): errs.append('missing steward approval')
 if scan_payload_for_contact_or_secret_terms(a): errs.append('sensitive terms')
 rt=a.get('restoration_type'); st=m.get('recommissioning_state')
 allowed={'recommissioned_active':{'restore_active_delivery','restore_active_with_errata','restore_successor_active'},'recommissioned_governance_only':{'remain_governance_only'},'requires_reprobe':{'require_reprobe'},'requires_routing_rebuild':{'require_routing_rebuild'},'blocked':{'blocked'}}
 if rt not in allowed.get(st,set()): errs.append('restoration type disallowed')
 if rt in {'restore_active_delivery','restore_active_with_errata','restore_successor_active'} and not a.get('monitor_receipt_refs'): errs.append('missing monitor evidence')
 if errs: print(json.dumps({'recorded':False,'reasons':errs})); return 1
 aid=sanitize_id(a.get('approval_id') or f"{rid}-{stable_payload_hash(a)[:12]}")
 out=Path(ns.restoration_root)/f'restoration/soil/approvals/{rid}/{aid}.restoration_approval.json'; rec=Path(str(out).replace('.json','_receipt.json'))
 a['recommissioning_id']=rid; write_json_atomic(out,a)
 write_json_atomic(rec,{'schema_version':'kfm.v1','receipt_type':'SoilDeliveryRestorationApprovalReceipt','approval_id':aid,'recommissioning_id':rid,'decision':'approved','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}})
 print(json.dumps({'recorded':True,'approval_id':aid,'approval_ref':str(out),'receipt_ref':str(rec)})); return 0
if __name__=='__main__': raise SystemExit(main())
