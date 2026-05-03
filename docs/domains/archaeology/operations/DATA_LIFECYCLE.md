# Data Lifecycle

## Truth path

`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`

## Lifecycle notes

- RAW is immutable and auditable.
- WORK is transform/normalization space.
- QUARANTINE stores blocked artifacts with reason codes.
- PROCESSED holds validated candidates.
- CATALOG/TRIPLET captures discoverability and provenance.
- PUBLISHED serves governed outputs with proofs.
