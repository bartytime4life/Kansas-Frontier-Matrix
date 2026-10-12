# KFM policy: infrastructure_interior
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.infrastructure_interior

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "infrastructure_interior"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
