package governance.obligation_execution

test_deny_missing_obligations if {
  out := data.governance.obligation_execution.deny with input as {"obligations": []}
  count(out) > 0
}

test_deny_retention_allow if {
  out := data.governance.obligation_execution.deny with input as {
    "obligations": [{"obligation_id":"x"}],
    "obligation_execution_receipts": [{}],
    "retention_expired": true,
    "publish_enforcement_report": {"publish_decision":"ALLOW","queue_summary":{"unresolved_count":0}},
    "consent_revoked_subject_ids": [],
    "public_artifact_fields": [],
    "run_receipt": {"signed":true,"verified":true}
  }
  count(out) > 0
}

test_allow_happy_path if {
  data.governance.obligation_execution.allow with input as {
    "obligations": [{"obligation_id":"x"}],
    "obligation_execution_receipts": [{}],
    "retention_expired": false,
    "publish_enforcement_report": {"publish_decision":"DENY","queue_summary":{"unresolved_count":0}},
    "consent_revoked_subject_ids": [],
    "public_artifact_fields": [],
    "run_receipt": {"signed":true,"verified":true}
  }
}
