# KFM policy: abstain_on_missing_evidence
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.abstain_on_missing_evidence

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "abstain_on_missing_evidence"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
