# ADR-0008: Domain Lane Template Standardization

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** domain architecture / documentation / onboarding

## Context

Domain lanes vary in structure and completeness, making onboarding, review, and automation inconsistent.

## Decision

All domain lanes follow a common template for required docs, contracts, source mappings, validators, and policy notes.

## Alternatives considered

- **Domain-specific bespoke layouts:** rejected because comparability and automation suffer.
- **Minimal README-only convention:** rejected because required governance artifacts are often omitted.

## Consequences

### Positive

- Faster onboarding and cross-domain review.
- Easier automation for linting and completeness checks.

### Negative / tradeoffs

- Standard template may feel rigid for niche domains.
- Existing lanes require backfill work.

## Verification

- Add structure checks for required files/sections per lane.
- Add documentation checks for required domain metadata.

## Migration / rollback

Adopt template incrementally per lane and track completion in runbooks or backlog.
