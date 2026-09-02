from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/release/validate_signed_bundle_timestamp_evidence.py"
SCHEMA = ROOT / "schemas/contracts/v1/release/signed_bundle_timestamp_evidence.schema.json"
CASES = ROOT / "fixtures/contracts/v1/release/signed_bundle_timestamp_evidence/cases.json"

SPEC = importlib.util.spec_from_file_location("validate_timestamp_evidence", VALIDATOR)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SignedBundleTimestampEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = json.loads(CASES.read_text(encoding="utf-8"))

    def test_schema_is_closed_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        governance = schema["properties"]["governance"]["properties"]
        self.assertFalse(governance["cryptographic_verification_performed"]["const"])
        self.assertFalse(governance["release_authorized"]["const"])

    def test_exact_fixture_outcomes_and_findings(self) -> None:
        cases = self.corpus["cases"]
        self.assertEqual(14, len(cases))
        self.assertEqual(6, sum(not case["expected"]["findings"] for case in cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                result = MODULE.validate_candidate(MODULE.materialize_case(self.corpus, case))
                self.assertEqual(case["expected"]["outcome"], result.outcome)
                self.assertEqual(case["expected"]["findings"], sorted({item.code for item in result.findings}))

    def test_finite_assessment_mapping(self) -> None:
        self.assertEqual(("PASS", ["TIMESTAMP_EVIDENCE_PRESENT"]), MODULE.expected_assessment("REQUIRED", "PRESENT"))
        self.assertEqual(("DENY", ["TIMESTAMP_EVIDENCE_REQUIRED_MISSING"]), MODULE.expected_assessment("REQUIRED", "ABSENT"))
        self.assertEqual(("ABSTAIN", ["TIMESTAMP_EVIDENCE_OPTIONAL_ABSENT"]), MODULE.expected_assessment("OPTIONAL", "ABSENT"))
        self.assertEqual(("ABSTAIN", ["TIMESTAMP_REQUIREMENT_UNKNOWN"]), MODULE.expected_assessment("UNKNOWN", "ABSENT"))
        self.assertEqual(("ERROR", ["TIMESTAMP_EVIDENCE_UNREADABLE"]), MODULE.expected_assessment("OPTIONAL", "UNREADABLE"))

    def test_public_identity_replays(self) -> None:
        candidate = MODULE.materialize_case(self.corpus, self.corpus["cases"][0])
        spec_hash, evidence_id = MODULE.canonical_identity(candidate)
        self.assertEqual(candidate["spec_hash"], spec_hash)
        self.assertEqual(candidate["evidence_id"], evidence_id)

    def test_fixture_cli_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(14, len(first.stdout.splitlines()))

    def test_duplicate_keys_nonfinite_missing_and_symlink_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            nonfinite = root / "nonfinite.json"
            target = root / "target.json"
            link = root / "link.json"
            duplicate.write_text('{"object_type":"a","object_type":"b"}', encoding="utf-8")
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            target.write_text("{}", encoding="utf-8")
            self.assertEqual(["JSON_DUPLICATE_KEY"], [item.code for item in MODULE.validate_record(duplicate).findings])
            self.assertEqual(["JSON_NONFINITE_NUMBER"], [item.code for item in MODULE.validate_record(nonfinite).findings])
            try:
                link.symlink_to(target)
            except OSError:
                self.skipTest("symlinks unavailable")
            self.assertEqual(["INPUT_SYMLINK_DENIED"], [item.code for item in MODULE.validate_record(link).findings])
        self.assertEqual(["INPUT_NOT_FILE"], [item.code for item in MODULE.validate_record(ROOT / "missing-timestamp-evidence.json").findings])

    def test_validator_has_no_network_crypto_or_effect_surface(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        for forbidden in (
            "import requests",
            "import urllib",
            "import socket",
            "import subprocess",
            "subprocess.run",
            "os.system",
            "cosign ",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
