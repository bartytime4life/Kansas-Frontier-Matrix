<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/archaeology/remote-sensing-anomalies/readme
title: data/published/layers/archaeology/remote-sensing-anomalies README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): archaeology domain steward
  - TODO(owner): remote-sensing steward
  - TODO(owner): map-layer steward
  - TODO(owner): cultural-review liaison
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
path: data/published/layers/archaeology/remote-sensing-anomalies/README.md
related:
  - ../../README.md
  - ../README.md
  - ../3d/README.md
  - ../candidate-features/README.md
  - ../chronology-views/README.md
  - ../public-generalized-sites/README.md
  - ../public-survey-coverage/README.md
  - ../../../archaeology/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
notes:
  - "Directory README for released public-safe Archaeology remote-sensing-anomaly layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Remote-sensing anomaly carriers are not findings, site confirmations, source evidence, or public truth unless release and review records explicitly support that status."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/archaeology/remote-sensing-anomalies/`

> Published layer sublane for released, public-safe **Archaeology remote-sensing-anomaly map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: archaeology](https://img.shields.io/badge/domain-archaeology-6e2a8a)
![Layer: remote sensing anomalies](https://img.shields.io/badge/layer-remote--sensing--anomalies-blue)
![Policy: restricted review](https://img.shields.io/badge/policy-restricted--review-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/archaeology/remote-sensing-anomalies/README.md`  
> **Truth posture:** CONFIRMED target path, Archaeology published README, and sibling Archaeology layer README files from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted anomaly layer files, schemas, validators, release manifests, review records, and governed routes.

> [!WARNING]
> This directory is not release authority and does not turn an anomaly into a confirmed feature or site. A remote-sensing-anomaly layer belongs here only after release authority, evidence support, validation, policy state, review state, correction path, rollback support, and integrity references exist. If support is incomplete, keep the artifact upstream or held.

---

## 1. Scope

This lane is for released public-safe Archaeology remote-sensing-anomaly layer carriers used by governed map, story, report, education, or UI surfaces.

Examples of valid carrier families, once released:

- public-safe anomaly context layers;
- anomaly layer sidecars and manifests;
- released public index files; and
- retired or superseded anomaly carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, restricted material, exact sensitive detail, unreviewed anomaly claims, confirmed-site claims, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/archaeology/` | Archaeology published layer parent scaffold. |
| `data/published/layers/archaeology/3d/` | Sibling 3D layer lane. |
| `data/published/layers/archaeology/candidate-features/` | Sibling candidate-feature layer lane. |
| `data/published/layers/archaeology/chronology-views/` | Sibling chronology-view layer lane. |
| `data/published/layers/archaeology/public-generalized-sites/` | Sibling generalized-site layer lane. |
| `data/published/layers/archaeology/public-survey-coverage/` | Sibling survey-coverage layer lane. |
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
- [ ] anomaly status, source sensor/context, geometry/generalization, time scope, method, uncertainty, and caveats are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/archaeology/remote-sensing-anomalies/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── archaeology-remote-sensing-anomalies-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
archaeology.published.layer.remote-sensing-anomalies.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Remote-sensing anomaly layers are high-trust public-facing carriers, not root truth and not confirmation. Keep them public-safe, reviewed, citable, uncertainty-aware, release-linked, correction-ready, and reversible. If release or review support is incomplete, keep the artifact upstream or held.
