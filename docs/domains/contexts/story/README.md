# Story Context

## Purpose
Owns narrative claim structures and publishable Story Node composition.

## Responsibilities
- Manage claims and claim-to-evidence links
- Produce story publish payloads

## Non-responsibilities
- Raw ingest pipeline operations

## Owned entities
- Story node
- Claim graph

## Invariants
- MUST bind claims to evidence references.
- MUST fail publication when required links are unresolved.

## Interfaces
### Inputs
- Claims, evidence references, policy outcomes

### Outputs
- Story publish contracts
