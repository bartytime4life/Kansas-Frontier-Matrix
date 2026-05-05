#!/usr/bin/env python3
"""
Validate KFM PROV sidecar files.

Checks:
- JSON Schema validity
- required generated EvidenceBundle entity
- required license
- required spec_hash
- run linkage
- attribution linkage
- used entity linkage
- optional explicit used relations
- public publication safety posture
- no RAW / WORK / QUARANTINE references
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/provenance/kfm_prov_sidecar.schema.json")

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
    activity = activities[activity_id]

    if artifact.get("prov:type") != "kfm:EvidenceBundle":
        fail("generated artifact must be prov:type kfm:EvidenceBundle")

    license_value = assert_present(artifact, "dct:license", "artifact")
    assert_not_blocked(license_value, "artifact dct:license")

    access_rights = artifact.get("dct:accessRights")
    if access_rights is not None:
        assert_not_blocked(access_rights, "artifact dct:accessRights")

    assert_present(artifact, "kfm:spec_hash", "artifact")

    policy_label = artifact.get("kfm:policy_label")
    if policy_label is not None and policy_label != "public":
        fail("published artifact provenance requires kfm:policy_label=public")

    sensitivity = artifact.get("kfm:sensitivity")
    if sensitivity is not None and sensitivity != "public":
        fail("published artifact provenance requires kfm:sensitivity=public")

    publication_context = doc.get("kfm:publication_context")
    if publication_context == "public":
        if policy_label is not None and policy_label != "public":
            fail("public publication context requires artifact kfm:policy_label=public")
        if sensitivity is not None and sensitivity != "public":
            fail("public publication context requires artifact kfm:sensitivity=public")

    used_refs = activity.get("prov:used", [])
    if not used_refs:
        fail("pipeline activity missing prov:used input references")

    for ref in used_refs:
        if ref not in entities:
            fail(f"activity prov:used references missing entity: {ref}")

    explicit_used = doc.get("used", [])
    for idx, relation in enumerate(explicit_used):
        relation_activity = relation.get("prov:activity")
        relation_entity = relation.get("prov:entity")

        if relation_activity not in activities:
            fail(f"used[{idx}] references missing activity: {relation_activity}")

        if relation_entity not in entities:
            fail(f"used[{idx}] references missing entity: {relation_entity}")

    derived_from = doc.get("wasDerivedFrom", [])
    for idx, relation in enumerate(derived_from):
        generated_entity = relation.get("prov:generatedEntity")
        used_entity = relation.get("prov:usedEntity")
        relation_activity = relation.get("prov:activity")

        if generated_entity not in entities:
            fail(f"wasDerivedFrom[{idx}] references missing generated entity: {generated_entity}")

        if used_entity not in entities:
            fail(f"wasDerivedFrom[{idx}] references missing used entity: {used_entity}")

        if relation_activity is not None and relation_activity not in activities:
            fail(f"wasDerivedFrom[{idx}] references missing activity: {relation_activity}")

    if contains_forbidden_ref(doc):
        fail("public provenance sidecar references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM PROV sidecar: {sidecar_path}")


if __name__ == "__main__":
    main()
