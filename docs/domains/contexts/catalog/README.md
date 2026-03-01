# Catalog Context

## Purpose
Owns discoverability metadata and machine-readable catalog artifacts.

## Responsibilities
- Build and validate STAC/DCAT/PROV-facing metadata
- Maintain versioned dataset descriptors

## Non-responsibilities
- Policy adjudication
- Story claim authoring

## Owned entities
- Catalog entry
- Dataset metadata projection

## Invariants
- MUST keep version lineage traceable.
- MUST not publish entries with unresolved required provenance links.

## Interfaces
### Inputs
- Ingest outputs

### Outputs
- Catalog documents and contract-valid metadata
