# KFM policy: dna_segment_public_deny
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.dna_segment_public_deny

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "dna_segment_public_deny"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
