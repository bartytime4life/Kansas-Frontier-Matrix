from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = REPO_ROOT / "pipelines/domains/people-dna-land/validate.py"


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_pipeline_validate_correction_notice", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_dispatches_correction_notice_fixture_replay(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["correction-notice", "--fixtures"]) == 0
    assert calls == [
        (
            [
                sys.executable,
                str(module.VALIDATORS["correction-notice"]),
                "--fixtures",
            ],
            module.REPO_ROOT,
            False,
        )
    ]


def test_preserves_correction_notice_failure(monkeypatch):
    module = _load_module()
    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=1),
    )

    assert module.main(["correction-notice", "synthetic-invalid.json"]) == 1
