import io, json, tarfile, hashlib, re
from pathlib import Path

FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
SECRET_KEYS=("api_key","token","secret","password","authorization","credential","github_token","private_key","remote_url")
DENY_FLAGS=["publication_requested","public_dashboard_requested","tiles_requested","public_api_requested","emergency_alert_requested","regulatory_claims_requested","exact_sensitive_overlay_requested","auto_apply_requested","task_closure_requested","github_issue_creation_requested","github_pr_creation_requested","git_push_requested"]
REQ_DISCLAIMERS=["Internal manual evidence verification only.","Layer 9 does not apply fixes automatically.","Layer 9 does not close tasks.","Layer 9 does not create GitHub issues or pull requests.","Not publication output.","Not a public dashboard.","Not a public API.","Not a map tile product.","Not an emergency alert product.","Not regulatory analysis.","AirNow data are preliminary and subject to change.","Official regulatory air-quality data must come from EPA AQS/AirData.","Public release remains denied by policy."]

def cjson(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(txt): return hashlib.sha256(txt.encode("utf-8")).hexdigest()
def sid(prefix,parts): return f"{prefix}:{sh(cjson(parts))}"
def _loadj(p): return json.loads(Path(p).read_text())
def _scan_secret(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if any(s in str(k).lower() for s in SECRET_KEYS): return True
            if _scan_secret(x): return True
    if isinstance(v,list): return any(_scan_secret(i) for i in v)
    if isinstance(v,str):
        lo=v.lower()
        return any(k in lo for k in ["api_key","bearer ","github_token","password="])
    return False

def run_manual_evidence_verification(manifest_path,out_dir,created_at):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    m=_loadj(manifest_path); errors=[]; warnings=[]
    if _scan_secret(m): errors.append("SECRET_FIELD_DENIED")
    if m.get("local_file_only") is not True or m.get("no_network") is not True: errors.append("NETWORK_INTENT_DENIED")
    for f in DENY_FLAGS:
        if m.get(f) is True: errors.append("DENIED_REQUESTED_CAPABILITY")
    for path in list(m.get("layer8_inputs",{}).values())+[x.get("path","") for x in m.get("manual_evidence",[])]:
        if any(str(path).startswith(s) for s in FORBIDDEN_SCHEMES) or "://" in str(path): errors.append("UNSAFE_PATH")
    l8=m.get("layer8_inputs",{})
    required=["remediation_receipt_json","remediation_task_queue_jsonl","remediation_validation_matrix_json","remediation_evidence_requests_jsonl"]
    for r in required:
        if not Path(l8.get(r,"")).exists(): errors.append("MISSING_LAYER8_INPUT")
    tasks=[json.loads(x) for x in Path(l8.get("remediation_task_queue_jsonl","")).read_text().splitlines() if x.strip()] if Path(l8.get("remediation_task_queue_jsonl","")).exists() else []
    requests=[json.loads(x) for x in Path(l8.get("remediation_evidence_requests_jsonl","")).read_text().splitlines() if x.strip()] if Path(l8.get("remediation_evidence_requests_jsonl","")).exists() else []
    task_ids={t.get("task_id") for t in tasks}; req_ids={r.get("evidence_request_id") for r in requests}
    inv=[]; assess=[]
    for e in sorted(m.get("manual_evidence",[]),key=lambda x:(x.get("evidence_type",""),x.get("evidence_id",""),x.get("path",""))):
        p=Path(e["path"]); exists=p.exists(); txt=p.read_text() if exists else ""; b=p.read_bytes() if exists else b""
        md=e.get("human_readable",False)
        leak=bool(md and re.search(r"-?\d{1,2}\.\d{4,}\s*,\s*-?\d{1,3}\.\d{4,}",txt))
        vstat="PASS" if exists and not leak else "FAIL"
        if e.get("required") and not exists: errors.append("MISSING_REQUIRED_EVIDENCE")
        if leak: errors.append("EXACT_COORDINATE_LEAK")
        obj=None
        if exists and p.suffix==".json":
            try: obj=json.loads(txt).get("object_type")
            except Exception: pass
        rec={"object_type":"AirNowManualEvidenceInventoryRecord","schema_version":"v1","manual_evidence_inventory_record_id":sid("kfm:air_quality:airnow:manual_evidence_inventory_record:v1",[m.get("manifest_id"),e.get("evidence_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"evidence_id":e.get("evidence_id"),"evidence_type":e.get("evidence_type"),"path_original":e.get("path"),"required":bool(e.get("required")),"exists":exists,"media_type":"application/json" if p.suffix==".json" else ("text/markdown" if p.suffix==".md" else "text/plain"),"format":p.suffix.replace('.',''),"object_type_detected":obj,"related_task_id":e.get("related_task_id"),"related_evidence_request_id":e.get("related_evidence_request_id"),"byte_size":len(b),"sha256":hashlib.sha256(b).hexdigest() if exists else None,"contains_exact_coordinates_declared":bool(e.get("contains_exact_coordinates",False)),"contains_exact_coordinates_detected":leak,"human_readable":md,"sensitivity":"internal","validation_status":vstat,"warnings":[],"errors":[],"created_at":created_at}
        inv.append(rec)
        status="ACCEPTED" if vstat=="PASS" else "REJECTED"
        reason="UPDATED_MARKDOWN_DOC_PASS" if status=="ACCEPTED" else ("MISSING_REQUIRED_EVIDENCE" if not exists else "EXACT_COORDINATE_LEAK")
        if rec["related_task_id"] and rec["related_task_id"] not in task_ids and e.get("required",True): status="REJECTED"; reason="INVALID_TASK_REFERENCE"; errors.append("INVALID_TASK_REFERENCE")
        if rec["related_evidence_request_id"] and req_ids and rec["related_evidence_request_id"] not in req_ids and e.get("required",True): status="REJECTED"; reason="INVALID_EVIDENCE_REQUEST_REFERENCE"; errors.append("INVALID_EVIDENCE_REQUEST_REFERENCE")
        assess.append({"object_type":"AirNowEvidenceAssessmentRecord","schema_version":"v1","evidence_assessment_id":sid("kfm:air_quality:airnow:evidence_assessment:v1",[rec["evidence_id"],status,reason]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"evidence_id":rec["evidence_id"],"evidence_type":rec["evidence_type"],"related_task_id":rec["related_task_id"],"related_evidence_request_id":rec["related_evidence_request_id"],"assessment_status":status,"assessment_reason_code":reason,"assessment_detail":"Offline assessment.","required":rec["required"],"object_type_expected":e.get("expected_object_type"),"object_type_detected":rec["object_type_detected"],"checksum_verified":exists,"manual_attestation_verified":not e.get("manual_attestation_required",False) or any("attestation" in x.get("evidence_id","") for x in m.get("manual_evidence",[])),"required_disclaimers_present":all(d in txt for d in REQ_DISCLAIMERS) if md and exists else True,"forbidden_language_found":False,"exact_coordinates_found_in_human_doc":leak,"blocks_rerun":status!="ACCEPTED","public_release_allowed":False,"created_at":created_at})
    sat=[]; closure=[]; residual=[]
    for t in tasks:
        ta=[a for a in assess if a.get("related_task_id")==t.get("task_id") and a.get("required")]
        ok=bool(ta) and all(a["assessment_status"]=="ACCEPTED" for a in ta)
        s="SATISFIED_CANDIDATE" if ok else "NEEDS_MORE_INPUT"
        rid=sid("kfm:air_quality:airnow:task_satisfaction:v1",[t.get("task_id"),s])
        sat.append({"object_type":"AirNowTaskSatisfactionRecord","schema_version":"v1","task_satisfaction_id":rid,"source_id":"airnow","manifest_id":m.get("manifest_id"),"task_id":t.get("task_id"),"task_category":t.get("task_category","unknown"),"task_priority":t.get("task_priority","P3"),"task_status_from_layer8":t.get("task_status","OPEN_TEMPLATE_ONLY"),"satisfaction_status":s,"satisfaction_basis":"All required evidence accepted." if ok else "Missing required evidence.","accepted_evidence_assessment_ids":[a["evidence_assessment_id"] for a in ta if a["assessment_status"]=="ACCEPTED"],"rejected_evidence_assessment_ids":[a["evidence_assessment_id"] for a in ta if a["assessment_status"]!="ACCEPTED"],"missing_evidence_request_ids":[],"validation_result_ids":[],"closure_candidate_created":ok,"task_closed":False,"requires_manual_review":True,"blocks_internal_review_after_evidence":not ok,"blocks_publication_after_evidence":True,"public_release_allowed_after_evidence":False,"created_at":created_at})
        if ok: closure.append({"object_type":"AirNowClosureCandidate","schema_version":"v1","closure_candidate_id":sid("kfm:air_quality:airnow:closure_candidate:v1",[t.get("task_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"task_id":t.get("task_id"),"candidate_status":"READY_FOR_MANUAL_REVIEW","closure_not_performed":True,"task_closed":False,"closure_basis":"Required manual evidence was accepted by Layer 9 verification.","required_manual_review":True,"recommended_next_action":"Manually review evidence, then rerun Layer 7 gate using local artifacts.","public_release_allowed":False,"created_at":created_at})
        else: residual.append({"object_type":"AirNowResidualRemediationTask","schema_version":"v1","residual_task_id":sid("kfm:air_quality:airnow:residual_remediation_task:v1",[t.get("task_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"original_task_id":t.get("task_id"),"residual_status":"NEEDS_MORE_INPUT","reason_code":"MISSING_REQUIRED_EVIDENCE","reason_detail":"No accepted manual evidence satisfies the required evidence request.","next_required_evidence":[],"public_release_allowed":False,"created_at":created_at})
    workflow="MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN" if not residual and not errors else ("MANUAL_EVIDENCE_NEEDS_MORE_INPUT" if residual and not errors else "MANUAL_EVIDENCE_REJECTED")
    val="PASS" if workflow!="MANUAL_EVIDENCE_REJECTED" else "FAIL"; finite="ANSWER" if not errors else "DENY"
    # write outputs
    def wj(n,o): (out/n).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
    def wjl(n,rows): (out/n).write_text("".join(cjson(r)+"\n" for r in rows))
    resolved={"object_type":"AirNowResolvedManualEvidenceManifest","schema_version":"v1","resolved_manual_evidence_manifest_id":sid("kfm:air_quality:airnow:resolved_manual_evidence_manifest:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","lifecycle_stage":"manual_evidence_verification_not_applied_not_published","maximum_positive_outcome":"MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"auto_apply_allowed":False,"task_closure_allowed":False,"github_issue_creation_allowed":False,"github_pr_creation_allowed":False,"git_push_allowed":False,"layer8_input_count":len(l8),"manual_evidence_count":len(inv),"required_manual_evidence_count":sum(x['required'] for x in inv),"optional_manual_evidence_count":sum(not x['required'] for x in inv),"detected_layer8_workflow_outcome":"REMEDIATION_SCAFFOLD_READY","source_doc_refs":m.get("source_doc_refs",[]),"created_at":created_at}
    inv_obj={"object_type":"AirNowManualEvidenceInventory","schema_version":"v1","manual_evidence_inventory_id":sid("kfm:air_quality:airnow:manual_evidence_inventory:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"evidence_count":len(inv),"evidence_counts_by_type":{},"evidence_counts_by_status":{"PASS":sum(x['validation_status']=='PASS' for x in inv),"WARN":0,"FAIL":sum(x['validation_status']=='FAIL' for x in inv)},"records":inv,"created_at":created_at}
    assess_obj={"object_type":"AirNowEvidenceAssessmentMatrix","schema_version":"v1","records":assess,"created_at":created_at}
    sat_obj={"object_type":"AirNowTaskSatisfactionMatrix","schema_version":"v1","records":sat,"created_at":created_at}
    vres={"object_type":"AirNowVerificationValidationResults","schema_version":"v1","records":[],"created_at":created_at}
    rerun={"object_type":"AirNowRerunRecommendationPlan","schema_version":"v1","rerun_recommendation_plan_id":sid("kfm:air_quality:airnow:rerun_recommendation_plan:v1",[workflow]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"rerun_recommendation":"RERUN_LAYER7_GATE" if workflow=="MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN" else "COLLECT_MORE_EVIDENCE","rerun_allowed":workflow!="MANUAL_EVIDENCE_REJECTED","public_release_allowed":False,"recommended_commands":[],"blocked_commands":["curl","wget","gh issue create","gh pr create","git push","deploy","publish","upload"],"created_at":created_at}
    sb={"object_type":"AirNowManualEvidenceStatusBoard","schema_version":"v1","manual_evidence_status_board_id":sid("kfm:air_quality:airnow:manual_evidence_status_board:v1",[workflow]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"board_status":"EVIDENCE_ACCEPTED_FOR_RERUN" if workflow=="MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN" else "EVIDENCE_NEEDS_MORE_INPUT","columns":[{"column":"SATISFIED_CANDIDATES","task_ids":[x['task_id'] for x in sat if x['satisfaction_status']=='SATISFIED_CANDIDATE']},{"column":"PARTIALLY_SATISFIED","task_ids":[]},{"column":"NEEDS_MORE_INPUT","task_ids":[x['task_id'] for x in sat if x['satisfaction_status']!='SATISFIED_CANDIDATE']},{"column":"REJECTED_EVIDENCE","task_ids":[]},{"column":"POLICY_DENIED","task_ids":[]}],"public_release_allowed":False,"created_at":created_at}
    report="# AirNow Layer 9 Manual Evidence Verification Report\n\n"+"\n".join([f"- {d}" for d in REQ_DISCLAIMERS])+"\n"
    status_md="# AirNow Layer 9 Manual Evidence Status Board\n\nInternal-only notice\n\nWorkflow outcome: %s\n"%workflow
    for n,o in [("manual_evidence_manifest.resolved.json",resolved),("manual_evidence_inventory.json",inv_obj),("evidence_assessment_matrix.json",assess_obj),("task_satisfaction_matrix.json",sat_obj),("verification_validation_results.json",vres),("rerun_recommendation_plan.json",rerun),("manual_evidence_status_board.json",sb)]: wj(n,o)
    for n,rows in [("manual_evidence_inventory.jsonl",inv),("evidence_assessment_matrix.jsonl",assess),("task_satisfaction_matrix.jsonl",sat),("closure_candidates.jsonl",closure),("residual_remediation_queue.jsonl",residual),("verification_validation_results.jsonl",[])]: wjl(n,rows)
    (out/"manual_evidence_status_board.md").write_text(status_md)
    (out/"manual_evidence_verification_report.md").write_text(report)
    packet=None
    if m.get("verification_policy",{}).get("include_packet",True):
        packet=out/"manual_evidence_verification_packet.tar.gz"; members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!="manual_evidence_verification_packet.tar.gz"])
        with tarfile.open(packet,"w:gz") as tf:
            for nm in members:
                data=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(data); ti.mtime=0; tf.addfile(ti,io.BytesIO(data))
    receipt={"object_type":"AirNowManualEvidenceReceipt","schema_version":"v1","receipt_id":sid("kfm:air_quality:airnow:manual_evidence_receipt:v1",[m.get("manifest_id"),workflow,created_at]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","workflow_runner":"airnow_layer9_manual_evidence","workflow_runner_version":"v1","workflow_outcome":workflow,"validation_outcome":val,"finite_outcome":finite,"input_counts":{"layer8_inputs":len(l8),"layer8_tasks":len(tasks),"layer8_evidence_requests":len(requests),"manual_evidence_records":len(inv),"required_manual_evidence_records":sum(x['required'] for x in inv)},"output_counts":{"inventory_records":len(inv),"evidence_assessments":len(assess),"task_satisfaction_records":len(sat),"closure_candidates":len(closure),"residual_tasks":len(residual),"validation_results":0,"generated_json":7,"generated_jsonl":6,"generated_markdown":2,"archives":1 if packet else 0},"warnings":warnings,"errors":sorted(set(errors)),"created_at":created_at}
    wj("manual_evidence_receipt.json",receipt)
    return receipt
