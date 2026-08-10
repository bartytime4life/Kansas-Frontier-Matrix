from __future__ import annotations

import importlib

import pytest


CASES = (
    (
        "tools.validators.validate_layer_manifest",
        "tools.validators.data.validate_layer_manifest",
    ),
    (
        "tools.validators.validate_release_manifest",
        "tools.validators.release.validate_release_manifest",
    ),
)


@pytest.mark.parametrize(("compatibility_name", "canonical_name"), CASES)
def test_compatibility_entrypoint_delegates_without_forking_semantics(
    compatibility_name: str,
    canonical_name: str,
) -> None:
    compatibility = importlib.import_module(compatibility_name)
    canonical = importlib.import_module(canonical_name)
    assert compatibility.main is canonical.main


@pytest.mark.parametrize(("compatibility_name", "canonical_name"), CASES)
def test_compatibility_entrypoint_replays_canonical_fixtures(
    compatibility_name: str,
    canonical_name: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    compatibility = importlib.import_module(compatibility_name)
    canonical = importlib.import_module(canonical_name)
    assert compatibility.main ["--fixtures"] == 0
    assert capsys.readouterr().out
