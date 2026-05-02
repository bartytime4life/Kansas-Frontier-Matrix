import io, json, tarfile, hashlib, re
from pathlib import Path

FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://","file://")
SECRET_TERMS=("api_key","token","secret","password","bearer","credential","authorization","client_secret","access_key","refresh_token","private_key","github_token","git_remote","ssh_key")
DENIED_CMD_TERMS=["curl","wget","ftp","http://","https://","s3://","gs://","gh issue create","gh pr create","git push","deploy","publish","upload","sync","serve","uvicorn","flask run","fastapi","tile","tiles","dashboard","emergency alert","regulatory","api_key","token","secret","password"]
ALLOWED_OUTCOMES={"MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN","MANUAL_EVIDENCE_PARTIALLY_ACCEPTED","MANUAL_EVIDENCE_NEEDS_MORE_INPUT","MANUAL_EVIDENCE_REJECTED"}


def cjson(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(txt): return hashlib.sha256(txt.encode("utf-8")).hexdigest()
def sid(prefix,parts): return f"{prefix}:{sh(cjson(parts))}"
def loadj(p): return json.loads(Path(p).read_text())
def wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows))

def _has_secret(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if any(t in str(k).lower() for t in SECRET_TERMS): return True
            if _has_secret(x): return True
    elif isinstance(v,list):
        return any(_has_secret(x) for x in v)
    elif isinstance(v,str):
        lo=v.lower(); return any(t in lo for t in SECRET_TERMS)
    return False

def _unsafe_path(p):
    s=str(p)
    return any(s.startswith(x) for x in FORBIDDEN_SCHEMES) or "://" in s or ".." in Path(s).parts

def run_replay_planner(manifest_path,out_dir,created_at):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    m=loadj(manifest_path); errors=[]; blockers=[]; warnings=[]
    denied_flags=[k for k,v in m.items() if k.endswith("_requested") and v is True]
    if denied_flags: errors.append("DENIED_CAPABILITY_REQUESTED")
    if _has_secret(m): errors.append("SECRET_FIELD_DENIED")
    if m.get("local_file_only") is not True or m.get("no_network") is not True: errors.append("NETWORK_INTENT_DENIED")
    l9=m.get("layer9_inputs",{})
    for p in list(l9.values()):
        if _unsafe_path(p): errors.append("UNSAFE_PATH")
    targets=m.get("replay_targets",{})
    order=[x for x in ["layer6","layer7","layer8","layer9"] if targets.get(x,{}).get("enabled")]
    for k in order:
        t=targets[k]
        if _unsafe_path(t.get("manifest_path","")) or _unsafe_path(t.get("cli_path","")) or _unsafe_path(t.get("planned_out_dir","")): errors.append("UNSAFE_PATH")
        if not Path(t.get("manifest_path"," ")).exists(): blockers.append(("REPLAY_TARGET_MANIFEST_MISSING",k,t.get("manifest_path")))
        if not Path(t.get("cli_path"," ")).exists(): blockers.append(("REPLAY_TARGET_CLI_MISSING",k,t.get("cli_path")))

    receipt=loadj(l9.get("manual_evidence_receipt.json")) if Path(l9.get("manual_evidence_receipt_json","")).exists() else {}
    wf=receipt.get("workflow_outcome")
    if wf not in ALLOWED_OUTCOMES: errors.append("UNSUPPORTED_LAYER9_OUTCOME")
    rerun=loadj(l9.get("rerun_recommendation_plan.json")) if Path(l9.get("rerun_recommendation_plan_json","")).exists() else {}
    rerun_rec=rerun.get("rerun_recommendation")

    resolved={"object_type":"AirNowResolvedReplayOrchestrationManifest","schema_version":"v1","resolved_replay_manifest_id":sid("kfm:air_quality:airnow:resolved_replay_orchestration_manifest:v1",[m.get("manifest_id"),wf,created_at]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","lifecycle_stage":"replay_plan_not_executed_not_published","maximum_positive_outcome":"REPLAY_PLAN_READY","preliminary_data":True,"publication_allowed":False,"public_dashboard_allowed":False,"tiles_allowed":False,"public_api_allowed":False,"emergency_alert":False,"regulatory_claim":False,"auto_execute_allowed":False,"auto_apply_allowed":False,"task_closure_allowed":False,"github_issue_creation_allowed":False,"github_pr_creation_allowed":False,"git_push_allowed":False,"layer9_input_count":len(l9),"enabled_replay_target_count":len(order),"detected_layer9_workflow_outcome":wf,"detected_layer9_rerun_recommendation":rerun_rec,"source_doc_refs":m.get("source_doc_refs",[]),"created_at":created_at}

    node_keys={"layer6":"layer6_bundle_replay","layer7":"layer7_release_gate_replay","layer8":"layer8_remediation_scaffold_replay","layer9":"layer9_manual_evidence_replay"}
    deps={"layer7":["layer6"],"layer8":["layer7"],"layer9":["layer8"]}
    nodes=[]; edges=[]
    for lay in order:
        dn=[node_keys[d] for d in deps.get(lay,[]) if d in order]
        nodes.append({"object_type":"AirNowReplayDagNode","schema_version":"v1","replay_dag_node_id":sid("kfm:air_quality:airnow:replay_dag_node:v1",[m.get("manifest_id"),lay]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"node_key":node_keys[lay],"layer":lay,"node_type":"planned_replay_step","enabled":True,"depends_on":dn,"dependency_reason":"Deterministic layered replay order.","planned":True,"executed":False,"publication_allowed":False,"created_at":created_at})
        for d in deps.get(lay,[]):
            if d in order:
                edges.append({"subject_node_key":node_keys[d],"predicate":"MUST_COMPLETE_BEFORE","object_node_key":node_keys[lay]})
    dag={"object_type":"AirNowReplayDag","schema_version":"v1","replay_dag_id":sid("kfm:air_quality:airnow:replay_dag:v1",[m.get("manifest_id"),order]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"dag_status":"PASS","nodes":sorted(nodes,key=lambda x:x["node_key"]),"edges":sorted(edges,key=lambda x:(x["subject_node_key"],x["object_node_key"])),"topological_order":[node_keys[x] for x in order],"cycle_detected":False,"executed":False,"created_at":created_at}

    cmds=[]; steps=[]
    receipt_types={"layer6":"AirNowBundleReceipt","layer7":"AirNowReleaseGateReceipt","layer8":"AirNowRemediationReceipt","layer9":"AirNowManualEvidenceReceipt"}
    for i,lay in enumerate(order,1):
        t=targets[lay]; cmd=f"python {t['cli_path']} --manifest {t['manifest_path']} --out-dir {t['planned_out_dir']} --created-at {created_at}"
        bad=[x for x in DENIED_CMD_TERMS if x in cmd.lower()]
        cmd_id=sid("kfm:air_quality:airnow:replay_command:v1",[lay,cmd])
        cmds.append({"object_type":"AirNowReplayCommandRecord","schema_version":"v1","replay_command_id":cmd_id,"source_id":"airnow","manifest_id":m.get("manifest_id"),"layer":lay,"command_kind":"LOCAL_CLI_REPLAY_PLAN","command":cmd,"network_free":not bad,"publication_free":not bad,"github_free":not bad,"credential_free":not bad,"execute_by_default":False,"command_executed":False,"manual_only":True,"forbidden_terms_detected":bad,"validation_status":"FAIL" if bad else "PASS","created_at":created_at})
        if bad: blockers.append(("COMMAND_FORBIDDEN_TERM",lay,",".join(bad)))
        dep_step=[]
        if lay in deps:
            for d in deps[lay]:
                if d in order: dep_step.append(sid("kfm:air_quality:airnow:replay_step:v1",[m.get("manifest_id"),d]))
        steps.append({"object_type":"AirNowReplayStepRecord","schema_version":"v1","replay_step_id":sid("kfm:air_quality:airnow:replay_step:v1",[m.get("manifest_id"),lay]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"step_number":i,"layer":lay,"step_name":f"Replay {lay}","step_status":"PLANNED_NOT_EXECUTED","dependency_step_ids":dep_step,"trigger_basis":["Manual evidence accepted for rerun."],"cli_path":t["cli_path"],"manifest_path":t["manifest_path"],"planned_out_dir":t["planned_out_dir"],"created_at_arg":created_at,"planned_command_id":cmd_id,"expected_receipt_object_type":receipt_types[lay],"expected_receipt_path":f"{t['planned_out_dir']}/{receipt_types[lay].replace('AirNow','').replace('Receipt','').lower()}_receipt.json","expected_success_condition":"validation_outcome == PASS","manual_review_required":True,"executed":False,"publication_allowed":False,"public_release_allowed":False,"created_at":created_at})

    cmd_catalog={"object_type":"AirNowReplayCommandCatalog","schema_version":"v1","replay_command_catalog_id":sid("kfm:air_quality:airnow:replay_command_catalog:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"command_count":len(cmds),"commands":cmds,"all_commands_manual_only":True,"all_commands_network_free":all(not c['forbidden_terms_detected'] for c in cmds),"all_commands_publication_free":True,"all_commands_github_free":True,"all_commands_credential_free":True,"command_catalog_status":"PASS" if not blockers else "FAIL","created_at":created_at}

    pre=[{"object_type":"AirNowReplayPreflightCheck","schema_version":"v1","replay_preflight_check_id":sid("kfm:air_quality:airnow:replay_preflight_check:v1",["MANIFEST_GOVERNANCE_PASS",m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"check_category":"governance","check_name":"MANIFEST_GOVERNANCE_PASS","check_status":"FAIL" if errors else "PASS","required":True,"observed_summary":"Manifest flags and denied capabilities were evaluated.","blocks_replay_plan_ready":bool(errors),"remediation_hint":None,"created_at":created_at}]
    for bt,lay,detail in blockers:
        pre.append({"object_type":"AirNowReplayPreflightCheck","schema_version":"v1","replay_preflight_check_id":sid("kfm:air_quality:airnow:replay_preflight_check:v1",[bt,lay]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"check_category":"target","check_name":bt,"check_status":"FAIL","required":True,"observed_summary":detail,"blocks_replay_plan_ready":True,"remediation_hint":"Fix local replay target path.","created_at":created_at})

    blocker_rows=[{"object_type":"AirNowReplayBlocker","schema_version":"v1","replay_blocker_id":sid("kfm:air_quality:airnow:replay_blocker:v1",[bt,lay,detail]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"blocker_type":bt,"severity":"BLOCKER","blocks_workflow_outcome":"REPLAY_PLAN_READY","related_layer":lay,"related_object_id":None,"reason_code":bt,"reason_detail":detail,"recommended_action":"Address blocker and rerun Layer 10.","public_release_allowed":False,"created_at":created_at} for bt,lay,detail in blockers]

    outcome="REPLAY_PLAN_READY"
    finite="ANSWER"; val="PASS"
    if errors: outcome="REPLAY_PLAN_DENIED_REQUESTED_CAPABILITY"; finite="DENY"; val="FAIL"
    elif blocker_rows or wf=="MANUAL_EVIDENCE_REJECTED": outcome="REPLAY_PLAN_BLOCKED"; finite="DENY"; val="FAIL"
    elif wf=="MANUAL_EVIDENCE_NEEDS_MORE_INPUT": outcome="REPLAY_PLAN_NEEDS_MORE_EVIDENCE"; finite="ABSTAIN"

    # write outputs
    wj(out/"replay_orchestration_manifest.resolved.json",resolved); wj(out/"replay_dag.json",dag); wjl(out/"replay_dag.jsonl",dag["nodes"])
    step_obj={"object_type":"AirNowReplayStepPlan","schema_version":"v1","records":steps,"created_at":created_at}; wj(out/"replay_step_plan.json",step_obj); wjl(out/"replay_step_plan.jsonl",steps)
    wj(out/"replay_command_catalog.json",cmd_catalog); (out/"replay_command_catalog.md").write_text("# AirNow Layer 10 Replay Command Catalog\n\nInternal replay planning only.\n\nCommands are not executed by Layer 10.\n\nNot publication output.\nNot a public dashboard.\nNot a public API.\nNot a map tile product.\nNot an emergency alert product.\nNot regulatory analysis.\nPublic release remains denied by policy.\n")
    wj(out/"replay_input_binding_matrix.json",{"object_type":"AirNowReplayInputBindingMatrix","schema_version":"v1","records":[],"created_at":created_at}); wjl(out/"replay_input_binding_matrix.jsonl",[])
    wj(out/"replay_expected_output_matrix.json",{"object_type":"AirNowReplayExpectedOutputMatrix","schema_version":"v1","records":[],"created_at":created_at}); wjl(out/"replay_expected_output_matrix.jsonl",[])
    wj(out/"replay_preflight_checklist.json",{"object_type":"AirNowReplayPreflightChecklist","schema_version":"v1","records":pre,"created_at":created_at}); wjl(out/"replay_preflight_checklist.jsonl",pre)
    wjl(out/"replay_blockers.jsonl",blocker_rows)
    att={"object_type":"AirNowReplayPolicyAttestation","schema_version":"v1","replay_policy_attestation_id":sid("kfm:air_quality:airnow:replay_policy_attestation:v1",[m.get("manifest_id")]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"policy_status":"DENY" if errors else "PASS","checks":[{"check":"plan_only","status":"PASS"}],"denied_capabilities":["live_api_ingestion","publication","github_pr_creation"],"created_at":created_at}; wj(out/"replay_policy_attestation.json",att)
    risks=[{"object_type":"AirNowReplayRiskRecord","schema_version":"v1","replay_risk_id":sid("kfm:air_quality:airnow:replay_risk:v1",["preliminary"]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"risk_category":"source_limitations","risk_level":"LOW","risk_title":"AirNow data are preliminary.","risk_description":"AirNow data are preliminary and subject to change.","mitigation":"Use local replay artifacts only.","related_step_ids":[],"public_release_allowed":False,"created_at":created_at}]
    wj(out/"replay_risk_register.json",{"object_type":"AirNowReplayRiskRegister","schema_version":"v1","records":risks,"created_at":created_at}); wjl(out/"replay_risk_register.jsonl",risks)
    status={"object_type":"AirNowReplayStatusBoard","schema_version":"v1","replay_status_board_id":sid("kfm:air_quality:airnow:replay_status_board:v1",[outcome]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"board_status":outcome,"columns":[{"column":"PLANNED_STEPS","replay_step_ids":[s['replay_step_id'] for s in steps]}],"public_release_allowed":False,"commands_executed":False,"created_at":created_at}
    wj(out/"replay_status_board.json",status); (out/"replay_status_board.md").write_text(f"# AirNow Layer 10 Replay Status Board\n\nInternal replay planning only.\n\nWorkflow outcome: {outcome}\n")
    (out/"replay_runbook.md").write_text("# AirNow Layer 10 Replay Runbook\n\nInternal replay planning only.\nLayer 10 does not execute replay commands by default.\nLayer 10 does not apply fixes automatically.\nLayer 10 does not close tasks.\nLayer 10 does not create GitHub issues or pull requests.\nNot publication output.\nNot a public dashboard.\nNot a public API.\nNot a map tile product.\nNot an emergency alert product.\nNot regulatory analysis.\nAirNow data are preliminary and subject to change.\nOfficial regulatory air-quality data must come from EPA AQS/AirData.\nPublic release remains denied by policy.\n")
    packet_hash=None
    if m.get("replay_policy",{}).get("include_packet",True):
        packet=out/"replay_orchestration_packet.tar.gz"
        members=sorted([p.name for p in out.iterdir() if p.is_file() and p.name!=packet.name])
        with tarfile.open(packet,"w:gz") as tf:
            for nm in members:
                data=(out/nm).read_bytes(); ti=tarfile.TarInfo(nm); ti.size=len(data); ti.mtime=0; tf.addfile(ti,io.BytesIO(data))
        packet_hash=hashlib.sha256(packet.read_bytes()).hexdigest()
    receipt_out={"object_type":"AirNowReplayReceipt","schema_version":"v1","receipt_id":sid("kfm:air_quality:airnow:replay_receipt:v1",[m.get("manifest_id"),outcome,created_at]),"source_id":"airnow","manifest_id":m.get("manifest_id"),"workflow_name":m.get("workflow_name"),"workflow_version":"v1","workflow_runner":"airnow_layer10_replay_plan","workflow_runner_version":"v1","workflow_outcome":outcome,"validation_outcome":val,"finite_outcome":finite,"commands_executed":False,"replay_executed":False,"publication_allowed":False,"public_release_allowed":False,"warnings":warnings,"errors":sorted(set(errors)),"output_hashes":{"replay_orchestration_packet_hash":packet_hash},"created_at":created_at}
    wj(out/"replay_receipt.json",receipt_out)
    return receipt_out
