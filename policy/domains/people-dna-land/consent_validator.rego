# KFM policy: consent_validator
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.consent_validator

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "consent_validator"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
