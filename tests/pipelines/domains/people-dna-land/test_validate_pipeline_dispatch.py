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


def test_dispatches_to_existing_domain_validator(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["evidence-bundle", "synthetic.json"]) == 0
    assert calls == [
        (
            [
                sys.executable,
                str(module.VALIDATORS["evidence-bundle"]),
                "synthetic.json",
            ],
            module.REPO_ROOT,
            False,
        )
    ]


def test_dispatches_consent_overlay_with_required_manifest(monkeypatch):
    module = _load_module()
    calls = []

    def fake_run(command, *, cwd, check):
        calls.append((command, cwd, check))
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    argv = [
        "consent-overlay",
        "--revocation-manifest",
        "synthetic-revocations.json",
        "synthetic-overlay.json",
    ]
    assert module.main(argv) == 0
    assert calls == [
        (
            [
                sys.executable,
                str(module.VALIDATORS["consent-overlay"]),
                "--revocation-manifest",
                "synthetic-revocations.json",
                "synthetic-overlay.json",
            ],
            module.REPO_ROOT,
            False,
        )
    ]


def test_preserves_fail_closed_child_return_code(monkeypatch):
    module = _load_module()

    monkeypatch.setattr(
        module.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=1),
    )

    assert module.main(["living-person", "--fixtures"]) == 1


def test_missing_validator_fails_closed_without_execution(monkeypatch, tmp_path):
    module = _load_module()
    monkeypatch.setitem(module.VALIDATORS, "schema", tmp_path / "missing.py")

    def should_not_run(*args, **kwargs):
        raise AssertionError("subprocess must not run for a missing validator")

    monkeypatch.setattr(module.subprocess, "run", should_not_run)

    assert module.main(["schema"]) == 2


def test_double_dash_separator_is_not_forwarded(monkeypatch):
    module = _load_module()
    seen = {}

    def fake_run(command, *, cwd, check):
        seen["command"] = command
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(module.subprocess, "run", fake_run)

    assert module.main(["source-descriptor", "--", "candidate.json"]) == 0
    assert seen["command"][-1] == "candidate.json"
    assert "--" not in seen["command"]
