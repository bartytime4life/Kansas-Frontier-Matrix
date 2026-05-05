# ADR-0001: Schema Home

- **Status:** Accepted
- **Date:** 2026-05-05

## Decision
All canonical contract schemas are rooted under:

`schemas/contracts/v1/`

Versioned subdirectories beneath this path are the only valid homes for contract schema sources.

## Rationale
- Keeps schema ownership discoverable from one stable root.
- Supports versioned evolution without changing repository topology.
- Separates schema definitions from runtime code, fixtures, and generated artifacts.

## Consequences
- New contract schema work must be placed under `schemas/contracts/v1/` (or a future versioned sibling approved by ADR).
- Tools and docs should reference this path as the source of truth.
