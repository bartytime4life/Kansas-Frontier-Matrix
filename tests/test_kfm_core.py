import unittest

from packages.kfm_core.envelopes import runtime_envelope
from packages.kfm_core.identity import make_id
from packages.kfm_core.policy import allow_public, policy_decision_for_sensitivity


class KfmCoreTests(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(make_id("ev", 1), "ev-001")
        with self.assertRaises(ValueError):
            make_id("", 1)

    def test_envelope(self):
        env = runtime_envelope("ANSWER", {"ok": True})
        self.assertEqual(env["outcome"], "ANSWER")
        with self.assertRaises(ValueError):
            runtime_envelope("MAYBE", {})

    def test_policy(self):
        self.assertTrue(allow_public("PUBLIC_SAFE"))
        self.assertEqual(policy_decision_for_sensitivity("RESTRICTED"), "DENY")
