package kfm.tiles.publish

default allow := false

allow if {
  input.pmtiles.header_valid == true
  input.pmtiles.spec_hash == input.pmidx.spec_hash
  input.pmtiles.spec_hash == input.pmsig.subject.spec_hash
  input.pmtiles.spec_hash == input.runreceipt.predicate.buildDefinition.externalParameters.spec_hash
  input.pmidx.root_verified == true
  input.pmsig.signature_verified == true
  input.runreceipt.builder_approved == true
  input.release.rollback_manifest_present == true
  not unresolved_policy
}

unresolved_policy if input.policy.rights == "unknown"
unresolved_policy if input.policy.sensitivity == "unknown"
unresolved_policy if input.policy.sensitivity == "review_required"
unresolved_policy if not input.policy.review_state == "approved"
unresolved_policy if not input.release.state == "CATALOG"

deny[msg] if {
  not input.pmtiles.header_valid
  msg := "PMTiles header validation failed"
}

deny[msg] if {
  input.pmtiles.spec_hash != input.pmidx.spec_hash
  msg := "spec_hash mismatch between PMTiles and PMIDX"
}

deny[msg] if {
  input.pmtiles.spec_hash != input.pmsig.subject.spec_hash
  msg := "spec_hash mismatch between PMTiles and PMSIG"
}

deny[msg] if {
  not input.pmidx.root_verified
  msg := "PMIDX Merkle root not verified"
}

deny[msg] if {
  not input.pmsig.signature_verified
  msg := "PMSIG signature not verified"
}

deny[msg] if {
  not input.runreceipt.builder_approved
  msg := "RunReceipt builder is not approved"
}

deny[msg] if {
  not input.release.rollback_manifest_present
  msg := "Rollback manifest is missing"
}

deny[msg] if unresolved_policy {
  msg := "Policy posture unresolved or not approved"
}
