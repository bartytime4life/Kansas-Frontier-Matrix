# REORG SPRINT MANIFEST

## Truth labels
- **CONFIRMED:** inventory regenerated from `git ls-files`; 20 docs moved with `git mv`; references updated where found.
- **BLOCKED:** no machine-authority moves between `contracts/` and `schemas/`, or `policy/` and `policies/`.

## Scope
- Functional, manifest-driven docs lane normalization for domain slug consistency.
- Rebuilt reorg control artifacts under `docs/registers/reorg/`.

## Artifacts
- `path_inventory.tsv`
- `move_plan.tsv`
- `reference_update_plan.tsv`
- `authority_conflicts.md`
- `validation_report.md`
- `rollback_plan.sh`
