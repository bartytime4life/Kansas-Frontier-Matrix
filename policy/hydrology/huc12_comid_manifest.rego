package kfm.hydrology.huc12_comid_manifest

default allow := false

allow if count(deny) == 0

deny[msg] if {
  not input.current
  msg := "missing current manifest"
}

deny[msg] if {
  not input.previous
  msg := "missing previous released manifest"
}

deny[msg] if {
  current := input.current
  startswith(current.spec_hash, "sha256:") == false
  msg := "spec_hash must use sha256"
}

deny[msg] if {
  current := input.current
  current.run_receipt_url_verified != true
  msg := "run_receipt_url_verified must be true"
}

deny[msg] if {
  previous := input.previous
  current := input.current
  previous.nhd_snapshot_id != current.nhd_snapshot_id
  msg := sprintf("nhd_snapshot_id changed from %v to %v", [previous.nhd_snapshot_id, current.nhd_snapshot_id])
}

deny[msg] if {
  previous := input.previous
  current := input.current
  previous.crosswalk_digest != current.crosswalk_digest
  msg := sprintf("crosswalk_digest changed from %v to %v", [previous.crosswalk_digest, current.crosswalk_digest])
}
