<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-remote-sensing-lineage-activity-source-map
title: Pass 32 remote-sensing lineage activity - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - observability steward; remote-sensing steward; runtime steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-PROG-0012 and connected Drive architecture material with the existing OpenLineage projection lane and the bounded companion implementation
truth_posture: CONFIRMED source statement current-repository overlap and focused local proof / PROPOSED inactive companion / UNKNOWN production instrumentation upstream interoperability and hosted exact-head proof
related: [../../../contracts/telemetry/remote_sensing_lineage_activity.md, ../../../contracts/telemetry/openlineage_run_event_projection.md, new-ideas-4-openlineage-run-event-projection-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 remote-sensing lineage activity - governed implementation source map

## Source statement

`KFM-P32-PROG-0012` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a remote-sensing OpenLineage emitter carrying scene counts, runtime, retries, failure counts, and source links, with both OpenLineage and PROV activities. The card was visually checked on physical PDF page 1001; its extracted source-card record hashes to `sha256:30cd6af0a2cfa75beeabfa62523fc28dbf8b294838a314616f2152bd1e085f1b`.

Connected Google Drive material proposes asset-first orchestration with OpenLineage and PROV. The inspected Drive sources were the consolidated atlas (`1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa`), *KFM Full Atlas seed cards* (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`), and *New Ideas* (`142-qzQIydi1Erd3FJherlxxQ9BZqkbCjV06IuuQ-THc`). These are idea and architecture sources; they do not establish repository implementation or runtime authority.

## Repository reconciliation

At inspected `main@463381703bcd6eada8eea05e95c4a88912ed4b02`, the repository already had a dependency-closed, fixture-only `OpenLineageRunEventProjection` contract, schema, generator, validator, tests, workflow, and source map. Repository, branch, pull-request, and issue searches found no implementation for the exact Pass 32 remote-sensing card.

Creating a second run receipt, generic OpenLineage schema, evidence lane, telemetry sink, or pipeline would duplicate existing authority. The smallest gap is a composed companion that revalidates the existing projection and adds only bounded remote-sensing metrics, receipt-safe source links, and a PROV-shaped relation.

## Implemented boundary

The companion is deterministic, closed-shape, fixture-only, and no-network. It binds scene totals, processed/failed counts, retries, runtime, UTC-second interval, receipt-declared source references, the existing OpenLineage projection, and a local PROV-shaped activity. It supports coherent success and recorded-failure lineage, while partial upstream state abstains and policy denial remains denial.

Scene-count mismatch, runtime mismatch, run-outcome mismatch, missing source-descriptor links, facet drift, PROV drift, embedded-projection drift, identity drift, or unexpected coordinate fields fail closed. No imagery, geometry, raw payload, source byte, credential, endpoint, exporter, signing client, registry, catalog query, or model is present.

## Directory Rules and non-effects

Meaning remains in `contracts/`; shape in `schemas/`; synthetic cases in `fixtures/`; construction and validation in `tools/`; executable proof in `tests/`; source adaptation in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`. The implementation creates no new root and grants no source, evidence, policy, review, lifecycle, promotion, release, deployment, publication, or public-use authority.

## Validation and rollback

Local proof comprises Draft 2020-12 composite-schema validation, eleven exact-polarity fixtures, deterministic identity checks, reuse of the existing OpenLineage validator, no-network/static-effect guards, workflow pin/permission tests, and generated-receipt byte binding. Hosted exact-head CI and steward adoption remain pending. Rollback is a focused revert of this additive packet; no live source, telemetry event, backend, evidence, lifecycle state, release, deployment, or public artifact is affected.
