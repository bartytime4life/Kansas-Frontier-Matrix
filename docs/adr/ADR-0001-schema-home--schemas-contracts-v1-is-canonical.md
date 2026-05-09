# ADR

Status: PROPOSED

## Context
KFM requires common contract schemas with deterministic placement and finite runtime outcomes.

## Decision
- Schemas are canonical under `schemas/contracts/v1/`; semantic contract prose lives under `contracts/`.
- Runtime outcomes are finite: `ANSWER | ABSTAIN | DENY | ERROR`.
- `ai_receipt` excludes raw chain-of-thought fields by contract.
- ABSTAIN is a first-class policy/runtime decision and not an error condition.

## Consequences
- Governed API may safely return ABSTAIN while routes are scaffolded.
- Domain lanes can reference common schemas via `$ref` in follow-up PRs.
