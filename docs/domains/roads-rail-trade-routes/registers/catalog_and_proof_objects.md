# Catalog and Proof Objects

Defines the proof closure expectations before publication.

## Minimum objects
- `run_receipt`
- `evidence_bundle`
- `decision_envelope`
- `release_manifest`
- `catalog_matrix`

## Closure checks
- Every public claim resolves to EvidenceBundle refs.
- STAC/DCAT/PROV identifiers align with digests/spec hash.
- Release alias and rollback reference are explicit.
