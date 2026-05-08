# KFM policy: promotion_prerequisites
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.promotion_prerequisites

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "promotion_prerequisites"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
