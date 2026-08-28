from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_PATCH_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR_PATH = (
    REPO_PATCH_ROOT
    / "tools"
    / "validators"
    / "docs"
    / "meta-block"
    / "check_meta_blocks.py"
)
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "valid_repo"

spec = importlib.util.spec_from_file_location("kfm_docs_meta_block", VALIDATOR_PATH)
if spec is None or spec.loader is None:  # pragma: no cover
    raise RuntimeError("could not load docs meta-block validator")
meta_block = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = meta_block
spec.loader.exec_module(meta_block)


class DocsMetaBlockTestCase(unittest.TestCase):
    maxDiff = None

    def _copy_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "repo"
        shutil.copytree(FIXTURE_ROOT, root)
        return temporary, root

    def _validate(
        self,
        root: Path,
        *,
        profile: str = meta_block.PROFILE_PRESENT,
        registry: bool = True,
        git_diff: str | None = None,
        warnings_as_errors: bool = False,
    ):
        return meta_block.validate_meta_blocks(
            repo_root=root,
            inputs=("README.md", "docs"),
            profile=profile,
            registry_path=(
                "control_plane/document_registry.yaml" if registry else None
            ),
            git_diff=git_diff,
            warnings_as_errors=warnings_as_errors,
        )

    @staticmethod
    def _codes(result) -> set[str]:
        return {item.code for item in result.findings}

    @staticmethod
    def _git(root: Path, *args: str) -> str:
        run = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return run.stdout.strip()

    def _init_git(self, root: Path) -> str:
        self._git(root, "init", "-q")
        self._git(root, "config", "user.email", "fixture@example.invalid")
        self._git(root, "config", "user.name", "Fixture")
        self._git(root, "add", ".")
        self._git(root, "commit", "-qm", "fixture base")
        return self._git(root, "rev-parse", "HEAD")
