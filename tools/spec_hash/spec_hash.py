#!/usr/bin/env python3
"""Repository wrapper for the reusable KFM hashing package."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(PACKAGE_SRC))

from hashing.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
