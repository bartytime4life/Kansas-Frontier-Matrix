package kfm.fauna.ebird

deny[msg] if { not re_match("^sha256:[a-f0-9]{64}$", object.get(input, "kfm:spec_hash", "")); msg := "kfm:spec_hash missing or malformed" }
deny[msg] if { input.suppression_min_n < 10; msg := "suppression_min_n must be >= 10" }
deny[msg] if { input.aggregate; not input.aggregate in {"county", "huc12"}; msg := "aggregate must be county or huc12" }

deny[msg] if {
  is_public_layer
  object.get(input, "exact_points", "") != "restricted"
  msg := "exact_points must be restricted for public eBird layers"
}

deny[msg] if {
  is_public_layer
  some f in object.get(input, "allowlist_fields", object.get(input, "public_fields", []))
  lower(f) in {"decimallatitude","decimallongitude","latitude","longitude","lat","lon","point","geom","geometry"}
  msg := "public eBird layer allowlist contains exact coordinate field"
}

deny[msg] if {
  is_public_aggregate_row
  some k
  lower(k) in {"decimallatitude","decimallongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"}
  input[k]
  msg := "public aggregate rows containing exact coordinate fields"
}

deny[msg] if { is_public_aggregate_row; object.get(input, "policy_label", "") != "public_aggregate"; msg := "public aggregate output where policy_label is not public_aggregate" }
deny[msg] if { is_public_aggregate_row; not object.get(input, "kfm:spec_hash", ""); msg := "public aggregate output missing kfm:spec_hash" }
deny[msg] if { is_public_aggregate_row; input.checklist_count < input.suppression_min_n; msg := "public aggregate rows with checklist_count < suppression_min_n" }

is_public_layer if { object.get(input, "policy_label", "") == "public" or object.get(input, "policy_label", "") == "public_aggregate" }
is_public_aggregate_row if { object.get(input, "object_type", "") == "AggregateOccurrence" }


deny[msg] if { object.get(input,"object_type","")=="PromotionReceipt"; object.get(input,"policy_label","")!="public_aggregate"; msg:="promotion receipt policy_label must be public_aggregate" }
deny[msg] if { object.get(input,"object_type","")=="PromotionReceipt"; object.get(input,"public_safe",false)!=true; msg:="promotion receipt public_safe must be true" }
deny[msg] if { object.get(input,"object_type","")=="CatalogRecord"; object.get(input,"exact_points","")!="restricted"; msg:="catalog record exact_points must be restricted" }

deny[msg] if { object.get(input,"object_type","")=="PipelinePlan"; input.suppression_min_n < 10; msg := "pipeline plan suppression_min_n must be >= 10" }
deny[msg] if { object.get(input,"object_type","")=="PipelineManifest"; object.get(input,"public_safe_final_outputs",false) != true; msg := "pipeline manifest public_safe_final_outputs must be true" }
deny[msg] if { object.get(input,"object_type","")=="PipelineManifest"; object.get(input,"exact_points","") != "restricted"; msg := "pipeline manifest exact_points must be restricted" }
deny[msg] if { object.get(input,"object_type","")=="ValidationReport"; object.get(input,"status","")=="fail"; msg := "validation report status fail in promoted/public run" }

deny[msg] if {
  object.get(input,"object_type","")=="EbirdProductionCertificationPacket"
  object.get(input,"approval_decision","")=="approve"
  some g in object.get(input,"hard_gates",[])
  object.get(g,"status","")=="fail"
  msg := "approved certification contains failed hard gate"
}

deny[msg] if {
  object.get(input,"object_type","")=="PublicEbirdCorrectionRequestWorkflow"
  lower(json.marshal(input)) != ""
  contains(lower(json.marshal(input)), "credentials")
  msg := "public correction workflow requests credentials"
}

deny[msg] if {
  object.get(input,"object_type","")=="PublicEbirdTakedownRequestWorkflow"
  contains(lower(json.marshal(input)), "exact_private_locations")
  msg := "public takedown workflow requests exact private locations"
}

deny[msg] if {
  object.get(input,"object_type","")=="KfmEbirdVerifierFindingQueueItem"
  object.get(input,"severity","")=="critical"
  object.get(input,"finding_type","")=="public_safety_finding"
  object.get(input,"blocks_gate",false)!=true
  msg := "critical public-safety finding must block gate"
}

deny[msg] if {
  object.get(input,"object_type","")=="KfmEbirdVerifierFindingQueueItem"
  object.get(input,"severity","")=="critical"
  object.get(input,"finding_type","")=="public_safety_finding"
  object.get(input,"blocks_public_transparency_pass",false)!=true
  msg := "critical public-safety finding must block transparency"
}

deny[msg] if {
  object.get(input,"object_type","")=="KfmEbirdAuditResponsePacket"
  object.get(input,"status","")=="pass"
  some f in object.get(input,"findings",[])
  object.get(f,"severity","")=="critical"
  object.get(f,"response_status","")!="resolved"
  msg := "audit response packet pass while critical findings remain open"
}
