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
  scaffold schema imposes no field constraints yet. `valid_3.json` also
  proves the connectivity reference-hygiene check: `connectivity_edge_refs`
  and `corridor_refs` are sorted, unique, grammar-bounded arrays with no
  internal-lifecycle prefix.
- `invalid/` proves the rules the validator actually enforces: the root must
  be a JSON object, and — if declared — `connectivity_edge_refs`/
  `corridor_refs` must be non-empty, sorted, unique arrays of grammar-valid
  reference strings with no `raw:`/`work:`/`quarantine:`/`internal:`/
  `canonical:`/`model:` prefix. Duplicate JSON object keys and non-finite
  numbers fail earlier, at JSON parsing, so `--fixtures` replay (which
  expects every fixture to parse) cannot represent them; those cases are
  instead exercised as explicit-file arguments in
  `tests/validators/domains/habitat/test_habitat_patch_validator_entrypoint.py`.

Neither connectivity field is resolved to a real `ConnectivityEdge` or
`Corridor` object — both are themselves empty `PROPOSED` schema scaffolds
(`schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json`,
`corridor.schema.json`). This is a reference-shape check only, reusing the
shared CatalogMatrix closure validator's ref-hygiene rule unchanged
(`tools/validators/validate_catalog_matrix_closure.py`).

No fixture asserts a proposed `HabitatPatch` field name, source role, or
enum value as settled shape beyond that reference shape. Do not treat this
fixture set as HabitatPatch schema coverage.
