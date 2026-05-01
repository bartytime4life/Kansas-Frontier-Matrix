#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._remediation_common import load_json, sha256_file, stable_payload_hash

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--remediation-root',required=True); ap.add_argument('--remediation-id'); a=ap.parse_args(argv)
 root=Path(a.remediation_root)/'remediation/soil'; rid=a.remediation_id or load_json(root/'current_remediation_handoff.json')['active_remediation_id']; c=root/'cycles'/rid
 m=load_json(c/'remediation_handoff_manifest.json'); r=load_json(c/'remediation_handoff_receipt.json')
 ok=m.get('object_type')=='SoilRemediationHandoffManifest' and r.get('receipt_type')=='RemediationHandoffReceipt'
 reasons=[]
 for fn,h in m.get('artifact_hashes',{}).items():
  if fn=='remediation_handoff_manifest.json':
   continue
  if sha256_file(c/fn)!=h: ok=False; reasons.append('artifact hash mismatch')
 t=load_json(c/'remediation_transparency_log.json'); prev=None
 for e in t.get('entries',[]):
  x=dict(e); eh=x.pop('entry_hash',None)
  if stable_payload_hash(x)!=eh: ok=False; reasons.append('bad log hash'); break
  prev=eh
 if t.get('log_root')!=prev: ok=False; reasons.append('log root mismatch')
 out={'remediation_handoff_valid':ok,'remediation_id':rid,'corrective_id':m.get('corrective_id'),'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'remediation_state':m.get('remediation_state'),'failure_reasons':reasons}
 print(json.dumps(out,sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
