from __future__ import annotations
import importlib.util, json, sys, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
MODULE_PATH=ROOT/"tools/validators/map/tiles3d_stac_item_adapter/build_tiles3d_stac_item.py"
SPEC=importlib.util.spec_from_file_location("build_tiles3d_stac_item",MODULE_PATH)
assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=MODULE; SPEC.loader.exec_module(MODULE)
FIX=ROOT/"fixtures/map/tiles3d_stac_item_adapter"

class Tiles3DStacItemAdapterTests(unittest.TestCase):
    def test_valid_fixture_matches_expected_item(self)->None:
        result=MODULE.build(FIX/"valid/manifest.json",FIX/"valid/request.json",FIX/"package")
        self.assertTrue(result.ok,result.findings)
        expected=json.loads((FIX/"expected/valid_item.json").read_text(encoding="utf-8"))
        self.assertEqual(expected,result.item)
        self.assertEqual("unreleased",result.item["properties"]["kfm:release_state"])
        self.assertEqual(["metadata","3d-tiles"],result.item["assets"]["tileset-0002"]["roles"])

    def test_all_assets_bind_local_bytes(self)->None:
        item=MODULE.build(FIX/"valid/manifest.json",FIX/"valid/request.json",FIX/"package").item
        self.assertIsNotNone(item)
        for asset in item["assets"].values():
            path=FIX/"package"/asset["href"]
            self.assertEqual(asset["file:size"],path.stat().st_size)
            import hashlib
            self.assertEqual(asset["file:checksum"],"sha256:"+hashlib.sha256(path.read_bytes()).hexdigest())

    def test_fixture_reason_codes(self)->None:
        cases=json.loads((FIX/"expected_findings_manifest.json").read_text(encoding="utf-8"))["cases"]
        for case in cases:
            with self.subTest(case=case["case_id"]):
                result=MODULE.build(FIX/case["manifest"],FIX/case["request"],FIX/case["asset_root"])
                self.assertEqual(case["expected_outcome"],result.outcome)
                self.assertEqual(case["expected_findings"],sorted({f.code for f in result.findings}))

    def test_fixture_runner_is_deterministic(self)->None:
        self.assertEqual(0,MODULE.run_fixtures())
        self.assertEqual(0,MODULE.run_fixtures())

if __name__=="__main__": unittest.main()
