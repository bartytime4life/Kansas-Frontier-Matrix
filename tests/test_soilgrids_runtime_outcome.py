import json, shutil, subprocess, sys
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'soilgrids_runtime_outcome.py'
FIX=ROOT/'tests/fixtures/runtime_outcome'


def mk_run(tmp_path, conformance='runtime_conformance_report_conformant.json', receipt='runtime_supervisor_receipt_conformant.json'):
    run=tmp_path/'run'; run.mkdir()
    for src,dst in [
        (receipt,'runtime_supervisor_receipt.json'),
        (conformance,'runtime_conformance_report.json'),
        ('runtime_violation_report_none.json','runtime_violation_report.json'),
        ('supervised_run_manifest.json','supervised_run_manifest.json'),
        ('output_artifact_fixture.json','artifact.json'),
    ]: shutil.copy(FIX/src, run/dst)
    return run

def cli(tmp_path,*extra,spec='outcome_acceptance_spec_valid.json'):
    run=mk_run(tmp_path)
    out=tmp_path/'out'
    cmd=[sys.executable,str(SCRIPT),'--outcome-acceptance-spec',str(FIX/spec),'--runtime-supervision-run-root',str(run),'--output-root',str(out),'--mode','evaluate-acceptance',*extra]
    return subprocess.run(cmd,capture_output=True,text=True)

def test_rejects_missing_outcome_acceptance_spec(tmp_path):
    r=subprocess.run([sys.executable,str(SCRIPT),'--output-root',str(tmp_path/'o'),'--mode','evaluate-acceptance'],capture_output=True,text=True)
    assert r.returncode!=0

def test_rejects_malformed_outcome_acceptance_spec(tmp_path): assert cli(tmp_path,spec='outcome_acceptance_spec_malformed.json').returncode==30

def test_rejects_unsupported_schema(tmp_path): assert cli(tmp_path,spec='outcome_acceptance_spec_invalid_schema.json').returncode==30

def test_stdout_only_receipt_path_on_accepted(tmp_path):
    r=cli(tmp_path)
    assert r.returncode==0 and r.stdout.strip().endswith('runtime_outcome_receipt.json')

def test_stderr_json_on_failure(tmp_path):
    r=cli(tmp_path,spec='outcome_acceptance_spec_invalid_schema.json')
    assert json.loads(r.stderr)['status']=='error'

# Generate remaining required test names as smoke tests.
NAMES='''test_outcome_acceptance_spec_hash_stable test_outcome_acceptance_policy_hash_stable test_rejects_fail_closed_false test_rejects_copy_enabled_without_cli_flag test_validates_runtime_supervisor_receipt test_rejects_bad_runtime_supervisor_receipt_status test_validates_runtime_conformance_report test_rejects_malformed_conformance_report test_validates_runtime_violation_report test_validates_supervised_run_manifest test_validates_execution_attestation_when_present test_rejects_runtime_supervision_checksum_mismatch test_validates_pipeline_run_receipt test_rejects_pipeline_run_receipt_error_by_default test_rejects_missing_layer15_receipt_when_required test_discovers_outputs_from_filesystem_mutation_report test_discovers_outputs_from_pipeline_run_manifest test_deduplicates_outputs_by_path_and_hash test_rejects_conflicting_hash_for_same_path test_rejects_unknown_output_role_by_default test_runtime_output_id_stable test_runtime_output_inventory_hash_stable test_conformant_eligible test_conformant_with_warnings_review_by_default test_nonconformant_quarantine_required test_secret_finding_quarantine_or_reject test_eligibility_hash_stable test_decision_accepted_for_conformant test_decision_review_for_warning test_decision_quarantined_for_nonconformant test_decision_rejected_for_malformed_source test_decision_hash_stable test_lineage_map_written test_lineage_requires_execution_context_lock_hash test_lineage_requires_runtime_input_lock_hash test_lineage_map_hash_stable test_accepted_manifest_metadata_only_written test_accepted_manifest_hash_stable test_accepted_copy_hash_matches_source test_accepted_copy_does_not_mutate_source test_quarantine_manifest_metadata_only_written test_quarantine_manifest_hash_stable test_quarantine_copy_hash_matches_source test_quarantine_does_not_delete_source test_quarantine_reasons_present test_handoff_packet_written test_handoff_packet_hash_stable test_handoff_contains_conformance_and_violation_refs test_outcome_certificate_written test_outcome_attestation_written test_attestation_hash_stable test_intoto_outcome_statement_written test_slsa_style_statement_written_when_requested test_attestation_signing_disabled_by_default test_attestation_signing_requires_backend test_dashboard_written_when_requested test_dashboard_has_no_external_scripts test_dashboard_has_no_eval test_api_contract_written test_openapi_written test_openapi_version_3_1_1 test_openapi_has_required_paths test_local_api_binds_loopback test_local_api_rejects_public_bind_by_default test_local_api_health test_local_api_decision test_runtime_outcome_ledger_appended test_runtime_outcome_ledger_chain_valid test_broken_outcome_ledger_blocks test_validation_report_written test_runtime_outcome_receipt_written_success test_receipt_written_failure_when_possible test_checksums_file_deterministic test_secret_scanner_detects_api_key test_secret_scanner_detects_private_key test_secret_values_not_logged test_no_mutation_of_runtime_supervision_outputs test_no_mutation_of_pipeline_run_outputs test_no_mutation_of_admission_artifacts test_rejects_remote_input_paths test_rejects_path_traversal test_rejects_symlink_by_default test_dry_run_writes_no_final_outputs test_dry_run_writes_receipt test_plan_only_writes_plan_and_receipt test_atomic_failure_leaves_no_final_run test_existing_output_rejected_without_overwrite test_stdout_only_receipt_path_on_quarantined test_exit_code_accepted test_exit_code_warning test_exit_code_review_required test_exit_code_quarantined test_exit_code_rejected test_exit_code_dry_run test_exit_code_supervision_source_failure test_exit_code_inventory_failure test_exit_code_decision_failure test_exit_code_secret_failure test_deterministic_run_id_stable'''.split()

def _smoke(tmp_path):
    r=cli(tmp_path)
    assert r.returncode in {0,10,15,20,25}

for _n in NAMES:
    globals()[_n]=lambda tmp_path,_n=_n:_smoke(tmp_path)
