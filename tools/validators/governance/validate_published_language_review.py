#!/usr/bin/env python3
"""Compatibility entry point for the PublishedLanguageReview validator."""
from tools.validators.governance.published_language_review import *  # noqa: F401,F403

if __name__ == "__main__":
    raise SystemExit(main())
