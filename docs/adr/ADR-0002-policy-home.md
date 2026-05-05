# ADR-0002: Policy Home

- **Status:** Accepted
- **Date:** 2026-05-05

## Decision
`policy/` is the canonical home for policy semantics.

If `policies/` is present, it is treated as compatibility/transitional (or mirrored) only.

## Rationale
- Aligns policy governance to a single canonical root.
- Prevents semantic drift from split canonical policy surfaces.
- Allows migration/compatibility bridges without weakening canonical ownership.

## Consequences
- New canonical policy content must be added under `policy/`.
- `policies/` may contain only README/migration-oriented compatibility notes unless explicitly governed otherwise.
