#!/usr/bin/env python3
"""Validate the Habitat projection of the shared EvidenceBundle shape.

This domain entrypoint delegates structural validation to KFM's shared JSON
Schema runner. It does not define independent evidence semantics, establish
Habitat truth, clear sensitivity or geoprivacy review, or authorize policy,
release, publication, or species-occurrence claims.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.jsonschema_runner import run  # noqa: E402


SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/habitat/evidence_bundle.schema.json"
FIXTURES_DIR = REPO_ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"


def main(argv: Sequence[str] | None = None) -> int:
    """Run shared shape validation for explicit files or the fixture profile."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    return run(SCHEMA_PATH, FIXTURES_DIR, arguments)


if __name__ == "__main__":
    raise SystemExit(main())
