# Habitat suitability-model fixtures

Structural-only fixtures for `tools/validators/domains/habitat/validate_suitability_model.py`.

`schemas/contracts/v1/domains/habitat/suitability_model.schema.json` is a
`PROPOSED` scaffold: empty `properties`, `additionalProperties: true`, and
`type: object`. Field-level `SuitabilityModel` semantics (model card,
model-versus-observation source role, uncertainty, evidence, policy, release)
remain `NEEDS VERIFICATION` pending a domain-steward schema expansion (see
`contracts/domains/habitat/suitability_model.md`, "Schema posture" and
"Recommended semantics" / model-card topics).

- `valid/` proves any well-formed JSON object is currently accepted, since the
  scaffold schema imposes no field constraints yet.
- `invalid/` proves the one rule the current scaffold actually enforces: the
  root must be a JSON object. Duplicate JSON object keys and non-finite
  numbers fail earlier, at JSON parsing, so `--fixtures` replay (which expects
  every fixture to parse) cannot represent them; those cases are instead
  exercised as explicit-file arguments in
  `tests/validators/domains/habitat/test_suitability_model_validator_entrypoint.py`.

No fixture asserts a proposed `SuitabilityModel` field name, model-card
topic, or enum value as settled shape. Do not treat this fixture set as
SuitabilityModel schema coverage.
