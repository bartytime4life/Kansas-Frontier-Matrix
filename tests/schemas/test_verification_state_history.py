from __future__ import annotations

import json
import socket
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest import mock

from tools.validators._common.public_safe_fixture import MAX_FIXTURE_BYTES
from tools.validators.validate_verification_state_history import (
    FIXTURES_ROOT,
    canonical_spec_hash,
    main,
    replay_state,
    validate_document,
    validate_history_file,
)


class VerificationStateHistoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_files = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
        self.invalid_files = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))

    def _load_valid(self, name: str) -> dict[str, object]:
        return json.loads(
            (FIXTURES_ROOT / "valid" / name).read_text(encoding="utf-8")
        )

    def test_fixture_polarity_and_exact_negative_codes(self) -> None:
        self.assertEqual(len(self.valid_files), 2)
        for path in self.valid_files:
            with self.subTest(path=path.name):
                self.assertEqual(validate_history_file(path), [])

        expected_codes = {
            "invalid_missing_correction_ref.json": {
                "VERIFICATION_HISTORY_SCHEMA_INVALID"
            },
            "semantic_broken_chain.json": {
                "VERIFICATION_HISTORY_CHAIN_INVALID"
            },
            "semantic_effective_after_recorded.json": {
                "VERIFICATION_HISTORY_EFFECTIVE_AFTER_RECORDED"
            },
            "semantic_hash_mismatch.json": {
                "VERIFICATION_HISTORY_HASH_MISMATCH"
            },
            "semantic_invalid_timestamp.json": {
                "VERIFICATION_HISTORY_TIMESTAMP_INVALID"
            },
            "semantic_record_order.json": {
                "VERIFICATION_HISTORY_EVENT_ORDER_INVALID"
            },
            "semantic_transition_after_supersession.json": {
                "VERIFICATION_HISTORY_TRANSITION_INVALID"
            },
        }
        self.assertEqual({path.name for path in self.invalid_files}, set(expected_codes))
        for path in self.invalid_files:
            with self.subTest(path=path.name):
                codes = {finding.code for finding in validate_history_file(path)}
                self.assertEqual(codes, expected_codes[path.name])

    def test_late_recorded_correction_replays_both_time_axes(self) -> None:
        history = self._load_valid("valid_late_recorded_correction.json")
        cases = [
            ("2026-01-10T00:00:00Z", "2026-01-01T00:00:00Z", "UNKNOWN", True),
            ("2026-01-10T00:00:00Z", "2026-01-10T00:00:00Z", "ACTIVE", False),
            ("2026-01-20T00:00:00Z", "2026-01-25T00:00:00Z", "ACTIVE", False),
            ("2026-01-20T00:00:00Z", "2026-02-02T00:00:00Z", "CORRECTED", True),
            ("2026-01-25T00:00:00Z", "2026-02-06T00:00:00Z", "ACTIVE", False),
            ("2026-03-02T00:00:00Z", "2026-03-02T00:00:00Z", "SUPERSEDED", True),
        ]
        for effective_as_of, recorded_as_of, state, answer_blocked in cases:
            with self.subTest(effective_as_of=effective_as_of, recorded_as_of=recorded_as_of):
                result = replay_state(
                    history,
                    effective_as_of=effective_as_of,
                    recorded_as_of=recorded_as_of,
                )
                self.assertEqual(result.state, state)
                self.assertEqual(result.answer_blocked, answer_blocked)

    def test_revocation_blocks_answer_until_reverification_is_eligible(self) -> None:
        history = self._load_valid("valid_revocation_reverification.json")
        revoked = replay_state(
            history,
            effective_as_of="2026-02-10T00:00:00Z",
            recorded_as_of="2026-02-03T00:00:00Z",
        )
        restored = replay_state(
            history,
            effective_as_of="2026-02-10T00:00:00Z",
            recorded_as_of="2026-02-16T00:00:00Z",
        )
        self.assertEqual((revoked.state, revoked.answer_blocked), ("REVOKED", True))
        self.assertEqual((restored.state, restored.answer_blocked), ("ACTIVE", False))

    def test_hash_order_and_duplicate_identity_are_deterministic(self) -> None:
        history = self._load_valid("valid_late_recorded_correction.json")
        self.assertEqual(history["spec_hash"], canonical_spec_hash(history))

        reordered = deepcopy(history)
        events = reordered["events"]
        assert isinstance(events, list)
        events[1], events[2] = events[2], events[1]
        reordered["spec_hash"] = canonical_spec_hash(reordered)
        codes = {finding.code for finding in validate_document(reordered)}
        self.assertIn("VERIFICATION_HISTORY_EVENT_ORDER_INVALID", codes)

        duplicate = deepcopy(history)
        duplicate_events = duplicate["events"]
        assert isinstance(duplicate_events, list)
        duplicate_events[1]["event_id"] = duplicate_events[0]["event_id"]
        duplicate_events[1]["relates_to_event_id"] = duplicate_events[0]["event_id"]
        duplicate["spec_hash"] = canonical_spec_hash(duplicate)
        duplicate_codes = {finding.code for finding in validate_document(duplicate)}
        self.assertIn("VERIFICATION_HISTORY_EVENT_ID_DUPLICATE", duplicate_codes)

    def test_duplicate_json_keys_and_oversize_inputs_fail_before_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text(
                '{"schema_version":"1.0.0","schema_version":"1.0.0"}',
                encoding="utf-8",
            )
            self.assertEqual(validate_history_file(duplicate)[0].code, "FIXTURE_JSON_INVALID")

            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(validate_history_file(oversized)[0].code, "FIXTURE_TOO_LARGE")

    def test_cli_fixture_suite_and_single_file_polarity(self) -> None:
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(self.valid_files[0])]), 0)
        self.assertEqual(main([str(self.invalid_files[0])]), 1)
        self.assertEqual(main([]), 2)

    def test_replay_rejects_invalid_query_timestamp(self) -> None:
        history = self._load_valid("valid_late_recorded_correction.json")
        with self.assertRaisesRegex(ValueError, "invalid replay query timestamp"):
            replay_state(
                history,
                effective_as_of="2026-02-30T00:00:00Z",
                recorded_as_of="2026-03-01T00:00:00Z",
            )

    def test_validator_and_replay_have_no_network_dependency(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        history = self._load_valid("valid_late_recorded_correction.json")
        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            for path in self.valid_files + self.invalid_files:
                validate_history_file(path)
            replay_state(
                history,
                effective_as_of="2026-02-01T00:00:00Z",
                recorded_as_of="2026-02-01T00:00:00Z",
            )


if __name__ == "__main__":
    unittest.main()
