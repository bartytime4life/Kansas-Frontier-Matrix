#!/usr/bin/env python3
"""Validate EvidenceTemporalPostureAssessment records without network access.

The validator preserves the legacy evidence-side record shape and diagnostics
while assigning a distinct evidence responsibility. It creates no common-envelope,
SourceDescriptor, evidence, policy, review, lifecycle, release, or publication
authority.
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
CANONICAL_SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/evidence_temporal_posture_assessment"


def _dt(value: object) -> datetime | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("date-time value must be a string or null")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _validation_now(explicit: datetime | None = None) -> datetime:
    if explicit is not None:
        return explicit
    configured = os.environ.get("KFM_VALIDATION_NOW")
    if configured:
        parsed = _dt(configured)
        if parsed is None:
            raise ValueError("KFM_VALIDATION_NOW must be a date-time")
        return parsed
    return datetime.now(timezone.utc)


def validate_doc(
    doc: Mapping[str, object],
    *,
    schema_path: Path = CANONICAL_SCHEMA,
    now: datetime | None = None,
) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = [
        error.message
        for error in Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(doc)
    ]
    if errors:
        return errors

    times = doc["times"]
    assert isinstance(times, Mapping)
    valid_from, valid_to = _dt(times["valid_from"]), _dt(times["valid_to"])
    source_updated, retrieved = _dt(times["source_updated_at"]), _dt(times["retrieved_at"])
    released, corrected = _dt(times["released_at"]), _dt(times["corrected_at"])

    if valid_from and valid_to and valid_from > valid_to:
        errors.append("valid_from must not exceed valid_to")
    if source_updated and retrieved and source_updated > retrieved:
        errors.append("source_updated_at must not exceed retrieved_at")
    if released and retrieved and released < retrieved:
        errors.append("released_at must not precede retrieved_at")
    if corrected and (not released or corrected < released):
        errors.append("corrected_at requires and must not precede released_at")
    if doc["temporal_posture"] == "SUPERSEDED" and not doc.get("supersedes_ref"):
        errors.append("SUPERSEDED requires supersedes_ref")
    if doc["temporal_posture"] == "WITHDRAWN" and not doc.get("withdrawal_ref"):
        errors.append("WITHDRAWN requires withdrawal_ref")
    freshness_deadline = _dt(doc["freshness_deadline"])
    if (
        doc["temporal_posture"] == "CURRENT"
        and freshness_deadline
        and freshness_deadline < _validation_now(now)
    ):
        errors.append("CURRENT envelope freshness_deadline is elapsed")
    return errors


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
