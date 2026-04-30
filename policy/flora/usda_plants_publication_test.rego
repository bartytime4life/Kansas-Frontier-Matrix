package kfm.flora.usda_plants_publication_test
import rego.v1
import data.kfm.flora.usda_plants_publication
base := {"publication_approval":{"approver":{"approver_type":"human"}},"promoted_package":{"sealed":true},"release_manifest":{"release_hash":"sha256:x"},"publication_receipt":{"receipt_hash":"sha256:x"},"publication_ledger":{"ledger_hash":"sha256:x"},"auto_merge":false}
test_valid if { count(usda_plants_publication.deny with input as base) == 0 }
