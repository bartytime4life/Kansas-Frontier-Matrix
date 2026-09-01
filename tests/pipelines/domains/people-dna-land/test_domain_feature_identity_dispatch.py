from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = REPO_ROOT / "pipelines/domains/people-dna-land/validate.py"


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "people_dna_land_pipeline_validate", MODULE_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_dispatches_domain_feature_identity_fixture_replay(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["domain-feature-identity", "--fixtures"]) == 0
    assert calls == [
        (
            [
                sys.executable,
                str(module.VALIDATORS["domain-feature-identity"]),
                "--fixtures",
            ],
            module.REPO_ROOT,
            False,
        )
    ]
