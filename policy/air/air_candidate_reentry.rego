package kfm.air.candidate_reentry

default deny = []

deny[msg] { contains(lower(json.marshal(input)), "data/raw/"); msg := "raw/work/quarantine denied" }
deny[msg] { contains(lower(json.marshal(input)), "data/processed/air/"); msg := "processed exposure denied" }
deny[msg] { contains(lower(json.marshal(input)), "data/published/air/"); msg := "published mutation denied" }
deny[msg] { re_match("(?i)(secret|token|bearer|webhook|slack|pagerduty|calendar|kubectl|terraform|dns|cdn purge)", json.marshal(input)); msg := "secret/live instruction denied" }
deny[msg] { contains(lower(json.marshal(input)), "production"); contains(lower(json.marshal(input)), "fixture_signature"); msg := "fixture production claim denied" }
