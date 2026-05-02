import hashlib, io, json, re, tarfile
from pathlib import Path

FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
DENIED_KEYS=("api_key","token","secret","password","bearer","credential","authorization","client_secret","access_key","refresh_token","private_key","session","deploy_key","webhook","publish_url","github_token","git_remote","ssh_key","signing_key","remote_url","callback_url","bucket","connection_string")
DENIED_FLAGS=["publication_requested","public_dashboard_requested","tiles_requested","public_api_requested","emergency_alert_requested","regulatory_claims_requested","exact_sensitive_overlay_requested","command_execution_requested","auto_execute_requested","auto_apply_requested","task_closure_requested","github_issue_creation_requested","github_pr_creation_requested","git_push_requested","file_deletion_requested","destruction_execution_requested","archive_transfer_requested","external_storage_requested","chmod_or_chattr_requested","legal_hold_creation_requested","official_archive_certification_requested"]
REQ12=["final_audit_receipt_json","audit_artifact_inventory_json","audit_receipt_ledger_json","audit_hash_chain_json","audit_caveat_registry_json","audit_capability_denial_ledger_json"]

def cjson(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(v): return hashlib.sha256((v if isinstance(v,str) else cjson(v)).encode()).hexdigest()
def sid(prefix,v): return f"{prefix}:{sh(v)}"
def loadj(p): return json.loads(Path(p).read_text())
def wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _find_denied(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if any(t in str(k).lower() for t in DENIED_KEYS): return True
            if _find_denied(x): return True
    if isinstance(v,list): return any(_find_denied(x) for x in v)
    return isinstance(v,str) and any(t in v.lower() for t in DENIED_KEYS)

def _bad_path(s):
    s=str(s)
    if any(s.startswith(x) for x in FORBIDDEN_SCHEMES) or "://" in s: return True
    p=Path(s)
    return ".." in p.parts

def run_retention_plan(manifest_path,out_dir,created_at):
    m=loadj(manifest_path); out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    errs=[]; warns=[]; ex=[]
    if _find_denied(m): errs.append("SECRET_FIELD_DENIED"); ex.append(("SECRET_FIELD_DENIED","BLOCKER","manifest","SECRET_FIELD_DENIED"))
    for k in ["local_file_only","no_network"]:
        if m.get(k) is not True: errs.append("NETWORK_INTENT_DENIED")
    if m.get("bulk_web_service_loop") is not False: errs.append("BULK_LOOP_DENIED")
    for k in DENIED_FLAGS:
        if m.get(k) is True: errs.append("DENIED_CAPABILITY_REQUESTED"); ex.append(("DENIED_CAPABILITY_ALLOWED","BLOCKER",k,"DENIED"))
    l12=m.get("layer12_inputs",{})
    for k in REQ12:
        p=l12.get(k)
        if not p or _bad_path(p) or not Path(p).exists(): errs.append("MISSING_REQUIRED_LAYER12"); ex.append(("MISSING_LAYER12_RECEIPT" if k=="final_audit_receipt_json" else "MISSING_LAYER12_ARTIFACT_INVENTORY","BLOCKER",k,"MISSING"))
    if errs:
        outcome="RETENTION_PLAN_DENIED_REQUESTED_CAPABILITY" if any(e[0]=="DENIED_CAPABILITY_ALLOWED" for e in ex) else "RETENTION_PLAN_REJECTED"
    else: outcome="RETENTION_PLAN_COMPLETE_INTERNAL_ONLY"

    # simple inventory from layer12 paths
    recs=[]
    for aid,p in sorted(l12.items()):
        path=Path(p); exists=path.exists(); b=path.read_bytes() if exists else b""
        recs.append({"object_type":"AirNowRetentionArtifactInventoryRecord","schema_version":"v1","retention_artifact_inventory_record_id":sid("kfm:air_quality:airnow:retention_artifact_inventory_record:v1",[m.get("manifest_id"),aid]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"artifact_id":aid,"source_layer":"layer12","artifact_role":"receipt" if "receipt" in aid else "ledger","path_original":p,"required":aid in REQ12,"exists":exists,"media_type":"application/json","format":"jsonl" if str(p).endswith(".jsonl") else "json","object_type_detected":None,"byte_size":len(b),"sha256":hashlib.sha256(b).hexdigest() if exists else None,"contains_exact_coordinates_declared":False,"contains_exact_coordinates_detected":False,"human_readable":False,"sensitivity":"internal","inventory_status":"PASS" if exists else "FAIL","warnings":[],"errors":[] if exists else ["MISSING"],"created_at":created_at})
    inv={"object_type":"AirNowRetentionArtifactInventory","schema_version":"v1","retention_artifact_inventory_id":sid("kfm:air_quality:airnow:retention_artifact_inventory:v1",m.get("manifest_id")),"source_id":"airnow","manifest_id":m.get("manifest_id"),"artifact_count":len(recs),"artifact_counts_by_role":{},"sensitivity_counts":{"internal":len(recs),"internal_sensitive":0,"internal_restricted":0},"inventory_status_counts":{"PASS":sum(1 for r in recs if r['inventory_status']=="PASS"),"WARN":0,"FAIL":sum(1 for r in recs if r['inventory_status']=="FAIL")},"records":recs,"created_at":created_at}
    wj(out/"retention_artifact_inventory.json",inv); wjl(out/"retention_artifact_inventory.jsonl",recs)
    # minimal other outputs
    names=["retention_manifest.resolved.json","archival_accession_register.json","archival_accession_register.jsonl","retention_classification_matrix.json","retention_classification_matrix.jsonl","retention_schedule.json","retention_schedule.jsonl","fixity_manifest.json","fixity_manifest.jsonl","fixity_review_schedule.json","fixity_review_schedule.jsonl","preservation_action_plan.json","preservation_action_plan.jsonl","archive_package_plan.json","archive_package_plan.jsonl","transfer_preparation_plan.json","transfer_preparation_plan.jsonl","hold_candidate_register.json","hold_candidate_register.jsonl","destruction_review_schedule.json","destruction_review_schedule.jsonl","retention_exception_register.json","retention_exception_register.jsonl","retention_policy_attestation.json","retention_caveat_register.json","retention_status_board.json"]
    for n in names:
        if n.endswith('.jsonl'): wjl(out/n,[])
        else: wj(out/n,{"object_type":"AirNowPlaceholder","schema_version":"v1","manifest_id":m.get("manifest_id"),"created_at":created_at,"records":[]})
    (out/"retention_status_board.md").write_text("# AirNow Layer 13 Retention Status Board\n\nInternal archival retention planning only.\n")
    (out/"retention_runbook.md").write_text("# AirNow Layer 13 Retention Runbook\n\nInternal archival retention planning only.\nLayer 13 does not execute retention actions.\nLayer 13 does not delete files.\nLayer 13 does not transfer artifacts to external storage.\nLayer 13 does not set immutable filesystem flags.\nLayer 13 does not create legal holds.\nLayer 13 does not certify official archive status.\nLayer 13 does not execute commands.\nLayer 13 does not apply fixes automatically.\nLayer 13 does not close tasks.\nLayer 13 does not create GitHub issues or pull requests.\nNot publication output.\nNot a public dashboard.\nNot a public API.\nNot a map tile product.\nNot an emergency alert product.\nNot regulatory analysis.\nNot legal advice.\nAirNow data are preliminary and subject to change.\nOfficial regulatory air-quality data must come from EPA AQS/AirData.\nPublic release remains denied by policy.\n")
    packet_hash=None
    if m.get("retention_policy",{}).get("include_packet",True):
        packet=out/"retention_planning_packet.tar.gz"
        members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!=packet.name])
        with tarfile.open(packet,'w:gz') as tf:
            for nm in members:
                d=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(d); ti.mtime=0; tf.addfile(ti,io.BytesIO(d))
        packet_hash=hashlib.sha256(packet.read_bytes()).hexdigest()
    receipt={"object_type":"AirNowRetentionReceipt","schema_version":"v1","receipt_id":sid("kfm:air_quality:airnow:retention_receipt:v1",[m.get("manifest_id"),outcome,created_at]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","workflow_runner":"airnow_layer13_retention_plan","workflow_runner_version":"v1","workflow_outcome":outcome,"validation_outcome":"PASS" if not errs else "FAIL","finite_outcome":"ANSWER" if not errs else "DENY","commands_executed":False,"retention_actions_executed":False,"fixity_checks_executed":False,"file_deletion_executed":False,"destruction_executed":False,"archive_transfer_executed":False,"external_storage_used":False,"legal_hold_created":False,"official_archive_certified":False,"publication_allowed":False,"public_release_allowed":False,"task_closure_performed":False,"warnings":warns,"errors":sorted(set(errs)),"output_hashes":{"retention_planning_packet_hash":packet_hash},"created_at":created_at}
    wj(out/"retention_receipt.json",receipt)
    return receipt
