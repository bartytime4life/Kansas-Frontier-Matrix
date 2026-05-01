package air.reentry_continuous_assurance_refresh

default allow = false
allow { not deny[_] }

deny[msg] {
  some a in input.artifacts
  t := lower(json.marshal(a))
  contains(t, "data/raw/")
  msg := "raw path forbidden"
}

deny[msg] {
  some a in input.artifacts
  t := lower(json.marshal(a))
  contains(t, "data/work/") or contains(t, "data/quarantine/") or contains(t, "data/processed/air/")
  msg := "unsafe lifecycle path forbidden"
}

deny[msg] {
  some a in input.artifacts
  t := lower(json.marshal(a))
  contains(t, "data/published/air/")
  msg := "published path forbidden"
}

deny[msg] {
  some a in input.artifacts
  t := lower(json.marshal(a))
  contains(t, "http://") or contains(t, "https://") or contains(t, "kubectl") or contains(t, "terraform")
  msg := "live operational instruction forbidden"
}
