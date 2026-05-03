# Lifecycle and Promotion

Governed lifecycle for roads/rail/trade-routes artifacts.

## Lifecycle
`SOURCE -> RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`

## Promotion requirements
- EvidenceBundle closure and catalog/provenance consistency.
- Policy decision and finite runtime outcomes.
- Rollback target and correction lineage registered.

## Fail-closed behavior
- Unsupported claim: `ABSTAIN`.
- Policy prohibited claim: `DENY`.
- Processing/runtime failure: `ERROR`.
