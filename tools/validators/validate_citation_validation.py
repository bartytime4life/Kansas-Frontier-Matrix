#!/usr/bin/env python3
"""Compatibility entry point for the citation validation report profile."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.citation.validate_citation_validation_report import main


if __name__ == "__main__":
    raise SystemExit(main())
