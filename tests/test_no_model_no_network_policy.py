import unittest

from apps.api.no_model_no_network_policy import FINITE_OUTCOMES, focus_mock


class NoModelNoNetworkPolicyTests(unittest.TestCase):
    def test_focus_mock_finite_outcomes_only(self):
        cases = [
            {"question": "", "expected": "ABSTAIN"},
            {"question": "q", "network_required": True, "expected": "DENY"},
            {"question": "q", "model_required": True, "expected": "DENY"},
            {"question": "q", "evidence_resolved": False, "expected": "ABSTAIN"},
            {"question": "q", "evidence_resolved": True, "expected": "ANSWER"},
        ]
        for case in cases:
            expected = case.pop("expected")
            out = focus_mock(case)
            self.assertEqual(out["outcome"], expected)
            self.assertIn(out["outcome"], FINITE_OUTCOMES)

    def test_non_dict_request_errors(self):
        out = focus_mock("not-a-dict")
        self.assertEqual(out["outcome"], "ERROR")


if __name__ == "__main__":
    unittest.main()
