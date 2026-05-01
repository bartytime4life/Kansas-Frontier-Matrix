#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_review_release_validator import stable_hash, scan_forbidden

def load(p): return json.loads(Path(p).read_text())
def dump(p,d): Path(p).write_text(json.dumps(d,indent=2)+"\n")

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--package',required=True); ap.add_argument('--status',required=True); ap.add_argument('--replay-verification',required=True); ap.add_argument('--audit-ledger-entry',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 p,s,r,aud=load(a.package),load(a.status),load(a.replay_verification),load(a.audit_ledger_entry)
 f=[]
 if not p.get('policy_results',{}).get('passed'): f.append('policy_failed')
 if r.get('verification_posture')!='verified': f.append('replay_failed')
 f.extend(scan_forbidden(p))
 out={"review_queue_item_id":"gbif_review_item_TEST_001","domain":"fauna","source_system":"GBIF","queue_type":"public_publication_review","review_state":"pending_review","publication_package_id":p.get('publication_package_id'),"publication_status_id":s.get('publication_status_id'),"replay_verification_id":r.get('replay_verification_id'),"audit_ledger_entry_refs":[aud.get('audit_ledger_entry_id')],"source_evidence_bundle_ids":p.get('source_evidence_bundle_ids',[]),"download_keys":p.get('download_keys',[]),"answer_ids":p.get('answer_ids',[]),"ui_card_ids":p.get('ui_card_ids',[]),"claim_ids":p.get('claim_ids',[]),"rights_posture":p.get('rights_posture'),'sensitivity_posture':p.get('sensitivity_posture'),'presence_posture':p.get('presence_posture'),'policy_results':p.get('policy_results',{}),'replay_posture':r.get('verification_posture'),'review_required':True,'required_reviewer_roles':['fauna_steward'],'blocking_findings':f,'review_notes':[],'created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','review_queue_item_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
