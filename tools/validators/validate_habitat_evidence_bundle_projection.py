#!/usr/bin/env python3
"""Compatibility entrypoint for the Habitat EvidenceBundle projection validator.

The domain-owned implementation is authoritative for argument handling and path
resolution. This wrapper preserves the schema-declared historical command
without introducing a second validation implementation or evidence authority.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.habitat.validate_evidence_bundle import (  # noqa: E402
    main as validate_habitat_evidence_bundle,
)


def main(argv: Sequence[str] | None = None) -> int:
    """Delegate unchanged arguments to the domain-owned validator."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return validate_habitat_evidence_bundle(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
