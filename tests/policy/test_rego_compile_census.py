"""Every tracked Rego module must compile under the installed OPA.

The census compiles all tracked ``.rego`` files together, so a module that
conflicts with another (two ``default`` rules for one package rule, for example)
fails as it would in a single bundle. The only tolerated error is the disclosed
duplicate ``living_person_redaction.rego`` pair, which is CONFLICTED / HOLD in
``docs/policy/living_persons_geoprivacy.md`` and must not be resolved by a test.
A pass proves compilation only, not policy correctness or runtime binding.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
# Disclosed CONFLICTED / HOLD pair; each copy compiles alone.
TOLERATED_DUPLICATE = (
    "policy/domains/people-dna-land/living_person_redaction.rego",
    "policy/sensitivity/living_person_redaction.rego",
)


def _opa_binary() -> str:
    binary = os.environ.get("OPA_BIN") or shutil.which("opa")
    if not binary:
        pytest.skip("OPA_BINARY_UNAVAILABLE: install opa or set OPA_BIN to compile the Rego")
    return binary


def _rego_files() -> list[str]:
    completed = subprocess.run(["git", "ls-files", "-z", "*.rego"], cwd=ROOT,
                               capture_output=True, check=True)
    return sorted(p for p in completed.stdout.decode("utf-8").split("\0") if p)


def _check(paths: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([_opa_binary(), "check", "--format", "json", *paths], cwd=ROOT,
                          capture_output=True, text=True, timeout=120, check=False)


def _errors(completed: subprocess.CompletedProcess[str]) -> list[dict]:
    if completed.returncode == 0:
        return []
    payload = json.loads(completed.stdout or completed.stderr)
    errors = payload.get("errors", [])
    assert errors, f"opa check failed without reporting errors: {completed.stderr}"
    return errors


def _is_tolerated(error: dict) -> bool:
    message = error.get("message", "")
    return (error.get("location", {}).get("file") in TOLERATED_DUPLICATE
            and "data.kfm.living_person_redaction." in message
            and all(path in message for path in TOLERATED_DUPLICATE))


def test_tracked_rego_compiles_except_the_disclosed_duplicate():
    paths = _rego_files()
    assert paths, "expected tracked Rego modules"
    unexpected = [f"{e.get('location', {}).get('file')}: {e.get('code')}: {e.get('message')}"
                  for e in _errors(_check(paths)) if not _is_tolerated(e)]
    assert not unexpected, "\n".join(unexpected)


@pytest.mark.parametrize("path", TOLERATED_DUPLICATE)
def test_each_disclosed_duplicate_compiles_alone(path: str):
    completed = _check([path])
    assert completed.returncode == 0, completed.stderr
