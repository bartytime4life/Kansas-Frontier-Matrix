# REORG Sprint Manifest
Truth labels: CONFIRMED / PROPOSED / UNKNOWN / CONFLICTED / BLOCKED.

## Scope
- CONFIRMED: tracked-file inventory generated from `git ls-files`.
- CONFIRMED: reversible documentation relocation subset applied.
- CONFLICTED: schema and policy authority homes remain split and are documented.
- BLOCKED: large-scale machine-file authority moves not allowed without new ADR authorization.

## Artifacts
- `path_inventory.tsv`
- `move_plan.tsv`
- `reference_update_plan.tsv`
- `authority_conflicts.md`
- `validation_report.md`
- `rollback_plan.sh`

## What not to move without ADR
- `contracts/` <-> `schemas/` machine artifacts.
- `policy/` <-> `policies/` rego/json policy artifacts.
- `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/receipts`, `data/proofs`, `data/published` lifecycle artifacts.
