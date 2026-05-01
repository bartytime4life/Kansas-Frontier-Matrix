package kfm.air.reentry_deployment_readiness_refresh

default allow = false

bad_path(p) {
  contains(lower(p), "data/raw/")
} {
  contains(lower(p), "data/work/")
} {
  contains(lower(p), "data/quarantine/")
} {
  contains(lower(p), "data/processed/air/")
} {
  contains(lower(p), "data/published/air/")
}

deny[msg] {
  not input.ReentryClientDeliveryRefreshPostcheckReport
  msg := "missing postcheck"
}

deny[msg] {
  input.ReentryClientDeliveryRefreshPostcheckReport.result == "deny"
  msg := "postcheck denied"
}

deny[msg] {
  some p in input.artifact_refs
  bad_path(p)
  msg := sprintf("unsafe path: %v", [p])
}

allow {
  count(deny) == 0
}
