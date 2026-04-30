package kfm.flora.usda_plants_scheduled_observer

deny contains "USDA_PLANTS_SCHEDULE_PUBLICATION_CLAIM" if { input.observation.publishes }
deny contains "USDA_PLANTS_SCHEDULE_PROMOTION_CLAIM" if { input.observation.promotes }
deny contains "USDA_PLANTS_SCHEDULE_AUTO_PR_CLAIM" if { input.observation.creates_pr }
deny contains "USDA_PLANTS_SCHEDULE_WRITES_PUBLISHED" if { some r in input.bundle.refs; startswith(r.path,"published/") }
deny contains "USDA_PLANTS_SCHEDULE_DOWNLOADS_RAW_BY_DEFAULT" if { input.observation.downloads_raw; not input.allow_raw_download }
deny contains "USDA_PLANTS_SCHEDULE_MISSING_OBSERVATION_HASH" if { not input.observation.observation_hash }
deny contains "USDA_PLANTS_SCHEDULE_MISSING_ALERT_HASH" if { not input.alert.alert_hash }
deny contains "USDA_PLANTS_SCHEDULE_MISSING_QUEUE_HASH" if { not input.queue.queue_hash }
deny contains "USDA_PLANTS_SCHEDULE_MISSING_BUNDLE_HASH" if { not input.bundle.bundle_hash }
deny contains "USDA_PLANTS_SCHEDULE_CRITICAL_WITHOUT_REVIEW" if { input.alert.severity=="critical"; not input.alert.requires_human_review }
deny contains "USDA_PLANTS_SCHEDULE_CHANGED_WITHOUT_ALERT" if { input.observation.change_summary.changed; input.alert.severity=="none" }
deny contains "USDA_PLANTS_SCHEDULE_REAL_NETWORK_WITHOUT_ENV" if { input.observation.mode=="scheduled_observe_only"; input.environment.KFM_ALLOW_SCHEDULED_OBSERVATION != "1" }
deny contains "USDA_PLANTS_SCHEDULE_NON_USDA_SOURCE" if { not startswith(input.observation.source_uri,"https://plants.sc.egov.usda.gov/downloads"); not (input.test_mode and startswith(input.observation.source_uri,"http://localhost")) }
