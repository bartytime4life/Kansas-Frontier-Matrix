package governance.promotion

default allow := false

forbidden_path(p) if {
  lp := lower(p)
  contains(lp,"raw") or contains(lp,"work") or contains(lp,"quarantine")
}

allow if {
  input.policy_label != ""
  input.release_state != ""
  input.decision_log.allow == true
  input.steward_attestation.approved == true
  (input.signing.local_stub_signature == true) or (input.signing.signature != "" and input.signing.certificate != "")
  input.gatehouse_registration.receipt_id != ""
  input.publish_manifest.published_at > input.gatehouse_registration.registered_at
  not forbidden_path(input.artifact.public_path)
  count(input.obligations) > 0
}

deny[msg] if { forbidden_path(input.artifact.public_path); msg := "forbidden public path" }
deny[msg] if { not input.decision_log.allow; msg := "decision deny" }
deny[msg] if { count(input.obligations)==0; msg := "missing obligations" }
