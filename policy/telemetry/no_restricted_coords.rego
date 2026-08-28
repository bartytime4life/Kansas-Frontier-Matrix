# KFM policy: no_restricted_coords
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.no_restricted_coords

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "no_restricted_coords"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
