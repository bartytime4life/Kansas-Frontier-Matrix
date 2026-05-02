#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--restoration-root',required=True); p.add_argument('--approval',required=True); p.add_argument('--recommissioning-id')
 ns=p.parse_args(argv)
 rid=ns.recommissioning_id or load_current_delivery_recommissioning(ns.recommissioning_root)['active_recommissioning_id']
 mani=load_delivery_recommissioning_manifest(ns.recommissioning_root,rid)
 a=load_json(ns.approval)
 ok,reasons=validate_restoration_approval(a,mani)
 if a.get('recommissioning_id') and a.get('recommissioning_id')!=rid: ok=False; reasons.append('recommissioning mismatch')
 rt=a.get('restoration_type')
 if rt in {'restore_active_delivery','restore_active_with_errata','restore_successor_active'} and not (a.get('monitor_receipt_refs') or a.get('evidence_refs')): ok=False; reasons.append('missing monitor evidence')
 if not ok: print(json.dumps({'approval_recorded':False,'reasons':reasons})); return 1
 aid=sanitize_id(a.get('approval_id') or stable_payload_hash(a)[:16])
 out=Path(ns.restoration_root)/f'restoration/soil/approvals/{rid}'; out.mkdir(parents=True,exist_ok=True)
 ap=out/f'{aid}.restoration_approval.json'; rp=out/f'{aid}.restoration_approval_receipt.json'
 write_json_atomic(ap,a)
 rec={'schema_version':'kfm.v1','receipt_type':'DeliveryRestorationApprovalReceipt','domain':'soil','approval_id':aid,'recommissioning_id':rid,'decision':'approved','approval_ref':str(ap),'approval_sha256':sha256_file(ap),'created':utc_now_iso(),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(rp,rec)
 print(json.dumps({'approval_recorded':True,'approval_id':aid,'outputs':{'approval':str(ap),'receipt':str(rp)}})); return 0
if __name__=='__main__': raise SystemExit(main())
