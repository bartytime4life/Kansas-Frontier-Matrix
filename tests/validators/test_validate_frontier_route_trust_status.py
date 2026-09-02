from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/domains/roads-rail-trade/validate_frontier_route_trust_status.py"
SPEC = importlib.util.spec_from_file_location("validate_frontier_route_trust_status", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

class FrontierRouteTrustStatusValidatorTests(unittest.TestCase):
    def test_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(0, MODULE.run_fixtures())

    def test_schema_is_closed_and_profile_is_pinned(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("kfm.roads-rail-trade.frontier-route-trust-status.v1", schema["properties"]["profile"]["const"])
        self.assertEqual("contracts/domains/roads-rail-trade/frontier_route_trust_status.md", schema["x-kfm"]["contract_doc"])
        self.assertFalse(schema["$defs"]["feature_trust"]["additionalProperties"])

    def test_duplicate_feature_identity_is_rejected(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/duplicate-kfm-id.json")
        self.assertIn("DUPLICATE_FEATURE_ID", {finding.code for finding in findings})

    def test_public_visibility_must_match_disposition(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/visibility-mismatch.json")
        self.assertIn("VISIBILITY_DECISION_MISMATCH", {finding.code for finding in findings})

    def test_release_binding_is_fail_closed(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/release-mismatch.json")
        self.assertIn("RELEASE_BINDING_MISMATCH", {finding.code for finding in findings})

    def test_collection_decision_is_derived(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/collection-decision-mismatch.json")
        self.assertIn("COLLECTION_DECISION_MISMATCH", {finding.code for finding in findings})

    def test_public_projection_cannot_carry_withheld_rows(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/public-projection-leak.json")
        self.assertIn("PUBLIC_PROJECTION_LEAK", {finding.code for finding in findings})

    def test_raw_geometry_is_outside_projection_contract(self) -> None:
        findings = MODULE.validate_payload(MODULE.FIXTURES_ROOT / "invalid/raw-geometry-leak.json")
        self.assertIn("SCHEMA_INVALID", {finding.code for finding in findings})

    def test_validator_is_deterministic_and_no_network(self) -> None:
        path = MODULE.FIXTURES_ROOT / "valid/mixed-status.json"
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "getaddrinfo", side_effect=AssertionError("dns denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("socket denied")):
            self.assertEqual(MODULE.validate_payload(path), MODULE.validate_payload(path))

    def test_cli_fixture_mode(self) -> None:
        completed = subprocess.run([sys.executable, str(VALIDATOR_PATH), "--fixtures"], cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        self.assertIn("FRONTIER_ROUTE_TRUST_FIXTURES_VALID", completed.stdout)

    def test_ui_adapter_preserves_public_steward_boundary(self) -> None:
        source = (REPO_ROOT / "apps/explorer-web/src/features/domains/roads_rail_trade/layers.ts").read_text(encoding="utf-8")
        self.assertIn("PUBLIC_PAYLOAD_REQUIRED", source)
        self.assertIn("visible_in_public_catalog", source)
        self.assertIn("buildTrustOverlay", source)
        self.assertNotIn("fetch(", source)

if __name__ == "__main__":
    unittest.main()
