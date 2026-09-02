"""Deterministic, no-I/O selector for prevalidated mock response envelopes.

This bounded proof adapter does not interpret a request, choose an outcome,
validate schema semantics, call a model, resolve evidence, evaluate policy, or
emit a receipt. Its caller supplies a complete synthetic scenario matrix that
has been validated by the owning contract/schema lane. The adapter only
returns isolated copies so tests can exercise the four finite runtime outcomes
without provider, filesystem, network, clock, randomness, or secret access.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy


FINITE_OUTCOMES = ("ANSWER", "ABSTAIN", "DENY", "ERROR")


class MockAdapterConfigurationError(ValueError):
    """Raised when a synthetic scenario matrix is incomplete or malformed."""


class MockAdapterScenarioError(LookupError):
    """Raised when a caller requests a scenario that is not registered."""


class MockAdapter:
    """Select isolated finite-outcome envelopes from a fixed scenario matrix."""

    def __init__(
        self,
        scenarios: Mapping[str, Mapping[str, object]],
    ) -> None:
        if not isinstance(scenarios, Mapping) or not scenarios:
            raise MockAdapterConfigurationError(
                "scenario matrix must be a non-empty mapping"
            )

        prepared: dict[str, dict[str, object]] = {}
        observed_outcomes: set[str] = set()
        for scenario_id, envelope in scenarios.items():
            if not isinstance(scenario_id, str) or not scenario_id.strip():
                raise MockAdapterConfigurationError(
                    "scenario identifiers must be non-empty strings"
                )
            if not isinstance(envelope, Mapping):
                raise MockAdapterConfigurationError(
                    "scenario envelopes must be mappings"
                )

            outcome = envelope.get("outcome")
            if outcome not in FINITE_OUTCOMES:
                raise MockAdapterConfigurationError(
                    "scenario envelope outcome is outside the finite set"
                )

            prepared[scenario_id] = deepcopy(dict(envelope))
            observed_outcomes.add(outcome)

        if observed_outcomes != set(FINITE_OUTCOMES):
            raise MockAdapterConfigurationError(
                "scenario matrix must cover every finite outcome"
            )

        self._scenarios = prepared

    @property
    def scenario_ids(self) -> tuple[str, ...]:
        """Return registered scenario identifiers in deterministic order."""

        return tuple(sorted(self._scenarios))

    @property
    def outcomes(self) -> tuple[str, ...]:
        """Return the closed runtime outcome vocabulary."""

        return FINITE_OUTCOMES

    def respond(self, scenario_id: str) -> dict[str, object]:
        """Return an isolated envelope copy for one registered scenario."""

        try:
            envelope = self._scenarios[scenario_id]
        except (KeyError, TypeError):
            raise MockAdapterScenarioError(
                "requested scenario is not registered"
            ) from None
        return deepcopy(envelope)
