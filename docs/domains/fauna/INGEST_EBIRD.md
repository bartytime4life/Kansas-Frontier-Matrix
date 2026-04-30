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
