# ADR-0003: Source Ledger Authority and Source-State Gating

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** governance / source trust / ingestion

## Context

Source records carry verification status, rights posture, and trust metadata. Without a canonical source-state authority, ingestion and publication can drift.

## Decision

`data/registry/` source records and their governed status fields are authoritative for source trust and eligibility. Pipeline and publication gates must resolve status from that ledger, not from ad-hoc flags.

## Alternatives considered

- **Pipeline-local source flags:** rejected because they duplicate authority and drift.
- **Manual review-only source status:** rejected because enforcement is inconsistent without machine-readable gating.

## Consequences

### Positive

- One source of truth for source-state decisions.
- Better auditability of why a source was accepted, held, or denied.

### Negative / tradeoffs

- Requires strict schema and validator coverage for source records.
- May require migration of legacy source metadata.

## Verification

- Add CI checks that reject ingestion/publication when source status is missing or non-compliant.
- Add fixtures for allow/deny source-state transitions.

## Migration / rollback

Migrate pipelines to resolve source status from registry descriptors. If superseded, preserve this ADR and provide explicit alias behavior during transition.
