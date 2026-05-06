package kfm.flora.usda_plants_scheduled_observer_test
import data.kfm.flora.usda_plants_scheduled_observer
base := {"observation":{"publishes":false,"promotes":false,"creates_pr":false,"downloads_raw":false,"observation_hash":"sha256:a","change_summary":{"changed":false},"mode":"scheduled_mock","source_uri":"https://plants.sc.egov.usda.gov/downloads"},"alert":{"alert_hash":"sha256:b","severity":"none","requires_human_review":false},"queue":{"queue_hash":"sha256:c"},"bundle":{"bundle_hash":"sha256:d","refs":[]},"environment":{"KFM_ALLOW_SCHEDULED_OBSERVATION":"1"}}

test_valid { count(kfm.flora.usda_plants_scheduled_observer.deny with input as base)==0 }
test_pub { kfm.flora.usda_plants_scheduled_observer.deny contains "USDA_PLANTS_SCHEDULE_PUBLICATION_CLAIM" with input as object.union(base,{"observation":object.union(base.observation,{"publishes":true})}) }
