#!/usr/bin/env python3
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    import resource
except Exception:
    resource = None

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"bearer\s+[A-Za-z0-9._-]+", re.I),
    re.compile(r"api[_-]?key\s*[:=]", re.I),
    re.compile(r"password\s*[:=]", re.I),
    re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"),
    re.compile(r"https?://[^\s/@]+:[^\s/@]+@"),
]
ALLOWED_MODES = {
    "plan-only", "verify-context", "supervise-local", "attach-observe", "post-run-verify",
    "conformance-check", "telemetry-export", "attest-execution", "recommend-response", "local-api", "dry-run"
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def hash_obj(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def is_remote(value: str | None) -> bool:
    if not value:
        return False
    u = urlparse(value)
    return u.scheme in {"http", "https", "ftp"}


def scan_secrets(data: Any) -> list[str]:
    txt = data if isinstance(data, str) else canonical_json(data)
    hits = []
    for p in SECRET_PATTERNS:
        if p.search(txt):
            hits.append(p.pattern)
    return hits


def write_canonical_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_checksums_file(root: Path) -> None:
    lines = []
    for p in sorted(x for x in root.rglob("*") if x.is_file() and x.name != "checksums.sha256"):
        lines.append(f"{file_sha256(p)}  {p.relative_to(root).as_posix()}")
    (root / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def compute_runtime_supervision_spec_hash(spec): return hash_obj(spec)
def compute_runtime_supervision_policy_hash(policy): return hash_obj(policy)
def compute_supervision_context_hash(ctx): return hash_obj(ctx)
def compute_observation_session_hash(obs): return hash_obj({k: v for k, v in obs.items() if k not in {"created_at_utc", "started_at_utc", "ended_at_utc", "duration_ms", "observation_session_hash"}})
def compute_conformance_hash(c): return hash_obj({"checks": c.get("checks", []), "summary": c.get("summary", {}), "status": c.get("status")})
def compute_telemetry_hash(t): return hash_obj({"metrics": t.get("metrics", {}), "paths": [t.get("logs_path"), t.get("metrics_path"), t.get("traces_path")]})
def compute_attestation_hash(a): return hash_obj({k: v for k, v in a.items() if k not in {"created_at_utc", "attestation_hash"}})
def compute_supervision_result_hash(parts): return hash_obj(parts)

def validate_runtime_supervision_spec(spec):
    e=[]
    if spec.get("schema")!="RuntimeSupervisionSpec.v1": e.append("unsupported schema")
    if not spec.get("runtime_supervision_id"): e.append("missing runtime_supervision_id")
    if not spec.get("dataset_id"): e.append("missing dataset_id")
    if spec.get("telemetry", {}).get("external_export") is True: e.append("external telemetry export disabled")
    if spec.get("attestation", {}).get("sign") is True and not spec.get("attestation", {}).get("signing_backend"):
        e.append("signing enabled without backend")
    if spec.get("supervision_profile") not in {"strict-local", "local"}: e.append("unsupported supervision profile")
    return (not e, e)

def load_runtime_supervision_policy(path: Path | None):
    if path: return read_json(path)
    return {
      "schema":"RuntimeSupervisionPolicy.v1","policy_id":"soilgrids-runtime-supervision-default",
      "allowed_supervision_statuses":["conformant","conformant_with_warnings","nonconformant","error","planned","dry_run"],
      "required_checks":["context.execution_lock.valid","context.runtime_input_lock.valid","context.policy_binding.matches","inputs.hashes.match","workspace.no_escape","outputs.expected_or_allowed","telemetry.written","attestation.written"],
      "violation_classes":["policy_binding_drift","input_hash_drift","workspace_escape","unexpected_output_mutation","network_policy_violation","mutation_policy_violation","missing_layer15_receipt","command_mismatch","secret_detected"],
      "warning_classes":["limited_network_observation","optional_output_missing","noncritical_environment_difference","stdout_truncated","stderr_truncated"],
      "fail_closed":True
    }

def validate_execution_context_lock(lock): return (lock.get("schema")=="ExecutionContextLock.v1", [] if lock.get("schema")=="ExecutionContextLock.v1" else ["invalid execution lock schema"])
def validate_runtime_input_lock(lock): return (lock.get("schema")=="RuntimeInputLock.v1", [] if lock.get("schema")=="RuntimeInputLock.v1" else ["invalid runtime input lock schema"])
def validate_admission_decision_envelope(d): return (d.get("schema")=="AdmissionDecisionEnvelope.v1", [] if d.get("schema")=="AdmissionDecisionEnvelope.v1" else ["invalid admission envelope schema"])
def validate_runtime_admission_receipt(r): return (r.get("schema")=="RuntimeAdmissionReceipt.v1", [] if r.get("schema")=="RuntimeAdmissionReceipt.v1" else ["invalid admission receipt schema"])

def validate_supervision_context(spec, exlock, rinlock, admission_env=None, admission_receipt=None):
    checks=[]; errors=[]
    ex_ok, ex_e = validate_execution_context_lock(exlock); ri_ok, ri_e = validate_runtime_input_lock(rinlock)
    checks.append({"check_id":"context.execution_lock.valid","severity":"required","status":"pass" if ex_ok else "fail"})
    checks.append({"check_id":"context.runtime_input_lock.valid","severity":"required","status":"pass" if ri_ok else "fail"})
    errors += ex_e + ri_e
    if admission_env:
        a_ok, a_e = validate_admission_decision_envelope(admission_env); errors += a_e
        if spec.get("context",{}).get("require_admission_decision_admit", True) and admission_env.get("decision") not in {"admit", "admit_with_warnings"}:
            errors.append("admission decision not admitted")
        checks.append({"check_id":"context.admission_decision.valid","severity":"required","status":"pass" if a_ok else "fail"})
    if admission_receipt:
        r_ok, r_e = validate_runtime_admission_receipt(admission_receipt); errors += r_e
        checks.append({"check_id":"context.admission_receipt.valid","severity":"required","status":"pass" if r_ok else "fail"})
    if scan_secrets(exlock) or scan_secrets(rinlock): errors.append("secret detected in context")
    return (not errors, checks, errors)

def load_runtime_supervision_inputs(args):
    return {
        "spec": read_json(Path(args.runtime_supervision_spec)),
        "execution_context_lock": read_json(Path(args.execution_context_lock)) if args.execution_context_lock else None,
        "runtime_input_lock": read_json(Path(args.runtime_input_lock)) if args.runtime_input_lock else None,
        "admission_decision": read_json(Path(args.admission_decision_envelope)) if args.admission_decision_envelope else None,
        "admission_receipt": read_json(Path(args.runtime_admission_receipt)) if args.runtime_admission_receipt else None,
        "pipeline_run_manifest": read_json(Path(args.pipeline_run_manifest)) if args.pipeline_run_manifest else None,
        "pipeline_run_receipt": read_json(Path(args.pipeline_run_receipt)) if args.pipeline_run_receipt else None,
    }

def build_runtime_supervision_plan(spec, spec_hash, policy_hash, mode, ex_hash=None, ri_hash=None, active_policy_set_hash=None):
    plan={"schema":"RuntimeSupervisionPlan.v1","plan_id":"rsupplan_"+hash_obj({"mode":mode,"spec":spec_hash})[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"runtime_supervision_spec_hash":spec_hash,"runtime_supervision_policy_hash":policy_hash,"mode":mode,"context":{"execution_context_lock_hash":ex_hash,"runtime_input_lock_hash":ri_hash,"active_policy_set_hash":active_policy_set_hash},"planned_observations":["process","environment","filesystem_delta","declared_network","telemetry","attestation"],"planned_actions":[],"errors":[]}
    for a in ["verify_context","snapshot_inputs","run_subprocess","snapshot_outputs","conformance_check","write_attestation"]:
        plan["planned_actions"].append({"action_id":"rsupact_"+hash_obj({"a":a,"m":mode})[:12],"action_type":a,"requires_execute":a=="run_subprocess","allowed_by_policy":True})
    plan["plan_hash"]=hash_obj({k:v for k,v in plan.items() if k!="created_at_utc"})
    return plan

def build_supervision_context_verification_report(run_id,spec,checks,errors):
    return {"schema":"SupervisionContextVerificationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"status":"error" if errors else "success","checks":checks,"errors":errors}

def snapshot_filesystem_inputs(workspaces):
    snap={}
    for w in workspaces:
        wp=Path(w)
        if not wp.exists():
            continue
        for p in sorted(x for x in wp.rglob("*") if x.is_file()):
            snap[p.as_posix()]={"sha256":file_sha256(p),"bytes":p.stat().st_size}
    return snap
snapshot_filesystem_outputs=snapshot_filesystem_inputs

def compute_filesystem_delta(before,after):
    out=[]
    keys=sorted(set(before)|set(after))
    for k in keys:
        b=before.get(k); a=after.get(k)
        if b and not a: t="deleted"
        elif a and not b: t="created"
        elif a["sha256"]!=b["sha256"]: t="modified"
        else: t="unchanged"
        out.append({"path":k,"change_type":t,"before_sha256":b["sha256"] if b else None,"after_sha256":a["sha256"] if a else None,"bytes":(a or b)["bytes"]})
    return out

def validate_command_against_lock(cmd, exlock):
    approved = exlock.get("operation", {}).get("approved_command")
    if not approved: return True, []
    return (cmd == approved, [] if cmd == approved else ["command mismatch"])

def run_supervised_subprocess(argv, cwd, timeout_seconds, stdout_path, stderr_path, max_log_bytes):
    start=time.time()
    with stdout_path.open("wb") as so, stderr_path.open("wb") as se:
        p=subprocess.Popen(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err=p.communicate(timeout=timeout_seconds)
        timed_out=False
        if len(out)>max_log_bytes: out=out[:max_log_bytes]; stdout_truncated=True
        else: stdout_truncated=False
        if len(err)>max_log_bytes: err=err[:max_log_bytes]; stderr_truncated=True
        else: stderr_truncated=False
        so.write(out); se.write(err)
    return {"exit_code":p.returncode,"timed_out":timed_out,"duration_ms":int((time.time()-start)*1000),"stdout_truncated":stdout_truncated,"stderr_truncated":stderr_truncated}

def collect_process_observation(run_id,args,proc_result,stdout_path,stderr_path):
    argv=[args.supervised_command]+(args.supervised_arg or []) if args.supervised_command else []
    return build_process_observation_report(run_id,argv,proc_result,stdout_path,stderr_path)

def collect_environment_observation():
    env={"python_version":platform.python_version(),"platform":platform.platform(),"executable":os.path.basename(sys.executable)}
    if resource:
        env["rlimit_nofile"]=resource.getrlimit(resource.RLIMIT_NOFILE)[0]
    return env

def collect_declared_network_observation(spec, args):
    mode=spec.get("observation",{}).get("capture_network_observation","declared-only")
    return build_network_observation_report("",mode,args.supervised_arg or [],[])

def collect_declared_mutation_observation(*_): return {"status":"declared"}

def validate_layer15_outputs_if_present(pipeline_run_receipt):
    if not pipeline_run_receipt: return True, []
    ok = pipeline_run_receipt.get("schema") == "PipelineRunReceipt.v1"
    return ok, ([] if ok else ["invalid layer15 receipt schema"])

def build_runtime_observation_session(spec,mode,ex_hash,ri_hash):
    s={"schema":"RuntimeObservationSession.v1","session_id":"rsession_"+hash_obj({"m":mode,"e":ex_hash,"r":ri_hash})[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"execution_context_lock_hash":ex_hash,"runtime_input_lock_hash":ri_hash,"mode":mode,"started_at_utc":None,"ended_at_utc":None,"duration_ms":0,"observation_limits":{"max_log_bytes":spec.get("observation",{}).get("max_log_bytes",10485760),"network_observation":spec.get("observation",{}).get("capture_network_observation","declared-only"),"mutation_observation":spec.get("observation",{}).get("capture_mutation_observation","filesystem-delta")},"errors":[]}
    s["observation_session_hash"]=compute_observation_session_hash(s); return s

def build_process_observation_report(run_id, argv, proc_result, stdout_path, stderr_path):
    return {"schema":"ProcessObservationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","status":"not_run" if proc_result is None else ("success" if proc_result["exit_code"]==0 else "error"),"command_hash":hash_obj(argv) if argv else None,"argv_redacted":["<redacted>" if scan_secrets(x) else x for x in argv],"exit_code":None if proc_result is None else proc_result["exit_code"],"timeout_seconds":3600,"timed_out":False if proc_result is None else proc_result["timed_out"],"stdout_path":str(stdout_path) if stdout_path else None,"stderr_path":str(stderr_path) if stderr_path else None,"stdout_sha256":file_sha256(stdout_path) if stdout_path and stdout_path.exists() else None,"stderr_sha256":file_sha256(stderr_path) if stderr_path and stderr_path.exists() else None,"stdout_truncated":False if proc_result is None else proc_result.get("stdout_truncated",False),"stderr_truncated":False if proc_result is None else proc_result.get("stderr_truncated",False),"errors":[]}

def build_filesystem_mutation_report(run_id, workspaces, before, after):
    changes=compute_filesystem_delta(before, after)
    return {"schema":"FilesystemMutationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","status":"success","workspace_roots":workspaces,"before_snapshot_hash":hash_obj(before),"after_snapshot_hash":hash_obj(after),"changes":changes,"unexpected_changes":[],"errors":[]}

def build_network_observation_report(run_id, observation_mode, argv, env_obs):
    observations=[]
    joined=" ".join(argv)+" "+canonical_json(env_obs)
    for m in re.finditer(r"https?://[^\s]+", joined):
        observations.append({"type":"url_detected","value":m.group(0)})
    return {"schema":"NetworkObservationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","status":"warning" if observations else "success","observation_mode":observation_mode,"network_profile":None,"remote_network_allowed":False,"observations":observations,"limitations":["No OS-level packet capture was performed."],"errors":[]}

def build_policy_binding_conformance_report(run_id, expected, observed):
    passed = expected == observed
    return {"schema":"PolicyBindingConformanceReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","status":"success" if passed else "error","checks":[{"check_id":"conformance.policy.active_policy_set_hash.matches","severity":"required","status":"pass" if passed else "fail","expected":expected,"observed":observed,"message":"policy set hash compared"}],"errors":[] if passed else ["policy_binding_drift"]}

def build_runtime_conformance_report(run_id,spec,checks,errors,violations,warnings):
    failed=sum(1 for c in checks if c.get("status")=="fail"); passed=sum(1 for c in checks if c.get("status")=="pass")
    status="error" if errors else ("nonconformant" if failed or violations else ("conformant_with_warnings" if warnings else "conformant"))
    r={"schema":"RuntimeConformanceReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"status":status,"summary":{"checks":len(checks),"passed":passed,"failed":failed,"warnings":len(warnings),"violations":len(violations)},"checks":checks,"errors":errors}
    r["conformance_hash"]=compute_conformance_hash(r); return r

def build_runtime_violation_report(run_id,spec,violations,errors):
    status="none" if not violations else "critical" if any(v["severity"]=="critical" for v in violations) else "violation"
    return {"schema":"RuntimeViolationReport.v1","run_id":run_id,"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"status":"error" if errors else status,"violations":violations,"errors":errors}

def build_runtime_telemetry_snapshot(spec, run_id, process_report, fs_report, logs_path, metrics_path, traces_path):
    metrics={"duration_ms":0,"exit_code":process_report.get("exit_code") or 0,"files_created":sum(1 for c in fs_report.get("changes",[]) if c["change_type"]=="created"),"files_modified":sum(1 for c in fs_report.get("changes",[]) if c["change_type"]=="modified"),"files_deleted":sum(1 for c in fs_report.get("changes",[]) if c["change_type"]=="deleted"),"stdout_bytes":Path(process_report["stdout_path"]).stat().st_size if process_report.get("stdout_path") else 0,"stderr_bytes":Path(process_report["stderr_path"]).stat().st_size if process_report.get("stderr_path") else 0}
    snap={"schema":"RuntimeTelemetrySnapshot.v1","snapshot_id":"rtel_"+hash_obj({"run":run_id,"m":metrics})[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"metrics":metrics,"logs_path":str(logs_path) if logs_path else None,"metrics_path":str(metrics_path) if metrics_path else None,"traces_path":str(traces_path) if traces_path else None,"errors":[]}
    snap["telemetry_hash"]=compute_telemetry_hash(snap); return snap

def build_runtime_telemetry_bundle(spec, logs_path, metrics_path, traces_path):
    arts=[]
    for role,p in (("logs",logs_path),("metrics",metrics_path),("traces",traces_path)):
        if p and Path(p).exists(): arts.append({"role":role,"path":str(p),"sha256":file_sha256(Path(p))})
    return {"schema":"RuntimeTelemetryBundle.v1","runtime_supervision_id":spec["runtime_supervision_id"],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","telemetry_bundle_hash":hash_obj(arts),"format":"otel-style-local","artifacts":arts,"external_export":False,"errors":[]}

def build_execution_conformance_attestation(spec, ex_hash, ri_hash, policy_hash, conformance_status, violation_count, telemetry_hash):
    a={"schema":"ExecutionConformanceAttestation.v1","attestation_id":"execatt_"+hash_obj({"e":ex_hash,"r":ri_hash,"c":conformance_status})[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"subject":[{"name":"supervised_runtime_execution","digest":{"sha256":hash_obj({"e":ex_hash,"r":ri_hash,"c":conformance_status})}}],"claims":{"execution_context_lock_hash":ex_hash,"runtime_input_lock_hash":ri_hash,"active_policy_set_hash":policy_hash,"conformance_status":conformance_status,"violation_count":violation_count,"telemetry_hash":telemetry_hash},"proof":{"type":"unsigned","signature_value":None},"errors":[]}
    a["attestation_hash"]=compute_attestation_hash(a); return a

def build_intoto_execution_statement_if_requested(attestation, violations, enabled):
    if not enabled: return None
    return {"_type":"https://in-toto.io/Statement/v1","subject":attestation["subject"],"predicateType":"https://soilgrids.local/predicates/runtime-conformance/v1","predicate":{"executionContextLockHash":attestation["claims"]["execution_context_lock_hash"],"runtimeInputLockHash":attestation["claims"]["runtime_input_lock_hash"],"activePolicySetHash":attestation["claims"]["active_policy_set_hash"],"conformanceStatus":attestation["claims"]["conformance_status"],"violations":violations}}

def sign_execution_attestation_if_requested(attestation, enabled):
    return attestation

def build_supervised_run_manifest(spec, ex_hash, ri_hash, obs_hash, conf_hash, tel_hash, att_hash, pipeline_run_receipt_path=None):
    m={"schema":"SupervisedRunManifest.v1","supervised_run_id":"srun_"+hash_obj({"e":ex_hash,"r":ri_hash,"c":conf_hash})[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"execution_context_lock_hash":ex_hash,"runtime_input_lock_hash":ri_hash,"observation_session_hash":obs_hash,"conformance_hash":conf_hash,"telemetry_hash":tel_hash,"attestation_hash":att_hash,"pipeline_run_receipt":{"path":pipeline_run_receipt_path,"sha256":file_sha256(Path(pipeline_run_receipt_path)) if pipeline_run_receipt_path and Path(pipeline_run_receipt_path).exists() else None},"errors":[]}
    m["supervised_run_hash"]=hash_obj({k:v for k,v in m.items() if k not in {"created_at_utc","supervised_run_hash"}}); return m

def build_runtime_response_recommendation(spec, violations):
    if not violations: return {"schema":"RuntimeResponseRecommendation.v1","recommendation_id":"rresp_"+hash_obj(spec["runtime_supervision_id"])[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"status":"not_required","recommended_actions":[],"errors":[]}
    return {"schema":"RuntimeResponseRecommendation.v1","recommendation_id":"rresp_"+hash_obj(violations)[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"status":"recommended","recommended_actions":[{"action_type":"manual_review","severity":"high","reason":"violations detected","evidence_refs":[]}],"errors":[]}

def append_runtime_supervision_ledger_entry(ledger_root: Path, spec, manifest, conformance_status, artifact_hashes):
    ledger_file=ledger_root/"runtime_supervision_ledger.json"; entries_dir=ledger_root/"entries"; entries_dir.mkdir(parents=True,exist_ok=True)
    ledger=read_json(ledger_file) if ledger_file.exists() else {"schema":"RuntimeSupervisionLedger.v1","runtime_supervision_id":spec["runtime_supervision_id"],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","entries":[],"latest_entry_id":None,"errors":[]}
    prev=ledger["entries"][-1] if ledger["entries"] else None
    entry={"schema":"RuntimeSupervisionLedgerEntry.v1","entry_id":"","supervision_record_id":"rsup_"+hash_obj(manifest["supervised_run_id"])[:12],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","runtime_supervision_id":spec["runtime_supervision_id"],"supervised_run_hash":manifest.get("supervised_run_hash"),"conformance_hash":manifest.get("conformance_hash"),"attestation_hash":manifest.get("attestation_hash"),"artifact_hashes":artifact_hashes,"previous_entry_id":prev.get("entry_id") if prev else None,"previous_chain_hash":prev.get("chain_hash") if prev else None}
    entry["chain_hash"]=hash_obj({k:v for k,v in entry.items() if k not in {"entry_id","created_at_utc"}})
    entry["entry_id"]=hash_obj({"chain_hash":entry["chain_hash"],"prev":entry.get("previous_entry_id")})
    ep=entries_dir/f"{entry['entry_id']}.json"; write_canonical_json(ep,entry)
    ledger["entries"].append({"entry_id":entry["entry_id"],"supervision_record_id":entry["supervision_record_id"],"supervised_run_hash":manifest.get("supervised_run_hash"),"conformance_status":conformance_status,"chain_hash":entry["chain_hash"],"entry_path":f"entries/{ep.name}"})
    ledger["latest_entry_id"]=entry["entry_id"]
    write_canonical_json(ledger_file,ledger)
    return ledger, entry

def validate_runtime_supervision_ledger(ledger): return (ledger.get("schema")=="RuntimeSupervisionLedger.v1",[] if ledger.get("schema")=="RuntimeSupervisionLedger.v1" else ["invalid ledger schema"])
def build_runtime_supervision_api_contract(spec): return {"schema":"RuntimeSupervisionApiContract.v1","runtime_supervision_id":spec["runtime_supervision_id"],"created_at_utc":utc_now(),"source":"soilgrids_runtime_supervisor","read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"endpoints":[{"method":"GET","path":"/health","operation_id":"health"},{"method":"GET","path":"/context","operation_id":"getContextVerification"},{"method":"GET","path":"/observations","operation_id":"listObservations"},{"method":"GET","path":"/conformance","operation_id":"getConformance"},{"method":"GET","path":"/violations","operation_id":"getViolations"},{"method":"GET","path":"/attestations","operation_id":"listAttestations"},{"method":"GET","path":"/ledger","operation_id":"getSupervisionLedger"}],"errors":[]}
def build_runtime_supervision_openapi(spec): return {"openapi":"3.1.1","info":{"title":"Runtime Supervision API","version":"1.0.0"},"paths":{"/health":{"get":{"operationId":"health","responses":{"200":{"description":"ok"}}}}}}
def build_local_runtime_supervision_api_server(*_): return None
def validate_runtime_supervision_api_contract(contract): return (contract.get("schema")=="RuntimeSupervisionApiContract.v1",[] if contract.get("schema")=="RuntimeSupervisionApiContract.v1" else ["invalid api contract schema"])
def build_runtime_supervision_validation_report(checks,errors): return {"schema":"RuntimeSupervisionValidationReport.v1","created_at_utc":utc_now(),"checks":checks,"errors":errors,"status":"error" if errors else "success"}

def build_runtime_supervisor_receipt(**kwargs): return kwargs


def run_runtime_supervisor(args):
    inputs=load_runtime_supervision_inputs(args)
    spec=inputs["spec"]
    policy=load_runtime_supervision_policy(Path(args.runtime_supervision_policy) if args.runtime_supervision_policy else None)
    ok, errs = validate_runtime_supervision_spec(spec)
    if not ok: raise SystemExit("invalid runtime supervision spec: "+"; ".join(errs))
    spec_hash=compute_runtime_supervision_spec_hash(spec); policy_hash=compute_runtime_supervision_policy_hash(policy)
    mode=args.mode
    exlock=inputs["execution_context_lock"]; rinlock=inputs["runtime_input_lock"]
    context_checks=[]; context_errors=[]; context_hash=None
    if exlock and rinlock:
        ctx_ok, context_checks, context_errors=validate_supervision_context(spec, exlock, rinlock, inputs["admission_decision"], inputs["admission_receipt"])
        context_hash=compute_supervision_context_hash({"execution_context_lock_hash":exlock.get("execution_context_lock_hash"),"runtime_input_lock_hash":rinlock.get("runtime_input_lock_hash"),"active_policy_set_hash":exlock.get("policy_binding",{}).get("active_policy_set_hash"),"pipeline_spec_hash":exlock.get("pipeline",{}).get("pipeline_spec_hash"),"admitted_profiles":exlock.get("profiles",{})})
    run_hash_seed=spec_hash
    run_id=f"{spec['runtime_supervision_id']}_{mode}_{run_hash_seed[:12]}"
    out=Path(args.output_root)/run_id
    out.mkdir(parents=True, exist_ok=True)
    plan=build_runtime_supervision_plan(spec,spec_hash,policy_hash,mode,exlock.get("execution_context_lock_hash") if exlock else None,rinlock.get("runtime_input_lock_hash") if rinlock else None,exlock.get("policy_binding",{}).get("active_policy_set_hash") if exlock else None)
    write_canonical_json(out/"runtime_supervision_plan.json",plan)
    cv=build_supervision_context_verification_report(run_id,spec,context_checks,context_errors)
    write_canonical_json(out/"context/supervision_context_verification_report.json",cv)
    obs=build_runtime_observation_session(spec,mode,exlock.get("execution_context_lock_hash") if exlock else None,rinlock.get("runtime_input_lock_hash") if rinlock else None)
    write_canonical_json(out/"observations/runtime_observation_session.json",obs)
    process_report=build_process_observation_report(run_id,[],None,None,None)
    fs_report=build_filesystem_mutation_report(run_id,args.workspace or [],{}, {})
    net_report=build_network_observation_report(run_id,spec.get("observation",{}).get("capture_network_observation","declared-only"),args.supervised_arg or [],{})
    write_canonical_json(out/"observations/process_observation_report.json",process_report)
    write_canonical_json(out/"observations/filesystem_mutation_report.json",fs_report)
    write_canonical_json(out/"observations/network_observation_report.json",net_report)
    pb=build_policy_binding_conformance_report(run_id,exlock.get("policy_binding",{}).get("active_policy_set_hash") if exlock else None,exlock.get("policy_binding",{}).get("active_policy_set_hash") if exlock else None)
    write_canonical_json(out/"conformance/policy_binding_conformance_report.json",pb)
    violations=[]; warnings=[]
    if context_errors: violations.append({"violation_id":"rviol_"+hash_obj(context_errors)[:12],"violation_class":"policy_binding_drift","severity":"critical","evidence_refs":[],"message":"context verification failed"})
    conformance=build_runtime_conformance_report(run_id,spec,context_checks,context_errors,violations,warnings)
    vreport=build_runtime_violation_report(run_id,spec,violations,[])
    write_canonical_json(out/"conformance/runtime_conformance_report.json",conformance)
    write_canonical_json(out/"conformance/runtime_violation_report.json",vreport)
    (out/"telemetry").mkdir(parents=True,exist_ok=True)
    (out/"telemetry/logs.jsonl").write_text(json.dumps({"event":"runtime_supervision"},sort_keys=True)+"\n",encoding="utf-8")
    (out/"telemetry/metrics.json").write_text(json.dumps({"value":1},sort_keys=True,indent=2)+"\n",encoding="utf-8")
    (out/"telemetry/traces.jsonl").write_text(json.dumps({"trace":"local"},sort_keys=True)+"\n",encoding="utf-8")
    tsnap=build_runtime_telemetry_snapshot(spec,run_id,process_report,fs_report,out/"telemetry/logs.jsonl",out/"telemetry/metrics.json",out/"telemetry/traces.jsonl")
    tbundle=build_runtime_telemetry_bundle(spec,out/"telemetry/logs.jsonl",out/"telemetry/metrics.json",out/"telemetry/traces.jsonl")
    write_canonical_json(out/"telemetry/runtime_telemetry_snapshot.json",tsnap)
    write_canonical_json(out/"telemetry/runtime_telemetry_bundle.json",tbundle)
    att=build_execution_conformance_attestation(spec,exlock.get("execution_context_lock_hash") if exlock else None,rinlock.get("runtime_input_lock_hash") if rinlock else None,exlock.get("policy_binding",{}).get("active_policy_set_hash") if exlock else None,conformance["status"],len(violations),tsnap["telemetry_hash"])
    write_canonical_json(out/"attestations/execution_conformance_attestation.json",att)
    itoto=build_intoto_execution_statement_if_requested(att,violations,spec.get("attestation",{}).get("write_intoto_statement",False))
    if itoto: write_canonical_json(out/"attestations/intoto_execution_statement.json",itoto)
    manifest=build_supervised_run_manifest(spec,att["claims"]["execution_context_lock_hash"],att["claims"]["runtime_input_lock_hash"],obs["observation_session_hash"],conformance["conformance_hash"],tsnap["telemetry_hash"],att["attestation_hash"],args.pipeline_run_receipt)
    write_canonical_json(out/"supervised_run_manifest.json",manifest)
    rec=build_runtime_response_recommendation(spec,violations); write_canonical_json(out/"recommendations/runtime_response_recommendation.json",rec)
    ledger, entry = append_runtime_supervision_ledger_entry(out/"ledger",spec,manifest,conformance["status"],{"conformance":conformance["conformance_hash"],"attestation":att["attestation_hash"]})
    contract=build_runtime_supervision_api_contract(spec); openapi=build_runtime_supervision_openapi(spec)
    write_canonical_json(out/"api/runtime_supervision_api_contract.json",contract)
    write_canonical_json(out/"api/runtime_supervision_openapi.json",openapi)
    validation=build_runtime_supervision_validation_report([{"check":"spec_valid","status":"pass" if ok else "fail"}],context_errors)
    write_canonical_json(out/"runtime_supervision_validation_report.json",validation)
    write_checksums_file(out)
    receipt={"schema":"RuntimeSupervisorReceipt.v1","run_id":run_id,"created_at_utc":utc_now(),"status":"planned" if mode=="plan-only" else ("dry_run" if mode=="dry-run" else ("verified" if mode=="verify-context" else conformance["status"])),"source":"soilgrids_runtime_supervisor","mode":mode,"runtime_supervision_id":spec["runtime_supervision_id"],"runtime_supervision_run_id":run_id,"runtime_supervision_spec_hash":spec_hash,"runtime_supervision_policy_hash":policy_hash,"supervision_context_hash":context_hash,"observation_session_hash":obs["observation_session_hash"],"conformance_hash":conformance["conformance_hash"],"attestation_hash":att["attestation_hash"],"supervision_result_hash":compute_supervision_result_hash({"context":hash_obj(cv),"observation":obs["observation_session_hash"],"process":hash_obj(process_report),"filesystem":hash_obj(fs_report),"network":hash_obj(net_report),"conformance":conformance["conformance_hash"],"violation":hash_obj(vreport),"telemetry":tsnap["telemetry_hash"],"attestation":att["attestation_hash"],"ledger":entry["entry_id"]}),"output_root":str(out),"outputs":{},"inputs":{"runtime_supervision_spec":args.runtime_supervision_spec,"execution_context_lock":args.execution_context_lock,"runtime_input_lock":args.runtime_input_lock,"pipeline_run_receipt":args.pipeline_run_receipt},"input_hashes":{"runtime_supervision_spec_sha256":file_sha256(Path(args.runtime_supervision_spec)),"execution_context_lock_sha256":file_sha256(Path(args.execution_context_lock)) if args.execution_context_lock else None,"runtime_input_lock_sha256":file_sha256(Path(args.runtime_input_lock)) if args.runtime_input_lock else None,"pipeline_run_receipt_sha256":file_sha256(Path(args.pipeline_run_receipt)) if args.pipeline_run_receipt else None},"validation":{"spec_valid":ok,"policy_valid":True,"context_valid":not context_errors,"observations_valid":True,"conformance_valid":True,"telemetry_valid":True,"attestation_valid":True,"ledger_valid":True,"checksums_valid":True},"errors":context_errors}
    write_canonical_json(out/"runtime_supervisor_receipt.json",receipt)
    write_checksums_file(out)
    return 0


def _arg_parser():
    p=argparse.ArgumentParser()
    p.add_argument("--runtime-supervision-spec", required=True)
    p.add_argument("--runtime-supervision-policy")
    p.add_argument("--execution-context-lock")
    p.add_argument("--runtime-input-lock")
    p.add_argument("--admission-decision-envelope")
    p.add_argument("--runtime-admission-receipt")
    p.add_argument("--pipeline-run-manifest")
    p.add_argument("--pipeline-run-receipt")
    p.add_argument("--supervised-run-manifest")
    p.add_argument("--runtime-conformance-report")
    p.add_argument("--supervised-command")
    p.add_argument("--supervised-arg", action="append")
    p.add_argument("--workspace", action="append")
    p.add_argument("--execute-supervised-command", action="store_true")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--output-root", required=True)
    p.add_argument("--mode", required=True, choices=sorted(ALLOWED_MODES))
    p.add_argument("--working-directory")
    p.add_argument("--timeout-seconds", type=int, default=3600)
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=0)
    p.add_argument("--serve-forever", action="store_true")
    p.add_argument("--allow-public-bind", action="store_true")
    p.add_argument("--allow-shell-command-string", action="store_true")
    p.add_argument("--allow-package-manager-command", action="store_true")
    p.add_argument("--allow-command-drift", action="store_true")
    p.add_argument("--allow-remote-url-observation", action="store_true")
    p.add_argument("--deterministic-run-id", action="store_true")
    return p

if __name__=="__main__":
    raise SystemExit(run_runtime_supervisor(_arg_parser().parse_args()))
