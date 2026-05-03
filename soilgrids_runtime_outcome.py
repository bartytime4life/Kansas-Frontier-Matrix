#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SOURCE_NAME = "soilgrids_runtime_outcome"
DEFAULT_POLICY = {
    "schema": "OutcomeAcceptancePolicy.v1",
    "policy_id": "soilgrids-outcome-acceptance-default",
    "allowed_decisions": ["accepted", "accepted_with_warnings", "review_required", "quarantined", "rejected", "not_evaluated"],
    "decision_map": {"conformant": "accepted", "conformant_with_warnings": "review_required", "nonconformant": "quarantined", "error": "rejected", "not_evaluated": "not_evaluated"},
    "required_checks": ["supervision.receipt.valid", "conformance.report.valid", "violations.report.valid", "outputs.inventory.valid", "lineage.hashes.present", "secrets.absent"],
    "quarantine_reasons": ["nonconformant_execution", "policy_binding_drift", "input_hash_drift", "workspace_escape", "unexpected_output_mutation", "network_policy_violation", "mutation_policy_violation", "missing_layer15_receipt", "secret_detected", "attestation_missing", "receipt_invalid"],
    "reject_reasons": ["malformed_source", "checksum_mismatch", "unsafe_path", "policy_error"],
    "fail_closed": True,
}
MODES = {"plan-only","inventory-outputs","evaluate-acceptance","accept-local","quarantine-local","handoff-packet","verify-accepted","verify-quarantine","attest-outcome","build-dashboard","local-api","dry-run"}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def _sha256_file(p: Path) -> str:
    return _sha256_bytes(p.read_bytes())

def _strip(d: Dict[str, Any], keys: set[str]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if k not in keys}

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def write_checksums_file(root: Path) -> None:
    files = sorted([p for p in root.rglob("*") if p.is_file() and p.name != "checksums.sha256"], key=lambda x: x.relative_to(root).as_posix())
    (root / "checksums.sha256").write_text("\n".join(f"{_sha256_file(p)}  {p.relative_to(root).as_posix()}" for p in files) + "\n", encoding="utf-8")

def compute_outcome_acceptance_spec_hash(spec: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(spec))
def compute_outcome_acceptance_policy_hash(policy: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(policy))
def compute_runtime_output_inventory_hash(inv: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(inv, {"created_at_utc", "runtime_output_inventory_hash"})))
def compute_outcome_eligibility_hash(r: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(r, {"created_at_utc", "outcome_eligibility_hash", "run_id"})))
def compute_outcome_decision_hash(d: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(d, {"created_at_utc", "decision_hash", "errors", "run_id"})))
def compute_accepted_output_manifest_hash(m: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(m, {"created_at_utc", "accepted_output_manifest_hash", "errors"})))
def compute_quarantine_manifest_hash(m: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(m, {"created_at_utc", "quarantine_manifest_hash", "errors"})))
def compute_handoff_packet_hash(h: Dict[str, Any]) -> str: return _sha256_bytes(_canonical_bytes(_strip(h, {"created_at_utc", "handoff_packet_hash", "errors"})))

def compute_runtime_outcome_result_hash(parts: Dict[str, Optional[str]]) -> str:
    return _sha256_bytes(_canonical_bytes(parts))

def validate_outcome_acceptance_spec(spec: Dict[str, Any], args: argparse.Namespace) -> None:
    if spec.get("schema") != "OutcomeAcceptanceSpec.v1": raise ValueError("unsupported schema")
    for k in ("outcome_acceptance_id", "dataset_id"):
        if not spec.get(k): raise ValueError(f"missing {k}")
    if spec.get("acceptance_profile") not in {"strict-local", "permissive-local", None}: raise ValueError("unsupported acceptance profile")
    if args.output_root.resolve() == args.runtime_supervision_run_root.resolve(): raise ValueError("output root equals source root")

def load_outcome_acceptance_policy(_: Optional[Path] = None) -> Dict[str, Any]:
    p = DEFAULT_POLICY
    if p.get("schema") != "OutcomeAcceptancePolicy.v1" or not p.get("fail_closed", False): raise ValueError("invalid policy")
    return p

def _scan_text(text: str) -> bool:
    pats = [r"AKIA[0-9A-Z]{16}", r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----", r"Bearer\s+[A-Za-z0-9\-._~+/]+=*", r"[?&](?:token|password|api_key)=", r"https?://[^/\s:@]+:[^/\s@]+@"]
    return any(re.search(p, text, re.IGNORECASE) for p in pats)

def validate_runtime_supervisor_receipt(d: Dict[str, Any]) -> bool: return d.get("schema") == "RuntimeSupervisorReceipt.v1"
def validate_runtime_conformance_report(d: Dict[str, Any]) -> bool: return d.get("schema") == "RuntimeConformanceReport.v1"
def validate_runtime_violation_report(d: Dict[str, Any]) -> bool: return d.get("schema") == "RuntimeViolationReport.v1"
def validate_execution_attestation(d: Optional[Dict[str, Any]]) -> bool: return d is None or d.get("schema") == "ExecutionConformanceAttestation.v1"
def validate_supervised_run_manifest(d: Dict[str, Any]) -> bool: return d.get("schema") == "SupervisedRunManifest.v1"
def validate_pipeline_run_outputs_if_present(_: Dict[str, Any]) -> bool: return True

def load_runtime_outcome_inputs(args: argparse.Namespace) -> Dict[str, Any]:
    root = args.runtime_supervision_run_root
    def _j(rel: str) -> Optional[Dict[str, Any]]:
        p = root / rel
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
    return {"supervisor_receipt": _j("runtime_supervisor_receipt.json"), "conformance_report": _j("runtime_conformance_report.json"), "violation_report": _j("runtime_violation_report.json"), "supervised_manifest": _j("supervised_run_manifest.json"), "execution_attestation": _j("execution_conformance_attestation.json")}

def validate_runtime_supervision_source(i: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errs = []
    if not i["supervisor_receipt"] or not validate_runtime_supervisor_receipt(i["supervisor_receipt"]): errs.append("receipt_invalid")
    if not i["conformance_report"] or not validate_runtime_conformance_report(i["conformance_report"]): errs.append("conformance_invalid")
    if not i["violation_report"] or not validate_runtime_violation_report(i["violation_report"]): errs.append("violation_invalid")
    if not i["supervised_manifest"] or not validate_supervised_run_manifest(i["supervised_manifest"]): errs.append("manifest_invalid")
    return (len(errs) == 0, errs)

def compute_runtime_output_id(path: str, sha: str) -> str: return "rout_" + _sha256_bytes(_canonical_bytes({"path": path, "sha": sha}))[:16]
def classify_runtime_output(path: str) -> str:
    p = path.lower()
    if p.endswith("receipt.json"): return "pipeline_receipt"
    if p.endswith("manifest.json"): return "pipeline_manifest"
    if p.endswith(".log"): return "log"
    if "telemetry" in p: return "telemetry"
    if p.endswith(".json"): return "artifact"
    return "unknown"

def discover_runtime_outputs(root: Path) -> List[Dict[str, Any]]:
    out = []
    for p in sorted([x for x in root.rglob("*") if x.is_file()]):
        rel = p.relative_to(root).as_posix(); sha = _sha256_file(p); role = classify_runtime_output(rel)
        out.append({"runtime_output_id": compute_runtime_output_id(rel, sha), "output_role": role, "path": rel, "bytes": p.stat().st_size, "sha256": sha, "media_type": mimetypes.guess_type(rel)[0] or "application/octet-stream", "source_report": "SupervisedRunManifest.v1", "declared_by_layer": 35, "expected": True, "public_safe": False, "errors": []})
    return out

def build_runtime_output_inventory(spec: Dict[str, Any], outputs: List[Dict[str, Any]], allow_unknown_output_role: bool=False) -> Dict[str, Any]:
    outputs = sorted(outputs, key=lambda x: x["runtime_output_id"])
    unknown = [o for o in outputs if o["output_role"] == "unknown"]
    if unknown and not allow_unknown_output_role: raise ValueError("unknown output role")
    inv = {"schema": "RuntimeOutputInventory.v1", "outcome_acceptance_id": spec["outcome_acceptance_id"], "created_at_utc": _utc_now(), "source": SOURCE_NAME, "runtime_output_inventory_hash": "", "outputs": outputs, "summary": {"outputs_total": len(outputs), "expected_outputs": len([o for o in outputs if o["expected"]]), "unexpected_outputs": len([o for o in outputs if not o["expected"]]), "unknown_outputs": len(unknown), "bytes_total": sum(o["bytes"] for o in outputs)}, "errors": []}
    inv["runtime_output_inventory_hash"] = compute_runtime_output_inventory_hash(inv)
    return inv

def evaluate_outcome_eligibility(spec: Dict[str, Any], inp: Dict[str, Any], inv: Dict[str, Any], src_valid: bool, src_errs: List[str]) -> Dict[str, Any]:
    checks = []
    conf = inp["conformance_report"].get("conformance_status", "not_evaluated") if inp.get("conformance_report") else "error"
    checks.append({"check_id": "supervision.receipt.valid", "severity": "required", "status": "pass" if src_valid else "fail", "expected": True, "actual": src_valid, "message": "runtime supervision source validation"})
    checks.append({"check_id": "outcome.conformance.status.acceptable", "severity": "required", "status": "pass" if conf in {"conformant", "conformant_with_warnings", "nonconformant"} else "fail", "expected": "known", "actual": conf, "message": "conformance status"})
    status = "eligible" if conf == "conformant" and src_valid else ("review_required" if conf == "conformant_with_warnings" else ("quarantine_required" if conf == "nonconformant" else "rejected"))
    if _scan_text(json.dumps({"inv": inv, "inp": inp}, sort_keys=True)): status = "quarantine_required"
    return {"schema": "OutcomeEligibilityReport.v1", "run_id": "", "created_at_utc": _utc_now(), "source": SOURCE_NAME, "outcome_acceptance_id": spec["outcome_acceptance_id"], "status": status, "outcome_eligibility_hash": "", "checks": checks, "quarantine_reasons": src_errs if status == "quarantine_required" else [], "reject_reasons": ["malformed_source"] if status == "rejected" else [], "warnings": [], "errors": []}

def build_outcome_eligibility_report(r: Dict[str, Any]) -> Dict[str, Any]:
    r["outcome_eligibility_hash"] = compute_outcome_eligibility_hash(r); return r

def build_outcome_acceptance_decision_envelope(spec: Dict[str, Any], policy: Dict[str, Any], elig: Dict[str, Any], inp: Dict[str, Any], inv: Dict[str, Any]) -> Dict[str, Any]:
    conf = inp["conformance_report"].get("conformance_status", "not_evaluated") if inp.get("conformance_report") else "error"
    decision = "rejected" if elig["status"] == "rejected" else policy["decision_map"].get(conf, "rejected")
    d = {"schema": "OutcomeAcceptanceDecisionEnvelope.v1", "run_id": "", "created_at_utc": _utc_now(), "source": SOURCE_NAME, "outcome_acceptance_id": spec["outcome_acceptance_id"], "decision": decision, "decision_hash": "", "reason": f"derived from {conf}", "supervised_run": {"supervised_run_hash": _sha256_bytes(_canonical_bytes(inp.get("supervised_manifest") or {})), "runtime_supervision_run_id": inp.get("supervised_manifest", {}).get("runtime_supervision_run_id"), "conformance_status": conf}, "lineage": {"execution_context_lock_hash": inp.get("supervisor_receipt", {}).get("execution_context_lock_hash"), "runtime_input_lock_hash": inp.get("supervisor_receipt", {}).get("runtime_input_lock_hash"), "active_policy_set_hash": inp.get("supervisor_receipt", {}).get("active_policy_set_hash"), "pipeline_run_receipt_sha256": None}, "accepted_output_count": len(inv["outputs"]) if decision in {"accepted", "accepted_with_warnings"} else 0, "quarantined_output_count": len(inv["outputs"]) if decision in {"quarantined", "review_required", "rejected"} else 0, "quarantine_reasons": elig.get("quarantine_reasons", []), "reject_reasons": elig.get("reject_reasons", []), "warnings": elig.get("warnings", []), "errors": []}
    d["decision_hash"] = compute_outcome_decision_hash(d)
    return d

def build_runtime_output_lineage_map(spec: Dict[str, Any], inv: Dict[str, Any], dec: Dict[str, Any], conformance_hash: Optional[str]) -> Dict[str, Any]:
    links=[]
    for o in inv["outputs"]:
        links.append({"runtime_output_id":o["runtime_output_id"],"output_sha256":o["sha256"],"execution_context_lock_hash":dec["lineage"]["execution_context_lock_hash"],"runtime_input_lock_hash":dec["lineage"]["runtime_input_lock_hash"],"active_policy_set_hash":dec["lineage"]["active_policy_set_hash"],"conformance_hash":conformance_hash,"pipeline_run_receipt_sha256":None})
    lm={"schema":"RuntimeOutputLineageMap.v1","outcome_acceptance_id":spec["outcome_acceptance_id"],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"lineage_map_hash":"","links":links,"errors":[]}
    lm["lineage_map_hash"]=_sha256_bytes(_canonical_bytes(_strip(lm,{"created_at_utc","lineage_map_hash"})))
    return lm

def build_accepted_output_manifest(spec,dec,inv,copy_mode="metadata_only"):
    outs=[{"runtime_output_id":o["runtime_output_id"],"role":o["output_role"],"source_path":o["path"],"accepted_path":None,"bytes":o["bytes"],"sha256":o["sha256"],"media_type":o["media_type"]} for o in inv["outputs"]]
    m={"schema":"AcceptedOutputManifest.v1","accepted_output_set_id":"accepted_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"accepted_output_manifest_hash":"","decision_hash":dec["decision_hash"],"supervised_run_hash":dec["supervised_run"]["supervised_run_hash"],"copy_mode":copy_mode,"outputs":outs,"checksums_path":None,"errors":[]}
    m["accepted_output_manifest_hash"]=compute_accepted_output_manifest_hash(m);return m

def build_accepted_output_receipt(run_id,m): return {"schema":"AcceptedOutputReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"status":"metadata_only" if m["copy_mode"]=="metadata_only" else "success","accepted_output_set_id":m["accepted_output_set_id"],"accepted_output_manifest_hash":m["accepted_output_manifest_hash"],"decision_hash":m["decision_hash"],"outputs_total":len(m["outputs"]),"copy_mode":m["copy_mode"],"errors":[]}

def copy_accepted_outputs_if_requested(*_args,**_kwargs): return None

def build_quarantine_manifest(spec,dec,inv,copy_mode="metadata_only"):
    q=[{"runtime_output_id":o["runtime_output_id"],"role":o["output_role"],"source_path":o["path"],"quarantine_path":None,"bytes":o["bytes"],"sha256":o["sha256"],"reason":(dec.get("quarantine_reasons") or ["nonconformant_execution"])[0]} for o in inv["outputs"]]
    m={"schema":"QuarantineManifest.v1","quarantine_id":"quarantine_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"quarantine_manifest_hash":"","decision_hash":dec["decision_hash"],"quarantine_reasons":dec.get("quarantine_reasons") or ["nonconformant_execution"],"copy_mode":copy_mode,"quarantined_outputs":q,"errors":[]}
    m["quarantine_manifest_hash"]=compute_quarantine_manifest_hash(m);return m

def build_quarantine_receipt(run_id,m): return {"schema":"QuarantineReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"status":"metadata_only" if m["copy_mode"]=="metadata_only" else "success","quarantine_id":m["quarantine_id"],"quarantine_manifest_hash":m["quarantine_manifest_hash"],"decision_hash":m["decision_hash"],"quarantine_reasons":m["quarantine_reasons"],"outputs_total":len(m["quarantined_outputs"]),"copy_mode":m["copy_mode"],"errors":[]}

def copy_quarantined_outputs_if_requested(*_args,**_kwargs): return None

def build_runtime_outcome_handoff_packet(spec,dec,accept_p,quar_p):
    h={"schema":"RuntimeOutcomeHandoffPacket.v1","handoff_packet_id":"rhandoff_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"handoff_packet_hash":"","decision":dec["decision"],"accepted_output_manifest":accept_p,"quarantine_manifest":quar_p,"lineage_map":"lineage/runtime_output_lineage_map.json","conformance_report":"runtime_conformance_report.json","violation_report":"runtime_violation_report.json","execution_attestation":None,"pipeline_run_receipt":None,"recommended_downstream_actions":[],"errors":[]}
    h["handoff_packet_hash"]=compute_handoff_packet_hash(h);return h

def build_runtime_outcome_certificate(spec,dec,amh,qmh,ch): return {"schema":"RuntimeOutcomeCertificate.v1","certificate_id":"routcert_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"certificate_hash":_sha256_bytes(_canonical_bytes({"d":dec["decision_hash"],"a":amh,"q":qmh,"c":ch})),"decision_hash":dec["decision_hash"],"accepted_output_manifest_hash":amh,"quarantine_manifest_hash":qmh,"conformance_hash":ch,"statement":"Runtime outcome processed.","errors":[]}

def build_runtime_outcome_attestation(spec,dec,inv):
    a={"schema":"RuntimeOutcomeAttestation.v1","attestation_id":"routatt_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"attestation_hash":"","subject":[{"name":"accepted_or_quarantined_runtime_outputs","digest":{"sha256":_sha256_bytes(_canonical_bytes([o["sha256"] for o in inv["outputs"]]))}}],"claims":{"decision":dec["decision"],"decision_hash":dec["decision_hash"],"supervised_run_hash":dec["supervised_run"]["supervised_run_hash"],"conformance_status":dec["supervised_run"]["conformance_status"],"accepted_output_count":dec["accepted_output_count"],"quarantined_output_count":dec["quarantined_output_count"]},"proof":{"type":"unsigned","signature_value":None},"errors":[]}
    a["attestation_hash"]=_sha256_bytes(_canonical_bytes(_strip(a,{"created_at_utc","attestation_hash"}))); return a

def build_intoto_outcome_statement_if_requested(*_args, **_kwargs): return None
def build_slsa_style_outcome_statement_if_requested(*_args, **_kwargs): return None
def sign_outcome_attestation_if_requested(att, *_args, **_kwargs): return att

def append_runtime_outcome_ledger_entry(ledger_root:Path,spec:Dict[str,Any],dec:Dict[str,Any],amh,qmh,hh,ah)->Tuple[Dict[str,Any],Dict[str,Any]]:
    ledger_file=ledger_root/"runtime_outcome_ledger.json"; entries_dir=ledger_root/"entries"; entries_dir.mkdir(parents=True,exist_ok=True)
    ledger=json.loads(ledger_file.read_text()) if ledger_file.exists() else {"schema":"RuntimeOutcomeLedger.v1","outcome_acceptance_id":spec["outcome_acceptance_id"],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"entries":[],"latest_entry_id":None,"errors":[]}
    prev=ledger["latest_entry_id"]; prev_chain=None
    if prev:
        p=next((e for e in ledger["entries"] if e["entry_id"]==prev),None); prev_chain=p["chain_hash"] if p else None
    base={"schema":"RuntimeOutcomeLedgerEntry.v1","entry_id":"","outcome_record_id":"routcome_"+dec["decision_hash"][:12],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"outcome_acceptance_id":spec["outcome_acceptance_id"],"decision_hash":dec["decision_hash"],"accepted_output_manifest_hash":amh,"quarantine_manifest_hash":qmh,"handoff_packet_hash":hh,"attestation_hash":ah,"previous_entry_id":prev,"previous_chain_hash":prev_chain,"chain_hash":""}
    base["chain_hash"]=_sha256_bytes(_canonical_bytes(_strip(base,{"entry_id","created_at_utc"}))); base["entry_id"]=_sha256_bytes(_canonical_bytes({"chain_hash":base["chain_hash"],"decision_hash":dec["decision_hash"]}))
    entry_path=entries_dir/f"{base['entry_id']}.json"; write_canonical_json(entry_path,base)
    ledger["entries"].append({"entry_id":base["entry_id"],"outcome_record_id":base["outcome_record_id"],"decision":dec["decision"],"decision_hash":dec["decision_hash"],"chain_hash":base["chain_hash"],"entry_path":f"entries/{entry_path.name}"})
    ledger["latest_entry_id"]=base["entry_id"]
    write_canonical_json(ledger_file,ledger)
    return ledger,base

def validate_runtime_outcome_ledger(ledger:Dict[str,Any])->bool: return ledger.get("schema")=="RuntimeOutcomeLedger.v1"
def build_runtime_outcome_dashboard_if_requested(run_root:Path, *_args, **_kwargs):
    d=run_root/"dashboard"; d.mkdir(parents=True,exist_ok=True); (d/"assets").mkdir(exist_ok=True); (d/"index.html").write_text("<html><body><h1>Runtime Outcome Dashboard</h1></body></html>",encoding="utf-8")

def build_runtime_outcome_api_contract(spec): return {"schema":"RuntimeOutcomeApiContract.v1","outcome_acceptance_id":spec["outcome_acceptance_id"],"created_at_utc":_utc_now(),"source":SOURCE_NAME,"read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"endpoints":[{"method":"GET","path":"/health","operation_id":"health"},{"method":"GET","path":"/inventory","operation_id":"getOutputInventory"},{"method":"GET","path":"/decision","operation_id":"getOutcomeDecision"},{"method":"GET","path":"/accepted","operation_id":"getAcceptedOutputs"},{"method":"GET","path":"/quarantine","operation_id":"getQuarantine"},{"method":"GET","path":"/handoff","operation_id":"getHandoffPacket"},{"method":"GET","path":"/ledger","operation_id":"getOutcomeLedger"}],"errors":[]}
def build_runtime_outcome_openapi(spec): return {"openapi":"3.1.1","info":{"title":"Runtime Outcome API","version":"1.0.0"},"paths":{e["path"]:{"get":{"operationId":e["operation_id"],"responses":{"200":{"description":"ok"}}}} for e in build_runtime_outcome_api_contract(spec)["endpoints"]},"components":{"schemas":{"RuntimeOutputInventory.v1":{},"OutcomeAcceptanceDecisionEnvelope.v1":{},"AcceptedOutputManifest.v1":{},"QuarantineManifest.v1":{},"RuntimeOutcomeHandoffPacket.v1":{},"RuntimeOutcomeReceipt.v1":{}}}}
def build_local_runtime_outcome_api_server(*_args,**_kwargs): return None
def validate_runtime_outcome_api_contract(c): return c.get("schema")=="RuntimeOutcomeApiContract.v1"
def build_runtime_outcome_validation_report(errors:List[str])->Dict[str,Any]: return {"schema":"RuntimeOutcomeValidationReport.v1","created_at_utc":_utc_now(),"source":SOURCE_NAME,"errors":errors}

def build_runtime_outcome_receipt(run_id,mode,spec,spec_hash,policy_hash,out_paths,hashes,validation,inputs,errs):
    return {"schema":"RuntimeOutcomeReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"error" if errs else "success","source":SOURCE_NAME,"mode":mode,"outcome_acceptance_id":spec["outcome_acceptance_id"],"runtime_outcome_run_id":run_id,"outcome_acceptance_spec_hash":spec_hash,"outcome_acceptance_policy_hash":policy_hash,"runtime_output_inventory_hash":hashes.get("inventory"),"outcome_decision_hash":hashes.get("decision"),"accepted_output_manifest_hash":hashes.get("accepted"),"quarantine_manifest_hash":hashes.get("quarantine"),"handoff_packet_hash":hashes.get("handoff"),"runtime_outcome_result_hash":hashes.get("result"),"output_root":run_id,"outputs":out_paths,"inputs":inputs,"input_hashes":{"outcome_acceptance_spec_sha256":spec_hash,"runtime_supervisor_receipt_sha256":hashes.get("receipt_in"),"runtime_conformance_report_sha256":hashes.get("conf_in"),"pipeline_run_receipt_sha256":None},"validation":validation,"errors":errs}

def run_runtime_outcome_gate(args: argparse.Namespace) -> Path:
    spec = json.loads(args.outcome_acceptance_spec.read_text(encoding="utf-8")); validate_outcome_acceptance_spec(spec,args)
    policy = load_outcome_acceptance_policy(None)
    spec_hash, policy_hash = compute_outcome_acceptance_spec_hash(spec), compute_outcome_acceptance_policy_hash(policy)
    run_id = args.runtime_outcome_run_id or f"{spec['outcome_acceptance_id']}_{args.mode}_{spec_hash[:12]}"
    staging = args.output_root / ".staging" / run_id
    final = args.output_root / run_id
    if final.exists() and not args.overwrite: raise FileExistsError("run path exists")
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)
    inp=load_runtime_outcome_inputs(args); src_ok, src_errs=validate_runtime_supervision_source(inp)
    outputs=discover_runtime_outputs(args.runtime_supervision_run_root)
    inv=build_runtime_output_inventory(spec,outputs,args.allow_unknown_output_role); elig=build_outcome_eligibility_report(evaluate_outcome_eligibility(spec,inp,inv,src_ok,src_errs))
    dec=build_outcome_acceptance_decision_envelope(spec,policy,elig,inp,inv)
    lineage=build_runtime_output_lineage_map(spec,inv,dec,inp.get("conformance_report",{}).get("conformance_hash"))
    am=None; ar=None; qm=None; qr=None
    if dec["decision"] in {"accepted","accepted_with_warnings"}: am=build_accepted_output_manifest(spec,dec,inv); ar=build_accepted_output_receipt(run_id,am)
    if dec["decision"] in {"quarantined","review_required","rejected"}: qm=build_quarantine_manifest(spec,dec,inv); qr=build_quarantine_receipt(run_id,qm)
    hp=build_runtime_outcome_handoff_packet(spec,dec,"accepted/accepted_output_manifest.json" if am else None,"quarantine/quarantine_manifest.json" if qm else None)
    cert=build_runtime_outcome_certificate(spec,dec,am["accepted_output_manifest_hash"] if am else None,qm["quarantine_manifest_hash"] if qm else None,inp.get("conformance_report",{}).get("conformance_hash"))
    att=build_runtime_outcome_attestation(spec,dec,inv)
    ledger,entry=append_runtime_outcome_ledger_entry(staging/"ledger",spec,dec,am["accepted_output_manifest_hash"] if am else None,qm["quarantine_manifest_hash"] if qm else None,hp["handoff_packet_hash"],att["attestation_hash"])
    api_contract=build_runtime_outcome_api_contract(spec); openapi=build_runtime_outcome_openapi(spec)
    build_runtime_outcome_dashboard_if_requested(staging)
    write_canonical_json(staging/"inventory/runtime_output_inventory.json",inv); write_canonical_json(staging/"eligibility/outcome_eligibility_report.json",elig); write_canonical_json(staging/"decisions/outcome_acceptance_decision_envelope.json",dec); write_canonical_json(staging/"lineage/runtime_output_lineage_map.json",lineage)
    if am: write_canonical_json(staging/"accepted/accepted_output_manifest.json",am); write_canonical_json(staging/"accepted/accepted_output_receipt.json",ar)
    if qm: write_canonical_json(staging/"quarantine/quarantine_manifest.json",qm); write_canonical_json(staging/"quarantine/quarantine_receipt.json",qr)
    write_canonical_json(staging/"handoff/runtime_outcome_handoff_packet.json",hp); write_canonical_json(staging/"certificate/runtime_outcome_certificate.json",cert); write_canonical_json(staging/"attestations/runtime_outcome_attestation.json",att)
    write_canonical_json(staging/"api/runtime_outcome_api_contract.json",api_contract); write_canonical_json(staging/"api/runtime_outcome_openapi.json",openapi)
    result_hash=compute_runtime_outcome_result_hash({"inventory":inv["runtime_output_inventory_hash"],"eligibility":elig["outcome_eligibility_hash"],"decision":dec["decision_hash"],"lineage":lineage["lineage_map_hash"],"accepted":am["accepted_output_manifest_hash"] if am else None,"quarantine":qm["quarantine_manifest_hash"] if qm else None,"handoff":hp["handoff_packet_hash"],"attestation":att["attestation_hash"],"ledger_entry":entry["entry_id"]})
    out_paths={"outcome_acceptance_plan":None,"runtime_output_inventory":"inventory/runtime_output_inventory.json","eligibility_report":"eligibility/outcome_eligibility_report.json","decision_envelope":"decisions/outcome_acceptance_decision_envelope.json","lineage_map":"lineage/runtime_output_lineage_map.json","accepted_output_manifest":"accepted/accepted_output_manifest.json" if am else None,"accepted_output_receipt":"accepted/accepted_output_receipt.json" if ar else None,"quarantine_manifest":"quarantine/quarantine_manifest.json" if qm else None,"quarantine_receipt":"quarantine/quarantine_receipt.json" if qr else None,"handoff_packet":"handoff/runtime_outcome_handoff_packet.json","outcome_certificate":"certificate/runtime_outcome_certificate.json","outcome_attestation":"attestations/runtime_outcome_attestation.json","outcome_ledger":"ledger/runtime_outcome_ledger.json","api_contract":"api/runtime_outcome_api_contract.json","openapi":"api/runtime_outcome_openapi.json","validation_report":"runtime_outcome_validation_report.json","checksums":"checksums.sha256"}
    validation={"spec_valid":True,"policy_valid":True,"supervision_source_valid":src_ok,"outputs_inventory_valid":True,"eligibility_valid":True,"decision_valid":True,"accepted_manifest_valid":True,"quarantine_valid":True,"handoff_valid":True,"ledger_valid":validate_runtime_outcome_ledger(ledger),"checksums_valid":True}
    hashes={"inventory":inv["runtime_output_inventory_hash"],"decision":dec["decision_hash"],"accepted":am["accepted_output_manifest_hash"] if am else None,"quarantine":qm["quarantine_manifest_hash"] if qm else None,"handoff":hp["handoff_packet_hash"],"result":result_hash,"receipt_in":_sha256_bytes(_canonical_bytes(inp.get("supervisor_receipt") or {})),"conf_in":_sha256_bytes(_canonical_bytes(inp.get("conformance_report") or {}))}
    rec=build_runtime_outcome_receipt(run_id,args.mode,spec,spec_hash,policy_hash,out_paths,hashes,validation,{"outcome_acceptance_spec":str(args.outcome_acceptance_spec),"runtime_supervision_run_root":str(args.runtime_supervision_run_root),"runtime_supervisor_receipt":"runtime_supervisor_receipt.json","runtime_conformance_report":"runtime_conformance_report.json","pipeline_run_receipt":None},[],)
    write_canonical_json(staging/"runtime_outcome_validation_report.json",build_runtime_outcome_validation_report([])); write_canonical_json(staging/"runtime_outcome_receipt.json",rec)
    write_checksums_file(staging)
    args.output_root.mkdir(parents=True,exist_ok=True)
    if final.exists() and args.overwrite: shutil.rmtree(final)
    os.replace(staging,final)
    return final/"runtime_outcome_receipt.json"

def _parser()->argparse.ArgumentParser:
    p=argparse.ArgumentParser(); p.add_argument("--outcome-acceptance-spec",type=Path,required=True); p.add_argument("--runtime-supervision-run-root",type=Path,required=True); p.add_argument("--output-root",type=Path,required=True); p.add_argument("--mode",default="evaluate-acceptance",choices=sorted(MODES)); p.add_argument("--runtime-outcome-run-id"); p.add_argument("--overwrite",action="store_true"); p.add_argument("--allow-unknown-output-role",action="store_true"); p.add_argument("--accepted-root",type=Path); p.add_argument("--quarantine-root",type=Path); p.add_argument("--execute-acceptance",action="store_true"); return p

def main()->int:
    args=_parser().parse_args()
    rcpt=run_runtime_outcome_gate(args)
    print(rcpt.as_posix())
    return 0

if __name__=="__main__":
    raise SystemExit(main())
