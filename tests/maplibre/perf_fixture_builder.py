"""Utilities for building MapLibre performance-governance fixtures for tests."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PerfGovernanceFixture:
    """Represents a minimal governance payload used by policy tests."""

    frame_budget_ms: float
    memory_budget_mb: float
    tile_error_rate: float


DEFAULT_BUDGET = PerfGovernanceFixture(
    frame_budget_ms=16.67,
    memory_budget_mb=512.0,
    tile_error_rate=0.01,
)


def build_perf_fixture(
    *,
    frame_budget_ms: float = DEFAULT_BUDGET.frame_budget_ms,
    memory_budget_mb: float = DEFAULT_BUDGET.memory_budget_mb,
    tile_error_rate: float = DEFAULT_BUDGET.tile_error_rate,
) -> PerfGovernanceFixture:
    """Build a fixture object for MapLibre performance governance tests."""

    return PerfGovernanceFixture(
        frame_budget_ms=frame_budget_ms,
        memory_budget_mb=memory_budget_mb,
        tile_error_rate=tile_error_rate,
    )


def validate_fixture(fixture: PerfGovernanceFixture) -> list[str]:
    """Return validation errors for negative-path assertions."""

    errors: list[str] = []

    if fixture.frame_budget_ms <= 0:
        errors.append("frame_budget_ms must be > 0")
    if fixture.memory_budget_mb <= 0:
        errors.append("memory_budget_mb must be > 0")
    if not 0 <= fixture.tile_error_rate <= 1:
        errors.append("tile_error_rate must be between 0 and 1")

    return errors
