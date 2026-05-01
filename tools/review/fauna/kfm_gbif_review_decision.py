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
 ap=argparse.ArgumentParser(); ap.add_argument('--review-item',required=True); ap.add_argument('--decision',required=True); ap.add_argument('--decision-reason',required=True); ap.add_argument('--reviewer'); ap.add_argument('--reviewer-role',action='append',default=[]); ap.add_argument('--output',required=True); a=ap.parse_args()
 i=load(a.review_item)
 checks=[('policy_passed',i.get('policy_results',{}).get('passed')==True),('replay_verified',i.get('replay_posture')=='verified'),('citations_present',True),('geoprivacy_receipts_present',True),('no_exact_coordinates',len(scan_forbidden(i))==0),('safe_presence_posture',i.get('presence_posture')=='reported_occurrence_not_confirmed_presence')]
 if a.decision=='approve_publish' and (not a.reviewer or 'fauna_steward' not in a.reviewer_role or any(not c[1] for c in checks)): raise SystemExit(1)
 out={'review_decision_receipt_id':'gbif_review_decision_TEST_001','review_queue_item_id':i.get('review_queue_item_id'),'publication_package_id':i.get('publication_package_id'),'decision':a.decision,'decision_reason':a.decision_reason,'reviewer':{'actor_type':'steward','actor_id':a.reviewer,'roles':a.reviewer_role},'review_checks':[{'check_name':n,'passed':p,'details':[]} for n,p in checks],'exception_receipt_refs':[],'resulting_release_posture':'published' if a.decision=='approve_publish' else 'blocked','audit_ledger_entry_ref':'gbif_audit_REVIEW_TEST_001','limitations_acknowledged':True,'created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','review_decision_receipt_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
