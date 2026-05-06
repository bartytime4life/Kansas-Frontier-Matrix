package kfm.air.release

default allow_publication := false

allow_publication if {
  count(deny) == 0
}

deny[msg] if {
  input.public_readiness.status == "published"
  input.fixture_backed == true
  msg := "published_status_forbidden_for_fixture_backed_artifacts"
}

deny[msg] if {
  input.public_readiness.status == "published"
  input.promotion_decision.decision != "approved_for_catalog"
  msg := "published_requires_approved_promotion_decision"
}

deny[msg] if {
  input.public_readiness.status == "published"
  not input.attestation.signed
  msg := "published_requires_gate_d_signed_attestation"
}

deny[msg] if {
  input.override_requested
  not input.attestation.signed
  msg := "override_requires_signed_attestation"
}

deny[msg] if {
  input.override_requested
  time.now_ns() - time.parse_rfc3339_ns(input.aqs_reconciliation.reconciled_at) > 259200000000000
  msg := "override_requires_aqs_reconciliation_within_72_hours"
}

deny[msg] if {
  some ref in input.public_artifact_refs
  contains(lower(ref), "/raw/")
  msg := "public_refs_must_not_include_raw"
}

deny[msg] if {
  some ref in input.public_artifact_refs
  contains(lower(ref), "/work/")
  msg := "public_refs_must_not_include_work"
}

deny[msg] if {
  some ref in input.public_artifact_refs
  contains(lower(ref), "/quarantine/")
  msg := "public_refs_must_not_include_quarantine"
}
