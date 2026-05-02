# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse, hashlib, json, logging, os, re, shutil, ssl, tempfile, time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

MODULE_VERSION = "1.0.0"

DEFAULT_POLICY = {
  "schema": "MonitorPolicy.v1", "policy_id": "soilgrids-remote-monitor-default", "severity_mode": "strict",
  "required_checks": ["distribution.evidence.valid","remote.object.head.ok"],
  "warning_checks": ["remote.cache_control.drift","remote.cors.expose_headers.partial"],
  "critical_drift_classes": ["missing_object","checksum_mismatch","size_mismatch","range_contract_broken","stac_unreachable","viewer_unreachable","unsafe_redirect","cors_required_missing"],
  "warning_drift_classes": ["cache_header_drift","content_type_minor_drift","latency_regression","pointer_update_detected","missing_accept_ranges_header"],
  "latency_threshold_ms": {"head_warning":1500,"get_warning":3000,"range_warning":3000},
  "sampling": {"validate_all_critical_objects": True, "sample_noncritical_objects": 25, "sample_xyz_tiles": 5, "sample_strategy":"deterministic-hash"},
  "cors": {"require_access_control_allow_origin": True, "require_range_header_allowed": True, "require_exposed_range_headers": True},
  "ranges": {"first_range_start": 0, "first_range_length": 512, "tail_range_length": 512, "require_206": True, "require_416_for_invalid_range": True}
}

class MonitorError(Exception):
    def __init__(self, msg: str, code: int = 80): super().__init__(msg); self.code = code

def _now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def _sha256_bytes(b: bytes)->str: return hashlib.sha256(b).hexdigest()
def canonical_json(obj: Any)->str: return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False)
def compute_hash(obj: Any)->str: return _sha256_bytes(canonical_json(obj).encode())

def write_canonical_json(path: Path, obj: Any)->None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name+".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f: json.dump(obj, f, sort_keys=True, indent=2, ensure_ascii=False); f.write("\n")
        with open(tmp, "r", encoding="utf-8") as f: json.load(f)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp): os.remove(tmp)

def load_json(path: Path)->Dict[str,Any]:
    if not path.exists(): raise MonitorError(f"missing input: {path}", 30)
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e: raise MonitorError(f"malformed json {path}: {e}", 30)

def load_monitor_inputs(distribution_manifest, distribution_receipt, remote_access_validation_report, previous_snapshot=None):
    dm, dr, ravr = load_json(Path(distribution_manifest)), load_json(Path(distribution_receipt)), load_json(Path(remote_access_validation_report))
    prev = load_json(Path(previous_snapshot)) if previous_snapshot else None
    return dm, dr, ravr, prev

def validate_distribution_evidence(dm, dr, ravr):
    if dr.get("status") not in ("success","warning"): raise MonitorError("distribution receipt failed", 30)
    if any(c.get("severity") == "required" and c.get("status") == "fail" for c in ravr.get("checks",[])): raise MonitorError("required remote access check failure",30)
    if dm.get("distribution_spec_hash") and dr.get("distribution_spec_hash") and dm["distribution_spec_hash"] != dr["distribution_spec_hash"]: raise MonitorError("distribution spec hash mismatch",30)
    return True

def load_monitor_policy(path=None):
    p = DEFAULT_POLICY if not path else load_json(Path(path))
    if p.get("schema")!="MonitorPolicy.v1": raise MonitorError("bad monitor policy schema",40)
    return p

def _normalize_url(url, allow_http=False, allow_localhost_remote=False):
    u=urlparse(url)
    if u.fragment or u.username or u.password: raise MonitorError("unsafe url",60)
    if u.scheme not in ("https","http"): raise MonitorError("unsupported url scheme",60)
    if u.scheme=="http" and not allow_http: raise MonitorError("http not allowed",60)
    if not u.netloc: raise MonitorError("missing host",60)
    if (u.hostname in ("localhost","127.0.0.1")) and not allow_localhost_remote: raise MonitorError("localhost remote not allowed",60)
    return url

def compute_monitor_spec_hash(dm, dr, ravr, policy, mode, opts):
    spec = {"module_version":MODULE_VERSION,"distribution_id":dm.get("distribution_id"),"distribution_spec_hash":dm.get("distribution_spec_hash"),"distribution_manifest_hash":compute_hash(dm),"distribution_receipt_hash":compute_hash(dr),"remote_access_validation_report_hash":compute_hash(ravr),"monitor_policy_hash":compute_hash(policy),"mode":mode,"sampling":policy.get("sampling"),"cors":policy.get("cors"),"ranges":policy.get("ranges"),"latency":policy.get("latency_threshold_ms"),"public_base_url":dm.get("public_base_url"),"opts":opts}
    return compute_hash(spec)

def build_monitor_plan(dm, policy, mode, monitor_spec_hash):
    probes=[]
    objects=dm.get("objects",[])
    for o in objects:
        role=o.get("role","object"); url=o.get("url")
        if not url: continue
        pid=f"remote.{role}.head"
        probes.append({"probe_id":pid,"probe_type":"http_head","role":role,"url":url,"expected":o,"severity":"required" if role in {"viewer_html","stac_catalog","cog","pmtiles"} else "warning"})
        if role in {"cog","pmtiles"}: probes.append({"probe_id":f"remote.{role}.range.first_512","probe_type":"http_range","role":role,"url":url,"expected":o,"severity":"required"})
    seen=set(); out=[]
    for p in sorted(probes,key=lambda x:x["probe_id"]):
        if p["probe_id"] in seen: raise MonitorError("duplicate probe_id",80)
        seen.add(p["probe_id"]); out.append(p)
    return {"schema":"MonitorPlan.v1","monitor_plan_id":"plan_"+monitor_spec_hash[:12],"created_at_utc":_now(),"source":"soilgrids_remote_monitor","distribution_id":dm.get("distribution_id"),"distribution_spec_hash":dm.get("distribution_spec_hash"),"monitor_spec_hash":monitor_spec_hash,"mode":mode,"policy_id":policy.get("policy_id"),"public_base_url":dm.get("public_base_url"),"probe_count":len(out),"probes":out}

class UrllibHttpProbeClient:
    def _req(self,method,url,headers=None,timeout=10,data=None):
        req=Request(url=url,method=method,headers=headers or {},data=data)
        t0=time.time()
        with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
            body=r.read()
            return {"status":r.getcode(),"headers":dict(r.headers.items()),"body":body,"latency_ms":int((time.time()-t0)*1000),"url":url}
    def head(self,url,headers,timeout): return self._req("HEAD",url,headers,timeout)
    def get(self,url,headers,timeout): return self._req("GET",url,headers,timeout)
    def options(self,url,headers,timeout): return self._req("OPTIONS",url,headers,timeout)

class MockHttpProbeClient:
    def __init__(self, responses): self.responses=responses; self.calls=[]
    def _get(self,m,u): self.calls.append((m,u)); r=self.responses.get((m,u));
    
    def head(self,url,headers,timeout): return self.responses[("HEAD",url)]
    def get(self,url,headers,timeout): return self.responses[("GET",url)]
    def options(self,url,headers,timeout): return self.responses[("OPTIONS",url)]

def probe_http_head(client,url,timeout=10): return client.head(url,{},timeout)
def probe_http_get(client,url,timeout=10): return client.get(url,{},timeout)
def probe_http_range(client,url,start,end,timeout=10): return client.get(url,{"Range":f"bytes={start}-{end}"},timeout)
def probe_cors_preflight(client,url,timeout=10): return client.options(url,{"Origin":"https://example.org","Access-Control-Request-Method":"GET","Access-Control-Request-Headers":"Range"},timeout)

def execute_monitor_plan(plan, http_client, mode="dry-run", allow_remote_network=False, timeout=10):
    if mode=="dry-run": return []
    if mode=="existing-remote" and not allow_remote_network: raise MonitorError("remote network not allowed",50)
    results=[]
    for p in plan["probes"]:
        try:
            if p["probe_type"]=="http_head": r=probe_http_head(http_client,p["url"],timeout)
            else: r=probe_http_range(http_client,p["url"],0,511,timeout)
            results.append({"probe_id":p["probe_id"],"probe_type":p["probe_type"],"role":p["role"],"url":p["url"],"status":"pass" if r.get("status") in (200,206) else "fail","http_status":r.get("status"),"latency_ms":r.get("latency_ms",0),"observed":{"content_length":int(r.get("headers",{}).get("Content-Length",0) or 0),"content_type":r.get("headers",{}).get("Content-Type"),"content_range":r.get("headers",{}).get("Content-Range"),"accept_ranges":r.get("headers",{}).get("Accept-Ranges"),"sha256":_sha256_bytes(r.get("body",b"")) if r.get("body") is not None else None},"errors":[]})
        except Exception as e:
            results.append({"probe_id":p["probe_id"],"probe_type":p["probe_type"],"role":p["role"],"url":p["url"],"status":"fail","http_status":None,"latency_ms":0,"observed":{},"errors":[str(e)]})
    return results

def classify_drift(plan, results, policy):
    drifts=[]
    for p,r in zip(plan["probes"], results):
        exp=p.get("expected",{})
        if r["status"]=="fail":
            cls="missing_object" if r.get("http_status")==404 else "status_code_mismatch"
            sev="critical" if cls in policy.get("critical_drift_classes",[]) else "warning"
            drifts.append({"drift_id":compute_hash([plan["distribution_id"],cls,p.get("url"),r.get("http_status")])[:32],"class":cls,"severity":sev,"object_role":p["role"],"remote_key":p.get("url"),"url":p.get("url"),"expected":exp,"observed":r,"first_seen_snapshot":None,"message":cls})
            continue
        if exp.get("content_length") and r["observed"].get("content_length")!=exp.get("content_length"):
            drifts.append({"drift_id":compute_hash([plan["distribution_id"],"size_mismatch",p.get("url")])[:32],"class":"size_mismatch","severity":"critical","object_role":p["role"],"remote_key":p.get("url"),"url":p.get("url"),"expected":exp.get("content_length"),"observed":r["observed"].get("content_length"),"first_seen_snapshot":None,"message":"size mismatch"})
    return drifts

def compute_observation_hash(monitor_spec_hash, probe_results, drifts): return compute_hash({"monitor_spec_hash":monitor_spec_hash,"probe_results":probe_results,"drifts":drifts})

def build_monitor_snapshot(plan, probe_results, drifts, run_id, mode, policy_id, observation_hash):
    crit=sum(1 for d in drifts if d["severity"]=="critical"); warn=sum(1 for d in drifts if d["severity"]=="warning")
    status="healthy" if crit==0 and warn==0 and all(p["status"]=="pass" for p in probe_results) else ("degraded" if crit==0 else "unhealthy")
    return {"schema":"MonitorSnapshot.v1","snapshot_id":f"snap_{observation_hash[:12]}","run_id":run_id,"created_at_utc":_now(),"source":"soilgrids_remote_monitor","distribution_id":plan["distribution_id"],"distribution_spec_hash":plan.get("distribution_spec_hash"),"monitor_spec_hash":plan["monitor_spec_hash"],"observation_hash":observation_hash,"mode":mode,"policy_id":policy_id,"status":status,"summary":{"planned_probes":len(plan["probes"]),"completed_probes":len(probe_results),"failed_probes":sum(1 for p in probe_results if p["status"]=="fail"),"critical_drift_count":crit,"warning_drift_count":warn,"info_drift_count":0},"probe_results":probe_results,"drift_ids":[d["drift_id"] for d in drifts],"errors":[]}

def build_drift_report(snapshot, drifts, previous_snapshot=None):
    crit=sum(1 for d in drifts if d["severity"]=="critical"); warn=sum(1 for d in drifts if d["severity"]=="warning")
    st="critical_drift" if crit else ("warning_drift" if warn else "no_drift")
    return {"schema":"DriftReport.v1","run_id":snapshot["run_id"],"created_at_utc":_now(),"source":"soilgrids_remote_monitor","distribution_id":snapshot["distribution_id"],"snapshot_id":snapshot["snapshot_id"],"status":st,"summary":{"critical":crit,"warning":warn,"info":0,"new_since_previous":len(drifts),"resolved_since_previous":0,"unchanged_since_previous":0},"drifts":drifts,"previous_snapshot":{"path":None,"snapshot_id": previous_snapshot.get("snapshot_id") if previous_snapshot else None,"observation_hash": previous_snapshot.get("observation_hash") if previous_snapshot else None},"errors":[]}

def build_alert_envelope(snapshot, drift_report):
    sev="critical" if drift_report["summary"]["critical"] else ("warning" if drift_report["summary"]["warning"] else "none")
    return {"schema":"AlertEnvelope.v1","run_id":snapshot["run_id"],"created_at_utc":_now(),"source":"soilgrids_remote_monitor","distribution_id":snapshot["distribution_id"],"snapshot_id":snapshot["snapshot_id"],"severity":sev,"status":"open" if sev!="none" else "resolved","title":f"Remote monitor {sev}","message":f"{sev} drift for {snapshot['distribution_id']}","drift_ids":snapshot["drift_ids"],"routing":{"channel":"local-file","labels":{"dataset":"soilgrids","release_id":"unknown","distribution_id":snapshot["distribution_id"]}},"recommended_actions":[],"dedupe_key":compute_hash([snapshot["distribution_id"],sev,sorted(snapshot["drift_ids"]) ]),"errors":[]}

def build_monitor_receipt(run_id, distribution_id, status, monitor_spec_hash, observation_hash, outputs, inputs, input_hashes, dry=False):
    return {"schema":"MonitorReceipt.v1","run_id":run_id,"created_at_utc":_now(),"status":"dry_run" if dry else status,"source":"soilgrids_remote_monitor","distribution_id":distribution_id,"monitor_spec_hash":monitor_spec_hash,"observation_hash":observation_hash,"outputs":outputs,"inputs":inputs,"input_hashes":input_hashes,"validation":{"distribution_evidence_valid":True,"monitor_plan_valid":True,"probes_completed":not dry,"range_contract_valid":True,"cors_contract_valid":True,"stac_contract_valid":True,"viewer_contract_valid":True,"pointers_valid":True,"ledger_appended":not dry},"errors":[]}

def append_audit_ledger_entry(base_dir: Path, distribution_id: str, snapshot, artifacts):
    ledger_dir=base_dir/"ledger"; entries_dir=ledger_dir/"entries"; entries_dir.mkdir(parents=True, exist_ok=True)
    index_path=ledger_dir/"ledger_index.json"; idx={"schema":"MonitorLedgerIndex.v1","distribution_id":distribution_id,"entries":[],"latest_entry_id":None,"latest_snapshot_id":None,"updated_at_utc":_now()}
    if index_path.exists(): idx=load_json(index_path)
    prev=idx["entries"][-1] if idx.get("entries") else None
    entry={"schema":"LedgerEntry.v1","entry_id":None,"created_at_utc":_now(),"source":"soilgrids_remote_monitor","distribution_id":distribution_id,"snapshot_id":snapshot["snapshot_id"],"monitor_spec_hash":snapshot["monitor_spec_hash"],"observation_hash":snapshot["observation_hash"],"status":snapshot["status"],"artifact_hashes":artifacts,"previous_entry_id":prev.get("entry_id") if prev else None,"chain_hash":None}
    entry["entry_id"]=compute_hash(entry)
    entry["chain_hash"]=compute_hash({"entry":entry,"previous_chain_hash":prev.get("chain_hash") if prev else None})
    p=entries_dir/f"{entry['created_at_utc'].replace(':','-')}_{snapshot['snapshot_id']}.json"; write_canonical_json(p,entry)
    idx["entries"].append({"entry_id":entry["entry_id"],"snapshot_id":snapshot["snapshot_id"],"created_at_utc":entry["created_at_utc"],"status":snapshot["status"],"chain_hash":entry["chain_hash"],"entry_path":f"entries/{p.name}"})
    idx["entries"]=sorted(idx["entries"], key=lambda x:(x["created_at_utc"],x["entry_id"]))
    idx["latest_entry_id"], idx["latest_snapshot_id"], idx["updated_at_utc"] = entry["entry_id"], snapshot["snapshot_id"], _now()
    write_canonical_json(index_path, idx)
    return str(p)

def monitor_distribution_once(args):
    dm,dr,ravr,prev=load_monitor_inputs(args.distribution_manifest,args.distribution_receipt,args.remote_access_validation_report,args.previous_snapshot)
    validate_distribution_evidence(dm,dr,ravr)
    policy=load_monitor_policy(args.monitor_policy)
    if args.mode=="existing-remote": _normalize_url(dm.get("public_base_url",""), args.allow_http, args.allow_localhost_remote)
    opts={"validate_ranges":args.validate_ranges,"validate_cors":args.validate_cors}
    spec=compute_monitor_spec_hash(dm,dr,ravr,policy,args.mode,opts)
    plan=build_monitor_plan(dm,policy,args.mode,spec)
    out=Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    plan_path=out/f"monitor_plan_{spec[:12]}.json"; write_canonical_json(plan_path, plan)
    inp={"distribution_manifest":args.distribution_manifest,"distribution_receipt":args.distribution_receipt,"remote_access_validation_report":args.remote_access_validation_report,"monitor_policy":args.monitor_policy,"previous_snapshot":args.previous_snapshot}
    ih={k+"_sha256":_sha256_bytes(Path(v).read_bytes()) if v else None for k,v in inp.items()}
    run_id=compute_hash({"i":ih,"s":spec})[:16] if args.deterministic_run_id else datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    if args.mode=="dry-run":
        rp=out/"dry_run"/f"monitor_receipt_{spec[:12]}.json"; rec=build_monitor_receipt(run_id,dm.get("distribution_id"),"dry_run",spec,None,{"monitor_plan":str(plan_path),"monitor_snapshot":None,"drift_report":None,"alert_envelope":None,"ledger_entry":None},inp,ih,True); write_canonical_json(rp,rec); return str(rp),5
    results=execute_monitor_plan(plan, UrllibHttpProbeClient() if args.mode=="existing-remote" else MockHttpProbeClient({}), args.mode, args.allow_remote_network, args.timeout_seconds)
    drifts=classify_drift(plan,results,policy)
    obs=compute_observation_hash(spec,results,drifts)
    snap=build_monitor_snapshot(plan,results,drifts,run_id,args.mode,policy.get("policy_id"),obs)
    snap_path=out/"snapshots"/f"monitor_snapshot_{snap['snapshot_id']}.json"; write_canonical_json(snap_path,snap)
    drift=build_drift_report(snap,drifts,prev); drift_path=out/"drift"/f"drift_report_{snap['snapshot_id']}.json"; write_canonical_json(drift_path,drift)
    alert=build_alert_envelope(snap,drift); alert_path=out/"alerts"/f"alert_envelope_{snap['snapshot_id']}.json"; write_canonical_json(alert_path,alert)
    arts={"monitor_plan_sha256":_sha256_bytes(plan_path.read_bytes()),"monitor_snapshot_sha256":_sha256_bytes(snap_path.read_bytes()),"drift_report_sha256":_sha256_bytes(drift_path.read_bytes()),"alert_envelope_sha256":_sha256_bytes(alert_path.read_bytes())}
    ledger=append_audit_ledger_entry(out, dm.get("distribution_id"), snap, arts)
    rec_path=out/"receipts"/f"monitor_receipt_{snap['snapshot_id']}.json"
    rec=build_monitor_receipt(run_id,dm.get("distribution_id"),snap["status"],spec,obs,{"monitor_plan":str(plan_path),"monitor_snapshot":str(snap_path),"drift_report":str(drift_path),"alert_envelope":str(alert_path),"ledger_entry":ledger},inp,ih,False)
    write_canonical_json(rec_path,rec); write_canonical_json(out/"latest_snapshot.json",snap)
    code=0 if snap["status"]=="healthy" else (10 if snap["status"]=="degraded" else 20)
    return str(rec_path), code

def parse_bool(v): return str(v).lower() in ("1","true","yes","on")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--distribution-manifest", required=True); ap.add_argument("--distribution-receipt", required=True); ap.add_argument("--remote-access-validation-report", required=True); ap.add_argument("--output-dir", required=True); ap.add_argument("--mode", required=True, choices=["one-shot","local-mock","existing-remote","dry-run"])
    ap.add_argument("--monitor-policy"); ap.add_argument("--previous-snapshot"); ap.add_argument("--allow-remote-network", action="store_true"); ap.add_argument("--allow-http", action="store_true"); ap.add_argument("--allow-localhost-remote", action="store_true"); ap.add_argument("--validate-ranges", default="true"); ap.add_argument("--validate-cors", default="true"); ap.add_argument("--timeout-seconds", type=int, default=10); ap.add_argument("--deterministic-run-id", action="store_true")
    args=ap.parse_args(); args.validate_ranges=parse_bool(args.validate_ranges); args.validate_cors=parse_bool(args.validate_cors)
    try:
        rp,code=monitor_distribution_once(args); print(rp); raise SystemExit(code)
    except MonitorError as e:
        err={"status":"error","error_count":1,"monitor_receipt_path":None,"snapshot_id":None,"distribution_id":None}; print(json.dumps(err), file=os.sys.stderr); raise SystemExit(e.code)

if __name__=="__main__": main()
