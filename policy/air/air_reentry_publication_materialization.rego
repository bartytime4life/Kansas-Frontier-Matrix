package air_reentry_publication_materialization

deny contains "MATERIALIZATION_PUBLISHED_PATH" if { contains(lower(json.marshal(input)), "data/published/air/") }
deny contains "MATERIALIZATION_READ_MODEL_PATH" if { contains(lower(json.marshal(input)), "data/published/air/read_model/") }
deny contains "MATERIALIZATION_RAW_WORK_QUARANTINE" if { re_match("(?i)(data/raw/|data/work/|data/quarantine/)", json.marshal(input)) }
deny contains "MATERIALIZATION_PROCESSED_EXPOSURE" if { contains(lower(json.marshal(input)), "data/processed/air/") }
deny contains "MATERIALIZATION_LIVE_OPS" if { re_match("(?i)(kubectl|terraform|pagerduty|slack|cdn purge|dns)", json.marshal(input)) }
deny contains "MATERIALIZATION_SECRET_LEAK" if { re_match("(?i)(secret|token|bearer|api[_-]?key|private[_-]?key)", json.marshal(input)) }
