<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/kfm-explorer-site-real-data-backfill-20260910
title: KFM Explorer Site Real-Data Backfill — 2026-09-10
type: architecture-reference
version: v1.1.0-draft
created: 2026-09-10
updated: 2026-09-24
status: draft; documentation-only; historical-source-record; not-released; not-for-life-safety
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "Site, source, evidence, hazards, release, and documentation stewardship NEEDS VERIFICATION"
policy_label: public
owning_root: docs/
responsibility: >
  Record the reconciliation between the Kansas Frontier Matrix Explorer Site
  checkpoint and the repository's existing source-role, hazards, smoke, and
  LiDAR doctrine without activating a source, contract, policy, release, or
  publication lane.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# KFM Explorer Site Real-Data Backfill — 2026-09-10

> **Status:** documentation reconciliation; historical Site capabilities and current source/platform checkpoints are separate. This edit performs no release or deployment and does not establish life-safety fitness.

This record preserves the 2026-09-10 account of bounded real-data context work in the existing Kansas Frontier Matrix Explorer Site. It is a convergence note between the Site source history and the Kansas Frontier Matrix repository. It does not copy the Site source tree into this repository and does not change source admission, contracts, schemas, policy, evidence, release, or publication state.

## Resource reconciliation — 2026-09-23 UTC

**CONFIRMED:** source inspected at
[`main@bb08d3e9b92e9251c193debab6567be843136070`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bb08d3e9b92e9251c193debab6567be843136070).
The observation falls on 2026-09-22 in America/Chicago. Repository source,
connected Site metadata, coordination records, and design proposals answer
different questions; their dates do not make them interchangeable authorities.

| Resource / feature | Reconciled status | Evidence and next boundary |
|---|---|---|
| Existing hosted Explorer | Sites reports v70, source `c402b063c60dc7ec8f23a497715d01cff6f7ffa5`, successful deployment, owner-private audience. | [Exact IDs, digest, preserved baseline v68 and prior v69 and method](../../apps/kansas-frontier-matrix-explorer/docs/sites-source-alignment.md). Browser acceptance, full source equivalence and recovery were not tested. |
| Explorer Web Living Atlas | Package-owned inline MapLibre composition exists; `maplibre-gl` is pinned to 6.9.0. The retained laboratory still uses `NullMapRuntime`. | [Consumer source boundary](../../apps/explorer-web/src/site/README.md), [package](../../packages/maplibre/package.json). External resources, source admission and release remain separate. |
| Monorepo Sites app | Vite/React with Explorer and About views; renderer-neutral `NullMapRuntime` and synthetic/generalized catalog. | [App guide](../../apps/kansas-frontier-matrix-explorer/README.md). This is not a mirror-equivalence claim about the standalone Site. |
| Local source custody | Offline local-data tools support an external private quarantine store. | [Runbook](../runbooks/local-pc-data-store.md). Capturing bytes and process receipts does not admit a source or show it on the map. |
| USGS earthquake work | Merged [#4674](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4674) contains offline request/history planning and bounded immutable candidates. | [Source](../../connectors/usgs/src/usgs/earthquake.py), [runbook](../runbooks/usgs-earthquake-live-history.md). No transport, scheduler, complete catalog, persisted release, or map integration is established. |
| Raspberry Shake | Browser-local MiniSEED/StationXML preview exists as `UNADMITTED_BROWSER_PREVIEW`; its resulting posture stays `HOLD`. | [App guide](../../apps/kansas-frontier-matrix-explorer/README.md#browser-local-waveform-preview). It is not a provider waveform service, evidence handoff or released observation. |
| Live-feed startup | [#4675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4675) merged during this review. The repository Worker returns HTTP 503 JSON `KFM_API_NOT_CONFIGURED`; diagnostic and startup-selection slices exist. | [Integration boundary](../../apps/kansas-frontier-matrix-explorer/docs/live-feed-startup.md). Selector/demo remain unmounted; no live API, supplied real snapshot, hosted repair or deployment is established. |
| Later seismic work | History-driver, local GeoJSON and workbook-preflight claims remain coordination/branch checkpoints. | [Notion backfill](https://app.notion.com/p/3d7a92021bf681a4ae8cc75930b302f2), [Drive backfill](https://docs.google.com/document/d/1uROL1Hkgr15oe2nH-9B2MUXdmzt2KSBo6ay1jt5dh4s/edit). Inspect those exact branches before treating them as main or hosted behavior; reported tests are not rerun here. |
| Hazard workspace, atlas views and Science Pack | **PROPOSED** integration/design direction, with bounded implementation slices documented separately. | [Hazard workspace](ui/firemap-inspired-hazard-workspace.md), [Living Atlas design](https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit), [Science Pack](../../README.md#a-finished-kfm-with-a-science-pack). A design list is not an installed, admitted, released product. |

### Authority, placement and source preservation

GitHub exact refs establish implementation. Notion coordinates current work and
open verification. Drive and the synced project PDFs/Markdown/DOCX retain
research, design and doctrine lineage unless expressly adopted; this update
does not rewrite those read-only synced files. The older checkpoints below
remain historical even when their original text uses “now” or “current.”

Placement follows accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../doctrine/directory-rules.md): `docs/` owns human
explanation; existing `apps/` documentation explains its application boundary;
the root README owns repository orientation. The rules' internally proposed
label is part of the adopted pinned artifact and is not edited here. No new
contract, schema, policy, source registry, proof, release or compatibility root
is created.

The security review here is documentation-boundary review, using the existing
[security policy](../../SECURITY.md), not a vulnerability scan or certification.
Preserve governed APIs/released artifacts, fail-closed evidence behavior,
source-role separation, rights and sensitivity checks, review, correction and
rollback. Neither newer prose nor a successful platform deployment clears
those controls.

## Exact checkpoints

### Historical authoring checkpoint — 2026-09-10

The v21 baseline, branch statement and validation counts below are retained
from the original authoring record. They do not describe current main, current
Site version, or validation performed by this documentation reconciliation.

| Surface | Checkpoint |
|---|---|
| Repository baseline | `bartytime4life/Kansas-Frontier-Matrix` `main@77c11c2db9c8c5b7c56e6c4335c429079cac79f2` |
| Site | [kansas-frontier-matrix-explorer](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site) |
| Site saved version | 21 |
| Site source commit | `e4cca734aa33fd7422f49b79c1ca644095900289` |
| Site deployment state | Not deployed by this change; the owner-only Site remains the current delivery surface |
| GitHub backfill state | This document is on the branch for the accompanying draft pull request |

The Site checkpoint passed `npm run build`, `npm test` (35 tests), and scoped ESLint for all changed files with zero errors. Full-project lint remains blocked by two pre-existing React effect errors in `app/observatory/workspace.tsx`; this change did not broaden that lint debt. Browser QA was not performed.

## Site capability map

Historical v21 feature account follows. These provider routes and reliability
claims were not exercised against v53 in this session and are not current
monorepo API claims.

### Smoke and atmosphere

The Site adds a bounded `noaa-hms-smoke` context feed at `/api/live-context?feed=noaa-hms-smoke`. It retrieves the daily NOAA HMS smoke KML through the Site's strict host/path allowlist, parses validated polygons, retains provider interval, density, satellite, and artifact identity, and exposes explicit partial/error outcomes. The feed is a rolling 24-hour context window; it is not an exposure, health, warning, perimeter, altitude, transport, surface-PM2.5, or all-clear product.

The implementation keeps the distinctions required by the repository's smoke seam: a smoke polygon is not a concentration observation; a satellite/analyzed product is not a surface measurement; a model is not an observation; and absence of a polygon is not evidence of no smoke or no fire.

### Raspberry Shake

The Site adds a bounded `raspberry-shake-stations` context feed at `/api/live-context?feed=raspberry-shake-stations`. It queries the Raspberry Shake FDSN station metadata service for the `AM` network inside the KFM event bounds, validates coordinates and station fields, caps the result set, and links each station to StationView.

This is the reliable first integration boundary: station identity, location, elevation, network, channel/instrument metadata when supplied, availability interval, provider identity, and StationView navigation. It does not claim a live waveform, event catalog, instrument-response-corrected amplitude, or earthquake warning. Historical FDSN data has provider latency and request limits; realtime StationView is a separate provider surface. A future waveform bridge must add response metadata, waveform parsing, time-window limits, provenance, caching, and evidence before it can be treated as a KFM observation.

### LiDAR-derived terrain

The Site now exposes LiDAR-derived terrain context through the USGS 3DEP hillshade and slope products, while keeping raw point clouds, work-unit-specific resolution, acquisition metadata, vertical datum, accuracy, and derivative lineage as explicit future gates. The current map remains at 1× terrain exaggeration and does not imply that a rendered raster is a raw LiDAR observation.

The repository's fixture-only `LidarDerivedProductLineageReceipt` remains the correct place to converge future LAZ → COPC/EPT → DEM → derivative lineage. This Site backfill does not activate that contract.

### Hazard layering and actionable-data posture

The Site preserves role separation across NWS alerts, NOAA radar, NOAA/NWM model context, USGS earthquakes, streamflow/river context, smoke footprints, Raspberry Shake station context, and terrain derivatives. Layer controls expose current bounded context and its provider service, while unavailable, partial, stale, ambiguous, denied, and error states remain visible.

The Site does not issue, interpret, confirm, rescind, or replace emergency, health, engineering, regulatory, or life-safety instructions. Synthetic hazard fixtures and historical frames remain distinguishable from provider context.

## Reliability controls

The following describes the historical Site-side design and checkpoint, not
a fresh verification of the hosted adapters.

The Site-side adapters use fixed provider allowlists, bounded geographic/time queries, response-size limits, strict parsers, caps on features/vertices/stations, finite cache windows, explicit provider/source identity, and no silent fallback from real context to synthetic data. The UI preserves the distinction between a provider's current context, a historical frame, a model output, and an unavailable source.

The public map should consume released KFM artifacts or bounded KFM APIs once the repository release lane is complete; it should not become an arbitrary upstream URL browser.

## Documentation reconciliation

The implementation was checked against these coordination and design references:

- [KFM Explorer — Living Atlas Interface, Default Views and Animation — v0.1](https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit?usp=drivesdk)
- [KFM Hourly Atmosphere Domain Builder v1.0](https://docs.google.com/document/d/16jrNLzHO94ld39NkeDFL0b6lMdn-LX6jt0iy44dKwt4/edit?usp=drivesdk)
- [KFM Baseline Geospatial Data and Tile Production Architecture](https://docs.google.com/document/d/18Yj-8arLq-m3MaUpr74cG1bIU31FazEt/edit)
- [KFM Real-Data Resource Integration — Research Manual & Delivery Hub](https://www.notion.so/3caa92021bf6816ea7f0cc902a9c9fa8)
- [KFM Living Atlas Interface and View Design](https://www.notion.so/3d2a92021bf681d68e6dfad0564d8687)
- [KFM Hazards coordination page](https://www.notion.so/3caa92021bf6811ea7f0cc902a9c9fa8)

These references are design/coordination inputs. They do not, by themselves, activate a source or prove production/publication readiness.

## Official provider references

- [NOAA HMS smoke product endpoint](https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/KML/)
- [Raspberry Shake FDSN documentation](https://manual.raspberryshake.org/fdsn.html)
- [Raspberry Shake StationView](https://stationview.raspberryshake.org/)
- [Raspberry Shake network record](https://www.fdsn.org/networks/detail/AM/)
- [USGS 3DEP products and services](https://www.usgs.gov/3d-elevation-program/about-3dep-products-services)
- [USGS 3DEP Lidar Explorer](https://apps.nationalmap.gov/lidar-explorer/)

Provider links document the source boundary; they are not an authorization to bypass KFM allowlists or release review.

## Required next gates

1. Separate smoke satellite footprints, FIRMS/hotspots, AirNow/AQS observations, model guidance, and advisories into distinct source-role contracts before any exposure or health interpretation.
2. Add a Raspberry Shake waveform/response bridge only with StationXML response handling, miniSEED validation, bounded time windows, provider limits, evidence identity, and a reviewed correction/rollback path.
3. Bind LiDAR products to exact 3DEP work-unit metadata, acquisition, native CRS/datum, units, point spacing, accuracy, nodata, processing, resampling, and derivative parameters.
4. Complete hazard lifecycle, evidence, expiry, correction, release, and rollback checks before any public or actionable claim.
5. Re-run the checks appropriate to the candidate and obtain independent review before a future merge or source/release transition; retained historical counts do not satisfy that step.

## Rollback

Revert this documentation revision if its checkpoint or interpretation is inaccurate; retain the historical authoring record. Any future correction should carry its own dated evidence. No Site deployment, provider-side mutation, authority transition or source-data migration is part of this reconciliation.
