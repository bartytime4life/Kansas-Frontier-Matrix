# KFM policy: deny_unpublished_public
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.deny_unpublished_public

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "deny_unpublished_public"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
