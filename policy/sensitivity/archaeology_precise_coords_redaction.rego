# KFM policy: archaeology_precise_coords_redaction
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.archaeology_precise_coords_redaction

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "archaeology_precise_coords_redaction"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
