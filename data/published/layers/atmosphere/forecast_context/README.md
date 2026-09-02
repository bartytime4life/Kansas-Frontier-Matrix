<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/forecast-context/readme
title: data/published/layers/atmosphere/forecast_context README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): forecast-context steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/atmosphere/forecast_context/README.md
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
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Directory README for released Atmosphere forecast-context layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Forecast-context carriers must preserve issuing/source authority, forecast cycle, valid time, stale-state posture, caveats, correction path, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/forecast_context/`

> Published layer sublane for released **Atmosphere forecast-context map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: forecast context](https://img.shields.io/badge/layer-forecast--context-blue)
![Boundary: not guidance](https://img.shields.io/badge/boundary-not--guidance-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/forecast_context/README.md`  
> **Truth posture:** CONFIRMED target path, Atmosphere published README, and sibling Atmosphere layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted forecast-context layer files, schemas, validators, release manifests, forecast-cycle records, and governed routes.

> [!WARNING]
> This directory is not release authority, official forecast authority, warning authority, emergency guidance, medical guidance, regulatory determination, catalog authority, or proof authority. A forecast-context layer belongs here only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Atmosphere forecast-context layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe forecast-context map layers;
- forecast-context layer sidecars and manifests;
- public index files that point only to released forecast-context layers; and
- retired or superseded forecast-context carriers with correction or rollback references.

This lane should not contain raw source captures, direct forecast feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, official forecast issuance, warnings, emergency instructions, medical guidance, regulatory determinations, or unreleased generated outputs.

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
- [ ] source roles, issuing/source authority, model or forecast family, cycle, and valid-time range are clear;
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
data/published/layers/atmosphere/forecast_context/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-forecast-context-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
atmosphere.published.layer.forecast_context.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Atmosphere forecast-context layers are public-facing context carriers, not root truth, release authority, official forecast authority, warning authority, emergency guidance, or regulatory determinations. Keep them citable, source-role-aware, cycle-aware, valid-time-aware, stale-state-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
