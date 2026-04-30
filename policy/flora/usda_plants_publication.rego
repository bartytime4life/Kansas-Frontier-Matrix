package kfm.flora.usda_plants_publication
import rego.v1
deny contains "USDA_PLANTS_PUBLICATION_APPROVAL_MISSING" if { not input.publication_approval }
deny contains "USDA_PLANTS_PUBLICATION_NON_HUMAN_APPROVAL" if { input.publication_approval.approver.approver_type != "human" }
deny contains "USDA_PLANTS_PUBLICATION_PROMOTED_PACKAGE_MISSING" if { not input.promoted_package }
deny contains "USDA_PLANTS_PUBLICATION_PROMOTED_PACKAGE_NOT_SEALED" if { input.promoted_package.sealed != true }
deny contains "USDA_PLANTS_PUBLICATION_MISSING_RELEASE_HASH" if { not input.release_manifest.release_hash }
deny contains "USDA_PLANTS_PUBLICATION_MISSING_RECEIPT_HASH" if { not input.publication_receipt.receipt_hash }
deny contains "USDA_PLANTS_PUBLICATION_MISSING_LEDGER_HASH" if { not input.publication_ledger.ledger_hash }
deny contains "USDA_PLANTS_PUBLICATION_AUTO_MERGE_CLAIM" if { input.auto_merge == true }
