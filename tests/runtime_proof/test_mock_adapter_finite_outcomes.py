"""Proof for the deterministic, fixture-backed finite-outcome MockAdapter.

The canonical RuntimeResponseEnvelope validator owns complete shape semantics.
This suite proves the smaller adapter responsibility: accept a prevalidated
synthetic scenario matrix, require all four outcomes, return deterministic
isolated copies, fail closed for unknown scenarios, and import no I/O surface.
"""
from __future__ import annotations

import ast
from copy import deepcopy
import json
from pathlib import Path
import unittest

from runtime.model_adapters.MockAdapter import (
    FINITE_OUTCOMES,
    MockAdapter,
    MockAdapterConfigurationError,
    MockAdapterScenarioError,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_PATH = REPOSITORY_ROOT / "runtime/model_adapters/MockAdapter.py"
VALID_FIXTURE_ROOT = (
    REPOSITORY_ROOT
    / "fixtures/contracts/v1/runtime/runtime_response_envelope/valid"
)


def _load_scenarios() -> dict[str, dict[str, object]]:
    scenarios: dict[str, dict[str, object]] = {}
    for path in sorted(VALID_FIXTURE_ROOT.glob("valid_*.json")):
        envelope = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(envelope, dict):
            raise AssertionError(f"expected object fixture: {path}")
        outcome = envelope.get("outcome")
        if not isinstance(outcome, str):
            raise AssertionError(f"expected string outcome: {path}")
        scenarios[f"fixture-{outcome.lower()}"] = envelope
    return scenarios


class MockAdapterFiniteOutcomeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = _load_scenarios()

    def test_fixture_matrix_covers_every_finite_outcome(self) -> None:
        adapter = MockAdapter(self.scenarios)

        self.assertEqual(adapter.outcomes, FINITE_OUTCOMES)
        self.assertEqual(
            {adapter.respond(name)["outcome"] for name in adapter.scenario_ids},
            set(FINITE_OUTCOMES),
        )
        self.assertEqual(adapter.scenario_ids, tuple(sorted(self.scenarios)))

    def test_repeated_responses_are_equal_but_isolated(self) -> None:
        adapter = MockAdapter(self.scenarios)

        first = adapter.respond("fixture-answer")
        second = adapter.respond("fixture-answer")

        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        first["outcome"] = "ERROR"
        self.assertEqual(adapter.respond("fixture-answer")["outcome"], "ANSWER")

    def test_constructor_isolates_registered_scenarios(self) -> None:
        original = deepcopy(self.scenarios)
        adapter = MockAdapter(self.scenarios)

        self.scenarios["fixture-answer"]["outcome"] = "ERROR"

        self.assertEqual(adapter.respond("fixture-answer"), original["fixture-answer"])

    def test_incomplete_or_unknown_outcome_matrix_fails_closed(self) -> None:
        incomplete = deepcopy(self.scenarios)
        incomplete.pop("fixture-deny")
        with self.assertRaisesRegex(
            MockAdapterConfigurationError,
            "cover every finite outcome",
        ):
            MockAdapter(incomplete)

        unknown = deepcopy(self.scenarios)
        unknown["fixture-answer"]["outcome"] = "WAITING"
        with self.assertRaisesRegex(
            MockAdapterConfigurationError,
            "outside the finite set",
        ):
            MockAdapter(unknown)

    def test_malformed_configuration_fails_closed(self) -> None:
        with self.assertRaises(MockAdapterConfigurationError):
            MockAdapter({})

        malformed_id = deepcopy(self.scenarios)
        malformed_id[""] = malformed_id.pop("fixture-error")
        with self.assertRaisesRegex(
            MockAdapterConfigurationError,
            "identifiers must be non-empty strings",
        ):
            MockAdapter(malformed_id)

        malformed_envelope = deepcopy(self.scenarios)
        malformed_envelope["fixture-error"] = []  # type: ignore[assignment]
        with self.assertRaisesRegex(
            MockAdapterConfigurationError,
            "envelopes must be mappings",
        ):
            MockAdapter(malformed_envelope)

    def test_unknown_scenario_error_does_not_echo_input(self) -> None:
        adapter = MockAdapter(self.scenarios)
        untrusted = "secret-like-scenario-value"

        with self.assertRaises(MockAdapterScenarioError) as captured:
            adapter.respond(untrusted)

        self.assertNotIn(untrusted, str(captured.exception))

    def test_adapter_source_has_no_io_or_dynamic_execution_surface(self) -> None:
        source = ADAPTER_PATH.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(ADAPTER_PATH))
        imported_roots: set[str] = set()
        called_names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(
                    alias.name.split(".", 1)[0] for alias in node.names
                )
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                called_names.add(node.func.id)

        self.assertLessEqual(
            imported_roots,
            {"__future__", "collections", "copy"},
        )
        self.assertTrue(
            called_names.isdisjoint(
                {"open", "exec", "eval", "compile", "input", "__import__"}
            )
        )


if __name__ == "__main__":
    unittest.main()
