import json
from pathlib import Path
from .checksums import sha256_path
from .constants import REQUIRED_L28,FORBIDDEN_RECEIPT_TRUE,EVIDENCE_TYPES,INTERNAL_ONLY_DISCLAIMER,FORBIDDEN_TEXT,COORD,SOURCES
from .ids import cjson,sid
from .loaders import loadj
from .manifest import validate_manifest,validate_path_safe

def _wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def _wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows),encoding="utf-8")

def _receipt(mid,created_at,errors):
    ok=not errors
    return {"object_type":"AirNowClosureArchiveIndexReviewReceipt","schema_version":"v1","workflow_runner":"airnow_layer29_closure_archive_index_review","manifest_id":mid,"workflow_outcome":"CLOSURE_ARCHIVE_INDEX_REVIEW_ACCEPTED_FOR_INTERNAL_REVIEW" if ok else "CLOSURE_ARCHIVE_INDEX_REVIEW_DENIED","validation_outcome":"PASS" if ok else "FAIL","finite_outcome":"ANSWER" if ok else "DENY","commands_executed":False,"review_actions_executed":False,"index_executed":False,"database_write_executed":False,"public_catalog_created":False,"search_service_created":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(errors),"output_hashes":{"closure_archive_index_review_packet_hash":None},"created_at":created_at}

def run_closure_archive_index_review(manifest_path,out_dir,created_at):
    m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); e=[]
    e.extend(validate_manifest(m))
    l28=m.get("layer28_inputs",{})
    for k in sorted(REQUIRED_L28):
        p=l28.get(k)
        if not p: e.append(f"MISSING_REQUIRED_INPUT:layer28_inputs:{k}"); continue
        if not validate_path_safe(p): e.append(f"UNSAFE_PATH:layer28_inputs:{k}"); continue
        if not Path(p).exists(): e.append(f"MISSING_INPUT_FILE:layer28_inputs:{k}")
    ev=m.get("manual_review_evidence",[])
    for i,x in enumerate(ev):
        if x.get("evidence_type") not in EVIDENCE_TYPES: e.append(f"INVALID_EVIDENCE_TYPE:{i}")
        p=x.get("path")
        if not p or not validate_path_safe(p): e.append(f"UNSAFE_PATH:manual_review_evidence:{i}")
        elif not Path(p).exists(): e.append(f"MISSING_INPUT_FILE:manual_review_evidence:{i}")
    if e:
        r=_receipt(m.get("manifest_id"),created_at,e); _wj(out/"closure_archive_index_review_receipt.json",r); return r
    l28r=loadj(l28["closure_archive_index_receipt_json"])
    if l28r.get("object_type")!="AirNowClosureArchiveIndexReceipt": e.append("INVALID_LAYER28_RECEIPT_OBJECT_TYPE")
    for f in FORBIDDEN_RECEIPT_TRUE:
        if l28r.get(f) is True: e.append(f"L28_RECEIPT_FORBIDDEN:{f}")
    rows=[]
    for x in ev:
        p=Path(x["path"]); txt=p.read_text(encoding="utf-8")
        if p.suffix.lower() in {".md",".txt"}:
            if INTERNAL_ONLY_DISCLAIMER not in txt: e.append(f"MISSING_INTERNAL_DISCLAIMER:{p.name}")
            if COORD.search(txt): e.append(f"COORDINATE_LEAK:{p.name}")
            if FORBIDDEN_TEXT.search(txt): e.append(f"FORBIDDEN_TEXT:{p.name}")
        rid=sid("evidence",[x.get("evidence_type"),x.get("path")])
        rows.append({"evidence_id":rid,"evidence_type":x["evidence_type"],"path":x["path"],"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
    rows=sorted(rows,key=lambda r:r["evidence_id"])
    if e:
        r=_receipt(m.get("manifest_id"),created_at,e); _wj(out/"closure_archive_index_review_receipt.json",r); return r
    _wj(out/"closure_archive_index_review_manifest.resolved.json",{"object_type":"AirNowClosureArchiveIndexReviewManifestResolved","manifest_id":m.get("manifest_id"),"created_at":created_at,"authoritative_references":SOURCES})
    _wj(out/"closure_archive_index_review_evidence_inventory.json",{"object_type":"AirNowClosureArchiveIndexReviewEvidenceInventory","records":rows,"created_at":created_at}); _wjl(out/"closure_archive_index_review_evidence_inventory.jsonl",rows)
    assess=[{"assessment_id":sid("assess",[r["evidence_id"]]),"evidence_id":r["evidence_id"],"assessment":"CANDIDATE_SUPPORT_INTERNAL_REVIEW"} for r in rows]; assess=sorted(assess,key=lambda x:x["assessment_id"])
    _wj(out/"closure_archive_index_review_assessment_matrix.json",{"object_type":"AirNowClosureArchiveIndexReviewAssessmentMatrix","records":assess,"created_at":created_at}); _wjl(out/"closure_archive_index_review_assessment_matrix.jsonl",assess)
    sat=[{"item_satisfaction_id":sid("sat",[a["assessment_id"]]),"assessment_id":a["assessment_id"],"satisfied":True} for a in assess]; sat=sorted(sat,key=lambda x:x["item_satisfaction_id"])
    _wj(out/"closure_archive_index_item_satisfaction_matrix.json",{"object_type":"AirNowClosureArchiveIndexItemSatisfactionMatrix","records":sat,"created_at":created_at}); _wjl(out/"closure_archive_index_item_satisfaction_matrix.jsonl",sat)
    cand=sorted([{"candidate_id":sid("cand",[m.get("manifest_id")]),"candidate":"ACCEPT_LAYER28_INDEX_PLAN_FOR_MANUAL_INTERNAL_REVIEW_ONLY","accepted":True}],key=lambda x:x["candidate_id"])
    _wjl(out/"closure_archive_index_acceptance_candidates.jsonl",cand); _wjl(out/"residual_closure_archive_index_blockers.jsonl",[])
    vals=[{"validation_id":sid("val",[m.get("manifest_id")]),"validation_outcome":"PASS"}]
    _wj(out/"closure_archive_index_review_validation_results.json",{"object_type":"AirNowClosureArchiveIndexReviewValidationResults","records":vals,"created_at":created_at}); _wjl(out/"closure_archive_index_review_validation_results.jsonl",vals)
    _wj(out/"closure_archive_index_review_readiness_summary.json",{"object_type":"AirNowClosureArchiveIndexReviewReadinessSummary","status":"READY_FOR_MANUAL_INTERNAL_INDEX_REVIEW_ONLY","created_at":created_at})
    _wj(out/"closure_archive_index_review_rerun_plan.json",{"object_type":"AirNowClosureArchiveIndexReviewRerunPlan","steps":[],"created_at":created_at})
    _wj(out/"closure_archive_index_review_policy_attestation.json",{"object_type":"AirNowClosureArchiveIndexReviewPolicyAttestation","internal_only":True,"public_release_allowed":False,"created_at":created_at})
    _wj(out/"closure_archive_index_review_caveat_register.json",{"object_type":"AirNowClosureArchiveIndexReviewCaveatRegister","caveats":["Candidate-only manual internal review intake."],"created_at":created_at})
    _wj(out/"closure_archive_index_review_status_board.json",{"object_type":"AirNowClosureArchiveIndexReviewStatusBoard","board_status":"CLOSURE_ARCHIVE_INDEX_REVIEW_INTAKE_COMPLETE_INTERNAL_ONLY","created_at":created_at})
    (out/"closure_archive_index_review_status_board.md").write_text("# AirNow Layer 29 Closure Archive Index Review Status Board\n\nInternal-only intake complete.\n",encoding="utf-8")
    (out/"closure_archive_index_review_report.md").write_text("# AirNow Layer 29 Closure Archive Index Review Report\n\nAccepted for manual internal index review only. No execution actions performed.\n",encoding="utf-8")
    r=_receipt(m.get("manifest_id"),created_at,[])
    _wj(out/"closure_archive_index_review_receipt.json",r)
    return r
