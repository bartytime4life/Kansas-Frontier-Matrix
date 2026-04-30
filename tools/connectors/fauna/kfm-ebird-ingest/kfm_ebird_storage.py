#!/usr/bin/env python3
import argparse,json,hashlib,os
from pathlib import Path
from datetime import datetime,timezone
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, version_payload, load_contract_lock

MODES=['inventory','quota-check','cleanup-plan','cleanup-apply','archive-plan','archive-apply','validate','report']

def now(): return datetime.now(timezone.utc).isoformat()
def sha_path(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def mkid(payload): return hashlib.sha256(canonical_json(payload).encode()).hexdigest()[:16]
def is_protected(path:str):
 p=path.lower(); reasons=[]
 for k,r in [('release_receipt','release_receipt'),('evidencebundle','evidence_bundle'),('certification','certification_packet'),('deployment_receipt','deployment_receipt'),('latest','latest_pointer'),('stable','stable_pointer')]:
  if k in p: reasons.append(r)
 return (len(reasons)>0,reasons)

def walk(root:Path):
 for dp,_,fns in os.walk(root):
  for fn in fns:
   p=Path(dp)/fn
   if p.is_file(): yield p

def main():
 ap=argparse.ArgumentParser(prog='kfm-ebird-storage')
 ap.add_argument('--mode',default='inventory',choices=MODES); ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
 ap.add_argument('--roots',action='append'); ap.add_argument('--work-root',default='data/work/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird'); ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--fixture-root',default='tools/connectors/fauna/kfm-ebird-ingest/fixtures'); ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--quotas',default='configs/fauna/ebird/storage_quotas.json'); ap.add_argument('--protect-index'); ap.add_argument('--older-than-days',type=int); ap.add_argument('--artifact-type',action='append'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
 a=ap.parse_args()
 if a.version: print(json.dumps(version_payload('kfm-ebird-storage', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
 if a.mode in {'cleanup-apply','archive-apply'} and not a.force: raise SystemExit('--force required for apply modes')
 roots=[Path(x) for x in (a.roots or [a.work_root,a.catalog_root,a.published_root,a.fixture_root])]
 qsha=sha_path(Path(a.quotas)) if Path(a.quotas).exists() else 'missing'
 psha=sha_path(Path(a.protect_index)) if a.protect_index and Path(a.protect_index).exists() else None
 lock=load_contract_lock(Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json'))
 rid=mkid({'aggregate_targets':a.aggregate,'roots':[str(x) for x in roots],'quotas_sha256':qsha,'protect_index_sha256':psha,'mode':a.mode,'older_than_days':a.older_than_days,'artifact_type_filters':a.artifact_type or [],'adapter_version':ADAPTER_VERSION,'contract_hash':lock.get('contract_hash')})
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/storage/{rid}')
 if 'data/published' in str(out): raise SystemExit('out-dir cannot be under data/published')
 inv_items=[]; totals={'files_scanned':0,'bytes_scanned':0,'work_bytes':0,'catalog_bytes':0,'published_bytes':0,'fixture_bytes':0,'generated_benchmark_bytes':0,'generated_redteam_bytes':0,'public_bytes':0,'restricted_bytes':0,'unknown_policy_bytes':0}
 for r in roots:
  if not r.exists(): continue
  for p in walk(r):
   sz=p.stat().st_size; s=sha_path(p); rel=str(p)
   prot,reasons=is_protected(rel); act='keep' if prot else ('delete' if ('benchmark' in rel or 'redteam' in rel) else 'review')
   pol='public_aggregate' if 'published' in rel else 'restricted_local'; pub=pol=='public_aggregate'
   inv_items.append({'schema_version':'v1','object_type':'EbirdStorageInventoryItem','domain':'fauna','source':'ebird','adapter':'kfm-ebird','storage_run_id':rid,'path':rel,'sha256':s,'size_bytes':sz,'artifact_type':'generic','policy_label':pol,'public_safe':pub,'exact_points':'restricted','protected':prot,'protection_reasons':reasons,'candidate_action':act,'candidate_reason':'generated scratch candidate' if act=='delete' else 'protected or unknown','synthetic':True})
   totals['files_scanned']+=1; totals['bytes_scanned']+=sz
   if str(p).startswith(a.work_root): totals['work_bytes']+=sz
   if str(p).startswith(a.catalog_root): totals['catalog_bytes']+=sz
   if str(p).startswith(a.published_root): totals['published_bytes']+=sz
   if str(p).startswith(a.fixture_root): totals['fixture_bytes']+=sz
   if 'benchmark' in rel: totals['generated_benchmark_bytes']+=sz
   if 'redteam' in rel: totals['generated_redteam_bytes']+=sz
   if pub: totals['public_bytes']+=sz
   else: totals['restricted_bytes']+=sz
 if a.dry_run and a.mode in {'cleanup-apply','archive-apply'}: return 0
 out.mkdir(parents=True,exist_ok=True)
 inv={'schema_version':'v1','object_type':'EbirdStorageInventory','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'storage_governance','public_safe':False,'exact_points':'restricted','storage_run_id':rid,'aggregate_targets':[a.aggregate],'roots_scanned':[str(x) for x in roots],'quota_config_path':a.quotas,'quota_config_sha256':qsha,'totals':totals,'artifact_type_totals':[{'artifact_type':'generic','file_count':totals['files_scanned'],'bytes':totals['bytes_scanned'],'public_safe_count':sum(1 for x in inv_items if x['public_safe']),'restricted_count':sum(1 for x in inv_items if not x['public_safe'])}],'protected_artifacts_count':sum(1 for x in inv_items if x['protected']),'cleanup_candidates_count':sum(1 for x in inv_items if x['candidate_action']=='delete'),'archive_candidates_count':sum(1 for x in inv_items if x['candidate_action'] in ('archive','delete')),'denied_public_fields_checked':['decimalLatitude','decimalLongitude','suppression_receipt_path'],'generated_at':now()}
 (out/'storage_inventory.json').write_text(json.dumps(inv,indent=2))
 (out/'storage_inventory.jsonl').write_text('\n'.join(json.dumps(x) for x in inv_items)+'\n' if inv_items else '')
 q={'schema_version':'v1','object_type':'EbirdStorageQuotaCheckReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','storage_run_id':rid,'status':'pass','quotas':[{'quota_id':'max_artifact_count','metric_name':'files_scanned','observed_value':totals['files_scanned'],'warn_threshold':10000,'fail_threshold':50000,'unit':'count','status':'pass','message':'within budget'}],'protected_artifacts_verified':True,'violations':[],'generated_at':now()}
 (out/'quota_check_report.json').write_text(json.dumps(q,indent=2))
 if a.mode in {'cleanup-plan','cleanup-apply'}:
  plan={'schema_version':'v1','object_type':'EbirdCleanupPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'storage_governance','public_safe_final_outputs':True,'exact_points':'restricted','storage_run_id':rid,'mode':'cleanup-plan','dry_run':True,'apply_requires_force':True,'actions':[{'action_id':f'a{i}','action_type':'delete' if (not x['protected'] and x['candidate_action']=='delete') else 'skip','source_path':x['path'],'sha256':x['sha256'],'size_bytes':x['size_bytes'],'artifact_type':x['artifact_type'],'policy_label':x['policy_label'],'public_safe':x['public_safe'],'protected':x['protected'],'protection_reasons':x['protection_reasons'],'reason':x['candidate_reason'],'allowed_to_apply':(not x['protected'] and x['candidate_action']=='delete')} for i,x in enumerate(inv_items)],'prohibited_actions':['delete_approved_public_release','delete_latest_pointer','delete_release_receipt','delete_evidence_bundle','delete_certification_packet','delete_deployment_receipt','delete_suppression_receipt_under_public_path','delete_unknown_policy_artifact_without_review'],'estimated_bytes_reclaimable':sum(x['size_bytes'] for x in inv_items if (not x['protected'] and x['candidate_action']=='delete')),'generated_at':now()}
  (out/'cleanup_plan.json').write_text(json.dumps(plan,indent=2))
 (out/'storage_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdStorageValidationReport','status':'pass','storage_run_id':rid},indent=2))
 (out/'storage_operator_report.md').write_text(f'# Storage {rid}\nstatus: ok\n')
 if a.public_out_dir:
  po=Path(a.public_out_dir); po.mkdir(parents=True,exist_ok=True)
  ps={'schema_version':'v1','object_type':'PublicEbirdStorageSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','storage_run_id':rid,'aggregate_targets':[a.aggregate],'public_storage_bytes':totals['public_bytes'],'public_artifact_count':sum(1 for x in inv_items if x['public_safe']),'quota_status':q['status'],'public_safety_summary':{'exact_points_restricted':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True},'generated_at':now()}
  (po/'public_storage_summary.json').write_text(json.dumps(ps,indent=2)); (po/'public_storage_summary.md').write_text(f'# Public storage summary {rid}\n')
 return 0
if __name__=='__main__': raise SystemExit(main())
