"""Long parametrize values get bounded, stable, unique test IDs (see tests/conftest.py)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

CONFTEST = Path(__file__).resolve().parents[1] / "conftest.py"
spec = importlib.util.spec_from_file_location("kfm_tests_conftest", CONFTEST)
assert spec and spec.loader
conftest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conftest)


def test_short_values_keep_pytest_default_ids() -> None:
    for value in ("", "x" * conftest.MAX_PARAMETER_ID_CHARACTERS, b"binary", 7, None, (1, 2)):
        assert conftest.short_parameter_id(value) is None


def test_long_values_get_bounded_stable_unique_ids() -> None:
    big = "x" * (4 * 1024 * 1024)
    ids = {conftest.short_parameter_id(v) for v in (big, big[:-1] + "y", b"a" * 2_000_000, bytearray(b"a" * 70))}
    assert len(ids) == 4
    assert all(len(i) <= 40 for i in ids)
    assert conftest.short_parameter_id(big) == conftest.short_parameter_id("x" * (4 * 1024 * 1024))
    assert conftest.short_parameter_id(big).startswith("str4194304-")


@pytest.mark.parametrize("value", ["a" * 100_000])
def test_hook_is_applied_to_collected_ids(request, value) -> None:
    assert len(request.node.nodeid) < 200
    assert "str100000-" in request.node.nodeid
