#!/usr/bin/env python3
"""Compatibility entry point for the canonical RollbackCard validator."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.release.validate_rollback_card import main


if __name__ == "__main__":
    raise SystemExit(main())
