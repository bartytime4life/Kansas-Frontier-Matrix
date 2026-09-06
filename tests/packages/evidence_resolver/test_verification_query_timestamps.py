"""Regression coverage for the bounded verification replay query grammar."""

from __future__ import annotations

from contextlib import ExitStack
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/evidence-resolver/src"))

from evidence_resolver.core import (  # noqa: E402
    evaluate_resolution_candidate,
    result_json,
)
from evidence_resolver.runtime_projection import (  # noqa: E402
    REQUIRED_NEXT_CHECKS,
    project_runtime_posture,
)
from evidence_resolver.verification_history import (  # noqa: E402
    canonical_spec_hash,
    parse_timestamp,
    replay_state,
    validate_history,
)


FIXTURE = (
    REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1/valid/resolved.json"
)
CANONICAL = "2026-01-02T00:00:00Z"
NONCANONICAL = (
    "2026-1-02T00:00:00Z",
    "2026-01-2T00:00:00Z",
    "2026-01-02T0:00:00Z",
    "2026-01-02T00:0:00Z",
    "2026-01-02T00:00:0Z",
    "2026-01-02t00:00:00Z",
    "2026-01-02T00:00:00z",
)
AXES = ("effective_as_of", "recorded_as_of")


class VerificationQueryTimestampTests(unittest.TestCase):
    def setUp(self) -> None:
        self.request = json.loads(FIXTURE.read_text(encoding="utf-8"))["request"]
        self.history = self.request["verification_history"]
        self.assertEqual((), validate_history(self.history))

    def test_existing_positive_fixture_retains_all_authority_gates(self) -> None:
        result = evaluate_resolution_candidate(self.request)
        self.assertEqual("RESOLVED", result.status)
        self.assertEqual((), result.issues)
        self.assertFalse(result.as_dict()["authoritative"])
        posture = project_runtime_posture(result)
        self.assertEqual("CONTINUE_GOVERNED_CHECKS", posture.disposition)
        self.assertEqual(REQUIRED_NEXT_CHECKS, posture.required_next_checks)
        self.assertFalse(posture.as_dict()["authoritative"])
        self.assertFalse(posture.as_dict()["renderable"])

    def test_parser_rejects_strptime_normalization(self) -> None:
        for value in NONCANONICAL:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError, "^timestamp must be a real UTC second$"
                ):
                    parse_timestamp(value)

    def test_replay_rejects_noncanonical_values_on_both_time_axes(self) -> None:
        for axis in AXES:
            for value in NONCANONICAL:
                with self.subTest(axis=axis, value=value):
                    query = dict.fromkeys(AXES, CANONICAL)
                    query[axis] = value
                    with self.assertRaisesRegex(
                        ValueError, "^invalid replay query timestamp$"
                    ):
                        replay_state(self.history, **query)

    def test_candidate_errors_instead_of_resolving_malformed_queries(self) -> None:
        for axis in AXES:
            for value in NONCANONICAL:
                with self.subTest(axis=axis, value=value):
                    request = deepcopy(self.request)
                    request["verification_as_of"][axis] = value
                    result = evaluate_resolution_candidate(request)
                    self.assertEqual("ERROR", result.status)
                    self.assertIsNone(result.bundle_id)
                    self.assertEqual(
                        [{"code": "verification/query-invalid",
                          "field": "verification_as_of"}],
                        result.as_dict()["issues"],
                    )
                    posture = project_runtime_posture(result)
                    self.assertEqual("ERROR", posture.disposition)
                    self.assertIsNone(posture.bundle_id)
                    self.assertFalse(posture.as_dict()["authoritative"])
                    self.assertFalse(posture.as_dict()["renderable"])

    def test_valid_calendar_boundaries_remain_supported(self) -> None:
        cases = (
            ("0001-01-01T00:00:00Z", (1, 1, 1, 0, 0, 0)),
            ("2000-02-29T23:59:59Z", (2000, 2, 29, 23, 59, 59)),
            ("2024-02-29T12:30:45Z", (2024, 2, 29, 12, 30, 45)),
            ("9999-12-31T23:59:59Z", (9999, 12, 31, 23, 59, 59)),
        )
        for value, parts in cases:
            with self.subTest(value=value):
                self.assertEqual(
                    datetime(*parts, tzinfo=timezone.utc), parse_timestamp(value)
                )

    def test_invalid_calendar_and_out_of_profile_forms_remain_rejected(self) -> None:
        values = (
            "2026-02-29T00:00:00Z", "2026-13-01T00:00:00Z",
            "2026-01-00T00:00:00Z", "2026-01-02T24:00:00Z",
            "2026-01-02T00:60:00Z", "2026-01-02T00:00:60Z",
            "2026-01-02T00:00:00+00:00", "2026-01-02T00:00:00.0Z",
            "2026-01-02 00:00:00Z", "2026-01-02T00:00:00Z\n",
            " 2026-01-02T00:00:00Z", "2026-01-02T00:00:00", "",
        )
        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError, "^timestamp must be a real UTC second$"
                ):
                    parse_timestamp(value)

    def test_non_string_parser_inputs_keep_safe_value_error(self) -> None:
        for value in (None, 0, True, b"2026-01-02T00:00:00Z", [], {}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError, "^timestamp must be a real UTC second$"
                ):
                    parse_timestamp(value)

    def test_history_event_shape_is_not_relaxed(self) -> None:
        for field in ("effective_at", "recorded_at"):
            for value in NONCANONICAL:
                with self.subTest(field=field, value=value):
                    history = deepcopy(self.history)
                    history["events"][0][field] = value
                    history["spec_hash"] = canonical_spec_hash(history)
                    self.assertEqual(
                        {"VERIFICATION_HISTORY_SCHEMA_INVALID"},
                        {finding.code for finding in validate_history(history)},
                    )

    def test_policy_outcomes_keep_their_existing_finite_projections(self) -> None:
        cases = (
            ("ANSWER", "RESOLVED", "CONTINUE_GOVERNED_CHECKS"),
            ("ABSTAIN", "UNRESOLVED", "ABSTAIN"),
            ("DENY", "DENIED", "DENY"),
            ("ERROR", "ERROR", "ERROR"),
        )
        for policy, status, disposition in cases:
            with self.subTest(policy=policy):
                request = deepcopy(self.request)
                request["lookup_context"]["policy_outcome"] = policy
                result = evaluate_resolution_candidate(request)
                self.assertEqual(status, result.status)
                posture = project_runtime_posture(result)
                self.assertEqual(disposition, posture.disposition)
                self.assertFalse(posture.as_dict()["authoritative"])
                self.assertFalse(posture.as_dict()["renderable"])
                if status != "RESOLVED":
                    self.assertIsNone(result.bundle_id)

    def test_invalid_query_keeps_error_precedence_over_policy(self) -> None:
        for policy in ("ANSWER", "ABSTAIN", "DENY", "ERROR"):
            with self.subTest(policy=policy):
                request = deepcopy(self.request)
                request["lookup_context"]["policy_outcome"] = policy
                request["verification_as_of"]["effective_as_of"] = NONCANONICAL[0]
                result = evaluate_resolution_candidate(request)
                self.assertEqual("ERROR", result.status)
                self.assertEqual(
                    ["verification/query-invalid"],
                    [issue.code for issue in result.issues],
                )
                self.assertIsNone(result.bundle_id)

    def test_valid_bitemporal_correction_replay_is_unchanged(self) -> None:
        history = deepcopy(self.history)
        history["events"].append({
            "event_id": "evt:002", "event_type": "CORRECTED",
            "state": "CORRECTED", "effective_at": "2026-01-03T00:00:00Z",
            "recorded_at": "2026-01-04T00:00:00Z",
            "reason_code": "SYNTHETIC_CORRECTION",
            "basis_refs": ["kfm://synthetic/receipt/correction-002"],
            "relates_to_event_id": "evt:001",
            "correction_ref": "kfm://synthetic/correction/002",
        })
        history["spec_hash"] = canonical_spec_hash(history)
        self.assertEqual((), validate_history(history))
        before = deepcopy(history)
        cases = (
            ("2026-01-02T00:00:00Z", "2026-01-04T00:00:00Z", "ACTIVE", "RESOLVED"),
            ("2026-01-03T00:00:00Z", "2026-01-03T23:59:59Z", "ACTIVE", "RESOLVED"),
            ("2026-01-03T00:00:00Z", "2026-01-04T00:00:00Z", "CORRECTED", "UNRESOLVED"),
        )
        for effective, recorded, state, status in cases:
            with self.subTest(effective=effective, recorded=recorded):
                query = {"effective_as_of": effective, "recorded_as_of": recorded}
                replay = replay_state(history, **query)
                self.assertEqual(state, replay.state)
                self.assertEqual(state != "ACTIVE", replay.answer_blocked)
                request = deepcopy(self.request)
                request["verification_history"] = history
                request["verification_as_of"] = query
                result = evaluate_resolution_candidate(request)
                self.assertEqual(status, result.status)
                if status == "UNRESOLVED":
                    self.assertIsNone(result.bundle_id)
                    self.assertEqual("ABSTAIN", project_runtime_posture(result).disposition)
        self.assertEqual(before, history)

    def test_hash_failure_and_unknown_history_remain_fail_closed(self) -> None:
        request = deepcopy(self.request)
        request["verification_history"]["spec_hash"] = "sha256:" + "0" * 64
        result = evaluate_resolution_candidate(request)
        self.assertEqual("ERROR", result.status)
        self.assertEqual(["verification/history-invalid"], [i.code for i in result.issues])
        request = deepcopy(self.request)
        request["verification_as_of"] = dict.fromkeys(AXES, "2025-12-31T23:59:59Z")
        result = evaluate_resolution_candidate(request)
        self.assertEqual("UNRESOLVED", result.status)
        self.assertEqual(["verification/unknown"], [i.code for i in result.issues])
        self.assertIsNone(result.bundle_id)
        self.assertEqual("ABSTAIN", project_runtime_posture(result).disposition)

    def test_query_diagnostics_are_deterministic_and_do_not_echo_input(self) -> None:
        sentinel = "protected-query-value-do-not-echo"
        request = deepcopy(self.request)
        request["verification_as_of"]["recorded_as_of"] = sentinel
        first = result_json(evaluate_resolution_candidate(request))
        self.assertEqual(first, result_json(evaluate_resolution_candidate(request)))
        self.assertNotIn(sentinel, first)
        self.assertEqual("ERROR", json.loads(first)["status"])

    def test_candidate_replay_avoids_guarded_io_and_input_mutation(self) -> None:
        before = deepcopy(self.request)
        # Warm stdlib timestamp parsing before the guards (not resolver I/O).
        parse_timestamp(CANONICAL)
        with ExitStack() as guards:
            mocks = [guards.enter_context(mock.patch(target, side_effect=AssertionError(target)))
                     for target in (
                         "socket.socket", "socket.getaddrinfo", "urllib.request.urlopen",
                         "subprocess.run", "pathlib.Path.read_text",
                     )]
            result = evaluate_resolution_candidate(self.request)
            self.assertEqual("RESOLVED", result.status)
            for guarded in mocks:
                guarded.assert_not_called()
        self.assertEqual(before, self.request)


if __name__ == "__main__":
    unittest.main()
