# Focus Context

## Purpose
Owns ask/answer flows with evidence-bound, policy-safe responses.

## Responsibilities
- Accept focus queries
- Build responses grounded in evidence + policy outcomes

## Non-responsibilities
- Catalog indexing internals

## Owned entities
- Focus query
- Focus response

## Invariants
- MUST bind every response to supporting evidence or explicit insufficiency.
- MUST enforce policy constraints before emitting results.

## Interfaces
### Inputs
- Query intents
- Evidence/policy outputs

### Outputs
- Focus answers with citations and reason codes
