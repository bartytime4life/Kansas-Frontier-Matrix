from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[2]
VALIDATOR=ROOT/"tools/validators/ui/validate_map_context_envelope.py"
SCHEMA=ROOT/"schemas/contracts/v1/ui/map_context_envelope.schema.json"
CASES=ROOT/"fixtures/ui/map_context_envelope/cases.json"
SPEC=importlib.util.spec_from_file_location("validate_map_context_envelope",VALIDATOR); assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=MODULE; SPEC.loader.exec_module(MODULE)
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.document=json.loads(CASES.read_text()); cls.cases=cls.document["cases"]
    def by_id(self,name): return next(c for c in self.cases if c["case_id"]==name)
    def record(self,case): return MODULE._case_record(self.document,case)
    def test_schema_closed_and_bound(self):
        s=json.loads(SCHEMA.read_text()); Draft202012Validator.check_schema(s); self.assertFalse(s["additionalProperties"]); self.assertEqual(s["x-kfm"]["contract_doc"],"contracts/ui/map_context_envelope.md")
    def test_valid_records_pass(self):
        for c in self.cases:
            if c["case_kind"]=="VALID": self.assertTrue(MODULE.validate_value(self.record(c)).ok,c["case_id"])
    def test_cases_exact(self):
        self.assertEqual(len(self.cases),16)
        for c in self.cases:            r=MODULE.validate_value(self.record(c)); self.assertEqual("PASS" if r.ok else "FAIL",c["expected_outcome"],c["case_id"]); self.assertEqual(sorted({x.code for x in r.findings}),c["expected_findings"],c["case_id"])
    def test_schema_and_semantic_negative_boundary(self):
        s=json.loads(SCHEMA.read_text()); v=Draft202012Validator(s,format_checker=FormatChecker())
        schema_neg=[c for c in self.cases if c["case_kind"]=="SCHEMA_NEGATIVE"]; semantic=[c for c in self.cases if c["case_kind"]=="SEMANTIC_NEGATIVE"]; self.assertEqual((len(schema_neg),len(semantic)),(4,10))
        for c in schema_neg: self.assertTrue(list(v.iter_errors(self.record(c))),c["case_id"])
        for c in semantic: self.assertFalse(list(v.iter_errors(self.record(c))),c["case_id"])
    def test_identity_reproduces(self):
        obj=self.record(self.by_id("valid-view")); self.assertEqual(MODULE._identity_hash(obj),obj["spec_hash"]); self.assertEqual(MODULE._identity_id(obj),obj["envelope_id"])
    def test_renderer_specific_state_rejected(self): self.assertEqual({x.code for x in MODULE.validate_value(self.record(self.by_id("invalid-renderer-specific-field"))).findings},{"SCHEMA_INVALID"})
    def test_internal_reference_denied_without_echo(self):
        c=self.by_id("semantic-invalid-internal-ref"); r=MODULE.validate_value(self.record(c)); report=json.dumps([]); report=json.dumps([{"code":x.code,"field":x.field} for x in r.findings]); self.assertIn("INTERNAL_REFERENCE_DENIED",report); self.assertNotIn("internal:release:soil",report)
    def test_duplicate_and_nonfinite_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            a=Path(d)/"a.json"; a.write_text('{"a":1,"a":2}'); b=Path(d)/"b.json"; b.write_text('{"a":NaN}')
            self.assertEqual({x.code for x in MODULE.validate(a).findings},{"JSON_DUPLICATE_KEY"}); self.assertEqual({x.code for x in MODULE.validate(b).findings},{"JSON_NONFINITE_NUMBER"})
    def test_no_network_replay_and_cli(self):
        with mock.patch.object(socket,"create_connection",side_effect=AssertionError("network")),mock.patch.object(socket,"socket",side_effect=AssertionError("network")):
            a=MODULE.fixture_suite(); b=MODULE.fixture_suite(); self.assertEqual(a,b); self.assertTrue(a[0])
        c=subprocess.run([sys.executable,str(VALIDATOR),"--fixtures"],cwd=ROOT,capture_output=True,text=True,check=False); self.assertEqual(c.returncode,0,c.stdout+c.stderr); self.assertEqual(len(c.stdout.splitlines()),16); self.assertNotIn('"suite_match":false',c.stdout)
if __name__=="__main__": unittest.main()
