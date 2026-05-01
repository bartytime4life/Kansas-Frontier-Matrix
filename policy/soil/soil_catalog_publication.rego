package soil.catalog_publication

deny contains "decision_not_pass" if {
  input.validation_summary.decision != "pass"
}

deny contains "missing_evidence_bundle_ref" if {
  not input.artifacts.evidence_bundle_ref
  not input.evidence_bundle_ref
}

deny contains "missing_signatures" if {
  not input.signatures
}

deny contains "unknown_rights_status" if {
  input.rights_status == "unknown"
}

deny contains "missing_policy_label" if {
  not input.policy_label
}

deny contains "restricted_sensitivity" if {
  input.sensitivity == "restricted"
}

deny contains "private_sensitivity" if {
  input.sensitivity == "private"
}
