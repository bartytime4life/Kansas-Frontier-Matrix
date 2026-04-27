# ADR-0004: EvidenceBundle as the Public Unit of Inspection

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** evidence / publication / governance

## Context

Public claims require inspectable evidence. If evidence packaging is inconsistent, consumers cannot reliably verify provenance, policy posture, or decision lineage.

## Decision

`EvidenceBundle` is the minimum public inspection artifact for governed outputs. Public-facing API/UI surfaces must link claims and rendered outputs back to the associated bundle.

## Alternatives considered

- **Receipt-only publication evidence:** rejected because run logs alone are not a full evidence package.
- **Narrative-only evidence summaries:** rejected because they are not machine-verifiable.

## Consequences

### Positive

- Reliable inspection boundary for audits and corrections.
- Stronger parity between human and machine verification.

### Negative / tradeoffs

- Adds publication overhead for every outward artifact.
- Requires stable bundle schemas and compatibility handling.

## Verification

- Gate release on EvidenceBundle presence and resolvability.
- Add contract tests for bundle references from API responses and catalog metadata.

## Migration / rollback

Introduce compatibility adapters for legacy outputs while requiring new outputs to emit bundle references.
