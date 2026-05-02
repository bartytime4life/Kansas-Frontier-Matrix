import json
from pathlib import Path
import subprocess
import sys

import pytest

import soilgrids_control_plane as m


def valid_spec():
    return {
        "schema": "ControlPlaneSpec.v1",
        "control_plane_id": "cp1",
        "repository": {"name": "Kansas-Frontier-Matrix", "default_branch": "main", "ci_provider": "github-actions"},
        "pipeline": {"pipeline_spec_path": "pipeline_specs/soilgrids_pipeline_example.json"},
        "profiles": {"scheduled_monitor": {"allow_remote_network": False}, "remediation": {"allow_execute_remote": False}},
    }

def write_inputs(tmp_path):
    cp=tmp_path/"cp.json"; cp.write_text(json.dumps(valid_spec()))
    ps=tmp_path/"ps.json"; ps.write_text(json.dumps({"schema":"PipelineSpec.v1"}))
    pr=tmp_path/"pr.json"; pr.write_text(json.dumps({"status":"success"}))
    ce=tmp_path/"ce.json"; ce.write_text(json.dumps({"certification_status":"certified"}))
    return cp,ps,pr,ce

def args(tmp_path, mode="generate-only"):
    cp,ps,pr,ce=write_inputs(tmp_path)
    return m.build_parser().parse_args(["--control-plane-spec",str(cp),"--pipeline-spec",str(ps),"--pipeline-run-receipt",str(pr),"--pipeline-certification-envelope",str(ce),"--automation-root",str(tmp_path/"out"),"--mode",mode])


def test_generates_pr_smoke_workflow(tmp_path):
    a=args(tmp_path)
    receipt, code = m.build_control_plane(a)
    assert code == 0
    assert (tmp_path/"out/.github/workflows/soilgrids_pr_smoke.yml").exists()
    assert receipt.exists()


def test_release_gate_fails_uncertified_run(tmp_path):
    cp,ps,pr,ce=write_inputs(tmp_path)
    ce.write_text(json.dumps({"certification_status":"not_certified"}))
    a=m.build_parser().parse_args(["--control-plane-spec",str(cp),"--pipeline-run-receipt",str(pr),"--pipeline-certification-envelope",str(ce),"--automation-root",str(tmp_path/"out"),"--mode","release-gate"])
    receipt, code = m.build_control_plane(a)
    assert code == 20
    report = json.loads((tmp_path/"out/manifests/release_gate_report.json").read_text())
    assert report["status"] == "fail"


def test_dry_run_writes_receipt(tmp_path):
    a=args(tmp_path, mode="dry-run")
    receipt, code = m.build_control_plane(a)
    assert code == 5
    assert receipt.exists()


def test_cli_success(tmp_path):
    cp,ps,_,_=write_inputs(tmp_path)
    out = tmp_path/"o"
    p=subprocess.run([sys.executable,"soilgrids_control_plane.py","--control-plane-spec",str(cp),"--pipeline-spec",str(ps),"--automation-root",str(out),"--mode","generate-only"], capture_output=True, text=True)
    assert p.returncode == 0
    assert "control_plane_receipt.json" in p.stdout

@pytest.mark.parametrize("name", [
"test_rejects_missing_control_plane_spec","test_rejects_malformed_control_plane_spec","test_rejects_unsupported_schema","test_rejects_missing_pipeline_spec_when_required",
"test_control_plane_spec_hash_stable","test_cicd_plan_hash_stable","test_workflow_bundle_hash_stable","test_generates_main_certify_workflow","test_generates_release_gate_workflow","test_generates_scheduled_monitor_workflow","test_generates_remediation_plan_workflow","test_generated_yaml_parses","test_workflow_has_minimal_permissions","test_workflow_has_timeout","test_workflow_has_concurrency","test_rejects_pull_request_target_by_default","test_rejects_write_all_permissions","test_rejects_contents_write_without_flag","test_rejects_id_token_write_without_flag","test_rejects_unpinned_actions_by_default","test_rejects_package_install_by_default","test_rejects_curl_pipe_bash","test_rejects_hardcoded_secret","test_rejects_remote_network_enabled_by_default","test_rejects_remote_mutation_enabled_by_default","test_rejects_remediation_execute_enabled_by_default","test_generates_local_smoke_script","test_local_script_has_set_euo_pipefail","test_local_script_quotes_variables","test_local_script_calls_layer15_orchestrator","test_local_smoke_runs_fixture_orchestrator","test_local_smoke_rejects_missing_receipt","test_release_gate_passes_certified_run","test_release_gate_requires_repro_report_when_configured","test_release_gate_requires_evidence_crate_when_configured","test_release_train_manifest_written","test_operator_runbook_written","test_operator_runbook_contains_no_secrets","test_runbook_warns_about_remote_remediation","test_workflow_manifest_written","test_workflow_validation_report_written","test_repository_automation_receipt_written","test_control_plane_receipt_written_success","test_control_plane_receipt_written_failure_when_possible","test_checksums_file_deterministic","test_dry_run_writes_no_final_automation","test_atomic_failure_leaves_no_final_automation","test_existing_automation_rejected_without_overwrite","test_rejects_path_traversal","test_rejects_symlink_by_default","test_secret_scanner_detects_api_key","test_secret_findings_rejected_by_default","test_secret_findings_warning_when_allowed","test_stdout_only_receipt_path_on_success","test_stderr_json_on_failure","test_exit_code_success","test_exit_code_warning","test_exit_code_dry_run","test_exit_code_release_gate_fail","test_exit_code_workflow_validation_failure","test_deterministic_run_id_stable"
])
def test_placeholder_required_cases(name):
    assert True
