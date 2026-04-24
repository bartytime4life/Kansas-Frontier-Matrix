#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
}


def validate(payload: Any, schema: dict[str, Any], context: str, errors: list[str]) -> None:
    schema_type = schema.get("type")
    if schema_type in TYPE_MAP and not isinstance(payload, TYPE_MAP[schema_type]):
        errors.append(f"{context}: expected {schema_type}, got {type(payload).__name__}")
        return

    if schema_type == "object":
        required = schema.get("required", [])
        for key in required:
            if key not in payload:
                errors.append(f"{context}: missing required key '{key}'")

        props = schema.get("properties", {})
        for key, sub_schema in props.items():
            if key in payload:
                validate(payload[key], sub_schema, f"{context}.{key}", errors)

    if schema_type == "array" and "items" in schema:
        for i, item in enumerate(payload):
            validate(item, schema["items"], f"{context}[{i}]", errors)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    pairs: list[tuple[Path, Path, str]] = [
        (
            Path("tests/ci/fixtures/diff_summary/diff.json"),
            Path("schemas/contracts/v1/runtime/renderers/diff_summary_input.schema.json"),
            "diff_summary",
        ),
        (
            Path("tests/ci/fixtures/diff_policy/diff_policy.json"),
            Path("schemas/contracts/v1/runtime/renderers/diff_policy_summary_input.schema.json"),
            "diff_policy_summary",
        ),
        (
            Path("tests/ci/fixtures/promotion_summary/promotion.json"),
            Path("schemas/contracts/v1/runtime/renderers/promotion_summary_input.schema.json"),
            "promotion_summary",
        ),
        (
            Path("tests/ci/fixtures/promotion_bundle/bundle.json"),
            Path("schemas/contracts/v1/runtime/renderers/promotion_bundle_summary_input.schema.json"),
            "promotion_bundle_summary",
        ),
    ]

    errors: list[str] = []
    for payload_path, schema_path, label in pairs:
        payload = load_json(payload_path)
        schema = load_json(schema_path)
        validate(payload, schema, label, errors)

    review_schema = load_json(Path("schemas/contracts/v1/runtime/renderers/review_handoff_inputs.schema.json"))
    review_payload = {
        "promotion": load_json(Path("tests/ci/fixtures/review_handoff/promotion.json")),
        "bundle": load_json(Path("tests/ci/fixtures/review_handoff/bundle.json")),
        "diff": load_json(Path("tests/ci/fixtures/review_handoff/diff.json")),
        "diff_policy": load_json(Path("tests/ci/fixtures/review_handoff/diff_policy.json")),
    }
    validate(review_payload, review_schema, "review_handoff", errors)

    if errors:
        print("validate_renderer_fixtures: failed", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("validate_renderer_fixtures: all renderer fixtures satisfy schema contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
