package kfm.air.qa

default allow := false

allow if {
  count(deny) == 0
}

deny[msg] if {
  input.metrics.nowcast_max > 35
  msg := "gate_a_nowcast_max_exceeds_35"
}

deny[msg] if {
  input.metrics.nowcast_vs_baseline_sigma > 2
  msg := "gate_b_nowcast_vs_baseline_sigma_exceeds_2"
}

deny[msg] if {
  input.metrics.station_coverage_pct < 75
  msg := "gate_c_station_coverage_below_75"
}

deny[msg] if {
  input.aqs_flags_summary.hard_denial_rows_in_baseline > 0
  msg := "aqs_hard_denial_rows_present_in_baseline"
}

deny[msg] if {
  input.decision == "candidate"
  not input.flags.run_receipt_ref
  msg := "missing_run_receipt_ref_for_public_promotion"
}

deny[msg] if {
  input.decision == "candidate"
  not input.flags.evidence_bundle_ref
  msg := "missing_evidence_bundle_ref_for_public_promotion"
}
