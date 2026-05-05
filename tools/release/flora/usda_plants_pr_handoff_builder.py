from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json

def main():
 a=argparse.ArgumentParser();a.add_argument('--release-candidate',required=True);a.add_argument('--snapshot-diff',required=True);a.add_argument('--watcher-run-receipt',required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',required=True);x=a.parse_args()
 o={'schema_version':'1.0.0','object_type':'usda_plants_pr_handoff_manifest','handoff_id':f'kfm.pr_handoff.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'branch_suggestion':f'data/usda-plants-{x.snapshot_date}','title_suggestion':f'USDA PLANTS snapshot candidate {x.snapshot_date}','body_summary':['No publication or promotion requested.','Release candidate generated for review.'],'changed_refs':[x.release_candidate,x.snapshot_diff,x.watcher_run_receipt],'required_review_gates':['schema_validation','dataset_validation','policy_validation','proof_manifest','catalog_closure','sensitivity_review'],'blockers':['PUBLICATION_NOT_REQUESTED','PROMOTION_NOT_REQUESTED'],'status':'ready_for_human_review'}
 o['handoff_hash']=canonical_hash(o,'handoff_hash');write_json(Path(x.out),o)
if __name__=='__main__':main()
