package kfm.air.reentry_maintenance_rollforward_refresh

default deny = []
json_text := lower(json.marshal(input))
contains_lc(h, n) { contains(lower(h), lower(n)) }

deny[msg] { not input.reentry_maintenance_refresh_closure_record; msg := "ReentryMaintenanceRefreshClosureRecord is required" }
deny[msg] { not input.reentry_remediation_refresh_rollforward_plan; msg := "ReentryRemediationRefreshRollforwardPlan is required" }
deny[msg] { contains_lc(json_text,"data/raw/"); msg := "RAW reference denied" }
deny[msg] { contains_lc(json_text,"data/work/"); msg := "WORK reference denied" }
deny[msg] { contains_lc(json_text,"data/quarantine/"); msg := "QUARANTINE reference denied" }
deny[msg] { contains_lc(json_text,"data/processed/air/"); msg := "PROCESSED exposure denied" }
deny[msg] { contains_lc(json_text,"data/published/air/"); msg := "published air reference denied" }
deny[msg] { contains_lc(json_text,"data/published/air/read_model/"); msg := "published read model reference denied" }
deny[msg] { contains_lc(json_text,"http://") ; msg := "live endpoint denied" }
deny[msg] { contains_lc(json_text,"https://") ; msg := "external endpoint denied" }
