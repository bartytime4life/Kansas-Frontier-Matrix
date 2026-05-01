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
 ap=argparse.ArgumentParser(); ap.add_argument('--package',required=True); ap.add_argument('--status',required=True); ap.add_argument('--review-decision',required=True); ap.add_argument('--release-channel',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 p,s,d=load(a.package),load(a.status),load(a.review_decision)
 state='published' if d.get('decision')=='approve_publish' else 'blocked'
 out={'release_registry_entry_id':'gbif_release_TEST_001','domain':'fauna','source_system':'GBIF','release_channel':a.release_channel,'release_state':state,'publication_package_id':p.get('publication_package_id'),'publication_status_id':s.get('publication_status_id'),'review_decision_receipt_id':d.get('review_decision_receipt_id'),'exception_receipt_refs':[],'source_evidence_bundle_ids':p.get('source_evidence_bundle_ids',[]),'download_keys':p.get('download_keys',[]),'query_predicate_hashes':p.get('query_predicate_hashes',[]),'public_aggregate_ids':p.get('public_aggregate_ids',[]),'geoprivacy_receipt_refs':p.get('geoprivacy_receipt_refs',[]),'catalog_entry_ids':p.get('catalog_entry_ids',[]),'claim_ids':p.get('claim_ids',[]),'answer_ids':p.get('answer_ids',[]),'answer_receipt_refs':p.get('answer_receipt_refs',[]),'ui_card_ids':p.get('ui_card_ids',[]),'map_layer_ids':[],'artifact_hashes':{'publication_package':p.get('kfm:spec_hash'),'review_decision_receipt':d.get('kfm:spec_hash'),'public_manifest':'sha256:TBD'},'rights_posture':p.get('rights_posture'),'sensitivity_posture':p.get('sensitivity_posture'),'presence_posture':p.get('presence_posture'),'public_url_paths':[f"/fauna/gbif/occurrence-aggregates/{p.get('publication_package_id')}"],'supersedes':[],'superseded_by':None,'withdrawal_receipt_refs':[],'correction_receipt_refs':[],'created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','release_registry_entry_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
