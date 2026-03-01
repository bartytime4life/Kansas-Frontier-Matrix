# Ingest Context

## Purpose
Owns acquisition intake and normalization hand-off into catalog-ready structures.

## Responsibilities
- Intake source manifests and acquisition metadata
- Validate source-level shape before catalog hand-off
- Emit deterministic ingest outputs and receipts

## Non-responsibilities
- Public catalog publication
- Story composition

## Owned entities
- Acquisition request
- Ingest receipt

## Invariants
- MUST produce deterministic outputs for same input/versioned transform.
- MUST preserve source lineage required for downstream provenance.

## Interfaces
### Inputs
- Acquisition manifests

### Outputs
- Catalog-ready datasets + ingest receipts
