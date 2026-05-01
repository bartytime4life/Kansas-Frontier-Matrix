package air.reentry_operational_handoff_refresh

default allow = false

allow {
  not deny[_]
}

deny[msg] {
  some a in input.artifacts
  contains(lower(json.marshal(a)), "data/raw/")
  msg := "raw path forbidden"
}

deny[msg] {
  some a in input.artifacts
  contains(lower(json.marshal(a)), "data/processed/air/")
  msg := "processed path forbidden"
}

deny[msg] {
  some a in input.artifacts
  contains(lower(json.marshal(a)), "data/published/air/")
  msg := "published path forbidden"
}
