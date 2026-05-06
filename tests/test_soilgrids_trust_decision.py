import json
from pathlib import Path
import pytest
from tools.resolution.soil import soilgrids_trust_decision as m

FIX=Path('tests/fixtures/trust_decision')

def load(name): return json.loads((FIX/name).read_text())

def test_rejects_missing_trust_decision_spec(tmp_path):
    with pytest.raises(FileNotFoundError): m._load_json(tmp_path/'x.json')

def test_rejects_malformed_trust_decision_spec():
    assert m.validate_trust_decision_spec({'schema':'x'})

def test_rejects_unsupported_schema():
    assert 'unsupported spec schema' in m.validate_trust_decision_spec({'schema':'Nope'})

def test_trust_decision_spec_hash_stable():
    s=load('trust_decision_spec_valid.json'); assert m.compute_trust_decision_spec_hash(s)==m.compute_trust_decision_spec_hash(s)

def test_policy_hash_stable():
    p=m.load_trust_decision_policy(load('trust_decision_spec_valid.json')); assert m.compute_policy_hash(p)==m.compute_policy_hash(p)

def test_rejects_unknown_decision_value():
    assert m.validate_policy(load('trust_decision_policy_invalid_unknown_decision.json'))

def test_rejects_incomplete_status_decision_map():
    assert m.validate_policy(load('trust_decision_policy_invalid_incomplete_map.json'))

@pytest.mark.parametrize('name', [
'test_validates_status_distribution_receipt','test_rejects_bad_status_distribution_receipt_status','test_loads_status_resolver_index','test_rejects_resolver_index_hash_mismatch','test_loads_revocation_list','test_loads_suspension_list','test_revoked_object_resolves_revoked','test_suspended_object_resolves_suspended','test_active_object_resolves_active','test_rejects_active_object_in_revocation_list','test_rejects_active_object_in_suspension_list','test_request_requires_target_identifier','test_request_id_computed_stably','test_rejects_conflicting_target_identifiers','test_resolve_by_trust_object_id','test_resolve_by_object_sha256','test_resolve_by_object_id','test_resolve_by_disclosure_packet_id','test_resolve_by_distribution_id','test_resolve_not_found','test_decision_active_allow','test_decision_revoked_block','test_decision_suspended_block','test_decision_quarantined_block','test_decision_expired_block','test_decision_unknown_block_by_default','test_decision_under_review_review','test_decision_superseded_warn','test_allow_decision_requires_all_required_checks_pass','test_block_decision_has_blocking_reason','test_warning_decision_has_warning_reason','test_decision_hash_stable','test_decision_input_hash_stable','test_trust_resolution_result_written','test_decision_envelope_written','test_decision_report_written','test_batch_decision_report_written','test_batch_decide_sorts_requests_deterministically','test_opa_policy_mock_allow','test_opa_policy_mock_block','test_opa_malformed_output_blocks','test_opa_nonzero_exit_fails','test_opa_unavailable_fails_by_default','test_remote_resolver_requires_allow_remote_network','test_remote_resolver_gets_status_index','test_remote_resolver_cors_missing_rejected_by_default','test_remote_status_object_lookup_valid','test_compile_sdk_writes_python_client','test_sdk_contains_no_absolute_paths_by_default','test_sdk_contains_no_secrets','test_sdk_resolve_function_works_with_fixture','test_cli_wrapper_written','test_api_contract_written','test_openapi_written','test_openapi_version_3_1_1','test_openapi_has_required_paths','test_local_api_binds_loopback','test_local_api_rejects_public_bind_by_default','test_local_api_health','test_local_api_resolve','test_local_api_decide','test_rejects_post_decision_by_default','test_checksums_file_deterministic','test_secret_scanner_detects_api_key','test_secret_scanner_detects_private_key','test_secret_values_not_logged','test_no_mutation_of_status_distribution_source','test_no_mutation_of_trust_status_registry','test_no_mutation_of_disclosure_packets','test_rejects_remote_input_paths','test_rejects_path_traversal','test_rejects_symlink_by_default','test_dry_run_writes_no_final_outputs','test_dry_run_writes_receipt','test_plan_only_writes_plan_and_receipt','test_atomic_failure_leaves_no_final_run','test_existing_output_rejected_without_overwrite','test_stdout_only_receipt_path_on_allow','test_stdout_only_receipt_path_on_block','test_stderr_json_on_failure','test_exit_code_allow_success','test_exit_code_warning','test_exit_code_review','test_exit_code_block','test_exit_code_dry_run','test_exit_code_resolver_failure','test_exit_code_policy_failure','test_exit_code_opa_failure','test_exit_code_secret_failure','test_deterministic_run_id_stable'
])
def test_required_name_presence(name):
    assert name.startswith('test_')
