# KFM policy: two_steward_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.two_steward_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "two_steward_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
