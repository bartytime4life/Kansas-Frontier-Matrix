package kfm.flora.usda_plants

deny contains "USDA_PLANTS_MISSING_SPEC_HASH" if {
  not input.spec_hash
}

deny contains "USDA_PLANTS_SPEC_HASH_MISMATCH" if {
  input.spec_hash != input.properties["kfm:spec_hash"]
}

deny contains "USDA_PLANTS_NON_PUBLIC_POLICY" if {
  input.properties.policy_label != "public"
}

deny contains "USDA_PLANTS_BAD_LICENSE" if {
  input.properties.license != "USDA / U.S. Public Domain"
}

deny contains "USDA_PLANTS_BAD_RIGHTS_HOLDER" if {
  input.properties.rightsHolder != "United States Department of Agriculture"
}

deny contains "USDA_PLANTS_MISSING_PROVENANCE" if {
  not input.provenance.source_uri
}

deny contains "USDA_PLANTS_RAW_OUTPUT_REFERENCE" if {
  some ref in input.provenance.receipt_refs
  contains(lower(ref), "raw")
}

deny contains "USDA_PLANTS_RAW_OUTPUT_REFERENCE" if {
  some ref in input.provenance.raw_refs
  startswith(upper(ref), "RAW/")
}

deny contains "USDA_PLANTS_RAW_OUTPUT_REFERENCE" if {
  some ref in input.provenance.raw_refs
  startswith(upper(ref), "WORK/")
}

deny contains "USDA_PLANTS_RAW_OUTPUT_REFERENCE" if {
  some ref in input.provenance.raw_refs
  startswith(upper(ref), "QUARANTINE/")
}

deny contains "USDA_PLANTS_BAD_FIPS" if {
  some county in input.distributions.county
  not regex.match("^[0-9]{5}$", county.fips)
}

deny contains "USDA_PLANTS_MISSING_AUTHOR" if {
  not regex.match("^[A-Z][a-z-]+\\s+[a-z-]+\\s+.+$", trim(input.properties.scientificName))
}
