from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = REPO_ROOT / "pipelines/domains/people-dna-land/rollback.py"


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_pipeline_rollback", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fixture_mode_delegates_to_revocation_assessment(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["--fixtures"]) == 0
    assert calls == [
        (
            [
                sys.executable,
                str(module.ASSESSMENT_VALIDATOR),
                "--fixtures",
            ],
            module.REPO_ROOT,
            False,
        )
    ]


def test_input_mode_forwards_only_local_assessment_path(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["--input", "synthetic-assessment.json"]) == 0
    assert calls[0][0][-2:] == ["--input", "synthetic-assessment.json"]


def test_preserves_fail_closed_child_return_code(monkeypatch):
    module = _load_module()
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=1),
    )

    assert module.main(["--fixtures"]) == 1


def test_missing_validator_fails_closed_without_execution(monkeypatch, tmp_path):
    module = _load_module()
    monkeypatch.setattr(module, "ASSESSMENT_VALIDATOR", tmp_path / "missing.py")

    def should_not_run(*args, **kwargs):
        raise AssertionError("subprocess must not run for a missing validator")

    monkeypatch.setattr(module.subprocess, "run", should_not_run)

    assert module.main(["--fixtures"]) == 2


@pytest.mark.parametrize("exact", ("--fixtures", "--input"))
def test_assessment_modes_reject_abbreviated_option_names(exact):
    module = _load_module()

    for length in range(3, len(exact)):
        option = exact[:length]
        with pytest.raises(SystemExit) as exc:
            module.main([option])
        assert exc.value.code == 2


def test_operational_execute_flag_is_not_supported():
    module = _load_module()

    with pytest.raises(SystemExit) as exc:
        module.main(["--execute"])

    assert exc.value.code == 2
