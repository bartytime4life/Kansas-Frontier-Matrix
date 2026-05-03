# Pipeline Inventory

Inventory of planned pipeline stages and validators for this lane.

## Stages
1. Source intake and descriptor gate.
2. RAW capture and fingerprinting.
3. WORK normalization and schema/geometry/time validation.
4. QUARANTINE for ambiguous/invalid/sensitive records.
5. PROCESSED outputs and catalog/prov linkage.
6. Proof pack and release promotion decision.

## Validators
- Source role and authority gate.
- Geometry/CRS and topology checks.
- Temporal overlap/conflict checks.
- Sensitivity and public-safe generalization checks.
