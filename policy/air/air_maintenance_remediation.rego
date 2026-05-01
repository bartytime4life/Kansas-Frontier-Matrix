package kfm.air.maintenance_remediation

default deny = []

deny[msg] {
  some a in input.artifacts
  contains(lower(a.path), "data/raw/")
  msg := "raw/work/quarantine/processed references are denied"
}

deny[msg] {
  contains(lower(json.marshal(input)), "kubectl")
  msg := "live operational instructions denied"
}
