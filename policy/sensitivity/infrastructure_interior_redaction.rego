# KFM policy: infrastructure_interior_redaction
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.infrastructure_interior_redaction

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "infrastructure_interior_redaction"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
