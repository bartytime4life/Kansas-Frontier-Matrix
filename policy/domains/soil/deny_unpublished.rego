# KFM policy: soil_deny_unpublished
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.soil_deny_unpublished

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "soil_deny_unpublished"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
