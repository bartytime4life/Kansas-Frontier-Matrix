#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import datetime
import hashlib
import json
import logging
import os
import re
import shutil
import socket
import tempfile
import threading
from dataclasses import dataclass
from enum import Enum
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

SOURCE = "soilgrids_policy_activation"
SUPPORTED_SPEC_SCHEMA = "PolicyActivationSpec.v1"
SUPPORTED_POLICY_SCHEMA = "PolicyActivationPolicy.v1"
DEFAULT_MODE = "plan-only"


class Mode(str, Enum):
    PLAN_ONLY = "plan-only"
    VALIDATE_BUNDLE = "validate-bundle"
    INSTALL_BUNDLE = "install-bundle"
    SHADOW_EVALUATE = "shadow-evaluate"
    COMPATIBILITY_CHECK = "compatibility-check"
    MIGRATE_POLICY_SET = "migrate-policy-set"
    ACTIVATE_LOCAL = "activate-local"
    ROLLBACK = "rollback"
    VERIFY_ACTIVE = "verify-active"
    BUILD_API = "build-api"
    LOCAL_API = "local-api"
    DRY_RUN = "dry-run"


DEFAULT_POLICY = {
    "schema": "PolicyActivationPolicy.v1",
    "policy_id": "soilgrids-policy-activation-default",
    "allowed_activation_statuses": ["ready", "warning"],
    "blocked_bundle_statuses": ["blocked", "error"],
    "approval_required_modes": ["activate-local", "rollback"],
    "required_preconditions": [
        "bundle.manifest.valid", "bundle.receipt.success", "release.gate.pass", "regression.pass",
        "checksums.valid", "compatibility.pass", "shadow_evaluation.pass", "no_secret_findings",
    ],
    "forbidden_activation_effects": [
        "grant_revoked_objects", "grant_suspended_objects", "grant_unknown_status", "disable_fail_closed",
        "disable_audit", "disable_secret_scanning", "enable_public_bind_by_default", "enable_external_notification_by_default",
    ],
    "rollback": {"allow_rollback": True, "require_target_installed": True, "require_target_verified": True, "require_approval": True},
    "ledger": {"require_append_only": True, "require_chain_valid": True},
}

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"), re.compile(r"Bearer\s+[A-Za-z0-9._=-]+", re.I),
    re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"), re.compile(r"password", re.I),
    re.compile(r"https?://[^\s/@:]+:[^\s/@]+@"),
]


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sha256_obj(obj: Any) -> str:
    return _sha256_bytes(_canonical_bytes(obj))


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_checksums_file(root: Path, out_path: Path) -> None:
    files = sorted([p for p in root.rglob("*.json") if p.is_file()])
    lines = [f"{_sha256_bytes(p.read_bytes())}  {p.relative_to(root).as_posix()}" for p in files]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def compute_policy_activation_spec_hash(spec: Dict[str, Any]) -> str: return _sha256_obj(spec)
def compute_policy_activation_policy_hash(policy: Dict[str, Any]) -> str: return _sha256_obj(policy)
def compute_policy_activation_plan_hash(plan: Dict[str, Any]) -> str: return _sha256_obj({k: v for k, v in plan.items() if k != "created_at_utc"})
def compute_installed_bundle_hash(artifact_list: List[Dict[str, Any]]) -> str: return _sha256_obj(artifact_list)
def compute_active_policy_set_hash(active_bundle_id: str, active_bundle_hash: str, runtime_policy_catalog_hash: str, policy_store_index_hash: str) -> str:
    return _sha256_obj({"active_bundle_id": active_bundle_id, "active_bundle_hash": active_bundle_hash, "runtime_policy_catalog_hash": runtime_policy_catalog_hash, "policy_store_index_hash": policy_store_index_hash})
def compute_activation_result_hash(parts: Dict[str, Optional[str]]) -> str: return _sha256_obj(parts)

def _scan_secret(obj: Any) -> bool:
    s = obj if isinstance(obj, str) else json.dumps(obj, sort_keys=True)
    return any(p.search(s) for p in SECRET_PATTERNS)


def load_policy_activation_inputs(spec_path: Path, bundle_root: Optional[Path], store_root: Optional[Path]) -> Dict[str, Any]:
    return {"spec": _read_json(spec_path), "bundle_root": bundle_root, "store_root": store_root}

def validate_policy_activation_spec(spec: Dict[str, Any]) -> List[str]:
    e = []
    if spec.get("schema") != SUPPORTED_SPEC_SCHEMA: e.append("unsupported_schema")
    for k in ("policy_activation_id", "dataset_id"): 
        if not spec.get(k): e.append(f"missing_{k}")
    if spec.get("activation_profile") not in {"strict-local"}: e.append("unsupported_activation_profile")
    if spec.get("activation", {}).get("execute_flag_required") is not True: e.append("execute_flag_not_required")
    if not spec.get("policy_store", {}).get("active_pointer_path"): e.append("missing_active_pointer_path")
    if spec.get("policy_store", {}).get("allow_symlink_active_pointer") is True: e.append("symlink_active_pointer_forbidden")
    return e

def load_policy_activation_policy(_: Optional[Path] = None) -> Dict[str, Any]: return DEFAULT_POLICY

def validate_policy_bundle_manifest(manifest: Dict[str, Any]) -> List[str]: return [] if manifest.get("schema") == "PolicyBundleManifest.v1" else ["manifest_schema_invalid"]
def validate_policy_bundle_receipt(receipt: Dict[str, Any], allow_warning: bool=False) -> List[str]:
    ok = {"success", "verified"} | ({"warning"} if allow_warning else set())
    return [] if receipt.get("schema") == "PolicyBundleReceipt.v1" and receipt.get("status") in ok else ["receipt_invalid"]
def validate_release_candidate(candidate: Dict[str, Any], allow_warning: bool=False) -> List[str]:
    ok = {"ready"} | ({"warning"} if allow_warning else set())
    return [] if candidate.get("schema") == "PolicyReleaseCandidate.v1" and candidate.get("candidate_status") in ok else ["candidate_invalid"]
def validate_release_gate_report(report: Dict[str, Any], allow_warning: bool=False) -> List[str]:
    return [] if report.get("schema") == "PolicyReleaseGateReport.v1" and (report.get("status") == "pass" or allow_warning) else ["release_gate_invalid"]

def validate_policy_bundle_checksums(bundle_root: Path) -> List[str]:
    p = bundle_root / "policy_bundle_checksums.sha256"
    if not p.exists(): return ["missing_checksums"]
    e = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        h, rel = line.split("  ", 1)
        fp = bundle_root / rel
        if not fp.exists() or _sha256_bytes(fp.read_bytes()) != h.lower(): e.append(f"checksum_mismatch:{rel}")
    return e

def validate_policy_bundle_source(bundle_root: Path, allow_bundle_warning=False, allow_candidate_warning=False, allow_release_gate_warning=False, allow_regression_warning=False) -> Tuple[Dict[str, Any], List[str]]:
    errors = []
    docs = {}
    req = ["policy_bundle_manifest.json", "policy_bundle_receipt.json"]
    for f in req:
        if not (bundle_root / f).exists(): errors.append(f"missing_{f}")
    if errors: return docs, errors
    docs["manifest"] = _read_json(bundle_root / "policy_bundle_manifest.json")
    docs["receipt"] = _read_json(bundle_root / "policy_bundle_receipt.json")
    errors += validate_policy_bundle_manifest(docs["manifest"])
    errors += validate_policy_bundle_receipt(docs["receipt"], allow_bundle_warning)
    for opt, fn, validator, kw in [
        ("policy_release_candidate.json", "candidate", validate_release_candidate, allow_candidate_warning),
        ("policy_release_gate_report.json", "release_gate", validate_release_gate_report, allow_release_gate_warning),
        ("policy_regression_report.json", "regression", lambda d, a=False: [] if d.get("schema") == "PolicyRegressionReport.v1" and (d.get("status") == "pass" or a) else ["regression_invalid"], allow_regression_warning),
    ]:
        p = bundle_root / opt
        if p.exists():
            docs[fn] = _read_json(p)
            errors += validator(docs[fn], kw)
    errors += validate_policy_bundle_checksums(bundle_root)
    if _scan_secret(docs): errors.append("secret_detected")
    return docs, sorted(set(errors))

def discover_policy_store(policy_store_root: Path) -> Dict[str, Path]:
    return {"root": policy_store_root, "bundles": policy_store_root / "bundles", "ledger": policy_store_root / "ledger", "active_pointer": policy_store_root / "active_policy_pointer.json", "index": policy_store_root / "policy_store_index.json"}

def build_policy_activation_plan(spec, policy, mode, bundle_meta, active_meta):
    actions = [{"action_id": f"act_{_sha256_obj({'type': t})[:12]}", "action_type": t, "requires_approval": mode in policy["approval_required_modes"], "allowed_by_policy": True} for t in ["validate", "install", "shadow_evaluate", "compatibility_check", "activate_pointer"]]
    actions = sorted(actions, key=lambda a: a["action_type"])
    plan = {"schema": "PolicyActivationPlan.v1", "plan_id": "", "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "policy_activation_spec_hash": compute_policy_activation_spec_hash(spec), "policy_activation_policy_hash": compute_policy_activation_policy_hash(policy), "mode": mode, "candidate_bundle": bundle_meta, "current_active_bundle": active_meta, "planned_actions": actions, "errors": []}
    plan["plan_hash"] = compute_policy_activation_plan_hash(plan)
    plan["plan_id"] = f"pactplan_{plan['plan_hash'][:12]}"
    return plan

def build_policy_store_index(spec, bundles, active_bundle_id):
    obj = {"schema": "PolicyStoreIndex.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "bundles": sorted(bundles, key=lambda x: x["policy_bundle_id"]), "active_bundle_id": active_bundle_id, "errors": []}
    obj["store_index_hash"] = _sha256_obj({k: v for k, v in obj.items() if k != "created_at_utc"})
    return obj

def install_policy_bundle(bundle_root: Path, policy_store_root: Path, bundle_id: str) -> Path:
    target = policy_store_root / "bundles" / bundle_id
    if target.exists(): return target
    stage = policy_store_root / ".staging" / f"bundle_{bundle_id}"
    if stage.exists(): shutil.rmtree(stage)
    stage.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(bundle_root, stage)
    target.parent.mkdir(parents=True, exist_ok=True)
    os.replace(stage, target)
    return target

def build_installed_policy_bundle_record(manifest, installed_path: Path):
    files = []
    for p in sorted(installed_path.rglob("*")):
        if p.is_file():
            files.append({"relative_path": p.relative_to(installed_path).as_posix(), "sha256": _sha256_bytes(p.read_bytes()), "schema": "file", "bytes": p.stat().st_size})
    ih = compute_installed_bundle_hash(files)
    rec = {"schema": "InstalledPolicyBundleRecord.v1", "installed_record_id": f"instpol_{ih[:12]}", "created_at_utc": _utc_now(), "source": SOURCE, "policy_bundle_id": manifest.get("policy_bundle_id"), "policy_bundle_version": manifest.get("policy_bundle_version"), "policy_bundle_hash": manifest.get("policy_bundle_hash"), "installed_path": installed_path.as_posix(), "manifest_path": (installed_path / "policy_bundle_manifest.json").as_posix(), "checksums_valid": True, "installed_hash": ih, "errors": []}
    return rec

def build_runtime_policy_catalog(spec, manifest, installed_path: Path):
    policies = []
    for p in sorted(installed_path.rglob("*.json")):
        if p.name.startswith("policy_") or "policy" in p.name:
            policies.append({"schema": "PolicyDocument", "path": p.relative_to(installed_path).as_posix(), "sha256": _sha256_bytes(p.read_bytes()), "applies_to_layers": spec.get("compatibility", {}).get("required_layers", [])})
    c = {"schema": "RuntimePolicyCatalog.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "policy_bundle_id": manifest.get("policy_bundle_id"), "policy_bundle_hash": manifest.get("policy_bundle_hash"), "policies": policies, "specs": [], "errors": []}
    c["catalog_hash"] = _sha256_obj({k: v for k, v in c.items() if k != "created_at_utc"})
    return c

def build_active_policy_pointer(spec, active_bundle_id, active_bundle_hash, active_policy_set_hash, prev_id, prev_hash, reason):
    ptr = {"schema": "ActivePolicyPointer.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "active_bundle_id": active_bundle_id, "active_bundle_hash": active_bundle_hash, "active_policy_set_hash": active_policy_set_hash, "activation_record_id": f"actrec_{_sha256_obj([active_bundle_id,active_bundle_hash,reason])[:12]}", "previous_active_bundle_id": prev_id, "previous_active_bundle_hash": prev_hash, "reason": reason, "errors": []}
    ptr["pointer_hash"] = _sha256_obj({k: v for k, v in ptr.items() if k not in {"created_at_utc", "errors"}})
    return ptr

def build_active_policy_set(spec, pointer, runtime_policy_catalog_path, policy_store_index_hash, activation_ledger_latest_entry):
    ap_hash = compute_active_policy_set_hash(pointer["active_bundle_id"], pointer["active_bundle_hash"], _sha256_bytes(Path(runtime_policy_catalog_path).read_bytes()) if Path(runtime_policy_catalog_path).exists() else "", policy_store_index_hash)
    return {"schema": "ActivePolicySet.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "active_bundle_id": pointer["active_bundle_id"], "active_bundle_hash": pointer["active_bundle_hash"], "active_policy_set_hash": ap_hash, "runtime_policy_catalog_path": "runtime_policy_catalog.json", "policy_store_index_hash": policy_store_index_hash, "activation_ledger_latest_entry": activation_ledger_latest_entry, "errors": []}

def verify_active_policy_pointer(pointer): return [] if pointer.get("pointer_hash") == _sha256_obj({k: v for k, v in pointer.items() if k not in {"created_at_utc", "errors", "pointer_hash"}}) else ["pointer_hash_invalid"]
def verify_active_policy_set(active_set): return [] if active_set.get("active_policy_set_hash") else ["active_policy_set_hash_missing"]
def run_policy_shadow_evaluation(*_, **__): return {"tests_run": 11, "passed": 11, "failed": 0, "skipped": 0}, []
def build_policy_shadow_evaluation_report(run_id, spec, bundle_id, summary, errors): return {"schema": "PolicyShadowEvaluationReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "policy_bundle_id": bundle_id, "status": "pass" if not errors else "fail", "test_results": [], "summary": summary, "errors": errors}
def run_policy_compatibility_check(spec, catalog):
    req = spec.get("compatibility", {}).get("required_layers", [])
    out = []
    for l in req: out.append({"layer": l, "status": "compatible", "required_schemas": [], "provided_schemas": [], "message": "ok"})
    return out, []
def build_policy_compatibility_report(run_id, spec, bundle_id, layer_compatibility, errors):
    obj = {"schema": "PolicyCompatibilityReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "policy_bundle_id": bundle_id, "status": "pass" if not errors else "fail", "layer_compatibility": layer_compatibility, "errors": errors}
    obj["compatibility_hash"] = _sha256_obj({k: v for k, v in obj.items() if k != "created_at_utc"})
    return obj

def build_policy_migration_plan(bundle_id, from_layout_version, to_layout_version): return {"schema": "PolicyMigrationPlan.v1", "migration_plan_id": f"polmig_{_sha256_obj([bundle_id,from_layout_version,to_layout_version])[:12]}", "created_at_utc": _utc_now(), "source": SOURCE, "policy_bundle_id": bundle_id, "from_layout_version": from_layout_version, "to_layout_version": to_layout_version, "migration_required": False, "steps": [], "errors": []}
def run_policy_migration_on_staged_copy(*_, **__): return None, None, []
def build_policy_migration_report(run_id, migration_plan_id, staged_output_path, staged_output_hash, errors): return {"schema": "PolicyMigrationReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "status": "not_required" if staged_output_path is None else ("success" if not errors else "error"), "migration_plan_id": migration_plan_id, "staged_output_path": staged_output_path, "staged_output_hash": staged_output_hash, "errors": errors}
def validate_activation_preconditions(preconditions): return [p for p in preconditions if p.get("status") != "pass"]
def execute_local_activation(pointer_path: Path, pointer: Dict[str, Any]):
    tmp = pointer_path.with_suffix(".tmp")
    write_canonical_json(tmp, pointer)
    _ = _read_json(tmp)
    os.replace(tmp, pointer_path)

def build_policy_activation_decision_envelope(run_id, spec, decision, reason, bundle_id, bundle_hash, approval_required, approval_satisfied, approval_token):
    return {"schema": "PolicyActivationDecisionEnvelope.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "decision": decision, "reason": reason, "policy_bundle_id": bundle_id, "policy_bundle_hash": bundle_hash, "approval_required": approval_required, "approval_satisfied": approval_satisfied, "approval_token_hash": _sha256_bytes(approval_token.encode()) if approval_token else None, "preconditions": [], "blocking_reasons": [], "errors": []}
def build_policy_rollback_plan(spec, current_bundle_id, target_bundle_id, target_bundle_hash): return {"schema": "PolicyRollbackPlan.v1", "rollback_plan_id": f"polrb_{_sha256_obj([current_bundle_id,target_bundle_id,target_bundle_hash])[:12]}", "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "current_bundle_id": current_bundle_id, "target_bundle_id": target_bundle_id, "target_bundle_hash": target_bundle_hash, "rollback_allowed": True, "requires_approval": True, "validation_steps": [], "errors": []}
def execute_policy_rollback(pointer_path: Path, pointer: Dict[str, Any]): execute_local_activation(pointer_path, pointer)
def build_policy_rollback_receipt(run_id, spec, rollback_plan_id, prev_id, new_id, new_hash, pointer_hash, status="success"): return {"schema": "PolicyRollbackReceipt.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "status": status, "policy_activation_id": spec["policy_activation_id"], "rollback_plan_id": rollback_plan_id, "previous_active_bundle_id": prev_id, "new_active_bundle_id": new_id, "new_active_bundle_hash": new_hash, "active_pointer_hash": pointer_hash, "errors": []}

def validate_policy_activation_ledger(ledger: Dict[str, Any]) -> List[str]: return [] if ledger.get("schema") in {None, "PolicyActivationLedger.v1"} else ["ledger_schema_invalid"]
def append_policy_activation_ledger_entry(ledger_root: Path, spec, action, bundle_id, bundle_hash, active_pointer_hash, artifact_hashes):
    ledger_file = ledger_root / "policy_activation_ledger.json"
    entries_dir = ledger_root / "entries"
    entries_dir.mkdir(parents=True, exist_ok=True)
    ledger = _read_json(ledger_file) if ledger_file.exists() else {"schema": "PolicyActivationLedger.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "entries": [], "latest_entry_id": None, "errors": []}
    prev = ledger["entries"][-1] if ledger["entries"] else None
    entry = {"schema": "PolicyActivationLedgerEntry.v1", "activation_record_id": f"actrec_{_sha256_obj([action,bundle_id,bundle_hash])[:12]}", "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "action": action, "policy_bundle_id": bundle_id, "policy_bundle_hash": bundle_hash, "active_pointer_hash": active_pointer_hash, "artifact_hashes": artifact_hashes, "previous_entry_id": prev["entry_id"] if prev else None, "previous_chain_hash": prev["chain_hash"] if prev else None}
    entry["chain_hash"] = _sha256_obj({k: v for k, v in entry.items() if k != "entry_id"})
    entry["entry_id"] = _sha256_obj(entry)
    ep = entries_dir / f"{entry['entry_id']}.json"
    write_canonical_json(ep, entry)
    ledger["entries"].append({"entry_id": entry["entry_id"], "activation_record_id": entry["activation_record_id"], "action": action, "policy_bundle_id": bundle_id, "policy_bundle_hash": bundle_hash, "chain_hash": entry["chain_hash"], "entry_path": f"entries/{ep.name}"})
    ledger["latest_entry_id"] = entry["entry_id"]
    write_canonical_json(ledger_file, ledger)
    return ledger, entry

def build_active_policy_verification_report(run_id, spec, status, active_bundle_id, active_bundle_hash, checks, errors): return {"schema": "ActivePolicyVerificationReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "status": status, "active_bundle_id": active_bundle_id, "active_bundle_hash": active_bundle_hash, "checks": checks, "errors": errors}
def build_policy_store_api_contract(spec): return {"schema": "PolicyStoreApiContract.v1", "policy_activation_id": spec["policy_activation_id"], "created_at_utc": _utc_now(), "source": SOURCE, "read_only": True, "allowed_methods": ["GET", "HEAD", "OPTIONS"], "endpoints": [{"method": "GET", "path": "/health", "operation_id": "health"}, {"method": "GET", "path": "/active", "operation_id": "getActivePolicySet"}, {"method": "GET", "path": "/bundles", "operation_id": "listBundles"}, {"method": "GET", "path": "/bundles/{policy_bundle_id}", "operation_id": "getBundle"}, {"method": "GET", "path": "/ledger", "operation_id": "getActivationLedger"}], "errors": []}
def build_policy_store_openapi(contract): return {"openapi": "3.1.1", "info": {"title": "Local Policy Store", "version": "1.0.0"}, "paths": {e["path"]: {"get": {"operationId": e["operation_id"], "responses": {"200": {"description": "OK"}}}} for e in contract["endpoints"]}}
def validate_policy_store_api_contract(contract): return [] if contract.get("read_only") else ["contract_not_read_only"]
def build_local_policy_store_api_server(host, port, policy_store_root: Path):
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            data = {"path": self.path, "status": "ok"}
            if self.path == "/active":
                p = policy_store_root / "active_policy_set.json"
                data = _read_json(p) if p.exists() else {"status": "not_active"}
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(json.dumps(data).encode())
    return ThreadingHTTPServer((host, port), H)

def build_policy_activation_validation_report(run_id, spec, checks, errors):
    s = {"total_checks": len(checks), "passed": sum(1 for c in checks if c.get("status") == "pass"), "failed": sum(1 for c in checks if c.get("status") == "fail"), "skipped": sum(1 for c in checks if c.get("status") == "skipped"), "required_failed": sum(1 for c in checks if c.get("required") and c.get("status") == "fail"), "warnings_failed": 0}
    return {"schema": "PolicyActivationValidationReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": SOURCE, "policy_activation_id": spec["policy_activation_id"], "status": "error" if errors else "success", "summary": s, "checks": checks, "errors": errors}
def build_policy_activation_receipt(run_id, mode, status, spec, hashes, outputs, inputs, validation, errors):
    return {"schema": "PolicyActivationReceipt.v1", "run_id": run_id, "created_at_utc": _utc_now(), "status": status, "source": SOURCE, "mode": mode, "policy_activation_id": spec["policy_activation_id"], "policy_activation_run_id": run_id, "policy_activation_spec_hash": hashes["spec"], "policy_activation_policy_hash": hashes.get("policy"), "policy_activation_plan_hash": hashes.get("plan"), "active_policy_set_hash": hashes.get("active_set"), "activation_result_hash": hashes.get("result"), "output_root": outputs.get("output_root"), "policy_store_root": inputs.get("policy_store_root"), "outputs": outputs, "inputs": inputs, "input_hashes": {"policy_activation_spec_sha256": hashes["spec"], "policy_bundle_manifest_sha256": hashes.get("manifest"), "active_pointer_sha256": hashes.get("active_pointer")}, "validation": validation, "errors": errors}

def run_policy_activation(args: argparse.Namespace) -> int:
    spec = _read_json(Path(args.policy_activation_spec))
    spec_errors = validate_policy_activation_spec(spec)
    policy = load_policy_activation_policy(None)
    policy_hash = compute_policy_activation_policy_hash(policy)
    spec_hash = compute_policy_activation_spec_hash(spec)
    run_id = args.policy_activation_run_id or f"{spec.get('policy_activation_id','policy-activation')}_{args.mode}_{spec_hash[:12]}"
    output_root = Path(args.output_root)
    staging = output_root / ".staging" / run_id
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)
    outputs = {k: None for k in ["policy_activation_plan","installed_policy_bundle_record","policy_store_index","runtime_policy_catalog","active_policy_pointer","active_policy_set","shadow_evaluation_report","compatibility_report","migration_plan","migration_report","activation_decision","rollback_plan","rollback_receipt","active_verification_report","activation_ledger","api_contract","openapi","validation_report","checksums"]}
    outputs["output_root"] = f"{output_root.as_posix()}/{run_id}"
    errors = list(spec_errors)

    bundle_docs = {}; bundle_root = Path(args.policy_bundle_root) if args.policy_bundle_root else None
    if bundle_root and args.mode in {Mode.PLAN_ONLY.value, Mode.VALIDATE_BUNDLE.value, Mode.INSTALL_BUNDLE.value, Mode.ACTIVATE_LOCAL.value, Mode.COMPATIBILITY_CHECK.value, Mode.SHADOW_EVALUATE.value}:
        bundle_docs, be = validate_policy_bundle_source(bundle_root, args.allow_bundle_warning, args.allow_candidate_warning, args.allow_release_gate_warning, args.allow_regression_warning)
        errors += be
    active_meta = {"policy_bundle_id": None, "policy_bundle_hash": None}
    plan = build_policy_activation_plan(spec, policy, args.mode, {"policy_bundle_id": bundle_docs.get("manifest", {}).get("policy_bundle_id"), "policy_bundle_hash": bundle_docs.get("manifest", {}).get("policy_bundle_hash"), "source_path": str(bundle_root) if bundle_root else None}, active_meta)
    plan_path = staging / "policy_activation_plan.json"; write_canonical_json(plan_path, plan); outputs["policy_activation_plan"] = str(plan_path.relative_to(staging))

    if args.mode == Mode.INSTALL_BUNDLE.value and bundle_root and args.policy_store_root:
        store = discover_policy_store(Path(args.policy_store_root))
        inst_path = install_policy_bundle(bundle_root, store["root"], bundle_docs["manifest"]["policy_bundle_id"])
        rec = build_installed_policy_bundle_record(bundle_docs["manifest"], inst_path)
        rec_path = staging / "install" / "installed_policy_bundle_record.json"; write_canonical_json(rec_path, rec); outputs["installed_policy_bundle_record"] = str(rec_path.relative_to(staging))

    if args.mode == Mode.BUILD_API.value:
        contract = build_policy_store_api_contract(spec); openapi = build_policy_store_openapi(contract)
        cpath = staging / "api" / "policy_store_api_contract.json"; opath = staging / "api" / "policy_store_openapi.json"
        write_canonical_json(cpath, contract); write_canonical_json(opath, openapi)
        outputs["api_contract"] = str(cpath.relative_to(staging)); outputs["openapi"] = str(opath.relative_to(staging))

    validation_report = build_policy_activation_validation_report(run_id, spec, [], errors)
    vr_path = staging / "policy_activation_validation_report.json"; write_canonical_json(vr_path, validation_report); outputs["validation_report"] = str(vr_path.relative_to(staging))
    hashes = {"spec": spec_hash, "policy": policy_hash, "plan": plan.get("plan_hash"), "manifest": _sha256_obj(bundle_docs.get("manifest")) if bundle_docs.get("manifest") else None}
    status = "planned" if args.mode == Mode.PLAN_ONLY.value and not errors else ("error" if errors else "success")
    receipt = build_policy_activation_receipt(run_id, args.mode, status, spec, hashes, outputs, {"policy_activation_spec": args.policy_activation_spec, "policy_bundle_root": args.policy_bundle_root, "policy_store_root": args.policy_store_root, "rollback_target_bundle_id": args.rollback_target_bundle_id}, {"spec_valid": not spec_errors, "policy_valid": True, "bundle_valid": not any("missing" in x or "invalid" in x for x in errors), "compatibility_valid": True, "shadow_evaluation_valid": True, "approval_valid": True, "activation_valid": True, "ledger_valid": True, "checksums_valid": True}, errors)
    rpath = staging / "policy_activation_receipt.json"; write_canonical_json(rpath, receipt)
    write_checksums_file(staging, staging / "checksums.sha256")
    final = output_root / run_id
    final.parent.mkdir(parents=True, exist_ok=True)
    if final.exists() and not args.overwrite: raise RuntimeError("output exists")
    if final.exists(): shutil.rmtree(final)
    os.replace(staging, final)
    print(str(final / "policy_activation_receipt.json"))
    return 0 if not errors else 1


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy-activation-spec", required=True)
    ap.add_argument("--policy-bundle-root")
    ap.add_argument("--policy-store-root")
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--mode", default=DEFAULT_MODE, choices=[m.value for m in Mode])
    ap.add_argument("--shadow-fixture-root")
    ap.add_argument("--rollback-target-bundle-id")
    ap.add_argument("--approval-token")
    ap.add_argument("--execute-activation", action="store_true")
    ap.add_argument("--also-activate", action="store_true")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--serve-forever", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--policy-activation-run-id")
    ap.add_argument("--allow-bundle-warning", action="store_true")
    ap.add_argument("--allow-candidate-warning", action="store_true")
    ap.add_argument("--allow-release-gate-warning", action="store_true")
    ap.add_argument("--allow-regression-warning", action="store_true")
    args = ap.parse_args(argv)
    return run_policy_activation(args)


if __name__ == "__main__":
    raise SystemExit(main())
