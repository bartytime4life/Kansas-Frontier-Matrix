# Hydrology SourceDescriptor fixtures

Fixtures for `tools/validators/domains/hydrology/validate_source_descriptor.py`'s
`domain_scope` membership check.

The shared SourceDescriptor schema itself
(`schemas/contracts/v1/source/source_descriptor.schema.json`) is already
exhaustively fixture-tested by the shared corpus at
`fixtures/contracts/v1/source/source_descriptor/`; this directory does not
duplicate that coverage. It exists only to exercise the one rule this
domain adapter adds on top: an optional `domain_scope` (or legacy `domain`)
must include `"hydrology"` when declared.

- `valid/valid_1.json` is a real committed fixture (`fixtures/contracts/v1/source/source_descriptor/valid/valid_1.json`) already scoped to hydrology.
- `invalid/invalid_domain_scope_mismatch.json` is a copy of the real soil-scoped fixture (`fixtures/contracts/v1/source/source_descriptor/valid/valid_2.json`), which is schema-valid but declares a `domain_scope` that does not include hydrology.

Neither fixture is proof of source admission, rights, sensitivity
clearance, policy approval, or release. See
`contracts/source/source_descriptor.md` for the shared contract.
