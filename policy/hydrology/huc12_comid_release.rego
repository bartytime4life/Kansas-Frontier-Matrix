package kfm.hydrology.huc12_comid_release

default allow := false

bad_lifecycle(uri) if {
  re_match(".*/(raw|work|quarantine)/.*", lower(uri))
}

deny contains "catalog record is missing" if not input.catalog

deny contains "evidence bundle is missing" if not input.evidence_bundle

deny contains "manifest validation result is not ok" if not input.manifest_validation_ok

deny contains "crosswalk digest check is not ok" if not input.crosswalk_digest_check_ok

deny contains "run receipt verification is not true" if not input.run_receipt_verified

deny contains "evidence bundle signature verification is not true" if not input.evidence_bundle_signature_verified

deny contains "catalog release_state must be published for public resolution" if {
  input.require_public
  input.catalog.release_state != "published"
}

deny contains "manifest_id mismatch" if input.manifest.manifest_id != input.catalog.manifest_id
deny contains "manifest_id mismatch" if input.evidence_bundle.manifest_id != input.catalog.manifest_id

deny contains "timeslice_id mismatch" if input.manifest.timeslice_id != input.catalog.timeslice_id
deny contains "timeslice_id mismatch" if input.evidence_bundle.timeslice_id != input.catalog.timeslice_id

deny contains "crosswalk_digest mismatch" if input.manifest.crosswalk_digest != input.catalog.crosswalk_digest
deny contains "crosswalk_digest mismatch" if input.evidence_bundle.crosswalk_digest != input.catalog.crosswalk_digest

deny contains "manifest_digest mismatch" if input.actual_manifest_digest != input.catalog.manifest_digest
deny contains "manifest_digest mismatch" if input.evidence_bundle.manifest_digest != input.catalog.manifest_digest

deny contains "published uri lifecycle leakage" if bad_lifecycle(input.catalog.published_manifest_uri)
deny contains "published uri lifecycle leakage" if bad_lifecycle(input.catalog.published_crosswalk_uri)
deny contains "published uri lifecycle leakage" if bad_lifecycle(input.catalog.evidence_bundle_uri)

deny contains "steward review required but not approved" if {
  input.evidence_bundle.steward_review.required
  input.evidence_bundle.steward_review.status != "approved"
}

deny contains "overlapping conflicting time slices" if input.overlapping_conflict

allow if {
  count(deny) == 0
  input.catalog.release_state == "published"
}
