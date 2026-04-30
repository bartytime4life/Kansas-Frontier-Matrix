package kfm.flora.usda_plants_source_intake

test_valid_no_deny if { count(data.kfm.flora.usda_plants_source_intake.deny with input as {"source_uri":"https://plants.sc.egov.usda.gov/downloads","network_mode":"disabled","environment":{"ci":true},"raw_files":[{"sha256":"sha256:abc","path":"raw/a"}],"missing_roles":[],"quarantine_report":{"status":"closed"},"drift_report":{"status":"pass","quarantine_required":false},"staged_manifest":{"raw_manifest_status":"pass","staged_files":[{"path":"work/a"}]},"manifest_hash":"sha256:abc"})==0 }
