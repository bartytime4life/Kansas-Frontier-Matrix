# ADR-0011: Catalog, Proof, and Release Separation

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** publication architecture / provenance / release governance

## Context

Catalog discovery records, proof artifacts, and release manifests serve different purposes. Collapsing them creates ambiguous authority.

## Decision

Keep catalog metadata, proof/attestation artifacts, and release manifests as separate but linked objects. No single record may substitute for all three responsibilities.

## Alternatives considered

- **Single monolithic publication record:** rejected because it mixes concerns and weakens audit clarity.
- **Catalog-only publication model:** rejected because discovery metadata cannot replace proof and release state.

## Consequences

### Positive

- Clearer audit trails and accountability.
- Better compatibility with external catalog consumers.

### Negative / tradeoffs

- More objects to maintain and validate per release.
- Requires robust cross-link validation.

## Verification

- Release checks ensure all three object classes exist and cross-reference correctly.
- Tests verify rollback and correction paths preserve separation.

## Migration / rollback

Add linking adapters for legacy releases while transitioning to fully separated publication artifacts.
