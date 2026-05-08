# KFM policy: finite_envelope_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.finite_envelope_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "finite_envelope_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
