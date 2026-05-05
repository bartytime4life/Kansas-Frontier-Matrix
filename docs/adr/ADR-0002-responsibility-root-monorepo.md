# ADR-0002: Responsibility-Root Monorepo Layout

- **Status:** Accepted
- **Date:** 2026-05-05

## Decision
Repository layout is responsibility-rooted (e.g., `apps/`, `schemas/`, `contracts/`, `tools/`, `tests/`) and forbids greenfield domain roots at repository top level.

## Rationale
- Enforces clear separation of concerns by function.
- Avoids domain sprawl at root and keeps governance/tooling predictable.
- Preserves consistent paths for automation and policy checks.

## Consequences
- Domain-specific content belongs under approved responsibility roots.
- New top-level folders must align to responsibility, not domain naming.
- Directory-rule checks remain the enforcement point for root hygiene.
