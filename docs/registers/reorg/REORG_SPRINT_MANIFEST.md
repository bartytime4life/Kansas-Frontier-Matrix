# REORG Sprint Manifest

## Scope
- Deep functional manifest-driven organization sprint focused on doc-domain slug normalization and inventory tooling.

## Truth labels
- **CONFIRMED**: tracked inventory generated from `git ls-files`; domain docs moved via `git mv`; reference rewrites applied.
- **CONFLICTED**: schema and policy authority split remains open but documented by ADRs/maps.
- **BLOCKED**: no machine-authority moves attempted due to ADR constraints.

## Applied subset
- Normalized domain doc folder `docs/domains/atmosphere-air/` -> `docs/domains/atmosphere_air/`.
- Rewrote references to new path across docs/tests/register artifacts.
- Added repo inventory tooling and manifest checker.

## Artifacts
- `path_inventory.tsv`, `move_plan.tsv`, `reference_update_plan.tsv`, `authority_conflicts.md`, `validation_report.md`, `rollback_plan.sh`.
