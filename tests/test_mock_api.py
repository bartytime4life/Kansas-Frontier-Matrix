import unittest

from apps.api.kfm_mock_api import focus_decision, get_drawer, get_evidence_bundle


class MockApiTests(unittest.TestCase):
    def test_evidence_known(self):
        payload, code = get_evidence_bundle("evb-hydro-001")
        self.assertEqual(code, 200)
        self.assertEqual(payload["id"], "evb-hydro-001")

    def test_evidence_unknown(self):
        payload, code = get_evidence_bundle("unknown")
        self.assertEqual(code, 404)
        self.assertEqual(payload["outcome"], "ABSTAIN")

    def test_drawer_unknown(self):
        payload, code = get_drawer("missing")
        self.assertEqual(code, 404)
        self.assertEqual(payload["outcome"], "ABSTAIN")

    def test_focus_decision(self):
        payload, code = focus_decision({"question": "sensitive parcel"})
        self.assertEqual(code, 200)
        self.assertEqual(payload["outcome"], "DENY")
