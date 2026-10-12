<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/agriculture/stress/readme
title: data/published/layers/agriculture/stress README
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
path: data/published/layers/agriculture/stress/README.md
related:
  - ../../README.md
  - ../README.md
  - ../../../agriculture/README.md
  - ../aggregate/README.md
  - ../crop_progress_county/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/agriculture/RELEASE_INDEX.md
notes:
  - "Directory README for released Agriculture stress layer carriers. It replaces a placeholder file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/agriculture/stress/`

> Published layer sublane for released **Agriculture stress map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: agriculture](https://img.shields.io/badge/domain-agriculture-green)
![Layer: stress](https://img.shields.io/badge/layer-stress-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/agriculture/stress/README.md`  
> **Truth posture:** CONFIRMED target path and related Agriculture layer docs from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted stress layer files, schemas, validators, release manifests, and governed routes.

> [!WARNING]
> This directory is not release authority. A stress layer belongs here only after the release record, evidence support, validation, policy state, correction path, and rollback support exist.

---

## 1. Scope

This lane is for released Agriculture stress layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- stress-context map layers;
- stress layer sidecars;
- released layer manifests;
- released public indexes; and
- retired or superseded layer carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, source-level detail, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/agriculture/` | Agriculture published layer parent. |
| `data/published/layers/agriculture/aggregate/` | Sibling aggregate layer lane. |
| `data/published/layers/agriculture/crop_progress_county/` | Sibling county crop-progress layer lane. |
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
- [ ] stress metric, crop scope, geometry scope, time scope, and method are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/agriculture/stress/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── agriculture-stress-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
agriculture.published.layer.stress.<stress_metric>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Agriculture stress layers are public-facing carriers, not root truth and not release authority. Keep them citable, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
