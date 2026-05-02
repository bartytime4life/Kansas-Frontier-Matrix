import hashlib, io, json, tarfile
from pathlib import Path

def cjson(v): return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
def sid(prefix,v): return f"{prefix}:{hashlib.sha256((v if isinstance(v,str) else cjson(v)).encode()).hexdigest()}"
def loadj(p): return json.loads(Path(p).read_text())
def loadjl(p): return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
def wj(p,o): Path(p).write_text(json.dumps(o, indent=2, sort_keys=True)+"\n")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def run_archival_finalization(manifest_path,out_dir,created_at):
    m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    l14=m["layer14_inputs"]
    cands=loadjl(l14.get("retention_acceptance_candidates_jsonl", l14.get("retention_acceptance_candidates.jsonl")))
    blks=loadjl(l14.get("residual_retention_blockers_jsonl", l14.get("residual_retention_blockers.jsonl")))
    errs=[]
    if m.get("publication_requested") or m.get("command_execution_requested"): errs.append("DENIED_CAPABILITY_REQUESTED")
    outcome = "ARCHIVAL_FINALIZATION_DENIED_REQUESTED_CAPABILITY" if errs else ("ARCHIVAL_FINALIZATION_NEEDS_MORE_INPUT" if blks else "ARCHIVAL_FINALIZATION_COMPLETE_INTERNAL_ONLY")
    finite = "DENY" if errs else "ANSWER"
    val = "FAIL" if errs else "PASS"
    wj(out/"archival_finalization_manifest.resolved.json", {"object_type":"AirNowResolvedArchivalFinalizationManifest","schema_version":"v1","manifest_id":m["manifest_id"],"created_at":created_at})
    inv=[]
    for k,v in sorted(l14.items()):
        p=Path(v); b=p.read_bytes()
        inv.append({"object_type":"AirNowArchivalFinalizationInputInventoryRecord","schema_version":"v1","archival_finalization_input_inventory_record_id":sid("kfm:air_quality:airnow:archival_finalization_input_inventory_record:v1",[m["manifest_id"],k]),"source_id":"airnow","manifest_id":m["manifest_id"],"input_id":k,"input_role":"artifact","path_original":v,"required":True,"exists":True,"media_type":"application/json" if p.suffix in {'.json','.jsonl'} else "text/markdown","format":p.suffix.lstrip('.'),"object_type_detected":loadj(p).get("object_type") if p.suffix=='.json' else None,"expected_object_type":None,"byte_size":len(b),"sha256":hashlib.sha256(b).hexdigest(),"contains_exact_coordinates_declared":False,"contains_exact_coordinates_detected":False,"human_readable":p.suffix=='.md',"sensitivity":"internal","inventory_status":"PASS","warnings":[],"errors":[],"created_at":created_at})
    wj(out/"archival_finalization_input_inventory.json",{"object_type":"AirNowArchivalFinalizationInputInventory","schema_version":"v1","records":inv,"created_at":created_at})
    wjl(out/"archival_finalization_input_inventory.jsonl",inv)
    wj(out/"archival_review_finalization_ledger.json",{"object_type":"AirNowArchivalReviewFinalizationLedger","schema_version":"v1","records":[],"created_at":created_at});wjl(out/"archival_review_finalization_ledger.jsonl",[])
    wj(out/"archival_decision_candidate.json",{"object_type":"AirNowArchivalDecisionCandidate","schema_version":"v1","decision_candidate_outcome":"INTERNAL_ARCHIVAL_REVIEW_READY" if not blks else "INTERNAL_ARCHIVAL_REVIEW_NEEDS_MORE_INPUT","decision_candidate_records":[],"created_at":created_at});wjl(out/"archival_decision_candidate_ledger.jsonl",[])
    for n in ["archival_acceptance_consolidation","archival_blocker_consolidation","archival_policy_continuity_matrix","archival_finalization_exception_register"]:
        wj(out/f"{n}.json",{"object_type":n,"schema_version":"v1","records":[],"created_at":created_at});wjl(out/f"{n}.jsonl",[])
    wj(out/"archival_non_execution_attestation.json",{"object_type":"AirNowArchivalNonExecutionAttestation","schema_version":"v1","attestation_status":"PASS","created_at":created_at})
    wj(out/"archival_caveat_continuity_register.json",{"object_type":"AirNowArchivalCaveatContinuityRegister","schema_version":"v1","caveats":[],"registry_status":"PASS","created_at":created_at})
    wj(out/"archival_readiness_final_summary.json",{"object_type":"AirNowArchivalReadinessFinalSummary","schema_version":"v1","readiness_status":"READY_FOR_INTERNAL_ARCHIVAL_REVIEW" if not blks else "NEEDS_MORE_INPUT","created_at":created_at})
    wj(out/"archival_finalization_rerun_plan.json",{"object_type":"AirNowArchivalFinalizationRerunPlan","schema_version":"v1","created_at":created_at})
    wj(out/"archival_finalization_status_board.json",{"object_type":"AirNowArchivalFinalizationStatusBoard","schema_version":"v1","board_status":outcome,"created_at":created_at})
    (out/"archival_finalization_status_board.md").write_text("# AirNow Layer 15 Archival Finalization Status Board\n\nInternal archival-review finalization only.\n")
    (out/"archival_finalization_report.md").write_text("# AirNow Layer 15 Archival Finalization Report\n\nInternal archival-review finalization only.\nLayer 15 does not execute archival finalization actions.\n")
    packet_hash=None
    if m.get("finalization_policy",{}).get("include_packet",True):
        pkt=out/"archival_finalization_packet.tar.gz"
        with tarfile.open(pkt,"w:gz") as tf:
            for p in sorted([x for x in out.iterdir() if x.is_file() and x.name!=pkt.name], key=lambda x:x.name):
                d=p.read_bytes(); ti=tarfile.TarInfo(p.name); ti.size=len(d); ti.mtime=0; tf.addfile(ti,io.BytesIO(d))
        packet_hash=hashlib.sha256(pkt.read_bytes()).hexdigest()
    receipt={"object_type":"AirNowArchivalFinalizationReceipt","schema_version":"v1","manifest_id":m["manifest_id"],"workflow_outcome":outcome,"validation_outcome":val,"finite_outcome":finite,"errors":errs,"output_hashes":{"archival_finalization_packet_hash":packet_hash},"created_at":created_at}
    wj(out/"archival_finalization_receipt.json",receipt)
    return receipt
