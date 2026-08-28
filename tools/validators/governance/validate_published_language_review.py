#!/usr/bin/env python3
"""Compatibility entry point for the PublishedLanguageReview validator."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.governance.published_language_review import *  # noqa: E402,F401,F403

if __name__ == "__main__":
    raise SystemExit(main())
