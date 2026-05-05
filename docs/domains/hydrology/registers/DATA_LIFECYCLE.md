# Hydrology Data Lifecycle

## Lifecycle states
- `RAW`: pinned incoming fixtures/snapshots.
- `WORK`: normalized candidates.
- `QUARANTINE`: invalid or ambiguous candidates.
- `PROCESSED`: validated deterministic artifacts.
- `CATALOGED`: STAC/DCAT/PROV references closed.
- `PUBLISHED`: released artifacts only.

## Required transitions
1. `RAW -> WORK`: descriptor and rights gates pass.
2. `WORK -> PROCESSED`: schema + policy + role checks pass.
3. `WORK -> QUARANTINE`: ambiguity, policy failure, or missing required fields.
4. `PROCESSED -> PUBLISHED`: proof + catalog closure + decision envelope pass.

## Correction and rollback
- Never delete immutable artifacts.
- Corrections supersede prior release manifests.
- Rollback moves aliases back to a prior released manifest.
