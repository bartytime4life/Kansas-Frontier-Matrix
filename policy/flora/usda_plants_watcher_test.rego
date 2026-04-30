package kfm.flora.usda_plants_watcher_test
import data.kfm.flora.usda_plants_watcher

test_valid { count(usda_plants_watcher.deny with input as {"published":false,"promoted":false,"receipt_hash":"x"})==0 }
