from __future__ import annotations

from tools.receipts.compare_receipt_sets import compare_manifests


def test_compare_manifests_detects_added_removed_and_changed() -> None:
    left_manifest = {
        "manifest_id": "kfm.receipt_manifest.ecology.left",
        "receipts": [
            {
                "receipt_type": "validator_result",
                "receipt_ref": "validator.json",
                "decision": "pass",
            },
            {
                "receipt_type": "proof_result",
                "receipt_ref": "proof.json",
                "decision": "proof_required",
            },
        ],
    }

    right_manifest = {
        "manifest_id": "kfm.receipt_manifest.ecology.right",
        "receipts": [
            {
                "receipt_type": "validator_result",
                "receipt_ref": "validator.json",
                "decision": "fail",
            },
            {
                "receipt_type": "promotion_result",
                "receipt_ref": "promotion.json",
                "decision": "pass",
            },
        ],
    }

    diff = compare_manifests(left_manifest, right_manifest)

    assert diff["summary"] == {
        "added_count": 1,
        "removed_count": 1,
        "changed_count": 1,
    }
    assert diff["added"][0]["receipt_type"] == "promotion_result"
    assert diff["removed"][0]["receipt_type"] == "proof_result"
    assert diff["changed"][0]["receipt_ref"] == "validator.json"
