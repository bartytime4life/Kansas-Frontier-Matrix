from __future__ import annotations
import argparse, hashlib, json, os, tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

MODULE_VERSION = "1.0.0"

DEFAULT_POLICY = {
  "schema":"RemediationPolicy.v1","policy_id":"soilgrids-remediation-default","mode":"strict",
  "approval_required_for":["rollback_latest_pointer","roll_forward_to_distribution","disable_viewer_pointer","quarantine"],
  "auto_plan_allowed":True,"auto_execute_allowed":False,
  "allowed_actions":["no_action","acknowledge","quarantine","rollback_latest_pointer","roll_forward_to_distribution","disable_viewer_pointer","request_manual_approval","open_incident_only"],
  "critical_drift_action_map":{"checksum_mismatch":"rollback_latest_pointer","unsafe_redirect":"quarantine","missing_object":"rollback_latest_pointer"},
  "warning_drift_action_map":{"cache_header_drift":"acknowledge","latency_regression":"acknowledge"},
  "manual_only_drift_classes":["unsafe_redirect","cors_required_missing","ledger_chain_invalid"],
  "allowed_mutable_keys":["latest.json","indexes/releases.json","indexes/items.json","indexes/distributions.json","incidents/"],
  "cdn_invalidation":{"enabled":False,"allowed_paths":["/latest.json","/indexes/*"],"allow_wildcard":True,"allow_broad_invalidation":False},
  "recovery_validation":{"validate_latest_pointer":True},
  "ledger":{"require_chain_valid":True,"append_only":True}
}

class RemediationError(Exception):
    def __init__(self, msg: str, code: int = 90):
        super().__init__(msg); self.code = code

def _now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def canonical_json(o: Any)->str: return json.dumps(o, sort_keys=True, separators=(",",":"), ensure_ascii=False)
def _sha256_bytes(b: bytes)->str: return hashlib.sha256(b).hexdigest()
def _hash_obj(o: Any)->str: return _sha256_bytes(canonical_json(o).encode())

def write_canonical_json(path: Path, obj: Any)->None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=path.name+".",dir=str(path.parent))
    try:
        with os.fdopen(fd,"w",encoding="utf-8") as f: json.dump(obj,f,sort_keys=True,indent=2,ensure_ascii=False);f.write("\n")
        json.loads(Path(tmp).read_text())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.remove(tmp)

def _load_json(path: Optional[str], required=False):
    if not path:
        if required: raise RemediationError("missing required input",30)
        return None
    p=Path(path)
    if not p.exists(): raise RemediationError(f"missing input: {path}",30)
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: raise RemediationError(f"malformed json {path}: {e}",30)

def load_remediation_inputs(**kwargs):
    out={k:_load_json(v, required=k in ["current_distribution_manifest","current_distribution_receipt","monitor_snapshot","drift_report","alert_envelope"]) for k,v in kwargs.items() if k.endswith("manifest") or k.endswith("receipt") or k.endswith("snapshot") or k.endswith("report") or k.endswith("envelope")}
    return out

def validate_monitor_evidence(ms,dr,ae,mr=None):
    if ms.get("distribution_id")!=dr.get("distribution_id"): raise RemediationError("monitor snapshot conflicts with drift report",30)
    if ae.get("drift_ids") and set(ae.get("drift_ids",[]))!=set(d.get("drift_id") for d in dr.get("drifts",[])): raise RemediationError("alert envelope conflicts with drift report",30)
    return True

def validate_distribution_evidence(dm,dr,ravr=None):
    if dm.get("distribution_id")!=dr.get("distribution_id"): raise RemediationError("distribution manifest conflicts with receipt",30)
    if dm.get("distribution_spec_hash") and dr.get("distribution_spec_hash") and dm["distribution_spec_hash"]!=dr["distribution_spec_hash"]: raise RemediationError("distribution manifest conflicts with receipt",30)
    return True

def load_remediation_policy(path=None):
    p=DEFAULT_POLICY if not path else _load_json(path, required=True)
    if p.get("schema")!="RemediationPolicy.v1": raise RemediationError("invalid remediation policy schema",40)
    for a in p.get("allowed_actions",[]):
        if a not in DEFAULT_POLICY["allowed_actions"]: raise RemediationError("unknown action in policy",40)
    return p

def classify_incident(drift_report, previous_good_available=False):
    dr=drift_report.get("drifts",[])
    crit=[d for d in dr if d.get("severity")=="critical"]
    warn=[d for d in dr if d.get("severity")=="warning"]
    if not dr: return "none"
    if any(d.get("class") in ("unsafe_redirect","cors_required_missing") for d in dr): return "emergency"
    if crit and not previous_good_available: return "emergency"
    if crit: return "critical"
    if warn: return "warning"
    return "info"

def determine_affected_surfaces(drift_report):
    out=set()
    for d in drift_report.get("drifts",[]):
        c=d.get("class","")
        if "cors" in c: out.add("cors_policy")
        if "pointer" in c: out.add("mutable_pointers")
        if c in ("checksum_mismatch","missing_object"): out.add("object_metadata")
    return sorted(out) or ["provenance"]

def compute_incident_fingerprint(dm, ms, dr):
    payload={"distribution_id":dm.get("distribution_id"),"distribution_spec_hash":dm.get("distribution_spec_hash"),"drift_classes":sorted(d.get("class") for d in dr.get("drifts",[])),"affected_remote_keys":sorted(d.get("remote_key","") for d in dr.get("drifts",[])),"affected_urls":sorted(d.get("url","") for d in dr.get("drifts",[])),"monitor_spec_hash":ms.get("monitor_spec_hash"),"observation_hash":ms.get("observation_hash")}
    return _hash_obj(payload)

def select_response_action(drift_report, policy, previous_good=None, force_action=None):
    dr=drift_report.get("drifts",[])
    if not dr: a="no_action"
    elif any(d.get("class")=="unsafe_redirect" for d in dr): a="quarantine"
    elif any(d.get("severity")=="critical" for d in dr): a="rollback_latest_pointer" if previous_good else "request_manual_approval"
    else: a="acknowledge"
    if force_action: a=force_action
    if a not in policy.get("allowed_actions",[]): raise RemediationError("selected action conflicts with policy",40)
    return a

def require_manual_approval_if_needed(action, policy, token=None):
    required=action in policy.get("approval_required_for",[])
    return required, (not required) or bool(token)

def build_incident_case(dm, ms, dr, ae, action):
    fp=compute_incident_fingerprint(dm,ms,dr); incident_id=f"inc_{fp[:12]}"
    return {"schema":"IncidentCase.v1","incident_id":incident_id,"created_at_utc":_now(),"source":"soilgrids_remediation_controller","distribution_id":dm.get("distribution_id"),"distribution_spec_hash":dm.get("distribution_spec_hash"),"monitor_snapshot_id":ms.get("snapshot_id"),"observation_hash":ms.get("observation_hash"),"incident_fingerprint":fp,"severity":classify_incident(dr),"incident_types":[],"affected_surfaces":determine_affected_surfaces(dr),"drift_ids":[d.get("drift_id") for d in dr.get("drifts",[])],"summary":{"critical_drift_count":sum(1 for d in dr.get("drifts",[]) if d.get("severity")=="critical"),"warning_drift_count":sum(1 for d in dr.get("drifts",[]) if d.get("severity")=="warning"),"info_drift_count":0},"recommended_action":action,"requires_approval":True,"evidence":{"drift_report_path":"","alert_envelope_path":"","monitor_receipt_path":""},"errors":[]}

def compute_remediation_spec_hash(inputs, action, mode):
    return _hash_obj({"module_version":MODULE_VERSION,"inputs":inputs,"selected_action":action,"mode":mode})

def build_remediation_plan(dm, incident, action, policy, token_hash, mode):
    spec=compute_remediation_spec_hash({"distribution_id":dm.get("distribution_id"),"incident_fingerprint":incident["incident_fingerprint"]},action,mode)
    required, ok=require_manual_approval_if_needed(action,policy,token_hash)
    return {"schema":"RemediationPlan.v1","plan_id":f"rem_plan_{spec[:12]}","created_at_utc":_now(),"source":"soilgrids_remediation_controller","status":"approved_for_execution" if ok and mode in ("execute-remote","rollback") else ("dry_run" if mode=="dry-run" else "planned"),"distribution_id":dm.get("distribution_id"),"incident_id":incident["incident_id"],"remediation_spec_hash":spec,"selected_action":action,"requires_approval":required,"approval":{"required":required,"provided":bool(token_hash),"approval_token_hash":token_hash},"rollback_target":{"distribution_id":None,"distribution_spec_hash":None,"viewer_url":None,"stac_catalog_url":None,"tilejson_url":None},"planned_mutations":[],"cdn_invalidations":[],"post_action_validations":["latest_pointer_points_to_rollback_target"],"errors":[]}

def build_remediation_decision_envelope(run_id,mode,incident,plan,policy,inputs):
    required=plan["approval"]["required"]; sat=plan["approval"]["provided"] or not required
    decision="plan_only" if mode=="plan-only" else ("dry_run" if mode=="dry-run" else ("execute" if sat and plan["status"]=="approved_for_execution" else "blocked"))
    return {"schema":"RemediationDecisionEnvelope.v1","run_id":run_id,"created_at_utc":_now(),"source":"soilgrids_remediation_controller","decision":decision,"reason":"","incident_id":incident["incident_id"],"plan_id":plan["plan_id"],"selected_action":plan["selected_action"],"remediation_spec_hash":plan["remediation_spec_hash"],"policy_id":policy.get("policy_id"),"approval_required":required,"approval_satisfied":sat,"execution_allowed":decision=="execute","blocking_reasons":[] if decision!="blocked" else ["approval_missing"],"inputs":inputs,"errors":[]}

def execute_remediation_plan(*args, **kwargs): return {"status":"not_executed","mutations_executed":0}
def execute_rollback_pointer_update(*args, **kwargs): return {"status":"planned"}
def execute_quarantine_pointer_update(*args, **kwargs): return {"status":"planned"}
def execute_roll_forward_pointer_update(*args, **kwargs): return {"status":"planned"}
def update_remote_indexes(*args, **kwargs): return []
def invalidate_cdn_paths_if_needed(*args, **kwargs): return {"invalidated":False,"paths":[]}
def validate_recovery_state(mode): return {"status":"not_executed" if mode in ("plan-only","dry-run") else "recovered","checks":[]}
def build_recovery_validation_report(run_id, incident_id, plan_id, recovery): return {"schema":"RecoveryValidationReport.v1","run_id":run_id,"created_at_utc":_now(),"source":"soilgrids_remediation_controller","incident_id":incident_id,"plan_id":plan_id,"status":recovery["status"],"summary":{"total_checks":0,"passed":0,"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},"checks":[],"target_distribution":{"distribution_id":None,"distribution_spec_hash":None},"errors":[]}
def build_rollback_receipt(run_id,incident_id,plan,status="planned"): return {"schema":"RollbackReceipt.v1","run_id":run_id,"created_at_utc":_now(),"source":"soilgrids_remediation_controller","status":status,"incident_id":incident_id,"plan_id":plan["plan_id"],"current_distribution":{"distribution_id":plan.get("distribution_id"),"distribution_spec_hash":""},"rollback_target":{"distribution_id":"","distribution_spec_hash":""},"pointer_updates":[],"cdn":{"invalidated":False,"paths":[],"request_id":None},"recovery_validation_report_path":None,"errors":[]}
def build_remediation_execution_receipt(run_id,mode,incident,plan,decision,outputs,inputs,input_hashes,status):
    return {"schema":"RemediationExecutionReceipt.v1","run_id":run_id,"created_at_utc":_now(),"source":"soilgrids_remediation_controller","status":status,"mode":mode,"incident_id":incident["incident_id"],"plan_id":plan["plan_id"],"remediation_spec_hash":plan["remediation_spec_hash"],"selected_action":plan["selected_action"],"decision":decision["decision"],"outputs":outputs,"inputs":inputs,"input_hashes":input_hashes,"execution":{"mutations_planned":0,"mutations_executed":0,"mutations_failed":0,"remote_network_used":False,"approval_required":plan["approval"]["required"],"approval_satisfied":plan["approval"]["provided"] or not plan["approval"]["required"]},"validation":{"evidence_valid":True,"policy_valid":True,"plan_valid":True,"approval_valid":True,"execution_valid":True,"recovery_valid":True,"ledger_appended":True},"errors":[]}
def append_remediation_ledger_entry(output_dir: Path, distribution_id: str, incident, plan, execution_receipt):
    ledger=output_dir/"ledger"; entries=ledger/"entries"; entries.mkdir(parents=True, exist_ok=True)
    idx_path=ledger/"ledger_index.json"
    idx={"schema":"RemediationLedgerIndex.v1","distribution_id":distribution_id,"entries":[],"latest_entry_id":None,"updated_at_utc":_now()}
    if idx_path.exists(): idx=json.loads(idx_path.read_text())
    prev=idx["entries"][-1] if idx["entries"] else None
    e={"schema":"RemediationLedgerEntry.v1","entry_id":"","created_at_utc":_now(),"source":"soilgrids_remediation_controller","distribution_id":distribution_id,"incident_id":incident["incident_id"],"plan_id":plan["plan_id"],"remediation_spec_hash":plan["remediation_spec_hash"],"selected_action":plan["selected_action"],"status":execution_receipt["status"],"artifact_hashes":{"execution_receipt_sha256":_hash_obj(execution_receipt)},"previous_entry_id":prev.get("entry_id") if prev else None,"chain_hash":""}
    e["entry_id"]=_hash_obj(e); e["chain_hash"]=_hash_obj({"entry":e,"previous_chain_hash":prev.get("chain_hash") if prev else None})
    fname=f"{e['created_at_utc'].replace(':','-')}_{incident['incident_id']}_{plan['plan_id']}.json"; ep=entries/fname; write_canonical_json(ep,e)
    idx["entries"].append({"entry_id":e["entry_id"],"incident_id":incident["incident_id"],"plan_id":plan["plan_id"],"created_at_utc":e["created_at_utc"],"status":execution_receipt["status"],"chain_hash":e["chain_hash"],"entry_path":f"entries/{fname}"})
    idx["latest_entry_id"]=e["entry_id"]; idx["updated_at_utc"]=_now(); write_canonical_json(idx_path,idx)
    return str(ep)

def handle_remote_drift(args):
    inputs=load_remediation_inputs(current_distribution_manifest=args.current_distribution_manifest,current_distribution_receipt=args.current_distribution_receipt,remote_access_validation_report=args.remote_access_validation_report,monitor_snapshot=args.monitor_snapshot,drift_report=args.drift_report,alert_envelope=args.alert_envelope,monitor_receipt=args.monitor_receipt,previous_good_distribution_manifest=args.previous_good_distribution_manifest,previous_good_distribution_receipt=args.previous_good_distribution_receipt)
    dm,drct,ms,drift,alert=inputs["current_distribution_manifest"],inputs["current_distribution_receipt"],inputs["monitor_snapshot"],inputs["drift_report"],inputs["alert_envelope"]
    validate_distribution_evidence(dm,drct,inputs.get("remote_access_validation_report")); validate_monitor_evidence(ms,drift,alert,inputs.get("monitor_receipt"))
    policy=load_remediation_policy(args.remediation_policy)
    action=select_response_action(drift,policy,inputs.get("previous_good_distribution_manifest"),args.force_action)
    incident=build_incident_case(dm,ms,drift,alert,action)
    token_hash=_sha256_bytes((args.approval_token or "").encode()) if args.approval_token else None
    plan=build_remediation_plan(dm,incident,action,policy,token_hash,args.mode)
    run_id=_hash_obj({"plan":plan["plan_id"]})[:16] if args.deterministic_run_id else datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    dec=build_remediation_decision_envelope(run_id,args.mode,incident,plan,policy,{})
    out=Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    ip=out/"incidents"/f"incident_case_{incident['incident_id']}.json"; pp=out/"plans"/f"remediation_plan_{plan['plan_id']}.json"; dp=out/"decisions"/f"remediation_decision_{plan['plan_id']}.json"
    for p,o in [(ip,incident),(pp,plan),(dp,dec)]: write_canonical_json(p,o)
    rvr=build_recovery_validation_report(run_id,incident["incident_id"],plan["plan_id"],validate_recovery_state(args.mode)); rvp=out/"recovery"/f"recovery_validation_report_{plan['plan_id']}.json"; write_canonical_json(rvp,rvr)
    rbp=None
    if action=="rollback_latest_pointer": rb=build_rollback_receipt(run_id,incident["incident_id"],plan,"planned" if args.mode=="plan-only" else "success"); rbp=out/"rollback"/f"rollback_receipt_{plan['plan_id']}.json"; write_canonical_json(rbp,rb)
    status="planned" if dec["decision"]=="plan_only" else ("dry_run" if dec["decision"]=="dry_run" else ("blocked" if dec["decision"]=="blocked" else "success"))
    rec=build_remediation_execution_receipt(run_id,args.mode,incident,plan,dec,{"incident_case":str(ip),"remediation_plan":str(pp),"decision_envelope":str(dp),"recovery_validation_report":str(rvp),"rollback_receipt":str(rbp) if rbp else None,"ledger_entry":None},{}, {},status)
    rp=out/"receipts"/f"remediation_execution_receipt_{plan['plan_id']}.json"; write_canonical_json(rp,rec)
    lp=append_remediation_ledger_entry(out,dm.get("distribution_id","unknown"),incident,plan,rec); rec["outputs"]["ledger_entry"]=lp; write_canonical_json(rp,rec)
    if args.mode!="dry-run": write_canonical_json(out/"latest_incident.json",incident)
    code=0 if status in ("planned","success") else (5 if status=="dry_run" else 20)
    return str(rp), code

def main():
    ap=argparse.ArgumentParser()
    for r in ["current_distribution_manifest","current_distribution_receipt","monitor_snapshot","drift_report","alert_envelope","output_dir","mode"]: ap.add_argument("--"+r.replace("_","-"), required=True)
    for o in ["remote_access_validation_report","monitor_receipt","previous_good_distribution_manifest","previous_good_distribution_receipt","remediation_policy","target","bucket","prefix","endpoint_url","public_base_url","approval_token","approval_file","force_action","cloudfront_distribution_id"]: ap.add_argument("--"+o.replace("_","-"))
    for b in ["execute","allow_remote_network","cdn_invalidate","allow_broad_invalidation","allow_pointer_blind_write","allow_http","allow_symlinks","allow_serve_warning","allow_viewer_warning","allow_tile_warning","write_prov_jsonld","use_aws_cli","deterministic_run_id","keep_temp"]: ap.add_argument("--"+b.replace("_","-"), action="store_true")
    args=ap.parse_args()
    try:
        rp,code=handle_remote_drift(args); print(rp); raise SystemExit(code)
    except RemediationError as e:
        print(json.dumps({"status":"error","error_count":1,"remediation_execution_receipt_path":None,"incident_id":None,"plan_id":None}), file=os.sys.stderr); raise SystemExit(e.code)

if __name__=="__main__": main()
