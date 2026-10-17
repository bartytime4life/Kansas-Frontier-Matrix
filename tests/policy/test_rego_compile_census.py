"""Every tracked Rego module must compile under the installed OPA.

The census compiles all tracked ``.rego`` files together, so a module that
conflicts with another (two ``default`` rules for one package rule, for example)
fails as it would in a single bundle. No conflict is tolerated: the former
duplicate ``living_person_redaction.rego`` pair was resolved on 2026-10-15 by
keeping ``policy/sensitivity/living_person_redaction.rego`` and retiring the
``policy/domains/people-dna-land/`` copy.
A pass proves compilation only, not policy correctness or runtime binding.
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
RETAINED_LIVING_PERSON_REDACTION = "policy/sensitivity/living_person_redaction.rego"
RETIRED_LIVING_PERSON_REDACTION = "policy/domains/people-dna-land/living_person_redaction.rego"


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


def test_tracked_rego_compiles_as_one_bundle():
    paths = _rego_files()
    assert paths, "expected tracked Rego modules"
    completed = _check(paths)
    assert completed.returncode == 0, completed.stdout or completed.stderr


def test_living_person_redaction_has_one_tracked_home():
    paths = _rego_files()
    assert RETAINED_LIVING_PERSON_REDACTION in paths
    assert RETIRED_LIVING_PERSON_REDACTION not in paths
