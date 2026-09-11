<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/kfm-explorer-site-real-data-backfill-20260910
title: KFM Explorer Site Real-Data Backfill — 2026-09-10
type: architecture-reference
version: v1.1.0-draft
status: documentation-only; branch-updated; pr-4463-closed; not-released; not-for-life-safety
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

> **Status:** documentation-only, branch-updated, PR #4463 closed, not released, not deployed, and not for life-safety use.

This record backfills the governed real-data work completed in the existing Kansas Frontier Matrix Explorer Site. It is a convergence note between the Site source history and the Kansas Frontier Matrix repository. It does not copy the Site source tree into this repository and does not change source admission, contracts, schemas, policy, evidence, release, or publication state.

## Exact checkpoints

| Surface | Checkpoint |
|---|---|
| Repository baseline | `bartytime4life/Kansas-Frontier-Matrix` `main@47de77deb845bbba948c66566d9b88696cb14f8b` |
| Site | [kansas-frontier-matrix-explorer](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site) |
| Site saved version | 24 (current checkpoint; version 23 is the prior saved checkpoint) |
| Site source commit | `acf6499d99bd1b7c131e79b17735f95145ef808f` |
| Site deployment state | Not deployed by this change; the owner-only Site remains the current delivery surface |
| GitHub backfill state | PR #4463 is closed; this branch contains the updated documentation; no new PR was opened by this alignment |

The Site checkpoint passed `npm run build`, `npm test` (37 tests), `npx tsc --noEmit`, and scoped ESLint for all changed files with zero errors. Version 22 adds the visible priority context control deck and a clear `Controls` affordance on registry layer rows. Version 23 adds the typed feature, connection, action, code-surface, route, and cross-reference validation registries. Version 24 fixes the narrow-panel Layer Catalog layout: the catalog now owns one vertical scroll surface, the nested official-source scrollbar no longer crowds out the registry list, the Layers badge shows active/available counts, and shortcut controls target registered layers, priority earthquake/water/smoke context, and all source controls. Full-project lint remains blocked by two pre-existing React effect errors in `app/observatory/workspace.tsx`; this change did not broaden that lint debt. Browser QA was not performed.

## Site capability map

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

### Priority layer controls

Version 22 makes the previously buried controls discoverable in the first layer-panel view:

- a visible priority deck groups **Earthquakes + seismic context**, **Hydrology + water systems**, and **Smoke + weather context**;
- each group has direct per-source show/hide buttons, group-level Show all / Hide all actions, selected-source counts, loaded-feature counts, and READY/PARTIAL/HELD/UNAVAILABLE state labels;
- the existing source disclosures remain the detailed control surface for opacity, freshness, provider limits, refresh actions, and official links;
- registry layers now display an explicit **Controls** / **Hide controls** affordance so opacity, zoom, feature inspection, solo mode, and draw-order controls are not hidden behind an unlabeled title interaction.

This is a presentation and discoverability improvement only. It does not change source roles, temporal holds, admission state, evidence, release, or public alert authority.

## Site capability registry

Version 23 adds a small typed registry layer inside the Site so the visible product surface, provider connections, coding ownership, and actions can be aligned without duplicating handler logic:

- `app/site-features.ts` maps user-facing features to status, source ids, action ids, owning paths, and boundaries.
- `app/site-connections.ts` derives a normalized connection manifest from the fixed `OFFICIAL_CONTEXT_SOURCES` allowlist.
- `app/site-actions.ts` describes control modes, handler paths, inputs, outcomes, and safety boundaries.
- `app/site-architecture.ts` maps code surfaces and routes to verification paths.
- `app/site-registry.ts` validates cross-file references and exposes counts wired into the Layer Catalog.
- `docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md` records the alignment contract and held integration gates.

The registry is traceability infrastructure. It does not add an arbitrary upstream URL path, activate Raspberry Shake waveforms, activate the fixture-only LiDAR lineage contract, change KFM source admission, or authorize deployment/publication.

## Layer Catalog visibility correction

Version 24 addresses the narrow-panel failure mode shown in the Layer Catalog capture. Previously, the official operational-context card and the registry layer list competed inside nested flex/scroll containers, so the source-detail disclosure could occupy the visible area while the other layer toggles collapsed below the panel. The fix gives the catalog body one vertical scroll surface, keeps the official context card and registry groups at natural height, and adds explicit shortcuts for registered layers, priority earthquake/water/smoke context, and all source controls. The registry rows retain their direct visibility toggles plus the existing opacity, zoom, feature, solo, and draw-order controls.

This is a UI reliability and discoverability correction only. It does not change provider roles, evidence admission, hazard interpretation, source freshness, release state, or deployment state.

## Reliability controls

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
5. Re-run repository validation and independent review before merging this documentation or changing any source/release state.

## Rollback

Revert the documentation branch if the checkpoint, provider boundary, or repository baseline is found to be inaccurate. No Site deployment or provider-side mutation is part of this backfill.
