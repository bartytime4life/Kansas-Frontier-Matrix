# KFM policy: archaeology_precise_coords
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.archaeology_precise_coords

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "archaeology_precise_coords"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
