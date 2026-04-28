#!/usr/bin/env python3
"""Fail-closed validator for connector admission candidates."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = (
    "connector_id",
    "source_id",
    "source_role",
    "rights_status",
    "policy_label",
    "candidate_ref",
)

ALLOWED_RIGHTS = {"approved", "public", "licensed"}
ALLOWED_POLICY_LABEL = {"public", "public-safe"}


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        fail("candidate payload must be a JSON object")
    return loaded


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_connector_candidate.py <candidate.json>")

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing candidate file: {path}")

    doc = load_json(path)

    for key in REQUIRED_FIELDS:
        value = doc.get(key)
        if value in (None, ""):
            fail(f"missing required field: {key}")

    if doc["rights_status"] not in ALLOWED_RIGHTS:
        fail("rights_status must be one of approved/public/licensed")

    if doc["policy_label"] not in ALLOWED_POLICY_LABEL:
        fail("policy_label must be public or public-safe")

    if doc.get("status") not in (None, "candidate", "reviewed"):
        fail("status must be candidate/reviewed when provided")

    print(f"ALLOW: valid connector candidate: {path}")


if __name__ == "__main__":
    main()
