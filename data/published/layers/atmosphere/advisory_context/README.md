<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/atmosphere/advisory-context/readme
title: data/published/layers/atmosphere/advisory_context README
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
path: data/published/layers/atmosphere/advisory_context/README.md
related:
  - ../../README.md
  - ../README.md
  - ../../../atmosphere/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../../docs/domains/atmosphere/RELEASE_INDEX.md
notes:
  - "Directory README for released Atmosphere advisory-context layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Advisory-context carriers must redirect to official issuing authorities and must not replace emergency, medical, regulatory, or life-safety guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/atmosphere/advisory_context/`

> Published layer sublane for released **Atmosphere advisory-context map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Layer: advisory context](https://img.shields.io/badge/layer-advisory--context-blue)
![Boundary: not guidance](https://img.shields.io/badge/boundary-not--guidance-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/atmosphere/advisory_context/README.md`  
> **Truth posture:** CONFIRMED target path, Atmosphere published README, Atmosphere architecture doc, and Atmosphere layer scaffold from current repo evidence / PROPOSED layout and naming / NEEDS VERIFICATION for emitted advisory-context layer files, schemas, validators, release manifests, and governed routes.

> [!WARNING]
> This directory is not release authority and is not an emergency, medical, regulatory, or life-safety guidance surface. An advisory-context layer belongs here only after release authority, evidence support, validation, policy state, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Atmosphere advisory-context layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- advisory-context map layers;
- advisory-context layer sidecars and manifests;
- public index files that point only to released advisory-context layers; and
- retired or superseded advisory-context carriers with correction or rollback references.

This lane should not contain upstream lifecycle material, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, release decisions, official advisory issuance, emergency instructions, medical guidance, regulatory determinations, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/atmosphere/` | Atmosphere published layer parent scaffold. |
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
- [ ] evidence references resolve;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the public surface;
- [ ] official issuing authority, time scope, audience, method, caveats, and stale-state posture are clear;
- [ ] correction and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/atmosphere/advisory_context/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-advisory-context-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
atmosphere.published.layer.advisory_context.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

---

## Maintainer note

Atmosphere advisory-context layers are public-facing carriers, not root truth, release authority, or official guidance. Keep them citable, authority-aware, time-aware, stale-state-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream.
