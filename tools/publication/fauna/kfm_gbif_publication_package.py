#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash, scan

def load(p): return json.loads(Path(p).read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--evidencebundle',required=True);ap.add_argument('--aggregates',required=True);ap.add_argument('--geoprivacy-receipt',required=True)
    ap.add_argument('--catalog',required=True);ap.add_argument('--claims',required=True);ap.add_argument('--answer',required=True);ap.add_argument('--ui-cards',required=True);ap.add_argument('--answer-receipt',required=True);ap.add_argument('--output',required=True)
    a=ap.parse_args()
    eb=load(a.evidencebundle); ag=load(a.aggregates); gp=load(a.geoprivacy_receipt); cat=load(a.catalog); cl=load(a.claims); ans=load(a.answer); ui=load(a.ui_cards); ar=load(a.answer_receipt)
    errs=scan({"aggregates":ag,"answer":ans,"ui":ui})
    if not ar: errs.append('missing answer receipt')
    if not gp: errs.append('missing geoprivacy receipt')
    if errs:
        print('\n'.join(errs)); raise SystemExit(1)
    pkg={
      "publication_package_id":"gbif_pubpkg_TEST_001","domain":"fauna","source_system":"GBIF","package_type":"public_occurrence_answer_package","lifecycle_state":"PUBLICATION_PACKAGE","release_posture":"public_candidate",
      "source_evidence_bundle_ids":[eb.get('evidence_bundle_id')],"download_keys":[eb.get('download_key')],"query_predicate_hashes":[eb.get('query_predicate_hash')],"public_aggregate_ids":[x.get('aggregate_id') for x in ag],"geoprivacy_receipt_refs":[gp.get('receipt_id')],"catalog_entry_ids":[x.get('catalog_entry_id') for x in cat],"claim_ids":[x.get('claim_id') for x in cl],"answer_ids":[ans.get('answer_id')],"answer_receipt_refs":[ar.get('answer_receipt_id')],"ui_card_ids":[x.get('ui_card_id') for x in ui],"map_layer_ids":[],
      "rights_posture":ans.get('rights_posture','public_allowed'),"sensitivity_posture":ans.get('sensitivity_posture','public_generalized'),"presence_posture":"reported_occurrence_not_confirmed_presence",
      "policy_results":{"policy_version":"gbif_publication_ops.v1","passed":True,"deny_count":0,"denies":[]},
      "artifact_hashes":{"evidencebundle":[stable_hash(eb)],"public_aggregates":[stable_hash(ag)],"geoprivacy_receipts":[stable_hash(gp)],"catalog_entries":[stable_hash(cat)],"triplet_claims":[stable_hash(cl)],"runtime_answers":[stable_hash(ans)],"ui_cards":[stable_hash(ui)],"answer_receipts":[stable_hash(ar)]},
      "limitations":["GBIF occurrence aggregates are reported occurrence evidence, not confirmed species-presence determinations.","Public output is generalized and does not expose exact occurrence coordinates."],
      "created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    pkg["kfm:spec_hash"]=stable_hash(pkg,exclude=("created_at","publication_package_id","kfm:spec_hash"))
    Path(a.output).write_text(json.dumps(pkg,indent=2)+"\n")
    print("ok")
if __name__=='__main__': main()
