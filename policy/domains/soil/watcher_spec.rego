package kfm.soil_watcher_spec

default allow := false

deny contains "SOIL_WATCHER_NETWORK_DENIED" if input.governance.network_authorized
deny contains "SOIL_WATCHER_EXECUTION_DENIED" if input.governance.execution_authorized
deny contains "SOIL_WATCHER_RAW_ADMISSION_DENIED" if input.governance.raw_admission_authorized
deny contains "SOIL_WATCHER_PROMOTION_DENIED" if input.governance.promotion_authorized
deny contains "SOIL_WATCHER_RELEASE_DENIED" if input.governance.release_authorized
deny contains "SOIL_WATCHER_PUBLICATION_DENIED" if input.governance.publication_authorized
deny contains "SOIL_WATCHER_LIVE_MODE_DENIED" if input.execution_mode != "FIXTURE_ONLY"
deny contains "SOIL_WATCHER_NETWORK_MODE_DENIED" if input.network_mode != "DENY"
deny contains "SOIL_WATCHER_OUTPUT_ZONE_DENIED" if {
  some i
  input.outputs[i].target_zone != "WORK"
  input.outputs[i].target_zone != "QUARANTINE"
}

allow if count(deny) == 0
