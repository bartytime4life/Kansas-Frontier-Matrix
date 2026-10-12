<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/archaeology/candidate-features/readme
title: data/published/layers/archaeology/candidate-features README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): archaeology domain steward
  - TODO(owner): map-layer steward
  - TODO(owner): cultural-review liaison
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
path: data/published/layers/archaeology/candidate-features/README.md
related:
  - ../../README.md
  - ../README.md
  - ../3d/README.md
  - ../../../archaeology/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
notes:
  - "Directory README for released public-safe Archaeology candidate-feature layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Candidate-feature carriers are not findings, source evidence, or public truth unless release and review records explicitly support that status."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/archaeology/candidate-features/`

> Published layer sublane for released, public-safe **Archaeology candidate-feature map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: archaeology](https://img.shields.io/badge/domain-archaeology-6e2a8a)
![Layer: candidate features](https://img.shields.io/badge/layer-candidate--features-blue)
![Policy: restricted review](https://img.shields.io/badge/policy-restricted--review-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/archaeology/candidate-features/README.md`  
> **Truth posture:** CONFIRMED target path, Archaeology published README, sibling 3D layer README, and Archaeology layer scaffold from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted candidate-feature layer files, schemas, validators, release manifests, review records, and governed routes.

> [!WARNING]
> This directory is not release authority and does not turn a candidate into a confirmed feature. A candidate-feature layer belongs here only after release authority, evidence support, validation, policy state, review state, correction path, and rollback support exist. If support is incomplete, keep the artifact upstream or held.

---

## 1. Scope

This lane is for released public-safe Archaeology candidate-feature layer carriers used by governed map, story, report, education, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe candidate-feature context layers;
- candidate-feature layer sidecars and manifests;
- released public index files; and
- retired or superseded candidate-feature carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, restricted material, exact sensitive detail, confirmed-site claims, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/archaeology/` | Archaeology published layer parent scaffold. |
| `data/published/layers/archaeology/3d/` | Sibling 3D layer lane. |
| `data/published/archaeology/` | Archaeology published domain carrier lane. |
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
- [ ] review state is complete for the intended audience;
- [ ] candidate status, geometry/generalization, time scope, method, and caveats are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/archaeology/candidate-features/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── archaeology-candidate-features-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
archaeology.published.layer.candidate-features.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Candidate-feature layers are high-trust public-facing carriers, not root truth and not confirmation. Keep them public-safe, reviewed, citable, release-linked, correction-ready, and reversible. If release or review support is incomplete, keep the artifact upstream or held.
