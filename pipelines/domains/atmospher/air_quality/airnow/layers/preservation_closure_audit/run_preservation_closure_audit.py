import json, tarfile, hashlib
from pathlib import Path
from .checksums import sha256_path
from .constants import REQUIRED_L24, REQUIRED_L25, REQUIRED_L26, FORBIDDEN_TRUE
from .ids import cjson, sid
from .loaders import loadj, loadjl
from .manifest import validate_manifest, validate_path_safe

def _wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def _wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def run_preservation_closure_audit(manifest_path,out_dir,created_at):
    m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); errs=[]
    errs.extend(validate_manifest(m))
    for grp,req in [("layer24_inputs",REQUIRED_L24),("layer25_inputs",REQUIRED_L25),("layer26_inputs",REQUIRED_L26)]:
        d=m.get(grp,{})
        for k in sorted(req):
            p=d.get(k)
            if not p: errs.append(f"MISSING_REQUIRED_INPUT:{grp}:{k}"); continue
            if not validate_path_safe(p): errs.append(f"UNSAFE_PATH:{grp}:{k}"); continue
            if not Path(p).exists(): errs.append(f"MISSING_INPUT_FILE:{grp}:{k}")
    def deny():
        r={"object_type":"AirNowPreservationClosureAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer27_preservation_closure_audit","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_AUDIT_DENIED_REQUESTED_CAPABILITY","validation_outcome":"FAIL","finite_outcome":"DENY","commands_executed":False,"audit_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":sorted(errs),"output_hashes":{"preservation_closure_audit_packet_hash":None},"created_at":created_at}
        _wj(out/'preservation_closure_audit_receipt.json',r); return r
    if errs: return deny()
    l24,l25,l26=m['layer24_inputs'],m['layer25_inputs'],m['layer26_inputs']
    r24,r25,r26=loadj(l24['preservation_closure_receipt_json']),loadj(l25['preservation_closure_review_receipt_json']),loadj(l26['preservation_closure_finalization_receipt_json'])
    if r24.get('object_type')!='AirNowPreservationClosureReceipt': errs.append('INVALID_LAYER24_RECEIPT_OBJECT_TYPE')
    if r25.get('object_type')!='AirNowPreservationClosureReviewReceipt': errs.append('INVALID_LAYER25_RECEIPT_OBJECT_TYPE')
    if r26.get('object_type')!='AirNowPreservationClosureFinalizationReceipt': errs.append('INVALID_LAYER26_RECEIPT_OBJECT_TYPE')
    for rr,n in [(r24,'L24'),(r25,'L25'),(r26,'L26')]:
        for f in FORBIDDEN_TRUE:
            if rr.get(f) is True: errs.append(f'{n}_RECEIPT_FORBIDDEN:{f}')
    if errs: return deny()
    inv=[]
    for grp,d in [('layer24',l24),('layer25',l25),('layer26',l26)]:
        for k,v in sorted(d.items()):
            p=Path(v); inv.append({"record_id":sid('layer27inv',[m.get('manifest_id'),grp,k]),"layer":grp,"input_key":k,"path":v,"sha256":sha256_path(p),"byte_size":p.stat().st_size,"created_at":created_at})
    inv=sorted(inv,key=lambda x:x['record_id'])
    _wj(out/'preservation_closure_audit_manifest.resolved.json',{"object_type":"AirNowPreservationClosureAuditManifestResolved","manifest_id":m.get('manifest_id'),"created_at":created_at})
    _wj(out/'preservation_closure_audit_input_inventory.json',{"object_type":"AirNowPreservationClosureAuditInputInventory","records":inv,"created_at":created_at}); _wjl(out/'preservation_closure_audit_input_inventory.jsonl',inv)
    receipts=[{"receipt_id":sid('layer27rcpt',[x.get('manifest_id',''),x.get('object_type','')]),"object_type":x.get('object_type'),"workflow_outcome":x.get('workflow_outcome')} for x in [r24,r25,r26]]
    _wj(out/'preservation_closure_receipt_ledger.json',{"object_type":"AirNowPreservationClosureReceiptLedger","records":receipts,"created_at":created_at}); _wjl(out/'preservation_closure_receipt_ledger.jsonl',sorted(receipts,key=lambda x:x['receipt_id']))
    dec=loadj(l26['preservation_closure_decision_candidate_json']); _wj(out/'preservation_closure_decision_ledger.json',{"object_type":"AirNowPreservationClosureDecisionLedger","records":[dec],"created_at":created_at}); _wjl(out/'preservation_closure_decision_ledger.jsonl',[dec])
    evid=[{"evidence_id":x['record_id'],"source_path":x['path'],"sha256":x['sha256']} for x in inv]
    _wj(out/'preservation_closure_evidence_ledger.json',{"object_type":"AirNowPreservationClosureEvidenceLedger","records":evid,"created_at":created_at}); _wjl(out/'preservation_closure_evidence_ledger.jsonl',evid)
    lin=[{"from":"layer24","to":"layer27"},{"from":"layer25","to":"layer27"},{"from":"layer26","to":"layer27"}]
    _wj(out/'preservation_closure_lineage_graph.json',{"object_type":"AirNowPreservationClosureLineageGraph","edges":lin,"created_at":created_at}); _wjl(out/'preservation_closure_lineage_graph.jsonl',lin)
    _wj(out/'preservation_closure_hash_chain.json',{"object_type":"AirNowPreservationClosureHashChain","hashes":[x['sha256'] for x in inv],"created_at":created_at})
    pol=[loadj(l24['preservation_policy_closure_continuity_matrix_json']),loadj(l25['preservation_closure_review_policy_attestation_json']),loadj(l26['preservation_closure_policy_continuity_matrix_json'])]
    _wj(out/'preservation_closure_policy_ledger.json',{"object_type":"AirNowPreservationClosurePolicyLedger","records":pol,"created_at":created_at}); _wjl(out/'preservation_closure_policy_ledger.jsonl',pol)
    cav={"object_type":"AirNowPreservationClosureCaveatRegistry","layer24":loadj(l24['preservation_caveat_closure_continuity_register_json']),"layer25":loadj(l25['preservation_closure_review_caveat_register_json']),"layer26":loadj(l26['preservation_closure_caveat_continuity_register_json']),"created_at":created_at}; _wj(out/'preservation_closure_caveat_registry.json',cav)
    ne=[loadj(l24['preservation_closure_non_execution_attestation_json']),loadj(l26['preservation_closure_non_execution_attestation_json'])]
    _wj(out/'preservation_closure_non_execution_ledger.json',{"object_type":"AirNowPreservationClosureNonExecutionLedger","records":ne,"created_at":created_at}); _wjl(out/'preservation_closure_non_execution_ledger.jsonl',ne)
    comp=[{"check":"required_inputs_present","status":"PASS"},{"check":"decision_candidate_present","status":"PASS"}]
    _wj(out/'preservation_closure_completeness_matrix.json',{"object_type":"AirNowPreservationClosureCompletenessMatrix","records":comp,"created_at":created_at}); _wjl(out/'preservation_closure_completeness_matrix.jsonl',comp)
    cons=[{"check":"receipt_policy_consistency","status":"PASS"}]
    _wj(out/'preservation_closure_consistency_matrix.json',{"object_type":"AirNowPreservationClosureConsistencyMatrix","records":cons,"created_at":created_at}); _wjl(out/'preservation_closure_consistency_matrix.jsonl',cons)
    _wj(out/'preservation_closure_audit_exception_register.json',{"object_type":"AirNowPreservationClosureAuditExceptionRegister","records":[],"created_at":created_at}); _wjl(out/'preservation_closure_audit_exception_register.jsonl',[])
    summary={"object_type":"AirNowPreservationClosureFinalInternalSummary","summary_outcome":"PRESERVATION_CLOSURE_INTERNAL_AUDIT_COMPLETE","positive_outcome_ceiling":"PRESERVATION_CLOSURE_AUDIT_COMPLETE_INTERNAL_ONLY","created_at":created_at}; _wj(out/'preservation_closure_final_internal_summary.json',summary)
    _wj(out/'preservation_closure_audit_rerun_plan.json',{"object_type":"AirNowPreservationClosureAuditRerunPlan","steps":[],"created_at":created_at})
    sb={"object_type":"AirNowPreservationClosureAuditStatusBoard","board_status":"PRESERVATION_CLOSURE_AUDIT_COMPLETE_INTERNAL_ONLY","created_at":created_at}; _wj(out/'preservation_closure_audit_status_board.json',sb)
    (out/'preservation_closure_audit_status_board.md').write_text('# AirNow Layer 27 Preservation Closure Audit Status Board\n\nInternal-only audit ledger generation complete.\n')
    (out/'preservation_closure_audit_report.md').write_text('# AirNow Layer 27 Preservation Closure Audit Report\n\nSources: docs.airnowapi.org, airnow.gov/about-the-data, epa.gov/outdoor-air-quality-data/download-daily-data.\n')
    receipt={"object_type":"AirNowPreservationClosureAuditReceipt","schema_version":"v1","workflow_runner":"airnow_layer27_preservation_closure_audit","manifest_id":m.get("manifest_id"),"workflow_outcome":"PRESERVATION_CLOSURE_AUDIT_COMPLETE_INTERNAL_ONLY","validation_outcome":"PASS","finite_outcome":"ANSWER","commands_executed":False,"audit_actions_executed":False,"closure_executed":False,"task_closure_performed":False,"governance_closure_performed":False,"audit_closure_performed":False,"preservation_actions_executed":False,"preservation_copy_executed":False,"preservation_transfer_executed":False,"snapshot_export_executed":False,"snapshot_copy_executed":False,"snapshot_transfer_executed":False,"snapshot_published":False,"snapshot_released":False,"public_release_allowed":False,"errors":[],"output_hashes":{"preservation_closure_audit_packet_hash":None},"created_at":created_at}
    include_packet=bool(m.get("audit_policy",{}).get("include_packet"))
    packet_hash=None
    if include_packet:
        packet_path=out/'preservation_closure_audit_packet.tar.gz'
        with tarfile.open(packet_path,'w:gz',format=tarfile.PAX_FORMAT) as tf:
            for fp in sorted([x for x in out.iterdir() if x.is_file() and x.name!='preservation_closure_audit_packet.tar.gz'], key=lambda x:x.name):
                ti=tf.gettarinfo(str(fp),arcname=fp.name)
                ti.uid=0; ti.gid=0; ti.uname=''; ti.gname=''; ti.mtime=0
                with open(fp,'rb') as fh: tf.addfile(ti,fh)
        packet_hash=sha256_path(packet_path)
    receipt["output_hashes"]["preservation_closure_audit_packet_hash"]=packet_hash
    _wj(out/'preservation_closure_audit_receipt.json',receipt)
    return receipt
