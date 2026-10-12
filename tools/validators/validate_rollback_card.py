#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical release RollbackCard validator.

The reviewed implementation lives at
``tools/validators/release/validate_rollback_card.py``.  This historical path
keeps existing callers working by delegating to that implementation rather
than maintaining a second validator or creating a parallel authority surface.

A passing result remains bounded candidate-shape and local-consistency evidence
only. It does not execute rollback, authorize release mutation, erase history,
or publish.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.release.validate_rollback_card import main as _canonical_main  # noqa: E402


def main(argv: Sequence[str] | None = None) -> int:
    """Delegate to the canonical release RollbackCard validator."""

    return _canonical_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
