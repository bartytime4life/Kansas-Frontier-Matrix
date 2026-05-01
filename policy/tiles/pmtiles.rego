package tiles.pmtiles

forbidden_path(path) if {
  is_string(path)
  re_match("(?i)(^|/)(RAW|WORK|QUARANTINE)(/|$)", path)
}

review_band if {
  input.masked_pct > 0.15
  input.masked_pct <= 0.30
}

deny[msg] if {
  forbidden_path(input.base_archive.href)
  msg := "public PMTiles refs cannot target RAW/WORK/QUARANTINE"
}

deny[msg] if {
  forbidden_path(input.delta_archive.href)
  msg := "public PMTiles refs cannot target RAW/WORK/QUARANTINE"
}

deny[msg] if {
  input.geoprivacy.sensitive_geometry
  not input.geoprivacy.redaction_receipt
  msg := "sensitive geometry requires geoprivacy receipt"
}

deny[msg] if {
  input.delta_archive.completeness_pct < 0.95
  msg := "delta promotion requires completeness >= 95%"
}

deny[msg] if {
  input.masked_pct > 0.30
  msg := "masked_pct > 30% is reject"
}

deny[msg] if {
  review_band
  not input.attestations.steward
  msg := "review band requires steward attestation"
}

deny[msg] if {
  review_band
  not input.attestations.reviewer
  msg := "review band requires reviewer attestation"
}

deny[msg] if {
  not input.rights
  msg := "unknown rights posture"
}

deny[msg] if {
  not input.license
  msg := "unknown license posture"
}

deny[msg] if {
  not re_match("^sha256:[a-f0-9]{64}$", input.base_archive.digest)
  msg := "missing or malformed base archive digest"
}

deny[msg] if {
  not re_match("^sha256:[a-f0-9]{64}$", input.delta_archive.digest)
  msg := "missing or malformed delta archive digest"
}

deny[msg] if {
  count(input.proof_refs) == 0
  msg := "missing proof refs"
}

deny[msg] if {
  count(input.signature_refs) == 0
  msg := "missing signature refs"
}
