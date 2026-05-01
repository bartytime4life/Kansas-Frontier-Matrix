package kfm.fauna.gbif_distribution_test
import data.kfm.fauna.gbif_distribution

test_missing_spec_hash_denied { some m; m:=gbif_distribution.deny with input as {"kind":"distribution_bundle","doc":{}} }
test_cache_reason_denied { some m; m:=gbif_distribution.deny with input as {"kind":"cache","doc":{}} }
