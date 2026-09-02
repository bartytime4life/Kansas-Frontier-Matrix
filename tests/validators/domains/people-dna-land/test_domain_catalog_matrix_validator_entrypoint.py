from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = (
    REPO_ROOT / "tools/validators/domains/people-dna-land/validate_catalog_matrix.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_catalog_matrix_validator", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_delegates_fixture_replay_without_network_or_rewrite(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["--fixtures"]) == 0
    assert calls == [
        (
            [sys.executable, str(module.SHARED_VALIDATOR), "--fixtures"],
            module.REPO_ROOT,
            False,
        )
    ]


def test_delegates_candidate_path_exactly(monkeypatch):
    module = _load_module()
    seen = {}

    def fake_run(command, *, cwd, check):
        seen["command"] = command
        seen["cwd"] = cwd
        seen["check"] = check
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["synthetic-catalog-closure.json"]) == 0
    assert seen == {
        "command": [
            sys.executable,
            str(module.SHARED_VALIDATOR),
            "synthetic-catalog-closure.json",
        ],
        "cwd": module.REPO_ROOT,
        "check": False,
    }


def test_preserves_shared_validator_failure(monkeypatch):
    module = _load_module()
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=1),
    )

    assert module.main(["synthetic-catalog-closure.json"]) == 1


def test_missing_shared_validator_fails_closed(monkeypatch, tmp_path):
    module = _load_module()
    monkeypatch.setattr(module, "SHARED_VALIDATOR", tmp_path / "missing.py")

    def should_not_run(*args, **kwargs):
        raise AssertionError("subprocess must not run for a missing validator")

    monkeypatch.setattr(module.subprocess, "run", should_not_run)

    assert module.main(["--fixtures"]) == 2


def test_fixture_mode_rejects_explicit_candidates(monkeypatch, capsys):
    module = _load_module()

    def should_not_run(*args, **kwargs):
        raise AssertionError("subprocess must not run for mixed validation modes")

    monkeypatch.setattr(module.subprocess, "run", should_not_run)

    assert module.main(["--fixtures", "explicit-candidate.json"]) == 2
    assert (
        "Cannot combine --fixtures with explicit CatalogMatrix files"
        in capsys.readouterr().err
    )
