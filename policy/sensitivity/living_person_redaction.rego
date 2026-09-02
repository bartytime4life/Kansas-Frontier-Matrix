# KFM policy: living_person_redaction
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.living_person_redaction

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "living_person_redaction"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
