# KFM policy: license_compatibility
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.license_compatibility

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "license_compatibility"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
