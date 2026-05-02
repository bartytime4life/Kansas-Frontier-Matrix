import json
from pathlib import Path
from .checksums import sha256_path
from .ids import sid,cjson
from .loaders import loadj,loadjl
from .manifest import validate_manifest, validate_path_safe

REFS=["https://docs.airnowapi.org/","https://docs.airnowapi.org/webservices","https://docs.airnowapi.org/faq","https://docs.airnowapi.org/docs/AirNowAPIFactSheet.pdf","https://docs.airnowapi.org/docs/HourlyAQObsFactSheet.pdf","https://docs.airnowapi.org/docs/HourlyDataFactSheet.pdf","https://docs.airnowapi.org/docs/DailyDataFactSheet.pdf","https://www.airnowapi.org/docs/MonitoringSiteFactSheet.pdf","https://www.airnow.gov/about-the-data","https://docs.airnowapi.org/docs/DataUseGuidelines.pdf","https://www.epa.gov/outdoor-air-quality-data/download-daily-data"]

def _wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def _wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowSnapshotAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer19_snapshot_audit","manifest_id":m.get("manifest_id"),"workflow_outcome":"SNAPSHOT_AUDIT_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"audit_actions_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"snapshot_audit_packet_hash":None},"created_at":created_at}
 _wj(out/"snapshot_audit_receipt.json",r); return r

def _chk_receipt(rcp,pfx,errs):
 for f in ["publication_allowed","public_release_allowed","snapshot_export_executed","snapshot_copy_executed","snapshot_transfer_executed","snapshot_published","snapshot_released","archive_transfer_allowed","file_deletion_allowed","legal_hold_creation_allowed","official_archive_certification_allowed","command_execution_allowed","final_accession_execution_allowed","task_closure_allowed"]:
  if rcp.get(f) is True: errs.append(f"{pfx}_FORBIDDEN:{f}")

def run_snapshot_audit(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=validate_manifest(m)
 l16=m.get("layer16_inputs",{}); l17=m.get("layer17_inputs",{}); l18=m.get("layer18_inputs",{})
 req={"layer16_inputs":["snapshot_export_receipt_json","snapshot_manifest_preview_json","snapshot_non_execution_attestation_json","snapshot_policy_continuity_matrix_json","snapshot_caveat_continuity_register_json"],"layer17_inputs":["snapshot_review_receipt_json","snapshot_acceptance_candidates_jsonl","residual_snapshot_blockers_jsonl","snapshot_review_policy_attestation_json","snapshot_review_caveat_register_json"],"layer18_inputs":["snapshot_finalization_receipt_json","snapshot_decision_candidate_json","snapshot_acceptance_consolidation_json","snapshot_blocker_consolidation_json","snapshot_non_execution_attestation_json","snapshot_policy_continuity_matrix_json","snapshot_caveat_continuity_register_json"]}
 for sect,keys in req.items():
  src=m.get(sect,{})
  for k in keys:
   p=src.get(k)
   if not p: errs.append(f"MISSING_REQUIRED_INPUT:{sect}.{k}"); continue
   if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{sect}.{k}")
   elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{sect}.{k}")
 if errs: return _deny(m,out,created_at,errs)
 r16=loadj(l16['snapshot_export_receipt_json']); r17=loadj(l17['snapshot_review_receipt_json']); r18=loadj(l18['snapshot_finalization_receipt_json'])
 if r16.get('object_type')!='AirNowSnapshotExportReceipt': errs.append('INVALID_LAYER16_RECEIPT_OBJECT_TYPE')
 if r17.get('object_type')!='AirNowSnapshotReviewReceipt': errs.append('INVALID_LAYER17_RECEIPT_OBJECT_TYPE')
 if r18.get('object_type')!='AirNowSnapshotFinalizationReceipt': errs.append('INVALID_LAYER18_RECEIPT_OBJECT_TYPE')
 _chk_receipt(r16,'LAYER16_RECEIPT',errs); _chk_receipt(r17,'LAYER17_RECEIPT',errs); _chk_receipt(r18,'LAYER18_RECEIPT',errs)
 if errs: return _deny(m,out,created_at,errs)
 ac=sorted(loadjl(l17['snapshot_acceptance_candidates_jsonl']), key=lambda x:x.get('candidate_id',''))
 bl=sorted(loadjl(l17['residual_snapshot_blockers_jsonl']), key=lambda x:x.get('blocker_id',''))
 l18_dec=loadj(l18['snapshot_decision_candidate_json']); l18_non=loadj(l18['snapshot_non_execution_attestation_json']); l18_pol=loadj(l18['snapshot_policy_continuity_matrix_json']); l18_cav=loadj(l18['snapshot_caveat_continuity_register_json'])
 _wj(out/'snapshot_audit_manifest.resolved.json',{"object_type":"AirNowResolvedSnapshotAuditManifest","schema_version":"v1","manifest_id":m.get('manifest_id'),"created_at":created_at})
 inv=[]
 for sect in ['layer16_inputs','layer17_inputs','layer18_inputs']:
  for k,v in sorted(m.get(sect,{}).items()):
   p=Path(v); inv.append({"input_record_id":sid('kfm:air_quality:airnow:snapshot_audit_input_record:v1',[m.get('manifest_id'),sect,k]),"layer":sect,"input_id":k,"path_original":v,"exists":p.exists(),"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
 _wj(out/'snapshot_audit_input_inventory.json',{"object_type":"AirNowSnapshotAuditInputInventory","schema_version":"v1","records":inv,"created_at":created_at}); _wjl(out/'snapshot_audit_input_inventory.jsonl',sorted(inv,key=lambda x:x['input_record_id']))
 receipts=[r16,r17,r18]; _wj(out/'snapshot_receipt_ledger.json',{"object_type":"AirNowSnapshotReceiptLedger","schema_version":"v1","records":receipts,"created_at":created_at}); _wjl(out/'snapshot_receipt_ledger.jsonl',sorted(receipts,key=lambda x:x.get('object_type','')))
 dec=[l18_dec]; _wj(out/'snapshot_decision_ledger.json',{"object_type":"AirNowSnapshotDecisionLedger","schema_version":"v1","records":dec,"created_at":created_at}); _wjl(out/'snapshot_decision_ledger.jsonl',dec)
 ev=ac+bl; _wj(out/'snapshot_evidence_ledger.json',{"object_type":"AirNowSnapshotEvidenceLedger","schema_version":"v1","records":ev,"created_at":created_at}); _wjl(out/'snapshot_evidence_ledger.jsonl',ev)
 lin=[{"from":"layer16","to":"layer17"},{"from":"layer17","to":"layer18"},{"from":"layer18","to":"layer19"}]; _wj(out/'snapshot_lineage_graph.json',{"object_type":"AirNowSnapshotLineageGraph","schema_version":"v1","edges":lin,"created_at":created_at}); _wjl(out/'snapshot_lineage_graph.jsonl',lin)
 hashes=[{"name":p.name,"sha256":sha256_path(p)} for p in sorted(out.glob('*.json')) if p.name!='snapshot_hash_chain.json']
 _wj(out/'snapshot_hash_chain.json',{"object_type":"AirNowSnapshotHashChain","schema_version":"v1","records":hashes,"created_at":created_at})
 pol={"object_type":"AirNowSnapshotPolicyLedger","schema_version":"v1","layer16":loadj(l16['snapshot_policy_continuity_matrix_json']),"layer17":loadj(l17['snapshot_review_policy_attestation_json']),"layer18":l18_pol,"created_at":created_at}; _wj(out/'snapshot_policy_ledger.json',pol); _wjl(out/'snapshot_policy_ledger.jsonl',[pol])
 cav={"object_type":"AirNowSnapshotCaveatRegistry","schema_version":"v1","layer16":loadj(l16['snapshot_caveat_continuity_register_json']),"layer17":loadj(l17['snapshot_review_caveat_register_json']),"layer18":l18_cav,"created_at":created_at}; _wj(out/'snapshot_caveat_registry.json',cav)
 non=[loadj(l16['snapshot_non_execution_attestation_json']),l18_non]; _wj(out/'snapshot_non_execution_ledger.json',{"object_type":"AirNowSnapshotNonExecutionLedger","schema_version":"v1","records":non,"created_at":created_at}); _wjl(out/'snapshot_non_execution_ledger.jsonl',non)
 comp=[{"check":"required_inputs_present","pass":True},{"check":"required_receipts_present","pass":True}]; cons=[{"check":"no_public_release","pass":True},{"check":"no_execution","pass":True}]
 _wj(out/'snapshot_completeness_matrix.json',{"object_type":"AirNowSnapshotCompletenessMatrix","schema_version":"v1","records":comp,"created_at":created_at}); _wjl(out/'snapshot_completeness_matrix.jsonl',comp)
 _wj(out/'snapshot_consistency_matrix.json',{"object_type":"AirNowSnapshotConsistencyMatrix","schema_version":"v1","records":cons,"created_at":created_at}); _wjl(out/'snapshot_consistency_matrix.jsonl',cons)
 _wj(out/'snapshot_audit_exception_register.json',{"object_type":"AirNowSnapshotAuditExceptionRegister","schema_version":"v1","records":[],"created_at":created_at}); _wjl(out/'snapshot_audit_exception_register.jsonl',[])
 outcome='SNAPSHOT_INTERNAL_AUDIT_COMPLETE' if not bl else 'SNAPSHOT_INTERNAL_AUDIT_NEEDS_MORE_INPUT'
 _wj(out/'snapshot_final_internal_summary.json',{"object_type":"AirNowSnapshotFinalInternalSummary","schema_version":"v1","summary_outcome":outcome,"positive_outcome_ceiling":"SNAPSHOT_AUDIT_COMPLETE_INTERNAL_ONLY","references":REFS,"created_at":created_at})
 _wj(out/'snapshot_audit_rerun_plan.json',{"object_type":"AirNowSnapshotAuditRerunPlan","schema_version":"v1","steps":[],"created_at":created_at})
 _wj(out/'snapshot_audit_status_board.json',{"object_type":"AirNowSnapshotAuditStatusBoard","schema_version":"v1","board_status":"SNAPSHOT_AUDIT_COMPLETE_INTERNAL_ONLY","created_at":created_at})
 (out/'snapshot_audit_status_board.md').write_text('# AirNow Layer 19 Snapshot Audit Status Board\n\nInternal-only snapshot-retention audit. No export, publication, release, or transfer.\n')
 (out/'snapshot_audit_report.md').write_text('# AirNow Layer 19 Snapshot Audit Report\n\nInternal-only retention audit ledger compilation; no command execution and no public release.\n')
 r={"object_type":"AirNowSnapshotAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer19_snapshot_audit","manifest_id":m.get('manifest_id'),"workflow_outcome":"SNAPSHOT_AUDIT_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"audit_actions_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"snapshot_audit_packet_hash":None},"created_at":created_at}
 _wj(out/'snapshot_audit_receipt.json',r); return r
