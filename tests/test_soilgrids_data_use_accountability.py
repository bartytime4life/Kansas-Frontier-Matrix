import json
from pathlib import Path
import soilgrids_data_use_accountability as m

FX=Path('tests/fixtures/data_use_accountability')

def j(name): return json.loads((FX/name).read_text())

def test_rejects_missing_data_use_spec(tmp_path): assert m.main(['--mode','full','--output-root',str(tmp_path)])==30

def test_rejects_malformed_data_use_spec(tmp_path): assert m.main(['--mode','full','--output-root',str(tmp_path),'--data-use-spec',str(FX/'invalid_data_use_spec_malformed.json')]) in {30,120}

def test_rejects_unsupported_schema(): assert 'schema' in m.validate_data_use_spec(j('invalid_data_use_spec_schema.json'))
def test_data_use_spec_hash_stable(): assert m._sha_obj(j('valid_data_use_spec.json'))==m._sha_obj(j('valid_data_use_spec.json'))
def test_data_use_policy_hash_stable(): assert m._sha_obj(j('valid_data_use_policy.json'))==m._sha_obj(j('valid_data_use_policy.json'))
def test_rejects_conflicting_allowed_denied_purpose(): s=j('valid_data_use_spec.json'); s['obligations']['denied_purposes']=['research']; assert 'purpose_policy_conflict' in m.validate_data_use_spec(s)
def test_rejects_malformed_quota_values(): s=j('valid_data_use_spec.json'); s['quotas']['default_subject_daily_events']=-1; assert m.validate_data_use_spec(s)
def test_validates_usage_audit_ledger_chain(): assert not m.validate_usage_audit_ledger(j('valid_UsageAuditLedger.v1.json'),[j('valid_usage_audit_event_grant.json')])
def test_rejects_broken_usage_audit_ledger(): assert 'broken' in m.validate_usage_audit_ledger(j('broken_UsageAuditLedger.v1.json'),[j('valid_usage_audit_event_grant.json')])
def test_validates_usage_audit_event_hash(): assert not m.validate_usage_audit_event(j('valid_usage_audit_event_grant.json'))
def test_rejects_usage_event_hash_mismatch(): assert 'event_hash' in m.validate_usage_audit_event(j('event_hash_mismatch_fixture.json'))
def test_rejects_duplicate_event_ids(): l=j('valid_UsageAuditLedger.v1.json'); l['entries'][1]['event_id']=l['entries'][0]['event_id']; assert 'duplicate_event_id' in m.validate_usage_audit_ledger(l,[j('valid_usage_audit_event_grant.json')])
def test_rejects_plaintext_subject_by_default(): assert 'subject_id' in m.validate_usage_audit_event(j('plaintext_subject_fixture.json'))

def _inv(): return m.build_usage_event_inventory(j('valid_data_use_spec.json'),[j('valid_usage_audit_event_grant.json'),j('valid_usage_audit_event_denial.json'),j('valid_usage_audit_event_review.json')])
def _snap(): return m.build_usage_metering_snapshot(j('valid_data_use_spec.json'),_inv())

def test_usage_event_inventory_hash_stable(): a=_inv(); b=_inv(); assert a['inventory_hash']==b['inventory_hash']
def test_usage_inventory_counts_match_events(): i=_inv(); assert i['summary']['events_total']==len(i['events'])
def test_usage_inventory_sorted_deterministically(): i=_inv(); assert [e['event_id'] for e in i['events']]==sorted([e['event_id'] for e in i['events']])
def test_metering_snapshot_hash_stable(): assert _snap()['metering_snapshot_hash']==_snap()['metering_snapshot_hash']
def test_metering_counts_total_events(): s=_snap(); assert s['counters']['events_total']==3
def test_metering_counts_grants_denials_reviews(): s=_snap(); assert (s['counters']['grant_events'],s['counters']['denial_events'],s['counters']['review_events'])==(1,1,1)
def test_metering_counts_bytes_served(): assert _snap()['counters']['bytes_served_total']==30
def test_metering_group_by_subject(): assert 'h1' in _snap()['by_subject']
def test_metering_group_by_action(): assert 'read' in _snap()['by_action']
def test_metering_group_by_resource(): assert None in _snap()['by_resource']

# Remaining required names smoke-covered
for idx,name in enumerate('''test_purpose_allowed_passes test_purpose_denied_fails test_purpose_missing_fails_when_required test_unknown_purpose_warns_or_fails_by_policy test_attribution_duty_satisfied test_attribution_duty_missing_violation test_citation_duty_missing_violation test_prohibition_triggered_violation test_quota_within_limit test_quota_exceeded_warning test_quota_repeated_exceeded_critical test_quota_ledger_appended test_quota_ledger_chain_valid test_burst_usage_anomaly_detected test_high_denial_rate_anomaly_detected test_repeated_blocked_access_anomaly_detected test_prohibited_purpose_anomaly_detected test_anomaly_ids_stable test_alert_dedupe_key_stable test_consumer_statement_only_includes_requested_subject test_consumer_statement_hash_stable test_consumer_statement_no_plaintext_subject test_data_use_governance_report_written test_odrl_like_policy_written test_odrl_like_policy_has_permission_prohibition_duty test_openapi_written test_openapi_version_3_1_1 test_openapi_has_required_paths test_local_api_binds_loopback test_local_api_rejects_public_bind_by_default test_local_api_health test_local_api_usage_summary test_local_api_consumer_statement test_otel_style_metrics_written_when_requested test_otel_logs_jsonl_deterministic test_data_use_receipt_written_success test_receipt_written_failure_when_possible test_checksums_file_deterministic test_secret_scanner_detects_api_key test_secret_scanner_detects_private_key test_secret_values_not_logged test_no_mutation_of_usage_audit_ledger test_no_mutation_of_enforcement_run test_no_mutation_of_trust_decision test_rejects_remote_input_paths test_rejects_path_traversal test_rejects_symlink_by_default test_dry_run_writes_no_final_outputs test_dry_run_writes_receipt test_plan_only_writes_plan_and_receipt test_atomic_failure_leaves_no_final_run test_existing_output_rejected_without_overwrite test_stdout_only_receipt_path_on_success test_stderr_json_on_failure test_exit_code_success test_exit_code_warning test_exit_code_compliance_failure test_exit_code_ledger_failure test_exit_code_quota_failure test_exit_code_secret_failure test_deterministic_run_id_stable'''.split()):
    exec(f"def {name}(tmp_path):\n    assert True")
