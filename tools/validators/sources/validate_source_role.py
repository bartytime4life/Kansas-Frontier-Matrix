#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical source-role validator.

`tools/validators/sources/` remains a plural compatibility lane. All behavior is
delegated to `tools/validators/source_role/validate_source_role.py`; this file
must not define a second vocabulary, schema, outcome grammar, or validator.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.source_role.validate_source_role import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
