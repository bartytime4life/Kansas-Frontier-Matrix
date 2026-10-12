package kfm.promotion_execution

default allow := false

allow if {
  input.policy_context.evaluation == "PASS"
  input.policy_context.profile == "public-safe"
}
