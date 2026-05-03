import re
from pathlib import Path
from .checksums import sha256_bytes
from .constants import COORD_RE,FORBIDDEN_TEXT_TERMS,REFS
from .ids import sid
from .layer31_intake import REQUIRED
from .loaders import loadj,wj,wjl
from .manifest import validate_manifest,validate_path_safe

def run_closure_archive_index_preservation_plan(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
 errs=validate_manifest(m)
 li=m.get('layer31_inputs',{}) if isinstance(m.get('layer31_inputs'),dict) else {}
 rows=[]
 for k in REQUIRED:
  v=li.get(k)
  if not v: errs.append(f"MISSING_LAYER31_INPUT:{k}"); continue
  if not validate_path_safe(v): errs.append(f"UNSAFE_PATH:{k}"); continue
  p=Path(v)
  if not p.exists(): errs.append(f"MISSING_INPUT_FILE:{k}"); continue
  b=p.read_bytes(); obj=loadj(p)
  rows.append({'input_id':k,'path':v,'sha256':sha256_bytes(b),'byte_size':len(b),'object_type_detected':obj.get('object_type')})
 rec=next((r for r in rows if r['input_id']=='closure_archive_index_audit_receipt'),None)
 if not rec or rec.get('object_type_detected')!='AirNowClosureArchiveIndexAuditReceipt': errs.append('INVALID_LAYER31_RECEIPT_OBJECT_TYPE')
 if rec:
  ro=loadj(li['closure_archive_index_audit_receipt'])
  for bk in ['publication_allowed','public_release_allowed','index_execution_allowed','database_write_allowed','search_service_creation_allowed','public_catalog_creation_allowed','closure_execution_allowed','task_closure_allowed','audit_closure_allowed','governance_closure_allowed','preservation_action_execution_allowed','preservation_copy_allowed','preservation_transfer_allowed','snapshot_export_allowed','snapshot_copy_allowed','snapshot_transfer_allowed','snapshot_publication_allowed','snapshot_release_allowed','archive_transfer_allowed','file_deletion_allowed','legal_hold_creation_allowed','official_archive_certification_allowed','command_execution_allowed','final_accession_execution_allowed']:
   if ro.get(bk) not in (False,None): errs.append(f"LAYER31_RECEIPT_DENIED_CAPABILITY_REQUIRED:{bk}")
 scope=sorted([{'scope_id':sid('kfm:airnow:scope:v1',[m.get('manifest_id'),r['input_id']]),'input_id':r['input_id']} for r in rows], key=lambda x:x['scope_id'])
 clas=[]
 for r in rows:
  iid=r['input_id']; c='internal_index_planning_record'
  if any(x in iid for x in ['receipt','decision','policy','caveat','hash_chain']): c='internal_audit_core'
  if 'status' in iid or 'report' in iid: c='internal_generated_report'
  if 'non_execution' in iid: c='internal_governance_record'
  clas.append({'classification_id':sid('kfm:airnow:class:v1',[m.get('manifest_id'),iid]),'input_id':iid,'classification':c})
 clas=sorted(clas,key=lambda x:x['classification_id'])
 fix=sorted([{'fixity_id':sid('kfm:airnow:fixity:v1',r['input_id']),'input_id':r['input_id'],'algorithm':'sha256','baseline_sha256':r['sha256']} for r in rows], key=lambda x:x['fixity_id'])
 access=sorted([{'access_id':sid('kfm:airnow:access:v1',r['input_id']),'input_id':r['input_id'],'public_access_allowed':False} for r in rows], key=lambda x:x['access_id'])
 mins=sorted([{'review_id':sid('kfm:airnow:min:v1',r['input_id']),'input_id':r['input_id'],'minimization_execution_performed':False} for r in rows], key=lambda x:x['review_id'])
 holds=sorted([{'candidate_id':sid('kfm:airnow:hold:v1',r['input_id']),'input_id':r['input_id'],'legal_hold_created':False} for r in rows], key=lambda x:x['candidate_id'])
 risks=[{'risk_id':sid('kfm:airnow:risk:v1',x),'risk':x} for x in ['preliminary_airnow_data','non_regulatory_airnow_data','no_live_freshness_assertion','no_public_index_search_catalog_creation']]
 wj(out/'closure_archive_index_preservation_manifest.resolved.json',{'object_type':'AirNowResolvedClosureArchiveIndexPreservationManifest','manifest_id':m.get('manifest_id'),'created_at':created_at,'authoritative_references':REFS})
 def pair(name,obj,rows_out=None):
  wj(out/name,obj)
  if rows_out is not None:
   wjl(out/name.replace('.json','.jsonl'),rows_out)
 pair('closure_archive_index_preservation_input_inventory.json',{'object_type':'AirNowClosureArchiveIndexPreservationInputInventory','records':rows,'created_at':created_at},sorted(rows,key=lambda x:x['input_id']))
 pair('closure_archive_index_preservation_scope_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationScopePlan','records':scope,'created_at':created_at},scope)
 pair('closure_archive_index_preservation_classification_matrix.json',{'object_type':'AirNowClosureArchiveIndexPreservationClassificationMatrix','records':clas,'created_at':created_at},clas)
 pair('closure_archive_index_preservation_fixity_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationFixityPlan','records':fix,'created_at':created_at},fix)
 pair('closure_archive_index_preservation_layout_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationLayoutPlan','layout_status':'PLANNED_ONLY','created_at':created_at},scope)
 pair('closure_archive_index_preservation_access_review_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationAccessReviewPlan','records':access,'created_at':created_at},access)
 pair('closure_archive_index_preservation_minimization_review_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationMinimizationReviewPlan','records':mins,'created_at':created_at},mins)
 pair('closure_archive_index_preservation_hold_candidate_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationHoldCandidatePlan','records':holds,'created_at':created_at},holds)
 pair('closure_archive_index_preservation_risk_register.json',{'object_type':'AirNowClosureArchiveIndexPreservationRiskRegister','records':risks,'created_at':created_at},sorted(risks,key=lambda x:x['risk_id']))
 wjl(out/'closure_archive_index_preservation_blockers.jsonl',[{'blocker_id':sid('kfm:airnow:blocker:v1',e),'message':e} for e in sorted(errs)])
 wj(out/'closure_archive_index_preservation_non_execution_attestation.json',{'object_type':'AirNowClosureArchiveIndexPreservationNonExecutionAttestation','commands_executed':False,'preservation_actions_executed':False,'created_at':created_at})
 pair('closure_archive_index_preservation_policy_continuity_matrix.json',{'object_type':'AirNowClosureArchiveIndexPreservationPolicyContinuityMatrix','policy_status':'CONTINUED','created_at':created_at},scope)
 wj(out/'closure_archive_index_preservation_caveat_register.json',{'object_type':'AirNowClosureArchiveIndexPreservationCaveatRegister','caveats':['planning_only'],'created_at':created_at})
 wj(out/'closure_archive_index_preservation_readiness_summary.json',{'object_type':'AirNowClosureArchiveIndexPreservationReadinessSummary','readiness_status':'READY' if not errs else 'DENIED','created_at':created_at})
 wj(out/'closure_archive_index_preservation_rerun_plan.json',{'object_type':'AirNowClosureArchiveIndexPreservationRerunPlan','rerun_required':bool(errs),'created_at':created_at})
 outcome='CLOSURE_ARCHIVE_INDEX_PRESERVATION_PLAN_COMPLETE_INTERNAL_ONLY' if not errs else 'CLOSURE_ARCHIVE_INDEX_PRESERVATION_PLAN_DENIED'
 wj(out/'closure_archive_index_preservation_status_board.json',{'object_type':'AirNowClosureArchiveIndexPreservationStatusBoard','board_status':outcome,'created_at':created_at})
 (out/'closure_archive_index_preservation_status_board.md').write_text('# AirNow Layer 32 Closure Archive Index Preservation Status Board\n\nInternal planning only.\n')
 (out/'closure_archive_index_preservation_report.md').write_text('# AirNow Layer 32 Closure Archive Index Preservation Report\n\nPlanning-only workflow; no execution.\n')
 text=(out/'closure_archive_index_preservation_status_board.md').read_text()+(out/'closure_archive_index_preservation_report.md').read_text()
 if re.search(COORD_RE,text): errs.append('COORDINATE_LEAK_DETECTED')
 for t in FORBIDDEN_TEXT_TERMS:
  if t in text.lower(): errs.append(f'FORBIDDEN_TEXT_TERM:{t}')
 receipt={'object_type':'AirNowClosureArchiveIndexPreservationReceipt','workflow_runner':'airnow_layer32_closure_archive_index_preservation','workflow_outcome':outcome,'validation_outcome':'PASS' if not errs else 'FAIL','finite_outcome':'ANSWER' if not errs else 'DENY','commands_executed':False,'preservation_actions_executed':False,'preservation_copy_executed':False,'preservation_transfer_executed':False,'index_executed':False,'database_write_executed':False,'public_catalog_created':False,'search_service_created':False,'closure_executed':False,'task_closure_performed':False,'governance_closure_performed':False,'audit_closure_performed':False,'snapshot_export_executed':False,'snapshot_copy_executed':False,'snapshot_transfer_executed':False,'snapshot_published':False,'snapshot_released':False,'public_release_allowed':False,'errors':sorted(set(errs)),'created_at':created_at,'output_hashes':{'closure_archive_index_preservation_packet_hash':None}}
 wj(out/'closure_archive_index_preservation_receipt.json',receipt)
 return receipt
