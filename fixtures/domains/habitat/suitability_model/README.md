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
  scaffold schema imposes no field constraints yet. `valid_3.json` also
  proves the optional `model_card_ref` linkage check: it points at
  `support/model_card_pass.json`, which independently passes
  `tools/validators/governance/validate_model_card_envelope.py`.
- `invalid/` proves the rules the validator actually enforces: the root must
  be a JSON object, and — if declared — `model_card_ref` must be a non-empty
  string that resolves to a regular (non-symlink) file whose contents
  independently pass ModelCardEnvelope validation. Duplicate JSON object
  keys and non-finite numbers fail earlier, at JSON parsing, so `--fixtures`
  replay (which expects every fixture to parse) cannot represent them; those
  cases are instead exercised as explicit-file arguments in
  `tests/validators/domains/habitat/test_suitability_model_validator_entrypoint.py`.
- `support/` holds the standalone ModelCardEnvelope documents `valid/` and
  `invalid/` link to; see `support/README.md`.

`model_card_ref` is resolved as a plain repository-root-relative (or
absolute) filesystem path — a deliberately minimal, locally-scoped
convention for this validator only, since no KFM URI resolver contract
exists yet for cross-object references.

No fixture asserts a proposed `SuitabilityModel` field name, other
model-card topic, or enum value as settled shape. Do not treat this fixture
set as SuitabilityModel schema coverage.
