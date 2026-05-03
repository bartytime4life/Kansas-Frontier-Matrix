# REORG Sprint Manifest

Status labels: CONFIRMED / PROPOSED / UNKNOWN / CONFLICTED / BLOCKED

- Total tracked files inventoried: **7478** (CONFIRMED via `git ls-files`).
- Target-impact status: **BLOCKED** for high-volume move pass; repo already has mature doc homes and authority conflicts remain unresolved for `contracts/` vs `schemas/` and `policy/` vs `policies`.
- Moves applied in this sprint: **0** (BLOCKED for safety).
- Reference rewrites from moves: **0** (CONFIRMED no moved paths).
- Validation/tooling edits: **CONFIRMED** (boundary-check hardening and ignore hygiene).

## Classification summary

Derived from `docs/registers/reorg/path_inventory.tsv`.

- app_api: 25
- app_web: 78
- app_worker: 7
- config: 31
- connector: 6
- data_lifecycle_catalog: 8
- data_lifecycle_processed: 9
- data_lifecycle_proof: 2
- data_lifecycle_published: 8
- data_lifecycle_quarantine: 2
- data_lifecycle_raw: 2
- data_lifecycle_receipt: 6
- data_lifecycle_triplet: 2
- data_lifecycle_work: 2
- data_registry: 17
- doc_adr: 18
- doc_architecture: 20
- doc_domain: 255
- doc_register: 20
- doc_runbook: 13
- doc_source: 33
- doc_tracking: 2
- fixture: 79
- infra: 12
- migration: 3
- package: 25
- pipeline: 76
- policy: 198
- release: 2
- root_meta: 1
- schema_contract: 970
- style: 3
- test: 3676
- tool_validator: 1083
- unknown: 784

## What not to move without ADR

- `contracts/` <-> `schemas/` machine schemas.
- `policy/` <-> `policies/` rule packs.
- lifecycle authority lanes under `data/` (`raw/work/quarantine/processed/catalog/triplets/receipts/proofs/published`).

## Artifacts

- `path_inventory.tsv`
- `move_plan.tsv`
- `reference_update_plan.tsv`
- `authority_conflicts.md`
- `validation_report.md`
- `rollback_plan.sh`
