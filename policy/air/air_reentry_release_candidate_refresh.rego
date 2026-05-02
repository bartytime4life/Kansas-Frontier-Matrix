package kfm.air.reentry_release_candidate_refresh

default allow = false

is_bad_result(x) { x == "deny" }
is_bad_result(x) { x == "blocked" }

has_bad_path(v) {
  s := lower(json.marshal(v))
  contains(s, "data/raw/")
} {
  s := lower(json.marshal(v)); contains(s, "data/work/")
} {
  s := lower(json.marshal(v)); contains(s, "data/quarantine/")
} {
  s := lower(json.marshal(v)); contains(s, "data/processed/air/")
} {
  s := lower(json.marshal(v)); contains(s, "data/published/air/")
}

deny[msg] {
  not input.reentry_candidate_reentry_refresh_postcheck_report
  msg := "missing candidate reentry refresh postcheck"
}

deny[msg] {
  is_bad_result(input.reentry_candidate_reentry_refresh_postcheck_report.result)
  msg := "candidate reentry refresh postcheck denied"
}

deny[msg] {
  input.reentry_qa_revalidation_refresh_report
  is_bad_result(input.reentry_qa_revalidation_refresh_report.result)
  msg := "qa revalidation denied"
}

deny[msg] { has_bad_path(input); msg := "unsafe or published path reference" }

allow { count(deny) == 0 }
