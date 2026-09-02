# KFM policy: citation_validation_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.citation_validation_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "citation_validation_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
