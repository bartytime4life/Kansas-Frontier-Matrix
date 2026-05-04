import unittest
from apps.api.kfm_mock_api import focus_decision

class T(unittest.TestCase):
    def test_finite_outcomes(self):
        qs=[
            ("What does the synthetic hydrology record say about HYDRO_SYNTH_001 on 2026-04-20?","ANSWER"),
            ("What does the record say about HYDRO_SYNTH_MISSING?","ABSTAIN"),
            ("policy blocked synthetic question","DENY"),
        ]
        for q,expected in qs:
            payload,_=focus_decision({'question':q})
            self.assertEqual(payload['outcome'],expected)
