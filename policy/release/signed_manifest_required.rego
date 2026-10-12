# KFM policy: signed_manifest_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.signed_manifest_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "signed_manifest_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
