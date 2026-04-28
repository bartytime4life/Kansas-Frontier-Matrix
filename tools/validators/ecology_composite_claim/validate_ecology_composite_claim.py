#!/usr/bin/env python3
"""Validate ecology composite claim envelopes with fail-closed checks."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = (
    "claim_id",
    "claim_type",
    "statement",
    "evidence_ref",
    "spec_hash",
    "policy_label",
)

ALLOWED_CLAIM_TYPES = {"cite", "abstain", "deny"}


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        doc = json.load(handle)
    if not isinstance(doc, dict):
        fail("claim envelope must be a JSON object")
    return doc


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_ecology_composite_claim.py <claim.json>")

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing claim file: {path}")

    doc = load_json(path)

    for field in REQUIRED_FIELDS:
        if doc.get(field) in (None, ""):
            fail(f"missing required field: {field}")

    if doc["claim_type"] not in ALLOWED_CLAIM_TYPES:
        fail("claim_type must be cite, abstain, or deny")

    if doc["policy_label"] not in {"public", "public-safe"}:
        fail("policy_label must be public or public-safe")

    print(f"ALLOW: valid ecology composite claim: {path}")


if __name__ == "__main__":
    main()
