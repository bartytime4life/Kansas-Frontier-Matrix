package kfm.air.operational_handoff

default allow = false

unsafe_path[p] { some p in input.paths; contains(lower(p), "data/raw/") }
unsafe_path[p] { some p in input.paths; contains(lower(p), "data/work/") }
unsafe_path[p] { some p in input.paths; contains(lower(p), "data/quarantine/") }
unsafe_path[p] { some p in input.paths; contains(lower(p), "data/processed/air/") }

deny[msg] { not input.cutover_observation_present; msg := "missing cutover" }
deny[msg] { input.post_deploy_gate_result == "deny"; msg := "post deploy denied" }
deny[msg] { input.watch_window_result == "deny"; msg := "watch denied" }
deny[msg] { count(unsafe_path) > 0; msg := "unsafe path" }
allow { count(deny) == 0 }
