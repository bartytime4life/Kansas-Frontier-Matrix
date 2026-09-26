# Roads/Rail/Trade SourceDescriptor fixtures

Fixtures for `tools/validators/domains/roads-rail-trade/validate_source_descriptor.py`'s
`domain_scope` membership check.

The shared SourceDescriptor schema itself
(`schemas/contracts/v1/source/source_descriptor.schema.json`) is already
exhaustively fixture-tested by the shared corpus at
`fixtures/contracts/v1/source/source_descriptor/`; this directory does not
duplicate that coverage. It exists only to exercise the one rule this
domain adapter adds on top: an optional `domain_scope` (or legacy `domain`)
must include `"roads-rail-trade"` when declared.

- `valid/valid_1.json` is a synthetic fixture (`source_type: synthetic_fixture`, `source_role: fixture_only`) built for this check, since no committed SourceDescriptor fixture is currently scoped to this domain.
- `invalid/invalid_domain_scope_mismatch.json` is a copy of the real hydrology-scoped fixture (`fixtures/contracts/v1/source/source_descriptor/valid/valid_1.json`), which is schema-valid but declares a `domain_scope` that does not include this domain.

Neither fixture is proof of source admission, rights, sensitivity
clearance, policy approval, or release. See
`contracts/source/source_descriptor.md` for the shared contract.
