#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMAS = [
    Path("schemas/contracts/v1/correction/correction_notice.schema.json"),
    Path("schemas/contracts/v1/release/release_manifest.schema.json"),
    Path("schemas/contracts/v1/source/source_descriptor.schema.json"),
    Path("schemas/contracts/v1/data/dataset_version.schema.json"),
    Path("schemas/contracts/v1/policy/decision_envelope.schema.json"),
    Path("schemas/contracts/v1/common/header_profile.schema.json"),
    Path("schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"),
    Path("schemas/contracts/v1/evidence/evidence_bundle.schema.json"),
]

failures: list[str] = []

for schema_path in SCHEMAS:
    if not schema_path.exists():
        failures.append(f"missing schema: {schema_path}")
        continue

    try:
        payload = json.loads(schema_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"invalid JSON: {schema_path} ({exc})")
        continue

    schema = payload.get("$schema")
    if not isinstance(schema, str) or "json-schema.org" not in schema:
        failures.append(f"invalid or missing $schema in {schema_path}")

if failures:
    print("validate_schemas: failed", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    sys.exit(1)

print(f"validate_schemas: validated {len(SCHEMAS)} schema files")
