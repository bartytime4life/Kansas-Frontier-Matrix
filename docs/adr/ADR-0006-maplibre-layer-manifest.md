# ADR-0006: MapLibre Layer Manifest Contract

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** UI contract / mapping / publication

## Context

Map rendering depends on stable layer metadata and constraints. Without a manifest contract, UI behavior can diverge from data and policy guarantees.

## Decision

Map layers must be declared via a governed manifest schema that captures source, attribution, styling constraints, sensitivity flags, and evidence linkage.

## Alternatives considered

- **Inline per-component layer configs:** rejected because they fragment governance.
- **Runtime-only ad-hoc layer assembly:** rejected because reproducibility and policy checks weaken.

## Consequences

### Positive

- Consistent map behavior across environments.
- Better policy and attribution enforcement.

### Negative / tradeoffs

- Requires manifest versioning and migration strategy.
- Adds contract maintenance for UI teams.

## Verification

- Schema validation for layer manifests in CI.
- UI contract tests ensuring manifest-driven behavior.

## Migration / rollback

Support a compatibility parser for legacy layer configs until all clients adopt manifest schema.
