import importlib.util, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/"tools/validators/ai/validate_ai_evaluator_harness.py"
spec=importlib.util.spec_from_file_location("evalh", P)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class EvaluatorHarnessTests(unittest.TestCase):
    def test_fixture_replay(self):
        self.assertEqual([], m.replay())
    def test_pass_requires_allow(self):
        r={"evaluation_id":"x","artifact_kind":"vector","candidate_ref":"c","evidence_refs":["e"],"metrics":[{"name":"m","value":1,"threshold":1,"comparison":"gte"}],"policy_outcome":"HOLD","deterministic":True,"network_access":False,"result":"PASS","reason_codes":[],"spec_hash":"sha256:"+"a"*64}
        self.assertEqual("DENY", m.evaluate(r))
    def test_network_is_denied(self):
        r={"evaluation_id":"x","artifact_kind":"vector","candidate_ref":"c","evidence_refs":["e"],"metrics":[{"name":"m","value":1,"threshold":1,"comparison":"gte"}],"policy_outcome":"ALLOW","deterministic":True,"network_access":True,"result":"PASS","reason_codes":[],"spec_hash":"sha256:"+"a"*64}
        self.assertEqual("DENY", m.evaluate(r))

if __name__=="__main__": unittest.main()
