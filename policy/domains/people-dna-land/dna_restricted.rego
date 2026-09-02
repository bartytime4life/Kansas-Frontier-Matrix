# KFM policy: dna_restricted
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.dna_restricted

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "dna_restricted"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
