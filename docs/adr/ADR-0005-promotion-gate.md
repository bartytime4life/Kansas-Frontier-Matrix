# ADR-0005: Promotion Gate as a Governed State Transition

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** release / governance / policy

## Context

Promotion cannot be a simple file move. It must reflect evidence closure, policy compliance, and rollback readiness.

## Decision

Promotion to public-facing states is a governed transition requiring policy pass, evidence closure, and release manifest binding. Transitions fail closed when mandatory checks are incomplete.

## Alternatives considered

- **Best-effort promotion with warnings:** rejected because it permits unresolved risk.
- **Manual promotion without machine gates:** rejected because outcomes are non-repeatable.

## Consequences

### Positive

- Deterministic release governance and auditability.
- Clear rollback anchor from release manifests.

### Negative / tradeoffs

- Increased operational rigor and CI complexity.
- Potentially slower release cadence when checks are strict.

## Verification

- Promotion gate tests for allow/deny paths.
- Policy and proof checks integrated into CI workflows.

## Migration / rollback

Phase in gate requirements with transitional warnings, then enforce fail-closed behavior once coverage is complete.
