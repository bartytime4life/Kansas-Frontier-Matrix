<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/weather-observations/readme
title: data/published/layers/atmosphere/weather_observations README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): meteorology steward
  - TODO(owner): observations steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/atmosphere/weather_observations/README.md
related:
  - ../../README.md
  - ../README.md
  - ../advisory_context/README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../aod/README.md
  - ../aqi/README.md
  - ../forecast_context/README.md
  - ../meteorology/README.md
  - ../observations/README.md
  - ../precipitation/README.md
  - ../temperature/README.md
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Directory README for released Atmosphere weather-observation layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Weather-observation carriers must preserve source roles, observation method, metric family, observation time, freshness/stale-state posture, caveats, correction path, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/weather_observations/`

> Published layer sublane for released **Atmosphere weather-observation map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: weather observations](https://img.shields.io/badge/layer-weather--observations-blue)
![Boundary: context only](https://img.shields.io/badge/boundary-context--only-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/weather_observations/README.md`  
> **Truth posture:** CONFIRMED target path, Atmosphere published README, and sibling Atmosphere layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted weather-observation layer files, schemas, validators, release manifests, observation method records, and governed routes.

> [!WARNING]
> This directory is not release authority, raw observation storage, direct sensor-feed access, station/source registry authority, catalog authority, proof authority, or official monitoring authority. A weather-observation layer belongs here only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Atmosphere weather-observation layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe weather-observation context map layers;
- weather-observation layer sidecars and manifests;
- public index files that point only to released weather-observation layers; and
- retired or superseded weather-observation carriers with correction or rollback references.

This lane should not contain raw source captures, direct sensor feeds, direct station registries, direct forecast feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, official monitoring determinations, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/atmosphere/` | Atmosphere published layer parent scaffold. |
| `data/published/layers/atmosphere/advisory_context/` | Sibling advisory-context layer lane. |
| `data/published/layers/atmosphere/air_observations/` | Sibling air-observation layer lane. |
| `data/published/layers/atmosphere/air_stations/` | Sibling air-station layer lane. |
| `data/published/layers/atmosphere/aod/` | Sibling AOD layer lane. |
| `data/published/layers/atmosphere/aqi/` | Sibling AQI layer lane. |
| `data/published/layers/atmosphere/forecast_context/` | Sibling forecast-context layer lane. |
| `data/published/layers/atmosphere/meteorology/` | Sibling meteorology layer lane. |
| `data/published/layers/atmosphere/observations/` | Sibling observation layer lane. |
| `data/published/layers/atmosphere/precipitation/` | Sibling precipitation layer lane. |
| `data/published/layers/atmosphere/temperature/` | Sibling temperature layer lane. |
| `data/published/atmosphere/` | Atmosphere published domain carrier lane. |
| `release/` | Release authority. |
| `contracts/` | Semantic meaning. |
| `schemas/` | Machine shape. |
| `policy/` | Admissibility rules. |

[Back to top](#top)

---

## 3. Release checks

Before adding or changing files here, verify:

- [ ] release authority exists;
- [ ] EvidenceBundle references resolve;
- [ ] source roles, observation method, metric family, units, and observation time range are clear;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] time scope, freshness/stale-state posture, caveats, audience, and official-authority boundary are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/atmosphere/weather_observations/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-weather-observations-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
atmosphere.published.layer.weather_observations.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Atmosphere weather-observation layers are public-facing context carriers, not root truth, release authority, raw observations, direct source access, official monitoring determinations, or forecast authority. Keep them citable, source-role-aware, method-aware, metric-aware, unit-aware, time-aware, stale-state-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
