package kfm.soil.remediation_outcomes

deny[msg] {
  input.remediation_outcome_receipt.decision != "pass"
  input.remediation_outcome_receipt.decision != "degraded"
  input.remediation_outcome_receipt.decision != "governance_only"
  msg := "invalid remediation outcome decision"
}

deny[msg] {
  input.remediation_outcome_receipt.from_state != "REMEDIATION_HANDOFF_READY"
  msg := "invalid from_state"
}

deny[msg] {
  input.remediation_outcome_receipt.to_state != "REMEDIATION_OUTCOME_RECONCILED"
  msg := "invalid to_state"
}

deny[msg] {
  not input.remediation_outcome_receipt.signatures.dsse
  msg := "missing signature"
}
