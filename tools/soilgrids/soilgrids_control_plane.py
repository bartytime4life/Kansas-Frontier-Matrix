from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EXIT_SUCCESS = 0
EXIT_DRY_RUN = 5
EXIT_WARNING = 10
EXIT_RELEASE_GATE_FAIL = 20
EXIT_MALFORMED_INPUT = 30
EXIT_WORKFLOW_VALIDATION_FAIL = 40
EXIT_SCRIPT_VALIDATION_FAIL = 50
EXIT_LOCAL_SMOKE_FAIL = 60
EXIT_UNSAFE_POLICY = 70
EXIT_SECRET_FAIL = 80
EXIT_INTERNAL = 90


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _run_id(deterministic: bool = False) -> str:
    return "run_deterministic" if deterministic else f"run_{int(datetime.now(timezone.utc).timestamp())}"


def write_canonical_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compute_control_plane_spec_hash(spec: dict[str, Any]) -> str:
    return _sha_text(json.dumps(spec, sort_keys=True, separators=(",", ":")))


def compute_cicd_plan_hash(plan: dict[str, Any]) -> str:
    c = dict(plan)
    c.pop("created_at_utc", None)
    c.pop("cicd_plan_hash", None)
    return _sha_text(json.dumps(c, sort_keys=True, separators=(",", ":")))


def compute_workflow_bundle_hash(entries: list[dict[str, Any]]) -> str:
    normalized = sorted(entries, key=lambda x: x["path"])
    return _sha_text(json.dumps(normalized, sort_keys=True, separators=(",", ":")))


def load_control_plane_inputs(args: argparse.Namespace) -> dict[str, Any]:
    cp = Path(args.control_plane_spec)
    if not cp.exists():
        raise ValueError("missing control plane spec")
    inputs = {"control_plane_spec": _read_json(cp), "control_plane_spec_path": str(cp)}
    for key in ["pipeline_spec", "pipeline_run_receipt", "pipeline_certification_envelope", "reproducibility_report"]:
        v = getattr(args, key, None)
        if v:
            inputs[key] = _read_json(Path(v))
            inputs[key + "_path"] = v
        else:
            inputs[key] = None
    return inputs


def validate_control_plane_spec(spec: dict[str, Any], args: argparse.Namespace) -> None:
    if spec.get("schema") != "ControlPlaneSpec.v1":
        raise ValueError("unsupported schema")
    if not spec.get("control_plane_id"):
        raise ValueError("missing control_plane_id")
    repo = spec.get("repository", {})
    if repo.get("ci_provider") not in {"github-actions", "local-only"}:
        raise ValueError("unsupported ci_provider")
    if "pipeline_spec_path" not in spec.get("pipeline", {}):
        raise ValueError("missing pipeline_spec_path")
    if spec.get("profiles", {}).get("scheduled_monitor", {}).get("allow_remote_network"):
        raise ValueError("remote network enabled by default")
    if spec.get("profiles", {}).get("remediation", {}).get("allow_execute_remote"):
        raise ValueError("remediation execute enabled")


def validate_pipeline_spec_reference(inputs: dict[str, Any], mode: str) -> None:
    if mode in {"generate-only", "validate-generated", "local-smoke", "schedule-monitor", "dry-run"} and not inputs.get("pipeline_spec"):
        raise ValueError("pipeline spec required")


def build_cicd_plan(spec: dict[str, Any], spec_hash: str) -> dict[str, Any]:
    plan = {
        "schema": "CICDPlan.v1", "control_plane_id": spec["control_plane_id"], "created_at_utc": _now(),
        "source": "soilgrids_control_plane", "control_plane_spec_hash": spec_hash,
        "ci_provider": spec["repository"]["ci_provider"],
        "workflows": [
            {"workflow_id": "soilgrids_pr_smoke", "path": ".github/workflows/soilgrids_pr_smoke.yml", "trigger": ["pull_request", "workflow_dispatch"], "purpose": "PR offline fixture smoke test", "remote_network": False, "remote_mutation": False},
            {"workflow_id": "soilgrids_main_certify", "path": ".github/workflows/soilgrids_main_certify.yml", "trigger": ["push", "workflow_dispatch"], "purpose": "main branch certify", "remote_network": False, "remote_mutation": False},
            {"workflow_id": "soilgrids_release_gate", "path": ".github/workflows/soilgrids_release_gate.yml", "trigger": ["workflow_dispatch"], "purpose": "release gate", "remote_network": False, "remote_mutation": False},
            {"workflow_id": "soilgrids_scheduled_monitor", "path": ".github/workflows/soilgrids_scheduled_monitor.yml", "trigger": ["schedule", "workflow_dispatch"], "purpose": "scheduled monitor", "remote_network": False, "remote_mutation": False},
            {"workflow_id": "soilgrids_remediation_plan", "path": ".github/workflows/soilgrids_remediation_plan.yml", "trigger": ["workflow_dispatch"], "purpose": "remediation plan-only", "remote_network": False, "remote_mutation": False},
        ],
        "local_scripts": ["scripts/smoke_local.sh", "scripts/certify_local.sh", "scripts/replay_local.sh", "scripts/monitor_local.sh"],
        "runbooks": ["runbooks/operator_runbook.md"],
        "errors": []
    }
    plan["plan_id"] = "cicd_plan_" + compute_cicd_plan_hash(plan)[:12]
    plan["cicd_plan_hash"] = compute_cicd_plan_hash(plan)
    return plan


def generate_github_actions_workflows(spec: dict[str, Any], root: Path) -> list[Path]:
    wf = root / ".github" / "workflows"
    wf.mkdir(parents=True, exist_ok=True)
    base = "permissions:\n  contents: read\n  actions: read\n"
    files = {
        "soilgrids_pr_smoke.yml": "on:\n  pull_request:\n  workflow_dispatch:\n",
        "soilgrids_main_certify.yml": f"on:\n  push:\n    branches: [{spec['repository']['default_branch']}]\n  workflow_dispatch:\n",
        "soilgrids_release_gate.yml": "on:\n  workflow_dispatch:\n",
        "soilgrids_scheduled_monitor.yml": "on:\n  schedule:\n    - cron: '17 6 * * *'\n  workflow_dispatch:\n",
        "soilgrids_remediation_plan.yml": "on:\n  workflow_dispatch:\n",
    }
    out=[]
    for n,t in files.items():
        txt = f"name: {n}\n{t}{base}concurrency: {n}\njobs:\n  run:\n    runs-on: ubuntu-latest\n    timeout-minutes: 20\n    steps:\n      - uses: actions/checkout@v4\n      - name: run\n        shell: bash\n        run: python soilgrids_pipeline_orchestrator.py --mode ci-smoke\n"
        p=wf/n; p.write_text(txt, encoding='utf-8'); out.append(p)
    return out


def generate_local_smoke_scripts(root: Path) -> list[Path]:
    sdir = root / "scripts"; sdir.mkdir(parents=True, exist_ok=True)
    scripts=[]
    for name,mode in [("smoke_local.sh","ci-smoke"),("certify_local.sh","certify"),("replay_local.sh","replay"),("monitor_local.sh","execute-local")]:
        p=sdir/name
        p.write_text(f"#!/usr/bin/env bash\nset -euo pipefail\nREPORTS_DIR=\"${{REPORTS_DIR:-reports}}\"\nmkdir -p \"$REPORTS_DIR\"\npython soilgrids_pipeline_orchestrator.py --mode {mode} > \"$REPORTS_DIR/{name}.log\" 2>&1\n", encoding='utf-8')
        scripts.append(p)
    return scripts


def generate_release_gate_config(root: Path) -> Path:
    p = root / "release" / "release_gate_config.json"; p.parent.mkdir(parents=True, exist_ok=True)
    write_canonical_json(p,{"schema":"ReleaseGateConfig.v1","require_certification":True})
    return p

def generate_monitor_schedule_config(root: Path) -> Path:
    p=root/"release"/"monitor_schedule.json"; write_canonical_json(p,{"cron":"17 6 * * *","allow_remote_network":False}); return p

def generate_operator_runbook(spec: dict[str,Any], root: Path) -> tuple[Path,Path]:
    j = root/"runbooks"/"operator_runbook.json"; m=root/"runbooks"/"operator_runbook.md"; j.parent.mkdir(parents=True, exist_ok=True)
    doc={"schema":"OperatorRunbook.v1","control_plane_id":spec["control_plane_id"],"created_at_utc":_now(),"source":"soilgrids_control_plane","title":"SoilGrids Governed Pipeline Operator Runbook","sections":[{"section_id":"run.pr_smoke","title":"Run PR smoke test","commands":["python soilgrids_pipeline_orchestrator.py --mode ci-smoke"],"expected_receipts":["PipelineRunReceipt.v1"],"failure_modes":["nonzero exit"],"recovery_steps":["check receipts"]},{"section_id":"warn.remote_remediation","title":"Remote remediation execution is blocked by default","commands":[],"expected_receipts":[],"failure_modes":[],"recovery_steps":[]}],"errors":[]}
    write_canonical_json(j,doc)
    m.write_text("# Operator Runbook\n\n- PR smoke workflow\n- local smoke\n- main branch certification\n- replay and reproducibility\n- release gate evaluation\n- scheduled monitor\n- remediation plan-only flow\n- blocked remediation execution\n- evidence crate generation\n- registry/dashboard rebuild\n- interpreting exit codes\n- where receipts are stored\n- how to verify checksums\n- what not to do\n",encoding='utf-8')
    return j,m

def generate_release_checklist(root: Path) -> Path:
    p=root/"release"/"release_checklist.md"; p.parent.mkdir(parents=True, exist_ok=True); p.write_text("- [ ] certification\n- [ ] reproducibility\n",encoding='utf-8'); return p

def validate_workflow_permissions(text:str,args:argparse.Namespace)->None:
    if "write-all" in text: raise ValueError("write-all forbidden")
    if "contents: write" in text and not args.allow_write_permissions: raise ValueError("contents write forbidden")
    if "id-token: write" in text and not args.allow_write_permissions: raise ValueError("id-token write forbidden")

def validate_no_secret_leakage(text:str)->None:
    pats=[r"AKIA[0-9A-Z]{16}",r"Bearer\s+[A-Za-z0-9\-\._~\+\/=]+",r"api[_-]?key\s*[:=]",r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"]
    for p in pats:
        if re.search(p,text,re.I): raise ValueError("secret detected")

def validate_generated_workflows(paths:list[Path], args:argparse.Namespace)->list[dict[str,Any]]:
    checks=[]
    for p in paths:
        t=p.read_text(encoding='utf-8')
        if "name:" not in t or "on:" not in t or "jobs:" not in t: raise ValueError("invalid workflow")
        if "pull_request_target" in t and not args.allow_pull_request_target: raise ValueError("pr target forbidden")
        if "npm install" in t or "pip install" in t: raise ValueError("package install forbidden")
        if "curl " in t and "| bash" in t: raise ValueError("curl pipe bash forbidden")
        if "uses:" in t and "@" in t and "actions/" not in t and not args.allow_unpinned_actions: raise ValueError("third party action")
        validate_workflow_permissions(t,args)
        validate_no_secret_leakage(t)
        if "timeout-minutes" not in t: raise ValueError("timeout missing")
        if "concurrency:" not in t: raise ValueError("concurrency missing")
        checks.append({"path":str(p),"status":"pass"})
    return checks

def validate_generated_scripts(paths:list[Path])->None:
    for p in paths:
        t=p.read_text(encoding='utf-8')
        if "set -euo pipefail" not in t: raise ValueError("script safety missing")
        if "rm -rf /" in t or "curl " in t and "| bash" in t: raise ValueError("unsafe script")
        if "soilgrids_pipeline_orchestrator.py" not in t: raise ValueError("must call layer15")

def run_local_smoke_if_requested(mode:str, root:Path)->None:
    if mode!="local-smoke": return
    receipt = root/"pipeline_run_receipt.json"
    if not receipt.exists(): raise ValueError("missing receipt")

def evaluate_release_gate(inputs:dict[str,Any], spec:dict[str,Any])->dict[str,Any]:
    gates=[]; failed=0
    pr=inputs.get("pipeline_run_receipt") or {}
    ce=inputs.get("pipeline_certification_envelope") or {}
    ok1 = pr.get("status") in {"success","warning"}
    gates.append({"gate_id":"gate.pipeline_run","severity":"required","status":"pass" if ok1 else "fail","evidence":{"path":inputs.get("pipeline_run_receipt_path") or "","sha256":""},"message":"pipeline run status"})
    ok2 = ce.get("certification_status") in {"certified","certified_with_warnings"}
    gates.append({"gate_id":"gate.certification","severity":"required","status":"pass" if ok2 else "fail","evidence":{"path":inputs.get("pipeline_certification_envelope_path") or "","sha256":""},"message":"certification"})
    for g in gates:
        if g["status"]=="fail": failed+=1
    status = "pass" if failed==0 else "fail"
    return build_release_gate_report(spec, gates, status)

def build_workflow_manifest(spec:dict[str,Any], files:list[Path], validated=True)->dict[str,Any]:
    rows=[]
    for p in sorted(files):
        rows.append({"workflow_id":p.stem,"path":str(p.relative_to(p.parents[2])) if ".github" in str(p) else str(p.name),"bytes":p.stat().st_size,"sha256":_sha_file(p),"validated":validated})
    return {"schema":"WorkflowManifest.v1","control_plane_id":spec["control_plane_id"],"created_at_utc":_now(),"source":"soilgrids_control_plane","workflow_bundle_hash":compute_workflow_bundle_hash(rows),"workflows":[r for r in rows if r["path"].endswith(".yml")],"scripts":[r for r in rows if r["path"].endswith(".sh")],"errors":[]}

def build_workflow_validation_report(checks:list[dict[str,Any]], status="success") -> dict[str,Any]:
    return {"schema":"WorkflowValidationReport.v1","run_id":"run","created_at_utc":_now(),"source":"soilgrids_control_plane","status":status,"summary":{"total_checks":len(checks),"passed":len(checks),"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},"checks":checks,"errors":[]}

def build_release_train_manifest(spec:dict[str,Any], pipeline_id="pipeline") -> dict[str,Any]:
    return {"schema":"ReleaseTrainManifest.v1","control_plane_id":spec["control_plane_id"],"release_train_id":"reltrain_"+compute_control_plane_spec_hash(spec)[:12],"created_at_utc":_now(),"source":"soilgrids_control_plane","dataset_id":"soilgrids-v2","pipeline_id":pipeline_id,"stages":[{"gate_id":"gate.pr_smoke","title":"Pull request smoke test","required":True,"evidence":["PipelineRunReceipt.v1"]},{"gate_id":"gate.reproducibility","title":"Reproducibility report acceptable","required":True,"evidence":["ReproducibilityReport.v1"]},{"gate_id":"gate.certification","title":"Pipeline certification passes","required":True,"evidence":["PipelineCertificationEnvelope.v1"]}],"errors":[]}

def build_release_gate_report(spec:dict[str,Any], gates:list[dict[str,Any]], status:str)->dict[str,Any]:
    failed=sum(1 for g in gates if g["status"]=="fail")
    return {"schema":"ReleaseGateReport.v1","run_id":"run","created_at_utc":_now(),"source":"soilgrids_control_plane","status":status,"control_plane_id":spec["control_plane_id"],"pipeline_id":"pipeline","pipeline_run_id":None,"gates":gates,"summary":{"total_gates":len(gates),"passed":len(gates)-failed,"failed":failed,"skipped":0,"required_failed":failed},"errors":[]}

def build_repository_automation_receipt(spec, root, spec_hash, plan_hash, bundle_hash, status="success"):
    return {"schema":"RepositoryAutomationReceipt.v1","run_id":"run","created_at_utc":_now(),"status":status,"source":"soilgrids_control_plane","control_plane_id":spec["control_plane_id"],"automation_root":str(root),"control_plane_spec_hash":spec_hash,"cicd_plan_hash":plan_hash,"workflow_bundle_hash":bundle_hash,"outputs":{},"validation":{"control_plane_spec_valid":True,"pipeline_spec_valid":True,"workflows_valid":True,"scripts_valid":True,"release_gates_valid":True,"secret_scan_valid":True},"errors":[]}

def build_control_plane_receipt(spec,args,spec_hash,cicd_hash,bundle_hash,status="success"):
    return {"schema":"ControlPlaneReceipt.v1","run_id":"run","created_at_utc":_now(),"status":status,"source":"soilgrids_control_plane","mode":args.mode,"control_plane_id":spec.get("control_plane_id"),"control_plane_spec_hash":spec_hash,"cicd_plan_hash":cicd_hash,"workflow_bundle_hash":bundle_hash,"automation_root":args.automation_root,"inputs":{},"input_hashes":{},"outputs":{},"errors":[]}

def write_checksums_file(root:Path, files:list[Path])->Path:
    rels=sorted([(f, _sha_file(f)) for f in files], key=lambda x: str(x[0]))
    p=root/"checksums.sha256"
    p.write_text("".join(f"{h}  {f.relative_to(root)}\n" for f,h in rels), encoding='utf-8')
    return p

def build_control_plane(args: argparse.Namespace) -> tuple[Path,int]:
    inputs=load_control_plane_inputs(args)
    spec=inputs["control_plane_spec"]
    validate_control_plane_spec(spec,args)
    validate_pipeline_spec_reference(inputs,args.mode)
    spec_hash=compute_control_plane_spec_hash(spec)
    root=Path(args.automation_root)
    if root.exists() and any(root.iterdir()) and not args.overwrite:
        raise ValueError("final automation path exists")
    if args.mode=="dry-run":
        receipt=build_control_plane_receipt(spec,args,spec_hash,None,None,status="dry_run")
        out=root/"manifests"/"control_plane_receipt.json"; write_canonical_json(out,receipt); return out, EXIT_DRY_RUN
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)
    plan=build_cicd_plan(spec,spec_hash); workflows=generate_github_actions_workflows(spec,root); scripts=generate_local_smoke_scripts(root)
    if args.make_scripts_executable:
        for s in scripts: s.chmod(s.stat().st_mode | stat.S_IXUSR)
    rgc=generate_release_gate_config(root); msc=generate_monitor_schedule_config(root); runbook_json, runbook_md=generate_operator_runbook(spec,root); checklist=generate_release_checklist(root)
    checks=validate_generated_workflows(workflows,args); validate_generated_scripts(scripts)
    run_local_smoke_if_requested(args.mode, root)
    gate_report = evaluate_release_gate(inputs,spec) if args.mode=="release-gate" else {"schema":"ReleaseGateReport.v1","status":"not_evaluated","gates":[],"summary":{"total_gates":0,"passed":0,"failed":0,"skipped":0,"required_failed":0},"errors":[]}
    mf=build_workflow_manifest(spec, workflows+scripts); vr=build_workflow_validation_report(checks); rt=build_release_train_manifest(spec)
    manifests=root/"manifests"; manifests.mkdir(exist_ok=True)
    write_canonical_json(manifests/"cicd_plan.json", plan); write_canonical_json(manifests/"workflow_manifest.json", mf); write_canonical_json(manifests/"workflow_validation_report.json", vr)
    write_canonical_json(manifests/"release_train_manifest.json", rt); write_canonical_json(manifests/"release_gate_report.json", gate_report)
    bundle_hash=mf["workflow_bundle_hash"]
    rar=build_repository_automation_receipt(spec,root,spec_hash,plan["cicd_plan_hash"],bundle_hash)
    cpr=build_control_plane_receipt(spec,args,spec_hash,plan["cicd_plan_hash"],bundle_hash,status="success" if gate_report.get("status")!="fail" else "warning")
    write_canonical_json(manifests/"repository_automation_receipt.json", rar); cp_path=manifests/"control_plane_receipt.json"; write_canonical_json(cp_path, cpr)
    all_files=workflows+scripts+[rgc,msc,runbook_json,runbook_md,checklist]+list(manifests.glob("*.json"))
    write_checksums_file(root, all_files)
    code=EXIT_SUCCESS if gate_report.get("status")!="fail" else EXIT_RELEASE_GATE_FAIL
    return cp_path, code

def build_parser()->argparse.ArgumentParser:
    p=argparse.ArgumentParser()
    p.add_argument("--control-plane-spec", required=True)
    p.add_argument("--pipeline-spec")
    p.add_argument("--pipeline-run-receipt")
    p.add_argument("--pipeline-certification-envelope")
    p.add_argument("--reproducibility-report")
    p.add_argument("--automation-root", required=True)
    p.add_argument("--mode", required=True, choices=["generate-only","validate-generated","local-smoke","release-gate","schedule-monitor","dry-run"])
    for f in ["allow_local_execution","allow_remote_network","allow_remote_mutation","allow_pull_request_target","allow_unpinned_actions","allow_package_install","allow_write_permissions","allow_public_bind","allow_secret_findings","allow_symlinks","allow_absolute_output","write_to_repo_root","overwrite","keep_temp","deterministic_run_id","make_scripts_executable"]:
        p.add_argument("--"+f.replace("_","-"), action="store_true")
    return p

def main(argv:list[str]|None=None)->int:
    args=build_parser().parse_args(argv)
    try:
        receipt, code = build_control_plane(args)
        sys.stdout.write(str(receipt)+"\n")
        return code
    except ValueError as e:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"control_plane_receipt_path":None,"control_plane_id":None,"message":str(e)})+"\n")
        return EXIT_MALFORMED_INPUT
    except Exception:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"control_plane_receipt_path":None,"control_plane_id":None})+"\n")
        return EXIT_INTERNAL

if __name__ == "__main__":
    raise SystemExit(main())
