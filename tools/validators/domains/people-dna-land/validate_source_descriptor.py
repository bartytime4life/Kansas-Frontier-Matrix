#!/usr/bin/env python3
"""Validate People/DNA/Land SourceDescriptor candidates via shared source authority.

This domain entrypoint delegates to the repository's shared SourceDescriptor
validator and therefore inherits the existing schema and deterministic fixture
polarity. Validation checks shape only. It does not admit or activate a source,
retrieve source payloads, decide rights, consent, sensitivity, or authority,
promote lifecycle state, release, publish, or wire Explorer/runtime behavior.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.sources.validate_source_descriptor import main as _shared_main  # noqa: E402


def main(argv: Sequence[str] | None = None) -> int:
    """Run the shared SourceDescriptor validator through the People/DNA/Land seam."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return _shared_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
