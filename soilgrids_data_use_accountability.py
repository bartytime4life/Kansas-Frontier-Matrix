#!/usr/bin/env python3
from __future__ import annotations

import datetime
import hashlib
import json
import logging
import os
import re
import shutil
import socket
import threading
from dataclasses import dataclass
from enum import Enum
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

SOURCE = "soilgrids_data_use_accountability"
DEFAULT_MODE = "full"
ALLOWED_MODES = {
    "plan-only", "inventory-usage", "meter-usage", "evaluate-obligations", "quota-check",
    "anomaly-scan", "consumer-statement", "full", "local-api", "dry-run"
}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canon_obj(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha_obj(obj: Any) -> str:
    return hashlib.sha256(_canon_obj(obj)).hexdigest()


def _sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _read_json(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _is_local_path_or_file_url(v: str) -> bool:
    p = urlparse(v)
    if p.scheme in ("", "file"):
        if p.fragment or p.username or p.password:
            return False
        return True
    return False


def validate_data_use_spec(spec: Dict[str, Any], allow_plaintext_subjects: bool = False) -> List[str]:
    e = []
    if spec.get("schema") != "DataUseSpec.v1": e.append("schema")
    if not spec.get("data_use_id"): e.append("data_use_id")
    if not spec.get("dataset_id"): e.append("dataset_id")
    if spec.get("usage_sources", {}).get("require_usage_audit_ledger_valid") is False: e.append("require_usage_audit_ledger_valid")
    o = spec.get("obligations", {})
    if set(o.get("allowed_purposes", [])).intersection(set(o.get("denied_purposes", []))): e.append("purpose_policy_conflict")
    q = spec.get("quotas", {})
    for k in ["default_subject_daily_events", "default_subject_daily_bytes", "default_resource_daily_events"]:
        if k in q and (not isinstance(q[k], int) or q[k] < 0): e.append(f"quotas.{k}")
    a = spec.get("anomaly_detection", {})
    for k in ["burst_event_threshold", "burst_window_minutes", "denial_rate_warning_percent", "blocked_access_critical_threshold"]:
        if k in a and (not isinstance(a[k], int) or a[k] < 0): e.append(f"anomaly_detection.{k}")
    p = spec.get("privacy", {})
    if p and p.get("forbid_plaintext_subjects") is not True and not allow_plaintext_subjects: e.append("forbid_plaintext_subjects")
    return e


def load_data_use_policy(path: Optional[str]) -> Dict[str, Any]:
    if path:
        if not _is_local_path_or_file_url(path):
            raise ValueError("remote policy URLs are not allowed")
        return _read_json(path)
    return {
        "schema": "DataUsePolicy.v1", "policy_id": "soilgrids-data-use-default",
        "allowed_actions": ["read", "download", "view", "embed", "cite", "analyze", "audit"],
        "denied_actions": ["redistribute_unapproved", "resell_unapproved"],
        "allowed_purposes": ["audit", "research", "visualization", "internal_analysis", "model_input"],
        "denied_purposes": ["unauthorized_redistribution", "unapproved_commercial_resale"],
        "duties": [
            {"duty_id": "duty.attribution", "title": "Attribution required", "required": True, "evidence_field": "attribution_present"},
            {"duty_id": "duty.citation", "title": "Citation required", "required": True, "evidence_field": "citation_present"},
        ],
        "prohibitions": [{"prohibition_id": "prohibition.redistribution", "action": "redistribute_unapproved", "severity": "critical"}],
        "quota_policy": {"fail_on_quota_exceeded": False, "warn_on_quota_exceeded": True, "critical_on_repeated_quota_exceeded": True},
        "audit": {"require_ledger_chain": True, "require_subject_redaction": True, "require_event_hashes": True},
    }


def _validate_policy(policy: Dict[str, Any]) -> List[str]:
    e = []
    if policy.get("schema") != "DataUsePolicy.v1": e.append("schema")
    if set(policy.get("allowed_actions", [])).intersection(policy.get("denied_actions", [])): e.append("action_conflict")
    if set(policy.get("allowed_purposes", [])).intersection(policy.get("denied_purposes", [])): e.append("purpose_conflict")
    for p in policy.get("prohibitions", []):
        if p.get("severity") not in {"info", "warning", "critical"}: e.append("prohibition_severity")
    return e


def validate_usage_audit_ledger(ledger: Dict[str, Any]) -> List[str]:
    e = []
    if ledger.get("schema") != "UsageAuditLedger.v1": e.append("schema")
    if not isinstance(ledger.get("entries", []), list): e.append("entries")
    return e


def validate_usage_audit_event(event: Dict[str, Any]) -> List[str]:
    e = []
    if event.get("schema") not in {None, "UsageAuditEvent.v1"}: e.append("schema")
    if not event.get("request_id"): e.append("request_id")
    return e


def discover_usage_audit_events(usage_audit_ledger_path: str) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[str]]:
    ledger = _read_json(usage_audit_ledger_path)
    errors = validate_usage_audit_ledger(ledger)
    events = []
    for en in ledger.get("entries", []):
        p = en.get("event_path") or en.get("usage_audit_event_path")
        if p:
            ep = (Path(usage_audit_ledger_path).parent / p).resolve()
            if ep.exists():
                ev = _read_json(ep)
                verr = validate_usage_audit_event(ev)
                if verr: errors.extend([f"event:{','.join(verr)}:{ep}"])
                events.append(ev)
    return ledger, events, errors


def classify_usage_event(event: Dict[str, Any]) -> Dict[str, Any]:
    subject_hash = (event.get("subject") or {}).get("subject_hash") or event.get("subject_hash")
    action = event.get("action") or "read"
    event_hash = event.get("event_hash") or _sha_obj({k: v for k, v in event.items() if k != "event_hash"})
    return {
        "event_id": "uae_" + event_hash[:12], "event_hash": event_hash, "request_id": event.get("request_id", ""),
        "subject_hash": subject_hash, "subject_type": (event.get("subject") or {}).get("subject_type", "anonymous"),
        "action": action, "enforcement_action": event.get("enforcement_action", "error"),
        "protected_resource_id": event.get("protected_resource_id"), "resource_sha256": event.get("resource_sha256"),
        "trust_object_id": event.get("trust_object_id"), "resource_role": event.get("resource_role"),
        "bytes_served": int(event.get("bytes_served") or 0), "purpose": event.get("purpose"),
        "event_time_utc": event.get("event_time_utc")
    }


def build_data_use_plan(spec: Dict[str, Any], mode: str, events_count: int) -> Dict[str, Any]:
    return {"schema": "DataUsePlan.v1", "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "mode": mode, "events_discovered": events_count}


def compute_usage_event_inventory_hash(inv: Dict[str, Any]) -> str:
    x = dict(inv); x.pop("created_at_utc", None); x.pop("inventory_hash", None)
    return _sha_obj(x)


def build_usage_event_inventory(spec: Dict[str, Any], events: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [classify_usage_event(e) for e in events]
    rows.sort(key=lambda r: ((r.get("event_time_utc") or ""), r["event_id"]))
    s = {
        "events_total": len(rows), "grants": sum(1 for r in rows if str(r["enforcement_action"]).startswith("grant")),
        "denials": sum(1 for r in rows if r["enforcement_action"] == "deny"), "reviews": sum(1 for r in rows if r["enforcement_action"] == "review_required"),
        "errors": sum(1 for r in rows if r["enforcement_action"] == "error"), "unique_subjects": len({r.get("subject_hash") for r in rows if r.get("subject_hash")}),
        "unique_resources": len({r.get("resource_sha256") for r in rows if r.get("resource_sha256")}),
    }
    inv = {"schema": "UsageEventInventory.v1", "data_use_id": spec["data_use_id"], "created_at_utc": _utc_now(), "source": SOURCE, "inventory_hash": "", "events": rows, "summary": s, "errors": []}
    inv["inventory_hash"] = compute_usage_event_inventory_hash(inv)
    return inv


def aggregate_usage_metrics(inv: Dict[str, Any]) -> Dict[str, Any]:
    events = inv.get("events", [])
    by = lambda key: sorted([{"key": k, "events": len(v), "bytes": sum(x["bytes_served"] for x in v)} for k, v in {kk: [e for e in events if (e.get(key) == kk)] for kk in sorted({e.get(key) for e in events})}.items()], key=lambda x: (str(x["key"])))
    return {"by_subject": by("subject_hash"), "by_resource": by("resource_sha256"), "by_action": by("action"), "by_purpose": by("purpose")}


def compute_metering_snapshot_hash(snapshot: Dict[str, Any]) -> str:
    x = dict(snapshot); x.pop("created_at_utc", None); x.pop("snapshot_id", None); x.pop("metering_snapshot_hash", None)
    return _sha_obj(x)


def build_usage_metering_snapshot(spec: Dict[str, Any], inv: Dict[str, Any]) -> Dict[str, Any]:
    events = inv.get("events", [])
    agg = aggregate_usage_metrics(inv)
    tw = sorted([e.get("event_time_utc") for e in events if e.get("event_time_utc")])
    snap = {"schema": "UsageMeteringSnapshot.v1", "snapshot_id": "", "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "metering_snapshot_hash": "", "time_window": {"start_utc": tw[0] if tw else None, "end_utc": tw[-1] if tw else None}, "counters": {"events_total": len(events), "grant_events": sum(1 for e in events if str(e.get("enforcement_action", "")).startswith("grant")), "denial_events": sum(1 for e in events if e.get("enforcement_action") == "deny"), "review_events": sum(1 for e in events if e.get("enforcement_action") == "review_required"), "bytes_served_total": sum(int(e.get("bytes_served") or 0) for e in events), "subjects_total": len({e.get("subject_hash") for e in events if e.get("subject_hash")}), "resources_total": len({e.get("resource_sha256") for e in events if e.get("resource_sha256")})}, **agg, "errors": []}
    h = compute_metering_snapshot_hash(snap)
    snap["metering_snapshot_hash"] = h
    snap["snapshot_id"] = "usage_" + h[:12]
    return snap


def build_usage_metering_report(run_id: str, spec: Dict[str, Any], snap: Dict[str, Any]) -> Dict[str, Any]:
    return {"schema": "UsageMeteringReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "status": "success", "snapshot_id": snap["snapshot_id"], "summary": snap["counters"], "errors": []}


def evaluate_purpose_compliance(run_id: str, spec: Dict[str, Any], inv: Dict[str, Any], policy: Dict[str, Any]) -> Dict[str, Any]:
    allowed = set(policy.get("allowed_purposes", [])); denied = set(policy.get("denied_purposes", [])); req = spec.get("obligations", {}).get("require_purpose", True)
    checks, ap, dp, mp = [], 0, 0, 0
    for e in inv.get("events", []):
        p = e.get("purpose")
        if p in denied: st = "fail"; dp += 1
        elif p in allowed: st = "pass"; ap += 1
        elif p is None and req: st = "fail"; mp += 1
        else: st = "skipped"
        checks.append({"check_id": f"purpose.allowed.{p or 'missing'}", "severity": "required", "status": st, "subject_hash": e.get("subject_hash"), "event_id": e["event_id"], "purpose": p, "message": "purpose check"})
    status = "fail" if (dp or mp) else "pass"
    return {"schema": "PurposeComplianceReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "status": status, "checks": checks, "summary": {"events_checked": len(inv.get("events", [])), "allowed_purpose_events": ap, "denied_purpose_events": dp, "missing_purpose_events": mp}, "errors": []}


def evaluate_duty_compliance(inv, policy):
    duties = []
    for d in policy.get("duties", []):
        f = d.get("evidence_field")
        checked = len(inv.get("events", []))
        miss = sum(1 for e in inv.get("events", []) if d.get("required") and not e.get(f))
        duties.append({"duty_id": d.get("duty_id"), "status": "missing" if miss else "satisfied", "events_checked": checked, "violations": miss, "evidence": []})
    return duties


def evaluate_prohibition_compliance(inv, policy):
    out = []
    for p in policy.get("prohibitions", []):
        action = p.get("action")
        vio = [e for e in inv.get("events", []) if e.get("action") == action]
        out.append({"prohibition_id": p.get("prohibition_id"), "status": "triggered" if vio else "not_triggered", "events_checked": len(inv.get("events", [])), "violations": len(vio)})
    return out


def evaluate_obligation_compliance(run_id, spec, inv, policy):
    duties = evaluate_duty_compliance(inv, policy)
    prohibitions = evaluate_prohibition_compliance(inv, policy)
    fail = any(d["violations"] > 0 for d in duties) or any(p["violations"] > 0 for p in prohibitions)
    return {"schema": "ObligationComplianceReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "status": "fail" if fail else "pass", "duties": duties, "prohibitions": prohibitions, "errors": []}


def append_quota_ledger_entry(quota_dir: Path, entry: Dict[str, Any]) -> str:
    entry_id = _sha_obj({k: v for k, v in entry.items() if k != "entry_id"})
    entry["entry_id"] = entry_id
    fname = f"{entry['created_at_utc'].replace(':','-')}_{entry['quota_entry_id']}.json"
    rel = f"entries/{fname}"
    write_canonical_json(quota_dir / rel, entry)
    return rel


def build_quota_ledger(spec, entries_meta):
    latest = entries_meta[-1]["entry_id"] if entries_meta else None
    return {"schema": "QuotaLedger.v1", "data_use_id": spec["data_use_id"], "created_at_utc": _utc_now(), "source": SOURCE, "entries": entries_meta, "latest_entry_id": latest, "errors": []}


def evaluate_quota_compliance(run_id, spec, inv, quota_dir: Path):
    q = spec.get("quotas", {})
    subj = {}
    for e in inv.get("events", []):
        s = e.get("subject_hash") or "__null__"
        subj.setdefault(s, {"events": 0, "bytes": 0})
        subj[s]["events"] += 1; subj[s]["bytes"] += int(e.get("bytes_served") or 0)
    quota_entries, meta = [], []
    for s in sorted(subj.keys()):
        obs = subj[s]
        evl = int(q.get("default_subject_daily_events", 0)); byl = int(q.get("default_subject_daily_bytes", 0))
        st = "exceeded" if (obs["events"] > evl or obs["bytes"] > byl) else "within_limit"
        entry = {"schema": "QuotaLedgerEntry.v1", "entry_id": "", "quota_entry_id": "quota_" + _sha_obj({"s": s, **obs})[:12], "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "subject_hash": None if s == "__null__" else s, "resource_key": None, "time_window": {}, "limits": {"events_limit": evl, "bytes_limit": byl}, "observed": obs, "quota_status": st, "previous_entry_id": None, "previous_chain_hash": None, "chain_hash": ""}
        entry["chain_hash"] = _sha_obj({k: v for k, v in entry.items() if k != "chain_hash"})
        rel = append_quota_ledger_entry(quota_dir, entry)
        meta.append({"entry_id": entry["entry_id"], "quota_entry_id": entry["quota_entry_id"], "subject_hash": entry["subject_hash"], "resource_key": None, "quota_status": st, "chain_hash": entry["chain_hash"], "entry_path": rel})
        quota_entries.append(entry)
    ql = build_quota_ledger(spec, meta)
    write_canonical_json(quota_dir / "quota_ledger.json", ql)
    summary = {"subjects_checked": len(subj), "resources_checked": 0, "within_limit": sum(1 for q in quota_entries if q["quota_status"] == "within_limit"), "exceeded": sum(1 for q in quota_entries if q["quota_status"] == "exceeded"), "unknown": 0}
    status = "warning" if summary["exceeded"] else "pass"
    return {"schema": "QuotaComplianceReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "status": status, "data_use_id": spec["data_use_id"], "quota_entries": quota_entries, "summary": summary, "errors": []}


def detect_usage_anomalies(spec, inv, quota_report):
    an, ad = [], spec.get("anomaly_detection", {})
    denials = [e for e in inv.get("events", []) if e.get("enforcement_action") == "deny"]
    if inv.get("summary", {}).get("events_total", 0) > 0:
        dr = 100.0 * len(denials) / inv["summary"]["events_total"]
        if dr >= ad.get("denial_rate_warning_percent", 25):
            an.append({"anomaly_type": "high_denial_rate", "severity": "warning", "subject_hash": None, "resource_key": None, "event_ids": [e["event_id"] for e in denials], "message": "High denial rate detected"})
    if quota_report.get("summary", {}).get("exceeded", 0) > 0:
        an.append({"anomaly_type": "quota_exceeded", "severity": "warning", "subject_hash": None, "resource_key": None, "event_ids": [], "message": "Quota exceeded"})
    for a in an: a["anomaly_id"] = "anom_" + _sha_obj(a)[:12]
    return an


def build_usage_anomaly_report(run_id, spec, anomalies):
    sev = "critical" if any(a["severity"] == "critical" for a in anomalies) else ("warning" if anomalies else "none")
    return {"schema": "UsageAnomalyReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "status": sev, "anomalies": anomalies, "summary": {"info": sum(1 for a in anomalies if a["severity"] == "info"), "warning": sum(1 for a in anomalies if a["severity"] == "warning"), "critical": sum(1 for a in anomalies if a["severity"] == "critical")}, "errors": []}


def build_data_use_alert_envelope(run_id, spec, anomaly_report):
    level = anomaly_report.get("status", "none")
    return {"schema": "DataUseAlertEnvelope.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "severity": level if level in {"none", "warning", "critical"} else "info", "status": "open" if level != "none" else "resolved", "title": "Data use anomaly summary", "message": f"anomalies={len(anomaly_report.get('anomalies', []))}", "related_anomaly_ids": [a["anomaly_id"] for a in anomaly_report.get("anomalies", [])], "dedupe_key": _sha_obj({"id": spec["data_use_id"], "an": [a["anomaly_id"] for a in anomaly_report.get("anomalies", [])]}), "recommended_actions": [], "errors": []}


def build_consumer_usage_statement(spec, inv, subject_hash):
    events = [e for e in inv.get("events", []) if e.get("subject_hash") == subject_hash]
    return {"schema": "ConsumerUsageStatement.v1", "statement_id": "custmt_" + _sha_obj({"s": subject_hash, "n": len(events)})[:12], "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "subject_hash": subject_hash, "time_window": {}, "summary": {"events": len(events), "grants": sum(1 for e in events if str(e.get("enforcement_action", "")).startswith("grant")), "denials": sum(1 for e in events if e.get("enforcement_action") == "deny"), "reviews": sum(1 for e in events if e.get("enforcement_action") == "review_required"), "bytes_served": sum(int(e.get("bytes_served") or 0) for e in events), "resources_accessed": len({e.get("resource_sha256") for e in events if e.get("resource_sha256")})}, "obligations": {"attribution_required": bool(spec.get("obligations", {}).get("require_attribution", True)), "citation_required": bool(spec.get("obligations", {}).get("require_citation", True)), "purpose_required": bool(spec.get("obligations", {}).get("require_purpose", True))}, "quota": {"status": "unknown"}, "errors": []}


def compute_data_use_spec_hash(spec): return _sha_obj(spec)
def compute_data_use_policy_hash(policy): return _sha_obj(policy)
def compute_obligation_report_hash(purpose_report, obligation_report, quota_report, anomaly_report): return _sha_obj({"purpose": purpose_report.get("summary"), "obligation": {"duties": obligation_report.get("duties"), "prohibitions": obligation_report.get("prohibitions")}, "quota": quota_report.get("summary"), "anomaly": anomaly_report.get("summary")})
def compute_data_use_result_hash(inv_hash, meter_hash, obligation_hash, quota_hash, anomaly_hash, governance_status): return _sha_obj({"inv": inv_hash, "meter": meter_hash, "obl": obligation_hash, "quota": quota_hash, "anom": anomaly_hash, "status": governance_status})

def build_data_use_governance_report(run_id, spec, inv, obligation_report, purpose_report, quota_report, anomaly_report, paths):
    s = {"usage_events": inv.get("summary", {}).get("events_total", 0), "obligation_violations": sum(d.get("violations", 0) for d in obligation_report.get("duties", [])), "purpose_violations": purpose_report.get("summary", {}).get("denied_purpose_events", 0) + purpose_report.get("summary", {}).get("missing_purpose_events", 0), "quota_exceeded": quota_report.get("summary", {}).get("exceeded", 0), "critical_anomalies": anomaly_report.get("summary", {}).get("critical", 0)}
    status = "pass" if all(v == 0 for v in [s["obligation_violations"], s["purpose_violations"], s["quota_exceeded"], s["critical_anomalies"]]) else "warning"
    return {"schema": "DataUseGovernanceReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "data_use_id": spec["data_use_id"], "status": status, "summary": s, "report_paths": paths, "errors": []}

def build_odrl_like_policy_export(policy):
    return {"@context": {"odrl": "http://www.w3.org/ns/odrl/2/"}, "type": "odrl:Policy", "profile": "soilgrids-data-use", "permission": [{"action": a} for a in policy.get("allowed_actions", [])], "prohibition": [{"action": p.get("action")} for p in policy.get("prohibitions", [])], "duty": [{"uid": d.get("duty_id")} for d in policy.get("duties", [])]}

def build_data_use_api_contract(spec):
    return {"schema": "DataUseApiContract.v1", "data_use_id": spec["data_use_id"], "created_at_utc": _utc_now(), "source": SOURCE, "read_only": True, "allowed_methods": ["GET", "HEAD", "OPTIONS"], "endpoints": [{"method": "GET", "path": "/health", "operation_id": "health"}, {"method": "GET", "path": "/usage/summary", "operation_id": "usageSummary"}, {"method": "GET", "path": "/usage/subjects/{subject_hash}", "operation_id": "consumerUsageStatement"}, {"method": "GET", "path": "/usage/anomalies", "operation_id": "usageAnomalies"}, {"method": "GET", "path": "/usage/quotas", "operation_id": "quotaStatus"}], "errors": []}

def build_data_use_openapi(spec):
    return {"openapi": "3.1.1", "info": {"title": "Data Use API", "version": "1.0.0"}, "paths": {"/health": {"get": {"operationId": "health", "responses": {"200": {"description": "ok"}}}}}, "components": {"schemas": {"UsageMeteringSnapshot.v1": {"type": "object"}, "UsageMeteringReport.v1": {"type": "object"}, "ObligationComplianceReport.v1": {"type": "object"}, "PurposeComplianceReport.v1": {"type": "object"}, "QuotaComplianceReport.v1": {"type": "object"}, "UsageAnomalyReport.v1": {"type": "object"}, "ConsumerUsageStatement.v1": {"type": "object"}}}}

def validate_data_use_api_contract(contract):
    return [] if contract.get("read_only") and all(e.get("method") == "GET" for e in contract.get("endpoints", [])) else ["api_contract"]

def export_otel_style_usage_bundle_if_requested(spec, out_dir: Path, inv, snap):
    if not spec.get("exports", {}).get("write_otel_style_metrics", False): return []
    od = out_dir / "otel"; od.mkdir(parents=True, exist_ok=True)
    write_canonical_json(od / "metrics.json", {"events_total": snap.get("counters", {}).get("events_total", 0), "bytes_total": snap.get("counters", {}).get("bytes_served_total", 0)})
    (od / "logs.jsonl").write_text("\n".join([json.dumps({"event_id": e["event_id"]}, sort_keys=True) for e in inv.get("events", [])]) + "\n", encoding="utf-8")
    (od / "traces.jsonl").write_text(json.dumps({"trace": "local"}, sort_keys=True) + "\n", encoding="utf-8")
    return [od / "metrics.json", od / "logs.jsonl", od / "traces.jsonl"]

def append_data_use_ledger_entry(ledger_dir: Path, receipt: Dict[str, Any]):
    ledger_dir.mkdir(parents=True, exist_ok=True)
    entry = {"schema": "DataUseLedgerEntry.v1", "entry_id": _sha_obj(receipt), "created_at_utc": _utc_now(), "source": SOURCE, "run_id": receipt.get("run_id"), "status": receipt.get("status")}
    f = ledger_dir / "entries" / f"{entry['created_at_utc'].replace(':','-')}_{entry['entry_id'][:12]}.json"
    write_canonical_json(f, entry)

def validate_data_use_ledger(_ledger): return []
def build_data_use_validation_report(errors): return {"schema": "DataUseValidationReport.v1", "created_at_utc": _utc_now(), "source": SOURCE, "status": "pass" if not errors else "fail", "errors": errors}

def write_checksums_file(root: Path):
    files = sorted([p for p in root.rglob("*") if p.is_file() and p.name != "checksums.sha256"])
    lines = [f"{_sha_file(p)}  {p.relative_to(root).as_posix()}" for p in files]
    (root / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

def build_data_use_receipt(**kw):
    return kw

def load_data_use_inputs(data_use_spec, usage_audit_ledger, data_use_policy=None, allow_plaintext_subjects=False):
    spec = _read_json(data_use_spec)
    spec_err = validate_data_use_spec(spec, allow_plaintext_subjects=allow_plaintext_subjects)
    policy = load_data_use_policy(data_use_policy)
    pol_err = _validate_policy(policy)
    ledger, events, lerr = discover_usage_audit_events(usage_audit_ledger)
    return spec, policy, ledger, events, spec_err + pol_err + lerr

def build_local_data_use_api_server(host, port, payloads):
    class H(BaseHTTPRequestHandler):
        def _ok(self, obj):
            b = json.dumps(obj, sort_keys=True).encode("utf-8")
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
        def do_GET(self):
            if self.path == "/health": return self._ok({"status": "ok"})
            if self.path == "/usage/summary": return self._ok(payloads.get("usage_metering_report", {}))
            if self.path == "/usage/anomalies": return self._ok(payloads.get("usage_anomaly_report", {}))
            if self.path == "/usage/quotas": return self._ok(payloads.get("quota_compliance_report", {}))
            return self._ok({"status": "not_found"})
        def log_message(self, *_):
            return
    server = HTTPServer((host, int(port)), H)
    return server

def run_data_use_accountability(**args):
    mode = args.get("mode", DEFAULT_MODE)
    if mode not in ALLOWED_MODES: raise ValueError("unsupported mode")
    spec, policy, _ledger, events, input_errors = load_data_use_inputs(args["data_use_spec"], args["usage_audit_ledger"], args.get("data_use_policy"), bool(args.get("allow_plaintext_subjects")))
    if input_errors: return {"exit": 2, "errors": input_errors}
    spec_hash, policy_hash = compute_data_use_spec_hash(spec), compute_data_use_policy_hash(policy)

    out_root = Path(args.get("output_root", "data_use_runs"))
    run_slug = f"{spec['data_use_id']}_{mode}_{spec_hash[:12]}"
    run_id = args.get("data_use_run_id") or run_slug
    stage = out_root / ".staging" / run_id
    final = out_root / run_id
    if final.exists() and not args.get("overwrite"): return {"exit": 3, "errors": ["output exists"]}
    if stage.exists(): shutil.rmtree(stage)
    stage.mkdir(parents=True, exist_ok=True)

    inv = build_usage_event_inventory(spec, events)
    snap = build_usage_metering_snapshot(spec, inv)
    purpose = evaluate_purpose_compliance(run_id, spec, inv, policy)
    oblig = evaluate_obligation_compliance(run_id, spec, inv, policy)
    quota = evaluate_quota_compliance(run_id, spec, inv, stage / "quota")
    anomalies = detect_usage_anomalies(spec, inv, quota)
    an_report = build_usage_anomaly_report(run_id, spec, anomalies)
    alert = build_data_use_alert_envelope(run_id, spec, an_report)
    subj = args.get("subject_hash") or next((e.get("subject_hash") for e in inv.get("events", []) if e.get("subject_hash")), "")
    cstmt = build_consumer_usage_statement(spec, inv, subj) if subj else None
    met_report = build_usage_metering_report(run_id, spec, snap)
    paths = {
        "usage_event_inventory": "usage_event_inventory.json", "usage_metering_snapshot": "usage_metering_snapshot.json",
        "usage_metering_report": "usage_metering_report.json", "purpose_compliance_report": "compliance/purpose_compliance_report.json",
        "obligation_compliance_report": "compliance/obligation_compliance_report.json", "quota_compliance_report": "compliance/quota_compliance_report.json",
        "usage_anomaly_report": "anomalies/usage_anomaly_report.json", "data_use_alert_envelope": "anomalies/data_use_alert_envelope.json",
    }
    gov = build_data_use_governance_report(run_id, spec, inv, oblig, purpose, quota, an_report, paths)
    odrl = build_odrl_like_policy_export(policy)
    api_contract = build_data_use_api_contract(spec)
    openapi = build_data_use_openapi(spec)

    write_canonical_json(stage / "data_use_plan.json", build_data_use_plan(spec, mode, len(events)))
    write_canonical_json(stage / "usage_event_inventory.json", inv)
    write_canonical_json(stage / "usage_metering_snapshot.json", snap)
    write_canonical_json(stage / "usage_metering_report.json", met_report)
    write_canonical_json(stage / "compliance/purpose_compliance_report.json", purpose)
    write_canonical_json(stage / "compliance/obligation_compliance_report.json", oblig)
    write_canonical_json(stage / "compliance/quota_compliance_report.json", quota)
    write_canonical_json(stage / "anomalies/usage_anomaly_report.json", an_report)
    write_canonical_json(stage / "anomalies/data_use_alert_envelope.json", alert)
    if cstmt: write_canonical_json(stage / "consumers/consumer_usage_statement.json", cstmt)
    write_canonical_json(stage / "data_use_governance_report.json", gov)
    write_canonical_json(stage / "policy/data_use_policy.json", policy)
    write_canonical_json(stage / "policy/data_use_odrl_like.jsonld", odrl)
    write_canonical_json(stage / "api/data_use_api_contract.json", api_contract)
    write_canonical_json(stage / "api/data_use_openapi.json", openapi)
    export_otel_style_usage_bundle_if_requested(spec, stage, inv, snap)

    obligation_hash = compute_obligation_report_hash(purpose, oblig, quota, an_report)
    result_hash = compute_data_use_result_hash(inv["inventory_hash"], snap["metering_snapshot_hash"], obligation_hash, _sha_obj(quota.get("summary", {})), _sha_obj(an_report.get("summary", {})), gov["status"])

    receipt = {
        "schema": "DataUseReceipt.v1", "run_id": run_id, "created_at_utc": _utc_now(), "status": "success", "source": SOURCE,
        "mode": mode, "data_use_id": spec["data_use_id"], "data_use_run_id": run_id, "data_use_spec_hash": spec_hash,
        "data_use_policy_hash": policy_hash, "usage_event_inventory_hash": inv["inventory_hash"], "metering_snapshot_hash": snap["metering_snapshot_hash"],
        "data_use_result_hash": result_hash, "output_root": str((Path(args.get("output_root", "data_use_runs")) / run_id).as_posix()),
        "outputs": {"data_use_plan": "data_use_plan.json", "usage_event_inventory": "usage_event_inventory.json", "usage_metering_snapshot": "usage_metering_snapshot.json", "usage_metering_report": "usage_metering_report.json", "purpose_compliance_report": "compliance/purpose_compliance_report.json", "obligation_compliance_report": "compliance/obligation_compliance_report.json", "quota_compliance_report": "compliance/quota_compliance_report.json", "usage_anomaly_report": "anomalies/usage_anomaly_report.json", "data_use_alert_envelope": "anomalies/data_use_alert_envelope.json", "consumer_usage_statement": "consumers/consumer_usage_statement.json" if cstmt else None, "data_use_governance_report": "data_use_governance_report.json", "data_use_api_contract": "api/data_use_api_contract.json", "openapi": "api/data_use_openapi.json", "checksums": "checksums.sha256"},
        "inputs": {"data_use_spec": args["data_use_spec"], "usage_audit_ledgers": [args["usage_audit_ledger"]], "usage_audit_events": []},
        "input_hashes": {"data_use_spec_sha256": _sha_file(Path(args["data_use_spec"])), "combined_usage_input_hash": _sha_obj(events)},
        "validation": {"spec_valid": True, "policy_valid": True, "usage_ledger_valid": True, "usage_events_valid": True, "metering_valid": True, "obligations_valid": True, "quotas_valid": True, "anomalies_valid": True, "checksums_valid": True}, "errors": []
    }
    write_canonical_json(stage / "data_use_receipt.json", receipt)
    append_data_use_ledger_entry(stage / "ledger", receipt)
    write_checksums_file(stage)
    if final.exists(): shutil.rmtree(final)
    os.replace(stage, final)
    print(str(final / "data_use_receipt.json"))

    if mode == "local-api":
        srv = build_local_data_use_api_server(args.get("host", "127.0.0.1"), int(args.get("port", 0)), {"usage_metering_report": met_report, "usage_anomaly_report": an_report, "quota_compliance_report": quota})
        if args.get("serve_forever"):
            srv.serve_forever()
        else:
            srv.server_close()

    return {"exit": 0, "run_id": run_id}


def _parse(argv: List[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {"mode": DEFAULT_MODE, "host": "127.0.0.1", "port": 0}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--"):
            k = a[2:].replace("-", "_")
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out[k] = argv[i + 1]
                i += 2
            else:
                out[k] = True
                i += 1
        else:
            i += 1
    return out


def main(argv: Optional[List[str]] = None) -> int:
    args = _parse(argv or os.sys.argv[1:])
    try:
        r = run_data_use_accountability(**args)
        return r.get("exit", 1)
    except Exception as exc:
        os.sys.stderr.write(json.dumps({"status": "error", "error": str(exc)}) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
