#!/usr/bin/env python3
"""
Validate KFM PublishReceipt files.

Checks:
- JSON Schema validity
- receipt_type is kfm:PublishReceipt
- status is PUBLISHED
- closure_status is PUBLISHABLE
- public-only policy posture
- reviewed or published review state
- artifact_count matches listed artifacts
- required artifact closure references exist
- no RAW / WORK / QUARANTINE references
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/release/kfm_publish_receipt.schema.json")

FORBIDDEN_PUBLIC_REFS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)

BLOCKED_PUBLIC_VALUES = {
    "TODO",
    "todo",
    "UNKNOWN",
    "unknown",
    "NEEDS-VERIFICATION",
    "restricted",
    "deny",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def contains_forbidden_ref(value: Any) -> bool:
    if isinstance(value, str):
        lowered = value.lower()
        return any(token in lowered for token in FORBIDDEN_PUBLIC_REFS)

    if isinstance(value, dict):
        return any(contains_forbidden_ref(v) for v in value.values())

    if isinstance(value, list):
        return any(contains_forbidden_ref(v) for v in value)

    return False


def assert_present(mapping: dict[str, Any], key: str, label: str) -> Any:
    value = mapping.get(key)
    if value in (None, ""):
        fail(f"{label} missing {key}")
    return value


def assert_not_blocked(value: Any, label: str) -> None:
    if isinstance(value, str) and value in BLOCKED_PUBLIC_VALUES:
        fail(f"{label} cannot be {value}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_publish_receipt.py <publish-receipt.json>")

    receipt_path = Path(sys.argv[1])

    if not receipt_path.exists():
        fail(f"missing PublishReceipt: {receipt_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(receipt_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    if doc.get("receipt_type") != "kfm:PublishReceipt":
        fail("PublishReceipt requires receipt_type=kfm:PublishReceipt")

    if doc.get("status") != "PUBLISHED":
        fail("PublishReceipt requires status=PUBLISHED")

    plan = assert_present(doc, "plan", "PublishReceipt")

    if not isinstance(plan, dict):
        fail("PublishReceipt plan must be an object")

    if plan.get("closure_status") != "PUBLISHABLE":
        fail("PublishReceipt requires plan.closure_status=PUBLISHABLE")

    if plan.get("policy_label") != "public":
        fail("PublishReceipt requires plan.policy_label=public")

    if plan.get("review_state") not in {"reviewed", "published"}:
        fail("PublishReceipt requires plan.review_state reviewed or published")

    for key in (
        "release_id",
        "manifest_id",
        "manifest_path",
        "policy_label",
        "review_state",
        "closure_status",
    ):
        value = assert_present(plan, key, "plan")
        assert_not_blocked(value, f"plan {key}")

    artifacts = assert_present(plan, "artifacts", "plan")

    if not isinstance(artifacts, list):
        fail("plan.artifacts must be an array")

    if not artifacts:
        fail("plan.artifacts cannot be empty")

    artifact_count = assert_present(plan, "artifact_count", "plan")

    if artifact_count != len(artifacts):
        fail("plan.artifact_count does not match length of plan.artifacts")

    for idx, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(f"plan.artifacts[{idx}] must be an object")

        label = f"plan.artifacts[{idx}]"

        for key in (
            "artifact_ref",
            "evidence_ref",
            "provenance_ref",
            "stac_ref",
            "dcat_ref",
        ):
            value = assert_present(artifact, key, label)
            assert_not_blocked(value, f"{label} {key}")

    if contains_forbidden_ref(doc):
        fail("public PublishReceipt references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM PublishReceipt: {receipt_path}")


if __name__ == "__main__":
    main()
