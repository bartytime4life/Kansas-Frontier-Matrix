# Atmosphere / Air API Contracts

Contract expectations for governed atmosphere-air APIs.

## Response envelope

Finite outcomes only:

- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

## Contract constraints

- Include knowledge character and source role in payloads.
- Include EvidenceRefs for consequential claims.
- Include freshness and temporal support details.
- Deny when rights/evidence/policy checks fail.
