#!/usr/bin/env python3
"""
Validate KFM PROV sidecar files.

Checks:
- JSON Schema validity
- required artifact entity
- required license
- required spec_hash
- run linkage
- attribution linkage
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/provenance/kfm_prov_sidecar.schema.json")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_prov_sidecar.py <artifact.prov.jsonld>")

    sidecar_path = Path(sys.argv[1])

    if not sidecar_path.exists():
        fail(f"missing provenance sidecar: {sidecar_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(sidecar_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    entities = doc.get("entity", {})
    activities = doc.get("activity", {})
    agents = doc.get("agent", {})

    artifact_id = doc["wasGeneratedBy"]["prov:entity"]
    activity_id = doc["wasGeneratedBy"]["prov:activity"]
    attributed_entity_id = doc["wasAttributedTo"]["prov:entity"]
    agent_id = doc["wasAttributedTo"]["prov:agent"]

    if artifact_id not in entities:
        fail(f"wasGeneratedBy references missing entity: {artifact_id}")

    if activity_id not in activities:
        fail(f"wasGeneratedBy references missing activity: {activity_id}")

    if attributed_entity_id != artifact_id:
        fail("wasAttributedTo entity does not match generated artifact entity")

    if agent_id not in agents:
        fail(f"wasAttributedTo references missing agent: {agent_id}")

    artifact = entities[artifact_id]

    if artifact.get("prov:type") != "kfm:EvidenceBundle":
        fail("generated artifact must be prov:type kfm:EvidenceBundle")

    if not artifact.get("dct:license"):
        fail("artifact missing dct:license")

    if not artifact.get("kfm:spec_hash"):
        fail("artifact missing kfm:spec_hash")

    used = activities[activity_id].get("prov:used", [])

    if not used:
        fail("pipeline activity missing prov:used input references")

    for ref in used:
        if ref not in entities:
            fail(f"activity prov:used references missing entity: {ref}")

    print(f"ALLOW: valid KFM PROV sidecar: {sidecar_path}")


if __name__ == "__main__":
    main()
