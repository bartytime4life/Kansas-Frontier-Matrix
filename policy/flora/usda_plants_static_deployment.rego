package flora.usda_plants_static_deployment

deny[msg] { not input.deployment_approval.approved_by; msg := "missing human approval" }
deny[msg] { input.deployment_approval.approval_actor_type != "human"; msg := "non-human approval" }
deny[msg] { some r in input.refs; contains(r,"/raw/") or contains(r,"/work/") or contains(r,"/quarantine/"); msg := "raw/work/quarantine refs" }
deny[msg] { some k; k := input.claims[_]; contains(lower(k),"occurrence_lat") or contains(lower(k),"occurrence_lon"); msg := "occurrence coordinate leaks" }
deny[msg] { input.claims.external_basemap == true; msg := "external basemap claims" }
deny[msg] { input.claims.long_lived_secrets == true; msg := "long-lived secret claims" }
deny[msg] { count(input.hashes) == 0; msg := "missing hashes" }
deny[msg] { not contains(lower(input.attribution),"usda plants") ; msg := "bad attribution" }
deny[msg] { input.claims.auto_merge == true; msg := "auto-merge claims" }
