from __future__ import annotations
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MODULE_PATH=ROOT/"tools/validators/runtime/validate_graph_runtime_compatibility_matrix.py"
SPEC=importlib.util.spec_from_file_location("validate_graph_runtime_compatibility_matrix",MODULE_PATH)
assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name]=MODULE
SPEC.loader.exec_module(MODULE)

class GraphRuntimeCompatibilityMatrixTests(unittest.TestCase):
    def test_control_plane_projection_passes(self) -> None:
        result=MODULE.validate(ROOT/"control_plane/graph_runtime_compatibility_matrix.json")
        self.assertTrue(result.ok, result.findings)

    def test_fixture_manifest_matches_exact_reason_codes(self) -> None:
        root=ROOT/"fixtures/contracts/v1/runtime/graph_runtime_compatibility_matrix"
        manifest=json.loads((root/"expected_findings_manifest.json").read_text(encoding="utf-8"))
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result=MODULE.validate(root/case["input"])
                self.assertEqual(case["expected_outcome"],result.outcome)
                self.assertEqual(case["expected_findings"],sorted({finding.code for finding in result.findings}))

    def test_supported_rows_require_bound_evidence(self) -> None:
        path=ROOT/"fixtures/contracts/v1/runtime/graph_runtime_compatibility_matrix/semantic_invalid/supported_without_evidence.json"
        codes={finding.code for finding in MODULE.validate(path).findings}
        self.assertIn("SUPPORTED_EVIDENCE_INCOMPLETE",codes)

    def test_clustered_support_requires_passed_rehearsal(self) -> None:
        path=ROOT/"fixtures/contracts/v1/runtime/graph_runtime_compatibility_matrix/semantic_invalid/clustered_without_rehearsal.json"
        codes={finding.code for finding in MODULE.validate(path).findings}
        self.assertIn("SUPPORTED_CLUSTER_REHEARSAL_INCOMPLETE",codes)

    def test_fixture_runner_is_deterministic(self) -> None:
        self.assertEqual(0,MODULE.run_fixtures())
        self.assertEqual(0,MODULE.run_fixtures())

if __name__=="__main__":
    unittest.main()
