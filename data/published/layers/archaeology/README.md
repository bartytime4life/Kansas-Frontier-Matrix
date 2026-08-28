<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/archaeology/readme
title: data/published/layers/archaeology README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): archaeology domain steward
  - TODO(owner): map-layer steward
  - TODO(owner): sensitivity reviewer
  - TODO(owner): cultural-review liaison
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
path: data/published/layers/archaeology/README.md
related:
  - ../README.md
  - ../../archaeology/README.md
  - 3d/README.md
  - candidate-features/README.md
  - chronology-views/README.md
  - public-generalized-sites/README.md
  - public-survey-coverage/README.md
  - remote-sensing-anomalies/README.md
  - ../../../../release/README.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
  - ../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
notes:
  - "Parent README for released public-safe Archaeology published layer carriers. It replaces a scaffold file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "All Archaeology published layer children are restricted-review unless release evidence proves a safer posture."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/archaeology/`

> Parent published-layer lane for released, public-safe **Archaeology map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: archaeology](https://img.shields.io/badge/domain-archaeology-6e2a8a)
![Carrier: map layers](https://img.shields.io/badge/carrier-map--layers-blue)
![Policy: restricted review](https://img.shields.io/badge/policy-restricted--review-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/archaeology/README.md`  
> **Truth posture:** CONFIRMED target path and child Archaeology layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted layer files, schemas, validators, release manifests, review records, tile builds, and governed routes.

> [!WARNING]
> This directory is not release authority. A layer belongs under this tree only after release authority, evidence support, validation, policy state, review state, correction path, rollback support, and integrity references exist. If support is incomplete, keep the artifact upstream or held.

---

## 1. Scope

This parent lane organizes released public-safe Archaeology map-layer carriers used by governed map, story, report, education, export, or UI surfaces.

This lane may reference child layer families such as:

- public-safe 3D context layers;
- candidate-feature context layers;
- chronology-view layers;
- public generalized-site layers;
- public survey-coverage layers;
- remote-sensing anomaly layers;
- released layer manifests;
- released public indexes; and
- retired or superseded layer carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, restricted material, exact sensitive detail, unreviewed claims, confirmed-site claims without release support, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Child lane index

| Child lane | Role | Status |
|---|---|---|
| [`3d/`](3d/) | Released public-safe Archaeology 3D map carriers. | Draft restricted-review directory contract. |
| [`candidate-features/`](candidate-features/) | Released public-safe candidate-feature context carriers. | Draft restricted-review directory contract. |
| [`chronology-views/`](chronology-views/) | Released public-safe chronology-view carriers. | Draft restricted-review directory contract. |
| [`public-generalized-sites/`](public-generalized-sites/) | Released public-safe generalized-site carriers. | Draft restricted-review directory contract. |
| [`public-survey-coverage/`](public-survey-coverage/) | Released public-safe survey-coverage carriers. | Draft restricted-review directory contract. |
| [`remote-sensing-anomalies/`](remote-sensing-anomalies/) | Released public-safe remote-sensing anomaly carriers. | Draft restricted-review directory contract. |

Add new child layer families only when their release purpose, evidence support, review posture, validation expectations, public-safety posture, and rollback path are clear.

[Back to top](#top)

---

## 3. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/archaeology/` | Archaeology published domain carrier lane. |
| `release/` | Release authority. |
| `contracts/` | Semantic meaning. |
| `schemas/` | Machine shape. |
| `policy/` | Admissibility rules. |

[Back to top](#top)

---

## 4. Release checks

Before adding or changing files under this parent lane, verify:

- [ ] release authority exists;
- [ ] evidence references resolve;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] review state is complete for the intended audience;
- [ ] public-safety posture, audience class, scope, method, time period, uncertainty, and caveats are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 5. Suggested layout

```text
data/published/layers/archaeology/
├── README.md
├── 3d/
│   └── README.md
├── candidate-features/
│   └── README.md
├── chronology-views/
│   └── README.md
├── public-generalized-sites/
│   └── README.md
├── public-survey-coverage/
│   └── README.md
├── remote-sensing-anomalies/
│   └── README.md
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── archaeology-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
archaeology.published.layer.<layer_family>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Published Archaeology layers are high-trust public-facing carriers, not root truth and not release authority. Keep them public-safe, reviewed, citable, release-linked, correction-ready, and reversible. If release or review support is incomplete, keep the artifact upstream or held.
