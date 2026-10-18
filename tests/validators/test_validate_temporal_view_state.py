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
    fail_frame,
    normalize_boundary,
    normalize_temporal_query,
    request_frame,
    validate_frame_context,
    validate_temporal_view_state,
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

    def test_calendar_profiles_reject_impossible_values(self) -> None:
        cases = (
            ("date_only", "2024-02-30"),
            ("date_only", "2023-02-29"),
            ("month", "2024-13"),
            ("month", "2024-00"),
            ("year", "0000"),
        )
        for profile, raw in cases:
            with self.subTest(profile=profile, raw=raw):
                state = self._state()
                state["selection"] = deepcopy(state["selection"])
                state["selection"]["start"] = deepcopy(state["selection"]["start"])
                state["selection"]["start"].update(
                    {"profile": profile, "raw": raw, "normalized": None}
                )
                result = normalize_temporal_query(state)
                self.assertEqual(result.status, "ERROR")
                self.assertEqual(result.code, "CALENDAR_VALUE_INVALID")
                self.assertIsNone(result.query_id)

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


def instant(raw: str, normalized: str | None = None) -> dict[str, object]:
    return {"profile": "instant", "raw": raw, "normalized": raw if normalized is None else normalized}


class TemporalCoreSemanticsTests(unittest.TestCase):
    """Semantic branches of packages/temporal behind the JSON Schema gate."""

    def _state(self) -> dict[str, object]:
        return json.loads((FIXTURE_ROOT / "valid" / "valid_snapshot.json").read_text(encoding="utf-8"))

    def _query(self, mutate) -> tuple[str, str]:
        state = self._state()
        mutate(state)
        result = normalize_temporal_query(state)
        return result.status, result.code

    def _window(self, start: dict[str, object], end: dict[str, object]) -> tuple[str, str]:
        def mutate(state: dict) -> None:
            state["selection"].update(selection_mode="WINDOW", start=start, end=end)
        return self._query(mutate)

    def test_instant_windows_compare_instants_not_strings(self) -> None:
        # "...:00Z" sorts after "...:00.5Z" as text; the window is still ordered.
        self.assertEqual(("SUPPORTED", "OK"), self._window(instant("2024-01-01T00:00:00Z"), instant("2024-01-01T00:00:00.5Z")))
        self.assertEqual(("SUPPORTED", "OK"), self._window(
            instant("2024-01-01T01:00:00+01:00", "2024-01-01T00:00:00Z"), instant("2024-01-01T00:30:00Z")))
        self.assertEqual(("ERROR", "REVERSED_INTERVAL"), self._window(instant("2024-01-01T00:00:00.5Z"), instant("2024-01-01T00:00:00Z")))

    def test_boundary_outcomes_are_typed_and_never_repaired(self) -> None:
        cases = [
            ({"profile": "decade", "raw": "1990s"}, "ERROR", "BOUNDARY_PROFILE_INVALID"),
            ({"profile": "year", "raw": ""}, "ERROR", "BOUNDARY_RAW_REQUIRED"),
            ({"profile": "year", "raw": "2024", "normalized": 2024}, "ERROR", "NORMALIZED_TYPE_INVALID"),
            ({"profile": "geologic_age", "raw": "Permian", "normalized": "x"}, "ERROR", "NORMALIZED_PRECISION_VIOLATION"),
            ({"profile": "geologic_age", "raw": "Permian"}, "UNSUPPORTED", "UNSUPPORTED_PROFILE"),
            ({"profile": "instant", "raw": "2024-01-01"}, "ERROR", "INSTANT_SYNTAX_INVALID"),
            ({"profile": "instant", "raw": "2024-02-30T00:00:00Z"}, "ERROR", "INSTANT_SYNTAX_INVALID"),
            ({"profile": "instant", "raw": "2024-01-01T00:00:00Z"}, "ERROR", "NORMALIZED_INSTANT_MISSING"),
            (instant("2024-01-01T00:00:00Z", "2024-01-01T00:00:00"), "ERROR", "NORMALIZED_INSTANT_INVALID"),
            (instant("2024-01-01T00:00:00+02:00", "2024-01-01T00:00:00Z"), "ERROR", "NORMALIZATION_MISMATCH"),
            ({"profile": "month", "raw": "2024-01", "normalized": "2024-01-01T00:00:00Z"}, "ERROR", "NORMALIZED_PRECISION_VIOLATION"),
            ({"profile": "month", "raw": "2024-1"}, "ERROR", "CALENDAR_SYNTAX_INVALID"),
            ({"profile": "year", "raw": "0000"}, "ERROR", "CALENDAR_VALUE_INVALID"),
            ({"profile": "uncertain_range", "raw": "circa 1870"}, "SUPPORTED", "CALENDAR_PRESERVED"),
        ]
        for boundary, status, code in cases:
            with self.subTest(boundary=boundary):
                result = normalize_boundary(boundary)
                self.assertEqual((status, code), (result.status, result.code))
        mismatch = normalize_boundary(instant("2024-01-01T00:00:00+02:00", "2024-01-01T00:00:00Z"))
        self.assertEqual("2023-12-31T22:00:00Z", mismatch.normalized)

    def test_query_members_are_closed_sets(self) -> None:
        def set_in(section: str, key: str, value: object):
            return lambda state: state[section].__setitem__(key, value)
        cases = [
            (lambda state: state.__setitem__("pins", []), "QUERY_MEMBER_INVALID"),
            (set_in("query", "disclosure_profile", "other"), "DISCLOSURE_PROFILE_INVALID"),
            (set_in("query", "query_class", "LATEST"), "QUERY_CLASS_INVALID"),
            (set_in("query", "time_basis", "WALL_CLOCK"), "TIME_BASIS_INVALID"),
            (set_in("query", "interval_semantics", "FUZZY"), "INTERVAL_SEMANTICS_INVALID"),
            (set_in("query", "point_event_semantics", "NEAR"), "POINT_EVENT_SEMANTICS_INVALID"),
            (set_in("query", "master_time", "ANY"), "MASTER_TIME_INVALID"),
            (set_in("query", "controlling_layer_id", "../layer"), "CONTROLLING_LAYER_INVALID"),
            (lambda state: state["selection"].pop("start"), "SELECTION_START_REQUIRED"),
            (set_in("selection", "selection_mode", "RANGE"), "SELECTION_MODE_INVALID"),
            (set_in("selection", "anchor", "MIDDLE"), "SELECTION_ANCHOR_INVALID"),
            (set_in("selection", "support_ref", " bad"), "SUPPORT_REF_INVALID"),
            (set_in("display", "mode", "LOOP"), "DISPLAY_MODE_INVALID"),
            (set_in("display", "step_rule", "RANDOM"), "STEP_RULE_INVALID"),
            (set_in("display", "direction", "SIDEWAYS"), "DIRECTION_INVALID"),
            (set_in("display", "missing_data_policy", "ZERO_FILL"), "MISSING_DATA_POLICY_INVALID"),
            (set_in("display", "aggregate_semantics", "MEAN"), "AGGREGATE_INVALID"),
            (set_in("display", "window_duration", ""), "WINDOW_DURATION_INVALID"),
            (set_in("display", "step_rule", "REGULAR"), "SNAPSHOT_STEP_INVALID"),
            (set_in("pins", "pin_status", "MAYBE"), "PIN_STATUS_INVALID"),
            (set_in("pins", "release_refs", "kfm:release:x"), "PIN_REFS_INVALID"),
            (lambda state: state["pins"].update(dataset_version_refs=[], release_refs=[]), "PIN_REQUIRED_FOR_PINNED"),
            (set_in("as_of", "knowledge_cutoff", "yesterday"), "INSTANT_SYNTAX_INVALID"),
        ]
        for mutate, code in cases:
            with self.subTest(code=code):
                self.assertEqual(("ERROR", code), self._query(mutate))
        unsupported = self._state()
        unsupported["as_of"]["knowledge_cutoff"] = "2024-01-02T00:00:00"
        result = normalize_temporal_query(unsupported)
        self.assertEqual(("UNSUPPORTED", "UNKNOWN_TIMEZONE"), (result.status, result.code))
        self.assertEqual(compute_query_id(unsupported), result.query_id)

    def test_display_modes_require_their_configuration(self) -> None:
        def display(**values):
            return lambda state: state["display"].update(values)
        def window(**values):
            def mutate(state: dict) -> None:
                state["display"].update(values)
                state["selection"].update(selection_mode="WINDOW", end=instant("2024-01-03T00:00:00Z"))
            return mutate
        cases = [
            (display(mode="MOVING_WINDOW", step_rule="REGULAR"), "MOVING_WINDOW_CONFIGURATION_INVALID"),
            (display(mode="ACCUMULATION"), "ACCUMULATION_SEMANTICS_REQUIRED"),
            (display(mode="EVENT_STEP", step_rule="REGULAR"), "EVENT_STEP_RULE_REQUIRED"),
            (display(mode="COMPARISON"), "COMPARISON_SIDES_REQUIRED"),
            (lambda state: (state["display"].update(mode="COMPARISON"),
                            state["comparison"].update(enabled=True, left="kfm:a", right="kfm:b", compatibility="INCOMPATIBLE")),
             "COMPARISON_INCOMPATIBLE"),
            (lambda state: state["comparison"].update(enabled=True), "COMPARISON_MODE_REQUIRED"),
        ]
        for mutate, code in cases:
            with self.subTest(code=code):
                self.assertEqual(("ERROR", code), self._query(mutate))
        for mutate in (window(mode="MOVING_WINDOW", step_rule="CALENDAR", window_duration="P7D"),
                       display(mode="ACCUMULATION", aggregate_semantics="EVENT_COUNT"),
                       display(mode="EVENT_STEP", step_rule="AVAILABLE_EVENT")):
            self.assertEqual(("SUPPORTED", "OK"), self._query(mutate))

    def test_interval_profiles_order_and_ambiguity(self) -> None:
        self.assertEqual(("ERROR", "MIXED_BOUNDARY_PROFILES"),
                         self._window(instant("2024-01-01T00:00:00Z"), {"profile": "year", "raw": "2024"}))
        self.assertEqual(("ERROR", "REVERSED_INTERVAL"),
                         self._window({"profile": "month", "raw": "2024-03"}, {"profile": "month", "raw": "2024-02"}))
        self.assertEqual(("SUPPORTED", "OK"),
                         self._window({"profile": "date_only", "raw": "2024-02-28"}, {"profile": "date_only", "raw": "2024-03-01"}))
        self.assertEqual(("UNSUPPORTED", "UNCERTAIN_ORDERING"),
                         self._window({"profile": "uncertain_range", "raw": "circa 1870"}, {"profile": "uncertain_range", "raw": "before 1880"}))
        self.assertEqual(("UNSUPPORTED", "UNSUPPORTED_PROFILE"),
                         self._window({"profile": "geologic_age", "raw": "Permian"}, {"profile": "geologic_age", "raw": "Triassic"}))

    def test_view_state_findings_accumulate_before_query_outcome(self) -> None:
        state = self._state()
        state["state_id"] = compute_state_id(state)
        self.assertEqual(("SUPPORTED", ()), validate_temporal_view_state(state))
        state.update(profile="other", schema_version="0.0.1", active_layer_ids=["a", "a"],
                     spatial_scope={"public_safe": False})
        status, findings = validate_temporal_view_state(state)
        self.assertEqual("SUPPORTED", status)
        self.assertEqual(("PROFILE_INVALID", "SCHEMA_VERSION_INVALID", "ACTIVE_LAYER_IDS_INVALID",
                          "SPATIAL_SCOPE_NOT_PUBLIC_SAFE", "STATE_ID_MISMATCH"), findings)
        state["display"]["mode"] = "LOOP"
        self.assertEqual("ERROR", validate_temporal_view_state(state)[0])
        state["display"]["mode"] = "SNAPSHOT"
        state["as_of"]["knowledge_cutoff"] = "2024-01-02T00:00:00"
        self.assertEqual("UNSUPPORTED", validate_temporal_view_state(state)[0])

    def _frame(self, state: dict, *layers: TemporalFrameLayer, **overrides) -> TemporalFrameContext:
        fields = {"state_id": compute_state_id(state), "query_id": compute_query_id(state), "selected_support": {},
                  "layers": layers, "dataset_version_refs": (), "release_refs": (), "policy_status": "CURRENT_POLICY"}
        fields.update(overrides)
        return TemporalFrameContext(**fields)

    def test_frame_context_rejects_leaks_and_unknown_states(self) -> None:
        state = self._state()
        def layer(layer_id="kfm:layer:a", **values):
            fields = {"layer_id": layer_id, "actual_time": "2024-01-01T00:00:00Z", "availability": "AVAILABLE",
                      "evidence_refs": (), "source_version_ref": None, "release_status": "RELEASED"}
            fields.update(values)
            return TemporalFrameLayer(**fields)
        cases = [
            (self._frame(state, layer(), profile="other"), "FRAME_PROFILE_INVALID"),
            (self._frame(state, layer(), outcome="DENY"), "FRAME_OUTCOME_BLOCKED"),
            (self._frame(state, layer(), layer()), "DUPLICATE_LAYER_FRAME"),
            (self._frame(state, layer(release_status="CANDIDATE")), "AVAILABLE_LAYER_INCOMPLETE"),
            (self._frame(state, layer(actual_time=None)), "AVAILABLE_LAYER_INCOMPLETE"),
            (self._frame(state, layer(availability="WITHHELD", actual_time=None, evidence_refs=("kfm:evidence:restricted",))),
             "WITHHELD_DATA_LEAK"),
            (self._frame(state, layer(availability="EXPIRED")), "NONAVAILABLE_TIME_LEAK"),
            (self._frame(state, layer(availability="PENDING")), "AVAILABILITY_INVALID"),
        ]
        for frame, code in cases:
            with self.subTest(code=code):
                self.assertEqual(("ERROR", code), validate_frame_context(frame))
        self.assertEqual(("SUPPORTED", "OK"), validate_frame_context(
            self._frame(state, layer(), layer("kfm:layer:b", availability="OUTSIDE_COVERAGE", actual_time=None), outcome="ABSTAIN")))

    def test_runtime_reducer_keeps_prior_frames_on_mismatch_and_failure(self) -> None:
        state = self._state()
        first = request_frame(state)
        self.assertEqual((1, "LOADING"), (first.generation, first.status))
        good = self._frame(state, TemporalFrameLayer("kfm:layer:a", "2024-01-01T00:00:00Z", "AVAILABLE", (), None, "RELEASED"))
        committed = commit_frame(first, 1, good)
        for frame in (self._frame(state, *good.layers, state_id="kfm:temporal-view-state:sha256:" + "0" * 64),
                      self._frame(state, *good.layers, query_id="kfm:temporal-query:sha256:" + "0" * 64)):
            self.assertIs(first, commit_frame(first, 1, frame))
        bad = commit_frame(first, 1, self._frame(state, *good.layers, profile="other"))
        self.assertEqual(("ERROR", "FRAME_PROFILE_INVALID", None), (bad.status, bad.error_code, bad.committed_frame))
        idle = create_runtime_state()
        self.assertIs(idle, commit_frame(idle, 0, good))

        broken = self._state()
        broken["display"]["mode"] = "LOOP"
        second = request_frame(broken, committed)
        self.assertEqual((2, "ERROR", "DISPLAY_MODE_INVALID"), (second.generation, second.status, second.error_code))
        self.assertIs(good, second.committed_frame)
        self.assertIs(second, fail_frame(second, 1, "LATE"))
        failed = fail_frame(second, 2, "RENDER_FAILED")
        self.assertEqual(("ERROR", "RENDER_FAILED"), (failed.status, failed.error_code))
        self.assertIs(good, failed.committed_frame)


if __name__ == "__main__":
    unittest.main()
