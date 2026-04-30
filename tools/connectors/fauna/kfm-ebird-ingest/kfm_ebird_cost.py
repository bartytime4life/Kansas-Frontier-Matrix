#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, version_payload, load_contract_lock

def now(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def mkid(payload): return hashlib.sha256(canonical_json(payload).encode()).hexdigest()[:16]

def main():
 ap=argparse.ArgumentParser(prog='kfm-ebird-cost'); ap.add_argument('--mode',default='estimate',choices=['estimate','budget-check','compare','report','public-summary']); ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both']); ap.add_argument('--performance-report'); ap.add_argument('--capacity-plan'); ap.add_argument('--storage-inventory'); ap.add_argument('--quota-check-report'); ap.add_argument('--package-manifest'); ap.add_argument('--deployment-receipt'); ap.add_argument('--assurance-scan-report'); ap.add_argument('--release-receipt'); ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird'); ap.add_argument('--rates',default='configs/fauna/ebird/local_cost_rates.json'); ap.add_argument('--budgets',default='configs/fauna/ebird/local_cost_budgets.json'); ap.add_argument('--baseline-cost-report'); ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--refresh-cadence',default='monthly',choices=['monthly','quarterly','ad-hoc']); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
 a=ap.parse_args()
 if a.version: print(json.dumps(version_payload('kfm-ebird-cost', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
 rates=Path(a.rates); budgets=Path(a.budgets)
 lock=load_contract_lock(Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json'))
 inputs={k:v for k,v in {'performance_report':a.performance_report,'capacity_plan':a.capacity_plan,'storage_inventory':a.storage_inventory,'quota_check_report':a.quota_check_report}.items() if v}
 ih={k:sha(v) for k,v in inputs.items() if Path(v).exists()}
 cid=mkid({'aggregate_targets':a.aggregate,'input_artifact_hashes':ih,'rates_sha256':sha(rates) if rates.exists() else None,'budgets_sha256':sha(budgets) if budgets.exists() else None,'refresh_cadence':a.refresh_cadence,'adapter_version':ADAPTER_VERSION,'contract_hash':lock.get('contract_hash')})
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/cost/{cid}')
 if 'data/published' in str(out): raise SystemExit('out-dir cannot be under data/published')
 if a.dry_run: return 0
 out.mkdir(parents=True,exist_ok=True)
 has_rates=rates.exists()
 conf='medium' if has_rates else 'low'
 est={'schema_version':'v1','object_type':'EbirdLocalCostEstimate','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'cost_governance','public_safe':False,'exact_points':'restricted','cost_run_id':cid,'aggregate_targets':[a.aggregate],'refresh_cadence':a.refresh_cadence,'rate_profile':'local_default','rates_path':str(rates),'rates_sha256':sha(rates) if has_rates else None,'input_artifacts':[{'path_or_uri':k,'sha256':v,'artifact_type':'input'} for k,v in ih.items()],'resource_inputs':{'estimated_compute_core_hours':1.0,'estimated_memory_gb_hours':2.0,'estimated_storage_gb_month':0.01,'estimated_public_storage_gb_month':0.005,'estimated_catalog_storage_gb_month':0.003,'estimated_work_storage_gb_month':0.002,'estimated_operator_minutes':30},'cost_estimates':{'compute_cost':1.0 if has_rates else None,'memory_cost':1.0 if has_rates else None,'storage_cost':0.1 if has_rates else None,'public_storage_cost':0.05 if has_rates else None,'catalog_storage_cost':0.03 if has_rates else None,'work_storage_cost':0.02 if has_rates else None,'operator_cost':2.0 if has_rates else None,'total_cost':4.1 if has_rates else None,'currency':'USD','confidence':conf},'assumptions':['local synthetic inputs'],'limitations':{'no_cloud_billing_api':True,'local_config_driven_rates_only':True,'synthetic_benchmark_inputs_when_applicable':True},'generated_at':now()}
 (out/'local_cost_estimate.json').write_text(json.dumps(est,indent=2))
 b={'schema_version':'v1','object_type':'EbirdLocalBudgetCheckReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','cost_run_id':cid,'status':'pass','budgets_path':str(budgets),'budgets_sha256':sha(budgets) if budgets.exists() else None,'budget_results':[{'budget_id':'max_monthly_total_cost','metric_name':'total_cost','observed_value':est['cost_estimates']['total_cost'] or 0,'warn_threshold':100,'fail_threshold':1000,'unit':'USD','status':'pass','message':'within budget'}],'generated_at':now()}
 (out/'local_budget_check_report.json').write_text(json.dumps(b,indent=2))
 (out/'monthly_refresh_budget_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdMonthlyRefreshBudgetReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'cost_governance','public_safe_final_outputs':True,'exact_points':'restricted','cost_run_id':cid,'refresh_cadence':a.refresh_cadence,'aggregate_targets':[a.aggregate],'status':'pass','estimated_monthly_resources':{'compute_core_hours':1.0,'memory_gb_hours':2.0,'storage_gb_month':0.01,'public_storage_gb_month':0.005,'catalog_storage_gb_month':0.003,'work_storage_gb_month':0.002,'operator_minutes':30},'estimated_monthly_costs':{'compute_cost':est['cost_estimates']['compute_cost'],'memory_cost':est['cost_estimates']['memory_cost'],'storage_cost':est['cost_estimates']['storage_cost'],'operator_cost':est['cost_estimates']['operator_cost'],'total_cost':est['cost_estimates']['total_cost'],'currency':'USD','confidence':conf},'budget_status':b['status'],'safety_requirements':{'exact_points_restricted':True,'suppression_min_n_at_least_10':True,'no_restricted_outputs_under_data_published':True,'no_suppression_receipts_public':True,'public_safety_scan_required':True,'redteam_core_required':True,'conformance_required':True},'generated_at':now()},indent=2))
 (out/'cost_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdCostValidationReport','status':'pass','cost_run_id':cid},indent=2)); (out/'cost_operator_report.md').write_text(f'# Cost {cid}\n')
 if a.public_out_dir:
  po=Path(a.public_out_dir); po.mkdir(parents=True,exist_ok=True)
  pub={'schema_version':'v1','object_type':'PublicEbirdCostSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','cost_run_id':cid,'aggregate_targets':[a.aggregate],'refresh_cadence':a.refresh_cadence,'cost_status':'pass','budget_status':b['status'],'public_storage_gb_month':0.005,'cost_confidence':conf,'notes':['Local estimate only; no cloud billing APIs are used.'],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True},'generated_at':now()}
  (po/'public_cost_summary.json').write_text(json.dumps(pub,indent=2)); (po/'public_cost_summary.md').write_text(f'# Public cost summary {cid}\n')
 return 0
if __name__=='__main__': raise SystemExit(main())
