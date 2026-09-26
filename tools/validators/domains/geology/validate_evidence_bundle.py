#!/usr/bin/env python3
"""Compatibility entrypoint for the Geology EvidenceBundle projection validator.

The domain-owned implementation at ``validate_schema.py`` is authoritative for
argument handling and path resolution (see
``tests/validators/domains/geology/test_evidence_bundle_schema_convergence.py``).
This wrapper preserves the conventionally-named entrypoint without introducing
a second validation implementation or evidence authority.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.geology.validate_schema import (  # noqa: E402
    main as validate_geology_evidence_bundle,
)


def main(argv: Sequence[str] | None = None) -> int:
    """Delegate unchanged arguments to the domain-owned validator."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return validate_geology_evidence_bundle(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
