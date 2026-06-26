<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/precipitation/readme
title: data/published/layers/atmosphere/precipitation README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): meteorology steward
  - TODO(owner): hydrology-context steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/atmosphere/precipitation/README.md
related:
  - ../../README.md
  - ../README.md
  - ../advisory_context/README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../aod/README.md
  - ../aqi/README.md
  - ../climate_anomaly/README.md
  - ../climate_normals/README.md
  - ../forecast_context/README.md
  - ../meteorology/README.md
  - ../observations/README.md
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Directory README for released Atmosphere precipitation layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Precipitation layer carriers must preserve source roles, observed/estimated/forecast method, accumulation window, units, valid time, freshness/stale-state posture, caveats, correction path, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/precipitation/`

> Published layer sublane for released **Atmosphere precipitation map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: precipitation](https://img.shields.io/badge/layer-precipitation-blue)
![Boundary: context only](https://img.shields.io/badge/boundary-context--only-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/precipitation/README.md`  
> **Truth posture:** CONFIRMED target path, Atmosphere published README, and sibling Atmosphere layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted precipitation layer files, schemas, validators, release manifests, accumulation/method records, and governed routes.

> [!WARNING]
> This directory is not release authority, official forecast authority, warning authority, flood guidance, emergency guidance, regulatory determination, raw observation storage, catalog authority, or proof authority. A precipitation layer belongs here only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Atmosphere precipitation layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe precipitation context map layers;
- precipitation layer sidecars and manifests;
- public index files that point only to released precipitation layers; and
- retired or superseded precipitation carriers with correction or rollback references.

This lane should not contain raw source captures, direct sensor feeds, direct radar feeds, direct forecast feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, official forecast issuance, warnings, flood guidance, emergency instructions, regulatory determinations, or unreleased generated outputs.

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
| `data/published/layers/atmosphere/climate_anomaly/` | Sibling climate-anomaly layer lane. |
| `data/published/layers/atmosphere/climate_normals/` | Sibling climate-normal layer lane. |
| `data/published/layers/atmosphere/forecast_context/` | Sibling forecast-context layer lane. |
| `data/published/layers/atmosphere/meteorology/` | Sibling meteorology layer lane. |
| `data/published/layers/atmosphere/observations/` | Sibling observation layer lane. |
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
- [ ] source roles, observed/estimated/forecast method, accumulation window, units, and valid-time range are clear;
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
data/published/layers/atmosphere/precipitation/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-precipitation-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
atmosphere.published.layer.precipitation.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Atmosphere precipitation layers are public-facing weather and hydrology-context carriers, not root truth, release authority, official forecasts, warnings, flood guidance, emergency guidance, regulatory determinations, or raw observations. Keep them citable, source-role-aware, method-aware, accumulation-window-aware, unit-aware, valid-time-aware, stale-state-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
