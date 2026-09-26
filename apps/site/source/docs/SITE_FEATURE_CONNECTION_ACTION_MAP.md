# KFM Explorer Site Feature / Connection / Action Map

Status: active Site architecture manifest, `kfm-site-registry-v1`.

This document explains the small registry layer in `app/`. It is a traceability
surface for the existing Site; it is not a second source of truth for provider
data, KFM evidence, policy, release, or deployment.

## Registry files

| File | Responsibility | Runtime use |
|---|---|---|
| `app/site-features.ts` | User-visible product features, maturity/status, owning paths, connection ids, action ids, and boundaries | Feature inventory and alignment checks |
| `app/site-connections.ts` | Normalized view of the fixed `OFFICIAL_CONTEXT_SOURCES` allowlist | Provider/source identity, adapter paths, refresh actions, and evidence boundary |
| `app/site-actions.ts` | Visible actions and their handler paths, modes, inputs, outcomes, and safety boundaries | Action contracts for controls, reports, source handoffs, and connector work |
| `app/site-architecture.ts` | Code surfaces and route contracts | Coding ownership, verification paths, and route-level trust boundaries |
| `app/site-registry.ts` | Cross-file registry, counts, and non-throwing validation | UI summary, tests, and documentation alignment |

## Surface map

| User concern | Feature records | Connection records | Action families |
|---|---|---|---|
| Earthquakes + seismic context | `earthquake-seismic-context`, `priority-context-deck` | `usgs-earthquakes`, `raspberry-shake-stations` | toggle, refresh, opacity, provider source |
| Hydrology + water systems | `hydrology-river-pulse`, `priority-context-deck` | USGS streamflow, NWPS, 3DHP, WBD, NWM analysis, NWM short-range | range, exact observation, refresh, toggle, opacity |
| Fire + smoke + weather | `smoke-weather-context`, `date-bound-observatory`, `priority-context-deck` | NIFC WFIGS/IRWIN Kansas incident reports, NASA GIBS dated NOAA-20 selectable thermal detections and separate provider-default image, NOAA NESDIS dated GOES GeoColor imagery, HMS smoke, NWS alerts, NOAA radar | inspect working incident records, nearby thermal detections, and NOAA's visual cloud context without inferring event identity; open official news sources; check detection UTC day, select exact GeoColor image time, use radar playback, toggle, opacity |
| Airflow forecast context | `airflow-forecast-context` | NWS NDFD forecast wind barbs through the Kansas-bounded Site tile route | toggle, reload tiles, opacity, provider source; exact forecast valid time and historical wind frames are unavailable |
| LiDAR + terrain | `lidar-terrain-context`, `held-lidar-lineage` | 3DEP hillshade, 3DEP slope | toggle, opacity, provider source, intake draft |
| Reports + decisions | `evidence-drawer-and-trust`, `report-story-workspaces`, `bounded-focus-mode` | none; context remains excluded or explicitly labeled | inspect, Focus, local save, report, intake |

## Reliability contract

- The connection manifest is derived from the existing fixed official context
  allowlist. It does not add an arbitrary URL loader or silently create a new
  upstream integration.
- Every feature and connection points to owning code paths and declares a
  boundary. Missing, partial, stale, empty, and error outcomes remain states;
  they are never inferred into a positive observation or all-clear.
- Actions distinguish local UI changes, read-only connector calls, external
  navigation, and device-local drafts. No action in this manifest authorizes a
  repository mutation, provider mutation, KFM release, or public deployment.
- Earthquake, hydrology, fire reports, smoke, radar, Raspberry Shake, and LiDAR records remain
  `EXTERNAL_CONTEXT_ONLY` or held until source-role, evidence, correction,
  release, and rollback gates support a stronger claim.

## Alignment contract

| System | Authority in this alignment | What is synchronized |
|---|---|---|
| Sites | Current runtime and saved Site source | Registry files, UI wiring, tests, and saved version |
| GitHub | Repository implementation and architecture authority | Documentation-only traceability record against `main@bb08d3e9b92e9251c193debab6567be843136070` |
| Google Drive | Design/reference and handoff record | Current Site checkpoint, registry file map, validation result, and next gates |
| Notion | Coordination and knowledge capture | Current checkpoint, implementation boundaries, and follow-up ownership |

The Site source and the repository remain separately versioned. Alignment means
the boundaries, feature names, provider roles, code paths, and verification
claims are reconciled and documented; it does not copy Site source into
repository `main`, activate held integrations, merge a PR, or deploy the Site.

## Site / repository / domain checkpoint

- The active Sites project is `appgprj_6aa0b1c41bc08191bfd86003920f1631`,
  with slug `kansas-frontier-matrix-explorer` and canonical host
  `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site`.
- No custom domain was attached when checked on 2026-09-17. The canonical
  `chatgpt.site` host is the only domain currently represented here.
- The repository checkpoint inspected on 2026-09-24 is
  `bartytime4life/Kansas-Frontier-Matrix@bb08d3e9b92e9251c193debab6567be843136070` on `main`.
- Both manifests name this same Site project. The standalone manifest binds
  `DB` and `BUCKET`; the monorepo consumer has null D1/R2 bindings and a separate
  Vite/React fixture implementation. A matching project ID does not make that
  consumer safe to publish over this application.
- Both source manifests pin MapLibre `6.9.0`; identical dependency versions do
  not establish source equivalence or WebGL acceptance.
- The read-only repository check preserves the server observation timestamp,
  expires after 60 seconds and labels old observations as requiring refresh.
  Responses use `no-store` so another HTTP cache cannot extend that validity.
  A differing commit is described as different, without inferring ancestry.
- Feature-family and map-function counts are derived from their inventories.
  Repository cards retain their own dated evidence; they are not runtime metrics.

## Telemetry boundaries

| Signal | Actual producer and meaning | Verification limit |
|---|---|---|
| Renderer checks | `app/map-performance.ts` samples style, canvas and tile state; the main and snapshot map show finite failure classes instead of MapLibre exception text | No measured FPS, complete layer visibility, provider response detail or source admission implied |
| Provider state | Fixed adapters and observation timestamps | Retrieval, observation and display times remain separate; empty is not an all-clear |
| GitHub currentness | Fixed public branch metadata, one-minute validity | No synchronization, CI result, merge/release acceptance or health inference |
| Qwen context | `app/page.tsx` builds a bounded diagnostic snapshot; `app/qwen-context.ts` labels it | Model availability requires a separate endpoint/bridge check; generated text is interpretation |
| Earth Engine camera | `app/globe-context.ts` samples the map camera | No Earth Engine connection or sensor telemetry |
| Monorepo telemetry | Fixture validators and projection generators at the pinned repository | General telemetry-safety and Rego emission policies are placeholders; no collector or sink acceptance |

The executable local validation is `npm test` (build, then the complete test
inventory). `tests/repository-status.test.mjs` covers timestamp/identity rejection,
expiry, cache age, redirect cancellation and failure after expiry. Production
provider/browser acceptance is separate. Rollback is a same-Site source revert;
retain the preserved v68 recovery baseline and storage bindings.

## Held ideas intentionally scaffolded

- Raspberry Shake waveform retrieval remains a future bridge requiring bounded
  waveform windows, StationXML response metadata, miniSEED validation, caching,
  evidence identity, and correction/rollback review.
- 3DEP/LiDAR remains a derived terrain context carrier until exact work-unit
  acquisition, CRS/datum, units, spacing, accuracy, nodata, processing,
  resampling, and lineage are bound to a released contract.
- Smoke footprints remain separate from thermal anomalies, air-quality
  observations, transport models, fire perimeters, and advisories.
- Hydrology keeps gauge observations, official forecasts, modeled guidance,
  hydrography, and watershed boundaries as distinct source roles and clocks.
