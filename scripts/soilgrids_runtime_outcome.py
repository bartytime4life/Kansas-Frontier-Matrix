#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SOURCE_NAME = "soilgrids_runtime_outcome"
MODES = {"plan-only","inventory-outputs","evaluate-acceptance","accept-local","quarantine-local","handoff-packet","verify-accepted","verify-quarantine","attest-outcome","local-api","dry-run","verified"}
EXIT_CODES={"accepted":0,"planned":0,"verified":0,"dry_run":5,"accepted_with_warnings":10,"review_required":15,"quarantined":20,"rejected":25,"malformed":30,"supervision":40,"pipeline":50,"inventory":60,"decision":70,"manifest":80,"handoff":90,"api":100,"unsafe":110,"secret":120,"ledger":130,"internal":140}

DEFAULT_POLICY={"schema":"OutcomeAcceptancePolicy.v1","fail_closed":True,"allowed_decisions":["accepted","accepted_with_warnings","review_required","quarantined","rejected"],"decision_map":{"conformant":"accepted","conformant_with_warnings":"review_required","nonconformant":"quarantined","error":"rejected"},"required_checks":["supervision.receipt.valid","conformance.report.valid","violations.report.valid","outputs.inventory.valid","lineage.hashes.present","secrets.absent"]}


def _utc()->str: return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def _cb(o:Any)->bytes: return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def _h(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def _fh(p:Path)->str: return _h(p.read_bytes())
def _strip(d:dict,drop:set[str])->dict: return {k:v for k,v in d.items() if k not in drop}
def write_json(p:Path,o:Any)->None: p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n")

def scan_secrets(text:str)->bool:
    pats=[r"AKIA[0-9A-Z]{16}",r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----",r"api[_-]?key\s*[:=]"]
    return any(re.search(x,text,re.I) for x in pats)

def load_json(p:Path)->dict:
    try: return json.loads(p.read_text())
    except Exception as e: raise ValueError(f"malformed JSON: {p}") from e

def validate_spec(spec:dict,args:argparse.Namespace)->None:
    if spec.get("schema")!="OutcomeAcceptanceSpec.v1": raise ValueError("unsupported schema")
    for k in ("outcome_acceptance_id","dataset_id"):
        if not spec.get(k): raise ValueError(f"missing {k}")
    if spec.get("acceptance_profile") not in {None,"strict-local","permissive-local"}: raise ValueError("unsupported acceptance_profile")
    if spec.get("copy_accepted_artifacts") and not args.copy_accepted_artifacts: raise ValueError("copy_accepted_artifacts enabled without CLI flag")
    if spec.get("copy_quarantined_artifacts") and not args.copy_quarantined_artifacts: raise ValueError("copy_quarantined_artifacts enabled without CLI flag")

def validate_policy(policy:dict)->None:
    if policy.get("schema")!="OutcomeAcceptancePolicy.v1": raise ValueError("bad policy schema")
    if policy.get("fail_closed") is not True: raise ValueError("fail_closed must be true")
    for k in ("allowed_decisions","decision_map","required_checks"):
        if k not in policy: raise ValueError("incomplete decision_map")

def validate_supervision(inp:dict,args:argparse.Namespace)->tuple[bool,list[str]]:
    errs=[]
    if inp["receipt"].get("schema")!="RuntimeSupervisorReceipt.v1": errs.append("receipt_invalid")
    if inp["receipt"].get("status")=="error" and not args.allow_supervision_warning: errs.append("receipt_status_error")
    if inp["conformance"].get("schema")!="RuntimeConformanceReport.v1": errs.append("conformance_invalid")
    if inp["violation"].get("schema")!="RuntimeViolationReport.v1": errs.append("violation_invalid")
    if inp["manifest"].get("schema")!="SupervisedRunManifest.v1": errs.append("manifest_invalid")
    if inp.get("attestation") and inp["attestation"].get("schema")!="ExecutionConformanceAttestation.v1": errs.append("attestation_invalid")
    return (not errs,errs)

def discover_outputs(root:Path)->list[dict]:
    outs=[]
    for p in sorted(x for x in root.rglob('*') if x.is_file()):
        rel=p.relative_to(root).as_posix(); sha=_fh(p)
        role="artifact" if rel.endswith('.json') else ("log" if rel.endswith('.log') else "unknown")
        outs.append({"path":rel,"sha256":sha,"output_role":role,"bytes":p.stat().st_size,"runtime_output_id":"rout_"+_h(_cb({"p":rel,"h":sha}))[:16]})
    return outs

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--outcome-acceptance-spec",type=Path,required=True)
    ap.add_argument("--output-root",type=Path,required=True)
    ap.add_argument("--mode",required=True,choices=sorted(MODES))
    ap.add_argument("--runtime-supervision-run-root",type=Path,default=Path('.'))
    ap.add_argument("--outcome-acceptance-policy",type=Path)
    ap.add_argument("--runtime-outcome-run-id")
    ap.add_argument("--allow-supervision-warning",action="store_true")
    ap.add_argument("--allow-pipeline-warning",action="store_true")
    ap.add_argument("--allow-unknown-output-role",action="store_true")
    ap.add_argument("--copy-accepted-artifacts",action="store_true")
    ap.add_argument("--copy-quarantined-artifacts",action="store_true")
    ap.add_argument("--allow-public-bind",action="store_true")
    ap.add_argument("--host",default="127.0.0.1")
    ap.add_argument("--serve-forever",action="store_true")
    ap.add_argument("--deterministic-run-id",action="store_true")
    ap.add_argument("--overwrite",action="store_true")
    args=ap.parse_args()
    receipt_path=None
    run_id=args.runtime_outcome_run_id or "runtime_outcome"
    try:
        spec=load_json(args.outcome_acceptance_spec); validate_spec(spec,args)
        policy=load_json(args.outcome_acceptance_policy) if args.outcome_acceptance_policy else DEFAULT_POLICY; validate_policy(policy)
        root=args.runtime_supervision_run_root
        inp={"receipt":load_json(root/"runtime_supervisor_receipt.json"),"conformance":load_json(root/"runtime_conformance_report.json"),"violation":load_json(root/"runtime_violation_report.json"),"manifest":load_json(root/"supervised_run_manifest.json")}
        if (root/"execution_conformance_attestation.json").exists(): inp["attestation"]=load_json(root/"execution_conformance_attestation.json")
        ok,errs=validate_supervision(inp,args)
        if not ok: raise RuntimeError("supervision failed")
        outs=discover_outputs(root)
        if any(o["output_role"]=="unknown" for o in outs) and not args.allow_unknown_output_role: raise RuntimeError("unknown output role")
        if scan_secrets(json.dumps(outs)): raise PermissionError("secret finding")
        conf=inp["conformance"].get("conformance_status","error")
        decision=policy["decision_map"].get(conf,"rejected")
        if args.mode=="dry-run": rc=EXIT_CODES["dry_run"]
        else: rc=EXIT_CODES.get(decision,EXIT_CODES["decision"])
        outdir=args.output_root/run_id
        if outdir.exists() and not args.overwrite: raise FileExistsError("output exists")
        if outdir.exists(): shutil.rmtree(outdir)
        outdir.mkdir(parents=True)
        inv={"schema":"RuntimeOutputInventory.v1","outputs":outs,"created_at_utc":_utc()}; inv["runtime_output_inventory_hash"]=_h(_cb(_strip(inv,{"created_at_utc","runtime_output_inventory_hash"})))
        dec={"schema":"OutcomeAcceptanceDecisionEnvelope.v1","decision":decision,"created_at_utc":_utc()}; dec["decision_hash"]=_h(_cb(_strip(dec,{"created_at_utc","decision_hash"})))
        write_json(outdir/"inventory/runtime_output_inventory.json",inv); write_json(outdir/"decisions/outcome_acceptance_decision_envelope.json",dec)
        receipt={"schema":"RuntimeOutcomeReceipt.v1","runtime_outcome_run_id":run_id,"status":"success","mode":args.mode,"decision":decision}
        receipt_path=outdir/"runtime_outcome_receipt.json"; write_json(receipt_path,receipt)
        print(receipt_path.as_posix())
        return rc
    except ValueError:
        err={"status":"error","error_count":1,"runtime_outcome_receipt_path":str(receipt_path) if receipt_path else None,"runtime_outcome_run_id":run_id if run_id else None}
        print(json.dumps(err),file=os.sys.stderr); return EXIT_CODES["malformed"]
    except PermissionError:
        err={"status":"error","error_count":1,"runtime_outcome_receipt_path":str(receipt_path) if receipt_path else None,"runtime_outcome_run_id":run_id if run_id else None}
        print(json.dumps(err),file=os.sys.stderr); return EXIT_CODES["secret"]
    except RuntimeError as e:
        code=EXIT_CODES["supervision"] if "supervision" in str(e) else EXIT_CODES["inventory"]
        err={"status":"error","error_count":1,"runtime_outcome_receipt_path":str(receipt_path) if receipt_path else None,"runtime_outcome_run_id":run_id if run_id else None}
        print(json.dumps(err),file=os.sys.stderr); return code
    except Exception:
        err={"status":"error","error_count":1,"runtime_outcome_receipt_path":str(receipt_path) if receipt_path else None,"runtime_outcome_run_id":run_id if run_id else None}
        print(json.dumps(err),file=os.sys.stderr); return EXIT_CODES["internal"]

if __name__=="__main__": raise SystemExit(main())
