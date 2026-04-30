package kfm.flora.usda_plants_live_fetch_test
import data.kfm.flora.usda_plants_live_fetch

test_valid { count(usda_plants_live_fetch.deny with input as {"plan":{"plan_hash":"x"},"receipt":{"receipt_hash":"y"}})==0 }
