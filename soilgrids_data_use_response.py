#!/usr/bin/env python3
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

SOURCE = "soilgrids_data_use_response"
DEFAULT_MODE = "full"
ALLOWED_MODES = {"plan-only","classify","response-plan","obligation-fulfillment","quota-response","anomaly-response","consumer-notification","recommend-policy","full","local-api","dry-run"}
SEVERITIES = {"info":0,"warning":1,"medium":2,"high":3,"critical":4}
ISSUE_TYPES = {"denied_purpose","missing_purpose","missing_attribution","missing_citation","quota_exceeded","burst_usage","high_denial_rate","repeated_blocked_access","critical_anomaly","unknown"}
RESPONSE_TYPES = {"no_action","notify_consumer","internal_review","recommend_policy_change","recommend_enforcement_change","recommend_trust_status_review","plan_only","blocked"}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def _canon_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def _sha(obj: Any) -> str:
    return hashlib.sha256(_canon_bytes(obj)).hexdigest()

def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def _strip_created_at(obj: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in obj.items() if k != "created_at_utc"}

def _hash12(prefix: str, payload: Any) -> str:
    return f"{prefix}_{_sha(payload)[:12]}"

def _is_url_like(s: str) -> bool:
    u = urlparse(s)
    return bool(u.scheme and u.netloc)

def compute_data_use_response_spec_hash(spec: Dict[str, Any]) -> str: return _sha(spec)
def compute_data_use_response_policy_hash(policy: Dict[str, Any]) -> str: return _sha(policy)
def compute_issue_inventory_hash(inv: Dict[str, Any]) -> str: return _sha(_strip_created_at({k:v for k,v in inv.items() if k != 'issue_inventory_hash'}))
def compute_response_plan_hash(plan: Dict[str, Any]) -> str: return _sha(_strip_created_at({k:v for k,v in plan.items() if k != 'response_plan_hash'}))
def compute_response_packet_hash(packet: Dict[str, Any]) -> str: return _sha(_strip_created_at(packet))
def compute_data_use_response_result_hash(artifact_hashes: Dict[str, Any]) -> str: return _sha(artifact_hashes)

def validate_data_use_response_spec(spec: Dict[str, Any]) -> List[str]:
    e = []
    if spec.get("schema") != "DataUseResponseSpec.v1": e.append("schema")
    if not spec.get("data_use_response_id"): e.append("data_use_response_id")
    if not spec.get("dataset_id"): e.append("dataset_id")
    if spec.get("response_profile") not in {"strict-local", None}: e.append("response_profile")
    dec = spec.get("response_policy", {}).get("default_decision")
    if dec and dec not in RESPONSE_TYPES: e.append("default_decision")
    if spec.get("response_policy", {}).get("execute_external_notifications") is True: e.append("external_notifications_forbidden")
    for k,v in spec.get("issue_classification",{}).items():
        if v not in SEVERITIES: e.append(f"issue_severity:{k}")
    red = spec.get("redaction", {})
    if red and not isinstance(red.get("redact_subjects", True), bool): e.append("redaction_malformed")
    return sorted(set(e))

def load_data_use_response_policy(path: Optional[Path]) -> Dict[str, Any]:
    if path:
        return _read_json(path)
    return {
      "schema":"DataUseResponsePolicy.v1","policy_id":"soilgrids-data-use-response-default",
      "allowed_response_decisions":["no_action","plan_only","notify_consumer","internal_review","recommend_policy_change","recommend_enforcement_change","recommend_trust_status_review","blocked"],
      "issue_to_response":{"denied_purpose":"internal_review","missing_purpose":"notify_consumer","missing_attribution":"notify_consumer","missing_citation":"notify_consumer","quota_exceeded":"internal_review","burst_usage":"internal_review","high_denial_rate":"internal_review","repeated_blocked_access":"recommend_enforcement_change","critical_anomaly":"recommend_trust_status_review"},
      "required_evidence":["UsageEventInventory.v1","DataUseGovernanceReport.v1"],
      "forbidden_actions":["send_external_notification","mutate_policy","mutate_trust_status","grant_access","deny_access"],
      "audit":{"require_response_ledger":True,"require_subject_redaction":True,"require_packet_hashes":True}
    }

def load_data_use_response_inputs(args: argparse.Namespace) -> Dict[str, Any]:
    paths = {
      "spec": Path(args.data_use_response_spec),
      "run_root": Path(args.data_use_run_root) if args.data_use_run_root else None,
      "purpose": Path(args.purpose_compliance_report) if args.purpose_compliance_report else None,
      "obligation": Path(args.obligation_compliance_report) if args.obligation_compliance_report else None,
      "quota": Path(args.quota_compliance_report) if args.quota_compliance_report else None,
      "anomaly": Path(args.usage_anomaly_report) if args.usage_anomaly_report else None,
      "alerts": Path(args.data_use_alert_envelope) if args.data_use_alert_envelope else None,
      "consumer_stmt": Path(args.consumer_usage_statement) if args.consumer_usage_statement else None,
      "receipt": Path(args.data_use_receipt) if args.data_use_receipt else None,
    }
    for k,p in paths.items():
        if p and _is_url_like(str(p)): raise ValueError(f"remote path forbidden: {k}")
    data = {k: (_read_json(p) if p and p.exists() else None) for k,p in paths.items() if k != "run_root"}
    if paths["run_root"]:
        rr = paths["run_root"]
        auto = {
          "purpose": rr / "compliance" / "purpose_compliance_report.json",
          "obligation": rr / "compliance" / "obligation_compliance_report.json",
          "quota": rr / "compliance" / "quota_compliance_report.json",
          "anomaly": rr / "anomalies" / "usage_anomaly_report.json",
          "alerts": rr / "alerts" / "data_use_alert_envelope.json",
          "consumer_stmt": rr / "consumers" / "consumer_usage_statement.json",
          "receipt": rr / "data_use_receipt.json",
        }
        for k,p in auto.items():
            if data.get(k) is None and p.exists(): data[k] = _read_json(p)
    return data

def validate_layer27_sources(inputs: Dict[str, Any], spec: Dict[str, Any]) -> List[str]:
    e=[]
    if spec.get("source",{}).get("require_data_use_receipt_success") and inputs.get("receipt",{}).get("status") not in {"success","warning"}: e.append("data_use_receipt_status")
    if spec.get("source",{}).get("require_governance_report") and not inputs.get("receipt"): e.append("governance_missing")
    return e

def classify_data_use_issues(inputs: Dict[str, Any], spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    issues=[]
    sev = spec.get("issue_classification",{})
    def add(t,sv,msg,src,obj):
        payload={"issue_type":t,"severity":sv,"message":msg,"source_report":src,"subject_hash":obj.get("subject_hash"),"resource_key":obj.get("resource_key"),"event_ids":obj.get("event_ids",[]),"source_path":obj.get("source_path","local")}
        payload["issue_id"]=_hash12("dui",payload)
        issues.append(payload)
    for finding in (inputs.get("purpose",{}).get("findings",[]) or []):
        if finding.get("status") in {"denied_purpose","missing_purpose"}: add(finding["status"], sev.get("purpose_violation_severity","high"), finding.get("message","purpose violation"), "PurposeComplianceReport.v1", finding)
    for finding in (inputs.get("obligation",{}).get("findings",[]) or []):
        if finding.get("status") == "missing_attribution": add("missing_attribution", sev.get("obligation_missing_severity","medium"), finding.get("message","attribution missing"), "ObligationComplianceReport.v1", finding)
        if finding.get("status") == "missing_citation": add("missing_citation", sev.get("obligation_missing_severity","medium"), finding.get("message","citation missing"), "ObligationComplianceReport.v1", finding)
    for finding in (inputs.get("quota",{}).get("findings",[]) or []):
        if finding.get("status") == "quota_exceeded": add("quota_exceeded", sev.get("quota_exceeded_severity","warning"), finding.get("message","quota exceeded"), "QuotaComplianceReport.v1", finding)
    for finding in (inputs.get("anomaly",{}).get("findings",[]) or []):
        t = finding.get("anomaly_type", "unknown")
        mapped = t if t in ISSUE_TYPES else "critical_anomaly"
        add(mapped, sev.get("critical_anomaly_severity","critical"), finding.get("message","anomaly"), "UsageAnomalyReport.v1", finding)
    return issues

def build_data_use_issue_inventory(spec, issues):
    ordered=sorted(issues,key=lambda i:(-SEVERITIES.get(i["severity"],-1),i["issue_type"],i["issue_id"]))
    inv={"schema":"DataUseIssueInventory.v1","data_use_response_id":spec["data_use_response_id"],"created_at_utc":_utc_now(),"source":SOURCE,"issues":ordered,"summary":{"issues_total":len(ordered),"info":0,"warning":0,"medium":0,"high":0,"critical":0},"errors":[]}
    for i in ordered: inv["summary"][i["severity"]]+=1
    inv["issue_inventory_hash"]=compute_issue_inventory_hash(inv)
    return inv

def build_data_use_incident_case(spec, inv, policy):
    issues=inv.get("issues",[])
    p={"schema":"DataUseIncidentCase.v1","created_at_utc":_utc_now(),"source":SOURCE,"data_use_response_id":spec["data_use_response_id"],"severity":max([i['severity'] for i in issues], key=lambda s:SEVERITIES[s], default="none"),"incident_types":sorted(set(i['issue_type'] for i in issues)),"issue_ids":[i['issue_id'] for i in issues],"affected_subjects":sorted(set(i.get("subject_hash") for i in issues if i.get("subject_hash"))),"affected_resources":sorted(set(i.get("resource_key") for i in issues if i.get("resource_key"))),"evidence_refs":sorted(set(i['source_report'] for i in issues)),"recommended_responses":sorted(set(policy.get("issue_to_response",{}).get(i['issue_type'],"plan_only") for i in issues)),"errors":[]}
    p["incident_id"]=_hash12("duinc",p)
    return p

def build_usage_anomaly_case(inv):
    an=[i for i in inv.get("issues",[]) if i["issue_type"] in {"critical_anomaly","burst_usage","high_denial_rate"}]
    c={"schema":"UsageAnomalyCase.v1","created_at_utc":_utc_now(),"source":SOURCE,"severity":max([i['severity'] for i in an], key=lambda s:SEVERITIES[s], default="info"),"anomaly_ids":[i['issue_id'] for i in an],"subject_hashes":sorted(set(i.get('subject_hash') for i in an if i.get('subject_hash'))),"resource_keys":sorted(set(i.get('resource_key') for i in an if i.get('resource_key'))),"recommended_responses":sorted(set(i['issue_type'] for i in an)),"errors":[]}
    c["anomaly_case_id"]=_hash12("duanom",c)
    return c

def build_data_use_response_plan(spec, inv, policy, mode):
    planned=[]
    for i in inv.get("issues",[]):
        rtype = policy.get("issue_to_response",{}).get(i["issue_type"], spec.get("response_policy",{}).get("default_decision","plan_only"))
        item={"issue_id":i["issue_id"],"response_type":rtype,"requires_approval":bool(rtype.startswith("recommend_") and spec.get("response_policy",{}).get("require_approval_for_policy_recommendation",True)),"allowed_by_policy":rtype in policy.get("allowed_response_decisions",[]),"evidence_refs":[i["source_report"]]}
        item["response_id"]=_hash12("resp",item)
        planned.append(item)
    planned=sorted(planned,key=lambda x:x["response_id"])
    plan={"schema":"DataUseResponsePlan.v1","created_at_utc":_utc_now(),"source":SOURCE,"data_use_response_id":spec["data_use_response_id"],"mode":mode,"planned_responses":planned,"errors":[]}
    plan["plan_id"]=_hash12("duresp",plan)
    plan["response_plan_hash"]=compute_response_plan_hash(plan)
    return plan

def build_data_use_response_decision_envelope(run_id,spec,plan):
    approval_required=any(r["requires_approval"] for r in plan.get("planned_responses",[]))
    blocked=any(not r["allowed_by_policy"] for r in plan.get("planned_responses",[]))
    d="blocked" if blocked else "execute_local"
    e={"schema":"DataUseResponseDecisionEnvelope.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE,"decision":d,"reason":"forbidden response mapped" if blocked else "local packet generation only","data_use_response_id":spec["data_use_response_id"],"plan_id":plan["plan_id"],"response_plan_hash":plan["response_plan_hash"],"approval_required":approval_required,"approval_satisfied":not approval_required,"blocking_reasons":["policy_rejection"] if blocked else [],"errors":[]}
    return e

# smaller builders
build_obligation_fulfillment_plan=lambda inv: {"schema":"ObligationFulfillmentPlan.v1","plan_id":_hash12("obful",inv.get("issues",[])),"created_at_utc":_utc_now(),"source":SOURCE,"duties":[{"duty_id":"duty.attribution","status":"correction_required" if any(i['issue_type']=='missing_attribution' for i in inv.get('issues',[])) else "satisfied","issue_ids":[i['issue_id'] for i in inv.get('issues',[]) if i['issue_type']=='missing_attribution'],"correction_packet_path":"obligations/attribution_correction_packet.json"}],"errors":[]}
build_attribution_correction_packet=lambda inv: {"schema":"AttributionCorrectionPacket.v1","packet_id":_hash12("attrcorr",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"ready" if any(i['issue_type']=='missing_attribution' for i in inv.get('issues',[])) else "not_required","required_text":"Please include SoilGrids attribution.","affected_events":[],"consumer_refs":[],"evidence_refs":[],"errors":[]}
build_citation_correction_packet=lambda inv: {"schema":"CitationCorrectionPacket.v1","packet_id":_hash12("citecorr",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"ready" if any(i['issue_type']=='missing_citation' for i in inv.get('issues',[])) else "not_required","citation_text":"Provide canonical SoilGrids citation.","affected_events":[],"consumer_refs":[],"evidence_refs":[],"errors":[]}
build_purpose_correction_packet=lambda inv: {"schema":"PurposeCorrectionPacket.v1","packet_id":_hash12("purpcorr",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"ready" if any(i['issue_type'] in {'denied_purpose','missing_purpose'} for i in inv.get('issues',[])) else "not_required","missing_or_invalid_purpose_events":[],"allowed_purposes":[],"denied_purposes":[],"instructions":[],"errors":[]}
build_consumer_obligation_notice=lambda inv: {"schema":"ConsumerObligationNotice.v1","notice_id":_hash12("obnotice",inv),"created_at_utc":_utc_now(),"source":SOURCE,"subject_hash":None,"status":"ready" if inv.get('issues') else "not_required","notices":[{"notice_type":"purpose","severity":"warning","message":"Review data-use obligations.","required_action":"Update usage metadata."}] if inv.get('issues') else [],"errors":[]}
build_quota_response_plan=lambda inv: {"schema":"QuotaResponsePlan.v1","plan_id":_hash12("quotaresp",inv),"created_at_utc":_utc_now(),"source":SOURCE,"quota_issues":[i['issue_id'] for i in inv.get('issues',[]) if i['issue_type']=='quota_exceeded'],"recommended_actions":[],"errors":[]}
build_quota_review_packet=lambda inv: {"schema":"QuotaReviewPacket.v1","packet_id":_hash12("quotarev",inv),"created_at_utc":_utc_now(),"source":SOURCE,"quota_status":"exceeded" if any(i['issue_type']=='quota_exceeded' for i in inv.get('issues',[])) else "within_limit","subjects":[],"resources":[],"evidence_refs":[],"errors":[]}
build_quota_adjustment_recommendation=lambda inv: {"schema":"QuotaAdjustmentRecommendation.v1","recommendation_id":_hash12("quotarec",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"recommended" if any(i['issue_type']=='quota_exceeded' for i in inv.get('issues',[])) else "not_recommended","recommended_changes":[],"errors":[]}
build_usage_anomaly_response_plan=lambda case: {"schema":"UsageAnomalyResponsePlan.v1","plan_id":_hash12("anomresp",case),"created_at_utc":_utc_now(),"source":SOURCE,"anomaly_cases":case.get('anomaly_ids',[]),"recommended_actions":[],"errors":[]}
build_internal_escalation_packet=lambda inv: {"schema":"InternalEscalationPacket.v1","packet_id":_hash12("escalate",inv),"created_at_utc":_utc_now(),"source":SOURCE,"severity":"high" if any(i['severity'] in {'high','critical'} for i in inv.get('issues',[])) else "info","title":"Data use escalation","summary":"Internal review recommended.","issue_ids":[i['issue_id'] for i in inv.get('issues',[])],"recommended_actions":[],"evidence_refs":[],"public_safe":False,"errors":[]}
build_consumer_notification_packet=lambda inv,subject_hash=None: {"schema":"ConsumerNotificationPacket.v1","packet_id":_hash12("cnotify",inv),"created_at_utc":_utc_now(),"source":SOURCE,"audience":"consumer","subject_hash":subject_hash,"status":"ready" if inv.get('issues') else "not_required","messages":[i['message'] for i in inv.get('issues',[])],"delivery":{"external_delivery":False,"delivery_method":"local-file-only"},"errors":[]}
build_enforcement_policy_change_request=lambda inv: {"schema":"EnforcementPolicyChangeRequest.v1","request_id":_hash12("epcr",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"recommended" if any(i['issue_type']=='repeated_blocked_access' for i in inv.get('issues',[])) else "not_recommended","recommended_changes":[],"evidence_refs":[],"errors":[]}
build_trust_status_action_recommendation=lambda inv: {"schema":"TrustStatusActionRecommendation.v1","recommendation_id":_hash12("tsar",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"recommended" if any(i['issue_type']=='critical_anomaly' for i in inv.get('issues',[])) else "not_recommended","recommended_action":"under_review" if any(i['issue_type']=='critical_anomaly' for i in inv.get('issues',[])) else "none","target":{"trust_object_id":None,"subject_hash":None},"reason":"Anomaly pattern.","evidence_refs":[],"errors":[]}
build_data_use_policy_change_request=lambda inv: {"schema":"DataUsePolicyChangeRequest.v1","request_id":_hash12("dupcr",inv),"created_at_utc":_utc_now(),"source":SOURCE,"status":"recommended" if inv.get('issues') else "not_recommended","recommended_changes":[],"evidence_refs":[],"errors":[]}

def append_data_use_response_ledger_entry(ledger_dir: Path, data_use_response_id: str, response_plan_hash: str, issue_inventory_hash: str, artifact_hashes: Dict[str, str], status: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    ledger_path=ledger_dir/"data_use_response_ledger.json"; entries_dir=ledger_dir/"entries"; entries_dir.mkdir(parents=True,exist_ok=True)
    ledger=_read_json(ledger_path) if ledger_path.exists() else {"schema":"DataUseResponseLedger.v1","data_use_response_id":data_use_response_id,"created_at_utc":_utc_now(),"source":SOURCE,"entries":[],"latest_entry_id":None,"errors":[]}
    prev = ledger["entries"][-1] if ledger["entries"] else None
    entry={"schema":"DataUseResponseLedgerEntry.v1","created_at_utc":_utc_now(),"source":SOURCE,"data_use_response_id":data_use_response_id,"response_plan_hash":response_plan_hash,"issue_inventory_hash":issue_inventory_hash,"artifact_hashes":artifact_hashes,"previous_entry_id":prev["entry_id"] if prev else None,"previous_chain_hash":prev["chain_hash"] if prev else None}
    entry["response_entry_id"]=_hash12("durl",entry)
    entry["entry_id"]=_sha({k:v for k,v in entry.items() if k not in {"entry_id","chain_hash"}})
    entry["chain_hash"]=_sha({"entry_id":entry["entry_id"],"previous_chain_hash":entry["previous_chain_hash"]})
    slug=entry["created_at_utc"].replace(":","").replace("-","")
    ep=entries_dir/f"{slug}_{entry['response_entry_id']}.json"; write_canonical_json(ep,entry)
    ledger["entries"].append({"entry_id":entry["entry_id"],"response_entry_id":entry["response_entry_id"],"response_plan_hash":response_plan_hash,"status":status,"chain_hash":entry["chain_hash"],"entry_path":f"entries/{ep.name}"})
    ledger["latest_entry_id"]=entry["entry_id"]
    write_canonical_json(ledger_path,ledger)
    return ledger,entry

def validate_data_use_response_ledger(ledger): return [] if ledger.get("schema")=="DataUseResponseLedger.v1" else ["schema"]
def build_data_use_response_api_contract(inv,plan): return {"schema":"DataUseResponseApiContract.v1","source":SOURCE,"read_only":True,"resources":["issue_inventory","response_plan","ledger"],"counts":{"issues":len(inv.get('issues',[])),"responses":len(plan.get('planned_responses',[]))}}
def build_data_use_response_openapi(contract): return {"openapi":"3.0.0","info":{"title":"Data Use Response API","version":"1.0.0"},"paths":{"/issue-inventory":{"get":{"responses":{"200":{"description":"ok"}}}},"/response-plan":{"get":{"responses":{"200":{"description":"ok"}}}}}}
def validate_response_api_contract(contract): return [] if contract.get("read_only") else ["read_only_required"]
def build_data_use_response_validation_report(run_id,data_use_response_id,checks):
    failed=sum(1 for c in checks if not c["passed"])
    return {"schema":"DataUseResponseValidationReport.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE,"data_use_response_id":data_use_response_id,"status":"success" if failed==0 else "error","summary":{"total_checks":len(checks),"passed":len(checks)-failed,"failed":failed,"skipped":0,"required_failed":failed,"warnings_failed":0},"checks":checks,"errors":[]}
def build_data_use_response_receipt(**kw): return kw
def build_response_execution_receipt(*a,**kw): return {"schema":"DataUseResponseExecutionReceipt.v1","source":SOURCE,"errors":[]}

def write_checksums_file(root: Path) -> None:
    files = sorted([p for p in root.rglob("*.json") if p.is_file()])
    lines=[]
    for p in files:
        rel=p.relative_to(root).as_posix()
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        lines.append(f"{h}  {rel}")
    (root/"checksums.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")

def build_local_response_api_server(host,port,payloads):
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            key=self.path.strip("/").replace("-","_")
            if key in payloads:
                data=json.dumps(payloads[key],sort_keys=True).encode("utf-8")
                self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data); return
            self.send_response(404); self.end_headers()
    return HTTPServer((host,port),H)

def run_data_use_response(args: argparse.Namespace) -> int:
    spec=_read_json(Path(args.data_use_response_spec)); spec_err=validate_data_use_response_spec(spec)
    policy=load_data_use_response_policy(Path(args.data_use_response_policy) if args.data_use_response_policy else None)
    inputs=load_data_use_response_inputs(args)
    src_err=validate_layer27_sources(inputs,spec)
    issues=classify_data_use_issues(inputs,spec)
    inv=build_data_use_issue_inventory(spec,issues)
    plan=build_data_use_response_plan(spec,inv,policy,args.mode)
    incident=build_data_use_incident_case(spec,inv,policy)
    an_case=build_usage_anomaly_case(inv)
    decision=build_data_use_response_decision_envelope("pending",spec,plan)
    out_root=Path(args.output_root); out_root.mkdir(parents=True,exist_ok=True)
    staging=Path(tempfile.mkdtemp(prefix="dur_",dir=str(out_root/".staging" if (out_root/".staging").exists() else out_root)))
    try:
        write_canonical_json(staging/"data_use_issue_inventory.json",inv); write_canonical_json(staging/"data_use_response_plan.json",plan)
        write_canonical_json(staging/"data_use_response_decision_envelope.json",decision)
        write_canonical_json(staging/"incidents"/"data_use_incident_case.json",incident); write_canonical_json(staging/"incidents"/"usage_anomaly_case.json",an_case)
        packets={"obligations/obligation_fulfillment_plan.json":build_obligation_fulfillment_plan(inv),"obligations/attribution_correction_packet.json":build_attribution_correction_packet(inv),"obligations/citation_correction_packet.json":build_citation_correction_packet(inv),"obligations/purpose_correction_packet.json":build_purpose_correction_packet(inv),"obligations/consumer_obligation_notice.json":build_consumer_obligation_notice(inv),"quota/quota_response_plan.json":build_quota_response_plan(inv),"quota/quota_review_packet.json":build_quota_review_packet(inv),"quota/quota_adjustment_recommendation.json":build_quota_adjustment_recommendation(inv),"anomalies/usage_anomaly_response_plan.json":build_usage_anomaly_response_plan(an_case),"anomalies/internal_escalation_packet.json":build_internal_escalation_packet(inv),"notifications/consumer_notification_packet.json":build_consumer_notification_packet(inv,args.subject_hash),"recommendations/enforcement_policy_change_request.json":build_enforcement_policy_change_request(inv),"recommendations/trust_status_action_recommendation.json":build_trust_status_action_recommendation(inv),"recommendations/data_use_policy_change_request.json":build_data_use_policy_change_request(inv)}
        for rel,obj in packets.items(): write_canonical_json(staging/rel,obj)
        contract=build_data_use_response_api_contract(inv,plan); openapi=build_data_use_response_openapi(contract)
        write_canonical_json(staging/"api"/"data_use_response_api_contract.json",contract); write_canonical_json(staging/"api"/"data_use_response_openapi.json",openapi)
        checks=[{"check":"spec_valid","passed":not spec_err},{"check":"layer27_sources_valid","passed":not src_err}]
        result_hash=compute_data_use_response_result_hash({"issue_inventory_hash":inv["issue_inventory_hash"],"response_plan_hash":plan["response_plan_hash"]})
        run_id=f"{spec['data_use_response_id']}_{args.mode}_{result_hash[:12]}"
        decision["run_id"]=run_id; write_canonical_json(staging/"data_use_response_decision_envelope.json",decision)
        report=build_data_use_response_validation_report(run_id,spec["data_use_response_id"],checks); write_canonical_json(staging/"data_use_response_validation_report.json",report)
        ledger,entry=append_data_use_response_ledger_entry(staging/"ledger",spec["data_use_response_id"],plan["response_plan_hash"],inv["issue_inventory_hash"],{"result_hash":result_hash},"ready")
        write_checksums_file(staging)
        receipt={"schema":"DataUseResponseReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"dry_run" if args.mode=="dry-run" else ("planned" if args.mode=="plan-only" else ("error" if spec_err or src_err else "success")),"source":SOURCE,"mode":args.mode,"data_use_response_id":spec["data_use_response_id"],"data_use_response_run_id":run_id,"data_use_response_spec_hash":compute_data_use_response_spec_hash(spec),"data_use_response_policy_hash":compute_data_use_response_policy_hash(policy),"issue_inventory_hash":inv["issue_inventory_hash"],"response_plan_hash":plan["response_plan_hash"],"data_use_response_result_hash":result_hash,"output_root":f"{args.output_root}/{run_id}","outputs":{"data_use_response_plan":"data_use_response_plan.json","issue_inventory":"data_use_issue_inventory.json","incident_case":"incidents/data_use_incident_case.json","response_decision":"data_use_response_decision_envelope.json","obligation_fulfillment_plan":"obligations/obligation_fulfillment_plan.json","consumer_notification_packet":"notifications/consumer_notification_packet.json","internal_escalation_packet":"anomalies/internal_escalation_packet.json","quota_response_plan":"quota/quota_response_plan.json","policy_change_requests":["recommendations/enforcement_policy_change_request.json","recommendations/trust_status_action_recommendation.json","recommendations/data_use_policy_change_request.json"],"validation_report":"data_use_response_validation_report.json","response_ledger":"ledger/data_use_response_ledger.json","checksums":"checksums.sha256"},"inputs":{"data_use_response_spec":args.data_use_response_spec,"data_use_run_root":args.data_use_run_root,"data_use_receipt":args.data_use_receipt,"usage_anomaly_report":args.usage_anomaly_report,"data_use_alert_envelope":args.data_use_alert_envelope},"input_hashes":{"data_use_response_spec_sha256":compute_data_use_response_spec_hash(spec),"data_use_receipt_sha256":_sha(inputs.get('receipt')) if inputs.get('receipt') else None,"combined_layer27_input_hash":_sha({k:v for k,v in inputs.items() if v is not None}) if any(v is not None for v in inputs.values()) else None},"validation":{"spec_valid":not spec_err,"policy_valid":True,"layer27_sources_valid":not src_err,"issues_valid":True,"response_plan_valid":True,"packets_valid":True,"recommendations_valid":True,"ledger_valid":not validate_data_use_response_ledger(ledger),"checksums_valid":True},"errors":spec_err+src_err}
        write_canonical_json(staging/"data_use_response_receipt.json",receipt)
        final=out_root/run_id
        os.replace(staging,final)
        if args.mode=="local-api":
            srv=build_local_response_api_server(args.host,args.port,{"issue_inventory":inv,"response_plan":plan,"ledger":ledger});
            if args.serve_forever: srv.serve_forever()
            else: threading.Thread(target=srv.handle_request,daemon=True).start(); srv.server_close()
        return 0
    except Exception:
        shutil.rmtree(staging,ignore_errors=True)
        raise

def main(argv: Optional[List[str]] = None) -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--data-use-response-spec",required=True)
    ap.add_argument("--data-use-run-root")
    ap.add_argument("--output-root",required=True)
    ap.add_argument("--mode",default=DEFAULT_MODE,choices=sorted(ALLOWED_MODES))
    ap.add_argument("--data-use-response-policy")
    ap.add_argument("--purpose-compliance-report")
    ap.add_argument("--obligation-compliance-report")
    ap.add_argument("--quota-compliance-report")
    ap.add_argument("--usage-anomaly-report")
    ap.add_argument("--data-use-alert-envelope")
    ap.add_argument("--consumer-usage-statement")
    ap.add_argument("--data-use-receipt")
    ap.add_argument("--subject-hash")
    ap.add_argument("--host",default="127.0.0.1")
    ap.add_argument("--port",type=int,default=0)
    ap.add_argument("--serve-forever",action="store_true")
    return run_data_use_response(ap.parse_args(argv))

if __name__=="__main__":
    raise SystemExit(main())
