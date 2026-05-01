package fauna.gbif_runtime_answer_test
import data.fauna.gbif_runtime_answer

test_deny_missing_hash { d:=gbif_runtime_answer.deny with input as {"answer":{},"query":{},"receipt":{}}; count(d)>0 }
test_deny_exact_coordinate_must_abstain { d:=gbif_runtime_answer.deny with input as {"answer":{"kfm:spec_hash":"x","answer_posture":"cited_answer","claims":[],"answer_receipt_ref":"r"},"query":{"query_type":"exact_coordinates"},"receipt":{"policy_version":"v","geoprivacy_checked":true}}; count(d)>0 }
