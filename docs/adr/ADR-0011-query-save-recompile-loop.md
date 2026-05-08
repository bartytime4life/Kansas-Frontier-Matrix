# ADR-0011-query-save-recompile-loop

- **Status:** proposed
- **Decision Date:** 2026-05-08
- **Scope:** architecture/governance
- **Supersedes:** none

## Context
This ADR was created from the April–May 2026 backlog normalization request to ensure a canonical decision record exists in `docs/adr/`.

## Decision
Governed incremental loop: query→save→validate→compile→review→promote→recompile; no autonomous publishing.

## Consequences
- Governs future implementation and validation work for this decision area.
- Requires follow-up updates to schemas/contracts/policy/tests as applicable.

## Verification
- Add concrete file/path evidence and tests before marking this ADR as accepted.
