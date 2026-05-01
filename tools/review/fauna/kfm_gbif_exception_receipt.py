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
 ap=argparse.ArgumentParser(); ap.add_argument('--package',required=True); ap.add_argument('--exception-type',required=True); ap.add_argument('--allowed-effect',required=True); ap.add_argument('--reason',required=True); ap.add_argument('--reviewer'); ap.add_argument('--reviewer-role',action='append',default=[]); ap.add_argument('--output',required=True); a=ap.parse_args()
 p=load(a.package)
 if not a.reviewer: raise SystemExit(1)
 out={'exception_receipt_id':'gbif_exception_TEST_001','exception_type':a.exception_type,'publication_package_id':p.get('publication_package_id'),'scope':{'artifact_ids':[p.get('publication_package_id')],'dataset_keys':['TEST_DATASET_KEY'],'taxon_keys':['TEST_TAXON_KEY'],'geography_ids':['KS-DOUGLAS'],'expires_at':'2026-12-31T23:59:59Z'},'exception_reason':a.reason,'allowed_effect':a.allowed_effect,'not_allowed_to_override':['exact_coordinate_leak','missing_citation','missing_geoprivacy_receipt','restricted_sensitivity','confirmed_presence_language'],'reviewer_required':True,'reviewer':{'actor_type':'steward','actor_id':a.reviewer,'roles':a.reviewer_role},'approval_basis':'documented_steward_review','audit_ledger_entry_ref':'gbif_audit_EXCEPTION_TEST_001','created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','exception_receipt_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
