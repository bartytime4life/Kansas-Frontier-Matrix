# KFM policy: attribution_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.attribution_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "attribution_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
