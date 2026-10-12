"""Negative-path tests for MapLibre performance governance fixture validation."""

from tests.maplibre.perf_fixture_builder import build_perf_fixture, validate_fixture


def test_rejects_zero_frame_budget() -> None:
    fixture = build_perf_fixture(frame_budget_ms=0)
    errors = validate_fixture(fixture)

    assert "frame_budget_ms must be > 0" in errors


def test_rejects_negative_memory_budget() -> None:
    fixture = build_perf_fixture(memory_budget_mb=-1)
    errors = validate_fixture(fixture)

    assert "memory_budget_mb must be > 0" in errors


def test_rejects_out_of_range_tile_error_rate() -> None:
    fixture = build_perf_fixture(tile_error_rate=1.5)
    errors = validate_fixture(fixture)

    assert "tile_error_rate must be between 0 and 1" in errors
