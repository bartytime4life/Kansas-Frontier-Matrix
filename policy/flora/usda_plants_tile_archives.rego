package kfm.flora.usda_plants_tile_archives
import rego.v1
deny contains "USDA_PLANTS_ARCHIVE_APPROVAL_MISSING" if { not input.archive_publication_approval }
deny contains "USDA_PLANTS_ARCHIVE_NON_HUMAN_APPROVAL" if { input.archive_publication_approval.approver.approver_type != "human" }
deny contains "USDA_PLANTS_ARCHIVE_DEPLOYMENT_CLAIM" if { input.static_host_handoff.deploys }
