package fauna.gbif_runtime_answer

forbidden := {"confirmed present","verified present"}

deny[msg] { not input.answer["kfm:spec_hash"]; msg := "runtime answer missing kfm:spec_hash" }
deny[msg] { input.answer.answer_posture == "cited_answer"; count(input.answer.claims)==0; msg := "cited_answer with no claims" }
deny[msg] { input.answer.answer_posture == "cited_answer"; not input.answer.answer_receipt_ref; msg := "cited_answer missing answer_receipt_ref" }
deny[msg] { some c in input.answer.claims; count(c.citations)==0; msg := "cited_answer with no citations" }
deny[msg] { some c in input.answer.claims; c.rights_posture != "public_allowed"; msg := "rights_posture != public_allowed" }
deny[msg] { some c in input.answer.claims; c.sensitivity_posture == "restricted"; msg := "sensitivity_posture == restricted" }
deny[msg] { some c in input.answer.claims; c.presence_posture != "reported_occurrence_not_confirmed_presence"; msg := "presence_posture invalid" }
deny[msg] { input.query.query_type=="exact_coordinates"; input.answer.answer_posture!="abstain"; msg := "exact-coordinate query must abstain" }
deny[msg] { input.query.query_type=="confirmed_presence"; input.answer.answer_posture!="abstain"; msg := "confirmed-presence query must abstain" }
deny[msg] { lower(input.answer.summary) in forbidden; msg := "forbidden language" }
deny[msg] { not input.receipt.policy_version; msg := "answer receipt missing policy_version" }
deny[msg] { input.receipt.geoprivacy_checked != true; msg := "answer receipt missing geoprivacy_checked == true" }
