package tiles.delta_apply

test_valid { count(deny with input as {"receipt_version":"v1","result":"PASS","manifest_hash":"sha256:1111111111111111111111111111111111111111111111111111111111111111","base_spec_hash":"sha256:2222222222222222222222222222222222222222222222222222222222222222","input_refs":{"manifest":"tests/a","base_store":"tests/b","delta_store":"tests/c","ledger":"tests/d"},"output_refs":{"out_store":"tests/o"},"checks":[{"name":"x","result":"PASS"}],"rejected_checks":[]} )==0 }

test_missing_hash { "missing manifest hash" in deny with input as {"receipt_version":"v1","result":"PASS","base_spec_hash":"sha256:2","input_refs":{},"output_refs":{},"checks":[],"rejected_checks":[]} }
