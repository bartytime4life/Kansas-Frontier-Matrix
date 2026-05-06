package tiles.delta_apply

forbidden(v){ re_match("(?i)(/RAW/|/WORK/|/QUARANTINE/|raw://|work://|quarantine://)", v) }

deny contains "missing manifest hash" { not input.manifest_hash }
deny contains "missing base spec hash" { not input.base_spec_hash }
deny contains "missing receipt_version" { not input.receipt_version }
deny contains "forbidden input ref" { some k; forbidden(input.input_refs[k]) }
deny contains "forbidden output ref" { some k; forbidden(input.output_refs[k]) }
deny contains "pass receipt has rejected checks" { input.result=="PASS"; count(input.rejected_checks)>0 }
deny contains "pass receipt has failed checks" { input.result=="PASS"; some c in input.checks; c.result=="FAIL" }
