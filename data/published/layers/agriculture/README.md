<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/agriculture/readme
title: data/published/layers/agriculture README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): agriculture domain steward
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/layers/agriculture/README.md
related:
  - ../README.md
  - ../../agriculture/README.md
  - aggregate/README.md
  - crop_progress_county/README.md
  - stress/README.md
  - ../../../../release/README.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
  - ../../../../docs/domains/agriculture/RELEASE_INDEX.md
notes:
  - "Parent README for released Agriculture published layer carriers. It replaces a scaffold file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/agriculture/`

> Parent published-layer lane for released **Agriculture map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: agriculture](https://img.shields.io/badge/domain-agriculture-green)
![Carrier: map layers](https://img.shields.io/badge/carrier-map--layers-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/agriculture/README.md`  
> **Truth posture:** CONFIRMED target path and child Agriculture layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted layer files, schemas, validators, release manifests, tile builds, and governed routes.

> [!WARNING]
> This directory is not release authority. A layer belongs under this tree only after the release record, evidence support, validation, policy state, correction path, and rollback support exist.

---

## 1. Scope

This parent lane organizes released Agriculture map-layer carriers used by governed map, API, report, export, or UI surfaces.

This lane may reference child layer families such as:

- aggregate Agriculture layers;
- county crop-progress layers;
- Agriculture stress layers;
- released layer manifests;
- released public indexes; and
- retired or superseded layer carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, source-level detail, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Child lane index

| Child lane | Role | Status |
|---|---|---|
| [`aggregate/`](aggregate/) | Released aggregate Agriculture map carriers. | Draft directory contract. |
| [`crop_progress_county/`](crop_progress_county/) | Released county crop-progress Agriculture map carriers. | Draft directory contract. |
| [`stress/`](stress/) | Released Agriculture stress map carriers. | Draft directory contract. |

Add new child layer families only when their release purpose, evidence support, validation expectations, and rollback posture are clear.

[Back to top](#top)

---

## 3. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/agriculture/` | Agriculture published domain carrier lane. |
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
- [ ] scope, method, time period, and source role are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 5. Suggested layout

```text
data/published/layers/agriculture/
├── README.md
├── aggregate/
│   └── README.md
├── crop_progress_county/
│   └── README.md
├── stress/
│   └── README.md
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── agriculture-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
agriculture.published.layer.<layer_family>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Published Agriculture layers are public-facing carriers, not root truth and not release authority. Keep them citable, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
