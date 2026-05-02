import json
from pathlib import Path

from .checksums import sha256_path
from .constants import LAYER25_REQUIRED
from .ids import cjson, sid
from .loaders import loadj, loadjl
from .manifest import validate_manifest, validate_path_safe


def _wj(p, o): Path(p).write_text(json.dumps(o, indent=2, sort_keys=True)+"\n")
def _wjl(p, rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _deny(m, out, created_at, errs):
    r={"object_type":"AirNowPreservationClosureFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer26_preservation_closure_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_FINALIZATION_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"finalization_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(errs),"output_hashes":{"preservation_closure_finalization_packet_hash":None},"created_at":created_at}
    _wj(out/"preservation_closure_finalization_receipt.json",r);return r

def run_preservation_closure_finalization(manifest_path, out_dir, created_at):
    m=loadj(manifest_path);out=Path(out_dir);out.mkdir(parents=True, exist_ok=True)
    errs=validate_manifest(m);l25=m.get("layer25_inputs",{})
    for k in sorted(LAYER25_REQUIRED):
        p=l25.get(k)
        if not p: errs.append(f"MISSING_REQUIRED_INPUT:{k}"); continue
        if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{k}")
        elif not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{k}")
    if errs: return _deny(m,out,created_at,errs)
    rcp=loadj(l25["preservation_closure_review_receipt_json"])
    if rcp.get("object_type")!="AirNowPreservationClosureReviewReceipt": errs.append("INVALID_LAYER25_RECEIPT_OBJECT_TYPE")
    for f in ["publication_allowed","public_release_allowed","closure_executed","task_closure_performed","audit_closure_performed","governance_closure_performed","preservation_actions_executed","preservation_copy_executed","preservation_transfer_executed","snapshot_export_executed","snapshot_copy_executed","snapshot_transfer_executed","snapshot_published","snapshot_released","archive_transfer_executed","file_deleted","legal_hold_created","official_archive_certified","commands_executed","final_accession_executed"]:
        if rcp.get(f) is True: errs.append(f"LAYER25_RECEIPT_FORBIDDEN:{f}")
    if errs: return _deny(m,out,created_at,errs)
    cands=sorted(loadjl(l25["preservation_closure_acceptance_candidates_jsonl"]), key=lambda x:x.get("candidate_id",""))
    blks=sorted(loadjl(l25["residual_preservation_closure_blockers_jsonl"]), key=lambda x:x.get("blocker_id",""))
    assess=loadj(l25["preservation_closure_review_assessment_matrix_json"]); sats=loadj(l25["preservation_closure_item_satisfaction_matrix_json"])
    val=loadj(l25["preservation_closure_review_validation_results_json"]); pol=loadj(l25["preservation_closure_review_policy_attestation_json"])
    cav=loadj(l25["preservation_closure_review_caveat_register_json"]); ready=loadj(l25["preservation_closure_review_readiness_summary_json"])
    _wj(out/"preservation_closure_finalization_manifest.resolved.json", {"object_type":"AirNowResolvedPreservationClosureFinalizationManifest","schema_version":"v1","manifest_id":m.get("manifest_id"),"created_at":created_at})
    inv=[]
    for k,v in sorted(l25.items()):
        p=Path(v);inv.append({"object_type":"AirNowPreservationClosureFinalizationInputInventoryRecord","schema_version":"v1","input_id":k,"path_original":v,"exists":p.exists(),"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at,"preservation_closure_finalization_input_inventory_record_id":sid("kfm:air_quality:airnow:preservation_closure_finalization_input_inventory_record:v1",[m.get("manifest_id"),k])})
    _wj(out/"preservation_closure_finalization_input_inventory.json", {"object_type":"AirNowPreservationClosureFinalizationInputInventory","schema_version":"v1","records":inv,"created_at":created_at});_wjl(out/"preservation_closure_finalization_input_inventory.jsonl",inv)
    _wj(out/"preservation_closure_acceptance_consolidation.json", {"object_type":"AirNowPreservationClosureAcceptanceConsolidation","schema_version":"v1","records":cands,"accepted_count":len(cands),"created_at":created_at});_wjl(out/"preservation_closure_acceptance_consolidation.jsonl",cands)
    _wj(out/"preservation_closure_blocker_consolidation.json", {"object_type":"AirNowPreservationClosureBlockerConsolidation","schema_version":"v1","records":blks,"blocker_count":len(blks),"created_at":created_at});_wjl(out/"preservation_closure_blocker_consolidation.jsonl",blks)
    policy={"object_type":"AirNowPreservationClosurePolicyContinuityMatrix","schema_version":"v1","policy_attestation":pol,"validation_results":val,"continuity_status":"PASS","created_at":created_at}
    _wj(out/"preservation_closure_policy_continuity_matrix.json",policy);_wjl(out/"preservation_closure_policy_continuity_matrix.jsonl",[policy])
    _wj(out/"preservation_closure_caveat_continuity_register.json", {"object_type":"AirNowPreservationClosureCaveatContinuityRegister","schema_version":"v1","caveats":cav.get("caveats",[]),"created_at":created_at})
    outcome="INTERNAL_PRESERVATION_CLOSURE_REVIEW_READY" if (cands and not blks) else ("INTERNAL_PRESERVATION_CLOSURE_REVIEW_NEEDS_MORE_INPUT" if blks else "INTERNAL_PRESERVATION_CLOSURE_REVIEW_PARTIAL")
    _wj(out/"preservation_closure_readiness_final_summary.json", {"object_type":"AirNowPreservationClosureReadinessFinalSummary","schema_version":"v1","layer25_readiness":ready,"readiness_status":outcome,"created_at":created_at})
    rows=[{"record_type":"acceptance_candidate",**x,"execution_enabled":False} for x in cands]+[{"record_type":"residual_blocker",**x,"execution_enabled":False} for x in blks]
    ledger={"object_type":"AirNowPreservationClosureReviewFinalizationLedger","schema_version":"v1","assessment_matrix":assess,"item_satisfaction_matrix":sats,"validation_results":val,"policy_attestation":pol,"caveat_register":cav,"layer25_receipt":rcp,"records":rows,"created_at":created_at}
    _wj(out/"preservation_closure_review_finalization_ledger.json",ledger);_wjl(out/"preservation_closure_review_finalization_ledger.jsonl",rows)
    dec={"object_type":"AirNowPreservationClosureDecisionCandidate","schema_version":"v1","decision_candidate_id":sid("kfm:air_quality:airnow:preservation_closure_decision_candidate:v1",[m.get("manifest_id"),outcome]),"decision_candidate_outcome":outcome,"positive_outcome_ceiling":"PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY","public_release_allowed":False,"created_at":created_at}
    _wj(out/"preservation_closure_decision_candidate.json",dec);_wjl(out/"preservation_closure_decision_candidate_ledger.jsonl",[dec])
    _wj(out/"preservation_closure_non_execution_attestation.json", {"object_type":"AirNowPreservationClosureNonExecutionAttestation","schema_version":"v1","commands_executed":False,"finalization_actions_executed":False,"closure_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"created_at":created_at})
    _wj(out/"preservation_closure_finalization_exception_register.json", {"object_type":"AirNowPreservationClosureFinalizationExceptionRegister","schema_version":"v1","records":[],"created_at":created_at});_wjl(out/"preservation_closure_finalization_exception_register.jsonl",[])
    _wj(out/"preservation_closure_finalization_rerun_plan.json", {"object_type":"AirNowPreservationClosureFinalizationRerunPlan","schema_version":"v1","steps":[],"created_at":created_at})
    _wj(out/"preservation_closure_finalization_status_board.json", {"object_type":"AirNowPreservationClosureFinalizationStatusBoard","schema_version":"v1","board_status":"PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY","created_at":created_at})
    (out/"preservation_closure_finalization_status_board.md").write_text("# AirNow Layer 26 Preservation Closure Finalization Status Board\n\nInternal finalization planning only. No closure execution, no publication, no preservation transfer.\n")
    (out/"preservation_closure_finalization_report.md").write_text("# AirNow Layer 26 Preservation Closure Finalization Report\n\nReferences: docs.airnowapi.org, airnow.gov/about-the-data, epa.gov/outdoor-air-quality-data/download-daily-data.\n")
    receipt={"object_type":"AirNowPreservationClosureFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer26_preservation_closure_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_FINALIZATION_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"finalization_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"preservation_closure_finalization_packet_hash":None},"created_at":created_at}
    _wj(out/"preservation_closure_finalization_receipt.json",receipt)
    return receipt
