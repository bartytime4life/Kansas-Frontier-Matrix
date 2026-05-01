#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')

def load_materialization(dirs,name):
 for d in dirs:
  p=Path(d)/name
  if p.exists(): return p,json.loads(p.read_text())
 raise SystemExit(f'missing {name}')

def main():
 p=argparse.ArgumentParser();p.add_argument('--materialization-dir',action='append',default=[]);p.add_argument('--materialization-ledger',required=True);p.add_argument('--materialization-postcheck',required=True);p.add_argument('--materialization-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--source-read-model-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-plan',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 post=json.loads(Path(a.materialization_postcheck).read_text());aud=json.loads(Path(a.materialization_audit).read_text());led=json.loads(Path(a.materialization_ledger).read_text())
 if post.get('result') in {'deny','blocked'} or aud.get('result') in {'deny','blocked'} or not led.get('chain_hash'): raise SystemExit('DENY')
 req={n:load_materialization(a.materialization_dir,n)[0] for n in ['reentry_public_read_model_refresh_request.json','reentry_publication_delta_seed.json','reentry_publication_receipt_candidate.json','reentry_publication_artifact_preview_manifest.json','reentry_publication_manifest_finalization_candidate.json']}
 asof=a.as_of or now(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 plan={'schema_version':'v1','refresh_plan_id':'rpr-'+hashlib.sha256(asof.encode()).hexdigest()[:10],'domain':'atmosphere.air','created_at':now(),'as_of':asof,'public_read_model_refresh_request_ref':str(req['reentry_public_read_model_refresh_request.json']),'publication_delta_seed_ref':str(req['reentry_publication_delta_seed.json']),'publication_receipt_candidate_ref':str(req['reentry_publication_receipt_candidate.json']),'artifact_preview_manifest_ref':str(req['reentry_publication_artifact_preview_manifest.json']),'publication_manifest_finalization_candidate_ref':str(req['reentry_publication_manifest_finalization_candidate.json']),'materialization_postcheck_report_ref':a.materialization_postcheck,'materialization_audit_report_ref':a.materialization_audit,'materialization_ledger_manifest_ref':a.materialization_ledger,'source_read_model_refs':[],'planned_read_model_artifacts':[{'artifact_type':'candidate','target_path':str(out/'reentry_public_index_refresh_candidate.json'),'source_ref':str(req['reentry_publication_receipt_candidate.json']),'candidate_only':True,'immutable_preview':True}], 'planned_delta_artifacts':[],'planned_invalidation_artifacts':[],'non_mutation_guarantees':['no published writes'],'forbidden_actions':['publish','deploy'],'safety_checks':{'fixture_only':True},'status':'fixture_refresh_plan'}
 if not a.dry_run: (out/'reentry_public_read_model_refresh_plan.json').write_text(json.dumps(plan,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
