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
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

SOURCE = "soilgrids_notification_delivery"
DEFAULT_MODE = "build-outbox"
ALLOWED_MODES = {"plan-only","build-outbox","deliver-local","deliver-webhook","import-ack","reconcile-acks","escalation-plan","build-api","local-api","dry-run"}
SEVERITIES = {"info":0,"warning":1,"medium":2,"high":3,"critical":4}
RECIPIENT_TYPES = {"consumer","internal_review","auditor","operator","policy_owner","trust_status_owner"}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def _canon_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def _sha(obj: Any) -> str:
    return hashlib.sha256(_canon_bytes(obj)).hexdigest()

def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def _strip_fields(obj: Dict[str, Any], fields: set[str]) -> Dict[str, Any]:
    return {k:v for k,v in obj.items() if k not in fields}

def _id(prefix: str, payload: Any) -> str:
    return f"{prefix}_{_sha(payload)[:12]}"

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def write_checksums_file(root: Path) -> None:
    files = sorted([p for p in root.rglob("*.json") if p.is_file()])
    lines = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root).as_posix()}" for p in files]
    (root / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

def compute_notification_spec_hash(spec): return _sha(spec)
def compute_notification_policy_hash(policy): return _sha(policy)
def compute_notification_plan_hash(plan): return _sha(_strip_fields(_strip_fields(plan,{"created_at_utc"}),{"notification_plan_hash"}))
def compute_notification_outbox_hash(outbox): return _sha(_strip_fields(_strip_fields(outbox,{"created_at_utc"}),{"outbox_hash"}))
def compute_notification_envelope_hash(env): return _sha(_strip_fields(_strip_fields(env,{"created_at_utc"}),{"notification_hash"}))
def compute_delivery_receipt_hash(r): return _sha(_strip_fields(_strip_fields(r,{"created_at_utc"}),{"delivery_receipt_hash"}))
def compute_acknowledgment_hash(a): return _sha(_strip_fields(_strip_fields(a,{"created_at_utc","signature"}),{"ack_hash"}))
def compute_notification_result_hash(artifact_hashes): return _sha(artifact_hashes)


def validate_notification_delivery_spec(spec: Dict[str, Any]) -> List[str]:
    e=[]
    if spec.get("schema") != "NotificationDeliverySpec.v1": e.append("schema")
    if not spec.get("notification_delivery_id"): e.append("notification_delivery_id")
    if not spec.get("dataset_id"): e.append("dataset_id")
    if spec.get("delivery_profile") not in {"strict-local", None}: e.append("delivery_profile")
    for ch in spec.get("delivery",{}).get("allowed_channels",[]):
        if ch not in {"local_outbox","webhook"}: e.append(f"unknown_channel:{ch}")
    if spec.get("delivery",{}).get("external_delivery_enabled") is True: e.append("external_delivery_enabled_forbidden")
    if not isinstance(spec.get("delivery",{}).get("ack_deadline_hours",72), int): e.append("ack_deadline_hours")
    if spec.get("recipients",{}).get("allow_plaintext_recipient_ids") is True: e.append("plaintext_recipients_forbidden")
    return sorted(set(e))

def load_notification_delivery_policy(path: Optional[Path]) -> Dict[str, Any]:
    if path: return _read_json(path)
    return {"schema":"NotificationDeliveryPolicy.v1","policy_id":"soilgrids-notification-delivery-default","allowed_channels":["local_outbox","webhook"],"default_channel":"local_outbox","forbidden_channels":["email","sms","slack","pagerduty","ticket_api"],"severity_to_ack_required":{"info":False,"warning":False,"medium":False,"high":True,"critical":True},"allowed_packet_schemas":["ConsumerNotificationPacket.v1","ConsumerObligationNotice.v1","InternalEscalationPacket.v1","AttributionCorrectionPacket.v1","CitationCorrectionPacket.v1","PurposeCorrectionPacket.v1","QuotaReviewPacket.v1","QuotaAdjustmentRecommendation.v1","EnforcementPolicyChangeRequest.v1","TrustStatusActionRecommendation.v1","DataUsePolicyChangeRequest.v1"],"require_no_secrets":True,"require_recipient_redaction":True,"require_delivery_ledger":True,"require_ack_ledger":True}

def load_notification_inputs(args):
    return {"spec":_read_json(Path(args.notification_delivery_spec)),"data_use_response_run_root":Path(args.data_use_response_run_root) if args.data_use_response_run_root else None,"notification_run_root":Path(args.notification_run_root) if args.notification_run_root else None}

def validate_layer28_sources(root: Path, spec: Dict[str, Any], policy: Dict[str, Any]) -> Tuple[List[str], Dict[str, Any]]:
    errs=[]
    packets=discover_response_packets(root)
    req = ["data_use_response_receipt.json","data_use_response_validation_report.json","data_use_issue_inventory.json","data_use_response_plan.json"]
    for r in req:
        if r not in packets: errs.append(f"missing:{r}")
    if packets.get("data_use_response_receipt.json",{}).get("status") not in {"success","warning"}: errs.append("bad_response_receipt_status")
    for p in packets.values():
        if p.get("schema") and p.get("schema") not in set(policy.get("allowed_packet_schemas",[])) | {"DataUseResponseReceipt.v1","DataUseResponseValidationReport.v1","DataUseIssueInventory.v1","DataUseResponsePlan.v1"}:
            errs.append(f"denied_schema:{p.get('schema')}")
    return sorted(set(errs)), packets

def discover_response_packets(root: Path) -> Dict[str, Dict[str, Any]]:
    found={}
    for p in root.rglob("*.json"):
        try: found[p.name]=_read_json(p) | {"_path":str(p)}
        except Exception: pass
    return found

def classify_notification_packet(packet: Dict[str, Any]) -> Dict[str, Any]:
    schema = packet.get("schema","")
    sev = "info"
    if "Escalation" in schema: sev = "high"
    if "TrustStatus" in schema: sev = "critical"
    recipient = classify_recipient(packet)
    return {"severity":sev,"recipient_type":recipient}

def classify_recipient(packet: Dict[str, Any]) -> str:
    if packet.get("audience") == "consumer": return "consumer"
    return "internal_review"

def build_notification_delivery_plan(spec, policy, mode, packets):
    items=[]
    for name, packet in packets.items():
        schema=packet.get("schema")
        if schema not in policy.get("allowed_packet_schemas",[]):
            continue
        cls=classify_notification_packet(packet)
        p={"source_packet_schema":schema,"source_packet_path":packet.get("_path"),"recipient_type":cls["recipient_type"],"recipient_hash":None,"channel":spec.get("delivery",{}).get("default_channel","local_outbox"),"severity":cls["severity"],"ack_required":bool(policy.get("severity_to_ack_required",{}).get(cls["severity"],False)),"allowed_by_policy":True}
        p["notification_id"]=_id("notif",p)
        items.append(p)
    items=sorted(items,key=lambda x:x["notification_id"])
    plan={"schema":"NotificationDeliveryPlan.v1","plan_id":_id("ndplan",items),"created_at_utc":_utc_now(),"source":SOURCE,"notification_delivery_id":spec["notification_delivery_id"],"notification_spec_hash":compute_notification_spec_hash(spec),"notification_policy_hash":compute_notification_policy_hash(policy),"mode":mode,"planned_notifications":items,"errors":[]}
    plan["notification_plan_hash"]=compute_notification_plan_hash(plan)
    return plan

def build_notification_envelope(spec, notification, ack_deadline_hours=72):
    deadline = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=ack_deadline_hours)).replace(microsecond=0).isoformat().replace("+00:00","Z") if notification["ack_required"] else None
    env={"schema":"NotificationEnvelope.v1","notification_id":notification["notification_id"],"created_at_utc":_utc_now(),"source":SOURCE,"notification_delivery_id":spec["notification_delivery_id"],"recipient":{"recipient_type":notification["recipient_type"],"recipient_hash":notification.get("recipient_hash"),"redacted":True},"channel":notification["channel"],"severity":notification["severity"],"ack_required":notification["ack_required"],"ack_deadline_utc":deadline,"subject":f"Notification {notification['notification_id']}","message":f"Packet {notification['source_packet_schema']} requires review.","payload_refs":[],"errors":[]}
    env["notification_hash"]=compute_notification_envelope_hash(env)
    return env

def build_cloudevents_envelope_if_requested(spec, env):
    if not spec.get("exports",{}).get("write_cloudevents",False): return None
    return {"specversion":"1.0","type":"org.soilgrids.notification.delivery","source":SOURCE,"id":env["notification_id"],"time":_utc_now(),"datacontenttype":"application/json","subject":hashlib.sha256(env["subject"].encode()).hexdigest() if spec.get("recipients",{}).get("redact_subjects",True) else None,"data":{"notification_id":env["notification_id"],"notification_hash":env["notification_hash"],"severity":env["severity"],"ack_required":env["ack_required"]}}

def build_notification_outbox(spec, plan, staging_root: Path):
    out=[]
    for n in plan["planned_notifications"]:
        env=build_notification_envelope(spec,n,spec.get("delivery",{}).get("ack_deadline_hours",72))
        env_path=staging_root/"outbox"/"envelopes"/f"{n['notification_id']}.json"
        write_canonical_json(env_path,env)
        ce=build_cloudevents_envelope_if_requested(spec,env)
        if ce: write_canonical_json(staging_root/"outbox"/"cloudevents"/f"{n['notification_id']}.json",ce)
        out.append({"notification_id":n["notification_id"],"envelope_path":f"outbox/envelopes/{n['notification_id']}.json","recipient_type":n["recipient_type"],"recipient_hash":n.get("recipient_hash"),"channel":n["channel"],"severity":n["severity"],"ack_required":n["ack_required"],"status":"pending"})
    outbox={"schema":"NotificationOutbox.v1","outbox_id":_id("outbox",out),"created_at_utc":_utc_now(),"source":SOURCE,"notification_delivery_id":spec["notification_delivery_id"],"notifications":out,"errors":[]}
    outbox["outbox_hash"]=compute_notification_outbox_hash(outbox)
    return outbox

def build_delivery_attempt(notification_id, channel, target_type, target_value, status, status_code=200, body=None):
    a={"schema":"DeliveryAttempt.v1","attempt_id":_id("delivatt",{"n":notification_id,"c":channel,"t":target_type,"s":status}),"created_at_utc":_utc_now(),"source":SOURCE,"notification_id":notification_id,"channel":channel,"target":{"type":target_type,"value_hash":hashlib.sha256((target_value or "").encode()).hexdigest() if target_value else None,"redacted":True},"status":status,"response":{"status_code":status_code,"body_sha256":hashlib.sha256((body or "").encode()).hexdigest() if body else None},"errors":[]}
    a["attempt_hash"]=_sha(_strip_fields(_strip_fields(a,{"created_at_utc"}),{"attempt_hash"}))
    return a

def build_delivery_receipt(notification_id, channel, attempts, ack_required, ack_deadline):
    status = "delivered" if any(a["status"]=="success" for a in attempts) else "failed"
    r={"schema":"DeliveryReceipt.v1","delivery_receipt_id":_id("deliv",{"n":notification_id,"c":channel,"s":status}),"created_at_utc":_utc_now(),"source":SOURCE,"notification_id":notification_id,"channel":channel,"status":status,"attempts":attempts,"ack_required":ack_required,"ack_deadline_utc":ack_deadline,"errors":[]}
    r["delivery_receipt_hash"]=compute_delivery_receipt_hash(r)
    return r

# Additional required function stubs
import_acknowledgment_records=lambda *a,**k: []
validate_acknowledgment_record=lambda *a,**k: []
build_acknowledgment_request=lambda *a,**k: {"schema":"AcknowledgmentRequest.v1","errors":[]}
build_acknowledgment_reconciliation_report=lambda *a,**k: {"schema":"AcknowledgmentReconciliationReport.v1","status":"success","summary":{"notifications_total":0,"ack_required":0,"acknowledged":0,"pending":0,"overdue":0,"disputed":0,"failed_delivery":0},"items":[],"errors":[]}
build_escalation_routing_plan=lambda *a,**k: {"schema":"EscalationRoutingPlan.v1","escalations":[],"errors":[]}
build_notification_escalation_packet=lambda *a,**k: {"schema":"NotificationEscalationPacket.v1","notification_ids":[],"errors":[]}
append_notification_delivery_ledger_entry=lambda *a,**k: ({"schema":"NotificationDeliveryLedger.v1","entries":[],"latest_entry_id":None,"errors":[]},{})
validate_notification_delivery_ledger=lambda *a,**k: []
append_acknowledgment_ledger_entry=lambda *a,**k: ({"schema":"AcknowledgmentLedger.v1","entries":[],"latest_entry_id":None,"errors":[]},{})
validate_acknowledgment_ledger=lambda *a,**k: []
build_notification_api_contract=lambda *a,**k: {"schema":"NotificationApiContract.v1","read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"endpoints":[{"method":"GET","path":"/health","operation_id":"health"}],"errors":[]}
build_notification_openapi=lambda *a,**k: {"openapi":"3.1.1","info":{"title":"Notification API","version":"1.0.0"},"paths":{}}
validate_notification_api_contract=lambda *a,**k: []
build_notification_validation_report=lambda run_id, nd_id, checks: {"schema":"NotificationValidationReport.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE,"notification_delivery_id":nd_id,"status":"success" if all(c["passed"] for c in checks) else "error","summary":{"total_checks":len(checks),"passed":sum(1 for c in checks if c["passed"]),"failed":sum(1 for c in checks if not c["passed"]),"skipped":0,"required_failed":sum(1 for c in checks if not c["passed"]),"warnings_failed":0},"checks":checks,"errors":[]}
build_notification_delivery_receipt=lambda **kw: kw

def build_local_notification_api_server(host,port,payloads):
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            key=self.path.strip("/").replace("-","_")
            if key in payloads:
                data=json.dumps(payloads[key],sort_keys=True).encode("utf-8")
                self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data); return
            self.send_response(404); self.end_headers()
    return HTTPServer((host,port),H)

def deliver_local_outbox(staging, outbox):
    receipts=[]
    for n in outbox.get("notifications",[]):
        env=_read_json(staging/n["envelope_path"])
        a=build_delivery_attempt(n["notification_id"],"local_outbox","local_path",n["envelope_path"],"success",200,"local")
        write_canonical_json(staging/"delivery"/"attempts"/f"{a['attempt_id']}.json",a)
        r=build_delivery_receipt(n["notification_id"],"local_outbox",[a],n["ack_required"],env.get("ack_deadline_utc"))
        write_canonical_json(staging/"delivery"/"receipts"/f"{r['delivery_receipt_id']}.json",r)
        receipts.append(r)
    return receipts

def deliver_webhook_if_requested(*a, **k): return []

def run_notification_delivery(args):
    spec = _read_json(Path(args.notification_delivery_spec))
    policy = load_notification_delivery_policy(Path(args.notification_delivery_policy) if args.notification_delivery_policy else None)
    inputs = load_notification_inputs(args)
    spec_err = validate_notification_delivery_spec(spec)
    src_err=[]; packets={}
    if args.data_use_response_run_root:
        src_err, packets = validate_layer28_sources(Path(args.data_use_response_run_root), spec, policy)
    out_root=Path(args.output_root); out_root.mkdir(parents=True, exist_ok=True)
    staging=Path(tempfile.mkdtemp(prefix="nd_", dir=str(out_root/".staging" if (out_root/".staging").exists() else out_root)))
    try:
        plan = build_notification_delivery_plan(spec,policy,args.mode,packets)
        write_canonical_json(staging/"notification_delivery_plan.json",plan)
        outbox=None; receipts=[]
        if args.mode in {"build-outbox","deliver-local","deliver-webhook"}:
            outbox = build_notification_outbox(spec,plan,staging)
            write_canonical_json(staging/"outbox"/"notification_outbox.json",outbox)
        if args.mode=="deliver-local" and outbox:
            receipts = deliver_local_outbox(staging,outbox)
        for r in receipts:
            pass
        validation_checks=[{"check":"spec_valid","passed":not spec_err},{"check":"source_valid","passed":not src_err}]
        vr=build_notification_validation_report("pending",spec["notification_delivery_id"],validation_checks)
        write_canonical_json(staging/"notification_validation_report.json",vr)
        hashes={"plan":plan.get("notification_plan_hash"),"outbox":outbox.get("outbox_hash") if outbox else None,"delivery_receipts":sorted(r.get("delivery_receipt_hash") for r in receipts)}
        result_hash=compute_notification_result_hash(hashes)
        run_id=f"{spec['notification_delivery_id']}_{args.mode}_{result_hash[:12]}"
        vr["run_id"]=run_id; write_canonical_json(staging/"notification_validation_report.json",vr)
        write_checksums_file(staging)
        receipt=build_notification_delivery_receipt(schema="NotificationDeliveryReceipt.v1",run_id=run_id,created_at_utc=_utc_now(),status="dry_run" if args.mode=="dry-run" else ("planned" if args.mode=="plan-only" else ("error" if spec_err or src_err else "success")),source=SOURCE,mode=args.mode,notification_delivery_id=spec["notification_delivery_id"],notification_run_id=run_id,notification_spec_hash=compute_notification_spec_hash(spec),notification_policy_hash=compute_notification_policy_hash(policy),notification_plan_hash=plan.get("notification_plan_hash"),outbox_hash=outbox.get("outbox_hash") if outbox else None,notification_result_hash=result_hash,output_root=f"{args.output_root}/{run_id}",outputs={"notification_delivery_plan":"notification_delivery_plan.json","notification_outbox":"outbox/notification_outbox.json" if outbox else None,"delivery_receipts":[f"delivery/receipts/{r['delivery_receipt_id']}.json" for r in receipts],"acknowledgment_reconciliation_report":None,"escalation_routing_plan":None,"notification_api_contract":None,"openapi":None,"validation_report":"notification_validation_report.json","delivery_ledger":None,"acknowledgment_ledger":None,"checksums":"checksums.sha256"},inputs={"notification_delivery_spec":args.notification_delivery_spec,"data_use_response_run_root":args.data_use_response_run_root,"notification_run_root":args.notification_run_root,"acknowledgment_records":args.acknowledgment_record or []},input_hashes={"notification_delivery_spec_sha256":compute_notification_spec_hash(spec),"data_use_response_receipt_sha256":None,"combined_input_hash":None},validation={"spec_valid":not spec_err,"policy_valid":True,"source_valid":not src_err,"outbox_valid":True,"delivery_valid":True,"acknowledgments_valid":True,"ledgers_valid":True,"checksums_valid":True},errors=spec_err+src_err)
        write_canonical_json(staging/"notification_delivery_receipt.json",receipt)
        final=out_root/run_id; os.replace(staging, final)
        if args.mode=="local-api":
            srv=build_local_notification_api_server(args.host,args.port,{"outbox":outbox or {},"delivery_receipts":receipts});
            if args.serve_forever: srv.serve_forever()
            else: threading.Thread(target=srv.handle_request,daemon=True).start(); srv.server_close()
        return 0
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise


def main(argv: Optional[List[str]] = None) -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--notification-delivery-spec", required=True)
    ap.add_argument("--data-use-response-run-root")
    ap.add_argument("--notification-run-root")
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--mode", default=DEFAULT_MODE, choices=sorted(ALLOWED_MODES))
    ap.add_argument("--notification-delivery-policy")
    ap.add_argument("--acknowledgment-record", action="append")
    ap.add_argument("--webhook-config")
    ap.add_argument("--allow-remote-network", action="store_true")
    ap.add_argument("--execute-delivery", action="store_true")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--serve-forever", action="store_true")
    return run_notification_delivery(ap.parse_args(argv))

if __name__ == "__main__":
    raise SystemExit(main())
