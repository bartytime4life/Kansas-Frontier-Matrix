from pathlib import Path
import tarfile,hashlib
from .constants import L33_REQUIRED,FORBIDDEN_RCP_TRUE,SOURCES
from .ids import sid
from .loaders import loadj,loadjl,wj,wjl
from .manifest import validate_manifest,validate_path_safe
from .checksums import sha256_path

def _deny(m,out,created_at,errs):
 r={"object_type":"AirNowClosureArchiveIndexPreservationFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer34_closure_archive_index_preservation_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"CLOSURE_ARCHIVE_INDEX_PRESERVATION_FINALIZATION_DENIED","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"finalization_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(set(errs)),"output_hashes":{"closure_archive_index_preservation_finalization_packet_hash":None},"created_at":created_at}
 wj(out/"closure_archive_index_preservation_finalization_receipt.json",r);return r



def _packet(out,created_at):
 pkt=out/"closure_archive_index_preservation_finalization_packet.tar.gz"
 files=sorted([x for x in out.iterdir() if x.is_file() and x.name!=pkt.name])
 with tarfile.open(pkt,"w:gz",format=tarfile.PAX_FORMAT) as tf:
  for f in files:
   rel=f.relative_to(out)
   if any(part==".." for part in rel.parts):
    raise ValueError("PACKET_PATH_TRAVERSAL")
   ti=tf.gettarinfo(str(f),arcname=str(rel).replace('\\','/'))
   ti.mtime=0; ti.uid=0; ti.gid=0; ti.uname=""; ti.gname=""
   with open(f,'rb') as fh: tf.addfile(ti,fh)
 h=hashlib.sha256(pkt.read_bytes()).hexdigest()
 return pkt.name,h

def run_closure_archive_index_preservation_finalization(manifest_path,out_dir,created_at):
 m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=validate_manifest(m); l33=m.get("layer33_inputs",{})
 for k in sorted(L33_REQUIRED):
  p=l33.get(k)
  if not p: errs.append(f"MISSING_REQUIRED_INPUT:{k}"); continue
  if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{k}"); continue
  if not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{k}")
 if errs: return _deny(m,out,created_at,errs)
 rcp=loadj(l33["closure_archive_index_preservation_review_receipt_json"])
 if rcp.get("object_type")!="AirNowClosureArchiveIndexPreservationReviewReceipt": errs.append("INVALID_LAYER33_RECEIPT_OBJECT_TYPE")
 for f in FORBIDDEN_RCP_TRUE:
  if rcp.get(f) is True: errs.append(f"LAYER33_RECEIPT_FORBIDDEN:{f}")
 if errs: return _deny(m,out,created_at,errs)
 cands=sorted(loadjl(l33["closure_archive_index_preservation_acceptance_candidates_jsonl"]),key=lambda x:x.get("candidate_id",""))
 blks=sorted(loadjl(l33["residual_closure_archive_index_preservation_blockers_jsonl"]),key=lambda x:x.get("blocker_id",""))
 assess=loadj(l33["closure_archive_index_preservation_review_assessment_matrix_json"]); sats=loadj(l33["closure_archive_index_preservation_item_satisfaction_matrix_json"])
 val=loadj(l33["closure_archive_index_preservation_review_validation_results_json"]); pol=loadj(l33["closure_archive_index_preservation_review_policy_attestation_json"])
 cav=loadj(l33["closure_archive_index_preservation_review_caveat_register_json"]); ready=loadj(l33["closure_archive_index_preservation_review_readiness_summary_json"])
 wj(out/"closure_archive_index_preservation_finalization_manifest.resolved.json",{"object_type":"AirNowResolvedClosureArchiveIndexPreservationFinalizationManifest","schema_version":"v1","manifest_id":m.get("manifest_id"),"created_at":created_at,"authoritative_references":SOURCES})
 inv=[]
 for k,v in sorted(l33.items()):
  p=Path(v);inv.append({"input_id":k,"path_original":v,"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at,"input_inventory_record_id":sid("kfm:air_quality:airnow:layer34_input",[m.get("manifest_id"),k])})
 wj(out/"closure_archive_index_preservation_finalization_input_inventory.json",{"object_type":"AirNowClosureArchiveIndexPreservationFinalizationInputInventory","records":inv,"created_at":created_at}); wjl(out/"closure_archive_index_preservation_finalization_input_inventory.jsonl",inv)
 rows=[{"record_type":"acceptance_candidate",**x,"execution_enabled":False} for x in cands]+[{"record_type":"residual_blocker",**x,"execution_enabled":False} for x in blks]
 wj(out/"closure_archive_index_preservation_review_finalization_ledger.json",{"object_type":"AirNowClosureArchiveIndexPreservationReviewFinalizationLedger","assessment_matrix":assess,"item_satisfaction_matrix":sats,"validation_results":val,"policy_attestation":pol,"caveat_register":cav,"readiness_summary":ready,"layer33_receipt":rcp,"records":rows,"created_at":created_at}); wjl(out/"closure_archive_index_preservation_review_finalization_ledger.jsonl",rows)
 outcome="INTERNAL_CLOSURE_ARCHIVE_INDEX_PRESERVATION_REVIEW_READY" if (cands and not blks) else ("INTERNAL_CLOSURE_ARCHIVE_INDEX_PRESERVATION_REVIEW_NEEDS_MORE_INPUT" if blks else "INTERNAL_CLOSURE_ARCHIVE_INDEX_PRESERVATION_REVIEW_PARTIAL")
 dec={"object_type":"AirNowClosureArchiveIndexPreservationDecisionCandidate","decision_candidate_id":sid("kfm:air_quality:airnow:closure_archive_index_preservation_decision_candidate:v1",[m.get("manifest_id"),outcome]),"decision_candidate_outcome":outcome,"positive_outcome_ceiling":"CLOSURE_ARCHIVE_INDEX_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY","public_release_allowed":False,"created_at":created_at}
 wj(out/"closure_archive_index_preservation_decision_candidate.json",dec); wjl(out/"closure_archive_index_preservation_decision_candidate_ledger.jsonl",[dec])
 wj(out/"closure_archive_index_preservation_acceptance_consolidation.json",{"object_type":"AirNowClosureArchiveIndexPreservationAcceptanceConsolidation","records":cands,"accepted_count":len(cands),"created_at":created_at}); wjl(out/"closure_archive_index_preservation_acceptance_consolidation.jsonl",cands)
 wj(out/"closure_archive_index_preservation_blocker_consolidation.json",{"object_type":"AirNowClosureArchiveIndexPreservationBlockerConsolidation","records":blks,"blocker_count":len(blks),"created_at":created_at}); wjl(out/"closure_archive_index_preservation_blocker_consolidation.jsonl",blks)
 wj(out/"closure_archive_index_preservation_non_execution_attestation.json",{"object_type":"AirNowClosureArchiveIndexPreservationNonExecutionAttestation","commands_executed":False,"finalization_actions_executed":False,"preservation_actions_executed":False,"created_at":created_at})
 wj(out/"closure_archive_index_preservation_policy_continuity_matrix.json",{"object_type":"AirNowClosureArchiveIndexPreservationPolicyContinuityMatrix","policy_attestation":pol,"validation_results":val,"continuity_status":"PASS","references":SOURCES,"created_at":created_at}); wjl(out/"closure_archive_index_preservation_policy_continuity_matrix.jsonl",[{"reference":r,"continuity_status":"PASS"} for r in SOURCES])
 wj(out/"closure_archive_index_preservation_caveat_continuity_register.json",{"object_type":"AirNowClosureArchiveIndexPreservationCaveatContinuityRegister","caveats":cav.get("caveats",[]),"created_at":created_at})
 wj(out/"closure_archive_index_preservation_readiness_final_summary.json",{"object_type":"AirNowClosureArchiveIndexPreservationReadinessFinalSummary","layer33_readiness":ready,"readiness_status":outcome,"created_at":created_at})
 wj(out/"closure_archive_index_preservation_finalization_exception_register.json",{"object_type":"AirNowClosureArchiveIndexPreservationFinalizationExceptionRegister","records":[],"created_at":created_at}); wjl(out/"closure_archive_index_preservation_finalization_exception_register.jsonl",[])
 wj(out/"closure_archive_index_preservation_finalization_rerun_plan.json",{"object_type":"AirNowClosureArchiveIndexPreservationFinalizationRerunPlan","steps":[],"created_at":created_at})
 wj(out/"closure_archive_index_preservation_finalization_status_board.json",{"object_type":"AirNowClosureArchiveIndexPreservationFinalizationStatusBoard","board_status":"CLOSURE_ARCHIVE_INDEX_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY","created_at":created_at})
 (out/"closure_archive_index_preservation_finalization_status_board.md").write_text("# AirNow Layer 34 Closure Archive Index Preservation Finalization Status Board\n\nInternal-only finalization planning complete.\n",encoding="utf-8")
 (out/"closure_archive_index_preservation_finalization_report.md").write_text("# AirNow Layer 34 Closure Archive Index Preservation Finalization Report\n\nCompiled internal finalization ledger from Layer 33 artifacts. No preservation/index/database/search/catalog/closure execution performed.\n",encoding="utf-8")
 packet_hash=None
 if m.get("finalization_policy",{}).get("include_packet") is True:
  _,packet_hash=_packet(out,created_at)
 rec={"object_type":"AirNowClosureArchiveIndexPreservationFinalizationReceipt","schema_version":"v1","workflow_runner":"airnow_layer34_closure_archive_index_preservation_finalization","manifest_id":m.get("manifest_id"),"workflow_outcome":"CLOSURE_ARCHIVE_INDEX_PRESERVATION_FINALIZATION_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"finalization_actions_executed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"closure_archive_index_preservation_finalization_packet_hash":packet_hash},"created_at":created_at}
 wj(out/"closure_archive_index_preservation_finalization_receipt.json",rec); return rec
