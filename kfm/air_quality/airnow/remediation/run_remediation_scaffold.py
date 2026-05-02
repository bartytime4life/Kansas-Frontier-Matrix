import io, json, tarfile, re
from pathlib import Path
from .ids import stable_id, sha256_text, cjson
from .constants import DENIED_FIELDS, SECRET_KEYS, FORBIDDEN_SCHEMES, OUTCOMES
from .task_builder import build_tasks

def _loadj(p): return json.loads(Path(p).read_text())
def _has_secret(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if any(s in str(k).lower() for s in SECRET_KEYS): return True
            if _has_secret(x): return True
    if isinstance(v,list): return any(_has_secret(i) for i in v)
    return False

def run_remediation_scaffold(manifest_path,out_dir,created_at):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    m=_loadj(manifest_path)
    errors=[]; warnings=[]
    if _has_secret(m): errors.append("secret_field")
    if m.get("local_file_only") is not True or m.get("no_network") is not True or m.get("bulk_web_service_loop") is not False: errors.append("governance_flags")
    for f in DENIED_FIELDS:
        if m.get(f) is True: errors.append(f"denied_requested:{f}")
    if m.get("workflow_policy",{}).get("maximum_positive_outcome")!="REMEDIATION_SCAFFOLD_READY": errors.append("bad_max_outcome")
    l7=m.get("layer7_inputs",{})
    for k,v in l7.items():
        if any(str(v).startswith(s) for s in FORBIDDEN_SCHEMES) or '://' in str(v): errors.append("unsafe_path")
    if errors:
        outcome=OUTCOMES["deny"]; val="FAIL"; finite="DENY"
        decision={"decision_outcome":"DENY_REQUESTED_CAPABILITY","public_release_allowed":False}
        evid=[]; rem=[]
    else:
        decision=_loadj(l7["release_gate_decision_json"]); evid=_loadj(l7["release_gate_evidence_matrix_json"]).get("records",[]); rem=_loadj(l7["remediation_plan_json"]).get("items",[])
        tasks=build_tasks(m,rem,evid,created_at)
        if any(t["task_priority"] in ("P0","P1") for t in tasks): outcome=OUTCOMES["needs"]
        elif any(t["task_priority"]=="P2" for t in tasks): outcome=OUTCOMES["warn"]
        else: outcome=OUTCOMES["ready"]
        val="PASS"; finite="ANSWER"
    tasks=build_tasks(m,rem,evid,created_at) if not errors else []
    # write outputs
    resolved={"object_type":"AirNowResolvedRemediationWorkflowManifest","schema_version":"v1","resolved_remediation_manifest_id":stable_id("kfm:air_quality:airnow:resolved_remediation_workflow_manifest:v1",[m.get("manifest_id"),decision.get("decision_outcome")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","lifecycle_stage":"remediation_scaffold_not_applied_not_published","maximum_positive_outcome":"REMEDIATION_SCAFFOLD_READY","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"auto_apply_allowed":False,"github_issue_creation_allowed":False,"github_pr_creation_allowed":False,"git_push_allowed":False,"layer7_input_count":len(l7),"required_disclaimer_count":len(m.get("required_disclaimers",[])),"detected_layer7_decision_outcome":decision.get("decision_outcome","UNKNOWN"),"detected_layer7_public_release_allowed":False,"source_doc_refs":m.get("source_doc_refs",[]),"created_at":created_at}
    (out/"remediation_workflow_manifest.resolved.json").write_text(json.dumps(resolved,indent=2,sort_keys=True)+"\n")
    (out/"remediation_task_queue.jsonl").write_text("".join(cjson(t)+"\n" for t in tasks))
    issue_dir=out/"remediation_issue_templates"; issue_dir.mkdir(exist_ok=True)
    issue_records=[]
    for t in tasks:
        short=t['task_id'].split(':')[-1][:8]; fn=f"{t['task_priority']}_{t['task_category']}_{t['task_source'].get('source_remediation_code','TASK')}_{short}.md".replace('/','_')
        text=f"# {t['title']}\n\nInternal remediation template only.\nThis file does not create a GitHub issue.\nNot publication output.\nNot an emergency alert product.\nNot regulatory analysis.\nAirNow data are preliminary and subject to change.\nOfficial regulatory air-quality data must come from EPA AQS/AirData.\nPublic release remains denied by policy.\n"
        (issue_dir/fn).write_text(text)
        issue_records.append({"object_type":"AirNowRemediationIssueTemplate","schema_version":"v1","issue_template_id":stable_id("kfm:air_quality:airnow:issue_template:v1",[t['task_id']]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"task_id":t['task_id'],"template_path":f"remediation_issue_templates/{fn}","title":f"[AirNow Layer 8] {t['title']}","labels":["airnow","internal-review","remediation",t['task_category'],"no-publication"],"assignee":None,"github_issue_created":False,"publication_allowed":False,"created_at":created_at})
    issue_records=sorted(issue_records,key=lambda x:x['issue_template_id'])
    (out/"remediation_issue_templates.jsonl").write_text("".join(cjson(r)+"\n" for r in issue_records))
    plan={"object_type":"AirNowRemediationWorkflowPlan","schema_version":"v1","workflow_plan_id":stable_id("kfm:air_quality:airnow:remediation_workflow_plan:v1",[m.get("manifest_id"),outcome]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","lifecycle_stage":"remediation_scaffold_not_applied_not_published","workflow_outcome":outcome,"preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"auto_apply_allowed":False,"github_issue_creation_allowed":False,"input_summary":{"layer7_decision_outcome":decision.get("decision_outcome"),"layer7_validation_outcome":"PASS","layer7_finite_outcome":"ANSWER","layer7_public_release_allowed":False,"layer7_internal_review_allowed":decision.get("decision_outcome")=="ALLOW_INTERNAL_REVIEW_ONLY"},"task_counts":{"total":len(tasks),"P0":sum(t['task_priority']=='P0' for t in tasks),"P1":sum(t['task_priority']=='P1' for t in tasks),"P2":sum(t['task_priority']=='P2' for t in tasks),"P3":sum(t['task_priority']=='P3' for t in tasks),"P4":sum(t['task_priority']=='P4' for t in tasks)},"task_counts_by_category":{},"patch_plan_counts_by_kind":{},"evidence_request_counts_by_type":{},"next_manual_steps":["Review local issue-template drafts."],"blocked_capabilities":["publication","public_dashboard","tiles","public_api","emergency_alerts","regulatory_claims"],"source_doc_refs":m.get("source_doc_refs",[]),"created_at":created_at}
    (out/"remediation_workflow_plan.json").write_text(json.dumps(plan,indent=2,sort_keys=True)+"\n")
    # minimal placeholder artifacts
    for f,obj in [("remediation_patch_plan.json",{"records":[]}), ("remediation_validation_matrix.json",{"records":[]}), ("remediation_status_board.json",{"columns":[]})]: (out/f).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    for f in ["remediation_patch_plan.jsonl","remediation_validation_matrix.jsonl","remediation_evidence_requests.jsonl"]: (out/f).write_text("")
    (out/"remediation_status_board.md").write_text("# AirNow Layer 8 Remediation Status Board\n\nInternal remediation scaffolding only.\n")
    (out/"remediation_runbook.md").write_text("# AirNow Layer 8 Remediation Runbook\n\nInternal remediation scaffolding only.\nLayer 8 does not apply fixes automatically.\nLayer 8 does not create GitHub issues or pull requests.\nNot publication output.\nNot a public dashboard.\nNot a public API.\nNot a map tile product.\nNot an emergency alert product.\nNot regulatory analysis.\nAirNow data are preliminary and subject to change.\nOfficial regulatory air-quality data must come from EPA AQS/AirData.\nPublic release remains denied by policy.\n")
    packet_hash=None
    if m.get("workflow_policy",{}).get("include_packet",True):
        pkt=out/"remediation_packet.tar.gz"
        members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!="remediation_packet.tar.gz"]+[f"remediation_issue_templates/{p.name}" for p in sorted(issue_dir.glob("*.md"))])
        with tarfile.open(pkt,"w:gz") as tf:
            for nm in members:
                p=out/nm
                if not p.exists(): p=out/nm.split('/',1)[0]/nm.split('/',1)[1]
                data=p.read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(data); ti.mtime=0; tf.addfile(ti,io.BytesIO(data))
        packet_hash=sha256_text(pkt.read_bytes().hex())
    receipt={"object_type":"AirNowRemediationReceipt","schema_version":"v1","receipt_id":stable_id("kfm:air_quality:airnow:remediation_receipt:v1",[m.get("manifest_id"),created_at,outcome]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","workflow_runner":"airnow_layer8_remediation_scaffold","workflow_runner_version":"v1","workflow_outcome":outcome,"validation_outcome":val,"finite_outcome":finite,"input_counts":{"layer7_inputs":len(l7),"layer7_evidence_records":len(evid),"layer7_remediation_items":len(rem),"required_disclaimers":len(m.get('required_disclaimers',[]))},"output_counts":{"tasks":len(tasks),"issue_templates":len(issue_records),"patch_plan_records":0,"validation_records":0,"evidence_requests":0,"generated_json":5,"generated_jsonl":5,"generated_markdown":2,"archives":1 if packet_hash else 0},"input_hashes":{"manifest_hash":sha256_text(Path(manifest_path).read_text())},"output_hashes":{"remediation_packet_hash":packet_hash},"outputs":{"remediation_workflow_manifest_resolved_json":"remediation_workflow_manifest.resolved.json"},"warnings":warnings,"errors":errors,"created_at":created_at}
    (out/"remediation_receipt.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    return receipt
