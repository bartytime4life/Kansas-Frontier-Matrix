from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[2]
VP=ROOT/"tools/validators/data/validate_stac_attestation_hook.py"
SPEC=importlib.util.spec_from_file_location("stac_hook",VP); assert SPEC and SPEC.loader
M=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=M; SPEC.loader.exec_module(M)

class Tests(unittest.TestCase):
    def suite(self): return json.loads(M.CASES.read_text(encoding="utf-8"))
    def test_schema_is_closed_and_inactive(self):
        schema=json.loads(M.SCHEMA.read_text()); Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"]); self.assertEqual(schema["x-kfm"]["status"],"PROPOSED_INACTIVE")
    def test_exact_fixture_polarity(self):
        suite=self.suite(); self.assertEqual(len(suite["cases"]),14)
        for case in suite["cases"]:
            with self.subTest(case=case["case_id"]):
                result=M.validate_payload(M.mutate(suite["base"],case["mutation"]))
                outcome="PASS" if result.ok else ("ERROR" if result.error else "FAIL")
                self.assertEqual(outcome,case["expected_outcome"])
                self.assertEqual(sorted({f.code for f in result.findings}),case["expected_codes"])
    def test_required_state_and_explicit_relation(self):
        base=self.suite()["base"]
        self.assertEqual({f.code for f in M.validate_payload(M.mutate(base,"MISSING_HOOK")).findings},{"ATTESTATION_LINK_REQUIRED"})
        self.assertEqual({f.code for f in M.validate_payload(M.mutate(base,"PROV_ONLY")).findings},{"ATTESTATION_LINK_REQUIRED"})
    def test_unreleased_may_omit_hook(self):
        self.assertTrue(M.validate_payload(M.mutate(self.suite()["base"],"UNRELEASED_NO_HOOK")).ok)
    def test_identity_reproduces(self):
        value=M.mutate(self.suite()["base"],"NONE")
        self.assertEqual(value["spec_hash"],M.compute_record_spec_hash(value))
        self.assertEqual(value["projection_id"],M.compute_projection_id(value))
    def test_duplicate_keys_and_nonfinite_fail_closed(self):
        for raw,code in [('{"a":1,"a":2}',"JSON_DUPLICATE_KEY"),('{"a":NaN}',"JSON_NONFINITE_NUMBER")]:
            with tempfile.TemporaryDirectory() as directory:
                path=Path(directory)/"x.json"; path.write_text(raw)
                self.assertEqual({f.code for f in M.validate_record(path).findings},{code})
    def test_missing_file_is_error(self):
        result=M.validate_record(ROOT/"missing-stac-hook.json"); self.assertTrue(result.error)
    def test_diagnostics_do_not_echo_values(self):
        value=M.mutate(self.suite()["base"],"NONE"); marker="UNTRUSTED_DO_NOT_ECHO"
        value["stac_item_id"]=marker; value["unexpected"]=marker
        report=M.serialize("candidate.json",M.validate_payload(value))
        self.assertNotIn(marker,report); self.assertIn("SCHEMA_INVALID",report)
    def test_suite_is_no_network_and_cli_deterministic(self):
        with mock.patch.object(socket,"create_connection",side_effect=AssertionError("network denied")), mock.patch.object(socket,"socket",side_effect=AssertionError("network denied")):
            ok,first=M.fixture_suite(); ok2,second=M.fixture_suite()
        self.assertTrue(ok and ok2); self.assertEqual(first,second)
        a=subprocess.run([sys.executable,str(VP),"--fixtures"],cwd=ROOT,capture_output=True,text=True)
        b=subprocess.run([sys.executable,str(VP),"--fixtures"],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(a.returncode,0,a.stdout+a.stderr); self.assertEqual(a.stdout,b.stdout); self.assertEqual(len(a.stdout.splitlines()),14)
    def test_validation_does_not_mutate_input(self):
        value=M.mutate(self.suite()["base"],"NONE"); before=json.dumps(value,sort_keys=True)
        M.validate_payload(value); self.assertEqual(json.dumps(value,sort_keys=True),before)

if __name__=="__main__": unittest.main()
