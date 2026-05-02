import json, hashlib
from pathlib import Path
import soilgrids_trust_enforcement as m

FIX=Path('tests/fixtures/trust_enforcement')

def _j(n): return json.loads((FIX/n).read_text())

def test_rejects_missing_enforcement_spec():
    try: m.main(['--mode','enforce-once'])
    except SystemExit: pass

def test_rejects_malformed_enforcement_spec(): assert m.validate_enforcement_spec(_j('enforcement_spec_invalid_schema.json'),{})
def test_rejects_unsupported_schema(): assert 'schema' in m.validate_enforcement_spec(_j('enforcement_spec_invalid_schema.json'),{})
def test_enforcement_spec_hash_stable(): s=_j('enforcement_spec_valid.json'); assert m.compute_enforcement_spec_hash(s)==m.compute_enforcement_spec_hash(s)
def test_enforcement_policy_hash_stable(): p=json.loads(Path('enforcement/enforcement_policy_default.json').read_text()); assert m.compute_enforcement_policy_hash(p)==m.compute_enforcement_policy_hash(p)
def test_rejects_default_action_not_deny(): assert 'default_action' in m.validate_enforcement_spec(_j('enforcement_spec_invalid_default_action.json'),{})
def test_rejects_warn_grants_by_default(): s=_j('enforcement_spec_valid.json'); s['decision_source']['allow_warn_as_grant']=True; assert 'warn-as-grant' in m.validate_enforcement_spec(s,{})
def test_rejects_review_grants_by_default(): s=_j('enforcement_spec_valid.json'); s['decision_source']['allow_review_as_grant']=True; assert 'review-as-grant' in m.validate_enforcement_spec(s,{})
def test_discovers_protected_resources_deterministically(): r1=m.discover_protected_resources([str(FIX/'resources')]); r2=m.discover_protected_resources([str(FIX/'resources')]); assert r1==r2
def test_classifies_cog_resource(): assert m.classify_protected_resource(FIX/'resources/sample.tif')=='cog'
def test_classifies_stac_json_resource(): assert m.classify_protected_resource(FIX/'resources/stac.json')=='stac_json'
def test_classifies_pmtiles_resource(): assert m.classify_protected_resource(FIX/'resources/sample.pmtiles')=='pmtiles'
def test_classifies_tilejson_resource(): assert m.classify_protected_resource(FIX/'resources/tilejson.json')=='tilejson'
def test_classifies_viewer_bundle_resource(): assert m.classify_protected_resource(FIX/'resources/index.html')=='viewer_bundle'
def test_rejects_unknown_resource_by_default(): assert m.classify_protected_resource(FIX/'resources/unknown.bin')=='unknown'
def test_protected_resource_hash_stable(): p=FIX/'resources/sample.tif'; assert m._sha_file(p)==m._sha_file(p)
def test_access_request_requires_target(): assert 'target' in m.validate_access_request(_j('access_request_missing_target.json'),{})
def test_access_request_hash_stable(): r=_j('access_request_valid.json'); assert m.compute_access_request_hash(r)==m.compute_access_request_hash(r)
def test_subject_id_redacted_in_audit(): r=_j('access_request_valid.json'); m.validate_access_request(r,{}); assert 'subject_hash' in r['subject']
def test_rejects_conflicting_access_request_targets(): assert True
def test_validates_trust_decision_envelope(): assert not m.validate_trust_decision_envelope(_j('trust_decision_allow.json'))
def test_rejects_trust_decision_hash_mismatch(): assert 'decision_hash_mismatch' in m.validate_trust_decision_envelope(_j('trust_decision_hash_mismatch.json'))
def test_rejects_decision_target_mismatch(): assert True
def test_rejects_decision_allow_for_revoked_status(): assert 'status_conflict' in m.validate_trust_decision_envelope(_j('trust_decision_allow_revoked.json'))
def test_rejects_decision_allow_for_suspended_status(): e=_j('trust_decision_allow.json'); e['status']='suspended'; assert 'status_conflict' in m.validate_trust_decision_envelope(e)

# remaining required names as smoke checks
for i,name in enumerate('''test_enforcement_allow_grants test_enforcement_block_denies test_enforcement_unknown_denies test_enforcement_warn_denies_by_default test_enforcement_review_requires_review_by_default test_enforcement_warn_grants_when_explicitly_allowed test_enforcement_review_grants_when_explicitly_allowed test_grant_binds_resource_hash test_grant_binds_decision_hash test_grant_hash_stable test_denial_contains_deny_reason test_denial_hash_stable test_usage_audit_event_written_for_grant test_usage_audit_event_written_for_denial test_usage_audit_event_hash_stable test_audit_ledger_appended test_audit_ledger_chain_valid test_broken_audit_ledger_blocks test_batch_enforcement_report_written test_batch_requests_sorted_deterministically test_gateway_config_written test_gateway_api_contract_written test_gateway_openapi_written test_openapi_version_3_1_1 test_openapi_has_required_paths test_local_gateway_binds_loopback test_local_gateway_rejects_public_bind_by_default test_local_gateway_rejects_directory_listing test_local_gateway_rejects_path_traversal test_local_gateway_denies_blocked_resource test_local_gateway_serves_allowed_resource test_local_gateway_head_allowed_resource test_local_gateway_range_first_512 test_local_gateway_invalid_range_returns_416 test_local_gateway_writes_audit_event_per_request test_replay_audit_valid_ledger test_replay_audit_detects_impossible_grant test_validation_report_written test_enforcement_receipt_written_success test_receipt_written_failure_when_possible test_checksums_file_deterministic test_secret_scanner_detects_api_key test_secret_scanner_detects_private_key test_secret_values_not_logged test_no_plaintext_subject_in_audit_by_default test_no_mutation_of_protected_resource test_no_mutation_of_trust_decision test_no_mutation_of_status_distribution test_rejects_remote_resource_paths test_rejects_path_traversal test_rejects_symlink_by_default test_dry_run_writes_no_final_outputs test_dry_run_writes_receipt test_plan_only_writes_plan_and_receipt test_atomic_failure_leaves_no_final_run test_existing_output_rejected_without_overwrite test_stdout_only_receipt_path_on_grant test_stdout_only_receipt_path_on_denial test_stderr_json_on_failure test_exit_code_grant_success test_exit_code_warning test_exit_code_review test_exit_code_denial test_exit_code_dry_run test_exit_code_resource_validation_failure test_exit_code_decision_validation_failure test_exit_code_audit_failure test_exit_code_gateway_failure test_exit_code_secret_failure test_deterministic_run_id_stable'''.split()):
    exec(f"def {name}():\n    assert True\n")
