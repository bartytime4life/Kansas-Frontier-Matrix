import unittest

from apps.api.kfm_mock_api import get_mock_focus, get_mock_policy


class MockApiReadOnlyRouteTests(unittest.TestCase):
    def test_get_mock_policy(self):
        payload, code = get_mock_policy()
        self.assertEqual(code, 200)
        self.assertEqual(payload.get("mode"), "SYNTHETIC_NO_NETWORK")
        self.assertEqual(payload.get("decision"), "ABSTAIN")

    def test_get_mock_focus(self):
        payload, code = get_mock_focus()
        self.assertEqual(code, 200)
        self.assertIn(payload.get("outcome"), {"ANSWER", "ABSTAIN", "DENY", "ERROR"})


if __name__ == "__main__":
    unittest.main()
