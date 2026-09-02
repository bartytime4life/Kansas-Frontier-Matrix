<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/readme
title: data/published/layers/atmosphere README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/atmosphere/README.md
related:
  - ../README.md
  - ../../atmosphere/README.md
  - advisory_context/README.md
  - air_observations/README.md
  - air_stations/README.md
  - aod/README.md
  - aqi/README.md
  - climate_anomaly/README.md
  - climate_normals/README.md
  - forecast_context/README.md
  - meteorology/README.md
  - observations/README.md
  - ozone/README.md
  - pm25/README.md
  - pm25_2026.pmtiles/README.md
  - precipitation/README.md
  - smoke_context/README.md
  - temperature/README.md
  - weather_observations/README.md
  - weather_stations/README.md
  - wind_field/README.md
  - ../../../../release/README.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
  - ../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Parent README for released Atmosphere map-layer lanes. It replaces a scaffold file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Child layer lanes must preserve source roles, method, time scope, freshness/stale state, caveats, correction path, rollback support, and integrity references."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/`

> Parent lane for released **Atmosphere public map-layer carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Surface: map layers](https://img.shields.io/badge/surface-map--layers-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/README.md`  
> **Truth posture:** CONFIRMED target path, published Atmosphere carrier lane, and child Atmosphere layer README files from current repo evidence / PROPOSED parent index and lane grouping / NEEDS VERIFICATION for emitted layer files, release manifests, schemas, validators, EvidenceBundle references, and governed map/API routes.

> [!WARNING]
> This directory is not release authority, source registry authority, catalog authority, proof authority, policy authority, schema authority, or official issuing authority. A child layer belongs under this path only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this parent layer lane is for. |
| [2. Child layer index](#2-child-layer-index) | Current Atmosphere layer sublanes. |
| [3. Repo fit](#3-repo-fit) | Boundary with release, contracts, schemas, policy, and published domain carriers. |
| [4. Release checks](#4-release-checks) | Minimum gates before files are treated as usable. |
| [5. Suggested parent layout](#5-suggested-parent-layout) | Proposed organization and naming. |
| [6. Maintainer checklist](#6-maintainer-checklist) | Review steps for future layer additions. |

---

## 1. Scope

`data/published/layers/atmosphere/` is the published map-layer parent lane for Atmosphere carriers. It is for released, public-safe air, weather, climate-context, advisory-context, and related Atmosphere layer outputs that are safe for governed map, API, report, export, or UI consumption.

This lane may index and organize released layer families such as:

- air-quality and pollutant context layers;
- station and observation context layers;
- weather, forecast-context, precipitation, temperature, and wind-field layers;
- climate-normal and climate-anomaly context layers;
- smoke, AOD, advisory, and remote-sensing context layers;
- release-scoped package carriers such as PMTiles; and
- retired, superseded, withdrawn, or corrected layer carriers with rollback references.

This lane should not contain raw source captures, direct feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Child layer index

| Sublane | Layer family | Primary release questions |
|---|---|---|
| [`advisory_context/`](advisory_context/) | Advisory context | Is official-authority boundary clear? Are redirects, time scope, caveats, and stale state preserved? |
| [`air_observations/`](air_observations/) | Air observations | Are observation method, source roles, time range, and official-monitoring boundary clear? |
| [`air_stations/`](air_stations/) | Air stations | Are station identity scope, source roles, and station metadata scope clear? |
| [`aod/`](aod/) | Aerosol optical depth | Are remote-sensing source family, method, resolution/generalization, and caveats clear? |
| [`aqi/`](aqi/) | AQI context | Are method, pollutant basis, observation inputs, stale state, and official-authority boundary clear? |
| [`climate_anomaly/`](climate_anomaly/) | Climate anomaly | Are baseline/reference period, anomaly metric, method, uncertainty, and caveats clear? |
| [`climate_normals/`](climate_normals/) | Climate normals | Are normal/reference period, metric family, method, uncertainty, and caveats clear? |
| [`forecast_context/`](forecast_context/) | Forecast context | Are source authority, model/forecast family, cycle, valid-time range, caveats, and stale state clear? |
| [`meteorology/`](meteorology/) | General meteorology | Are observed/derived method, metric family, valid time, and official-authority boundary clear? |
| [`observations/`](observations/) | General observations | Are observation method, metric family, time scope, and source roles clear? |
| [`ozone/`](ozone/) | Ozone | Are pollutant basis, method, time range, caveats, and official-authority boundary clear? |
| [`pm25/`](pm25/) | PM2.5 | Are pollutant basis, averaging period, method, time range, and caveats clear? |
| [`pm25_2026.pmtiles/`](pm25_2026.pmtiles/) | PM2.5 PMTiles package | Are PMTiles metadata, checksums, manifest, release link, and rollback support present? |
| [`precipitation/`](precipitation/) | Precipitation | Are accumulation window, units, method, valid-time range, and caveats clear? |
| [`smoke_context/`](smoke_context/) | Smoke context | Are smoke/plume method, confidence posture, PM2.5/AQI caveats, time scope, and authority boundary clear? |
| [`temperature/`](temperature/) | Temperature | Are metric family, units, method, valid-time range, and stale-state posture clear? |
| [`weather_observations/`](weather_observations/) | Weather observations | Are metric family, units, observation method, observation time range, and source roles clear? |
| [`weather_stations/`](weather_stations/) | Weather stations | Are station identity scope, metadata scope, source roles, and freshness state clear? |
| [`wind_field/`](wind_field/) | Wind field | Are vector semantics, units, vertical level, height reference, method, and valid time clear? |

[Back to top](#top)

---

## 3. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| [`../`](../) | Published map-layer parent. | This Atmosphere lane is one domain-specific child. |
| [`../../atmosphere/`](../../atmosphere/) | Published Atmosphere domain carriers. | Broader published domain lane; this path is map-layer-specific. |
| [`../../api_payloads/atmosphere/`](../../api_payloads/atmosphere/) | Released API-shaped carriers. | API payload carriers may point to layer releases, but do not define layer authority. |
| [`../../../../release/`](../../../../release/) | Release decisions, manifests, correction, withdrawal, rollback, signatures. | Release authority lives here. |
| [`../../../../contracts/`](../../../../contracts/) | Semantic meaning. | Layers conform to contracts; they do not define them. |
| [`../../../../schemas/`](../../../../schemas/) | Machine shape. | Layers validate against schemas; schemas live elsewhere. |
| [`../../../../policy/`](../../../../policy/) | Admissibility rules. | Layers carry policy outcome references; policy rules live elsewhere. |
| `data/catalog/` | Catalog and source-discovery records. | Catalog records support discovery and lineage; they do not publish. |
| `data/proofs/` | Evidence, proof packs, validation reports. | Proof support backs release; it is not itself the public layer carrier. |
| `data/receipts/` | Process memory and receipts. | Receipts show what ran; they do not authorize publication. |

[Back to top](#top)

---

## 4. Release checks

Before adding or changing any child layer carrier, verify:

- [ ] release authority exists;
- [ ] EvidenceBundle references resolve;
- [ ] source roles and source family are clear;
- [ ] method, metric family, units, time scope, and spatial scope are clear;
- [ ] freshness/stale-state posture is explicit;
- [ ] caveats, audience, and official-authority boundaries are explicit;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] integrity references bind the layer to the release record;
- [ ] correction, supersession, withdrawal, and rollback paths are recorded; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 5. Suggested parent layout

```text
data/published/layers/atmosphere/
├── README.md
├── advisory_context/
├── air_observations/
├── air_stations/
├── aod/
├── aqi/
├── climate_anomaly/
├── climate_normals/
├── forecast_context/
├── meteorology/
├── observations/
├── ozone/
├── pm25/
├── pm25_2026.pmtiles/
├── precipitation/
├── smoke_context/
├── temperature/
├── weather_observations/
├── weather_stations/
└── wind_field/
```

Suggested deterministic parent index name, if emitted later:

```text
atmosphere.published.layers.index.<release_id>.<short_hash>.json
```

Suggested child carrier naming pattern:

```text
atmosphere.published.layer.<layer_slug>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 6. Maintainer checklist

When adding a new Atmosphere layer sublane:

- [ ] confirm this parent README is the correct published-layer home;
- [ ] create or update the child `README.md` with `KFM_META_BLOCK_V2`;
- [ ] keep schemas under `schemas/`, contracts under `contracts/`, and policy under `policy/`;
- [ ] keep release decisions under `release/`;
- [ ] keep evidence, proof, validation, and receipt material in their respective lifecycle roots;
- [ ] mark proposed layouts as PROPOSED until validated by tooling;
- [ ] keep public clients on governed interfaces or approved released-artifact paths; and
- [ ] record correction and rollback paths before treating a layer as usable.

[Back to top](#top)

---

## Maintainer note

Atmosphere layer files are public-facing carriers, not root truth and not release authority. Keep every layer citable, source-role-aware, method-aware, time-aware, stale-state-aware, caveated, release-linked, integrity-bound, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream instead of treating this path as published output.
