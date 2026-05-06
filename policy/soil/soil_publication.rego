package soil.publication

deny contains "decision_not_pass" if {
  input.validation_summary.decision == "quarantine"
}

deny contains "decision_not_pass" if {
  input.validation_summary.decision == "review"
}

deny contains "masked_pct_gt_30" if {
  input.metrics.masked_pct > 30
}

deny contains "zscore_flag_true" if {
  input.flags.zscore_flag == true
}

deny contains "residual_sustained_true" if {
  input.flags.residual_sustained == true
}

deny contains "missing_evidence_bundle_ref" if {
  not input.evidence_bundle_ref
}

deny contains "missing_signatures" if {
  not input.signatures
}
