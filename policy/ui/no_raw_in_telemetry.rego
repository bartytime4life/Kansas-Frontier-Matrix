# KFM policy: no_raw_in_telemetry
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.no_raw_in_telemetry

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "no_raw_in_telemetry"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
