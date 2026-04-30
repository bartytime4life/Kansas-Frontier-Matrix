package kfm.flora.usda_plants_test

import data.kfm.flora.usda_plants

base := {
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "properties": {
    "kfm:spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "policy_label": "public",
    "license": "USDA / U.S. Public Domain",
    "rightsHolder": "United States Department of Agriculture",
    "scientificName": "Achillea millefolium L."
  },
  "provenance": {
    "source_uri": "https://plants.sc.egov.usda.gov/downloads",
    "raw_refs": ["tests/fixtures/flora/usda_plants/raw/checklist.csv"],
    "receipt_refs": ["receipts/flora/usda_plants/ingest_receipt.json"]
  },
  "distributions": {"county": [{"fips": "20091"}]}
}

test_valid_has_no_denies if {
  count(usda_plants.deny with input as base) == 0
}

test_missing_spec_hash_denied if {
  "USDA_PLANTS_MISSING_SPEC_HASH" in usda_plants.deny with input as object.remove(base, ["spec_hash"])
}

test_mismatched_spec_hash_denied if {
  mismatched := object.union(base, {"properties": object.union(base.properties, {"kfm:spec_hash": "sha256:bbbb"})})
  "USDA_PLANTS_SPEC_HASH_MISMATCH" in usda_plants.deny with input as mismatched
}

test_bad_license_denied if {
  bad := object.union(base, {"properties": object.union(base.properties, {"license": "CC-BY"})})
  "USDA_PLANTS_BAD_LICENSE" in usda_plants.deny with input as bad
}

test_bad_fips_denied if {
  bad := object.union(base, {"distributions": {"county": [{"fips": "20A91"}]}})
  "USDA_PLANTS_BAD_FIPS" in usda_plants.deny with input as bad
}

test_missing_author_denied if {
  bad := object.union(base, {"properties": object.union(base.properties, {"scientificName": "Achillea millefolium"})})
  "USDA_PLANTS_MISSING_AUTHOR" in usda_plants.deny with input as bad
}

test_raw_output_reference_denied if {
  bad := object.union(base, {"provenance": object.union(base.provenance, {"raw_refs": ["RAW/flora/usda.csv"]})})
  "USDA_PLANTS_RAW_OUTPUT_REFERENCE" in usda_plants.deny with input as bad
}
