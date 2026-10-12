# KFM policy: bundle_closure_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.bundle_closure_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "bundle_closure_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
