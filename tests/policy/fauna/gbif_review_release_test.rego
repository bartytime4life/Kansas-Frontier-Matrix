package fauna.gbif_review_release_test
import data.fauna.gbif_review_release

test_basic { count(gbif_review_release.deny with input as {"kind":"review_item","doc":{}})>0 }
