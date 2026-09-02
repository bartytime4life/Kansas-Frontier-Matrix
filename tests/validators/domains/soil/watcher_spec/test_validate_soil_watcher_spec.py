from __future__ import annotations
import importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
MODULE_PATH=ROOT/"tools/validators/domains/soil/watcher_spec/validate_soil_watcher_spec.py"
SPEC=importlib.util.spec_from_file_location("validate_soil_watcher_spec",MODULE_PATH);assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC);sys.modules[SPEC.name]=MODULE;SPEC.loader.exec_module(MODULE)
FIX=ROOT/"fixtures/domains/soil/watcher_spec"
class SoilWatcherSpecTests(unittest.TestCase):
    def test_repository_spec_passes(self)->None:
        result=MODULE.validate(ROOT/"pipeline_specs/watchers/soil_ssurgo_gnatsgo.json");self.assertTrue(result.ok,result.findings)
    def test_fixture_reason_codes(self)->None:
        cases=json.loads((FIX/"expected_findings_manifest.json").read_text(encoding="utf-8"))["cases"]
        for case in cases:
            with self.subTest(case=case["case_id"]):
                result=MODULE.validate(FIX/case["input"]);self.assertEqual(case["expected_outcome"],result.outcome);self.assertEqual(case["expected_findings"],sorted({f.code for f in result.findings}))
    def test_source_roles_do_not_collapse(self)->None:
        value=json.loads((ROOT/"pipeline_specs/watchers/soil_ssurgo_gnatsgo.json").read_text(encoding="utf-8"));roles={item["source_family"]:item["support_type"] for item in value["source_scope"]}
        self.assertEqual("AUTHORITATIVE_STATIC_SOIL_SURVEY",roles["SSURGO"]);self.assertEqual("GRIDDED_DERIVATIVE_SOIL",roles["GNATSGO"]);self.assertNotEqual(roles["SSURGO"],roles["GNATSGO"])
    def test_outputs_are_non_publishing(self)->None:
        value=json.loads((ROOT/"pipeline_specs/watchers/soil_ssurgo_gnatsgo.json").read_text(encoding="utf-8"));self.assertEqual({"WORK","QUARANTINE"},{item["target_zone"] for item in value["outputs"]});self.assertTrue(all(flag is False for flag in value["governance"].values()))
    def test_fixture_runner_is_deterministic(self)->None:
        self.assertEqual(0,MODULE.run_fixtures());self.assertEqual(0,MODULE.run_fixtures())
if __name__=="__main__":unittest.main()
