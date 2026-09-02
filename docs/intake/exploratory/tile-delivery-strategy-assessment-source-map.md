<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-intake-exploratory-tile-delivery-strategy-assessment-source-map
title: Tile delivery strategy assessment - governed source map
type: exploratory-intake; implementation-source-map
version: v1.0
status: draft; triaged; noncanonical
owners: OWNER_TBD — Map steward · Release steward · Runtime steward · Validation steward
created: 2026-08-12
updated: 2026-08-12
policy_label: public; map; release; tile-delivery; fixture-only; no-network
owning_root: docs/
responsibility: reconcile supplied PMTiles, XYZ, Martin/PostGIS, and MBTiles guidance with current repository owners and bound one inactive delivery-choice assessment
truth_posture: CONFIRMED supplied-source excerpts and inspected repository gap / PROPOSED fixture-only implementation / NEEDS VERIFICATION real consumers, source terms, artifacts, services, performance, rights, sensitivity, hosting, release, deployment, and publication state
related: [../../../contracts/release/tile_delivery_strategy_assessment.md, ../../../contracts/source/map_service_protocol_assessment.md, ../../../contracts/release/tile_artifact_manifest.md, ../../../schemas/contracts/v1/release/tile_delivery_strategy_assessment.schema.json]
tags: [kfm, intake, maplibre, pmtiles, xyz, martin, postgis, mbtiles, strategy]
notes: [The complete New Ideas 5-19-26 Drive document was reviewed through the connected Google Drive representation; the locally supplied MapLibre operating manual was text-extracted and relevant pages inspected; this source map grants no network, hosting, service, database, cache, release, deployment, publication, or public-use authority.]
[/KFM_META_BLOCK_V2] -->

# Tile delivery strategy assessment — governed source map

> [!IMPORTANT]
> **Authority:** `EXPLORATORY / IMPLEMENTATION LINEAGE ONLY`
> **Implementation:** closed synthetic assessment
> **Public effect:** none

## Evidence reconciled

| Evidence | Confirmed signal | Adaptation boundary |
|---|---|---|
| Google Drive document *New Ideas 5-19-26*, document ID `1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ`, complete connector representation reviewed | PMTiles is proposed for immutable published bundles; XYZ for subset invalidation or dynamic rendering; MBTiles for local/tooling; manifests, integrity, caching, and governed publication remain separate. | Proposed cache headers, zooms, tile sizes, hosting, signatures, and client logic are not adopted here. |
| Supplied `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf`, SHA-256 `77f56ec1ab632b76c7728cfb250330271b7dc8948db95c8c0594c92ad9ca6b36`, PDF pages 3, 5, 9, and 14 | PMTiles is recommended with gates for stable public-safe immutable/rebuildable bundles and range hosting; Martin/PostGIS is situational for dynamic, access-controlled, steward-mediated, or database-backed slicing; MBTiles is server-local/offline. | The manual is architecture guidance, not measured runtime evidence, source admission, vendor selection, or release authority. |
| Current repository `main@bff35f5ddf00ef623eacf96be13a743e134f482f` | `MapServiceProtocolAssessment` owns protocol-specific source declarations; `TileArtifactManifest` owns artifact shape; PMTiles cache and verification families already exist. No exact delivery-strategy assessment was found. | Add a composition seam; do not duplicate protocol, artifact, cache, renderer, policy, or release authorities. |
| GitHub overlap check on 2026-08-12 | No pull request or active branch matched `TileDeliveryStrategyAssessment` or `tile-delivery-strategy`. | Absence is bounded to exact and semantic names inspected on the pinned base. |

## Chosen bounded slice

The implementation adds one declaration assessment that:

- derives a recommended strategy from update, audience, safety, mediation,
  invalidation, PostGIS, offline, access-control, and range-hosting facts;
- checks strategy-specific reference obligations;
- denies public unsafe input, public MBTiles, public/access-control conflict,
  and static bypass of required mediation;
- emits only `PASS`, `HOLD`, `DENY`, or `ERROR`;
- binds the full candidate to deterministic JCS identity; and
- keeps every operational and authority effect false.

## Explicit non-effects

No URL, endpoint, credential, artifact bytes, database, performance sample, or
real layer is present. The assessment does not:

- activate PMTiles, XYZ, Martin, PostGIS, MBTiles, MapLibre, a CDN, or a tile
  server;
- verify range requests, CORS, cache headers, invalidation, database queries,
  rights, sensitivity, source health, or device performance;
- generate, host, release, deploy, publish, or render tiles; or
- replace `MapServiceProtocolAssessment`, `TileArtifactManifest`, cache
  controls, renderer adapters, policy decisions, release manifests,
  correction notices, or rollback cards.

## Directory Rules basis

The assessment is release-facing because it evaluates a candidate delivery
choice after protocol and artifact responsibilities remain separately owned.
Meaning therefore belongs under `contracts/release/`, with the companion
schema, fixtures, validator, tests, workflow, source map, and generated receipt
placed in their existing responsibility roots.

## Remaining holds

Real integration requires named consumers; primary protocol/tool versions and
terms; admitted artifact/service identities; measured range, cache,
invalidation, latency, memory, and device evidence; access-control and
sensitivity policy; correction and withdrawal behavior; release review;
deployment controls; public-safe rendering; and rollback proof.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, transparently revert this additive packet and rerun focused
tests plus generated-receipt validation. No live service, artifact, database,
cache, release, deployment, or publication cleanup is required.
