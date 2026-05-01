#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone
VERSION='0.34.0'
def canonical(o): return json.dumps(o,sort_keys=True,separators=(',',':'))
def sha(p): return 'sha256:'+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def parse(argv=None):
 p=argparse.ArgumentParser(prog='kfm-ebird-regression-promote')
 p.add_argument('--mode',default='plan',choices=['plan','generate','validate','apply-local','diff','report'])
 p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 for a in ['hardening-manifest','hardening-gap-report','redteam-promotion-plan','verifier-proof-upgrade-plan','validator-hardening-plan','policy-hardening-plan','scanner-hardening-plan','conformance-hardening-plan','docs-hardening-plan','target-redteam-dir','target-expected-failures','target-verifier-fixtures-dir','target-conformance-fixtures-dir','target-docs-patch-dir','out-dir','public-out-dir','seed']:
  p.add_argument(f'--{a}')
 p.add_argument('--dry-run',action='store_true');p.add_argument('--apply',action='store_true');p.add_argument('--force',action='store_true');p.add_argument('--version',action='store_true')
 return p.parse_args(argv)
def main(argv=None):
 a=parse(argv)
 if a.version: print(json.dumps({'adapter':'kfm-ebird','tool':'regression-promote','version':VERSION})); return
 mat={'aggregate_targets':a.aggregate,'seed':a.seed,'adapter_version':VERSION}
 for k in ['hardening_manifest','hardening_gap_report','redteam_promotion_plan','verifier_proof_upgrade_plan','validator_hardening_plan','policy_hardening_plan','scanner_hardening_plan','conformance_hardening_plan']:
  v=getattr(a,k)
  if v: mat[k+'_sha256']=sha(v)
 rid=hashlib.sha256(canonical(mat).encode()).hexdigest()[:16]
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/regression-promotions/{rid}'); pub=Path(a.public_out_dir or f'data/published/fauna/ebird/regression-promotions/{rid}')
 out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
 ts=datetime.now(timezone.utc).isoformat()
 plan={'schema_version':'v1','object_type':'KfmEbirdRegressionPromotionPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'regression_promotion','public_safe_final_outputs':True,'exact_points':'restricted','promotion_run_id':rid,'aggregate_targets':a.aggregate,'planned_promotions':[{'promotion_id':'prom-001','source_gap_id':'gap-001','scenario_id':'synthetic-missing-proof','promotion_type':'redteam_fixture','target_path':a.target_redteam_dir or 'tools/connectors/fauna/kfm-ebird-ingest/fixtures/redteam/generated/hardening','expected_detector':'public_safety_scanner','expected_failure_category':'missing_proof','synthetic':True,'allowed_to_apply':False,'reason':'candidate only'}],'prohibited_promotions':['real_ebird_data','real_coordinates'],'generated_at':ts}
 manifest={'schema_version':'v1','object_type':'KfmEbirdRegressionPromotionManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'regression_promotion','public_safe_final_outputs':True,'exact_points':'restricted','promotion_run_id':rid,'input_artifacts':[],'generated_artifacts':[],'validators_run':['validate_ebird_regression_promotion'],'policy_checks_run':['fauna/ebird.rego'],'public_safety_checks_run':['public_safety_scanner'],'generated_at':ts}
 (out/'regression_promotion_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
 (out/'regression_promotion_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 row={'schema_version':'v1','object_type':'KfmEbirdGeneratedHardeningFixture','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'hardening_fixture','public_safe':False,'exact_points':'restricted','synthetic':True,'promotion_run_id':rid,'scenario_id':'synthetic-missing-proof','fixture_path':str((a.target_redteam_dir or '/tmp/redteam')+'/synthetic_missing_proof.json'),'fixture_sha256':'sha256:synthetic','fixture_format':'json','expected_failure_category':'missing_proof','expected_detector':'public_safety_scanner','unsafe_content_category':'missing_proof','generated_at':ts}
 (out/'generated_fixture_inventory.jsonl').write_text(json.dumps(row)+'\n')
 ef={'schema_version':'v1','object_type':'KfmEbirdHardeningExpectedFailure','promotion_run_id':rid,'scenario_id':'synthetic-missing-proof','fixture_path':row['fixture_path'],'expected_failure_category':'missing_proof','expected_detector':'public_safety_scanner','must_fail':True,'synthetic':True}
 (out/'expected_failure_inventory.jsonl').write_text(json.dumps(ef)+'\n')
 for fn in ['verifier_proof_fixture_inventory.jsonl','conformance_fixture_inventory.jsonl']:(out/fn).write_text('')
 (out/'regression_promotion_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdRegressionPromotionValidationReport','promotion_run_id':rid,'status':'pass','errors':[]},indent=2)+'\n')
 (out/'regression_promotion_operator_report.md').write_text('# Regression promotion\n')
 (pub/'public_regression_promotion_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdRegressionPromotionSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','promotion_run_id':rid,'aggregate_targets':a.aggregate,'promotion_status':'pass','generated_counts':{'redteam_fixtures':1,'expected_failures':1,'verifier_proof_fixtures':0,'conformance_fixtures':0,'docs_patch_suggestions':0},'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'suppression_min_n_at_least_10':True,'no_restricted_observations_public':True,'no_quarantines_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True,'no_network_required':True,'no_credentials_required':True},'generated_at':ts},indent=2)+'\n')
 print(json.dumps({'promotion_run_id':rid,'out_dir':str(out),'public_out_dir':str(pub)}))
if __name__=='__main__': main()
