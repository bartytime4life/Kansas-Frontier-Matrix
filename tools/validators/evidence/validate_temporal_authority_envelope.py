#!/usr/bin/env python3
"""Compatibility entry point for legacy evidence TemporalAuthorityEnvelope records.

The unchanged legacy schema and identifier grammar are loaded explicitly. The
validation engine is the canonical EvidenceTemporalPostureAssessment validator;
no common TemporalAuthorityEnvelope conformance or translation is implied.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

MODULE_ROOT = Path(__file__).resolve().parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from validate_evidence_temporal_posture_assessment import (  # noqa: E402
    validate_doc as _validate_assessment,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
LEGACY_SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"


def validate_doc(doc: Mapping[str, object], *, now: datetime | None = None) -> list[str]:
    return _validate_assessment(doc, schema_path=LEGACY_SCHEMA, now=now)


def validate_file(path: Path, *, now: datetime | None = None) -> list[str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        return ["input root must be an object"]
    return validate_doc(value, now=now)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    errors = validate_file(args.file)
    if errors:
        for error in errors:
            print(error, file=os.sys.stderr)
        return 1
    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
