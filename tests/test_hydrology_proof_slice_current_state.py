import json
import unittest
from pathlib import Path


class HydrologyProofSliceCurrentStateTests(unittest.TestCase):
    def test_focus_abstains_when_bundle_closure_missing(self):
        p = Path("fixtures/domains/hydrology/focus/hydrology_synthetic_streamflow.public_abstain_missing_bundle_closure.json")
        data = json.loads(p.read_text())
        self.assertEqual(data.get("outcome"), "ABSTAIN")
        self.assertEqual(data.get("reason"), "MISSING_EVIDENCE")
        self.assertNotEqual(data.get("evidence_bundle_id"), "evb-hydro-synth-001")

    def test_promotion_denies_before_manifest_and_rollback_reference(self):
        p = Path(
            "fixtures/domains/hydrology/release_dry_runs/"
            "hydrology_synthetic_streamflow.publish_denied.missing_manifest_and_rollback_ref.json"
        )
        data = json.loads(p.read_text())
        self.assertEqual(data.get("decision"), "DENY")
        self.assertFalse(data.get("release_manifest_present"))
        self.assertFalse(data.get("rollback_reference_present"))
        self.assertFalse(data.get("publish_attempted"))


if __name__ == "__main__":
    unittest.main()
