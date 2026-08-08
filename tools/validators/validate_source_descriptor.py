#!/usr/bin/env python3
"""Validate SourceDescriptor candidates against the canonical v1 schema.

The entrypoint resolves repository paths from this file rather than from the
caller's working directory. It performs local schema validation only; it does
not fetch sources, activate connectors, decide rights or sensitivity, promote
lifecycle state, or publish.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.jsonschema_runner import run  # noqa: E402


SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
FIXTURES_DIR = REPO_ROOT / "fixtures/contracts/v1/source/source_descriptor"


def main(argv: Sequence[str] | None = None) -> int:
    """Run SourceDescriptor validation with repository-anchored paths."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return run(SCHEMA_PATH, FIXTURES_DIR, arguments)


if __name__ == "__main__":
    raise SystemExit(main())
