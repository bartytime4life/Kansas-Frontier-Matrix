from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.runtime import validate_verified_rendering_resource_envelope as validator

ROOT = Path(__file__).resolve().parents[2]


class VerifiedRenderingResourceEnvelopeTests(unittest.TestCase):
    def test_schema_is_valid_and_closed(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("PROPOSED", schema["x-kfm"]["status"])

    def test_exact_fixture_cases(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_status"], result.status)
                self.assertEqual(case["expected_rendering_state"], result.rendering_state)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_and_states_are_non_vacuous(self) -> None:
        cases = validator.load_fixtures()["cases"]
        statuses = Counter(case["expected_status"] for case in cases)
        states = {case["expected_rendering_state"] for case in cases if case["expected_status"] == "PASS"}
        self.assertGreaterEqual(statuses["PASS"], 10)
        self.assertGreaterEqual(statuses["DENY"], 6)
        self.assertEqual({"READY_FOR_SEPARATE_EXECUTION", "DEGRADED", "BLOCKED", "CANCELLED", "ERROR"}, states)

    def test_pass_never_claims_verification_decode_or_render(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            if case["expected_status"] != "PASS":
                continue
            document = validator.materialize_case(manifest, case)
            self.assertEqual(validator.expected_rendering_assessment(document), document["rendering_assessment"])
            self.assertFalse(document["rendering_assessment"]["render_allowed"])
            self.assertFalse(document["rendering_assessment"]["cryptographic_verification_performed"])
            self.assertFalse(document["governance"]["artifact_bytes_read"])
            self.assertFalse(document["governance"]["decode_performed"])
            self.assertFalse(document["governance"]["render_performed"])

    def test_identity_tamper_is_denied(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        document["release_binding"]["artifact_ref"] = "kfm:artifact:tampered"
        result = validator.validate_payload(document)
        self.assertEqual("DENY", result.status)
        self.assertEqual("RENDER_ENVELOPE_SPEC_HASH_MISMATCH", result.findings[0].code)

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        marker = "RENDER_ENVELOPE_ECHO_SENTINEL"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text('{"object_type":"%s","object_type":"duplicate"}' % marker, encoding="utf-8")
            completed = subprocess.run([sys.executable, str(Path(validator.__file__)), str(path)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, completed.returncode)
        self.assertIn("JSON_DUPLICATE_KEY", completed.stdout)
        self.assertNotIn(marker, completed.stdout + completed.stderr)

    def test_symlink_and_oversized_input_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            linked = subprocess.run([sys.executable, str(Path(validator.__file__)), str(link)], cwd=ROOT, capture_output=True, text=True, check=False)
            large = Path(directory) / "large.json"
            large.write_bytes(b" " * (validator.MAX_JSON_BYTES + 1))
            oversized = subprocess.run([sys.executable, str(Path(validator.__file__)), str(large)], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertIn("JSON_INPUT_SYMLINK_DENIED", linked.stdout)
        self.assertIn("JSON_INPUT_TOO_LARGE", oversized.stdout)

    def test_fixture_cli(self) -> None:
        completed = subprocess.run([sys.executable, str(Path(validator.__file__)), "--fixtures"], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn('"suite_match":true', completed.stdout)

    def test_validator_has_no_network_crypto_decoder_or_renderer_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "httpx", "aiohttp", "boto3", "subprocess", "cryptography", "maplibre", "WebWorker", "decode("):
            self.assertNotIn(token, source)

    def test_source_map_names_full_atlas_lineage_and_existing_boundaries(self) -> None:
        source = (ROOT / "docs/intake/exploratory/verified-rendering-resource-envelope-source-map.md").read_text(encoding="utf-8")
        for value in ("KFM-TRIAD-052", "KFM-CAND-0154", "KFM-CAND-0155", "KFM-CAND-0156", "renderer capability", "verifier capability", "PMTiles"):
            self.assertIn(value, source)


if __name__ == "__main__":
    unittest.main()
