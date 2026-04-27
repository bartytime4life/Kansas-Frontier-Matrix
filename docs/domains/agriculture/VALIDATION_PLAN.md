# Agriculture Validation Plan

Validation is fail-closed and fixture-first.

## Validation classes

1. **Schema validation**: required fields, enum values, formats, and object-shape compatibility.
2. **Source-role validation**: claim type must be compatible with source role.
3. **Rights/sensitivity validation**: unknown rights or missing sensitivity blocks release.
4. **Temporal validation**: timestamp semantics, staleness window, and period consistency.
5. **Unit/depth validation**: station variables preserve unit and depth context.
6. **Geospatial validation**: CRS integrity, geometry validity, and precision controls.
7. **Aggregate misuse validation**: prevent field-level claims from aggregate products.
8. **Catalog closure validation**: each public claim resolves to an EvidenceBundle.

## Minimum fixture set

- Valid station observation fixture.
- Invalid missing-rights fixture.
- Invalid aggregate-as-field-claim fixture.
- Valid gridded remote-sensing fixture with product metadata.
- Invalid missing-provenance fixture.
- Promotion-denied fixture with DecisionEnvelope reasons.

## CI expectations

- Run fixture validations on every PR touching agriculture lane docs/contracts/policy/tests.
- Treat failing negative fixtures as a hard fail.
- Publish validator summary artifacts with deterministic run IDs.
