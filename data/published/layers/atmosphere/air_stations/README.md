<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/air-stations/readme
title: data/published/layers/atmosphere/air_stations README
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
path: data/published/layers/atmosphere/air_stations/README.md
related:
  - ../../README.md
  - ../README.md
  - ../advisory_context/README.md
  - ../air_observations/README.md
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Directory README for released Atmosphere air-station layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Air-station layer carriers must preserve station identity scope, source roles, freshness/stale state, caveats, correction path, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/air_stations/`

> Published layer sublane for released **Atmosphere air-station map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: air stations](https://img.shields.io/badge/layer-air--stations-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/air_stations/README.md`  
> **Truth posture:** CONFIRMED target path, Atmosphere published README, and sibling Atmosphere layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted air-station layer files, schemas, validators, release manifests, station identity records, and governed routes.

> [!WARNING]
> This directory is not release authority, source registry authority, station identity authority, raw sensor-feed authority, or official-monitoring authority. An air-station layer belongs here only after release authority, EvidenceBundle support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Atmosphere air-station layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe air-station map layers;
- station-summary layer sidecars and manifests;
- public index files that point only to released air-station layers; and
- retired or superseded air-station carriers with correction or rollback references.

This lane should not contain raw source captures, direct sensor feeds, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, official monitoring determinations, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/atmosphere/` | Atmosphere published layer parent scaffold. |
| `data/published/layers/atmosphere/advisory_context/` | Sibling advisory-context layer lane. |
| `data/published/layers/atmosphere/air_observations/` | Sibling air-observation layer lane. |
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
- [ ] station identity scope and source roles are clear;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] time scope, freshness/stale state, caveats, and audience are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/atmosphere/air_stations/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-air-stations-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
atmosphere.published.layer.air_stations.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Atmosphere air-station layers are public-facing carriers, not root truth, release authority, source registry authority, raw observations, or official monitoring determinations. Keep them citable, source-role-aware, identity-aware, time-aware, stale-state-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
