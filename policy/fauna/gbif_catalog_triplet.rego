package kfm.fauna.gbif_catalog_triplet

deny[msg] if { input.catalog_entry == null; msg := "missing catalog entry" }
deny[msg] if { not input.evidence; msg := "missing triplet evidence block" }
deny[msg] if { not input.source_evidence_bundle_id; msg := "missing source_evidence_bundle_id" }
deny[msg] if { not input.download_key; msg := "missing download_key" }
deny[msg] if { not input.geoprivacy_receipt_ref; msg := "missing geoprivacy_receipt_ref" }
deny[msg] if { not input["kfm:spec_hash"]; msg := "missing kfm:spec_hash" }
deny[msg] if { input.rights_posture != "public_allowed"; msg := "rights_posture != public_allowed" }
deny[msg] if { input.sensitivity_posture == "restricted"; msg := "sensitivity_posture == restricted" }
deny[msg] if { input.presence_posture != "reported_occurrence_not_confirmed_presence"; msg := "presence_posture invalid" }
deny[msg] if { contains(lower(input.claim_text), "confirmed present"); msg := "forbidden confirmed presence language" }
deny[msg] if { input.answer_posture == "cited_answer"; count(input.claims) > 0; some i; count(input.claims[i].citations)==0; msg := "claims and no citations" }
deny[msg] if { input.decimalLatitude; msg := "readmodel exposes decimalLatitude" }
deny[msg] if { input.decimalLongitude; msg := "readmodel exposes decimalLongitude" }
deny[msg] if { input.query.exact_coordinates_requested; input.answer_posture != "abstain"; msg := "exact-coordinate query must abstain" }
