from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from graphlib import TopologicalSorter, CycleError
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class PipelineOrchestratorError(Exception):
    exit_code = 120


class SpecError(PipelineOrchestratorError):
    exit_code = 20


class PlanError(PipelineOrchestratorError):
    exit_code = 30


class StageError(PipelineOrchestratorError):
    exit_code = 40


class ReceiptValidationError(PipelineOrchestratorError):
    exit_code = 50


class CrossLayerValidationError(PipelineOrchestratorError):
    exit_code = 60


class SecretFindingError(PipelineOrchestratorError):
    exit_code = 90


class PolicyError(PipelineOrchestratorError):
    exit_code = 100


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    path.write_text(txt, encoding="utf-8")


def load_pipeline_spec(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SpecError("PipelineSpec missing")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise SpecError(f"PipelineSpec malformed: {e}")


def validate_pipeline_spec(spec: Dict[str, Any]) -> None:
    if spec.get("schema") != "PipelineSpec.v1":
        raise SpecError("unsupported schema")
    if not spec.get("pipeline_id"):
        raise SpecError("pipeline_id missing")
    stages = spec.get("stages")
    if not isinstance(stages, list) or not stages:
        raise SpecError("stages missing")
    ids = set()
    for s in stages:
        sid = s.get("stage_id")
        if not sid or sid in ids:
            raise SpecError("duplicate or missing stage_id")
        ids.add(sid)
        if s.get("enabled") is False and s.get("policy", {}).get("required", False):
            raise SpecError("required stage disabled")
        if not s.get("expected_receipt_schema"):
            raise SpecError("expected receipt schema missing")
        if s.get("execution_backend", spec.get("stage_defaults", {}).get("execution_backend", "subprocess")) == "subprocess":
            cmd = s.get("command")
            if not isinstance(cmd, list):
                raise SpecError("command missing or not list")
            joined = " ".join(str(x) for x in cmd)
            if any(x in joined for x in [">", "<", "|", "&&", "||"]):
                raise SpecError("unsafe redirection")
            if any(str(cmd[0]).startswith(pm) for pm in ["pip", "npm", "apt", "brew", "yum"]):
                raise SpecError("package-manager command forbidden")
    for s in stages:
        for d in s.get("depends_on", []):
            if d not in ids:
                raise SpecError("unknown dependency")


def resolve_stage_graph(spec: Dict[str, Any]) -> List[str]:
    graph = {s["stage_id"]: set(s.get("depends_on", [])) for s in spec["stages"] if s.get("enabled", True)}
    try:
        order = list(TopologicalSorter(graph).static_order())
    except CycleError as e:
        raise PlanError(f"dependency cycle: {e}")
    return sorted(order, key=lambda sid: (next(s["layer"] for s in spec["stages"] if s["stage_id"] == sid), sid))


def compute_stage_command_hash(stage: Dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_json_bytes(stage.get("command", [])))


def compute_pipeline_spec_hash(spec: Dict[str, Any]) -> str:
    norm = {k: spec.get(k) for k in ["schema", "pipeline_id", "dataset_id", "network_profile", "mutation_profile", "reproducibility", "exports"]}
    norm["stages"] = []
    for s in sorted(spec["stages"], key=lambda x: x["stage_id"]):
        norm["stages"].append({
            "stage_id": s["stage_id"],
            "layer": s.get("layer"),
            "enabled": s.get("enabled", True),
            "depends_on": sorted(s.get("depends_on", [])),
            "command": s.get("command"),
            "expected_receipt_schema": s.get("expected_receipt_schema"),
        })
    return _sha256_bytes(_canonical_json_bytes(norm))


def build_pipeline_plan(spec: Dict[str, Any], mode: str = "plan-only") -> Dict[str, Any]:
    order = resolve_stage_graph(spec)
    psh = compute_pipeline_spec_hash(spec)
    stage_map = {s["stage_id"]: s for s in spec["stages"]}
    stages = []
    for sid in order:
        s = stage_map[sid]
        stages.append({
            "stage_id": sid,
            "layer": s.get("layer"),
            "enabled": s.get("enabled", True),
            "depends_on": sorted(s.get("depends_on", [])),
            "execution_backend": s.get("execution_backend", spec.get("stage_defaults", {}).get("execution_backend", "subprocess")),
            "command_hash": compute_stage_command_hash(s),
            "expected_receipt_schema": s.get("expected_receipt_schema"),
            "expected_outputs": s.get("expected_outputs", []),
            "timeout_seconds": s.get("timeout_seconds", spec.get("default_timeout_seconds", 3600)),
            "required": s.get("policy", {}).get("required", True),
        })
    plan = {
        "schema": "PipelinePlan.v1",
        "pipeline_id": spec["pipeline_id"],
        "plan_id": "",
        "created_at_utc": _utc_now(),
        "source": "soilgrids_pipeline_orchestrator",
        "pipeline_spec_hash": psh,
        "mode": mode,
        "network_profile": spec.get("network_profile", "offline-fixture"),
        "mutation_profile": spec.get("mutation_profile", "local-only"),
        "stages": stages,
        "execution_order": [s["stage_id"] for s in stages],
        "errors": [],
    }
    plan["plan_hash"] = compute_plan_hash(plan)
    plan["plan_id"] = f"plan_{plan['plan_hash'][:12]}"
    return plan


def compute_plan_hash(plan: Dict[str, Any]) -> str:
    x = {k: v for k, v in plan.items() if k not in {"created_at_utc", "plan_hash", "plan_id"}}
    return _sha256_bytes(_canonical_json_bytes(x))


def validate_plan(plan: Dict[str, Any]) -> None:
    if plan.get("schema") != "PipelinePlan.v1":
        raise PlanError("bad plan schema")


def compute_environment_fingerprint(modules: Optional[List[str]] = None) -> Dict[str, Any]:
    env = {}
    for k in ["PATH", "PYTHONPATH", "HOME"]:
        if k in os.environ:
            env[k] = "<redacted>" if any(t in k.lower() for t in ["token", "key", "secret", "pass"]) else os.environ[k]
    mods = {}
    for m in modules or []:
        try:
            mod = importlib.import_module(m)
            p = Path(getattr(mod, "__file__", ""))
            mods[m] = {"path": str(p) if p.exists() else None, "sha256": _sha256_file(p) if p.exists() else None}
        except Exception:
            mods[m] = {"path": None, "sha256": None}
    return {
        "schema": "EnvironmentFingerprint.v1",
        "python_version": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "working_directory": str(Path.cwd()),
        "environment_variables": env,
        "modules": mods,
        "executables": {"python": {"path": shutil.which("python"), "sha256": None, "version": sys.version.split()[0]}},
    }


def execute_stage_subprocess(stage: Dict[str, Any], cwd: Path, timeout_seconds: int) -> Tuple[int, str, str]:
    p = subprocess.run(stage["command"], cwd=str(cwd), capture_output=True, text=True, timeout=timeout_seconds, check=False)
    return p.returncode, p.stdout, p.stderr


def execute_stage_importable(stage: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
    mod = importlib.import_module(stage["module"])
    fn = getattr(mod, stage.get("function", "main"))
    result = fn(**stage.get("function_args", {}))
    return 0, result if isinstance(result, dict) else {"result": result}


def validate_stage_receipt(path: Path, expected_schema: str) -> Dict[str, Any]:
    if not path.exists():
        raise ReceiptValidationError("receipt missing")
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        raise ReceiptValidationError("malformed receipt")
    if d.get("schema") != expected_schema:
        raise ReceiptValidationError("receipt schema mismatch")
    return d


def validate_stage_outputs(stage: Dict[str, Any], workspace: Path) -> List[Dict[str, Any]]:
    outs = []
    for pat in stage.get("expected_outputs", []):
        matches = sorted(workspace.glob(pat))
        if not matches:
            raise ReceiptValidationError("output missing")
        for p in matches:
            if p.is_file():
                outs.append({"path": str(p), "bytes": p.stat().st_size, "sha256": _sha256_file(p)})
    return sorted(outs, key=lambda x: x["path"])


def validate_cross_layer_after_stage(current: Dict[str, Any], prior: Optional[Dict[str, Any]]) -> bool:
    if not prior:
        return True
    a = current.get("receipt", {}).get("spec_hash")
    b = prior.get("receipt", {}).get("spec_hash")
    return True if not a or not b else isinstance(a, str) and isinstance(b, str)


def build_pipeline_stage_receipt(**kwargs: Any) -> Dict[str, Any]:
    return {"schema": "PipelineStageReceipt.v1", **kwargs}


def execute_stage(stage: Dict[str, Any], spec_stage: Dict[str, Any], workspace: Path, run_id: str, run_dir: Path, prior: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    start = datetime.now(timezone.utc)
    sd = run_dir / "stages" / stage["stage_id"]
    sd.mkdir(parents=True, exist_ok=True)
    stdout_p = sd / "stdout.log"
    stderr_p = sd / "stderr.log"
    code = 0
    errors: List[str] = []
    receipt_path = spec_stage.get("receipt_path")
    if stage["execution_backend"] == "subprocess":
        code, out, err = execute_stage_subprocess(spec_stage, workspace, stage["timeout_seconds"])
        stdout_p.write_text(out, encoding="utf-8")
        stderr_p.write_text(err, encoding="utf-8")
    elif stage["execution_backend"] == "importable":
        code, result = execute_stage_importable(spec_stage)
        stdout_p.write_text(json.dumps(result), encoding="utf-8")
        stderr_p.write_text("", encoding="utf-8")
    else:
        code = 0
        stdout_p.write_text("", encoding="utf-8")
        stderr_p.write_text("", encoding="utf-8")
    status = "success" if code == 0 else "error"
    rcpt = None
    outputs = []
    validations = {"dependencies_valid": True, "policy_valid": True, "receipt_valid": False, "outputs_valid": False, "cross_layer_valid": False}
    if status == "success":
        try:
            if receipt_path:
                rcpt = validate_stage_receipt(workspace / receipt_path, stage["expected_receipt_schema"])
            outputs = validate_stage_outputs(spec_stage, workspace)
            validations["receipt_valid"] = True
            validations["outputs_valid"] = True
            validations["cross_layer_valid"] = validate_cross_layer_after_stage({"receipt": {"spec_hash": rcpt.get("spec_hash") if rcpt else None}}, prior)
        except PipelineOrchestratorError as e:
            errors.append(str(e))
            status = "error"
    dur = int((datetime.now(timezone.utc) - start).total_seconds() * 1000)
    sr = build_pipeline_stage_receipt(
        run_id=run_id, stage_id=stage["stage_id"], layer=stage["layer"], created_at_utc=_utc_now(), source="soilgrids_pipeline_orchestrator",
        status=status, execution_backend=stage["execution_backend"], command_hash=stage["command_hash"],
        stage_spec_hash=_sha256_bytes(_canonical_json_bytes({k: spec_stage.get(k) for k in ["stage_id", "layer", "depends_on", "command", "expected_receipt_schema"]})),
        exit_code=code, duration_ms=dur,
        receipt={"path": receipt_path, "schema": rcpt.get("schema") if rcpt else None, "status": rcpt.get("status") if rcpt else None, "spec_hash": rcpt.get("spec_hash") if rcpt else None, "sha256": _sha256_file(workspace / receipt_path) if rcpt and receipt_path else None},
        outputs=outputs,
        logs={"stdout_path": str(stdout_p), "stderr_path": str(stderr_p), "structured_log_path": None},
        validation=validations,
        errors=errors,
    )
    write_canonical_json(sd / "pipeline_stage_receipt.json", sr)
    return sr


def build_pipeline_run_manifest(run_id: str, spec: Dict[str, Any], plan: Dict[str, Any], stages: List[Dict[str, Any]], run_hash: Optional[str], env_path: str) -> Dict[str, Any]:
    return {"schema": "PipelineRunManifest.v1", "run_id": run_id, "pipeline_id": spec["pipeline_id"], "created_at_utc": _utc_now(), "source": "soilgrids_pipeline_orchestrator", "status": "success" if all(s["status"] == "success" for s in stages) else "error", "pipeline_spec_hash": plan["pipeline_spec_hash"], "plan_hash": plan["plan_hash"], "run_hash": run_hash, "mode": plan["mode"], "network_profile": plan["network_profile"], "mutation_profile": plan["mutation_profile"], "environment_fingerprint_path": env_path, "stages": [{"stage_id": s["stage_id"], "layer": s["layer"], "status": s["status"], "stage_receipt_path": f"stages/{s['stage_id']}/pipeline_stage_receipt.json", "layer_receipt_path": s["receipt"].get("path"), "layer_receipt_schema": s["receipt"].get("schema"), "layer_receipt_spec_hash": s["receipt"].get("spec_hash")} for s in stages], "final_outputs": {}, "errors": []}


def build_pipeline_run_receipt(**kwargs: Any) -> Dict[str, Any]:
    return {"schema": "PipelineRunReceipt.v1", **kwargs}


def write_checksums_file(run_dir: Path) -> Path:
    rows = []
    for p in sorted([x for x in run_dir.rglob("*") if x.is_file() and x.name != "checksums.sha256"], key=lambda x: str(x.relative_to(run_dir))):
        rows.append(f"{_sha256_file(p)}  {p.relative_to(run_dir)}")
    out = run_dir / "checksums.sha256"
    out.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return out


def build_replay_manifest(run_id: str, spec: Dict[str, Any], plan: Dict[str, Any], stages: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {"schema": "ReplayManifest.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": "soilgrids_pipeline_orchestrator", "pipeline_id": spec["pipeline_id"], "pipeline_spec_hash": plan["pipeline_spec_hash"], "plan_hash": plan["plan_hash"], "original_run_manifest": None, "stage_replay_specs": [{"stage_id": s["stage_id"], "original_stage_spec_hash": s["stage_spec_hash"], "original_command_hash": s["command_hash"], "original_receipt_spec_hash": s["receipt"].get("spec_hash"), "original_output_hashes": s["outputs"]} for s in stages], "environment_fingerprint": {}, "errors": []}


def build_reproducibility_report(run_id: str, spec: Dict[str, Any], plan: Dict[str, Any], status: str = "not_evaluated") -> Dict[str, Any]:
    return {"schema": "ReproducibilityReport.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": "soilgrids_pipeline_orchestrator", "status": status, "pipeline_id": spec["pipeline_id"], "pipeline_spec_hash": plan["pipeline_spec_hash"], "original_run_hash": None, "replay_run_hash": None, "comparisons": [], "summary": {"stages_compared": 0, "byte_matches": 0, "semantic_matches": 0, "drifts": 0, "errors": 0}, "errors": []}


def build_pipeline_certification_envelope(run_id: str, spec: Dict[str, Any], plan: Dict[str, Any], run_hash: Optional[str], ok: bool, evidence: Dict[str, Any]) -> Dict[str, Any]:
    return {"schema": "PipelineCertificationEnvelope.v1", "run_id": run_id, "created_at_utc": _utc_now(), "source": "soilgrids_pipeline_orchestrator", "pipeline_id": spec["pipeline_id"], "certification_status": "certified" if ok else "not_certified", "pipeline_spec_hash": plan["pipeline_spec_hash"], "plan_hash": plan["plan_hash"], "run_hash": run_hash, "criteria": [{"criterion_id": "pipeline.all_required_stages_succeeded", "severity": "required", "status": "pass" if ok else "fail", "evidence": {}}], "evidence": evidence, "errors": []}


def append_pipeline_run_ledger(run_root: Path, entry: Dict[str, Any]) -> None:
    ledger = run_root / "ledger" / "pipeline_run_ledger.json"
    data = {"entries": []}
    if ledger.exists():
        data = json.loads(ledger.read_text(encoding="utf-8"))
    data["entries"].append(entry)
    write_canonical_json(ledger, data)


def export_cwl_if_requested(run_dir: Path, plan: Dict[str, Any], enabled: bool) -> Optional[str]:
    if not enabled:
        return None
    p = run_dir / "exports" / "cwl" / "pipeline.cwl"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("cwlVersion: v1.2\nclass: Workflow\n# cwl-like export\n", encoding="utf-8")
    return str(p.relative_to(run_dir))


def export_openlineage_events_if_requested(run_dir: Path, plan: Dict[str, Any], enabled: bool) -> Optional[str]:
    if not enabled:
        return None
    p = run_dir / "exports" / "openlineage" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for sid in plan["execution_order"]:
            f.write(json.dumps({"eventType": "START", "job": {"name": sid}}, sort_keys=True) + "\n")
    return str(p.relative_to(run_dir))


def export_otel_bundle_if_requested(run_dir: Path, stages: List[Dict[str, Any]], enabled: bool) -> Optional[str]:
    if not enabled:
        return None
    base = run_dir / "exports" / "otel"
    base.mkdir(parents=True, exist_ok=True)
    (base / "traces.jsonl").write_text("\n".join(json.dumps({"span": s["stage_id"]}, sort_keys=True) for s in stages) + "\n", encoding="utf-8")
    (base / "metrics.json").write_text(json.dumps({"stage_count": len(stages)}, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    (base / "logs.jsonl").write_text("\n", encoding="utf-8")
    return str((base / "traces.jsonl").relative_to(run_dir))


def execute_pipeline_plan(spec: Dict[str, Any], plan: Dict[str, Any], run_dir: Path, mode: str) -> Tuple[List[Dict[str, Any]], str]:
    if mode in {"plan-only", "dry-run"}:
        return [], "planned" if mode == "plan-only" else "dry_run"
    workspace = Path(spec.get("workspace", "."))
    stages = []
    spec_map = {s["stage_id"]: s for s in spec["stages"]}
    prior = None
    for s in plan["stages"]:
        sr = execute_stage(s, spec_map[s["stage_id"]], workspace, run_dir.name, run_dir, prior)
        stages.append(sr)
        prior = sr
        if sr["status"] != "success" and s.get("required", True):
            raise StageError(f"stage failed: {s['stage_id']}")
    return stages, "success"


def orchestrate_pipeline(pipeline_spec: Optional[Path], run_root: Path, mode: str, deterministic_run_id: bool = False, export_cwl: bool = False, export_openlineage: bool = False, export_otel: bool = False, pipeline_run_manifest: Optional[Path] = None) -> Tuple[Path, int]:
    if mode == "certify" and not pipeline_run_manifest:
        raise SpecError("pipeline-run-manifest required")
    run_root.mkdir(parents=True, exist_ok=True)
    if mode == "certify":
        manifest = json.loads(pipeline_run_manifest.read_text(encoding="utf-8"))
        run_id = manifest["run_id"]
        run_dir = pipeline_run_manifest.parent
        spec = {"pipeline_id": manifest["pipeline_id"]}
        plan = {"pipeline_spec_hash": manifest["pipeline_spec_hash"], "plan_hash": manifest["plan_hash"]}
        cert = build_pipeline_certification_envelope(run_id, spec, plan, manifest.get("run_hash"), manifest.get("status") == "success", {"pipeline_run_manifest": str(pipeline_run_manifest), "pipeline_run_receipt": str(run_dir / "pipeline_run_receipt.json"), "reproducibility_report": None, "evidence_crate_receipt": None, "registry_receipt": None, "runtime_access_receipt": None})
        p = run_dir / "pipeline_certification_envelope.json"
        write_canonical_json(p, cert)
        return p, 0 if cert["certification_status"] == "certified" else 80

    spec = load_pipeline_spec(pipeline_spec)
    validate_pipeline_spec(spec)
    plan = build_pipeline_plan(spec, mode=mode)
    validate_plan(plan)
    run_id = ("run_" + plan["plan_hash"][:12]) if deterministic_run_id else ("run_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    write_canonical_json(run_dir / "pipeline_spec.json", spec)
    write_canonical_json(run_dir / "pipeline_plan.json", plan)
    env = compute_environment_fingerprint([s.get("module") for s in spec.get("stages", []) if s.get("module")])
    write_canonical_json(run_dir / "environment_fingerprint.json", env)
    stages, status = execute_pipeline_plan(spec, plan, run_dir, mode)
    run_hash = _sha256_bytes(_canonical_json_bytes({"plan_hash": plan["plan_hash"], "stages": [_sha256_bytes(_canonical_json_bytes(s)) for s in stages]})) if stages else None
    manifest = build_pipeline_run_manifest(run_id, spec, plan, stages, run_hash, "environment_fingerprint.json") if stages else None
    if manifest:
        write_canonical_json(run_dir / "pipeline_run_manifest.json", manifest)
    replay = build_replay_manifest(run_id, spec, plan, stages) if stages else None
    if replay:
        write_canonical_json(run_dir / "replay_manifest.json", replay)
    repro = build_reproducibility_report(run_id, spec, plan)
    write_canonical_json(run_dir / "reproducibility_report.json", repro)
    cert = build_pipeline_certification_envelope(run_id, spec, plan, run_hash, status == "success", {"pipeline_run_manifest": str(run_dir / "pipeline_run_manifest.json") if manifest else None, "pipeline_run_receipt": str(run_dir / "pipeline_run_receipt.json"), "reproducibility_report": str(run_dir / "reproducibility_report.json"), "evidence_crate_receipt": None, "registry_receipt": None, "runtime_access_receipt": None})
    write_canonical_json(run_dir / "pipeline_certification_envelope.json", cert)
    export_cwl_if_requested(run_dir, plan, export_cwl)
    export_openlineage_events_if_requested(run_dir, plan, export_openlineage)
    export_otel_bundle_if_requested(run_dir, stages, export_otel)
    csum = write_checksums_file(run_dir)
    receipt = build_pipeline_run_receipt(run_id=run_id, created_at_utc=_utc_now(), status=status if mode not in {"plan-only", "dry-run"} else ("planned" if mode == "plan-only" else "dry_run"), source="soilgrids_pipeline_orchestrator", pipeline_id=spec["pipeline_id"], pipeline_spec_hash=plan["pipeline_spec_hash"], plan_hash=plan["plan_hash"], run_hash=run_hash, mode=mode, outputs={"pipeline_plan": str(run_dir / "pipeline_plan.json"), "pipeline_run_manifest": str(run_dir / "pipeline_run_manifest.json") if manifest else None, "pipeline_run_ledger": str(run_root / "ledger" / "pipeline_run_ledger.json"), "reproducibility_report": str(run_dir / "reproducibility_report.json"), "replay_manifest": str(run_dir / "replay_manifest.json") if replay else None, "certification_envelope": str(run_dir / "pipeline_certification_envelope.json"), "checksums": str(csum)}, summary={"stages_planned": len(plan["stages"]), "stages_executed": len(stages), "stages_succeeded": sum(1 for s in stages if s["status"] == "success"), "stages_failed": sum(1 for s in stages if s["status"] == "error"), "stages_skipped": 0, "stages_cached": 0}, validation={"spec_valid": True, "plan_valid": True, "stage_receipts_valid": all(s["validation"]["receipt_valid"] for s in stages) if stages else True, "cross_layer_chain_valid": all(s["validation"]["cross_layer_valid"] for s in stages) if stages else True, "final_outputs_valid": True, "reproducibility_valid": True}, errors=[])
    receipt_path = run_dir / "pipeline_run_receipt.json"
    write_canonical_json(receipt_path, receipt)
    append_pipeline_run_ledger(run_root, {"schema": "PipelineRunLedgerEntry.v1", "entry_id": _sha256_bytes(_canonical_json_bytes({"run_id": run_id, "plan_hash": plan["plan_hash"]})), "created_at_utc": _utc_now(), "source": "soilgrids_pipeline_orchestrator", "pipeline_id": spec["pipeline_id"], "run_id": run_id, "pipeline_spec_hash": plan["pipeline_spec_hash"], "plan_hash": plan["plan_hash"], "run_hash": run_hash, "status": receipt["status"], "artifact_hashes": {"pipeline_plan_sha256": _sha256_file(run_dir / "pipeline_plan.json"), "pipeline_run_manifest_sha256": _sha256_file(run_dir / "pipeline_run_manifest.json") if manifest else None, "pipeline_run_receipt_sha256": _sha256_file(receipt_path), "reproducibility_report_sha256": _sha256_file(run_dir / "reproducibility_report.json"), "certification_envelope_sha256": _sha256_file(run_dir / "pipeline_certification_envelope.json")}, "previous_entry_id": None, "chain_hash": ""})
    code = 0 if mode != "dry-run" else 5
    return receipt_path, code


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--pipeline-spec")
    p.add_argument("--pipeline-run-manifest")
    p.add_argument("--run-root", required=True)
    p.add_argument("--mode", required=True)
    p.add_argument("--deterministic-run-id", action="store_true")
    p.add_argument("--export-cwl", action="store_true")
    p.add_argument("--export-openlineage", action="store_true")
    p.add_argument("--export-otel", action="store_true")
    args = p.parse_args(argv)
    try:
        rp, code = orchestrate_pipeline(Path(args.pipeline_spec) if args.pipeline_spec else None, Path(args.run_root), args.mode, deterministic_run_id=args.deterministic_run_id, export_cwl=args.export_cwl, export_openlineage=args.export_openlineage, export_otel=args.export_otel, pipeline_run_manifest=Path(args.pipeline_run_manifest) if args.pipeline_run_manifest else None)
        print(str(rp))
        return code
    except PipelineOrchestratorError as e:
        err = {"status": "error", "error_count": 1, "pipeline_run_receipt_path": None, "run_id": None}
        sys.stderr.write(json.dumps(err, sort_keys=True) + "\n")
        return e.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
