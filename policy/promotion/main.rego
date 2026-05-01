package kfm.promotion

deny contains "PROMOTION_RIGHTS_UNKNOWN" if {
  input.rights_status == "unknown"
}

deny contains "PROMOTION_PUBLIC_FROM_PRIVATE_LIFECYCLE" if {
  input.public_release == true
  input.source_state == "RAW"
}

deny contains "PROMOTION_PUBLIC_FROM_PRIVATE_LIFECYCLE" if {
  input.public_release == true
  input.source_state == "WORK"
}

deny contains "PROMOTION_PUBLIC_FROM_PRIVATE_LIFECYCLE" if {
  input.public_release == true
  input.source_state == "QUARANTINE"
}

deny contains "PROMOTION_PUBLISHED_NEEDS_REVIEWER" if {
  input.target_state == "PUBLISHED"
  not input.reviewer
}

deny contains "PROMOTION_RESTRICTED_PUBLIC_RELEASE_BLOCKED" if {
  input.sensitivity == "restricted"
  input.public_release == true
}

deny contains "PROMOTION_MISSING_EVIDENCEBUNDLE_SPEC_HASH" if {
  not input.evidencebundle_spec_hash
}

deny contains "PROMOTION_MISSING_RUN_RECEIPT" if {
  not input.run_receipt_ref
}

deny contains "PROMOTION_MISSING_RUN_RECEIPT_BUNDLE" if {
  not input.run_receipt_bundle_ref
}

deny contains "PROMOTION_MISSING_COSIGN_VERIFICATION" if {
  input.public_release == true
  input.cosign_receipt_verified != true
}

deny contains "PROMOTION_GATEHOUSE_NOT_REGISTERED" if {
  input.public_release == true
  input.gatehouse_registration_posture != "registered"
}
