#!/usr/bin/env python3
"""Compatibility entry point for the canonical KFM validator orchestrator.

The canonical implementation and registry live at ``tools/validate_all.py``.
This path remains as a compatibility delegate for existing Makefile and CI
callers; it must not acquire a second registry or divergent exit semantics.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validate_all import main as orchestrator_main  # noqa: E402


def main(argv: Sequence[str] | None = None) -> int:
    forwarded = list(argv) if argv is not None else sys.argv[1:]
    if not forwarded:
        forwarded = ["--profile", "core"]
    return orchestrator_main(forwarded, repo_root=REPO_ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
