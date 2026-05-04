from pathlib import Path

# fixture -> schema mapping for required proof-slice artifacts
MAPPING = {
    "fixtures/source/source_descriptor.valid.json": "schemas/contracts/v1/source/source_descriptor.schema.json",
    "fixtures/source/source_descriptor.stale.valid.json": "schemas/contracts/v1/source/source_descriptor.schema.json",
    "fixtures/evidence/evidence_ref.valid.json": "schemas/contracts/v1/evidence/evidence_ref.schema.json",
    "fixtures/evidence/evidence_bundle.valid.json": "schemas/contracts/v1/evidence/evidence_bundle.schema.json",
    "fixtures/domains/hydrology/hydrology_feature.valid.json": "schemas/contracts/v1/domains/hydrology/hydrology_feature.schema.json",
    "fixtures/domains/hydrology/hydrology_observation.valid.json": "schemas/contracts/v1/domains/hydrology/hydrology_observation.schema.json",
    "fixtures/ai/focus_mode_request.valid.json": "schemas/contracts/v1/ai/focus_mode_request.schema.json",
    "fixtures/ai/focus_mode_response.answer.valid.json": "schemas/contracts/v1/ai/focus_mode_response.schema.json",
    "fixtures/ai/focus_mode_response.abstain.valid.json": "schemas/contracts/v1/ai/focus_mode_response.schema.json",
    "fixtures/ai/focus_mode_response.deny.valid.json": "schemas/contracts/v1/ai/focus_mode_response.schema.json",
    "fixtures/ai/focus_mode_response.error.valid.json": "schemas/contracts/v1/ai/focus_mode_response.schema.json",
    "fixtures/policy/policy_decision_allow.valid.json": "schemas/contracts/v1/policy/policy_decision.schema.json",
    "fixtures/policy/policy_decision_deny.valid.json": "schemas/contracts/v1/policy/policy_decision.schema.json",
    "fixtures/release/release_manifest.valid.json": "schemas/contracts/v1/release/release_manifest.schema.json",
}


def main() -> int:
    errors = []
    for fixture, schema in MAPPING.items():
        if not Path(fixture).exists():
            errors.append(f"missing fixture: {fixture}")
        if not Path(schema).exists():
            errors.append(f"missing schema: {schema}")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", f"fixture-schema mapping intact for {len(MAPPING)} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
