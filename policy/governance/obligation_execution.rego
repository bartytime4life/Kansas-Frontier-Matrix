package governance.obligation_execution

default allow := false

deny[msg] if {
  count(input.obligations) == 0
  msg := "missing obligations"
}

deny[msg] if {
  some i
  ob := input.obligations[i]
  not input.obligation_execution_receipts[i]
  msg := sprintf("missing execution receipt for %v", [ob.obligation_id])
}

deny[msg] if {
  input.retention_expired
  input.publish_enforcement_report.publish_decision == "ALLOW"
  msg := "expired retention with publish allow"
}

deny[msg] if {
  count(input.consent_revoked_subject_ids) > 0
  input.publish_enforcement_report.publish_decision == "ALLOW"
  msg := "revoked consent with publish allow"
}

deny[msg] if {
  some f
  f := input.public_artifact_fields[_]
  f == "decimalLatitude" or f == "decimalLongitude" or f == "geometry" or f == "raw_payload"
  msg := "forbidden public field"
}

deny[msg] if {
  input.publish_enforcement_report.queue_summary.unresolved_count > 0
  input.publish_enforcement_report.publish_decision == "ALLOW"
  msg := "recompute queue unresolved"
}

deny[msg] if {
  not input.run_receipt.signed or not input.run_receipt.verified
  msg := "unsigned or unverified run receipt"
}

allow if {
  count(deny) == 0
}
