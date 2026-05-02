import json
from pathlib import Path
from .checksums import sha256_path
from .constants import L29_REQUIRED
from .ids import cjson, sid
from .loaders import loadj, loadjl, wj, wjl
from .manifest import validate_manifest, validate_path_safe

REFS=["https://docs.airnowapi.org/","https://docs.airnowapi.org/webservices","https://docs.airnowapi.org/faq","https://docs.airnowapi.org/docs/AirNowAPIFactSheet.pdf","https://docs.airnowapi.org/docs/HourlyAQObsFactSheet.pdf","https://docs.airnowapi.org/docs/HourlyDataFactSheet.pdf","https://docs.airnowapi.org/docs/DailyDataFactSheet.pdf","https://www.airnowapi.org/docs/MonitoringSiteFactSheet.pdf","https://www.airnow.gov/about-the-data","https://docs.airnowapi.org/docs/DataUseGuidelines.pdf","https://www.epa.gov/outdoor-air-quality-data/download-daily-data"]

FORBIDDEN_RCP_TRUE=["publication_allowed","public_release_allowed","index_executed","database_write_executed","search_service_created","public_catalog_created","closure_executed","task_closure_performed","audit_closure_performed","governance_closure_performed","preservation_actions_executed","preservation_copy_executed","preservation_transfer_executed","snapshot_export_executed","snapshot_copy_executed","snapshot_transfer_executed","snapshot_published","snapshot_released","archive_transfer_executed","file_deleted","legal_hold_created","official_archive_certified","commands_executed","final_accession_executed"]

def _deny(m,out,created_at,errs):
    r={"object_type":"AirNowClosureArchiveIndexFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer30_closure_archive_index_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"CLOSURE_ARCHIVE_INDEX_FINALIZATION_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"finalization_actions_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"closure_archive_index_finalization_packet_hash":None},"created_at":created_at}
    wj(out/"closure_archive_index_finalization_receipt.json",r);return r

def run_closure_archive_index_finalization(manifest_path,out_dir,created_at):
    m=loadj(manifest_path);out=Path(out_dir);out.mkdir(parents=True, exist_ok=True)
    errs=validate_manifest(m);l29=m.get("layer29_inputs",{})
    for k in sorted(L29_REQUIRED):
        p=l29.get(k)
        if not p: errs.append(f"MISSING_REQUIRED_INPUT:{k}"); continue
        if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{k}")
        elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{k}")
    if errs: return _deny(m,out,created_at,errs)
    rcp=loadj(l29["closure_archive_index_review_receipt_json"])
    if rcp.get("object_type")!="AirNowClosureArchiveIndexReviewReceipt": errs.append("INVALID_LAYER29_RECEIPT_OBJECT_TYPE")
    for f in FORBIDDEN_RCP_TRUE:
        if rcp.get(f) is True: errs.append(f"LAYER29_RECEIPT_FORBIDDEN:{f}")
    if errs: return _deny(m,out,created_at,errs)
    cands=sorted(loadjl(l29["closure_archive_index_acceptance_candidates_jsonl"]), key=lambda x:x.get("candidate_id",""))
    blks=sorted(loadjl(l29["residual_closure_archive_index_blockers_jsonl"]), key=lambda x:x.get("blocker_id",""))
    assess=loadj(l29["closure_archive_index_review_assessment_matrix_json"]); sats=loadj(l29["closure_archive_index_item_satisfaction_matrix_json"])
    val=loadj(l29["closure_archive_index_review_validation_results_json"]); pol=loadj(l29["closure_archive_index_review_policy_attestation_json"])
    cav=loadj(l29["closure_archive_index_review_caveat_register_json"]); ready=loadj(l29["closure_archive_index_review_readiness_summary_json"])
    wj(out/"closure_archive_index_finalization_manifest.resolved.json",{"object_type":"AirNowResolvedClosureArchiveIndexFinalizationManifest","schema_version":"v1","manifest_id":m.get("manifest_id"),"created_at":created_at})
    inv=[]
    for k,v in sorted(l29.items()):
        p=Path(v);inv.append({"object_type":"AirNowClosureArchiveIndexFinalizationInputInventoryRecord","schema_version":"v1","input_id":k,"path_original":v,"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at,"closure_archive_index_finalization_input_inventory_record_id":sid("kfm:air_quality:airnow:closure_archive_index_finalization_input_inventory_record:v1",[m.get("manifest_id"),k])})
    wj(out/"closure_archive_index_finalization_input_inventory.json",{"object_type":"AirNowClosureArchiveIndexFinalizationInputInventory","schema_version":"v1","records":inv,"created_at":created_at}); wjl(out/"closure_archive_index_finalization_input_inventory.jsonl",inv,cjson)
    rows=[{"record_type":"acceptance_candidate",**x,"execution_enabled":False} for x in cands]+[{"record_type":"residual_blocker",**x,"execution_enabled":False} for x in blks]
    ledger={"object_type":"AirNowClosureArchiveIndexReviewFinalizationLedger","schema_version":"v1","assessment_matrix":assess,"item_satisfaction_matrix":sats,"validation_results":val,"policy_attestation":pol,"caveat_register":cav,"layer29_receipt":rcp,"records":rows,"created_at":created_at}
    wj(out/"closure_archive_index_review_finalization_ledger.json",ledger); wjl(out/"closure_archive_index_review_finalization_ledger.jsonl",rows,cjson)
    outcome="INTERNAL_CLOSURE_ARCHIVE_INDEX_REVIEW_READY" if (cands and not blks) else ("INTERNAL_CLOSURE_ARCHIVE_INDEX_REVIEW_NEEDS_MORE_INPUT" if blks else "INTERNAL_CLOSURE_ARCHIVE_INDEX_REVIEW_PARTIAL")
    dec={"object_type":"AirNowClosureArchiveIndexDecisionCandidate","schema_version":"v1","decision_candidate_id":sid("kfm:air_quality:airnow:closure_archive_index_decision_candidate:v1",[m.get("manifest_id"),outcome]),"decision_candidate_outcome":outcome,"positive_outcome_ceiling":"CLOSURE_ARCHIVE_INDEX_FINALIZATION_COMPLETE_INTERNAL_ONLY","public_release_allowed":False,"created_at":created_at}
    wj(out/"closure_archive_index_decision_candidate.json",dec); wjl(out/"closure_archive_index_decision_candidate_ledger.jsonl",[dec],cjson)
    wj(out/"closure_archive_index_acceptance_consolidation.json",{"object_type":"AirNowClosureArchiveIndexAcceptanceConsolidation","schema_version":"v1","records":cands,"accepted_count":len(cands),"created_at":created_at}); wjl(out/"closure_archive_index_acceptance_consolidation.jsonl",cands,cjson)
    wj(out/"closure_archive_index_blocker_consolidation.json",{"object_type":"AirNowClosureArchiveIndexBlockerConsolidation","schema_version":"v1","records":blks,"blocker_count":len(blks),"created_at":created_at}); wjl(out/"closure_archive_index_blocker_consolidation.jsonl",blks,cjson)
    wj(out/"closure_archive_index_non_execution_attestation.json",{"object_type":"AirNowClosureArchiveIndexNonExecutionAttestation","schema_version":"v1","commands_executed":False,"finalization_actions_executed":False,"closure_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"created_at":created_at})
    pcm={"object_type":"AirNowClosureArchiveIndexPolicyContinuityMatrix","schema_version":"v1","policy_attestation":pol,"validation_results":val,"continuity_status":"PASS","references":REFS,"created_at":created_at}
    wj(out/"closure_archive_index_policy_continuity_matrix.json",pcm); wjl(out/"closure_archive_index_policy_continuity_matrix.jsonl",[{"reference":r,"continuity_status":"PASS"} for r in REFS],cjson)
    wj(out/"closure_archive_index_caveat_continuity_register.json",{"object_type":"AirNowClosureArchiveIndexCaveatContinuityRegister","schema_version":"v1","caveats":cav.get("caveats",[]),"created_at":created_at})
    wj(out/"closure_archive_index_readiness_final_summary.json",{"object_type":"AirNowClosureArchiveIndexReadinessFinalSummary","schema_version":"v1","layer29_readiness":ready,"readiness_status":outcome,"created_at":created_at})
    wj(out/"closure_archive_index_finalization_exception_register.json",{"object_type":"AirNowClosureArchiveIndexFinalizationExceptionRegister","schema_version":"v1","records":[],"created_at":created_at}); wjl(out/"closure_archive_index_finalization_exception_register.jsonl",[],cjson)
    wj(out/"closure_archive_index_finalization_rerun_plan.json",{"object_type":"AirNowClosureArchiveIndexFinalizationRerunPlan","schema_version":"v1","steps":[],"created_at":created_at})
    wj(out/"closure_archive_index_finalization_status_board.json",{"object_type":"AirNowClosureArchiveIndexFinalizationStatusBoard","schema_version":"v1","board_status":"CLOSURE_ARCHIVE_INDEX_FINALIZATION_COMPLETE_INTERNAL_ONLY","created_at":created_at})
    (out/"closure_archive_index_finalization_status_board.md").write_text("# AirNow Layer 30 Closure Archive Index Finalization Status Board\n\nInternal finalization planning only. No index/database/search/catalog/closure execution; no public release.\n")
    (out/"closure_archive_index_finalization_report.md").write_text("# AirNow Layer 30 Closure Archive Index Finalization Report\n\nCompiled internal finalization ledger from Layer 29 review artifacts. References retained for provenance; no execution actions.\n")
    rec={"object_type":"AirNowClosureArchiveIndexFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer30_closure_archive_index_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"CLOSURE_ARCHIVE_INDEX_FINALIZATION_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"finalization_actions_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"closure_archive_index_finalization_packet_hash":None},"created_at":created_at}
    wj(out/"closure_archive_index_finalization_receipt.json",rec); return rec
