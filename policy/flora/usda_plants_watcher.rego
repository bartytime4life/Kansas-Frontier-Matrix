package kfm.flora.usda_plants_watcher

deny contains "USDA_PLANTS_WATCHER_PUBLISHED_TRUE" if { input.published }
deny contains "USDA_PLANTS_WATCHER_PROMOTED_TRUE" if { input.promoted }
deny contains "USDA_PLANTS_WATCHER_MISSING_RECEIPT_HASH" if { not input.receipt_hash }
