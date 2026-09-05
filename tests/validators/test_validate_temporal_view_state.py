"""Focused tests for the proposed TemporalViewState profile."""

from __future__ import annotations

import contextlib
from copy import deepcopy
import io
import json
import os
from pathlib import Path
import socket
import tempfile
import unittest
import urllib.request
from unittest import mock

from tools.validators.validate_temporal_view_state import (
    FIXTURE_ROOT,
    main,
    run_fixture_profile,
    validate_file,
)
from packages.temporal.src.temporal.core import (
    TemporalFrameContext,
    TemporalFrameLayer,
    commit_frame,
    compute_query_id,
    compute_state_id,
    create_runtime_state,
    normalize_temporal_query,
    request_frame,
    validate_frame_context,
)

ROOT = Path(__file__).resolve().parents[2]


class TemporalViewStateValidatorTests(unittest.TestCase):
    def _read(self, path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _state(self, name: str = "valid_snapshot.json") -> dict[str, object]:
        return self._read(FIXTURE_ROOT / "valid" / name)

    def _reidentify(self, state: dict[str, object]) -> dict[str, object]:
        state["state_id"] = compute_state_id(state)
        return state

    def test_valid_fixtures_pass_and_state_identity_is_reproducible(self) -> None:
        for name in ("valid_snapshot.json", "valid_comparison.json"):
            with self.subTest(name=name):
                state = self._state(name)
                report = validate_file(FIXTURE_ROOT / "valid" / name)
                self.assertEqual(report.outcome, "PASS", report.findings)
                self.assertEqual(state["state_id"], compute_state_id(state))

    def test_invalid_fixtures_fail_closed_for_reviewed_schema_errors(self) -> None:
        for name in ("invalid_extra_property.json", "invalid_display_mode.json"):
            with self.subTest(name=name):
                report = validate_file(FIXTURE_ROOT / "invalid" / name)
                self.assertEqual(report.outcome, "FAIL")
                self.assertTrue(any(item.code == "SCHEMA_INVALID" for item in report.findings))

    def test_unsupported_profiles_are_bounded_not_repaired(self) -> None:
        expected = {
            "geologic_age.json": "UNSUPPORTED_PROFILE",
            "naive_instant.json": "UNKNOWN_TIMEZONE",
        }
        for name, code in expected.items():
            with self.subTest(name=name):
                report = validate_file(FIXTURE_ROOT / "unsupported" / name)
                self.assertEqual(report.outcome, "UNSUPPORTED", report.findings)
                self.assertEqual(report.normalization, code)

    def test_calendar_and_window_profiles_keep_typed_boundaries(self) -> None:
        state = self._state()
        state["selection"] = deepcopy(state["selection"])
        state["selection"]["selection_mode"] = "WINDOW"
        state["selection"]["end"] = deepcopy(state["selection"]["start"])
        state["selection"]["end"]["raw"] = "2024-01-31T00:00:00Z"
        state["selection"]["end"]["normalized"] = "2024-01-31T00:00:00Z"
        state["display"] = deepcopy(state["display"])
        state["display"]["mode"] = "MOVING_WINDOW"
        state["display"]["step_rule"] = "CALENDAR"
        state["display"]["window_duration"] = "P1M"
        self._reidentify(state)
        result = normalize_temporal_query(state)
        self.assertEqual(result.status, "SUPPORTED", result)
        self.assertEqual(result.start.profile, "instant")
        self.assertEqual(result.end.profile, "instant")

    def test_regular_snapshot_and_reversed_interval_outcomes(self) -> None:
        state = self._state()
        query_result = normalize_temporal_query(state)
        self.assertEqual(query_result.status, "SUPPORTED")

        state["selection"] = deepcopy(state["selection"])
        state["selection"]["selection_mode"] = "WINDOW"
        state["selection"]["end"] = deepcopy(state["selection"]["start"])
        state["selection"]["start"]["raw"] = "2024-02-01T00:00:00Z"
        state["selection"]["start"]["normalized"] = "2024-02-01T00:00:00Z"
        state["selection"]["end"]["raw"] = "2024-01-01T00:00:00Z"
        state["selection"]["end"]["normalized"] = "2024-01-01T00:00:00Z"
        self.assertEqual(normalize_temporal_query(state).code, "REVERSED_INTERVAL")

    def _frame(self, state: dict[str, object]) -> TemporalFrameContext:
        query_id = compute_query_id(state)
        layer = TemporalFrameLayer(
            layer_id="kfm:layer:streamflow",
            actual_time="2024-01-01T00:00:00Z",
            availability="AVAILABLE",
            evidence_refs=("kfm:evidence:fixture:streamflow-2024-01-01",),
            source_version_ref="kfm:dataset:fixture:streamflow-v1",
            release_status="RELEASED",
        )
        return TemporalFrameContext(
            state_id=compute_state_id(state),
            query_id=query_id,
            selected_support={"raw": "2024-01-01T00:00:00Z"},
            layers=(layer,),
            dataset_version_refs=("kfm:dataset:fixture:streamflow-v1",),
            release_refs=("kfm:release:fixture:streamflow-v1",),
            policy_status="CURRENT_POLICY",
        )

    def test_generation_guard_rejects_stale_commit_and_accepts_current_commit(self) -> None:
        state = self._state()
        first = request_frame(state, create_runtime_state())
        newer = request_frame(state, first)
        frame = self._frame(state)
        self.assertIs(commit_frame(newer, first.generation, frame), newer)
        committed = commit_frame(newer, newer.generation, frame)
        self.assertEqual(committed.status, "COMMITTED")
        self.assertIs(committed.committed_frame, frame)

    def test_withheld_layer_cannot_carry_time_or_evidence(self) -> None:
        state = self._state()
        frame = self._frame(state)
        withheld = TemporalFrameContext(
            state_id=frame.state_id,
            query_id=frame.query_id,
            selected_support=frame.selected_support,
            layers=(
                TemporalFrameLayer(
                    layer_id=frame.layers[0].layer_id,
                    actual_time=None,
                    availability="WITHHELD",
                    evidence_refs=(),
                    source_version_ref=None,
                    release_status="WITHHELD",
                ),
            ),
            dataset_version_refs=frame.dataset_version_refs,
            release_refs=frame.release_refs,
            policy_status=frame.policy_status,
        )
        self.assertEqual(validate_frame_context(withheld), ("SUPPORTED", "OK"))

        leaked = TemporalFrameContext(
            state_id=withheld.state_id,
            query_id=withheld.query_id,
            selected_support=withheld.selected_support,
            layers=(
                TemporalFrameLayer(
                    layer_id=withheld.layers[0].layer_id,
                    actual_time="2024-01-01T00:00:00Z",
                    availability="WITHHELD",
                    evidence_refs=("kfm:evidence:restricted",),
                    source_version_ref=None,
                    release_status="WITHHELD",
                ),
            ),
            dataset_version_refs=withheld.dataset_version_refs,
            release_refs=withheld.release_refs,
            policy_status=withheld.policy_status,
        )
        self.assertEqual(validate_frame_context(leaked), ("ERROR", "WITHHELD_DATA_LEAK"))

    def test_fixture_profile_is_non_vacuous_and_no_network(self) -> None:
        def forbidden(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("unexpected network access")

        with (
            mock.patch.object(socket.socket, "connect", forbidden),
            mock.patch.object(socket, "create_connection", forbidden),
            mock.patch.object(urllib.request, "urlopen", forbidden),
        ):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(main(["--fixtures", "--format", "json"]), 0)
            output = stream.getvalue()
        self.assertEqual(output.count('"outcome":"PASS"'), 2)
        self.assertEqual(output.count('"outcome":"UNSUPPORTED"'), 2)
        self.assertEqual(output.count('"outcome":"FAIL"'), 2)
        self.assertNotIn("restricted", output)

    def test_cli_failure_does_not_echo_temporal_values(self) -> None:
        state = self._state()
        state["selection"] = deepcopy(state["selection"])
        state["selection"]["selection_mode"] = "WINDOW"
        state["selection"]["end"] = deepcopy(state["selection"]["start"])
        state["selection"]["start"]["raw"] = "2024-02-01T00:00:00Z"
        state["selection"]["start"]["normalized"] = "2024-02-01T00:00:00Z"
        state["selection"]["end"]["raw"] = "2024-01-01T00:00:00Z"
        state["selection"]["end"]["normalized"] = "2024-01-01T00:00:00Z"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(self._reidentify(state)), encoding="utf-8")
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(main([str(path)]), 1)
        self.assertIn("REVERSED_INTERVAL", stream.getvalue())
        self.assertNotIn("2024-02-01", stream.getvalue())

    def test_direct_script_entrypoint_is_available(self) -> None:
        self.assertTrue((ROOT / "tools/validators/validate_temporal_view_state.py").is_file())


if __name__ == "__main__":
    unittest.main()
