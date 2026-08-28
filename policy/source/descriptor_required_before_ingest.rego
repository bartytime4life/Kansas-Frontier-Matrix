# KFM policy: descriptor_required_before_ingest
# Status: PROPOSED greenfield stub. No real rules yet.
package kfm.descriptor_required_before_ingest

default deny := false

# Example structure — stewards will fill in.
# deny[reason] {
#     input.kind == "descriptor_required_before_ingest"
#     not input.evidence_bundle_resolved
#     reason := "evidence_bundle_unresolved"
# }
