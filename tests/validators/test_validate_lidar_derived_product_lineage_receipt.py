from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools/validators/validate_lidar_derived_product_lineage_receipt.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt/cases.json"
SCHEMA = REPO_ROOT / "schemas/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt.schema.json"

spec = importlib.util.spec_from_file_location("lidar_lineage_validator", VALIDATOR)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class LidarDerivedProductLineageReceiptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURES.read_text(encoding="utf-8"))
        base = self.fixture["base_document"]
        self.by_id = {
            case["case_id"]: {**case, "document": module.materialize_case(base, case)}
            for case in self.fixture["cases"]
        }

    def test_schema_is_closed_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("PROPOSED_INACTIVE", schema["x-kfm"]["status"])

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = module.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(12, len(report["cases"]))
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_valid_copc_dem_and_ept_terrain_chains_pass(self) -> None:
        expected = {
            "valid-laz-copc-dem": ["LAZ", "COPC", "DEM"],
            "valid-laz-ept-terrain": ["LAZ", "EPT", "TERRAIN"],
        }
        for case_id, kinds in expected.items():
            document = self.by_id[case_id]["document"]
            result = module.validate_document(document)
            self.assertEqual(("PASS", "LINEAGE_RECORDED", ()), (result.status, result.lineage_outcome, result.findings))
            self.assertEqual(kinds, [item["product_kind"] for item in document["products"]])
            self.assertTrue(document["lineage_summary"]["all_nodes_have_laz_ancestor"])

    def test_source_and_product_roles_fail_closed(self) -> None:
        for case_id in ("invalid-dem-observed-role", "invalid-carrier-source-capture-role"):
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("DENY", result.status)
            self.assertIn("SOURCE_ROLE_MISMATCH", {finding.code for finding in result.findings})

    def test_topology_ancestry_and_transform_fail_closed(self) -> None:
        expected = {
            "invalid-derived-transform-missing": "DERIVED_TRANSFORM_REQUIRED",
            "invalid-cycle-without-laz-ancestry": "LINEAGE_NOT_TOPOLOGICAL",
            "invalid-parent-unknown": "LINEAGE_PARENT_UNKNOWN",
        }
        for case_id, code in expected.items():
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("DENY", result.status)
            self.assertIn(code, {finding.code for finding in result.findings})

    def test_acquisition_spatial_reference_and_order_fail_closed(self) -> None:
        expected = {
            "invalid-acquisition-window-change": "ACQUISITION_WINDOW_MISMATCH",
            "invalid-vertical-units-change": "SPATIAL_REFERENCE_MISMATCH",
            "invalid-parent-order": "ORDER_OR_DUPLICATE_INVALID",
        }
        for case_id, code in expected.items():
            result = module.validate_document(self.by_id[case_id]["document"])
            self.assertEqual("DENY", result.status)
            self.assertIn(code, {finding.code for finding in result.findings})

    def test_authority_and_identity_tamper_fail_closed(self) -> None:
        authority = module.validate_document(self.by_id["invalid-authority-overclaim"]["document"])
        identity = module.validate_document(self.by_id["invalid-spec-hash"]["document"])
        self.assertEqual({"SCHEMA_INVALID"}, {finding.code for finding in authority.findings})
        self.assertEqual({"LINEAGE_SPEC_HASH_MISMATCH"}, {finding.code for finding in identity.findings})

    def test_symlink_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture.json"
            target.write_text(json.dumps(self.by_id["valid-laz-copc-dem"]["document"]), encoding="utf-8")
            link = Path(directory) / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = module.validate_file(link)
            self.assertEqual("ERROR", result.status)
            self.assertEqual({"LINEAGE_JSON_INVALID"}, {finding.code for finding in result.findings})

    def test_diagnostics_do_not_echo_untrusted_values(self) -> None:
        document = self.by_id["valid-laz-copc-dem"]["document"]
        document["untrusted_negative_canary"] = "UNTRUSTED_VALUE_DO_NOT_ECHO"
        result = module.validate_document(document)
        report = module._serialize(result)
        self.assertIn("SCHEMA_INVALID", report)
        self.assertNotIn("UNTRUSTED_VALUE_DO_NOT_ECHO", report)

    def test_cli_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR), "--fixtures"]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)
        self.assertTrue(json.loads(first.stdout)["ok"])

    def test_validator_has_no_network_or_write_surface(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        for token in (
            "import requests",
            "import urllib",
            "import socket",
            "import subprocess",
            "from subprocess",
            ".write_text(",
            ".write_bytes(",
            "os.remove(",
            "os.replace(",
            "open(",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
