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
 ap=argparse.ArgumentParser(); ap.add_argument('--package',required=True); ap.add_argument('--review-item',required=True); ap.add_argument('--review-decision',required=True); ap.add_argument('--release-registry',required=True); ap.add_argument('--manifest',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 p,i,d,r,m=[load(x) for x in [a.package,a.review_item,a.review_decision,a.release_registry,a.manifest]]
 checks=[('steward_approved',d.get('decision')=='approve_publish'),('policy_passed',i.get('policy_results',{}).get('passed')==True),('replay_verified',i.get('replay_posture')=='verified'),('manifest_public_safe',len(scan_forbidden(m))==0),('citation_index_present',bool(m.get('citation_index')))]
 failed=[n for n,pas in checks if not pas]
 out={'release_gate_result_id':'gbif_release_gate_TEST_001','gate_name':'gbif_public_release_gate','gate_version':'gbif_review_release.v1','publication_package_id':p.get('publication_package_id'),'review_queue_item_id':i.get('review_queue_item_id'),'review_decision_receipt_id':d.get('review_decision_receipt_id'),'release_registry_entry_id':r.get('release_registry_entry_id'),'manifest_id':m.get('manifest_id'),'gate_posture':'passed' if not failed else 'failed','checks':[{'check_name':n,'passed':pas,'details':[]} for n,pas in checks],'failed_checks':failed,'created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','release_gate_result_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
