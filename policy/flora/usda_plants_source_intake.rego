package kfm.flora.usda_plants_source_intake

deny contains "USDA_PLANTS_SOURCE_NON_USDA_URI" if { input.source_uri != "https://plants.sc.egov.usda.gov/downloads" }
deny contains "USDA_PLANTS_SOURCE_NETWORK_ENABLED_IN_CI" if { input.network_mode == "manual_enabled"; input.environment.ci == true }
deny contains "USDA_PLANTS_SOURCE_MISSING_CHECKSUM" if { some f in input.raw_files; not startswith(f.sha256,"sha256:") }
deny contains "USDA_PLANTS_SOURCE_MISSING_REQUIRED_ROLE" if { count(input.missing_roles) > 0 }
deny contains "USDA_PLANTS_SOURCE_QUARANTINE_OPEN" if { input.quarantine_report.status == "open" }
deny contains "USDA_PLANTS_SOURCE_DRIFT_FAIL" if { input.drift_report.status == "fail" }
deny contains "USDA_PLANTS_SOURCE_STAGE_FROM_FAILED_RAW" if { input.staged_manifest.raw_manifest_status != "pass" }
deny contains "USDA_PLANTS_SOURCE_STAGE_WITH_QUARANTINE" if { input.drift_report.quarantine_required == true }
deny contains "USDA_PLANTS_SOURCE_WRITES_PUBLISHED" if { some f in input.raw_files; contains(f.path,"published/") }
deny contains "USDA_PLANTS_SOURCE_WRITES_PUBLISHED" if { some f in input.staged_manifest.staged_files; contains(f.path,"published/") }
deny contains "USDA_PLANTS_SOURCE_MISSING_HASH" if { not input.manifest_hash }
