# Evidence Context

## Purpose
Owns resolution from references to verifiable evidence bundles.

## Responsibilities
- Resolve EvidenceRef to EvidenceBundle
- Track support/insufficient evidence outcomes

## Non-responsibilities
- Final policy decisioning

## Owned entities
- EvidenceRef
- EvidenceBundle

## Invariants
- MUST provide deterministic resolution against fixed inputs.
- MUST include reason codes when support is insufficient.

## Interfaces
### Inputs
- Evidence references from stories/focus/policy

### Outputs
- Evidence bundles and resolution reports
