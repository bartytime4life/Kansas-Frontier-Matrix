# KFM policy: rollback_card_required
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.rollback_card_required

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "rollback_card_required"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
