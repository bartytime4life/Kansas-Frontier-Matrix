package governance.decision_log_gate

default allow := false

allow if {
  input.promotion.decision_log_present
  input.promotion.decision_log_verification_report.ok
}

deny[msg] if {
  not input.promotion.decision_log_present
  msg := "decision log missing"
}

deny[msg] if {
  input.promotion.decision_log_present
  not input.promotion.decision_log_verification_report.ok
  msg := "decision log verification failed"
}
