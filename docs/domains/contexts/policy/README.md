# Policy Context

## Purpose
Owns allow/deny and obligations decisions from policy rules.

## Responsibilities
- Evaluate policy labels and constraints
- Produce explainable decision outputs

## Non-responsibilities
- Data acquisition
- Search ranking logic

## Owned entities
- Policy decision
- Obligation set

## Invariants
- MUST default deny when required evidence/policy context is missing.
- MUST include machine-readable reason codes.

## Interfaces
### Inputs
- Evidence outcomes
- Policy labels and request context

### Outputs
- allow/deny + obligations + reasons
