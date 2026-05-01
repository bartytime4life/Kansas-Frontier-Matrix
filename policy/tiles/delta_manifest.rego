package tiles.delta_manifest

forbidden_path(path) if {
  is_string(path)
  re_match("(?i)(^|/)(RAW|WORK|QUARANTINE)(/|$)", path)
}

deny[msg] if {
  not input.base_pmtiles.spec_hash
  msg := "missing base_pmtiles.spec_hash"
}

deny[msg] if {
  tile := input.tiles[_]
  not tile.run_receipt_url
  msg := "missing tile run_receipt_url"
}

deny[msg] if {
  tile := input.tiles[_]
  not re_match("^sha256:[a-fA-F0-9]{64}$", tile.digest)
  msg := "malformed tile digest"
}

deny[msg] if {
  tile := input.tiles[_]
  tile.change_type == "modified"
  tile.prior_digest == null
  msg := "rollback-risk: modified tile missing prior_digest"
}

deny[msg] if {
  tile := input.tiles[_]
  tile.change_type == "removed"
  tile.prior_digest == null
  msg := "rollback-risk: removed tile missing prior_digest"
}

deny[msg] if {
  tile := input.tiles[_]
  tile.change_type == "added"
  tile.prior_digest != null
  msg := "rollback-risk: added tile has non-null prior_digest"
}

deny[msg] if {
  forbidden_path(input.base_pmtiles.url)
  msg := "base_pmtiles.url references RAW/WORK/QUARANTINE"
}

deny[msg] if {
  tile := input.tiles[_]
  forbidden_path(tile.run_receipt_url)
  msg := "run_receipt_url references RAW/WORK/QUARANTINE"
}
