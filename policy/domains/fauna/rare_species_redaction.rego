# KFM policy: rare_species_redaction
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.rare_species_redaction

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "rare_species_redaction"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
