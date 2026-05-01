package kfm.fauna.gbif_public_aggregate

deny[msg] if { input.decimalLatitude; msg := "exact coordinates in public aggregate" }
deny[msg] if { input.decimalLongitude; msg := "exact coordinates in public aggregate" }
deny[msg] if { not input.source_evidence_bundle_id; msg := "missing EvidenceBundle reference" }
deny[msg] if { not input.download_key; msg := "missing download_key" }
deny[msg] if { not input["kfm:spec_hash"]; msg := "missing kfm:spec_hash" }
deny[msg] if { not input.geoprivacy_receipt_ref; msg := "missing geoprivacy receipt" }
deny[msg] if { input.observation_count < 10; msg := "observation_count < 10" }
deny[msg] if { input.rights_posture != "public_allowed"; msg := "rights_posture != public_allowed" }
deny[msg] if { input.sensitivity_posture == "restricted"; msg := "sensitivity_posture == restricted" }
deny[msg] if { input.geometry_role != "generalized_public_area"; msg := "geometry_role != generalized_public_area" }
