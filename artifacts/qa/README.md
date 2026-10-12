# artifacts/qa

**Class:** compatibility / QA output scaffold.  
**Status:** PROPOSED.  
**Trust posture:** non-authoritative, replaceable, and safe to regenerate.

This directory is the local/CI landing zone for lint output, coverage exports,
structured QA surfaces, visual inspection summaries, and aggregate validator
reports. Files here may help a reviewer understand a run, but they are not
canonical records.

## Exclusions

Do not place trust-bearing material here:

- Release decisions or manifests belong in `release/`.
- Receipts belong in `data/receipts/`.
- Proofs and evidence bundles belong in `data/proofs/`.
- Published layers and public data products belong in `data/published/`.
- Source registries and source authority records belong in their governed
  registry locations.
- Secrets, credentials, private source material, and sensitive evidence do not
  belong in `artifacts/`.

## Layout

| Path | Purpose |
|---|---|
| `lint/` | Lint output by tool. |
| `coverage/` | Test coverage exports and local HTML browser output. |
| `reports/` | Structured QA surfaces for catalog, docs, accessibility, render smoke, and visual diffs. |
| `validation/` | Aggregated validator inspection copy. |
