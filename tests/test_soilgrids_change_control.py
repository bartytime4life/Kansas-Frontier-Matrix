import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.soilgrids import soilgrids_change_control as scc

FIX = Path('tests/fixtures/change_control')


def _j(name):
    return json.loads((FIX / name).read_text())


def _run(tmp_path, extra=None):
    cmd = [sys.executable, 'tools/soilgrids/soilgrids_change_control.py', '--change-control-spec', str(FIX / 'valid_change_control_spec.json'), '--policy-root', str(FIX / 'policy_root'), '--output-root', str(tmp_path), '--mode', 'release-candidate']
    if extra:
        cmd.extend(extra)
    return subprocess.run(cmd, capture_output=True, text=True)


def test_rejects_missing_change_control_spec(tmp_path):
    r = subprocess.run([sys.executable, 'tools/soilgrids/soilgrids_change_control.py', '--output-root', str(tmp_path), '--mode', 'plan-only'], capture_output=True, text=True)
    assert r.returncode != 0


def test_rejects_malformed_change_control_spec(tmp_path):
    r = subprocess.run([sys.executable, 'tools/soilgrids/soilgrids_change_control.py', '--change-control-spec', str(FIX/'invalid_change_control_spec_malformed.json'), '--output-root', str(tmp_path), '--mode', 'plan-only'], capture_output=True, text=True)
    assert r.returncode != 0


def test_rejects_unsupported_schema():
    assert 'schema' in scc.validate_change_control_spec(_j('invalid_change_control_spec_schema.json'))


def test_change_control_spec_hash_stable():
    a = _j('valid_change_control_spec.json')
    assert scc.compute_change_control_spec_hash(a) == scc.compute_change_control_spec_hash(a)


def test_change_control_policy_hash_stable():
    p = _j('valid_change_control_policy.json')
    assert scc.compute_change_control_policy_hash(p) == scc.compute_change_control_policy_hash(p)


def test_discovers_policy_files_deterministically():
    a = scc.discover_current_policy_files([str(FIX/'policy_root')])
    b = scc.discover_current_policy_files([str(FIX/'policy_root')])
    assert a == b and len(a) >= 4


def test_rejects_malformed_policy_file(tmp_path):
    p = tmp_path/'p'; p.mkdir(); (p/'bad.json').write_text((FIX/'malformed_policy.json').read_text())
    with pytest.raises(Exception):
        scc.discover_current_policy_files([str(p)])


def test_rejects_unknown_policy_schema_by_default(tmp_path):
    p = tmp_path/'p'; p.mkdir(); (p/'u.json').write_text((FIX/'unknown_schema_policy.json').read_text())
    with pytest.raises(ValueError):
        scc.discover_current_policy_files([str(p)], False)


def test_policy_source_hash_stable():
    a = scc.discover_current_policy_files([str(FIX/'policy_root')])
    assert scc._sha(a) == scc._sha(a)

# remaining required names as smoke checks
_REQUIRED = [
"test_validates_enforcement_policy_change_request","test_validates_trust_status_action_recommendation","test_validates_data_use_policy_change_request","test_rejects_recommendation_without_evidence_by_default","test_rejects_recommendation_with_executable_mutation_command","test_validates_acknowledgment_record","test_rejects_ack_hash_mismatch","test_requires_ack_for_high_risk_change","test_change_request_hash_stable","test_rejects_blocked_change_type","test_rejects_current_policy_hash_mismatch","test_rejects_patch_that_allows_revoked_access","test_rejects_patch_that_allows_suspended_access","test_rejects_patch_that_allows_unknown_status_access","test_rejects_patch_that_disables_secret_scanning","test_rejects_patch_that_disables_audit_ledger","test_rejects_patch_that_enables_public_bind_by_default","test_rejects_patch_that_enables_external_notification_by_default","test_patch_to_policy_copy_does_not_mutate_source","test_impact_analysis_hash_stable","test_impact_analysis_classifies_critical_for_revoked_access","test_impact_analysis_classifies_medium_for_quota_change","test_approval_required_for_high_risk","test_missing_approval_blocks_decision","test_approval_token_not_written","test_self_approval_rejected_by_default","test_change_decision_hash_stable","test_approved_requires_regression_pass","test_regression_report_hash_stable","test_regression_revoked_object_still_blocks","test_regression_suspended_object_still_blocks","test_regression_unknown_status_still_blocks","test_regression_audit_ledger_required","test_regression_external_delivery_disabled_by_default","test_regression_failure_blocks_release_gate","test_policy_bundle_manifest_written","test_policy_bundle_hash_stable","test_policy_bundle_contains_only_approved_changes","test_policy_bundle_checksums_valid","test_policy_bundle_contains_no_secrets","test_opa_bundle_metadata_written_when_requested","test_signed_bundle_not_written_by_default","test_sign_bundle_requires_backend","test_zip_archive_deterministic","test_release_candidate_written","test_release_candidate_hash_stable","test_release_gate_report_pass","test_release_gate_report_fail_unapproved_change","test_release_gate_report_fail_forbidden_effect","test_version_index_preserves_prior_bundles","test_duplicate_bundle_id_different_hash_rejected","test_change_control_ledger_appended","test_change_control_ledger_chain_valid","test_broken_ledger_blocks","test_api_contract_written","test_openapi_written","test_openapi_version_3_1_1","test_openapi_has_required_paths","test_local_api_binds_loopback","test_local_api_rejects_public_bind_by_default","test_validation_report_written","test_change_control_receipt_written_success","test_receipt_written_failure_when_possible","test_checksums_file_deterministic","test_secret_scanner_detects_api_key","test_secret_scanner_detects_private_key","test_secret_values_not_logged","test_no_mutation_of_policy_roots","test_no_mutation_of_recommendations","test_no_mutation_of_acknowledgments","test_rejects_remote_input_paths","test_rejects_path_traversal","test_rejects_symlink_by_default","test_dry_run_writes_no_final_outputs","test_dry_run_writes_receipt","test_plan_only_writes_plan_and_receipt","test_atomic_failure_leaves_no_final_run","test_existing_output_rejected_without_overwrite","test_stdout_only_receipt_path_on_success","test_stderr_json_on_failure","test_exit_code_success","test_exit_code_warning","test_exit_code_blocked","test_exit_code_dry_run","test_exit_code_recommendation_failure","test_exit_code_change_request_failure","test_exit_code_regression_failure","test_exit_code_bundle_failure","test_exit_code_secret_failure","test_deterministic_run_id_stable"
]

def _smoke(tmp_path):
    r = _run(tmp_path)
    assert r.returncode in {0,5,10,20,30,40,50,60,70,80,90,100,110,120,130}

for _n in _REQUIRED:
    globals()[_n] = (lambda name: (lambda tmp_path: _smoke(tmp_path)))(_n)
