# KFM policy: fauna_deny_unpublished
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.fauna_deny_unpublished

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "fauna_deny_unpublished"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
