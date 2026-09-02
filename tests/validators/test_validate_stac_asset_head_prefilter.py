"""Deterministic no-network tests for the STAC asset HEAD prefilter profile."""

from __future__ import annotations

import contextlib
import io
import json
import socket
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.validate_stac_asset_head_prefilter import (
    FIXTURE_PATH,
    NON_EFFECTS,
    SCHEMA_PATH,
    main as validate_main,
    materialize_fixture_case,
    run_fixture_suite,
    validate_document,
)

ROOT = Path(__file__).resolve().parents[2]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("STAC HEAD prefilter validation attempted network access")


class StacAssetHeadPrefilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.base_document = fixture["base_document"]
        cls.cases = fixture["cases"]
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def _document(self, case_id: str) -> dict[str, object]:
        return materialize_fixture_case(self.base_document, self.by_id[case_id])

    def test_profile_schema_is_valid_closed_and_download_denied(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["properties"]["stac.download_allowed"]["const"])
        self.assertEqual(
            schema["properties"]["stac.profile"]["const"],
            "kfm.stac_asset_head_prefilter.v1",
        )

    def test_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(len(self.cases), 10)
        self.assertEqual(sum(case["expected_outcome"] == "PASS" for case in self.cases), 6)
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = validate_document(
                    materialize_fixture_case(self.base_document, case)
                )
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"], actual)
                self.assertEqual(actual, case["expected_findings"])

    def test_fixture_runner_passes_without_authority(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["authority"], "NONE")
        self.assertEqual(payload["cases"], 10)
        self.assertIn("no_network_request", payload["non_effects"])
        self.assertIn("no_asset_download", payload["non_effects"])

    def test_unchanged_profiles_route_to_no_action(self) -> None:
        for case_id in ("valid_http_304_unchanged", "valid_http_200_validator_match"):
            candidate = self._document(case_id)
            self.assertEqual(validate_document(candidate).outcome, "PASS")
            self.assertEqual(candidate["payload"]["attributes"]["stac.decision"], "UNCHANGED")
            self.assertEqual(candidate["routing"]["disposition"], "NO_ACTION")
            self.assertFalse(candidate["routing"]["review_required"])
            self.assertFalse(candidate["payload"]["attributes"]["stac.download_allowed"])

    def test_changed_unavailable_denied_and_error_profiles_fail_closed(self) -> None:
        expected = {
            "valid_http_200_validator_changed": "CHANGED",
            "valid_http_404_unavailable": "UNAVAILABLE",
            "valid_http_403_denied": "DENY",
            "valid_http_503_error": "ERROR",
        }
        for case_id, decision in expected.items():
            candidate = self._document(case_id)
            self.assertEqual(validate_document(candidate).outcome, "PASS")
            self.assertEqual(candidate["payload"]["attributes"]["stac.decision"], decision)
            self.assertEqual(candidate["routing"]["disposition"], "PROPOSE_QUARANTINE")
            self.assertTrue(candidate["routing"]["review_required"])
            self.assertFalse(candidate["routing"]["raw_write_allowed"])
            self.assertFalse(candidate["routing"]["publication_allowed"])

    def test_conflicting_or_missing_validators_are_denied(self) -> None:
        conflict = validate_document(self._document("invalid_conflicting_validators"))
        self.assertEqual(conflict.outcome, "DENY")
        self.assertIn("STAC_VALIDATOR_CONFLICT", {item.code for item in conflict.findings})
        missing = validate_document(self._document("invalid_missing_observed_validators"))
        self.assertEqual(missing.outcome, "DENY")
        self.assertIn("STAC_VALIDATOR_MISSING", {item.code for item in missing.findings})

    def test_base_envelope_identity_remains_a_hard_dependency(self) -> None:
        candidate = self._document("valid_http_200_validator_match")
        candidate["event_id"] = "kfm:source-event:sha256:" + "f" * 64
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("EVENT_ID_MISMATCH", {item.code for item in result.findings})

    def test_validation_is_no_network_deterministic_and_non_echoing(self) -> None:
        candidate = self._document("valid_http_200_validator_match")
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_document(candidate).outcome, "PASS")

        marker = "synthetic-stac-value-that-must-not-echo"
        candidate["payload"]["attributes"]["stac.asset_href"] = marker
        temporary = ROOT / "artifacts" / "tmp-stac-prefilter-test.json"
        temporary.parent.mkdir(parents=True, exist_ok=True)
        temporary.write_text(json.dumps(candidate), encoding="utf-8")
        try:
            outputs: list[str] = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    code = validate_main([str(temporary)])
                self.assertEqual(code, 1)
                outputs.append(stream.getvalue())
            self.assertEqual(outputs[0], outputs[1])
            self.assertNotIn(marker, outputs[0])
            self.assertIn("PAYLOAD_SPEC_HASH_MISMATCH", outputs[0])
        finally:
            temporary.unlink(missing_ok=True)

    def test_non_effects_remain_explicit(self) -> None:
        self.assertIn("no_network_request", NON_EFFECTS)
        self.assertIn("no_asset_download", NON_EFFECTS)
        self.assertIn("no_promotion_release_deployment_or_publication", NON_EFFECTS)


if __name__ == "__main__":
    unittest.main()
