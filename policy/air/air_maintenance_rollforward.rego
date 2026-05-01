package kfm.air.maintenance_rollforward

default deny = []

deny[msg] { some a in input.artifacts; contains(lower(a.path), "data/raw/"); msg := "raw/work/quarantine denied" }
deny[msg] { contains(lower(json.marshal(input)), "data/processed/air/"); msg := "processed exposure denied" }
deny[msg] { contains(lower(json.marshal(input)), "data/published/air/"); msg := "published mutation denied" }
deny[msg] { contains(lower(json.marshal(input)), "destructive\":true"); msg := "destructive rollforward denied" }
deny[msg] { contains(lower(json.marshal(input)), "fixture_signature") ; contains(lower(json.marshal(input)), "production"); msg := "fixture production claim denied" }
deny[msg] { contains(lower(json.marshal(input)), "nowcast"); contains(lower(json.marshal(input)), "validated aqs truth"); msg := "nowcast truth conflation denied" }
deny[msg] { re_match("(?i)(secret|token|bearer|webhook|slack|pagerduty|calendar|kubectl|terraform|dns|cdn purge)", json.marshal(input)); msg := "secret/live instruction denied" }
