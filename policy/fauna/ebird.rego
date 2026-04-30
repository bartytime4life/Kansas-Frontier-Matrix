package kfm.fauna.ebird

# Best-effort predicate checks use string containment, not a full parser.

deny[msg] if {
  not input.source_uri
  msg := "source_uri missing"
}

deny[msg] if {
  not input.query_predicate
  msg := "query_predicate missing"
}

deny[msg] if {
  not re_match("^sha256:[a-f0-9]{64}$", object.get(input, "kfm:spec_hash", ""))
  msg := "kfm:spec_hash missing or malformed"
}

deny[msg] if {
  input.suppression_min_n < 10
  msg := "suppression_min_n must be >= 10"
}

deny[msg] if {
  input.aggregate
  not input.aggregate in {"county", "huc12"}
  msg := "aggregate must be county or huc12"
}

deny[msg] if {
  is_public
  exact_field := lower(input.public_fields[_])
  exact_field in {"decimallatitude", "decimallongitude", "latitude", "longitude", "lat", "lon", "geom", "geometry"}
  msg := sprintf("public layer exposes exact field: %s", [exact_field])
}

deny[msg] if {
  is_public
  object.get(input, "exact_points", "") != "restricted"
  msg := "exact_points must be restricted for public eBird layers"
}

deny[msg] if {
  is_public
  qp := lower(input.query_predicate)
  not contains(qp, "complete==true")
  msg := "query_predicate must require complete checklists (best-effort)"
}

deny[msg] if {
  is_public
  qp := lower(input.query_predicate)
  not contains(qp, "protocol_type!='incidental'")
  msg := "query_predicate must exclude incidental protocol_type (best-effort)"
}

deny[msg] if {
  is_public
  qp := lower(input.query_predicate)
  not contains(qp, "duration_min>=5")
  msg := "query_predicate must include duration_min>=5 (best-effort)"
}

deny[msg] if {
  is_public
  qp := lower(input.query_predicate)
  not contains(qp, "distance_km<=5")
  msg := "query_predicate must include distance_km<=5 (best-effort)"
}

deny[msg] if {
  is_public
  qp := lower(input.query_predicate)
  not contains(qp, "number_observers<=10")
  msg := "query_predicate must include number_observers<=10 (best-effort)"
}

is_public if {
  object.get(input, "policy_label", "public") == "public"
}
