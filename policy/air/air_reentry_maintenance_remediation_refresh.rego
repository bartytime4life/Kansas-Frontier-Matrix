package kfm.air.reentry_maintenance_remediation_refresh

default deny = []

bad_result(v) { v == "deny" }
bad_result(v) { v == "blocked" }

contains_lc(h, n) { contains(lower(h), lower(n)) }

json_text := lower(json.marshal(input))

deny[msg] {
  not input.reentry_continuous_assurance_refresh_summary
  msg := "ReentryContinuousAssuranceRefreshSummary is required"
}

deny[msg] {
  p := input.reentry_continuous_assurance_refresh_postcheck_report
  not p
  msg := "ReentryContinuousAssuranceRefreshPostcheckReport is required"
}

deny[msg] {
  p := input.reentry_continuous_assurance_refresh_postcheck_report
  bad_result(p.result)
  msg := "continuous assurance refresh postcheck denied/blocked"
}

deny[msg] {
  a := input.reentry_continuous_assurance_refresh_audit_report
  not a
  msg := "ReentryContinuousAssuranceRefreshAuditReport is required"
}

deny[msg] {
  a := input.reentry_continuous_assurance_refresh_audit_report
  a.result == "deny"
  msg := "continuous assurance refresh audit denied"
}

deny[msg] {
  l := input.reentry_continuous_assurance_refresh_ledger_manifest
  not l
  msg := "ReentryContinuousAssuranceRefreshLedgerManifest is required"
}

deny[msg] {
  l := input.reentry_continuous_assurance_refresh_ledger_manifest
  not l.chain_hash
  msg := "continuous assurance refresh ledger chain hash invalid"
}

deny[msg] {
  contains_lc(json_text, "data/raw/")
  msg := "RAW reference denied"
}

deny[msg] {
  contains_lc(json_text, "data/work/")
  msg := "WORK reference denied"
}

deny[msg] {
  contains_lc(json_text, "data/quarantine/")
  msg := "QUARANTINE reference denied"
}

deny[msg] {
  contains_lc(json_text, "data/processed/air/")
  msg := "PROCESSED exposure denied"
}

deny[msg] {
  contains_lc(json_text, "data/published/air/")
  msg := "published air references denied"
}

deny[msg] {
  contains_lc(json_text, "data/published/air/read_model/")
  msg := "published read model references denied"
}

deny[msg] {
  contains_lc(json_text, "kubectl")
  msg := "live operational instructions denied"
}

deny[msg] {
  contains_lc(json_text, "terraform")
  msg := "terraform instructions denied"
}

deny[msg] {
  contains_lc(json_text, "http://")
  msg := "live endpoint URLs denied"
}

deny[msg] {
  contains_lc(json_text, "https://")
  msg := "external URLs denied in fixture governance artifacts"
}
