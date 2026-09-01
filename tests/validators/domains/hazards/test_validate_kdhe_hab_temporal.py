from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from tools.validators.domains.hazards.validate_kdhe_hab_temporal import (
    FIXTURES,
    main as validate_main,
    run_fixture_suite,
    validate_document,
    validate_file,
)


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("KDHE HAB temporal validation attempted network access")


class KdheHabTemporalValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.watch = json.loads(
            (FIXTURES / "valid" / "valid_watch.json").read_text(encoding="utf-8")
        )

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary_directory.name) / "candidate.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _candidate(self) -> dict[str, object]:
        return copy.deepcopy(self.watch)

    def test_committed_fixture_polarity_passes(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertGreater(payload["valid_fixtures"], 0)
        self.assertGreater(payload["invalid_fixtures"], 0)
        self.assertEqual(payload["authority"], "NONE")

    def test_observation_times_are_monotonic(self) -> None:
        candidate = self._candidate()
        candidate["first_observed_at"] = "2026-07-24T17:00:00Z"
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "KDHE_HAB_OBSERVATION_TIME_ORDER_INVALID",
            {finding.code for finding in result.findings},
        )

    def test_source_update_cannot_follow_retrieval(self) -> None:
        candidate = self._candidate()
        candidate["source_updated_at"] = "2026-07-24T17:00:00Z"
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "KDHE_HAB_SOURCE_TIME_AFTER_RETRIEVAL",
            {finding.code for finding in result.findings},
        )

    def test_current_snapshot_exceeding_budget_is_denied(self) -> None:
        candidate = self._candidate()
        candidate["retrieved_at"] = "2026-07-25T16:00:01Z"
        candidate["last_observed_at"] = "2026-07-25T16:00:01Z"
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "KDHE_HAB_FRESHNESS_BUDGET_EXCEEDED",
            {finding.code for finding in result.findings},
        )

    def test_active_state_must_be_current(self) -> None:
        candidate = self._candidate()
        candidate["freshness_status"] = "stale"
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "KDHE_HAB_ACTIVE_STATE_NOT_CURRENT",
            {finding.code for finding in result.findings},
        )

    def test_explicit_stale_source_remains_fail_closed_and_valid(self) -> None:
        stale = json.loads(
            (FIXTURES / "valid" / "valid_stale_source.json").read_text(encoding="utf-8")
        )
        self.assertEqual(validate_document(stale).outcome, "PASS")

    def test_validation_is_no_network_and_diagnostics_do_not_echo_values(self) -> None:
        candidate = self._candidate()
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_document(candidate).outcome, "PASS")

        marker = "synthetic-sensitive-marker-must-not-echo"
        candidate["evidence_refs"] = [marker]
        candidate["retrieved_at"] = "2026-07-25T16:00:01Z"
        candidate["last_observed_at"] = "2026-07-25T16:00:01Z"
        self.path.write_text(json.dumps(candidate) + "\n", encoding="utf-8")
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            self.assertEqual(validate_main([str(self.path)]), 1)
        self.assertNotIn(marker, stream.getvalue())
        self.assertIn("KDHE_HAB_FRESHNESS_BUDGET_EXCEEDED", stream.getvalue())

    def test_bounded_loader_returns_error_for_duplicate_and_malformed_json(self) -> None:
        self.path.write_text('{"source_id":"a","source_id":"b"}\n', encoding="utf-8")
        self.assertEqual(validate_file(self.path).outcome, "ERROR")
        self.path.write_text("{not-json}\n", encoding="utf-8")
        self.assertEqual(validate_file(self.path).outcome, "ERROR")

    def test_schema_invalid_types_return_finite_deny_results(self) -> None:
        invalid_state = self._candidate()
        invalid_state["normalized_state"] = ["WATCH"]
        self.assertEqual(validate_document(invalid_state).outcome, "DENY")

        invalid_budget = self._candidate()
        invalid_budget["freshness_budget_hours"] = 10**1000
        self.assertEqual(validate_document(invalid_budget).outcome, "DENY")


if __name__ == "__main__":
    unittest.main()
