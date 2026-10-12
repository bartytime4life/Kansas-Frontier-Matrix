# KFM policy: released_only_for_public
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.released_only_for_public

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "released_only_for_public"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
