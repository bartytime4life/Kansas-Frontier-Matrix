# eBird ingest (Layer 3)

Layer 3 adds local EBD TSV streaming execution:
- canonical restricted occurrence output (`jsonl` or `csv`)
- quarantine receipts for rejected/malformed rows
- run manifest with counts, hashes, and paths
- EvidenceBundle emission/validation compatibility with Layer 2

## Executable filter limitation

This adapter only executes the governed checklist QA predicate:

`complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10`

Semantically different predicates are rejected.

## Restricted-output warning

Exact coordinates are only emitted to restricted local outputs and are blocked from `data/published`.
No public exact-point publication is implemented in this layer.

## Layer 4 (aggregation)
- Public-safe aggregate contract (`AggregateOccurrence`) for `huc12` and `county`.
- Suppression threshold enforces `checklist_count >= suppression_min_n`.
- Restricted suppression receipt stores hashed suppressed group identifiers.
- Region assignment order: observation field, then optional synthetic GeoJSON spatial join.
- WARNING: public outputs must never contain exact coordinates.

## Layer 5: Governed Promotion
`kfm-ebird-promote` validates a Layer 4 aggregate + manifest + EvidenceBundle, computes deterministic `run_id`, and writes:
- `aggregates.(jsonl|csv)`
- `aggregate_manifest.json`
- `evidencebundle.json`
- `catalog_record.json`
- `triplets.jsonl`
- `evidence_drawer.json`
- `promotion_receipt.json`

Promotion is aggregate-only and never publishes exact coordinates, restricted observations, quarantines, or suppression-group details.


## Layer 6: Public View Build
`kfm-ebird-build-public-view` converts Layer 5 promoted aggregate outputs into static public API contracts:
- PublicAggregateFeature DTOs
- FeatureEvidenceDrawer DTOs
- ApiManifest
- LayerApiDescriptor
- Aggregate-only MapLibre config

Safety rules: no exact coordinates, no point/circle/heatmap/cluster eBird layers, no restricted observation/quarantine/suppression receipt serving. Boundary configuration references external public boundary datasets and does not bundle real HUC12/county boundaries.
