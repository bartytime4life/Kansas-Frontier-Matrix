# Package fixtures

Reusable, public-safe inputs for independently testable code under `packages/`.
These fixtures are test evidence only: production code must not import them, and
they do not establish contracts, source truth, policy, review, release, or
publication state.

## Inventory

- [`evidence_resolver/`](evidence_resolver/) — internal, versioned candidate
  checks for the non-authoritative evidence resolver package.
