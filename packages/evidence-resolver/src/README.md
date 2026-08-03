# Evidence resolver source root

Python `src`-layout container inherited from the
[`kfm-evidence-resolver` package](../README.md).

## Boundary contract

- Purpose: contain reusable, independently testable resolver helper code.
- Owner: evidence/proof and package stewards — `OWNER_TBD`.
- Belongs: source files with deterministic, no-hidden-I/O behavior.
- Prohibited: applications, deployable wrappers, source connectors, stores,
  registries, policy engines, release logic, public API routes, fixtures, or
  generated trust records.
- Inputs/outputs: inherited from the package-local v1alpha1 profile.
- Exposure: internal alpha; build/install behavior and supported Python
  versions remain **NEEDS VERIFICATION**.
- Mutation/retention: none.
- Validation: `make evidence-resolver` and `make evidence-resolver-deny`.
- Rollback: revert the bounded package slice; no data migration is required.

## Current tree

```text
packages/evidence-resolver/src/
├── README.md
└── evidence_resolver/   # internal Python import namespace
```

Production code may not depend on test fixtures. This source root may depend
only on the standard library or deliberately admitted lower-level packages;
it must not import from `apps/`, `tools/`, `tests/`, or `fixtures/`.

See the [module boundary](evidence_resolver/README.md), [package boundary](../README.md),
and [Directory Rules](../../../docs/doctrine/directory-rules.md).
