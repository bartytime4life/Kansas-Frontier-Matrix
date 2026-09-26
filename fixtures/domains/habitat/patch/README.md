# Habitat patch fixtures

Structural-only fixtures for `tools/validators/domains/habitat/validate_habitat_patch.py`.

`schemas/contracts/v1/domains/habitat/habitat_patch.schema.json` is a `PROPOSED`
scaffold: empty `properties`, `additionalProperties: true`, and `type: object`.
Field-level `HabitatPatch` semantics (identity, source role, geometry,
evidence, sensitivity, policy, release) remain `NEEDS VERIFICATION` pending a
domain-steward schema expansion (see
`contracts/domains/habitat/habitat_patch.md`, "Schema posture" and
"Recommended semantics").

- `valid/` proves any well-formed JSON object is currently accepted, since the
  scaffold schema imposes no field constraints yet.
- `invalid/` proves the one rule the current scaffold actually enforces: the
  root must be a JSON object. Duplicate JSON object keys and non-finite
  numbers fail earlier, at JSON parsing, so `--fixtures` replay (which expects
  every fixture to parse) cannot represent them; those cases are instead
  exercised as explicit-file arguments in
  `tests/validators/domains/habitat/test_habitat_patch_validator_entrypoint.py`.

No fixture asserts a proposed `HabitatPatch` field name, source role, or
enum value as settled shape. Do not treat this fixture set as HabitatPatch
schema coverage.
