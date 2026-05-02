package kfm.air.reentry_publication_boundary_refresh

default deny = []

deny contains "missing_gate_d_refresh_attestation" if { not input.gate_d_refresh_attestation }
deny contains "fixture_signature_cannot_authorize_production" if {
  input.gate_d_refresh_attestation.signature_type == "fixture_signature"
  input.gate_d_refresh_attestation.production_use_allowed == true
}
deny contains "missing_aqs_reconciliation" if { not input.aqs_reconciliation_refresh_checkpoint }
deny contains "pending_or_conflict_aqs_reconciliation" if {
  s := input.aqs_reconciliation_refresh_checkpoint.status
  s == "pending" or s == "conflict_detected" or s == "blocked"
}
deny contains "publication_claim_blocked" if {
  contains(lower(json.marshal(input)), "published")
}
