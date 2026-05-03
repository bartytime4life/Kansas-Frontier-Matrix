# Settlements & Infrastructure Schema Registry

Track schema object families, versioning posture, and compatibility expectations.

## Canonical home

Canonical schema home is **NEEDS VERIFICATION**:

- `schemas/contracts/v1/settlements/` + `schemas/contracts/v1/infrastructure/`, or
- repo-native `contracts/` equivalents.

Use one authority and record the decision in an ADR.

## Required object families

| Family | Minimum purpose |
|---|---|
| Settlement contracts | Place identity, names, status, boundaries, civic functions |
| Infrastructure contracts | Asset/network identity, topology, operator and dependency links |
| Observation contracts | Population/condition/service observations with source/time context |
| Governance contracts | EvidenceBundle, DecisionEnvelope, ReleaseManifest, correction records |

## Compatibility policy

- Version contracts semantically.
- Do not break published API DTOs without explicit migration notes.
- Preserve backward readability for at least one minor version.
- Encode supersession relationships for corrected records.
