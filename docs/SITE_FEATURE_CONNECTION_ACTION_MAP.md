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
| Smoke + weather | `smoke-weather-context`, `date-bound-observatory`, `priority-context-deck` | HMS smoke, NWS alerts, NOAA radar | exact frame, radar manifest refresh/playback, toggle, opacity |
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
- Earthquake, hydrology, smoke, radar, Raspberry Shake, and LiDAR records remain
  `EXTERNAL_CONTEXT_ONLY` or held until source-role, evidence, correction,
  release, and rollback gates support a stronger claim.

## Alignment contract

| System | Authority in this alignment | What is synchronized |
|---|---|---|
| Sites | Current runtime and saved Site source | Registry files, UI wiring, tests, and saved version |
| GitHub | Repository implementation and architecture authority | Documentation-only traceability record against `main@b44494c` after PR #4468 |
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
- No custom domain was attached when checked on 2026-09-11. The canonical
  `chatgpt.site` host is the only domain currently represented here.
- The current independently read repository checkpoint is
  `bartytime4life/Kansas-Frontier-Matrix@b44494c` on `main`, merged by PR #4468.
- The Site checkout’s `.openai/hosting.json` is authoritative for this Site.
  The repository child manifest still points at legacy project
  `appgprj_6a870a079c1c8191abb7401ef092a181`; that mismatch is surfaced as
  identity drift, not silently reconciled or used for deployment.

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
