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
VALIDATOR_PATH = REPO_ROOT / "tools/validators/map/validate_map_release_manifest.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/map_release_manifest.schema.json"
CONTRACT_PATH = REPO_ROOT / "contracts/release/map_release_manifest.md"
COMPAT_PATH = REPO_ROOT / "contracts/map/map_release_manifest/README.md"
FAMILY_README = REPO_ROOT / "schemas/contracts/v1/map/README.md"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/map/map_release_manifest/cases.json"

spec = importlib.util.spec_from_file_location("validate_map_release_manifest", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

CASES = json.loads(CASES_PATH.read_text(encoding="utf-8"))
VALID_CASES = {case["name"]: case for case in CASES["valid_cases"]}
INVALID_CASES = {case["name"]: case for case in CASES["invalid_cases"]}


class MapReleaseManifestTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))

    def test_valid_cases_cover_release_lifecycle(self) -> None:
        expected = {
            "candidate_pending_review": "CANDIDATE",
            "held_rights_unknown": "HELD",
            "published_generalized": "PUBLISHED",
            "published_public": "PUBLISHED",
            "rolled_back": "ROLLED_BACK",
            "superseded": "SUPERSEDED",
            "withdrawn": "WITHDRAWN",
        }
        self.assertEqual(set(expected), set(VALID_CASES))
        for name, state in expected.items():
            with self.subTest(name=name):
                result = validator.validate_payload(VALID_CASES[name]["payload"])
                self.assertTrue(result.ok, result.findings)
                self.assertEqual(state, result.release_state)

    def test_invalid_cases_have_exact_reviewed_findings(self) -> None:
        self.assertEqual(11, len(INVALID_CASES))
        for name, case in INVALID_CASES.items():
            with self.subTest(name=name):
                result = validator.validate_payload(case["payload"])
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(case["expected_codes"]),
                    sorted({item.code for item in result.findings}),
                )

    def test_identity_is_stable_across_mapping_key_order(self) -> None:
        payload = VALID_CASES["published_public"]["payload"]
        reordered = {key: payload[key] for key in reversed(list(payload))}
        self.assertEqual(payload["spec_hash"], validator.canonical_spec_hash(reordered))
        self.assertEqual(payload["map_release_id"], validator.expected_map_release_id(reordered))

    def test_published_case_has_catalog_evidence_review_attestation_and_rollback_closure(self) -> None:
        payload = VALID_CASES["published_public"]["payload"]
        for name in ("stac", "dcat", "prov"):
            self.assertTrue(payload["catalog_refs"][name])
        for name in (
            "artifact_manifests",
            "layer_manifest_refs",
            "style_manifest_refs",
            "evidence_refs",
            "policy_decision_refs",
            "rights_refs",
            "sensitivity_refs",
            "review_refs",
            "attestation_refs",
        ):
            self.assertTrue(payload[name])
        self.assertTrue(payload["rollback"]["verified"])
        self.assertIsNotNone(payload["rollback"]["rollback_target_ref"])
        self.assertIsNotNone(payload["rollback"]["rollback_card_ref"])

    def test_pmtiles_and_cog_require_range_and_cors_when_published(self) -> None:
        payload = VALID_CASES["published_public"]["payload"]
        ranged = [
            item
            for item in payload["artifact_manifests"]
            if item["artifact_type"] in {"PMTILES", "COG"}
        ]
        self.assertTrue(ranged)
        self.assertTrue(all(item["range_supported"] and item["cors_allowed"] for item in ranged))

    def test_generalized_case_carries_redaction_receipt(self) -> None:
        payload = VALID_CASES["published_generalized"]["payload"]
        self.assertEqual("GENERALIZED", payload["public_boundary"]["geometry_posture"])
        self.assertTrue(payload["redaction_receipt_refs"])

    def test_public_boundary_denies_internal_and_unreleased_paths(self) -> None:
        boundary = VALID_CASES["published_public"]["payload"]["public_boundary"]
        denied = (
            "raw_path_exposed",
            "work_path_exposed",
            "quarantine_path_exposed",
            "canonical_store_exposed",
            "unreleased_fetch_allowed",
            "direct_model_output_exposed",
        )
        self.assertTrue(all(boundary[key] is False for key in denied))

    def test_unknown_member_is_denied_by_schema(self) -> None:
        payload = dict(VALID_CASES["published_public"]["payload"])
        payload["unexpected"] = True
        result = validator.validate_payload(payload)
        self.assertFalse(result.ok)
        self.assertIn("SCHEMA_INVALID", {item.code for item in result.findings})

    def test_duplicate_key_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"v1","schema_version":"v2"}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("JSON_DUPLICATE_KEY", "/"),), result.findings)

    def test_nonfinite_number_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("JSON_NONFINITE_NUMBER", "/"),), result.findings)

    def test_symlink_input_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            result = validator.validate_file(link)
        self.assertTrue(result.operational_error)
        self.assertEqual((validator.Finding("INPUT_SYMLINK_DENIED", "/"),), result.findings)

    def test_validator_imports_no_network_client(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = (
            "import requests",
            "import httpx",
            "import aiohttp",
            "import socket",
            "from urllib",
        )
        self.assertFalse(any(token in source for token in forbidden))

    def test_docs_bind_one_semantic_contract_to_existing_map_schema(self) -> None:
        contract = CONTRACT_PATH.read_text(encoding="utf-8")
        compatibility = COMPAT_PATH.read_text(encoding="utf-8")
        family = FAMILY_README.read_text(encoding="utf-8")
        self.assertIn("schemas/contracts/v1/map/map_release_manifest.schema.json", contract)
        self.assertIn("canonical semantic contract", compatibility)
        self.assertIn("machine-backed fixture profile", family)
        self.assertNotIn("Schema: missing", contract)

    def test_cli_passes_valid_packet(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "published.json"
            path.write_text(
                json.dumps(VALID_CASES["published_public"]["payload"], sort_keys=True),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("PASS", payload["outcome"])
        self.assertEqual("PUBLISHED", payload["release_state"])
        self.assertEqual([], payload["findings"])
        self.assertEqual({False}, set(payload["authority"].values()))

    def test_cli_fails_contradictory_packet(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(
                json.dumps(INVALID_CASES["published_missing_rollback"]["payload"], sort_keys=True),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertEqual("FAIL", payload["outcome"])
        self.assertTrue(
            any(
                item["code"] == "PUBLISHED_ROLLBACK_CLOSURE_REQUIRED"
                for item in payload["findings"]
            )
        )

    def test_fixture_profile_cli_passes(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertEqual(18, len([line for line in completed.stdout.splitlines() if line.strip()]))


if __name__ == "__main__":
    unittest.main()
