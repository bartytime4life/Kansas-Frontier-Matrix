package kfm.flora.usda_plants_tile_archives
import rego.v1
test_valid_no_denies if { count(data.kfm.flora.usda_plants_tile_archives.deny with input as {"archive_publication_approval":{"approver":{"approver_type":"human"}},"static_host_handoff":{"deploys":false}})==0 }
