from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path


REPO_PATCH_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR_DIR = REPO_PATCH_ROOT / "tools" / "validators" / "docs" / "stale-scan"
VALIDATOR_PATH = VALIDATOR_DIR / "check_stale_docs.py"
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "valid_repo"


def load_validator():
    spec = importlib.util.spec_from_file_location("kfm_stale_scan", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load stale-scan validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def copy_fixture() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    temporary = tempfile.TemporaryDirectory()
    root = Path(temporary.name) / "repo"
    shutil.copytree(FIXTURE_ROOT, root)
    return temporary, root
