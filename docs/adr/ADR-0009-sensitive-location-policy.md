# ADR-0009: Sensitive-Location Publication Policy

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** policy / safety / publication

## Context

Publishing precise locations can create ecological, cultural, or personal harm. Sensitive data requires explicit redaction and access controls.

## Decision

Sensitive-location policy is fail-closed: exact geometry and restricted attributes are withheld from public surfaces unless policy explicitly permits release at required precision.

## Alternatives considered

- **Case-by-case manual redaction only:** rejected due to inconsistency risk.
- **Always-public exact locations:** rejected due to harm and governance risk.

## Consequences

### Positive

- Reduced harm from precise location disclosure.
- Clear policy enforcement at publication boundary.

### Negative / tradeoffs

- Public datasets may lose granularity.
- Requires strong classification and review workflows.

## Verification

- Policy tests for redaction/generalization rules.
- E2E checks confirming restricted fields never appear in public API/UI outputs.

## Migration / rollback

Backfill sensitivity metadata for existing sources and apply staged enforcement before strict fail-closed rollout.
