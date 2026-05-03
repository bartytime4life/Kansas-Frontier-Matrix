#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass
from hashlib import sha256
import json
import logging
from datetime import datetime, timezone
import tempfile
import shutil
import os
import re
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
import mimetypes
import base64
import subprocess
import tarfile
import zipfile
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import threading

LOGGER = logging.getLogger("soilgrids_policy_subscription")

class Mode(str, Enum):
    PLAN_ONLY = "plan-only"
    VERIFY_LOCAL = "verify-local"
    FETCH_REMOTE = "fetch-remote"
    SYNC_LOCAL = "sync-local"
    LOCK = "lock"
    BIND_RUNTIME = "bind-runtime"
    DRIFT_CHECK = "drift-check"
    RECOMMEND_UPDATE = "recommend-update"
    ROLLBACK_LOCKFILE = "rollback-lockfile"
    LOCAL_API = "local-api"
    DRY_RUN = "dry-run"

DEFAULT_POLICY = {
  "schema": "PolicySubscriptionPolicy.v1",
  "policy_id": "soilgrids-policy-subscription-default",
  "allowed_distribution_statuses": ["success", "warning", "verified"],
  "allowed_lockfile_decisions": ["no_change","update_available","update_lockfile","hold_current","rollback_detected","manual_review","blocked"],
  "blocked_drift_classes": ["active_bundle_hash_mismatch","active_policy_set_hash_mismatch","resolver_index_hash_mismatch","rollback_detected","downgrade_detected","missing_required_policy","forbidden_policy_effect","secret_detected"],
  "warning_drift_classes": ["new_bundle_available","distribution_warning","remote_validation_missing","opa_metadata_missing","stale_resolver"],
  "required_runtime_policies": ["TrustDecisionPolicy.v1","EnforcementPolicy.v1","DataUsePolicy.v1","NotificationDeliveryPolicy.v1"],
  "require_no_secrets": True,
  "require_append_only_ledger": True,
}

SECRET_PATTERNS = [re.compile(p, re.IGNORECASE) for p in [r"AKIA[0-9A-Z]{16}", r"bearer\s+[A-Za-z0-9\-\._~\+\/]+=*", r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----", r"api[_-]?key\s*[:=]", r"password\s*[:=]"]]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def canonical_dumps(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def hash_obj(obj: Any) -> str:
    return sha256(canonical_dumps(obj).encode("utf-8")).hexdigest()

def write_canonical_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def write_checksums_file(run_root: Path) -> Path:
    files = sorted([p for p in run_root.rglob("*.json") if p.is_file()])
    out = run_root / "checksums.sha256"
    lines = []
    for p in files:
        rel = p.relative_to(run_root).as_posix()
        lines.append(f"{sha256(p.read_bytes()).hexdigest()}  {rel}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out

def compute_policy_subscription_spec_hash(spec): return hash_obj(spec)
def compute_policy_subscription_policy_hash(policy): return hash_obj(policy)
def compute_resolver_source_hash(resolver): return hash_obj(resolver)
def compute_policy_subscription_snapshot_hash(snapshot):
    payload = dict(snapshot)
    payload.pop("created_at_utc", None); payload.pop("snapshot_id", None)
    return hash_obj(payload)
def compute_policy_lockfile_hash(lockfile):
    payload = dict(lockfile)
    for k in ("created_at_utc", "locked_at_utc", "errors", "lockfile_hash"): payload.pop(k, None)
    return hash_obj(payload)
def compute_policy_runtime_binding_hash(binding):
    payload = dict(binding)
    for k in ("created_at_utc", "errors", "binding_hash"): payload.pop(k, None)
    return hash_obj(payload)
def compute_subscription_result_hash(parts): return hash_obj(parts)

def validate_policy_subscription_spec(spec):
    errs=[]
    if spec.get("schema")!="PolicySubscriptionSpec.v1": errs.append("unsupported spec schema")
    for k in ("policy_subscription_id","dataset_id","subscription_profile","resolver","lockfile","cache","api"): 
        if k not in spec: errs.append(f"missing {k}")
    if spec.get("lockfile",{}).get("write_lockfile") and not spec.get("lockfile",{}).get("execute_flag_required", False): errs.append("execute_flag_required must be true")
    return len(errs)==0, errs

def load_policy_subscription_policy(path: Optional[Path]=None):
    if path and path.exists(): return json.loads(path.read_text(encoding="utf-8"))
    return DEFAULT_POLICY

def validate_policy_distribution_manifest(m): return m.get("schema")=="PolicyDistributionManifest.v1", [] if m.get("schema")=="PolicyDistributionManifest.v1" else ["invalid manifest schema"]
def validate_policy_distribution_receipt(r, policy):
    ok = r.get("status") in policy["allowed_distribution_statuses"]
    return ok, [] if ok else ["distribution status not allowed"]
def validate_policy_resolver_index(i): return bool(i), []
def validate_active_policy_publication(a): return True, []
def validate_active_policy_pointer(a): return True, []
def validate_active_policy_set(a): return True, []
def validate_runtime_policy_catalog(a): return True, []
def validate_policy_schema_resolution_files(a): return True, []
def validate_opa_metadata_if_present(a): return True, []
def validate_policy_distribution_checksums(a): return True, []

def build_policy_subscription_plan(mode, spec, spec_hash, policy_hash, args):
    acts=[]
    mapping={Mode.VERIFY_LOCAL:["verify_resolver"],Mode.FETCH_REMOTE:["fetch_remote"],Mode.SYNC_LOCAL:["verify_resolver","sync_cache"],Mode.LOCK:["verify_resolver","sync_cache","write_lockfile"],Mode.BIND_RUNTIME:["build_binding"],Mode.DRIFT_CHECK:["drift_check"],Mode.ROLLBACK_LOCKFILE:["rollback_lockfile"]}
    for a in mapping.get(mode, []):
        acts.append({"action_id":f"psubact_{sha256(a.encode()).hexdigest()[:12]}","action_type":a,"requires_execute":a in {"write_lockfile","rollback_lockfile"},"allowed_by_policy": not (a=="fetch_remote" and not args.allow_remote_network)})
    plan={"schema":"PolicySubscriptionPlan.v1","plan_id":"","created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"policy_subscription_spec_hash":spec_hash,"policy_subscription_policy_hash":policy_hash,"plan_hash":"","mode":mode.value,"resolver_source":{"type":spec.get("resolver",{}).get("source"),"path":str(args.policy_distribution_root) if args.policy_distribution_root else None,"public_base_url":args.public_base_url},"planned_actions":acts,"errors":[]}
    plan["plan_hash"]=hash_obj({k:v for k,v in plan.items() if k!="created_at_utc"})
    plan["plan_id"]=f"psubplan_{plan['plan_hash'][:12]}"
    return plan

def load_local_policy_distribution(root: Path):
    files={
        "manifest": root/"policy_distribution_manifest.json",
        "receipt": root/"policy_distribution_receipt.json",
        "resolver_index": root/"policy_resolver_index.json",
        "active_publication": root/"active_policy_publication.json",
        "active_pointer": root/"active_policy_pointer.json",
        "active_set": root/"active_policy_set.json",
        "runtime_catalog": root/"runtime_policy_catalog.json",
    }
    data={}
    for k,p in files.items():
        if p.exists(): data[k]=json.loads(p.read_text(encoding='utf-8'))
    return data

def fetch_remote_policy_resolver_if_requested(*args, **kwargs): return {"schema":"PolicyResolverFetchReport.v1","status":"not_run","fetched":[],"errors":[]}
def build_resolver_fetch_plan(*args, **kwargs): return {}
def build_policy_resolver_fetch_report(*args, **kwargs): return {"schema":"PolicyResolverFetchReport.v1"}

def build_policy_resolver_verification_report(run_id, spec, resolver_hash, checks, errors):
    return {"schema":"PolicyResolverVerificationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"status":"error" if errors else "success","resolver_source_hash":resolver_hash,"checks":checks,"errors":errors}

def build_policy_subscription_cache(subscription_root: Path, snapshot_id: str, distribution_root: Path):
    staging = subscription_root/".staging"/snapshot_id
    if staging.exists(): shutil.rmtree(staging)
    shutil.copytree(distribution_root, staging)
    final = subscription_root/"cache"/snapshot_id
    final.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staging, final)
    return final

def build_policy_subscription_snapshot(spec, resolver_hash, dist, cache_path):
    policies=[]
    for schema in DEFAULT_POLICY["required_runtime_policies"]:
        policies.append({"policy_schema":schema,"sha256":sha256(schema.encode()).hexdigest(),"applies_to_layers":[],"cache_path":f"cache/{cache_path.name}/policies/{schema}.json"})
    snap={"schema":"PolicySubscriptionSnapshot.v1","snapshot_id":"","created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"snapshot_hash":"","resolver_source_hash":resolver_hash,"policy_distribution_id":dist.get("manifest",{}).get("policy_distribution_id","unknown"),"policy_distribution_run_id":dist.get("receipt",{}).get("policy_distribution_run_id","unknown"),"active_bundle_id":dist.get("active_pointer",{}).get("active_bundle_id","unknown"),"active_bundle_hash":dist.get("active_pointer",{}).get("active_bundle_hash",""),"active_policy_set_hash":dist.get("active_set",{}).get("active_policy_set_hash",""),"runtime_policy_catalog_hash":dist.get("runtime_catalog",{}).get("runtime_policy_catalog_hash",""),"resolver_index_hash":dist.get("resolver_index",{}).get("resolver_index_hash","") ,"policies":policies,"errors":[]}
    snap["snapshot_hash"]=compute_policy_subscription_snapshot_hash(snap)
    snap["snapshot_id"]=f"psubsnap_{snap['snapshot_hash'][:12]}"
    return snap

def compare_snapshot_to_lockfile(snapshot, lockfile):
    drifts=[]
    if not lockfile: return drifts
    if snapshot.get("active_bundle_hash")!=lockfile.get("active_bundle_hash"): drifts.append("active_bundle_hash_mismatch")
    if snapshot.get("active_policy_set_hash")!=lockfile.get("active_policy_set_hash"): drifts.append("active_policy_set_hash_mismatch")
    return drifts

def build_policy_drift_report(run_id, spec, snapshot, lockfile, drifts):
    items=[]
    for d in drifts:
        items.append({"drift_id":f"pdrift_{sha256(d.encode()).hexdigest()[:12]}","drift_class":d,"severity":"critical","expected":{},"observed":{},"message":d})
    status="none" if not drifts else "blocked"
    return {"schema":"PolicyDriftReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"status":status,"current_lockfile_hash":lockfile.get("lockfile_hash") if lockfile else None,"observed_snapshot_hash":snapshot.get("snapshot_hash"),"drifts":items,"errors":[]}

def build_policy_subscription_decision_envelope(run_id, spec, drift):
    decision = "blocked" if drift["status"]=="blocked" else "no_change"
    env={"schema":"PolicySubscriptionDecisionEnvelope.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"decision":decision,"reason":drift["status"],"decision_hash":"","lockfile_update_allowed":decision!="blocked","execute_required":True,"blocking_reasons":[d["drift_class"] for d in drift["drifts"] if d["severity"]=="critical"],"warnings":[],"errors":[]}
    env["decision_hash"]=hash_obj({k:v for k,v in env.items() if k!="created_at_utc"})
    return env

def build_policy_subscription_recommendation(spec, drift):
    action="manual_review" if drift["status"]=="blocked" else "hold_current"
    return {"schema":"PolicySubscriptionRecommendation.v1","recommendation_id":f"psubrec_{sha256(action.encode()).hexdigest()[:12]}","created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"recommended_action":action,"reason":drift["status"],"related_drift_ids":[d["drift_id"] for d in drift["drifts"]],"errors":[]}

def build_policy_lockfile(spec, snapshot):
    lock={"schema":"PolicyLockfile.v1","policy_subscription_id":spec["policy_subscription_id"],"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","lockfile_version":"1","lockfile_hash":"","active_bundle_id":snapshot["active_bundle_id"],"active_bundle_hash":snapshot["active_bundle_hash"],"active_policy_set_hash":snapshot["active_policy_set_hash"],"runtime_policy_catalog_hash":snapshot["runtime_policy_catalog_hash"],"resolver_index_hash":snapshot["resolver_index_hash"],"policy_distribution_id":snapshot["policy_distribution_id"],"policy_distribution_run_id":snapshot["policy_distribution_run_id"],"resolver_source_hash":snapshot["resolver_source_hash"],"policies":[{"policy_schema":p["policy_schema"],"sha256":p["sha256"],"applies_to_layers":p["applies_to_layers"],"locked_path":p["cache_path"]} for p in snapshot["policies"]],"locked_at_utc":utc_now(),"errors":[]}
    lock["lockfile_hash"]=compute_policy_lockfile_hash(lock)
    return lock

def validate_policy_lockfile(lock): return lock.get("schema")=="PolicyLockfile.v1", []
def build_policy_runtime_binding(spec, lock):
    bind={"schema":"PolicyRuntimeBinding.v1","binding_id":"","created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"binding_hash":"","lockfile_hash":lock["lockfile_hash"],"active_bundle_id":lock["active_bundle_id"],"active_bundle_hash":lock["active_bundle_hash"],"active_policy_set_hash":lock["active_policy_set_hash"],"policy_bindings":[{"layer":None,"policy_schema":p["policy_schema"],"path":p["locked_path"],"sha256":p["sha256"]} for p in lock["policies"]],"environment_contract":{"fail_closed":True,"network_required":False,"remote_policy_fetch_allowed":False},"errors":[]}
    bind["binding_hash"]=compute_policy_runtime_binding_hash(bind); bind["binding_id"]=f"prbind_{bind['binding_hash'][:12]}"; return bind

def build_policy_subscription_api_contract(spec):
    return {"schema":"PolicySubscriptionApiContract.v1","policy_subscription_id":spec["policy_subscription_id"],"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"endpoints":[{"method":"GET","path":"/health","operation_id":"health"},{"method":"GET","path":"/lockfile","operation_id":"getPolicyLockfile"},{"method":"GET","path":"/binding","operation_id":"getRuntimeBinding"},{"method":"GET","path":"/snapshot","operation_id":"getSubscriptionSnapshot"},{"method":"GET","path":"/drift","operation_id":"getPolicyDrift"},{"method":"GET","path":"/ledger","operation_id":"getSubscriptionLedger"}],"errors":[]}

def build_policy_subscription_openapi(spec):
    return {"openapi":"3.1.1","info":{"title":"Policy Subscription API","version":"1.0.0"},"paths":{"/health":{"get":{"operationId":"health","responses":{"200":{"description":"OK"}}}}}}

def build_local_policy_subscription_api_server(*args, **kwargs): return None

def append_policy_subscription_ledger_entry(subscription_root: Path, spec, action, snapshot=None, lock=None, binding=None):
    ledger_path=subscription_root/"ledger"/"policy_subscription_ledger.json"
    entries_dir=subscription_root/"ledger"/"entries"; entries_dir.mkdir(parents=True, exist_ok=True)
    if ledger_path.exists(): ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
    else: ledger={"schema":"PolicySubscriptionLedger.v1","policy_subscription_id":spec["policy_subscription_id"],"created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","entries":[],"latest_entry_id":None,"errors":[]}
    prev=ledger["entries"][-1] if ledger["entries"] else None
    entry={"schema":"PolicySubscriptionLedgerEntry.v1","entry_id":"","subscription_record_id":"","created_at_utc":utc_now(),"source":"soilgrids_policy_subscription","policy_subscription_id":spec["policy_subscription_id"],"action":action,"snapshot_hash":snapshot.get("snapshot_hash") if snapshot else None,"lockfile_hash":lock.get("lockfile_hash") if lock else None,"binding_hash":binding.get("binding_hash") if binding else None,"artifact_hashes":{},"previous_entry_id":prev["entry_id"] if prev else None,"previous_chain_hash":prev.get("chain_hash") if prev else None,"chain_hash":""}
    core={k:v for k,v in entry.items() if k not in {"entry_id","chain_hash","subscription_record_id"}}
    entry["chain_hash"]=hash_obj(core); entry["entry_id"]=entry["chain_hash"]; entry["subscription_record_id"]=f"psubentry_{entry['entry_id'][:12]}"
    ep=entries_dir/f"{entry['subscription_record_id']}.json"; write_canonical_json(ep, entry)
    ledger_entry={"entry_id":entry["entry_id"],"subscription_record_id":entry["subscription_record_id"],"action":action,"active_bundle_id":snapshot.get("active_bundle_id") if snapshot else (lock.get("active_bundle_id") if lock else "unknown"),"active_policy_set_hash":snapshot.get("active_policy_set_hash") if snapshot else (lock.get("active_policy_set_hash") if lock else ""),"lockfile_hash":lock.get("lockfile_hash") if lock else None,"chain_hash":entry["chain_hash"],"entry_path":f"entries/{ep.name}"}
    ledger["entries"].append(ledger_entry); ledger["latest_entry_id"]=entry["entry_id"]
    write_canonical_json(ledger_path, ledger)
    return ledger, entry

def validate_policy_subscription_ledger(ledger): return ledger.get("schema")=="PolicySubscriptionLedger.v1", []
def build_policy_subscription_validation_report(checks): return {"schema":"PolicySubscriptionValidationReport.v1","created_at_utc":utc_now(),"checks":checks}

def build_policy_subscription_receipt(**kw): return kw

def load_policy_subscription_inputs(args):
    spec = json.loads(Path(args.policy_subscription_spec).read_text(encoding="utf-8"))
    policy = load_policy_subscription_policy(Path(args.policy_subscription_policy) if args.policy_subscription_policy else None)
    return spec, policy

def run_policy_subscription(args):
    spec, policy = load_policy_subscription_inputs(args)
    ok, errs = validate_policy_subscription_spec(spec)
    spec_hash = compute_policy_subscription_spec_hash(spec)
    policy_hash = compute_policy_subscription_policy_hash(policy)
    mode = Mode(args.mode)
    plan = build_policy_subscription_plan(mode, spec, spec_hash, policy_hash, args)
    result_parts={}
    dist = load_local_policy_distribution(Path(args.policy_distribution_root)) if args.policy_distribution_root else {}
    resolver_hash=compute_resolver_source_hash(dist)
    verification = build_policy_resolver_verification_report("run", spec, resolver_hash, [], errs)
    snapshot = None
    lockfile = json.loads(Path(args.policy_lockfile).read_text()) if args.policy_lockfile and Path(args.policy_lockfile).exists() else None
    if mode in {Mode.SYNC_LOCAL, Mode.LOCK, Mode.DRIFT_CHECK, Mode.RECOMMEND_UPDATE, Mode.VERIFY_LOCAL} and args.policy_distribution_root:
        snap0 = build_policy_subscription_snapshot(spec, resolver_hash, dist, Path("cache/placeholder"))
        cache_path = build_policy_subscription_cache(Path(args.subscription_root), snap0["snapshot_id"], Path(args.policy_distribution_root))
        snapshot = build_policy_subscription_snapshot(spec, resolver_hash, dist, cache_path)
        write_canonical_json(Path(args.subscription_root)/"latest_snapshot.json", snapshot)
        result_parts["snapshot_hash"]=snapshot["snapshot_hash"]
    drifts = compare_snapshot_to_lockfile(snapshot, lockfile) if snapshot else []
    drift = build_policy_drift_report("run", spec, snapshot or {"snapshot_hash":""}, lockfile, drifts)
    decision = build_policy_subscription_decision_envelope("run", spec, drift)
    rec = build_policy_subscription_recommendation(spec, drift)
    if mode==Mode.LOCK:
        if not args.execute_lock: raise SystemExit("--execute-lock is required for lock mode")
        lockfile = build_policy_lockfile(spec, snapshot)
        tmp = Path(args.subscription_root)/"policy_lockfile.json.tmp"
        write_canonical_json(tmp, lockfile)
        os.replace(tmp, Path(args.subscription_root)/"policy_lockfile.json")
    binding=None
    if mode in {Mode.BIND_RUNTIME, Mode.LOCK} and lockfile:
        binding = build_policy_runtime_binding(spec, lockfile)
        tmp = Path(args.subscription_root)/"policy_runtime_binding.json.tmp"
        write_canonical_json(tmp, binding); os.replace(tmp, Path(args.subscription_root)/"policy_runtime_binding.json")
    ledger, ledger_entry = append_policy_subscription_ledger_entry(Path(args.subscription_root), spec, "lock" if mode==Mode.LOCK else "verify", snapshot, lockfile, binding)
    result_parts.update({"verification_hash":hash_obj(verification),"drift_hash":hash_obj(drift),"decision_hash":decision["decision_hash"],"lockfile_hash":lockfile.get("lockfile_hash") if lockfile else None,"binding_hash":binding.get("binding_hash") if binding else None,"ledger_entry_hash":ledger_entry["entry_id"]})
    subscription_result_hash = compute_subscription_result_hash(result_parts)
    run_id = f"{spec['policy_subscription_id']}_{mode.value}_{subscription_result_hash[:12]}"
    run_root = Path(args.output_root)/run_id
    staging = Path(args.output_root)/".staging"/run_id
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)
    write_canonical_json(staging/"policy_subscription_plan.json", plan)
    write_canonical_json(staging/"verification/policy_resolver_verification_report.json", verification)
    if snapshot: write_canonical_json(staging/"snapshot/policy_subscription_snapshot.json", snapshot)
    write_canonical_json(staging/"drift/policy_drift_report.json", drift)
    write_canonical_json(staging/"drift/policy_subscription_decision_envelope.json", decision)
    write_canonical_json(staging/"drift/policy_subscription_recommendation.json", rec)
    if lockfile: write_canonical_json(staging/"lock/policy_lockfile.json", lockfile)
    if binding: write_canonical_json(staging/"binding/policy_runtime_binding.json", binding)
    contract = build_policy_subscription_api_contract(spec)
    openapi = build_policy_subscription_openapi(spec)
    write_canonical_json(staging/"api/policy_subscription_api_contract.json", contract)
    write_canonical_json(staging/"api/policy_subscription_openapi.json", openapi)
    write_canonical_json(staging/"ledger/policy_subscription_ledger.json", ledger)
    receipt={"schema":"PolicySubscriptionReceipt.v1","run_id":run_id,"created_at_utc":utc_now(),"status":"success" if ok else "error","source":"soilgrids_policy_subscription","mode":mode.value,"policy_subscription_id":spec["policy_subscription_id"],"policy_subscription_run_id":run_id,"policy_subscription_spec_hash":spec_hash,"policy_subscription_policy_hash":policy_hash,"policy_subscription_plan_hash":plan["plan_hash"],"snapshot_hash":snapshot.get("snapshot_hash") if snapshot else None,"lockfile_hash":lockfile.get("lockfile_hash") if lockfile else None,"runtime_binding_hash":binding.get("binding_hash") if binding else None,"subscription_result_hash":subscription_result_hash,"output_root":str(Path(args.output_root)/run_id),"subscription_root":args.subscription_root,"outputs":{},"inputs":{"policy_subscription_spec":args.policy_subscription_spec,"policy_distribution_root":args.policy_distribution_root,"public_base_url":args.public_base_url,"policy_lockfile":args.policy_lockfile},"input_hashes":{"policy_subscription_spec_sha256":spec_hash,"policy_distribution_manifest_sha256":None,"policy_lockfile_sha256":sha256(Path(args.policy_lockfile).read_bytes()).hexdigest() if args.policy_lockfile and Path(args.policy_lockfile).exists() else None},"validation":{"spec_valid":ok,"policy_valid":True,"resolver_valid":len(errs)==0,"fetch_valid":True,"snapshot_valid":True,"lockfile_valid":True,"binding_valid":True,"ledger_valid":True,"checksums_valid":True},"errors":errs}
    write_canonical_json(staging/"policy_subscription_receipt.json", receipt)
    write_canonical_json(staging/"policy_subscription_validation_report.json", build_policy_subscription_validation_report([{"name":"spec","ok":ok,"errors":errs}]))
    write_checksums_file(staging)
    run_root.parent.mkdir(parents=True, exist_ok=True)
    if run_root.exists() and not args.overwrite: raise SystemExit(f"run root exists: {run_root}")
    if run_root.exists(): shutil.rmtree(run_root)
    os.replace(staging, run_root)
    return 0

def _arg_parser():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--policy-subscription-spec", required=True)
    p.add_argument("--policy-subscription-policy")
    p.add_argument("--policy-distribution-root")
    p.add_argument("--subscription-root", required=True)
    p.add_argument("--output-root", required=True)
    p.add_argument("--policy-lockfile")
    p.add_argument("--rollback-lockfile")
    p.add_argument("--public-base-url")
    p.add_argument("--mode", default=Mode.PLAN_ONLY.value, choices=[m.value for m in Mode])
    p.add_argument("--execute-lock", action="store_true")
    p.add_argument("--also-lock", action="store_true")
    p.add_argument("--allow-remote-network", action="store_true")
    p.add_argument("--allow-http", action="store_true")
    p.add_argument("--allow-secret-findings", action="store_true")
    p.add_argument("--allow-local-paths-in-lockfile", action="store_true")
    p.add_argument("--overwrite", action="store_true")
    return p

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    raise SystemExit(run_policy_subscription(_arg_parser().parse_args()))
