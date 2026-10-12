#!/usr/bin/env python3
"""Validate SourceDescriptor candidates through the declared plural schema path.

This compatibility entrypoint resolves repository paths from this file and
delegates to the shared local JSON Schema runner. The plural schema is a
non-authoritative alias of the rich singular SourceDescriptor implementation.
Validation does not admit or activate a source, decide rights or sensitivity,
evaluate policy, resolve evidence, promote lifecycle state, or publish.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.jsonschema_runner import run  # noqa: E402


SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/sources/source_descriptor.schema.json"
FIXTURES_DIR = REPO_ROOT / "fixtures/contracts/v1/source/source_descriptor"


def main(argv: Sequence[str] | None = None) -> int:
    """Run the declared SourceDescriptor compatibility validator."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return run(SCHEMA_PATH, FIXTURES_DIR, arguments)


if __name__ == "__main__":
    raise SystemExit(main())
