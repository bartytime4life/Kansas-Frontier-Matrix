from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_domain_layer_descriptor.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_domain_layer_descriptor_validator", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fixture_polarity_is_executable_and_fail_closed():
    module = _load_module()
    assert module.main(["--fixtures"]) == 0


def test_no_input_fails_closed():
    module = _load_module()
    assert module.main([]) == 2


def test_fixture_mode_rejects_explicit_candidates(capsys):
    module = _load_module()
    candidate = (
        module.FIXTURES / "valid" / "public_safe_historical_aggregate.json"
    )
    assert candidate.is_file()

    assert module.main(["--fixtures", str(candidate)]) == 2
    assert (
        "Cannot combine --fixtures with explicit DomainLayerDescriptor files"
        in capsys.readouterr().err
    )
