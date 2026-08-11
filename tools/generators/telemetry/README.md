<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-generators-telemetry-readme
title: Telemetry Projection Generators
type: README
version: v0.1.0
status: draft; bounded-executable; local-only; no-network; non-authoritative
owners:
  - TODO-observability-steward
  - TODO-tooling-steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; tools; telemetry; generator
owning_root: tools/
responsibility: construct deterministic in-memory telemetry projection candidates from explicit governed inputs without exporting telemetry mutating repository state or creating evidence policy review release publication or public-use authority
truth_posture: CONFIRMED bounded executable and focused local tests / PROPOSED inactive profile / NEEDS VERIFICATION hosted exact-head CI and future runtime admission
related:
  - ../../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../../schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json
  - ../../../fixtures/contracts/v1/telemetry/openlineage_run_event_projection/README.md
  - ../../validators/telemetry/README.md
  - ../../../tests/validators/telemetry/README.md
notes:
  - "The generator reads an explicit local fixture manifest and writes JSON to stdout only."
  - "No network, Git, repository mutation, event export, signing, release, or publication client is imported."
[/KFM_META_BLOCK_V2] -->

# `tools/generators/telemetry/` — Telemetry Projection Generators

This lane owns deterministic construction of reviewable telemetry projection candidates. It does not own telemetry transport, storage, policy, evidence, review, promotion, release, deployment, or publication.

## Current executable

| File | Purpose | Effects |
|---|---|---|
| `build_openlineage_run_event_projection.py` | Builds one fixture-only terminal OpenLineage `RunEvent`-shaped projection and derives its finite decision and deterministic identity. | Reads an explicit local manifest and writes JSON to stdout; no network or repository write. |
| `build_remote_sensing_lineage_activity.py` | Composes coherent remote-sensing scene metrics and a PROV-shaped activity with an existing governed terminal projection. | Reads an explicit local manifest and writes JSON to stdout; no source access, network, exporter, or repository write. |

The executable reuses the repository hashing package for RFC 8785 JCS plus SHA-256 identity. It references the canonical runtime `RunReceipt` object rather than inventing a telemetry receipt.

## Run

```bash
python tools/generators/telemetry/build_openlineage_run_event_projection.py \
  --case valid-internal-success-complete

python tools/generators/telemetry/build_remote_sensing_lineage_activity.py \
  --case valid-success-activity
```

## Limits

- The generator does not fetch or validate the caller-pinned upstream OpenLineage schema URI.
- It does not emit `START` events in v1.
- It does not post to a lineage backend.
- It does not sign, attest, promote, release, deploy, publish, or authorize public use.

## Rollback

Remove this lane with its dependency-closed contract, schema, fixtures, validator, tests, workflow, source map, and authoring receipt. No runtime or data migration is involved.
