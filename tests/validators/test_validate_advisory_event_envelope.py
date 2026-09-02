from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators import validate_advisory_event_envelope as validator

CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/common/advisory_event_envelope/cases.json"
CASES = validator.load_fixture_cases()


class AdvisoryEventEnvelopeTests(unittest.TestCase):
    def _case(self, name: str) -> dict:
        for item in CASES:
            if item["name"] == name:
                return copy.deepcopy(item["envelope"])
        self.fail(f"fixture case not found: {name}")

    def _codes_for_data(self, data: dict) -> set[str]:
        result = validator.validate_envelope_object(data)
        return {finding.code for finding in result.findings}

    def _write(self, data: dict) -> Path:
        handle = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", encoding="utf-8", delete=False
        )
        json.dump(data, handle, indent=2)
        handle.close()
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        return Path(handle.name)

    def test_fixture_manifest_count_and_names(self) -> None:
        self.assertEqual(CASES_PATH.name, "cases.json")
        self.assertEqual(len(CASES), 15)
        self.assertEqual(len({item["name"] for item in CASES}), 15)

    def test_all_declared_fixture_polarity(self) -> None:
        ok, rows = validator.validate_fixture_polarity()
        self.assertTrue(ok)
        self.assertEqual(len(rows), 15)

    def test_six_valid_cases_pass(self) -> None:
        valid = [item for item in CASES if item["class"] == "valid"]
        self.assertEqual(len(valid), 6)
        for item in valid:
            with self.subTest(case=item["name"]):
                self.assertTrue(
                    validator.validate_envelope_object(item["envelope"]).ok
                )

    def test_negative_cases_have_exact_required_codes(self) -> None:
        rejected = [item for item in CASES if not item["expected_ok"]]
        self.assertEqual(len(rejected), 9)
        for item in rejected:
            with self.subTest(case=item["name"]):
                result = validator.validate_envelope_object(item["envelope"])
                self.assertFalse(result.ok)
                self.assertIn(
                    item["expected_code"],
                    {finding.code for finding in result.findings},
                )

    def test_event_id_is_recomputed(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["event"]["event_id"] = "kfm:advisory:" + "0" * 64
        self.assertIn("EVENT_ID_MISMATCH", self._codes_for_data(data))

    def test_payload_record_digest_is_recomputed(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["domain_payload"]["payload_record_digest"] = "sha256:" + "0" * 64
        self.assertIn("PAYLOAD_RECORD_DIGEST_MISMATCH", self._codes_for_data(data))

    def test_payload_source_digest_is_bound(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["domain_payload"]["payload_source_content_digest"] = (
            "sha256:" + "0" * 64
        )
        self.assertIn("PAYLOAD_SOURCE_DIGEST_MISMATCH", self._codes_for_data(data))

    def test_native_event_identity_is_bound(self) -> None:
        data = self._case("valid_1_hab_watch")
        wrong = "kdhe-hab:" + "0" * 64
        data["event"]["native_event_id"] = wrong
        data["temporal_authority"]["identity"]["native_id"] = wrong
        data["event"]["event_id"] = validator.canonical_event_id(data)
        codes = self._codes_for_data(data)
        self.assertIn("NATIVE_EVENT_ID_MISMATCH", codes)
        self.assertIn("TEMPORAL_NATIVE_ID_MISMATCH", codes)

    def test_source_surface_is_bound_to_payload(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["source_surface"]["snapshot_complete"] = False
        self.assertIn("SOURCE_SURFACE_MISMATCH", self._codes_for_data(data))

    def test_release_reference_fails_closed(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["temporal_authority"]["governance"]["release_ref"] = (
            "kfm://release/fixture"
        )
        self.assertIn("RELEASE_AUTHORITY_PRESENT", self._codes_for_data(data))

    def test_payload_path_traversal_is_rejected(self) -> None:
        data = self._case("valid_1_hab_watch")
        data["domain_payload"]["payload_ref"] = (
            "fixtures/domains/hazards/kdhe_hab_advisory_snapshot/"
            "valid/../valid_watch.json"
        )
        self.assertIn("SCHEMA_INVALID", self._codes_for_data(data))

    def test_duplicate_key_is_rejected(self) -> None:
        handle = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", encoding="utf-8", delete=False
        )
        handle.write('{"schema_version":"1.0.0","schema_version":"1.0.0"}')
        handle.close()
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        result = validator.validate_envelope(Path(handle.name))
        self.assertIn(
            "JSON_DUPLICATE_KEY", {finding.code for finding in result.findings}
        )

    def test_nonfinite_number_is_rejected(self) -> None:
        handle = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", encoding="utf-8", delete=False
        )
        handle.write('{"value": NaN}')
        handle.close()
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        result = validator.validate_envelope(Path(handle.name))
        self.assertIn(
            "JSON_NONFINITE_NUMBER", {finding.code for finding in result.findings}
        )

    @unittest.skipUnless(hasattr(os, "symlink"), "symlink support required")
    def test_input_symlink_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self._write(self._case("valid_1_hab_watch"))
            link = Path(tmp) / "candidate.json"
            os.symlink(target, link)
            result = validator.validate_envelope(link)
            self.assertIn(
                "INPUT_SYMLINK_DENIED",
                {finding.code for finding in result.findings},
            )

    def test_cli_success_and_failure(self) -> None:
        script = REPO_ROOT / "tools/validators/validate_advisory_event_envelope.py"
        valid = self._write(self._case("valid_1_hab_watch"))
        invalid = self._write(self._case("invalid_1_false_clear_attempt"))
        passed = subprocess.run(
            [sys.executable, str(script), str(valid)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertTrue(json.loads(passed.stdout)["ok"])
        rejected = subprocess.run(
            [sys.executable, str(script), str(invalid)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(rejected.returncode, 1, rejected.stderr)
        self.assertFalse(json.loads(rejected.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
