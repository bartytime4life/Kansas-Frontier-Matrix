# Hydrology API Contracts (Documentation)

## Contract posture
Hydrology API routes should expose only released artifacts and proof-linked summaries.

## Minimum response guarantees
- finite outcome envelope: `ANSWER | ABSTAIN | DENY | ERROR`
- evidence references for claims
- freshness/as-of metadata
- source-role transparency
- correction/rollback visibility

## Explicit denials
The API must deny direct access to RAW/WORK/QUARANTINE stores.

## Candidate route groups
- `GET /hydrology/layers`
- `GET /hydrology/units/{huc12}`
- `GET /hydrology/sites/{site_id}/observations`
- `GET /hydrology/evidence/{evidence_ref}`
