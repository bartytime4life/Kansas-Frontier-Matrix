from __future__ import annotations
import importlib.util,json,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[3]
VALIDATOR_PATH=ROOT/"tools/validators/governance/validate_proof_session_handoff.py"
spec=importlib.util.spec_from_file_location("proof_session_handoff",VALIDATOR_PATH);assert spec and spec.loader
validator=importlib.util.module_from_spec(spec);sys.modules[spec.name]=validator;spec.loader.exec_module(validator)
class ProofSessionHandoffTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.manifest=validator.load_fixtures()
 def test_schema_self_check(self):
  schema=json.loads(validator.SCHEMA_PATH.read_text(encoding="utf-8"));validator.Draft202012Validator.check_schema(schema)
 def test_exact_fixture_matrix(self):
  self.assertGreaterEqual(len(self.manifest["cases"]),17)
  for entry in self.manifest["cases"]:
   with self.subTest(case=entry["name"]):
    result=validator.validate_candidate(validator.materialize_fixture_case(self.manifest,entry));self.assertEqual(entry["expected"],{"outcome":result.outcome,"codes":result.codes})
 def test_positive_handoff_remains_review_required_and_non_authoritative(self):
  candidate=validator.materialize_fixture_case(self.manifest,self.manifest["cases"][0]);result=validator.validate_candidate(candidate)
  self.assertEqual("PASS",result.outcome);self.assertEqual("REVIEW_REQUIRED",result.assessment_state);self.assertTrue(candidate["handoff"]["review_required"]);self.assertTrue(all(x is False for x in candidate["session_claims"].values()));self.assertTrue(all(x is False for x in candidate["authority_claims"].values()))
 def test_identity_is_deterministic(self):
  first=validator.materialize_fixture_case(self.manifest,self.manifest["cases"][0]);second=validator.materialize_fixture_case(self.manifest,self.manifest["cases"][0]);self.assertEqual(first["profile_spec_hash"],second["profile_spec_hash"]);self.assertEqual(first["session_id"],second["session_id"])
 def test_duplicate_nonfinite_symlink_and_oversize_are_bounded_errors(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);duplicate=root/"duplicate.json";duplicate.write_text('{"a":1,"a":2}\n');self.assertEqual("JSON_DUPLICATE_KEY",validator.load_json_object(duplicate)[1][0].code)
   nonfinite=root/"nonfinite.json";nonfinite.write_text('{"a":NaN}\n');self.assertEqual("JSON_NONFINITE_NUMBER",validator.load_json_object(nonfinite)[1][0].code)
   target=root/"target.json";target.write_text("{}\n");link=root/"link.json";link.symlink_to(target);self.assertEqual("INPUT_SYMLINK_DENIED",validator.load_json_object(link)[1][0].code)
   large=root/"large.json";large.write_bytes(b"{"+b" "*validator.MAX_FILE_BYTES+b"}");self.assertEqual("FILE_TOO_LARGE",validator.load_json_object(large)[1][0].code)
 def test_validation_does_not_open_network(self):
  candidate=validator.materialize_fixture_case(self.manifest,self.manifest["cases"][0])
  with patch("socket.socket",side_effect=AssertionError("network denied")):result=validator.validate_candidate(candidate)
  self.assertEqual("PASS",result.outcome)
 def test_serialization_does_not_echo_candidate_values(self):
  candidate=validator.materialize_fixture_case(self.manifest,self.manifest["cases"][4]);result=validator.validate_candidate(candidate);output=validator._serialize(result);self.assertNotIn("20053",output);self.assertIn("SYNTHETIC_SUPPORT_FOR_REAL_SCOPE_DENIED",output)
 def test_cli_fixture_replay_is_deterministic(self):
  command=[sys.executable,str(VALIDATOR_PATH),"--fixtures"];first=subprocess.run(command,cwd=ROOT,capture_output=True,text=True);second=subprocess.run(command,cwd=ROOT,capture_output=True,text=True);self.assertEqual(0,first.returncode,first.stdout+first.stderr);self.assertEqual(first.stdout,second.stdout)
if __name__=="__main__":unittest.main()
