<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/agriculture/aggregate/readme
title: data/published/layers/agriculture/aggregate README
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
path: data/published/layers/agriculture/aggregate/README.md
related:
  - ../../README.md
  - ../README.md
  - ../../../agriculture/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/agriculture/RELEASE_INDEX.md
notes:
  - "Directory README for released aggregate Agriculture layer carriers. It replaces a placeholder file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/agriculture/aggregate/`

> Published layer sublane for released **aggregate Agriculture map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: agriculture](https://img.shields.io/badge/domain-agriculture-green)
![Layer: aggregate](https://img.shields.io/badge/layer-aggregate-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/agriculture/aggregate/README.md`  
> **Truth posture:** CONFIRMED target path and related Agriculture docs from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted layer files, schemas, validators, release manifests, and governed routes.

> [!WARNING]
> This directory is not release authority. A layer belongs here only after the release record, evidence support, validation, policy state, correction path, and rollback support exist.

---

## 1. Scope

This lane is for released aggregate Agriculture layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- aggregate map layers;
- aggregate layer sidecars;
- released layer manifests;
- released public indexes; and
- retired or superseded layer carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/agriculture/` | Agriculture published layer parent. |
| `data/published/agriculture/` | Agriculture published domain carrier lane. |
| `release/` | Release authority. |
| `contracts/` | Semantic meaning. |
| `schemas/` | Machine shape. |
| `policy/` | Admissibility rules. |

[Back to top](#top)

---

## 3. Release checks

Before adding or changing files here, verify:

- [ ] release authority exists;
- [ ] evidence references resolve;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] aggregation scope and time scope are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/agriculture/aggregate/
├── README.md
├── county/
│   └── <release_id>/
├── huc/
│   └── <release_id>/
├── grid/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── agriculture-aggregate-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
agriculture.published.layer.aggregate.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Aggregate Agriculture layers are public-facing carriers, not root truth and not release authority. Keep them citable, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
