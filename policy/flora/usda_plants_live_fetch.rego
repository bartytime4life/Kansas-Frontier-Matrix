package kfm.flora.usda_plants_live_fetch

deny contains "USDA_PLANTS_LIVE_MISSING_PLAN_HASH" if { not input.plan.plan_hash }
deny contains "USDA_PLANTS_LIVE_MISSING_RECEIPT_HASH" if { not input.receipt.receipt_hash }
