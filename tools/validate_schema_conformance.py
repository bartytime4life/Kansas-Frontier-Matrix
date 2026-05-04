import json
from pathlib import Path

REQUIRED = {
    "fixtures/source/source_descriptor.valid.json": ["id", "knowledge_character", "sensitivity"],
    "fixtures/evidence/evidence_ref.valid.json": ["id", "bundle_id", "knowledge_character"],
    "fixtures/evidence/evidence_bundle.valid.json": ["id", "evidence_refs", "knowledge_character"],
    "fixtures/release/release_manifest.valid.json": ["id", "rollback_target", "correction_route", "release_state"],
    "fixtures/policy/policy_decision_allow.valid.json": ["id", "decision", "knowledge_character"],
    "fixtures/policy/policy_decision_deny.valid.json": ["id", "decision", "knowledge_character"],
    "fixtures/ai/focus_mode_response.answer.valid.json": ["id", "outcome", "citations", "knowledge_character"],
}

ENUMS = {
    "release_state": {"DRAFT", "QUARANTINED", "PROCESSED", "CATALOGED", "REVIEWED", "RELEASE_CANDIDATE", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"},
    "decision": {"ALLOW", "ABSTAIN", "DENY", "ERROR"},
    "outcome": {"ANSWER", "ABSTAIN", "DENY", "ERROR"},
    "knowledge_character": {"OBSERVED", "DOCUMENTARY", "DERIVED", "MODELED", "GENERALIZED", "SOURCE_DEPENDENT", "SYNTHETIC_TEST"},
    "sensitivity": {"PUBLIC_SAFE", "GENERALIZED", "REDACTED", "RESTRICTED", "STEWARD_ONLY"},
}


def main() -> int:
    errors = []
    for path, required_keys in REQUIRED.items():
        obj = json.loads(Path(path).read_text())
        for key in required_keys:
            if key not in obj:
                errors.append(f"{path}: missing required key {key}")
        for key, values in ENUMS.items():
            if key in obj and obj[key] not in values:
                errors.append(f"{path}: invalid {key}={obj[key]}")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS", f"validated schema-conformance checks for {len(REQUIRED)} fixture contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
