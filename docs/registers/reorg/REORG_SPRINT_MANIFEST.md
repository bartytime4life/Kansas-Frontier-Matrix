# REORG Sprint Manifest

## Scope
- CONFIRMED full tracked-file inventory and family classification from `git ls-files`.
- CONFIRMED applied reversible hydrology domain documentation consolidation.
- CONFIRMED generated move/reference/authority/validation/rollback artifacts.

## Applied subset
- `docs/domains/hydrology/*` reorganized into `architecture/`, `registers/`, and `tracking/` homes.
- References rewritten in hydrology README and register indexes.

## Authority-sensitive boundaries
- Do not move machine schema files between `contracts/` and `schemas/` without ADR-authorized migration.
- Do not move policy code between `policy/` and `policies/` without ADR-authorized migration.
- Do not move lifecycle artifacts (`data/raw`, `work`, `quarantine`, `processed`, `catalog`, `triplets`, `published`, `receipts`, `proofs`) in this sprint.
