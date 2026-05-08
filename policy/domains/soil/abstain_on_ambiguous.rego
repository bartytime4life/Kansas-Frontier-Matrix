# KFM policy: soil_abstain_on_ambiguous
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.soil_abstain_on_ambiguous

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "soil_abstain_on_ambiguous"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
