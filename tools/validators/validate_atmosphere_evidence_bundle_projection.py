#!/usr/bin/env python3
"""Compatibility entrypoint for the Atmosphere EvidenceBundle projection."""

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.atmosphere.validate_evidence_bundle import (  # noqa: E402
    main,
)

if __name__ == "__main__":
    raise SystemExit(main())
